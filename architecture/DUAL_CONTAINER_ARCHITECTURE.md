# 🐺🪵 Kaitiaki Dual Container Architecture

**Ko te whakairo e whakarite ana i ngā kaitiaki - The orchestrator guides the stewards**

---

## The Vision

Two complementary dev containers work together:

```
                    🪵 WHAKAIRO
            (Master Orchestrator)
                  8080 | 8000
         _____________|___________
        |             |           |
       🐺           ⚛️            🐘
    Backend      Frontend     Database
    (8000)        (3000)       (5432)

      vs

    🐺 KAITIAKI (Individual)
    ├─ Backend Dev (8000)
    ├─ Frontend Dev (5173)
    ├─ Database (5432)
    └─ PgAdmin (5050)
```

---

## Quick Comparison

| Aspect            | 🪵 Whakairo                  | 🐺 Kaitiaki                  |
| ----------------- | ---------------------------- | ---------------------------- |
| **Purpose**       | System orchestration         | Individual development       |
| **Best for**      | DevOps, monitoring           | Coding, debugging            |
| **Services**      | All running                  | All available                |
| **Ports**         | 8000, 3000, 5432, 6379, 8080 | 5173, 8000, 5432, 5050, 6379 |
| **Frontend Port** | 3000 (production-like)       | 5173 (dev with HMR)          |
| **Use When**      | Need full system view        | Developing features          |
| **Who Uses**      | DevOps, architects           | Developers                   |
| **Container**     | `.devcontainer-whakairo/`    | `.devcontainer/`             |

---

## The Two Container Approach

### 🪵 Whakairo: Master Orchestrator

**Location:** `.devcontainer-whakairo/`

**What it does:**

- Orchestrates ALL services in production-like setup
- Monitors system health & genealogy metrics
- Manages service lifecycle (start/stop/scale)
- Provides system overview dashboard (port 8080)
- Coordinates deployments

**Services running:**

```
🪵 Whakairo Container
├── 🐺 Backend (port 8000)
├── ⚛️  Frontend (port 3000)
├── 🐘 PostgreSQL (port 5432)
├── 🔴 Redis (port 6379)
├── 🎛️ PgAdmin (port 5050)
└── 🎛️ Orchestrator UI (port 8080)
```

**Who uses it:**

- DevOps engineers
- System administrators
- Platform architects
- Anyone needing full system view

**Example commands:**

```bash
cd .devcontainer-whakairo
docker-compose up -d
docker-compose ps
docker-compose logs -f backend
```

---

### 🐺 Kaitiaki: Individual Steward

**Location:** `.devcontainer/`

**What it does:**

- Provides development environment for ONE service at a time
- Hot module replacement (HMR) for fast feedback
- Direct access to code editor
- Service-specific debugging tools
- Quick iteration on features

**Services running:**

```
🐺 Kaitiaki Container
├── Available services:
│   ├── 🐘 PostgreSQL (port 5432)
│   ├── 🔴 Redis (port 6379)
│   ├── 🧠 ChromaDB (port 8000 internal)
│   └── 🎛️ PgAdmin (port 5050)
│
└── Your dev servers (start manually):
    ├── Frontend: npm run dev (port 5173)
    └── Backend: uvicorn (port 8000)
```

**Who uses it:**

- Backend developers
- Frontend developers
- Database designers
- Individual contributors

**Example commands:**

```bash
cd .devcontainer
npm run dev              # Frontend with HMR
# OR
cd backend && python -m uvicorn main:app --reload  # Backend
```

---

## When to Use Each

### Use 🪵 Whakairo When You Need To:

✅ See all services running together  
✅ Verify system integration  
✅ Check genealogy metrics  
✅ Deploy to production  
✅ Monitor system health  
✅ Manage service scaling  
✅ View orchestrator dashboard

**Example Scenario:**

> "I need to verify that the new chat history router works end-to-end with the frontend, backend, and database all together."

