# 🚀 Backend Deployment Checklist

## Phase 1: Local Development ✅ (READY NOW)

### Infrastructure

- [x] FastAPI app with async architecture (main.py)
- [x] 6 modular routers created
- [x] Supabase config loader (pulls env on startup)
- [x] Error handling & logging
- [x] CORS middleware configured
- [x] Health check endpoint
- [x] Requirements.txt with all dependencies
- [x] Docker support (in docker-compose.yml)

### Testing Locally

- [ ] Run `uvicorn main:app --reload`
- [ ] Visit http://localhost:8000/docs
- [ ] Test `/health` endpoint
- [ ] Test `/config/public` endpoint
- [ ] Try a genealogy search via API
- [ ] Verify Supabase connection works

### Documentation

- [x] BACKEND_ARCHITECTURE.md (comprehensive)
- [x] QUICKSTART.md (quick reference)
- [x] FRONTEND_BACKEND_INTEGRATION.md (integration examples)
- [x] Code comments throughout

## Phase 2: Service Implementation (NEXT)

### Land Court Parser Service

- [ ] Create `services/land_court_parser.py`
- [ ] Implement document upload handling
- [ ] Extract genealogies from PDFs using regex/NLP
- [ ] Cross-reference with whakapapa system
- [ ] Add confidence scoring
- [ ] Handle multiple document formats

**Estimated:** 3-4 hours

### PDF Genealogy Extraction

- [ ] Create `services/pdf_genealogy_extractor.py`
- [ ] Integrate with LLM (Claude/GPT based on user preference)
- [ ] Extract key genealogical fields:
  - [ ] Names
  - [ ] Dates
  - [ ] Places
  - [ ] Relationships
- [ ] Summarize in te reo Māori
- [ ] Suggest whakapapa matches

**Estimated:** 2-3 hours

### Te Reo Language Service

- [ ] Create `services/te_reo_language.py`
- [ ] Implement macron support (ā, ē, ī, ō, ū)
- [ ] Add dictionary lookup
- [ ] Implement language detection
- [ ] Support dialect variants
- [ ] Create learning system based on genealogy

**Estimated:** 2-3 hours

### User Memory Encryption

- [ ] Create `services/encryption.py`
- [ ] Implement end-to-end encryption
- [ ] Add key management
- [ ] Create user_memory table migration
- [ ] Add encryption to user_preferences router

**Estimated:** 1-2 hours

### Collaboration Engine

- [ ] Implement genealogy verification workflow
- [ ] Add project creation/management
- [ ] Implement genealogy merging algorithm
- [ ] Add activity logging
- [ ] WebSocket support for real-time updates

**Estimated:** 3-4 hours

**Total Phase 2: ~12-16 hours**

## Phase 3: Frontend Integration (AFTER SERVICES)

### Tool Selector Component

- [ ] Create `src/components/ToolSelector.tsx`
- [ ] Let users select:
  - [ ] LLM provider (claude/gpt/local)
  - [ ] PDF parser (pypdf/pdfplumber/cultural)
  - [ ] Language (te-reo/english/adaptive)
  - [ ] Data sources
- [ ] Save preferences to backend
- [ ] Show available tools from `/config/public`

**Estimated:** 2 hours

### Document Upload Component

- [ ] Create `src/components/DocumentUpload.tsx`
- [ ] Handle Land Court documents
- [ ] Handle research PDFs
- [ ] Show extraction progress
- [ ] Display results (genealogies found)
- [ ] Suggest matches

**Estimated:** 2-3 hours

### Genealogy Search UI

- [ ] Enhance `src/components/WhakapapaSearch.tsx`
- [ ] Display search results with confidence
- [ ] Show genealogical networks
- [ ] Support filtering by tapu level (if user has permission)
- [ ] Add genealogy detail view
- [ ] Show evidence sources

**Estimated:** 2-3 hours

### Collaboration UI

- [ ] Create `src/components/CollaborationPanel.tsx`
- [ ] Show current projects
- [ ] Invite collaborators
- [ ] View activity log
- [ ] Verify genealogies together
- [ ] Merge genealogies

**Estimated:** 3-4 hours

**Total Phase 3: ~9-13 hours**

## Phase 4: Testing & Optimization

### Unit Tests

- [ ] Test whakapapa search logic
- [ ] Test Land Court parser
- [ ] Test genealogy matching
- [ ] Test te reo translation
- [ ] Test collaboration workflows

**Estimated:** 4-5 hours

### Integration Tests

- [ ] Test full upload -> extraction -> match flow
- [ ] Test multi-user collaboration
- [ ] Test document parsing with real files
- [ ] Test encryption/decryption

**Estimated:** 3-4 hours

### Performance Testing

- [ ] Load test genealogy searches
- [ ] Test concurrent uploads
- [ ] Measure vector search performance
- [ ] Optimize slow queries

