# 📁 Project Structure Guide

**Your clean, organized workspace for genealogy systems**

---

## Directory Overview

```
pack-dashboard/
│
├── 📄 ROOT NAVIGATION (START HERE)
│   ├── README.md                    ← Main project overview
│   ├── START_HERE_PHASE_6.md        ← Quick navigation guide
│   ├── QUICK_START_PHASE_6.md       ← Get up and running fast
│   └── QUICK_REFERENCE.md           ← Command cheat sheet
│
├── 🪵 CONTAINERS (Development Environments)
│   ├── containers/
│   │   ├── whakairo/                ← 🪵 Orchestrator Container
│   │   │   ├── devcontainer.json    ✓ VS Code config
│   │   │   ├── Dockerfile           ✓ Container image
│   │   │   ├── docker-compose.yml   ✓ All 6 services
│   │   │   ├── setup.sh             ✓ Initialization
│   │   │   ├── README.md            ✓ Full guide
│   │   │   ├── logs/                ✓ Service logs
│   │   │   ├── config/              ✓ Configuration
│   │   │   └── state/               ✓ System state
│   │   │
│   │   └── kaitiaki/                ← 🐺 Individual Developer Container
│   │       └── README.md            ✓ Development guide
│   │
│   └── .devcontainer/               ← (Legacy - use containers/kaitiaki now)
│
├── 💻 CODE (Application Source)
│   ├── backend/                     ← 🐺 FastAPI Backend
│   │   ├── main.py                  ✓ 350 lines, 9 routers, 39 endpoints
│   │   ├── kaitiaki/
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   ├── routers/
│   │   │   ├── whakapapa.py         ✓ Genealogy operations
│   │   │   ├── land_court.py        ✓ Court records
│   │   │   ├── pdf_processor.py     ✓ Document processing
│   │   │   ├── language.py          ✓ Te reo support
│   │   │   ├── user_preferences.py  ✓ User settings
│   │   │   ├── collaboration.py     ✓ Kaitiaki teamwork
│   │   │   ├── chat_history.py      ✓ Chat persistence
│   │   │   ├── config_management.py ✓ System config
│   │   │   └── admin_panel.py       ✓ Administration
│   │   ├── requirements.txt         ✓ Python dependencies
│   │   ├── Dockerfile              ✓ Backend container
│   │   └── BACKEND_ARCHITECTURE.md ✓ Detailed guide
│   │
│   ├── src/                         ← ⚛️ React Frontend
│   │   ├── components/
│   │   │   ├── ChatPanel.tsx
│   │   │   ├── KaitiakiSeedViewer.tsx
│   │   │   ├── MauriLens.tsx
│   │   │   ├── PacksTable.tsx
│   │   ├── lib/
│   │   │   ├── supabase.ts
│   │   │   ├── embedding.ts
│   │   │   └── llm/
│   │   ├── hooks/
│   │   ├── types/
│   │   ├── App.tsx
│   │   └── main.tsx
│   │
│   ├── supabase/                    ← 🐘 Database
│   │   ├── schema.sql               ✓ 6 whakapapa + genealogy tables
│   │   └── seed.sql                 ✓ Sample data
│   │
│   ├── public/                      ← Static assets
│   │   └── index.html
│   │
│   ├── mcp-server/                  ← MCP Server
│   │   ├── src/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── README.md
│   │
│   ├── scripts/                     ← Helper scripts
│   │   └── precommit-secrets.sh
│   │
│   └── dist/                        ← Build output (generated)
│
├── 📚 DOCUMENTATION (Phase by Phase)
│   ├── docs/
│   │   ├── architecture/            ← System design
│   │   │   ├── DUAL_CONTAINER_ARCHITECTURE.md     ✓ Two containers explained
│   │   │   ├── DUAL_CONTAINER_QUICK_REFERENCE.md ✓ Visual quick ref
│   │   │   ├── ARCHITECTURE.md                    ✓ Overall design
│   │   │   ├── OPERATIONAL_INFRASTRUCTURE.md      ✓ Operations
│   │   │   ├── KUBERNETES_READINESS.md            ✓ K8s guide
│   │   │   └── WHAKAPAPA_DEPLOYMENT.md            ✓ Deployment strategy
│   │   │
│   │   ├── guides/                  ← How-to guides
│   │   │   ├── QUICK_START_PHASE_6.md             ✓ Get running
│   │   │   ├── START_HERE_PHASE_6.md              ✓ Navigation guide
│   │   │   ├── DEPLOYMENT_CHECKLIST.md            ✓ Go live checklist
│   │   │   ├── SUPABASE_SETUP.md                  ✓ Database setup
│   │   │   ├── KAITIAKI_SDK_VISION.md             ✓ SDK design
│   │   │   ├── TE_REO_WORKFLOW.md                 ✓ Language workflow
│   │   │   ├── SELF_HOSTING.md                    ✓ Self-host guide
│   │   │   └── CONTRIBUTING.md                    ✓ Contribution guide
│   │   │
│   │   ├── phase-summaries/         ← Phase reviews
│   │   │   ├── PHASE_2_SUMMARY.md                 ✓ Phase 2 review
│   │   │   ├── PHASE_6_DELIVERY_MANIFEST.md       ✓ Phase 6 manifest
│   │   │   ├── PHASE_6_EXECUTIVE_SUMMARY.md       ✓ Phase 6 executive
│   │   │   ├── PHASE_6_FINAL_STATUS.md            ✓ Phase 6 final
│   │   │   ├── PHASE_6_VISUAL_SUMMARY.md          ✓ Phase 6 visual
│   │   │   ├── SESSION_6_COMPLETE.md              ✓ Session 6 recap
│   │   │   ├── SESSION_COMPLETE.md                ✓ All sessions recap
│   │   │   ├── BACKEND_DELIVERY_SUMMARY.md        ✓ Backend summary
│   │   │   └── BACKEND_STATUS.md                  ✓ Backend status
│   │   │
│   │   └── technical/               ← Technical reference
│   │       ├── FASTAPI_COMPLETE.md               ✓ FastAPI reference
│   │       ├── VECTOR_INDEX_GUIDE.md             ✓ Embeddings guide
│   │       ├── SEED_IMPLEMENTATION_SUMMARY.md    ✓ Seed system
│   │       ├── FRONTEND_BACKEND_INTEGRATION.md   ✓ Integration guide
│   │       ├── COMMUNITY_MODEL.md                ✓ Community model
│   │       ├── KAITIAKI_SEED_GUIDE.md            ✓ Seed guide
│   │       ├── FREE_TIER_ELIGIBILITY.md          ✓ Tier info
│   │       └── OWNERSHIP.md                      ✓ Ownership model
│   │
│   └── (Legacy docs to organize - see migration section)
│       ├── DOCUMENTATION_INDEX.md
│       ├── TEST_REPORT.md
│       ├── TRANSPARENCY.md
│       ├── FILES_CREATED_THIS_SESSION.md
│       └── BRANCHING.md
│
├── ⚙️ CONFIGURATION FILES (Root)
│   ├── devcontainer.json            ← Shared devcontainer (for .devcontainer/)
│   ├── docker-compose.yml           ← Shared compose (Kaitiaki)
│   ├── package.json                 ✓ Frontend dependencies + scripts
│   ├── tsconfig.json                ✓ TypeScript config
│   ├── tsconfig.node.json           ✓ Node TypeScript config
│   ├── vite.config.ts               ✓ Vite bundler config
│   ├── .eslintrc.cjs                ✓ ESLint rules
│   ├── .env.example                 ✓ Environment template
│   ├── .gitignore                   ✓ Git ignore patterns
│   ├── .gitattributes               ✓ Git attributes
│   ├── .husky/                      ✓ Pre-commit hooks
│   └── LICENSE                      ✓ MIT License
│
├── 🌐 WEB ROOT
│   └── index.html                   ← Static HTML entry point
│
└── 🔧 GIT & BUILD
    ├── .git/                        ← Git history
    ├── node_modules/                ← Frontend dependencies (generated)
    ├── tsconfig.tsbuildinfo        ← TypeScript cache
    ├── package-lock.json           ← Lock file
    └── (not committed to git)
```

