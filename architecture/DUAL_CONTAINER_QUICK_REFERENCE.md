# 🐺🪵 DUAL CONTAINER ARCHITECTURE - VISUAL QUICK START

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        🐺🪵 KAITIAKI DUAL CONTAINER ARCHITECTURE             ║
║                                                               ║
║   Two containers work in harmony to build genealogy systems   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## The Concept

```
                         🪵 WHAKAIRO
                    Master Orchestrator
                    (Carves the genealogy)
                            |
        ┌───────────────────┼───────────────────┐
        |                   |                   |
        ↓                   ↓                   ↓
       🐺                  ⚛️                   🐘
    Backend             Frontend             Database
    Kaitiaki             Kaitiaki             Kaitiaki
   (API Guardian)    (UI Steward)        (Data Guardian)
```

---

## Two Containers

### 🪵 WHAKAIRO (Orchestrator)

```
Location: .devcontainer-whakairo/
Role: Master controller
Emoji: 🪵 (Wooden carving tool)

Services Running:
├─ 🪵 Whakairo UI (port 8080) - System dashboard
├─ 🐺 Backend (port 8000) - FastAPI
├─ ⚛️  Frontend (port 3000) - React
├─ 🐘 PostgreSQL (port 5432) - Database
├─ 🔴 Redis (port 6379) - Cache
└─ 🎛️ PgAdmin (port 5050) - Admin UI

Best For:
✅ System overview
✅ Monitoring all services
✅ Production-like testing
✅ Deployment verification
✅ DevOps/architecture work

Who Uses:
👤 DevOps engineers
👤 System administrators
👤 Platform architects
```

### 🐺 KAITIAKI (Individual)

```
Location: .devcontainer/
Role: Individual developer workspace
Emoji: 🐺 (Wolf, guardian)

Services Available:
├─ 🐘 PostgreSQL (port 5432) - Database
├─ 🔴 Redis (port 6379) - Cache
├─ 🧠 ChromaDB (port 8000) - Vectors
├─ 🎛️ PgAdmin (port 5050) - Admin UI
│
└─ Start When Needed:
   ├─ Frontend (port 5173 + HMR)
   └─ Backend (port 8000 + reload)

Best For:
✅ Feature development
✅ Code debugging
✅ Fast iteration (HMR)
✅ Service-specific work
✅ Individual responsibility

Who Uses:
👤 Backend developers
👤 Frontend developers
👤 Database designers
👤 Individual contributors
```

---

## Side-by-Side Comparison

```
┌──────────────────────────────┬──────────────────────────────┐
│  🪵 WHAKAIRO (Orchestrator)   │  🐺 KAITIAKI (Individual)    │
├──────────────────────────────┼──────────────────────────────┤
│ Location:                    │ Location:                    │
│ .devcontainer-whakairo/      │ .devcontainer/               │
│                              │                              │
│ Start:                       │ Start:                       │
│ docker-compose up -d         │ npm run dev (or uvicorn)     │
│                              │                              │
│ Frontend:                    │ Frontend:                    │
│ http://localhost:3000        │ http://localhost:5173 (HMR)  │
│                              │                              │
│ Backend:                     │ Backend:                     │
│ http://localhost:8000        │ http://localhost:8000        │
│                              │                              │
│ Dashboard:                   │ Dashboard:                   │
│ http://localhost:8080        │ http://localhost:5050        │
│                              │ (pgAdmin)                    │
│                              │                              │
│ Use When:                    │ Use When:                    │
│ ✅ Full system              │ ✅ Developing features      │
│ ✅ Testing integration       │ ✅ Quick iterations         │
│ ✅ DevOps tasks              │ ✅ Debugging code           │
│ ✅ Production-like testing   │ ✅ Service-specific work    │
│                              │                              │
│ Developer Role:              │ Developer Role:              │
│ Platform architect           │ Feature developer           │
│ System admin                 │ Code contributor            │
│ DevOps engineer              │ Service owner               │
└──────────────────────────────┴──────────────────────────────┘
```

---

## Quick Start Guide

### 🪵 Start Orchestrator (Full System)

