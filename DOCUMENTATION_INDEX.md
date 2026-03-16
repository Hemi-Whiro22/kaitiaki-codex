# Documentation Index

Quick reference for all Pack Dashboard guides.

---

## For Users

### Getting Started

- **[README.md](README.md)** — Project overview, setup, key features
- **[SUPABASE_SETUP.md](SUPABASE_SETUP.md)** — Connect to managed Supabase cloud instance
- **[SELF_HOSTING.md](SELF_HOSTING.md)** — Run locally via Docker or deploy to VPS

### Features & How-Tos

- **[VECTOR_INDEX_GUIDE.md](VECTOR_INDEX_GUIDE.md)** — Deep dive: how semantic search works with pgvector + IVFFlat
- **[BRANCHING.md](BRANCHING.md)** — Git workflow (for developers)

### Licensing & Eligibility

- **[LICENSE](LICENSE)** — AGPL-3.0 + commercial exception (legal text)
- **[FREE_TIER_ELIGIBILITY.md](FREE_TIER_ELIGIBILITY.md)** — Who qualifies for free? When do you pay?
- **[OWNERSHIP.md](OWNERSHIP.md)** — What's ours vs third-party + data sovereignty statement

### Community & Contribution

- **[CONTRIBUTING.md](CONTRIBUTING.md)** — How to contribute code, docs, ideas
- **[COMMUNITY_MODEL.md](COMMUNITY_MODEL.md)** — Bounty program, revenue share, sponsorship tiers
- **[TRANSPARENCY.md](TRANSPARENCY.md)** — Annual budget & impact report

---

## Quick Navigation by Question

### "I want to use Pack Dashboard"

→ Start with [README.md](README.md)  
→ Then choose: [SUPABASE_SETUP.md](SUPABASE_SETUP.md) (cloud) or [SELF_HOSTING.md](SELF_HOSTING.md) (local)

### "Do I need to pay?"

→ [FREE_TIER_ELIGIBILITY.md](FREE_TIER_ELIGIBILITY.md)

### "What's the business model?"

→ [COMMUNITY_MODEL.md](COMMUNITY_MODEL.md)  
→ [TRANSPARENCY.md](TRANSPARENCY.md) (annual finances)

### "What's your license?"

→ [LICENSE](LICENSE)  
→ [OWNERSHIP.md](OWNERSHIP.md) (explained in plain English)

### "How does semantic search work?"

→ [VECTOR_INDEX_GUIDE.md](VECTOR_INDEX_GUIDE.md)

### "I want to contribute"

→ [CONTRIBUTING.md](CONTRIBUTING.md)  
→ [COMMUNITY_MODEL.md](COMMUNITY_MODEL.md) (bounties + revenue share)

### "How do I deploy this?"

→ [SUPABASE_SETUP.md](SUPABASE_SETUP.md) (managed)  
→ [SELF_HOSTING.md](SELF_HOSTING.md) (self-hosted)  
→ [BRANCHING.md](BRANCHING.md) (git workflow)

### "Who built this? Is my data safe?"

→ [OWNERSHIP.md](OWNERSHIP.md)

### "Where does my money go?"

→ [TRANSPARENCY.md](TRANSPARENCY.md)

---

## File Structure

```
pack-dashboard/
├── README.md                      # Start here
├── LICENSE                         # AGPL-3.0 + commercial exception
├──
├── 📚 GUIDES
├── SUPABASE_SETUP.md              # Cloud deployment
├── SELF_HOSTING.md                # Docker + local deployment
├── VECTOR_INDEX_GUIDE.md          # Semantic search deep dive
├── BRANCHING.md                   # Git workflow
├── CONTRIBUTING.md                # How to contribute
├──
├── 💼 BUSINESS & COMMUNITY
├── OWNERSHIP.md                   # What's ours vs third-party
├── LICENSE                         # Legal license text
├── FREE_TIER_ELIGIBILITY.md       # Who pays? When?
├── COMMUNITY_MODEL.md             # Bounties + revenue share
├── TRANSPARENCY.md                # Budget + impact (annual)
├──
├── 📋 THIS FILE
├── DOCUMENTATION_INDEX.md          # You are here
├──
├── 💻 CODE
├── package.json                   # Dependencies
├── tsconfig.json                  # TypeScript config
├── vite.config.ts                 # Build config
├── src/
│   ├── main.tsx                   # Entry point
│   ├── App.tsx                    # Main component
│   ├── types.ts                   # TypeScript types
│   ├── lib/
│   │   ├── embedding.ts           # Hash-based embeddings
│   │   ├── supabase.ts            # Supabase client
│   │   └── ...
│   ├── components/
│   │   ├── PacksTable.tsx         # Main UI component
│   │   └── ...
│   └── ...
├── supabase/
│   ├── schema.sql                 # PostgreSQL schema
│   ├── seed.sql                   # Sample data
│   └── ...
├──
├── 🐳 DEPLOYMENT
├── docker-compose.yml             # Local PostgreSQL + pgAdmin
├── .env.example                   # Environment template
├── Dockerfile                     # (optional) Container image
└── ...
```

