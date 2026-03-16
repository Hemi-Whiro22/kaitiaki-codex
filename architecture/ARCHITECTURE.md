# 🐺 Kaitiaki Pack Dashboard - System Architecture

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          VS CODE DEV CONTAINER                              │
│                      (Docker-in-Docker Enabled)                             │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                    FRONTEND (Vite Dev Server)                       │   │
│  │  ┌─────────────────┐                                               │   │
│  │  │  Browser:5173   │                                               │   │
│  │  ├─ React 18.3     │                                               │   │
│  │  ├─ Tailwind CSS   │                                               │   │
│  │  ├─ Hot Reload ✨  │                                               │   │
│  │  └─ localhost:5173 │                                               │   │
│  │                                                                     │   │
│  │  Components:                                                        │   │
│  │  ├─ App.tsx (Layout)                                              │   │
│  │  ├─ PacksTable (Left column)                                      │   │
│  │  ├─ ChatPanel (Right column)                                      │   │
│  │  └─ MauriLens (Overlay)                                           │   │
│  │                                                                     │   │
│  │  Libraries:                                                         │   │
│  │  ├─ embedding.ts (SHA-256 vectors)                                │   │
│  │  ├─ llm/orchestrator.ts (Modular LLM)                            │   │
│  │  └─ memory/personal.ts (User memory)                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│           │                                                                  │
│           │ HTTP + WebSocket                                               │
│           ↓                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    BACKEND SERVICES (Docker)                       │   │
│  │                    Network: pack-dev (172.28.0.0/16)               │   │
│  │                                                                     │   │
│  │  ┌─────────────────────────────────────────────────────────────┐   │   │
│  │  │  PostgreSQL 16 + pgvector (port 5432)                      │   │   │
│  │  ├─ Tables: packs, memory_entries, user_profiles             │   │   │
│  │  ├─ Extensions: pgvector, uuid-ossp                          │   │   │
│  │  ├─ Indexes: IVFFlat on packs.embedding                      │   │   │
│  │  ├─ Health checks: pg_isready                                │   │   │
│  │  └─ Volume: postgres_data_dev (persistent)                  │   │   │
│  │                                                                 │   │   │
│  │  ┌─ pgAdmin (port 5050) ─────────────────────────────────┐   │   │   │
│  │  │ UI for database management & query execution          │   │   │   │
│  │  └─────────────────────────────────────────────────────────┘   │   │   │
│  │                                                                 │   │   │
│  │  ┌─ Redis 7 (port 6379) ────────────────────────────────────┐   │   │   │
│  │  │ Cache, session store, job queue                          │   │   │   │
│  │  └─────────────────────────────────────────────────────────┘   │   │   │
│  │                                                                 │   │   │
│  │  ┌─ ChromaDB (port 8000) ────────────────────────────────────┐   │   │   │
│  │  │ Alternative vector embedding store                        │   │   │   │
│  │  └─────────────────────────────────────────────────────────┘   │   │   │
│  │                                                                 │   │   │
│  └─────────────────────────────────────────────────────────────────┘   │   │
│                                                                          │   │
│  Docker Socket: /var/run/docker.sock (mounted for DinD)               │   │
│  ┌──────────────────────────────────────────────────────────────────┐ │   │
│  │ Can run containers from within dev container                   │ │   │
│  │ docker ps, docker-compose up, etc. work normally              │ │   │
│  └──────────────────────────────────────────────────────────────────┘ │   │
│                                                                          │   │
└──────────────────────────────────────────────────────────────────────────┘   │
│  VS Code Extensions: Docker, Python, ESLint, Prettier, Copilot, etc.
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Frontend Component Architecture

