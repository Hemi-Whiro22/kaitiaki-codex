# IVFFlat Index Deep Dive

## What is IVFFlat?

**IVFFlat** = **Inverted File Flat**. It's a PostgreSQL indexing strategy for **approximate nearest neighbor (ANN) search** on high-dimensional vectors. In our case, finding semantically similar packs based on their 384-dimensional embeddings.

---

## Without Index (Brute Force)

```sql
-- Every query scans ALL rows and calculates distance
select * from packs
order by embedding <=> query_vector
limit 5;
```

**Problem**: With 1M packs, you calculate 1M cosine distances. This is **O(n)** — slow.

---

## With IVFFlat Index

```sql
create index idx_packs_embedding on packs
  using ivfflat (embedding vector_cosine_ops) with (lists = 10);
```

### How it Works (High Level)

1. **Training Phase (Index Creation)**

   - PostgreSQL trains a k-means clustering algorithm on your vectors
   - Divides the 384-dim space into `lists=10` clusters (regions/centroids)
   - Each cluster is like a "neighborhood" of similar vectors

2. **Insertion / Indexing**

   - New embeddings are assigned to their nearest cluster centroid
   - Stored in an **inverted file** (like a hash table): `cluster_id → list of vectors`

3. **Query Time (Search Phase)**
   ```
   a. User searches for "travel pack"
   b. Generate embedding for query: [0.1, 0.5, -0.2, ...]
   c. Find the K nearest cluster centroids to query
   d. Only search vectors in those clusters (not all 1M)
   e. Return top-5 most similar
   ```

### Example with `lists=10`

If you have 100,000 packs:

- **Without index**: check all 100k vectors → 100k cosine distance calculations
- **With IVFFlat (lists=10)**:
  - Find 2-3 nearest clusters (maybe 30k vectors)
  - Check only those 30k → ~70% faster

Trade-off: **approximate** (may miss a few very distant matches) vs **fast**.

---

## Our Configuration

```sql
create index idx_packs_embedding on public.packs
  using ivfflat (embedding vector_cosine_ops) with (lists = 10);
```

### Parameters Explained

- **`vector_cosine_ops`**: Use cosine distance (0-2 range, where 0 = identical, 2 = opposite)

  - Other options: `vector_l2_ops` (Euclidean), `vector_ip_ops` (inner product)
  - Cosine is best for semantic similarity (text/embeddings)

- **`lists = 10`**: Create 10 clusters
  - Too low (2-3): coarse regions, miss good matches
  - Too high (100+): build time ↑, space ↑, diminishing speed gains
  - **10 is a good default** for ~1k-100k vectors

---

## Query Execution

Our search function uses **cosine distance operator** (`<=>`) to find similar embeddings:

```sql
create or replace function match_packs_by_embedding(
  query_embedding vector(384),
  match_threshold float default 0.5,    -- Similarity must be > 50%
  match_count int default 5             -- Return top 5
) returns table (
  id uuid,
  name text,
  description text,
  similarity float
) language sql stable as $$
  select
    packs.id,
    packs.name,
    packs.description,
    1 - (packs.embedding <=> query_embedding) as similarity  -- Convert distance to similarity (0-1)
  from packs
  where packs.embedding is not null
    and 1 - (packs.embedding <=> query_embedding) > match_threshold
  order by packs.embedding <=> query_embedding
  limit match_count;
$$;
```

**Step-by-step**:

1. `packs.embedding <=> query_embedding` → **cosine distance** (0 = identical, 2 = opposite)
2. `1 - (distance)` → **similarity score** (1 = perfect match, -1 = opposite)
3. Filter: `similarity > 0.5` (only packs >50% similar)
4. Order by distance (nearest first)
5. Limit to 5 results

---

## Performance Impact

### Scenario: 50,000 packs

**Without index (full scan)**:

- Every query: 50,000 cosine calculations
- ~2-5 seconds per search

**With IVFFlat (lists=10)**:

- Scan ~5,000 vectors in relevant clusters
- ~200-500ms per search
- **5-10x faster** 🚀

### Build Time

- Index creation: ~1-2 seconds for 50k vectors (one-time cost)
- RAM usage: minimal (~few MB)
- Storage overhead: ~5-10% increase

---

## When to Tune `lists`

| Dataset Size | Suggested `lists` | Reason                                |
| ------------ | ----------------- | ------------------------------------- |
| <1,000       | 5                 | Tiny dataset, full scans often faster |
| 1k-10k       | 10 (default)      | Good balance                          |
| 10k-100k     | 20-30             | More clusters = finer search          |
| 100k-1M      | 50-100            | Very large; finer granularity helps   |
| 1M+          | 100-500           | Huge dataset; many clusters           |

---

## Advanced: Probing

PostgreSQL also supports **probing** — searching multiple nearest clusters:

```sql
set ivfflat.probes = 5;  -- Search top 5 clusters instead of default 1
```

- Default: probes=1 (fastest but least accurate)
- Higher probes = more thorough search, slower
- Trade-off: accuracy vs speed

---

## Visual Example

```
Embedding Space (simplified 2D for visualization):

WITHOUT INDEX:
┌─────────────────────────────┐
│ ●●●●●●●●●●●●●●●●●●●●●●●●● │  <- 100 vectors, search all
│ ●●●●●QUERY●●●●●●●●●●●●●●● ▢ │
│ ●●●●●●●●●●●●●●●●●●●●●●●●● │
└─────────────────────────────┘
Time: O(n) — scan every vector


WITH IVFFLAT (lists=4):
┌─────────────────────────────┐
│  Cluster 1  │   Cluster 2   │
│  ● ● ●     │   ● ● ● ●    │
│  ● ●QUERY ▢│   ● ● ● ●    │  <- Only search Cluster 2 (nearest to query)
├─────────────┼──────────────┤
│  Cluster 3  │   Cluster 4   │
│  ● ● ●     │   ● ● ● ●    │
│  ● ● ●     │   ● ● ● ●    │
└─────────────────────────────┘
Time: O(n/k) — scan 1/4 of vectors
```

---

## Our Use Case

For **pack-dashboard**:

- Hash-based embeddings (384-dim deterministic vectors)
- Small dataset initially (maybe 100s-1000s of packs)
- **IVFFlat with lists=10 is perfect**: fast, simple, scales to 100k+

As you grow:

- 10k packs: keep lists=10, still fast
- 100k+ packs: increase to lists=30-50 for better clustering

---

## Summary

| Aspect          | Details                                                                     |
| --------------- | --------------------------------------------------------------------------- |
| **What**        | IVFFlat partitions vector space into clusters for fast ANN search           |
| **Why**         | Cosine distance between 384-dim vectors is expensive; indexing speeds it up |
| **How**         | k-means clustering + inverted file lookups                                  |
| **Performance** | 5-10x faster than full table scans on large datasets                        |
| **Trade-off**   | Approximate (may miss outliers) vs exact (slow)                             |
| **Our config**  | 10 clusters; good for up to 100k vectors                                    |
| **Tuning**      | Increase `lists` as dataset grows                                           |

This is what makes semantic search **production-ready** on PostgreSQL! 🎯
