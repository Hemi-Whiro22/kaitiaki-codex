# 🐺 Kaitiaki Pack Dashboard - Quick Reference Guide

## 🚀 First Time Setup

```bash
# 1. Open workspace in VS Code
# 2. VS Code detects .devcontainer/devcontainer.json
# 3. Click "Reopen in Container"
# 4. Wait for container build (~3-5 minutes)
# 5. setup.sh runs automatically

# Once setup completes:
npm run dev
# → Opens http://localhost:5173
```

---

## 🎯 What's Where

### Frontend (Browser - http://localhost:5173)

| Component     | File             | Purpose                               |
| ------------- | ---------------- | ------------------------------------- |
| **Layout**    | `App.tsx`        | Two-column design (packs + chat)      |
| **Packs**     | `PacksTable.tsx` | Create & search packs with embeddings |
| **Chat**      | `ChatPanel.tsx`  | Smart chat with memory & LLM          |
| **Ingestion** | `MauriLens.tsx`  | Beautiful knowledge ingestion form    |

### Backend Services (Docker)

| Service        | Port | URL                   | Purpose         |
| -------------- | ---- | --------------------- | --------------- |
| **Frontend**   | 5173 | http://localhost:5173 | Vite dev server |
| **PostgreSQL** | 5432 | localhost:5432        | Vector database |
| **pgAdmin**    | 5050 | http://localhost:5050 | Database UI     |
| **Redis**      | 6379 | localhost:6379        | Cache & queues  |
| **ChromaDB**   | 8000 | http://localhost:8000 | Vector store    |

### Core Libraries

| File                      | Purpose                                    |
| ------------------------- | ------------------------------------------ |
| `lib/embedding.ts`        | SHA-256 deterministic embeddings (384-dim) |
| `lib/llm/orchestrator.ts` | Modular LLM providers (Local/Claude/GPT)   |
| `lib/memory/personal.ts`  | User-scoped memory with localStorage       |
| `lib/supabase.ts`         | Database client                            |

---

## 📋 Common Commands

### Development

```bash
npm run dev          # Start Vite dev server (hot reload)
npm run build        # Build for production
npm run lint         # Check code quality
npm run type-check   # TypeScript validation
npm run preview      # Test production build
```

### Docker Services

```bash
# Terminal aliases (auto-configured)
pack-up              # Start all services
pack-down            # Stop all services
pack-logs            # View service logs (live)
pack-shell           # Connect to PostgreSQL

# Or use docker-compose directly
docker-compose -f .devcontainer/docker-compose.yml ps
docker-compose -f .devcontainer/docker-compose.yml logs -f
docker-compose -f .devcontainer/docker-compose.yml restart
```

---

## 💬 Using ChatPanel (Right Side)

### Features

1. **Model Switcher** - [Local] [Claude] [GPT] buttons at top
2. **Memory Display** - Shows count and top topics at bottom
3. **Mauri Lens** - 🔍 button opens ingestion form
4. **Auto-Remember** - Type "remember" in message to save to memory
5. **Context** - Each response shows relevant memories & packs

### Example Interactions

**Save to Memory:**

```
User: "remember React is my favorite frontend framework"
→ Auto-ingests into personal memory ✓
```

**Ingest with Mauri Lens:**

```
1. Click "🔍 Mauri" button
2. Fill form:
   - Topic: "Machine Learning"
   - Content: "TensorFlow, PyTorch, Keras"
   - Tags: "ml, frameworks"
   - Privacy: Toggle public/private
3. Click Ingest
→ Saved to memory, confirmed with system message ✓
```

**Search Memory:**

```
User: "what ML tools do I know?"
→ Chat searches personal memories
→ Returns: "📌 Machine Learning (similarity: 0.95)"
→ LLM uses as context for response ✓
```

**Switch LLM Model:**

```
1. Click "Claude" button (top right)
2. Button highlights in emerald
3. Next message uses Claude provider
→ Model name shown in message timestamp ✓
```

---

## 📊 Using PacksTable (Left Side)

### Create Pack

```
1. Fill form:
   - Name: "My Research Pack"
   - Description: "All my findings..."
2. Click Create
→ Auto-generates embedding (SHA-256)
→ Stores in PostgreSQL with vector
→ Adds to table
✓
```

### Search Packs

```
1. Type in search box
2. Auto-generates query embedding
3. Queries Supabase: match_packs_by_embedding
4. Returns results sorted by similarity
→ Shows: Pack Name (Similarity %) - Description
✓
```

---

## 🔌 Database Connections

### PostgreSQL (from host terminal)

```bash
# Enter container shell
ssh into dev container or use terminal in VS Code

# Connect to database
psql -h localhost -U pack_user -d pack_dashboard
# Password: dev_password_change_me

# Common queries
SELECT * FROM packs;
SELECT * FROM memory_entries;
SELECT COUNT(*) FROM packs;
```

### PostgreSQL (using pgAdmin UI)

```
1. Open http://localhost:5050
2. Login: admin@awanet.nz / pgadmin_dev_password
3. Connect to server:
   - Host: postgres
   - Port: 5432
   - User: pack_user
   - Password: dev_password_change_me
4. Browse tables and run queries
```

---

## 💾 Data Persistence

### Where Data Lives

**Personal Memories:**

- **Location:** Browser localStorage
- **Key:** `personal_memory_system`
- **Survives:** Page refresh, browser restart
- **Persists:** ✅ Across development sessions

**Packs & Database:**

- **Location:** PostgreSQL (Docker volume)
- **Volume:** `postgres_data_dev`
- **Survives:** Container restart, rebuild
- **Persists:** ✅ Until volume deletion

**Session Data:**