---

## Quick Navigation

### 🚀 Getting Started

| Goal              | File                     |
| ----------------- | ------------------------ |
| First time?       | `START_HERE_PHASE_6.md`  |
| Quick commands?   | `QUICK_REFERENCE.md`     |
| Get running fast? | `QUICK_START_PHASE_6.md` |
| Main overview?    | `README.md`              |

### 🪵 Orchestrator (Full System)

| Goal                  | File                                     |
| --------------------- | ---------------------------------------- |
| Start orchestrator?   | `containers/whakairo/README.md`          |
| Orchestrator setup?   | `containers/whakairo/docker-compose.yml` |
| All services running? | `containers/whakairo/`                   |

### 🐺 Individual Development

| Goal              | File                                                        |
| ----------------- | ----------------------------------------------------------- |
| Develop features? | `containers/kaitiaki/README.md`                             |
| Frontend dev?     | `npm run dev` → http://localhost:5173                       |
| Backend dev?      | `cd backend && python -m uvicorn main:app --reload`         |
| Database work?    | `containers/kaitiaki/README.md` (Database Designer section) |

### 📚 Architecture & Design

| Goal            | File                                               |
| --------------- | -------------------------------------------------- |
| Two containers? | `docs/architecture/DUAL_CONTAINER_ARCHITECTURE.md` |
| System design?  | `docs/architecture/ARCHITECTURE.md`                |
| Operations?     | `docs/architecture/OPERATIONAL_INFRASTRUCTURE.md`  |
| Kubernetes?     | `docs/architecture/KUBERNETES_READINESS.md`        |

### 💻 Backend

| Goal                  | File                                    |
| --------------------- | --------------------------------------- |
| Backend details?      | `backend/BACKEND_ARCHITECTURE.md`       |
| 39 endpoints?         | `backend/main.py` (with router imports) |
| Add endpoint?         | Create in `backend/routers/`            |
| Backend dependencies? | `backend/requirements.txt`              |

### ⚛️ Frontend

