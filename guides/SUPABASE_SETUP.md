# Supabase + pgvector Setup Guide

## Does Supabase Support pgvector?

**Yes!** Supabase (built on PostgreSQL) fully supports the `pgvector` extension. All Supabase projects can enable it.

---

## How to Enable pgvector on Your Supabase Project

### Option 1: Via Supabase Dashboard (Easiest)

1. Go to your Supabase project → **SQL Editor**
2. Click **"New Query"**
3. Paste and run:
   ```sql
   create extension if not exists vector;
   ```
4. You'll see: `Success. No rows returned.`

### Option 2: Via Supabase CLI

If you're using the CLI:

```bash
supabase db execute "create extension if not exists vector;"
```

---

## Apply Our Full Schema to Supabase

Now run the complete schema from `supabase/schema.sql`:

```sql
-- Enable pgcrypto for gen_random_uuid
create extension if not exists pgcrypto;

-- Enable pgvector for embeddings (deterministic hash-based)
create extension if not exists vector;

-- Packs table with RLS
create table if not exists public.packs (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  description text,
  embedding vector(384),
  metadata jsonb default '{}',
  created_at timestamptz not null default now()
);

-- Enable RLS and simple read-all, insert-all policy for anon (adjust for real apps)
alter table public.packs enable row level security;

create policy if not exists "packs_read" on public.packs
  for select using (true);

create policy if not exists "packs_insert" on public.packs
  for insert with check (true);

-- IVFFlat index for fast approximate nearest neighbor search
create index if not exists idx_packs_embedding on public.packs
  using ivfflat (embedding vector_cosine_ops) with (lists = 10);

-- Vector similarity search function (using cosine distance)
create or replace function match_packs_by_embedding(
  query_embedding vector(384),
  match_threshold float default 0.5,
  match_count int default 5
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
    1 - (packs.embedding <=> query_embedding) as similarity
  from packs
  where packs.embedding is not null
    and 1 - (packs.embedding <=> query_embedding) > match_threshold
  order by packs.embedding <=> query_embedding
  limit match_count;
$$;

-- Seed data
insert into public.packs (name, description, embedding, metadata) values
  ('Starter Pack', 'Essential items to get going', '[0.1, 0.2, -0.3, ...]', '{"category": "beginner"}'),
  ('Dev Pack', 'Local dev tools and configs', '[0.15, 0.25, -0.25, ...]', '{"category": "developer"}'),
  ('Travel Pack', 'Things to bring on trips', '[0.05, 0.1, -0.4, ...]', '{"category": "travel"}');
```

---

## Supabase Limitations & Notes

### ✅ Works Out of the Box

- pgvector extension
- `vector(384)` data type
- Cosine/L2/IP distance operators (`<=>`, `<->`, `<#>`)
- IVFFlat indexes
- RPC functions (for our `match_packs_by_embedding()`)

### ⚠️ Important Considerations

1. **Anon Key RLS**: Our schema allows `anon` users to read/insert packs

   - **For production**: tighten RLS policies (require auth, user_id, etc.)
   - See `supabase/schema.sql` for `with check (true)` — this is permissive for demo

2. **Vector Size**: We use `vector(384)`

   - Hash-based embeddings are always 384-dim
   - If you switch to OpenAI embeddings later, use `vector(1536)`
   - Supabase supports any dimension

3. **Index Performance**: IVFFlat with `lists=10` is good up to ~100k vectors

   - Beyond that: increase `lists` parameter or use HNSW (if available)

4. **RPC Functions**: Supabase allows RPC calls via JavaScript client
   ```javascript
   const { data } = await supabase.rpc("match_packs_by_embedding", {
     query_embedding: "[0.1, 0.2, ...]",
     match_threshold: 0.5,
     match_count: 5,
   });
   ```

---

## Testing Vector Search Locally

Before deploying, test locally with Supabase local dev:

```bash
# Start Supabase locally
supabase start

# Apply migrations
supabase db push

# Test in your app
npm run dev
```

The app will use your local Supabase instance (no real API keys needed).

---

## Environment Setup for Your App

Add to `.env.local`:

```env
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGc...  # Your anon key from Supabase dashboard
```

The app will:

1. Connect to your Supabase project
2. Generate hash-based embeddings (browser-side, no API call)
3. Insert packs with embeddings into the `packs` table
4. Search via `match_packs_by_embedding()` RPC function

---

## Quick Checklist

- [ ] Go to Supabase dashboard → SQL Editor
- [ ] Run: `create extension if not exists vector;`
- [ ] Paste and run the full schema from `supabase/schema.sql`
- [ ] Set `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY` in `.env.local`
- [ ] Run `npm run dev` and test creating/searching packs
- [ ] Check the `match_packs_by_embedding()` function works

---

## Troubleshooting

### Error: "type vector does not exist"

→ pgvector extension not enabled. Run: `create extension if not exists vector;`

### Error: "function match_packs_by_embedding does not exist"

→ Schema not applied. Run the full SQL from `supabase/schema.sql` in the SQL editor.

### Embeddings not storing / null values

→ Check that the app generated embeddings before insert. Look at browser console for errors in `generateCombinedEmbedding()`.

### Search returns no results

→ Lower the `match_threshold` in `PacksTable.tsx` (default 0.3). Hash-based embeddings may be sparser than ML models.

---

## Next Steps

1. **Share your Supabase project URL** (no secrets) and I can:

   - Test vector insert/search remotely
   - Verify the schema and index are working
   - Debug any issues

2. **Scale embeddings**: Switch from hash-based to:

   - OpenAI embeddings (better quality, needs API key)
   - Supabase Edge Functions (self-hosted embeddings, no key)

3. **Add metadata filtering**: Search vectors + filter by tags/category

Ready to wire it up? Paste your Supabase project URL! 🚀

---

Generate a component called UserSettings with hooks
Run typecheck
Search for all pack-related types
Generate docs for src/types.ts
