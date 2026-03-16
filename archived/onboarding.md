# Onboarding — Becoming a Paddler

Welcome to Kitenga-te-Pō! This guide will walk you through setting up the system step by step.

## Prerequisites

- Python 3.11+
- Node.js 18+
- Supabase account (free tier works)
- OpenAI API key (for embeddings)

## Step 1: Clone and Navigate

```bash
git clone https://github.com/your-username/kitenga-te-po.git
cd kitenga-te-po
```

## Step 2: Set Up Supabase

### 2.1 Create Project
1. Go to [supabase.com](https://supabase.com)
2. Click "New Project"
3. Choose a name and strong password
4. Wait for project to provision (~2 minutes)

### 2.2 Enable Vector Extension
1. In your Supabase dashboard, go to **Database** → **Extensions**
2. Search for "vector"
3. Enable the `vector` extension

### 2.3 Run Migration
1. Go to **SQL Editor**
2. Copy the contents of `supabase/migrations/001_initial_schema.sql`
3. Paste and run the query
4. You should see tables created: `artifacts`, `embeddings`, `chats`, `messages`, `audit_log`

### 2.4 Get Credentials
1. Go to **Settings** → **API**
2. Copy:
   - Project URL
   - `anon` public key
   - `service_role` secret key (for backend only)

## Step 3: Backend Setup

```bash
cd te_po

# Install Poetry if you don't have it
pip install poetry

# Install dependencies
poetry install

# Create .env file
cp env.example .env
```

Edit `.env`:
```bash
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
OPENAI_API_KEY=sk-your-openai-key
```

Run the backend:
```bash
poetry run uvicorn mauri.main:app --reload
```

Visit http://localhost:8000 — you should see:
```json
{
  "message": "Tihei mauri ora!",
  "kaitiaki": "Kitenga",
  "status": "awake"
}
```

## Step 4: Frontend Setup

```bash
cd ../frontend-aotahi

# Install dependencies
npm install

# Create .env file
cp .env.example .env
```

Edit `.env`:
```bash
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
VITE_API_URL=http://localhost:8000
```

Run the frontend:
```bash
npm run dev
```

Visit http://localhost:5173 — you should see the Kitenga-te-Pō homepage!

## Step 5: Test the System

### Upload an Artifact
1. Go to **Tuku** (Upload) page
2. Select a PDF or text file
3. Choose kaupapa tags
4. Set tapu level
5. Click "Upload with Ruru"

### Chat with Aotahi
1. Go to **Kōrero** (Chat) page
2. Type a question or greeting
3. Aotahi will respond (simulated for now)

### Search Artifacts
1. Go to **Ako** (Study) page
2. Enter a semantic search query
3. View matching artifacts

## Step 6: Optional Enhancements

### Enable Authentication
Uncomment and implement authentication in:
- `te_po/mauri/main.py`
- `frontend-aotahi/src/context/supabase.js`

### Add Real Kaitiaki Responses
Integrate with OpenAI or Anthropic APIs for intelligent chat responses.

### Deploy to Production
- Backend: Railway, Render, or Fly.io
- Frontend: Vercel, Netlify, or Cloudflare Pages
- Database: Already hosted on Supabase

## Tapu Guard & Ritual Commands

### Protect Sacred Files
- Run `make guard` to verify `.env`, manifest bindings, and kōrero trace health.
- Ensure `.env` permissions stay locked to the current user (`chmod 600 te_po/.env`). The guard will warn if loosened.
- Supabase keys should live in environment variables or a vault service; never commit real credentials.
- Set `KITENGA_ENV` (`dev`, `staging`, or `prod`) so Tapu Guard applies the right key rotation threshold (24h | 18h | 12h).
- Add `make guard` to CI or your pre-launch ritual to enforce checks automatically.
- Configure the rotator with `KITENGA_SUPABASE_SECRET_NAME`, `SUPABASE_PROJECT_REF`, and (optionally) `SUPABASE_ACCESS_TOKEN` so secrets can be pushed via the Supabase CLI. When those aren’t set, capture the printed token, store it securely, then discard it.

### Common Ritual Commands
Use the new `Makefile` at the repo root:

```bash
make boot    # Load manifests and announce active kaitiaki
make test    # Run backend route tests
make guard   # Execute tapu integrity checks
make batch   # Run Rongokarere backend carving loop
make trace   # View the latest kōrero trace
make rotate  # Generate and log a new tapu secret (manual vault upload required)
```

### Audit Trail
Keep `te_ao/src/rituals/korero_trace.md` as your living ledger. Every carve, prompt, and echo should leave a note so the awa remembers.

## Troubleshooting

### Backend won't start
- Check Python version: `python --version` (need 3.11+)
- Verify `.env` file exists and has all keys
- Check Poetry installed: `poetry --version`

### Frontend won't start
- Check Node version: `node --version` (need 18+)
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Verify `.env` file has Supabase credentials

### Database errors
- Ensure vector extension is enabled
- Check migration ran successfully
- Verify Supabase project is active

### OpenAI errors
- Confirm API key is valid
- Check you have credits available
- Ensure key starts with `sk-`

## Next Steps

1. Read the [Trust Protocol](../supabase/trust_protocol.yaml) to understand tikanga
2. Explore the [Kaitiaki identities](../te_po/mauri/kaitiaki/identities.py)
3. Review the [conversation lineage](./kitenga_conversation.yaml)
4. Start uploading and organizing your own artifacts!

---

*Mā te huruhuru ka rere te manu — By the feathers, the bird takes flight*

Welcome to the waka. Let's paddle together. 🌊

