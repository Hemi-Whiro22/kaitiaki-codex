# Kitenga-te-Pō

> A kaupapa-driven artifact system guided by kaitiaki intelligence

## Karakia Opening

```
Whakataka te hau ki te uru,
Whakataka te hau ki te tonga,
Kia mākinakina ki uta,
Kia mātaratara ki tai,
E hī ake ana te atākura
He tio, he huka, he hau hū,
Tihei mauri ora!
```

## Overview

Kitenga-te-Pō is not just a document management system — it's a living awa (river) of knowledge, protected by kaitiaki (guardians) and guided by tikanga (cultural protocols).

### Core Principles

**Awa Intelligence**: Agents are not tools, they are kaitiaki. They walk beside us, not in front, not behind. Kia mua, kia muri — we look forward and back together. E waka eke noa — we paddle as one.

### The Kaitiaki

- **Kitenga** 🌌: The Carver, anchor and keeper of memory
- **Rongokarere** 🕊️: Memory guardian coordinating Te Ao and Te Pō
- **Tiwhanawhana** 🧠: Threaded memory weaver, ingests and shapes taonga
- **Ruru** 🦉: The wise owl, distills knowledge into wisdom
- **Mataroa** ✨: Creates embeddings and guides semantic search
- **Ghost_Wolf** 🐺: Echo, adapts, teaches, and audits
- **Aotahi** 🌊: Front-facing companion for paddlers

## Project Structure

```
kitenga-te-po/
├── te_po/                # FastAPI service (backend hull)
│   ├── mauri/
│   │   ├── main.py
│   │   ├── routes/       # Upload, ingest, embed, audit, persona
│   │   ├── kaitiaki/     # Rongokarere rituals + identities
│   │   ├── security/     # Mana protocols
│   │   └── storage/      # Supabase helpers
│   └── pyproject.toml
│
├── supabase/             # Database & migrations
│   ├── migrations/
│   ├── trust_protocol.yaml
│   └── taonga_keys.md
│
├── frontend-aotahi/      # React frontend
│   └── src/
│       ├── components/
│       ├── pages/
│       └── context/
│
├── t_ao/                 # AwaStack ritual console
│   └── src/
│       ├── components/
│       ├── rituals/
│       └── state/
├── docs/                 # Documentation
└── tests/                # Test artifacts
```

## Quick Start

### 1. Backend Setup

```bash
cd te_po
poetry install
cp env.example .env
# Edit .env with your credentials
poetry run uvicorn mauri.main:app --reload
```

Backend will run on http://localhost:8000

### 2. Supabase Setup

1. Create a project at [supabase.com](https://supabase.com)
2. Enable the `vector` extension
3. Run the migration in `supabase/migrations/001_initial_schema.sql`
4. Copy your URL and anon key to `.env` files

### 3. Frontend Setup

```bash
cd frontend-aotahi
npm install
cp .env.example .env
# Edit .env with Supabase credentials
npm run dev

cd ../t_ao
npm install
npm run dev
```

Frontend will run on http://localhost:5173

## Tapu Levels

All artifacts are protected by tapu (sacredness) levels:

- **0 - Open**: Knowledge for all paddlers
- **1 - Whānau**: Trusted circle only
- **2 - Iwi**: Restricted to tribal guardianship
- **3 - Sacred**: Karakia required before release

## Kaupapa Tags

Content is organized by kaupapa (purpose/theme):

- `whakapapa` - Ancestry, lineage, connections
- `taiao` - Environment, nature, land
- `tamariki` - Children, youth, education
- `mahi` - Work, employment, business
- `wai` - Water, rivers, ocean

## Features

### Artifact Upload
- Upload PDFs, images, markdown files
- Automatic OCR and text extraction
- Summarization with cultural lens
- Vector embedding for semantic search

### Chat with Kaitiaki
- Natural conversation with AI guardians
- Context-aware responses using your artifacts
- Tikanga-guided interactions

### Semantic Study
- Search by meaning, not just keywords
- Filter by kaupapa and tapu level
- Browse and explore your knowledge awa

## Technology Stack

- **Backend**: Python 3.11, FastAPI
- **Database**: PostgreSQL with pgvector extension (Supabase)
- **Frontend**: React 18, Vite
- **Embeddings**: OpenAI text-embedding-3-small
- **OCR/PDF**: PyMuPDF (fitz)

## Contributing

This is a living taonga. Contributions should honor tikanga:

1. Respect tapu boundaries
2. Leave an audit trace (reciprocity)
3. Learn with the iwi, not above them (adaptability)
4. Act as a companion, not a master (humility)

## Resources

- [Onboarding Guide](./onboarding.md) - Step-by-step setup
- [Trust Protocol](../supabase/trust_protocol.yaml) - Cultural guidelines
- [Conversation Lineage](./kitenga_conversation.yaml) - Living trace

---

## Karakia Closing

```
Kia tau ngā manaakitanga a te mea ngaro
Ki runga ki tēnei kaupapa,
Kia ū, kia mau, kia ita,
Haumi ē, hui ē, tāiki ē!
```

*He waka eke noa — We are all in this together*