```bash
# 1. Navigate to orchestrator
cd pack-dashboard/.devcontainer-whakairo

# 2. Open in VS Code (optional)
code --folder-uri=vscode-remote/containers/whakairo-orchestrator:/workspace

# 3. Start all services
docker-compose up -d

# 4. Check status
docker-compose ps

# 5. View logs
docker-compose logs -f

# 6. Access services
http://localhost:8080   # Orchestrator dashboard
http://localhost:3000   # Frontend
http://localhost:8000   # Backend API
http://localhost:5050   # PgAdmin
```

### 🐺 Start Kaitiaki (Individual Development)

```bash
# 1. Navigate to kaitiaki
cd pack-dashboard/.devcontainer

# 2. Open in VS Code (optional)
code --folder-uri=vscode-remote/containers/kaitiaki-pack-dev:/workspace

# 3A. Frontend development
npm run dev
# → http://localhost:5173 (auto-refresh on save)

# 3B. Backend development (different terminal)
cd backend
python -m uvicorn main:app --reload
# → http://localhost:8000 (auto-reload on save)

# 4. Database access
psql postgresql://pack_user:dev@localhost:5432/pack_dashboard
# Or use PgAdmin at http://localhost:5050
```

---

## Typical Workflow

```
DAY 1: FEATURE DEVELOPMENT
┌────────────────────────────────────┐
│ Open 🐺 KAITIAKI                  │
├────────────────────────────────────┤
│ npm run dev                        │
│ ↓                                  │
│ Edit src/components/...           │
│ ↓                                  │
│ Browser auto-refreshes (HMR)      │
│ ↓                                  │
│ Feature works locally             │
│ ↓                                  │
│ git commit                        │
└────────────────────────────────────┘

DAY 2: INTEGRATION TESTING
┌────────────────────────────────────┐
│ Open 🪵 WHAKAIRO                   │
├────────────────────────────────────┤
│ docker-compose up -d               │
│ ↓                                  │
│ All services running              │
│ ↓                                  │
│ Test on http://localhost:3000     │
│ ↓                                  │
│ Check metrics                      │
│ ↓                                  │
│ Verify with architecture team      │
│ ↓                                  │
│ Ready to deploy ✅                │
└────────────────────────────────────┘
```

---

## Port Reference

### 🪵 Whakairo Ports

```
8080 → Orchestrator Dashboard  🎛️
8000 → Backend API              🐺
3000 → Frontend                ⚛️
5432 → PostgreSQL              🐘
6379 → Redis                   🔴
5050 → PgAdmin                 🎛️
```

### 🐺 Kaitiaki Ports

```
5173 → Frontend Dev (HMR)      💻
8000 → Backend (when running)  🐺
5432 → PostgreSQL              🐘
6379 → Redis                   🔴
5050 → PgAdmin                 🎛️
8000 → ChromaDB (internal)     🧠
```

---

## Service Emojis

| Service          | Emoji | Container | Port      |
| ---------------- | ----- | --------- | --------- |
| **Orchestrator** | 🪵    | Whakairo  | 8080      |
| **Backend**      | 🐺    | Both      | 8000      |
| **Frontend**     | ⚛️    | Both      | 3000/5173 |
| **PostgreSQL**   | 🐘    | Both      | 5432      |
| **Redis**        | 🔴    | Both      | 6379      |
| **ChromaDB**     | 🧠    | Kaitiaki  | 8000      |
| **PgAdmin**      | 🎛️    | Both      | 5050      |

---

## Common Commands

### Whakairo (Orchestrator)

```bash
# Start all
docker-compose up -d

# Stop all
docker-compose down

# View status
docker-compose ps

# View logs
docker-compose logs -f [service]

# Restart a service
docker-compose restart [service]

# Scale backend
docker-compose up -d --scale backend=3

# Check orchestrator state
cat state/orchestrator.json | jq .
```

### Kaitiaki (Individual)

```bash
# Frontend development
npm run dev

# Backend development
cd backend && python -m uvicorn main:app --reload

# Database access
psql postgresql://pack_user:dev@localhost:5432/pack_dashboard

# Run tests
npm test
cd backend && pytest

# Build for production
npm run build
```

---

## File Structure