```
App.tsx (Two-column layout)
│
├─ PacksTable (Left Column)
│  ├─ Create Pack Form
│  │  ├─ Input: name, description
│  │  ├─ generateEmbeddingFromText()
│  │  └─ supabase.insert() → PostgreSQL
│  │
│  └─ Search Results
│     ├─ generateEmbeddingFromText(query)
│     ├─ supabase.rpc(match_packs_by_embedding)
│     └─ Display with similarity scores
│
└─ ChatPanel (Right Column)
   ├─ Header
   │  ├─ Title + Subtitle
   │  ├─ Mauri Lens Button (🔍)
   │  └─ Model Switcher Buttons
   │     ├─ [Local]
   │     ├─ [Claude]
   │     └─ [GPT]
   │
   ├─ Message History
   │  ├─ User Messages (right-aligned)
   │  └─ Assistant Messages (left-aligned)
   │     └─ With context bubbles (📌 Memory, 📦 Pack)
   │
   ├─ MauriLens Overlay (when open)
   │  ├─ Topic input
   │  ├─ Content textarea
   │  ├─ Tags input
   │  ├─ Public/Private toggle
   │  ├─ Preview pane
   │  └─ Submit button
   │
   └─ Message Input
      ├─ Text input (auto-remember on "remember" keyword)
      ├─ Submit button
      └─ Memory Stats
         ├─ Count
         ├─ Top topics
         └─ Clear button
```

---

## Data Flow Routes

### Route 1: Create & Search Packs

```
User Action: Click "Create Pack"
     ↓
PacksTable.handleCreatePack()
     ↓
Validate form: { name, description }
     ↓
generateEmbeddingFromText(description)
  (SHA-256 hash → 384-dim vector)
     ↓
supabase.insert("packs", {
  name,
  description,
  embedding: vector384
})
     ↓
PostgreSQL INSERT
     ↓
IVFFlat Index Updated (automatic)
     ↓
UI: Pack added to table ✅
```

---

### Route 2: Memory Ingestion via Mauri Lens

```
User Action: Click "🔍 Mauri" button
     ↓
MauriLens overlay opens
     ↓
Fill form:
  topic: string
  content: string
  tags: string[]
  isPublic: boolean
     ↓
User clicks "Ingest"
     ↓
ChatPanel.handleMauriIngest()
  ├─ generateEmbeddingFromText(content)
  ├─ memoryManager.addMemory(
  │    userId: "kaitiaki",
  │    topic,
  │    content,
  │    embedding,
  │    isPublic
  │  )
  └─ localStorage update
     ↓
UI: System message displays
UI: Overlay closes ✅
```

---

### Route 3: Chat with Context Enrichment

```
User types: "search ML frameworks"
     ↓
ChatPanel.handleSubmit()
     ↓
Create user message object
     ↓
findContext(input):
  ├─ generateEmbeddingFromText("search ML frameworks")
  ├─ memoryManager.searchUserMemories()
  │  ├─ Search localStorage
  │  ├─ Cosine similarity > 0.6
  │  └─ Sort by relevance
  ├─ supabase.rpc("match_packs_by_embedding")
  │  ├─ Query vector index
  │  ├─ Return top matches
  │  └─ Format results
  └─ Combine & deduplicate
     ↓
llmOrchestrator.generateResponse(input, context)
  ├─ Get current provider
  ├─ Add system message with context
  └─ Generate response (Local/Claude/GPT)
     ↓
Display message with context
  ├─ User message
  ├─ Assistant message + model name
  ├─ Context bubbles (📌 Memory, 📦 Pack)
  └─ Timestamp ✅
```

---

### Route 4: Auto-Remember on Keyword

```
User types: "remember React is awesome"
     ↓
ChatPanel.handleSubmit()
  ├─ Normal chat flow (Route 3)
  └─ Input includes "remember" keyword
     ↓
Automatic memory ingestion:
  ├─ Extract topic from input
  │  (remove "remember", "store", "save", "add")
  ├─ generateEmbeddingFromText(input)
  ├─ memoryManager.addMemory(
  │    userId: "kaitiaki",
  │    topic: extracted,
  │    content: input,
  │    embedding,
  │    isPublic: false
  │  )
  └─ Saved to localStorage ✅
```

---

### Route 5: LLM Provider Switching