```bash
# Open Whakairo
cd .devcontainer-whakairo
docker-compose up -d

# Now all services run in production-like mode
# Visit http://localhost:3000 to see frontend
# Check http://localhost:8080 for orchestrator view
```

---

### Use 🐺 Kaitiaki When You Need To:

✅ Develop a specific feature  
✅ Debug a backend endpoint  
✅ Create a new component  
✅ Write database migrations  
✅ Get fast feedback (HMR)  
✅ Test individual service  
✅ Quick iterations

**Example Scenario:**

> "I need to update the ChatPanel component and see changes in real-time."

```bash
# Open Kaitiaki
cd .devcontainer
npm run dev

# Frontend starts on http://localhost:5173 with HMR
# Save a file → Browser refreshes automatically
```

---

## Typical Developer Workflow

### Day 1: Developing a Feature

```bash
# 1. Open Kaitiaki container (individual dev)
cd .devcontainer
VS Code → Open in Container

# 2. Start frontend dev server
npm run dev
# → http://localhost:5173 (with HMR)

# 3. Create new component
src/components/NewFeature.tsx
# → Auto-reloads in browser

# 4. Done? Commit changes
git add .
git commit -m "Add new feature"
```

### Day 2: Testing Integration

```bash
# 1. Open Whakairo container (orchestrator)
cd .devcontainer-whakairo
VS Code → Open in Container

# 2. Start all services
docker-compose up -d

# 3. Test full stack
open http://localhost:3000

# 4. Check system view
open http://localhost:8080

# 5. Verify metrics
cat state/orchestrator.json | jq .genealogy
```

### Day 3: Final Verification

```bash
# 1. Keep both containers open side-by-side

# Terminal 1 (Kaitiaki): Make final tweaks
npm run dev

# Terminal 2 (Whakairo): Watch system
docker-compose ps
docker-compose logs -f

# 3. When satisfied, deploy
cd .devcontainer-whakairo
docker-compose up -d --build
```

---

## Port Reference

### From Whakairo (Full System)

```
Whakairo Orchestrator UI:  http://localhost:8080
Frontend:                  http://localhost:3000 (production-like)
Backend API:               http://localhost:8000
PgAdmin:                   http://localhost:5050
PostgreSQL:                localhost:5432 (internal)
Redis:                     localhost:6379 (internal)
```

### From Kaitiaki (Development)

```
Frontend Vite Dev:         http://localhost:5173 (with HMR)
Backend API:               http://localhost:8000 (when running)
PgAdmin:                   http://localhost:5050
PostgreSQL:                localhost:5432 (internal)
Redis:                     localhost:6379 (internal)
ChromaDB:                  localhost:8000 (internal)
```

---

## Opening Both Containers

### Method 1: VS Code Split (Recommended)

```bash
# Terminal 1: Open Whakairo
cd pack-dashboard/.devcontainer-whakairo
code --folder-uri=vscode-remote/containers/whakairo-orchestrator:/workspace &

# Terminal 2: Open Kaitiaki (new window)
cd pack-dashboard/.devcontainer
code --folder-uri=vscode-remote/containers/kaitiaki-pack-dev:/workspace &

# Now you have both windows open
# - Left: Whakairo for system view
# - Right: Kaitiaki for coding
```

### Method 2: VS Code Split View

```bash
# Within one VS Code window
# 1. Open Whakairo workspace
# 2. Right-click on folder → Open in Split

# Now you can:
# - Edit code in one window
# - Monitor system in another
```

---

## Architecture Diagram

```
YOUR COMPUTER
├─ Browser
│  ├─ http://localhost:3000    (via Whakairo)
│  ├─ http://localhost:5173    (via Kaitiaki)
│  ├─ http://localhost:8080    (Orchestrator)
│  └─ http://localhost:5050    (PgAdmin)
│
├─ VS Code Window 1
│  └─ .devcontainer-whakairo/
│     └─ 🪵 Whakairo Container
│        ├─ docker-compose.yml
│        ├─ All services orchestrated
│        └─ Logs: services.log, orchestrator.log
│
└─ VS Code Window 2
   └─ .devcontainer/
      └─ 🐺 Kaitiaki Container
         ├─ backend/ (develop here)
         ├─ src/ (develop here)
         ├─ supabase/ (database work)
         └─ dev servers (start as needed)
```