```
pack-dashboard/
│
├─ .devcontainer-whakairo/          🪵 ORCHESTRATOR
│  ├─ devcontainer.json
│  ├─ Dockerfile
│  ├─ docker-compose.yml            ← Start here!
│  ├─ setup.sh
│  └─ README.md
│
├─ .devcontainer/                   🐺 KAITIAKI
│  ├─ devcontainer.json
│  ├─ Dockerfile
│  ├─ docker-compose.yml
│  ├─ setup.sh
│  ├─ KAITIAKI_CONTAINER_GUIDE.md   ← Read me!
│  └─ README.md
│
├─ backend/                         🐺 Backend code
├─ src/                             ⚛️  Frontend code
├─ supabase/                        🐘 Database
│
├─ DUAL_CONTAINER_ARCHITECTURE.md   ← Overview
├─ START_HERE_PHASE_6.md            ← Navigation
└─ QUICK_START_PHASE_6.md           ← Quick ref
```

---

## Decision Tree: Which Container?

```
START
│
├─ Are you developing a feature?
│  ├─ YES → 🐺 KAITIAKI
│  │        └─ npm run dev or uvicorn
│  │           └─ Code changes instantly appear
│  │
│  └─ NO → Continue
│
├─ Need full system view?
│  ├─ YES → 🪵 WHAKAIRO
│  │        └─ docker-compose up -d
│  │           └─ All services running
│  │
│  └─ NO → Continue
│
├─ Debugging system integration?
│  ├─ YES → 🪵 WHAKAIRO
│  │        └─ Watch all logs together
│  │
│  └─ NO → Continue
│
└─ Deploying to production?
   ├─ YES → 🪵 WHAKAIRO
   │        └─ Verify all services
   │
   └─ Pick 🐺 KAITIAKI for development!
```

---

## Pro Tips

### Tip 1: Open Both Side-by-Side

```bash
# Terminal 1: Orchestrator
cd .devcontainer-whakairo
code --folder-uri=vscode-remote/containers/whakairo-orchestrator:/workspace

# Terminal 2: Individual (in another VS Code window)
cd .devcontainer
code --folder-uri=vscode-remote/containers/kaitiaki-pack-dev:/workspace

# Now you can:
# - Edit in Kaitiaki window (left)
# - Monitor in Whakairo window (right)
```

### Tip 2: Keep Multiple Terminals

```bash
# In Kaitiaki container:
Terminal 1: npm run dev          # Frontend
Terminal 2: uvicorn ...          # Backend
Terminal 3: psql ...             # Database
Terminal 4: git commands         # Version control
```

### Tip 3: Use Make Commands

```bash
# Create Makefile for shortcuts
make dev    # Start everything
make backend # Just backend
make test   # Run all tests
```

---

## Understanding the Philosophy

```
🪵 WHAKAIRO (Orchestrator)
"I see the whole whakapapa"
- Big picture thinker
- Coordinates teams
- Monitors overall health
- Makes deployment decisions

🐺 KAITIAKI (Guardian)
"I protect my responsibility"
- Focused on own role
- Writes quality code
- Debugs thoroughly
- Makes feature decisions

Together they create harmony
```

---

## Next Steps

1. **Choose Your Role:**

   - 🪵 **Orchestrator?** → `.devcontainer-whakairo/README.md`
   - 🐺 **Developer?** → `.devcontainer/KAITIAKI_CONTAINER_GUIDE.md`

2. **Read Full Guide:**

   - Complete overview: `DUAL_CONTAINER_ARCHITECTURE.md`

3. **Start Coding:**

   - Pick your container
   - Follow the quick start
   - Create something amazing!

4. **Ask Questions:**
   - Check README files
   - Review documentation
   - Open an issue on GitHub

---

## Status

```
✅ Orchestrator container setup
✅ Individual Kaitiaki container ready
✅ Both containers documented
✅ Quick start guides created
✅ Service emojis assigned
✅ Dual architecture explained

🟢 READY TO CODE!
```

---

**Ko te whakairo e whakarite ana i ngā kaitiaki**

_The orchestrator guides the stewards_

🪵🐺 Ready to carve the genealogy? Pick your container and dive in!