- **Location:** React state (ChatPanel messages)
- **Survives:** ❌ Page refresh
- **Persists:** ❌ (Lost on reload)

### Accessing Persisted Data

**Check localStorage:**

```javascript
// In browser console
JSON.parse(localStorage.getItem("personal_memory_system"));
```

**Export Memories:**

```javascript
// Copy & paste in browser console
copy(
  JSON.stringify(
    JSON.parse(localStorage.getItem("personal_memory_system")),
    null,
    2
  )
);
// Then paste into file
```

**Clear All Data:**

```bash
# Clear memories (browser console)
localStorage.clear()

# Restart database (terminal)
docker-compose -f .devcontainer/docker-compose.yml down -v
docker-compose -f .devcontainer/docker-compose.yml up -d
```

---

## ⚙️ Configuration

### Environment Variables

Located in `.devcontainer/devcontainer.json` under `containerEnv`:

```json
{
  "DATABASE_URL": "postgresql://pack_user:...",
  "REDIS_URL": "redis://:redis_dev_password@...",
  "NODE_ENV": "development"
}
```

### For Real LLM APIs (Optional)

Create `.env.local` in project root:

```env
VITE_OPENAI_API_KEY=sk-...
VITE_CLAUDE_API_KEY=sk-ant-...
VITE_SUPABASE_URL=https://...
VITE_SUPABASE_ANON_KEY=...
```

Then update `orchestrator.ts` to use real API calls.

---

## 🔍 Debugging Tips

### Check Service Health

```bash
docker-compose -f .devcontainer/docker-compose.yml ps
# Shows status of all services
```

### View Logs

```bash
# All services
docker-compose -f .devcontainer/docker-compose.yml logs -f

# Specific service
docker-compose -f .devcontainer/docker-compose.yml logs -f postgres
docker-compose -f .devcontainer/docker-compose.yml logs -f redis
```

### Browser DevTools

```
1. Press F12 in browser
2. Console tab: See any JavaScript errors
3. Network tab: Check API calls
4. Application tab: View localStorage
5. Performance tab: Profile performance
```

### React DevTools

- Extension: React Developer Tools (Chrome/Firefox)
- Shows component tree, props, state
- Great for debugging ChatPanel state

---

## 📚 File Structure

```
pack-dashboard/
├── .devcontainer/              # Dev container setup
│   ├── Dockerfile              # Container image
│   ├── devcontainer.json       # VS Code config
│   ├── docker-compose.yml      # Backend services
│   ├── setup.sh                # Auto-init script
│   ├── init-db.sh              # Database init
│   └── README-DEVCONTAINER.md  # Full docs
│
├── src/
│   ├── components/
│   │   ├── App.tsx             # Layout wrapper
│   │   ├── PacksTable.tsx      # Pack management
│   │   ├── ChatPanel.tsx       # Main chat interface
│   │   └── MauriLens.tsx       # Ingestion form
│   │
│   ├── lib/
│   │   ├── embedding.ts        # Vector generation
│   │   ├── supabase.ts         # DB client
│   │   ├── llm/
│   │   │   └── orchestrator.ts # LLM providers
│   │   └── memory/
│   │       └── personal.ts     # Memory system
│   │
│   ├── types/
│   │   └── types.ts            # TypeScript types
│   │
│   ├── App.tsx                 # Root component
│   └── main.tsx                # Entry point
│
├── supabase/
│   ├── schema.sql              # Database schema
│   └── seed.sql                # Sample data
│
├── mcp-server/                 # Model Context Protocol automation
│   └── src/
│       └── index.ts            # MCP tools
│
├── public/
│   └── index.html              # Static HTML
│
├── package.json                # Dependencies
├── tsconfig.json               # TypeScript config
├── vite.config.ts              # Vite config
├── docker-compose.yml          # Main compose (prod)
├── TEST_REPORT.md              # Full test results
└── README.md                   # Main documentation
```

---

## 🐛 Troubleshooting Quick Fixes

| Problem                             | Solution                                             |
| ----------------------------------- | ---------------------------------------------------- |
| **Services not starting**           | `pack-down && pack-up`                               |
| **Port already in use**             | Change port in docker-compose.yml                    |
| **PostgreSQL won't connect**        | Wait 30s, check `docker-compose ps`                  |
| **Vite not reloading**              | Restart dev server: `npm run dev`                    |
| **Memory not persisting**           | Check localStorage: `localStorage.key`               |
| **Component not rendering**         | Check browser console (F12) for errors               |
| **Hot reload slow**                 | Vite cache issue, restart with `npm run dev`         |
| **Docker socket permission denied** | Rebuild container: Cmd+Shift+P → "Rebuild Container" |

---

## 📞 Getting Help

1. **Check TEST_REPORT.md** - Full system test results
2. **Check .devcontainer/README-DEVCONTAINER.md** - Dev container docs
3. **Browser console (F12)** - JavaScript errors
4. **Docker logs** - `pack-logs` command
5. **Database UI** - pgAdmin at http://localhost:5050

---

## 🎯 Next Steps

### To Build Backend

1. Create `api/` folder for FastAPI/Express
2. Configure in docker-compose
3. Update LLM orchestrator to call API endpoints

### To Add Authentication

1. Set up Supabase Auth
2. Create login component
3. Update RLS policies for security

### To Deploy

1. Build Docker image: `docker build -t pack-dashboard .`
2. Push to registry (Docker Hub, ECR, etc.)
3. Deploy with docker-compose or Kubernetes

---

## 🌊 Remember

> "Te hau flows through the dev container!"
>
> Kaitiaki watches over your code. The pack protects the people.

---

**Quick Reference Version:** 1.0  
**Last Updated:** October 21, 2025  
**Created by:** GitHub Copilot