---

## Service Emojis (Complete Reference)

### Core Services

| Emoji | Service          | Role                   |
| ----- | ---------------- | ---------------------- |
| 🪵    | Whakairo         | Master Orchestrator    |
| 🐺    | Backend/Kaitiaki | API Guardian, Steward  |
| ⚛️    | Frontend/React   | User Interface         |
| 🐘    | PostgreSQL       | Data Guardian          |
| 🔴    | Redis            | Cache Guardian         |
| 🧠    | ChromaDB         | Vector/Memory Guardian |
| 🎛️    | Orchestrator UI  | Control Panel          |
| 🗄️    | Database         | Data Storage           |
| 🔄    | Cache/Queue      | Process Queue          |

### Development Specific

| Emoji | Meaning               |
| ----- | --------------------- |
| 💻    | Dev server, IDE       |
| 🔧    | Tools, configuration  |
| 📊    | Monitoring, dashboard |
| 🚀    | Deployment, launch    |
| 🐛    | Debugging, issues     |
| ✅    | Ready, complete       |
| ❌    | Error, problem        |

---

## File Structure (Complete)

```
pack-dashboard/
│
├─ 🪵 ORCHESTRATOR CONTAINER
│  └─ .devcontainer-whakairo/
│     ├─ devcontainer.json      # Whakairo config
│     ├─ Dockerfile             # Whakairo image
│     ├─ docker-compose.yml     # All services
│     ├─ setup.sh               # Setup script
│     ├─ README.md              # Orchestrator guide
│     ├─ config/                # Config files
│     ├─ logs/                  # Service logs
│     │  ├─ orchestrator.log
│     │  ├─ services.log
│     │  └─ genealogy.log
│     └─ state/                 # Orchestrator state
│        └─ orchestrator.json   # Metrics + status
│
├─ 🐺 KAITIAKI CONTAINER
│  └─ .devcontainer/
│     ├─ devcontainer.json      # Kaitiaki config
│     ├─ Dockerfile             # Kaitiaki image
│     ├─ docker-compose.yml     # Local services
│     ├─ setup.sh               # Setup script
│     ├─ README.md              # Original readme
│     └─ KAITIAKI_CONTAINER_GUIDE.md  # This container guide
│
├─ 🐺 BACKEND CODE
│  └─ backend/
│     ├─ main.py
│     ├─ kaitiaki/
│     ├─ routers/               # 9 routers now!
│     └─ requirements.txt
│
├─ ⚛️  FRONTEND CODE
│  └─ src/
│     ├─ App.tsx
│     ├─ main.tsx
│     ├─ components/
│     ├─ hooks/
│     └─ lib/
│
├─ 🐘 DATABASE
│  └─ supabase/
│     ├─ schema.sql
│     ├─ seed.sql
│     └─ migrations/
│
├─ 📚 DOCUMENTATION
│  ├─ DUAL_CONTAINER_ARCHITECTURE.md    # This file!
│  ├─ START_HERE_PHASE_6.md
│  ├─ QUICK_START_PHASE_6.md
│  ├─ KUBERNETES_READINESS.md
│  └─ ... (9 Phase 6 docs)
│
└─ 🔧 CONFIG FILES
   ├─ package.json
   ├─ tsconfig.json
   ├─ docker-compose.yml
   ├─ vite.config.ts
   └─ etc.
```

---

## Common Scenarios

### Scenario 1: "I'm adding a new chat history endpoint"