| Goal              | File              |
| ----------------- | ----------------- |
| Frontend code?    | `src/` directory  |
| Components?       | `src/components/` |
| Run dev server?   | `npm run dev`     |
| Build production? | `npm run build`   |

### 🐘 Database

| Goal           | File                          |
| -------------- | ----------------------------- |
| Schema?        | `supabase/schema.sql`         |
| Sample data?   | `supabase/seed.sql`           |
| Modify schema? | Edit `.sql` files and migrate |

### 🚢 Deployment

| Goal                 | File                                        |
| -------------------- | ------------------------------------------- |
| Deploy?              | `docs/architecture/DEPLOYMENT_CHECKLIST.md` |
| Production strategy? | `docs/architecture/WHAKAPAPA_DEPLOYMENT.md` |
| Self-host?           | `docs/guides/SELF_HOSTING.md`               |

---

## Container Relationships

```
pack-dashboard/
│
├── containers/whakairo/       🪵 ORCHESTRATOR
│   ├── docker-compose.yml     (runs ALL services together)
│   │   ├── backend/           → ../backend/
│   │   ├── src/               → ../src/
│   │   ├── supabase/          → ../supabase/
│   │   ├── postgres           (port 5432)
│   │   ├── redis              (port 6379)
│   │   └── pgadmin            (port 5050)
│   └── README.md              ← Start here to run full system
│
├── .devcontainer/             🐺 INDIVIDUAL (LEGACY PATH)
│   └── (maps to containers/kaitiaki conceptually)
│
├── containers/kaitiaki/       🐺 INDIVIDUAL (NEW PATH)
│   └── README.md              ← Development guide
│
└── Source Code (shared by both)
    ├── backend/
    ├── src/
    └── supabase/
```

---

## File Organization Philosophy

### 1️⃣ **Clear Entry Points**

- Root has main README + START_HERE guides
- New users aren't lost
- Clear paths for different roles

### 2️⃣ **By Purpose**

- `containers/` - Development environments
- `docs/` - Documentation by topic
- `backend/`, `src/`, `supabase/` - Source code
- Root - Configuration files

### 3️⃣ **Containers Are Co-Located**

- Both containers in `containers/` folder
- Easy to compare (whakairo vs kaitiaki)
- Each has own README with clear purpose

### 4️⃣ **Documentation Is Organized**

- `docs/architecture/` - System design
- `docs/guides/` - How-to guides
- `docs/phase-summaries/` - Progress tracking
- `docs/technical/` - Reference material

### 5️⃣ **Source Code Is Clean**

- Only essential directories at root
- Clear separation: backend, frontend, database
- No clutter or confusion

---

## When to Use Each Location

| Location               | When                   | Example                    |
| ---------------------- | ---------------------- | -------------------------- |
| `containers/whakairo/` | Need full system       | DevOps, deployment testing |
| `containers/kaitiaki/` | Individual development | Feature work, debugging    |
| `backend/`             | Backend code           | Add router, fix bug        |
| `src/`                 | Frontend code          | New component, UI          |
| `supabase/`            | Database schema        | Add table, modify query    |
| `docs/`                | Learning/reference     | Need guide, check status   |

---

## Migration Guide (If Moving Old Files)

Old files should move to `docs/`:

```
# BEFORE (Messy Root)
pack-dashboard/
├── ARCHITECTURE.md
├── BACKEND_DELIVERY_SUMMARY.md
├── TEST_REPORT.md
├── FILES_CREATED_THIS_SESSION.md
└── 37 other markdown files...

# AFTER (Clean Organization)
pack-dashboard/
├── docs/
│   ├── architecture/
│   │   ├── ARCHITECTURE.md
│   │   └── ...
│   ├── guides/
│   │   └── ...
│   ├── phase-summaries/
│   │   ├── BACKEND_DELIVERY_SUMMARY.md
│   │   └── ...
│   └── technical/
│       ├── TEST_REPORT.md
│       └── ...
```

---

## Next Steps

1. **Bookmark Key Files:**

   - `START_HERE_PHASE_6.md` - Your GPS
   - `QUICK_REFERENCE.md` - Quick commands
   - `containers/whakairo/README.md` - Orchestrator guide
   - `containers/kaitiaki/README.md` - Developer guide

2. **Choose Your Path:**

   - 🪵 **Orchestrator?** → `containers/whakairo/README.md`
   - 🐺 **Developer?** → `containers/kaitiaki/README.md`

3. **Get Coding:**

   - Follow the quick start for your role
   - Set up your development environment
   - Create something amazing!

4. **Contribute:**
   - See `docs/guides/CONTRIBUTING.md`
   - Follow the branching strategy
   - Submit pull requests

---

## Status

```
✅ Root navigation clear
✅ Containers co-located
✅ Documentation organized
✅ Source code clean
✅ Entry points obvious

🟢 STRUCTURE OPTIMIZED FOR SUCCESS
```

---

**Ko te wāhitau e hari ana i ngā kōrero**

_A well-organized structure carries the knowledge_

**Questions?** Check `START_HERE_PHASE_6.md` or browse `docs/`
