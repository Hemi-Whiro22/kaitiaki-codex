# Ownership & Licenses: Pack Dashboard

## What's Ours (AwaNet, AGPL-3.0)

### Original Code (Our IP)

- `src/App.tsx` — main React app
- `src/components/PacksTable.tsx` — pack UI with vector search
- `src/lib/embedding.ts` — **hash-based embedding generator** (deterministic SHA-256 vectors, no external API)
- `src/lib/supabase.ts` — Supabase client integration
- `src/types.ts` — TypeScript types
- `.gitattributes` — UTF-8/LF encoding config (we built this for the project)
- `.editorconfig` — editor settings (we configured this)
- `BRANCHING.md` — git workflow docs (ours)
- `VECTOR_INDEX_GUIDE.md` — vector indexing explanation (ours)
- `supabase/seed.sql` — seed data (ours)

**Licensed under**: AGPL-3.0 + commercial exception (see `LICENSE`)

- Free for: personal, educational, non-profit, small business (<NZD $1M revenue or ≤10 employees)
- Commercial orgs: need koha/paid license (contact: license@awanet.nz)

---

## What's Third-Party (Built-Ins, Open Source)

### PostgreSQL Extensions (BSD License)

| Extension  | Owner                               | License        | What it does                  |
| ---------- | ----------------------------------- | -------------- | ----------------------------- |
| `pgcrypto` | PostgreSQL Global Development Group | BSD            | UUID generation, encryption   |
| `pgvector` | pgvector contributors               | MIT/Apache-2.0 | Vector data type & operations |

### PostgreSQL Built-in Index Types (BSD License)

| Index Type | Owner              | License | What it does                                        |
| ---------- | ------------------ | ------- | --------------------------------------------------- |
| IVFFlat    | PostgreSQL Project | BSD     | Fast approximate nearest neighbor search on vectors |

### React & Build Tools (MIT/Apache-2.0)

| Package               | License             | Purpose                 |
| --------------------- | ------------------- | ----------------------- |
| react                 | MIT (Facebook/Meta) | UI framework            |
| react-dom             | MIT (Facebook/Meta) | React DOM binding       |
| vite                  | MIT                 | Build tool & dev server |
| typescript            | Apache-2.0          | Type checking           |
| @supabase/supabase-js | Apache-2.0          | Supabase client         |
| tslib                 | 0BSD                | TypeScript helpers      |
| husky                 | MIT                 | Git hooks               |

### Supabase Platform (Apache-2.0)

- Supabase is open-source backend-as-a-service (self-host or use managed)
- We use their managed PostgreSQL + Auth + Realtime
- You own your data; Supabase terms apply to hosted version

---

## Data Sovereignty & Free Tier Model

### Your Data = Your Data

- All pack data is stored in **your Supabase project**
- You have full access, can export anytime, can self-host
- AwaNet does not access, store, or monetize your data

### Free Tier (AGPL-3.0)

- Use pack-dashboard free if you meet criteria above
- If you modify & deploy as a service → must share source (AGPL copyleft)
- Share improvements back with the community

### Commercial Tier

- For-profit orgs with >NZD $1M revenue or >10 employees
- Need commercial license (koha/payment)
- Includes: support, guarantees, no AGPL copyleft requirement
- Contact: license@awanet.nz

---

## Enforcement & Compliance

### How We Prevent Corporate Free-Riding

1. **AGPL-3.0 Copyleft**: If a company deploys pack-dashboard as a service (SaaS), they must:

   - Share their source code with users (or release it)
   - Cannot keep modifications proprietary

2. **Commercial Exception**: Large orgs must purchase a license to:

   - Use proprietary deployment (no AGPL copyleft)
   - Get support & indemnification
   - Use without open-sourcing changes

3. **Audit & Enforcement**:
   - Monitor public SaaS deployments
   - Reach out for license compliance
   - Legal action if necessary (like other AGPL projects: MongoDB, etc.)

### What We Track

- GitHub stars/forks (public)
- Supabase deployments (if using managed)
- Self-hosted deployments (community reports)
- Legal: AGPL requires source sharing on network deployment

### What We Don't Track

- Your personal data (it's in your Supabase account, not ours)
- Internal company usage (AGPL allows internal use without sharing)
- Development/testing (no public deployment = free usage)

---

## Transparency

### What's Open Source

- All source code in this repo (GitHub public)
- Full dependencies listed in `package.json`
- Schema & migrations in `supabase/`

### What We Own

- Hash-based embedding logic (deterministic, no external API = sovereign)
- UI/UX design decisions
- Documentation & guides
- License & commercial terms

### What's Community

- PostgreSQL, pgvector, React, etc. (see `package.json`)
- Supabase platform (Apache-2.0)
- git/GitHub infrastructure

---

## Example Scenarios

| Scenario                            | Status                | Notes                                                          |
| ----------------------------------- | --------------------- | -------------------------------------------------------------- |
| **Personal project** (use our code) | ✅ FREE               | AGPL-3.0, no license needed                                    |
| **Non-profit (use our code)**       | ✅ FREE               | AGPL-3.0, share if you modify                                  |
| **Startup <10 people**              | ✅ FREE               | Under size threshold, AGPL-3.0                                 |
| **SaaS (use our code, modify)**     | ⚠️ AGPL APPLIES       | Must share source with users OR buy commercial license         |
| **Enterprise (use unmodified)**     | ⚠️ COMMERCIAL LICENSE | > NZD $1M revenue or >10 employees                             |
| **Fork & sell**                     | ❌ NOT ALLOWED        | AGPL + commercial exception apply; must license or open-source |
| **Internal company use**            | ✅ FREE               | No network deployment = no obligation to share                 |

---

## How to Comply

### If You're Free Tier

1. Acknowledge AGPL-3.0 in your project README
2. If you modify pack-dashboard, share your changes with users
3. Keep attribution to AwaNet

### If You're Commercial

1. Purchase a commercial license (email: license@awanet.nz)
2. Use without AGPL copyleft obligations
3. Get support & indemnification

---

## Questions?

- **Data privacy**: See `SUPABASE_SETUP.md` (your data is yours)
- **Vector indexing**: See `VECTOR_INDEX_GUIDE.md`
- **Licensing**: See `LICENSE`
- **Commercial inquiries**: license@awanet.nz

---

## TL;DR

✅ **We built**: hash embeddings, React UI, git encoding, docs, license model
🔧 **We use**: PostgreSQL, pgvector, IVFFlat, React, Supabase (all open-source)
💰 **Model**: Free for people (AGPL-3.0), pay for corps (commercial license)
🛡️ **Data**: Yours; we don't store it
📜 **License**: AGPL-3.0 + commercial exception

Keep it sovereign, keep it free. 🚀