**Estimated:** 2-3 hours

### Security Audit

- [ ] Verify RLS policies work
- [ ] Test encryption key rotation
- [ ] Verify user scoping
- [ ] Check API rate limiting
- [ ] Validate CORS settings

**Estimated:** 2-3 hours

**Total Phase 4: ~11-15 hours**

## Phase 5: Production Deployment

### Supabase Setup

- [ ] Configure Supabase Edge Functions (optional)
- [ ] Set up environment secrets
- [ ] Configure RLS policies correctly
- [ ] Set up backups
- [ ] Set up monitoring/alerts

**Estimated:** 2-3 hours

### Docker Optimization

- [ ] Optimize Dockerfile for production
- [ ] Add health check to docker-compose
- [ ] Set memory limits
- [ ] Configure logging
- [ ] Add resource monitoring

**Estimated:** 1-2 hours

### Deployment

- [ ] Choose deployment platform (Railway, Render, Fly.io, custom VPS)
- [ ] Set up CI/CD pipeline (GitHub Actions)
- [ ] Deploy to staging
- [ ] Performance testing in staging
- [ ] Deploy to production
- [ ] Set up monitoring

**Estimated:** 3-4 hours

### Documentation for Deployment

- [ ] Write deployment guide
- [ ] Document environment variables
- [ ] Document scaling strategy
- [ ] Document backup/recovery procedures

**Estimated:** 1-2 hours

**Total Phase 5: ~7-11 hours**

## Overall Timeline

| Phase     | Component              | Hours           | Status   |
| --------- | ---------------------- | --------------- | -------- |
| 1         | Backend Architecture   | ✅ Done         | Complete |
| 2         | Service Implementation | 12-16h          | ⏳ Next  |
| 3         | Frontend Integration   | 9-13h           | Pending  |
| 4         | Testing & Optimization | 11-15h          | Pending  |
| 5         | Production Deployment  | 7-11h           | Pending  |
| **Total** |                        | **46-65 hours** |          |

## Critical Path (Minimum for MVP)

For a working MVP:

1. **Land Court Parser** (core value - turning records into genealogies)
2. **Genealogy Search + Cross-reference** (connecting people)
3. **Tool Selector UI** (let users pick their tools)
4. **Basic Frontend Components** (upload, search, results)

**Estimated MVP time: 15-20 hours**

## Success Metrics

### Backend Readiness

- ✅ API responds to all 6 router endpoints
- ✅ Database queries return genealogies
- ✅ Supabase config loads on startup
- ✅ User preferences save/retrieve
- ✅ Memory encryption works
- ✅ Concurrent requests handled safely

### User Experience

- ✅ Upload Land Court document -> see genealogies within seconds
- ✅ Search for ancestor -> find matches with confidence scores
- ✅ Share genealogy with whānau -> they can verify
- ✅ Merge genealogies -> resolve conflicts collaboratively
- ✅ Remember preferences -> system learns what user wants

### Data Integrity

- ✅ No unauthorized data access (RLS enforced)
- ✅ Tapu data protected (encryption at rest)
- ✅ All genealogies verified before publication
- ✅ Activity logged for audit trail

## Known Limitations (Current)

- ❌ Land Court parser not yet implemented (endpoint returns mock data)
- ❌ PDF extraction using LLM not yet implemented
- ❌ Te reo translation service not yet implemented
- ❌ WebSocket for real-time collaboration not yet added
- ❌ Genealogy matching algorithm not yet optimized
- ❌ No ML model for genealogy confidence scoring

## Dependencies Ready

All Python packages specified in `requirements.txt`:

```
✅ FastAPI & Uvicorn (async framework)
✅ Pydantic (data validation)
✅ Supabase SDK (database + auth)
✅ SQLAlchemy (ORM)
✅ PyPDF & PDFPlumber (PDF parsing)
✅ Anthropic & OpenAI SDKs (LLM integration)
✅ Sentence Transformers (embeddings)
✅ ChromaDB (vector database)
✅ NLTK & Spacy (NLP)
✅ Redis (caching)
```

## Running Backend Right Now

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Backend ready at http://localhost:8000
# API docs at http://localhost:8000/docs
```

## Next Immediate Task

**Priority 1: Land Court Document Parser**

This is the core differentiator - turning colonial records into genealogical evidence:

1. Research Land Court document format
2. Create document parser module
3. Extract genealogical information
4. Test with sample documents
5. Integrate with search endpoint

**Owner:** (assign)
**Timeline:** 3-4 hours
**Deliverable:** `/api/land-court/upload` returns parsed genealogies

---

**Status:** 🟢 Ready for Phase 2 implementation

**Questions?** Review `BACKEND_ARCHITECTURE.md` or test endpoints in Swagger UI
