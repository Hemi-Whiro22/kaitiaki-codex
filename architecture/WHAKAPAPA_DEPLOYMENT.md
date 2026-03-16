# 🐺 WHAKAPAPA SYSTEM DEPLOYMENT GUIDE

## What Just Happened

You now have:

✅ **Whakapapa reunification database schema** (fully in seed.sql)  
✅ **Genealogy tables** (whakapapa_people, connections, whenua, marae)  
✅ **Tapu protection** (RLS policies, privacy levels)  
✅ **Example data** (Waitemata genealogy breaking colonial segregation)  
✅ **Seed data** (ready to deploy immediately)

---

## Immediate Next: UI Components

### What We Need to Build

```
src/components/
├── WhakapapaDiscovery.tsx      -- Search interface
├── WhakapapaCard.tsx            -- Shareable genealogy card
├── WhakapapaMap.tsx             -- Geographic visualization
└── WhakapapaVerification.tsx    -- Community verification UI

src/hooks/
├── useWhakapapaSearch.ts        -- Search matching algorithm
└── useWhakapapaMatches.ts       -- Find genealogical connections

src/lib/
└── whakapapa.ts                 -- Core logic (matching, verification)
```

### Example Component: WhakapapaDiscovery

```typescript
/**
 * 🐺 WHAKAPAPA DISCOVERY
 *
 * Interface for finding genealogical connections
 * Breaking colonial segregation through genealogy cross-reference
 */

export const WhakapapaDiscovery: React.FC = () => {
  const [searchType, setSearchType] = useState<
    "name" | "place" | "hapū" | "marae"
  >("name");
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<WhakapapaMatch[]>([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);

    // Call matching algorithm
    const matches = await searchWhakapapa({
      type: searchType,
      query: query,
    });

    setResults(matches);
    setLoading(false);
  };

  return (
    <div className="whakapapa-discovery">
      {/* Search interface */}
      {/* Results display */}
      {/* Connection visualization */}
    </div>
  );
};
```

---

## Phase 1: Basic Frontend (1 Component)

Just need to get the search working:

1. **WhakapapaDiscovery.tsx** - Let users search by name/place/hapū
2. **useWhakapapaSearch** hook - Query matching algorithm
3. **Display results** - Show connections found

This alone will:

- ✅ Help whānau find each other
- ✅ Show genealogical connections
- ✅ Prove people are connected (breaking colonial division)
- ✅ Create momentum for reunion

---

## Phase 2: Visualization & Sharing

Add:

- WhakapapaCard (shareable genealogy card)
- Map visualization (see where people from)
- Connection diagrams (show how whānau connected)

---

## Phase 3: Verification & Community

Add:

- Community verification (elders can verify)
- Event integration (know when/where to gather)
- Marae directory (find your community)

---

## How to Deploy Now

### Database is Ready

```bash
# When you spin up the dev container
npm run dev

# PostgreSQL initializes with seed.sql
# Whakapapa tables created automatically
# Example genealogy seeded
# Ready to query
```

### Test It

```bash
# Connect to PostgreSQL (from inside container)
pack-shell

# Query the data
SELECT name, hapū, iwi, birth_year
FROM whakapapa_people
ORDER BY birth_year;

# Should show:
# Hikuroa | Ngāti Te Ata | Ngāpuhi | 1783
# Aorangi | Ngāti Te Ata | Ngāpuhi | 1820
# Te Ao   | Ngāti Te Ata | Ngāpuhi | 1860
```

---

## The Power of What's Seeded

With just the seed data, you can:

✅ Show how genealogy was documented (even by colonizers)  
✅ Prove connections exist (using their records)  
✅ Demonstrate potential (imagine 1000s of genealogies)  
✅ Show path to reunification

---

## Why This Matters

**Colonizers used Land Court to separate us.**

Kaitiaki uses the SAME DATA to prove we're connected.

When whānau see their genealogy cross-referenced:

- "My line connects to YOUR line"
- "We're not enemies, we're whānau"
- "The Land Court tried to divide us"
- "But whakapapa proves we're one"

**That's when the pack reforms.**

---

## Next Action

### Immediate (Today)

```bash
npm run dev
# Query whakapapa tables (they're seeded)
# Celebrate that the foundation is there
```

### Soon (Next Session)

Build the search interface:

1. Create `src/components/WhakapapaDiscovery.tsx`
2. Create `src/hooks/useWhakapapaSearch.ts`
3. Show search results
4. Watch people find their genealogy

### Full Vision (Phase 1-3)

Build the full reunification system

- Search ✅
- Visualization
- Verification
- Community gathering

---

## The Genealogy is Already There

Because:
✅ Land Court documents it  
✅ Census records it  
✅ Our names prove it  
✅ Our marae know it

Kaitiaki just makes it visible.

And when it's visible, we remember.

And when we remember, we reunite.

**🐺 HE WAKA EKE NOA**
_We're all in the same canoe_

---

**Database Status:** ✅ READY  
**Seed Data:** ✅ DEPLOYED  
**UI Components:** ⏳ NEXT  
**Reunification Mission:** 🚀 UNDERWAY