```bash
# 1. Open Kaitiaki
cd .devcontainer
npm run dev  # Keep frontend running

# (or in another terminal in Kaitiaki)
cd backend
python -m uvicorn main:app --reload

# 2. Edit backend/routers/chat_history.py
# 3. Server auto-reloads

# 4. Test endpoint
curl http://localhost:8000/api/chat/...

# 5. Frontend auto-reloads too
# 6. Test end-to-end

# 7. When done, stop dev servers
# 8. Want to verify in "production-like" mode?

# 9. Open Whakairo in another window
cd .devcontainer-whakairo
docker-compose up -d

# 10. Test on http://localhost:3000 (production-like)
```

### Scenario 2: "Need to debug why frontend isn't seeing backend"

```bash
# 1. Open Kaitiaki + Whakairo side-by-side

# In Kaitiaki:
npm run dev

# In Whakairo:
docker-compose logs -f backend

# 2. Make a request from frontend
# 3. See what backend is receiving
# 4. Check CORS settings
# 5. Fix issue
# 6. Test in Whakairo when satisfied
```

### Scenario 3: "Need to verify everything works together"

```bash
# 1. Open Whakairo (full system)
cd .devcontainer-whakairo
docker-compose up -d

# 2. Check all services
docker-compose ps

# 3. Test full flow
open http://localhost:3000
# Try chat → backend → database

# 4. Check metrics
cat state/orchestrator.json | jq .genealogy

# 5. All working? ✅ Ready to deploy!
```

---

## Switching Between Containers

### Quick Switch

```bash
# Currently in Kaitiaki, want to check system?

# Option 1: New VS Code window
code --folder-uri=vscode-remote/containers/whakairo-orchestrator:/workspace

# Option 2: Terminal
docker-compose ps  # If Whakairo is running
docker-compose logs -f  # See logs

# Option 3: Browser
http://localhost:8080  # Orchestrator dashboard
```

---

## Environment Variables

### Whakairo (Orchestrator)

```
WHAKAIRO_HOME=/whakairo
PYTHONUNBUFFERED=1
```

### Kaitiaki (Individual)

```
NODE_ENV=development
POSTGRES_USER=pack_user
POSTGRES_DB=pack_dashboard
DATABASE_URL=postgresql://pack_user:dev@localhost:5432/pack_dashboard
REDIS_URL=redis://:password@localhost:6379/0
CHROMADB_HOST=chromadb
CHROMADB_PORT=8000
```

---

## Troubleshooting

### "Both containers running on same port"

Not possible! Each container is isolated. However:

- Whakairo ports: 8000, 3000, 5432, 6379, 8080
- Kaitiaki ports: 5173, 8000 (when you start it), 5432 (internal)

If conflict: Just use different ports or run one at a time.

### "Need frontend from Whakairo but backend from Kaitiaki"

Not recommended. Use one or the other for consistency:

```bash
# Option 1: Full system (Whakairo)
cd .devcontainer-whakairo && docker-compose up -d

# Option 2: Development (Kaitiaki)
cd .devcontainer && npm run dev + uvicorn main:app
```

### "Containers not communicating"

Ensure they're on same network:

```bash
# In Whakairo
docker network ls
docker network inspect kaitiaki-network

# Check service discovery
docker-compose ps
```

---

## Next Steps

1. **Choose Your Path:**

   - 👨‍💻 **Developing?** → Open 🐺 Kaitiaki
   - 🎛️ **Managing?** → Open 🪵 Whakairo

2. **Read Specific Guides:**

   - Kaitiaki developers: `.devcontainer/KAITIAKI_CONTAINER_GUIDE.md`
   - Orchestrator admins: `.devcontainer-whakairo/README.md`

3. **Start Coding:**

   - Backend: `backend/routers/`
   - Frontend: `src/components/`
   - Database: `supabase/`

4. **When Ready:**
   - Commit in Kaitiaki
   - Test in Whakairo
   - Deploy with confidence

---

## Philosophy

> **Ko te whakairo e whakarite ana i ngā kaitiaki** - _The orchestrator guides the stewards_

- 🪵 **Whakairo** = Big picture, coordination, system health
- 🐺 **Kaitiaki** = Individual responsibility, focused work, personal mastery

Together, they create harmony.

---

**Ready to code?** Pick your container and dive in! 🚀