```
User clicks [Claude] button
     ↓
ChatPanel state: setCurrentModel("claude")
     ↓
Button highlight changes to emerald
     ↓
User sends message
     ↓
ChatPanel.handleSubmit()
  ├─ llmOrchestrator.switchProvider("claude")
  ├─ llmOrchestrator.getCurrentProvider()
  │  └─ Returns ClaudeProvider
  └─ generateResponse() uses Claude
     ↓
Response generated by Claude
     ↓
Message displays with model: "claude-3-sonnet-20240229"
     ↓
✅ Provider switched for this message
```

---

## Backend Service Architecture

```
Docker Network: pack-dev (172.28.0.0/16)

┌─ PostgreSQL:5432 ─────────────────────────────────┐
│  Tables:                                           │
│  ├─ packs                                         │
│  │  ├─ id (uuid)                                 │
│  │  ├─ name (text)                               │
│  │  ├─ description (text)                        │
│  │  ├─ embedding (vector, 384-dim)               │
│  │  └─ timestamps                                │
│  │                                                │
│  ├─ memory_entries                               │
│  │  ├─ id (uuid)                                 │
│  │  ├─ user_id (text)                            │
│  │  ├─ topic (text)                              │
│  │  ├─ content (text)                            │
│  │  ├─ embedding (vector, 384-dim)               │
│  │  ├─ frequency (int)                           │
│  │  ├─ is_public (boolean)                       │
│  │  └─ timestamps                                │
│  │                                                │
│  ├─ user_profiles                                │
│  │  ├─ user_id (text)                            │
│  │  ├─ name (text)                               │
│  │  ├─ role (text: 'user' | 'orchestrator')      │
│  │  └─ timestamps                                │
│  │                                                │
│  Indexes:                                         │
│  ├─ IVFFlat on packs.embedding                  │
│  ├─ B-tree on timestamps                        │
│  └─ B-tree on user_id                           │
│                                                   │
│  Extensions:                                      │
│  ├─ pgvector (vector operations)                 │
│  ├─ uuid-ossp (uuid generation)                  │
│  └─ pg_stat_statements (performance)             │
└────────────────────────────────────────────────────┘

┌─ pgAdmin:5050 ────────────────────────────────────┐
│  Web UI for database management                   │
│  ├─ Query editor                                 │
│  ├─ Table browser                                │
│  ├─ Performance monitoring                       │
│  └─ Backup/restore tools                         │
└────────────────────────────────────────────────────┘

┌─ Redis:6379 ──────────────────────────────────────┐
│  In-memory cache & session store                  │
│  ├─ Session persistence                          │
│  ├─ Cache layer                                  │
│  ├─ Job queue (future)                           │
│  └─ Real-time subscriptions (future)              │
└────────────────────────────────────────────────────┘

┌─ ChromaDB:8000 ───────────────────────────────────┐
│  Alternative vector embedding store               │
│  ├─ REST API interface                           │
│  ├─ Vector collection storage                    │
│  └─ Metadata filtering                           │
└────────────────────────────────────────────────────┘
```

---

## Library Architecture

### embedding.ts

```
generateEmbeddingFromText(text: string)
├─ UTF-8 encode text
├─ SHA-256 hash (Web Crypto API)
├─ Normalize to [0, 1] range
├─ Expand to 384 dimensions
└─ Return Float32Array
   (Deterministic: same input = same output)
```

### llm/orchestrator.ts

```
LLMProvider (interface)
├─ ClaudeProvider
│  ├─ model: "claude-3-sonnet-20240229"
│  ├─ generateResponse(prompt, context)
│  └─ Stub: returns formatted string
├─ GPTProvider
│  ├─ model: "gpt-4-turbo"
│  ├─ generateResponse(prompt, context)
│  └─ Stub: returns formatted string
└─ LocalProvider
   ├─ model: "local-fallback"
   ├─ generateResponse(prompt, context)
   └─ Rule-based: detects "search", "remember", etc.

LLMOrchestrator (singleton)
├─ switchProvider(name)
├─ getCurrentProvider()
├─ getAvailableProviders()
└─ generateResponse(prompt, context)
```

### memory/personal.ts