---

## Reading Order

**For End Users (want to use the tool)**:

1. README.md
2. SUPABASE_SETUP.md or SELF_HOSTING.md (depending on deployment)
3. FREE_TIER_ELIGIBILITY.md (understand licensing)

**For Contributors (want to build/improve it)**:

1. README.md (overview)
2. CONTRIBUTING.md (how to contribute)
3. BRANCHING.md (git workflow)
4. Relevant deep dives (VECTOR_INDEX_GUIDE.md, etc.)

**For Business/Decision Makers**:

1. README.md (what is it?)
2. FREE_TIER_ELIGIBILITY.md (am I free?)
3. COMMUNITY_MODEL.md (revenue model)
4. OWNERSHIP.md (safety/control)
5. TRANSPARENCY.md (where does money go?)

**For Security/Compliance Auditors**:

1. OWNERSHIP.md (what's in-scope?)
2. LICENSE (legal framework)
3. CONTRIBUTING.md + COMMUNITY_MODEL.md (who has access?)
4. TRANSPARENCY.md (how is it funded?)
5. Code: src/ + supabase/ (implementation review)

---

## Glossary

| Term                   | Definition                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| **Pack**               | A collection of items with metadata (name, description, embedding)                          |
| **Embedding**          | 384-dimensional vector representing semantic meaning of text (via SHA-256 hash)             |
| **Vector Search**      | Finding similar packs by querying embeddings (semantic similarity, not keyword match)       |
| **AGPL-3.0**           | Copyleft license: modifications must be open-sourced OR a commercial license purchased      |
| **Free Tier**          | Users who qualify (non-profit, educational, small business, etc.) and don't pay             |
| **Commercial License** | Paid license for enterprises / SaaS companies (required to avoid AGPL copyleft)             |
| **IVFFlat Index**      | Approximate nearest-neighbor search index in PostgreSQL (5-10x faster than full table scan) |
| **pgvector**           | PostgreSQL extension for vector operations (embedding storage + cosine similarity)          |
| **RLS**                | Row-Level Security in PostgreSQL (controls who can read/write which rows)                   |
| **Supabase**           | Managed PostgreSQL + Auth + Realtime (Firebase alternative)                                 |
| **Self-Hosting**       | Running Pack Dashboard on your own hardware or VPS (not Supabase cloud)                     |
| **Bounty**             | Paid work (bug fix, feature, docs) that anyone can claim from the issue tracker             |

---

## Support & Questions

**Question about...**

- **Using the tool?** → community@awanet.nz
- **Contributing code?** → maintainers@awanet.nz + see CONTRIBUTING.md
- **Licensing/eligibility?** → license@awanet.nz (see FREE_TIER_ELIGIBILITY.md)
- **Business terms?** → partnerships@awanet.nz (see COMMUNITY_MODEL.md)
- **Security issue?** → security@awanet.nz (do NOT post publicly)
- **Transparency/audit?** → audit@awanet.nz (see TRANSPARENCY.md)
- **Code of conduct?** → conduct@awanet.nz (confidential)
- **Everything else?** → hello@awanet.nz

---

## License

All documentation is licensed under **AGPL-3.0** (same as code).

You can:

- ✅ Read it
- ✅ Share it
- ✅ Modify it
- ✅ Use it commercially (if your deployment is AGPL-3.0 or you have commercial license)

You must:

- ⚠️ Share modifications (if deployed)
- ⚠️ Give credit

See `LICENSE` for full terms.

---

**Last Updated**: January 2025  
**Maintainer**: AwaNet Community  
**Questions?** hello@awanet.nz