```
UserProfile
├─ userId: string
├─ name: string
├─ role: "user" | "orchestrator"
└─ createdAt: Date

MemoryEntry
├─ id: string
├─ userId: string
├─ topic: string
├─ content: string
├─ embedding: number[]
├─ frequency: number (incremented on search)
├─ isPublic: boolean
└─ timestamps

PersonalMemoryManager (singleton)
├─ registerUser(userId, name, role)
├─ addMemory(userId, topic, content, embedding, isPublic)
├─ getUserMemories(userId)
├─ searchUserMemories(userId, query, similarity, embedding)
├─ getAllAccessibleMemories(orchestratorId)
├─ clearUserMemories(userId)
└─ Storage: localStorage["personal_memory_system"]
```

---

## Development Workflow

```
1. Open VS Code
   ↓
2. "Reopen in Container"
   ↓
3. Dev container builds:
   ├─ Dockerfile compiled
   ├─ Node 20 + Python 3.11 + Docker CLI
   ├─ Git configured
   └─ Extensions installed
   ↓
4. postCreateCommand: setup.sh runs:
   ├─ docker-compose up -d (starts services)
   ├─ Waits for health checks
   ├─ npm ci (installs dependencies)
   └─ Displays connection details
   ↓
5. npm run dev
   ├─ Vite dev server starts (port 5173)
   ├─ Hot reload active
   └─ Browser opens automatically
   ↓
6. Development:
   ├─ Edit components (hot reload)
   ├─ Use npm aliases (pack-logs, pack-shell)
   ├─ Test LLM switching
   ├─ Ingest memories
   ├─ Create packs
   └─ Chat with context
   ↓
7. Commit to git:
   ├─ Husky pre-commit (secret scanning)
   ├─ ESLint check
   └─ TypeScript validation
```

---

## Deployment Strategy (Future)

```
Development:
└─ VS Code Dev Container
   └─ Local Docker Compose

Staging:
├─ Build Docker image
├─ Tag with version
└─ Push to registry

Production:
├─ Deploy image
├─ Run docker-compose
├─ Configure Kubernetes (future)
└─ Setup monitoring + logging
```

---

## Security Architecture

```
Data Flow Security:
├─ Frontend ←→ Backend (Docker network)
├─ Embeddings: Deterministic (no secret key)
├─ Memories: localStorage (client-side, not synced)
├─ Packs: PostgreSQL (RLS policies to implement)
└─ LLM: API keys in .env (not committed)

Privacy:
├─ Personal memories: Private by default
├─ Public flag: Only public memories shared with orchestrator
├─ User-scoped: Each user's own memory store
└─ Orchestrator: Cannot access private memories

Future (production):
├─ User authentication (Supabase Auth)
├─ Row-level security (RLS)
├─ Encryption at rest
├─ TLS for transit
└─ Audit logging
```

---

## Performance Characteristics

| Operation            | Time   | Notes                            |
| -------------------- | ------ | -------------------------------- |
| Embedding generation | ~5ms   | SHA-256 hashing                  |
| IVFFlat search       | <100ms | 1M vectors, tuned with lists=100 |
| Memory search        | <10ms  | 100 entries, in-memory           |
| Cosine similarity    | <1ms   | 384-dim vectors                  |
| Message render       | <50ms  | React + Tailwind                 |
| Hot reload           | <100ms | Vite HMR                         |
| Build time           | 1.62s  | Full TypeScript + Vite build     |

---

## Scalability Considerations

```
Current (Development):
├─ localStorage: ~5MB limit
├─ PostgreSQL: Single instance
├─ IVFFlat: Up to 10M vectors
└─ Suitable for: 1-10 users

Near-term (Production):
├─ Supabase RLS: User isolation
├─ Redis: Distributed cache
├─ ChromaDB: Distributed vectors
└─ Suitable for: 100-1K users

Long-term (Enterprise):
├─ Elasticsearch: Full-text search
├─ Weaviate: Distributed vectors
├─ PostgreSQL replication: HA
├─ Kubernetes: Auto-scaling
└─ Suitable for: 1M+ users
```

---

**Architecture Document** | Kaitiaki Pack Dashboard | October 21, 2025

🐺 Te hau flows through the architecture! 🌊
