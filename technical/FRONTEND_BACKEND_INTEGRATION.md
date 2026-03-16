# FastAPI ↔️ Frontend Integration Guide

## Overview

The FastAPI backend at `http://localhost:8000` serves all backend operations for the Kaitiaki platform. The React frontend communicates via REST API + WebSocket for real-time collaboration.

## Backend Services Running

When the dev container starts, these services are available:

```
✅ FastAPI Backend     http://localhost:8000
✅ PostgreSQL Database http://localhost:5432
✅ pgAdmin Dashboard   http://localhost:5050
✅ Redis Cache        redis://localhost:6379
✅ ChromaDB Vector DB http://localhost:8000 (integrated)
✅ React Frontend     http://localhost:5173
```

## API Client Setup

### In Your React Components

```typescript
// hooks/useKaitiakiAPI.ts
import axios from "axios";

const API_BASE = process.env.REACT_APP_API_URL || "http://localhost:8000/api";

const kaitiakiAPI = axios.create({
  baseURL: API_BASE,
  headers: {
    "Content-Type": "application/json",
    "User-ID": localStorage.getItem("user_id") || "anon",
  },
});

export const useKaitiakiAPI = () => {
  // Whakapapa endpoints
  const searchWhakapapa = async (query: string, type: string = "name") => {
    const response = await kaitiakiAPI.post("/whakapapa/search", {
      user_id: getCurrentUserId(),
      query,
      search_type: type,
    });
    return response.data;
  };

  // Land Court endpoints
  const uploadLandCourtDocument = async (file: File) => {
    const formData = new FormData();
    formData.append("file", file);
    const response = await kaitiakiAPI.post("/land-court/upload", formData);
    return response.data;
  };

  // PDF endpoints
  const summarizePDF = async (file: File) => {
    const formData = new FormData();
    formData.append("file", file);
    const response = await kaitiakiAPI.post(
      "/pdf/summarize-genealogy",
      formData
    );
    return response.data;
  };

  // Language endpoints
  const translateToTeReo = async (
    text: string,
    dialect: string = "standard"
  ) => {
    const response = await kaitiakiAPI.post("/language/translate", {
      user_id: getCurrentUserId(),
      text,
      target_dialect: dialect,
    });
    return response.data;
  };

  // User preferences
  const saveUserPreferences = async (preferences: any) => {
    const response = await kaitiakiAPI.post("/user/preferences", {
      user_id: getCurrentUserId(),
      preferences,
    });
    return response.data;
  };

  // Collaboration endpoints
  const shareGenealogy = async (genealogyId: string, targetUsers: string[]) => {
    const response = await kaitiakiAPI.post("/collab/share-genealogy", {
      user_id: getCurrentUserId(),
      genealogy_id: genealogyId,
      target_users: targetUsers,
    });
    return response.data;
  };

  return {
    searchWhakapapa,
    uploadLandCourtDocument,
    summarizePDF,
    translateToTeReo,
    saveUserPreferences,
    shareGenealogy,
  };
};
```

## Component Examples

### WhakapapaSearch Component

```typescript
// src/components/WhakapapaSearch.tsx
import { useState } from "react";
import { useKaitiakiAPI } from "../hooks/useKaitiakiAPI";

export function WhakapapaSearch() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const api = useKaitiakiAPI();

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const data = await api.searchWhakapapa(query);
      setResults(data.matches);
    } catch (error) {
      console.error("Search failed:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="whakapapa-search">
      <form onSubmit={handleSearch}>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Rapu i ngā tīpuna... (Search ancestors)"
        />
        <button disabled={loading}>
          {loading ? "Rapu ana..." : "Rapu (Search)"}
        </button>
      </form>

      <div className="results">
        {results.map((match: any) => (
          <div key={match.person_id} className="genealogy-match">
            <h3>{match.name}</h3>
            <p>Iwi: {match.iwi}</p>
            <p>Hapū: {match.hapū}</p>
            <p>Confidence: {(match.confidence * 100).toFixed(0)}%</p>
            <p>Tapu Level: {match.tapu_level}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

### UserPreferencesTool Selector

```typescript
// src/components/ToolSelector.tsx
import { useState, useEffect } from "react";
import { useKaitiakiAPI } from "../hooks/useKaitiakiAPI";

export function ToolSelector() {
  const [preferences, setPreferences] = useState({
    llm_provider: "claude",
    pdf_parser: "pdfplumber",
    language: "te-reo",
    data_sources: ["land-court", "research-papers"],
  });
  const [config, setConfig] = useState<any>(null);
  const api = useKaitiakiAPI();

  useEffect(() => {
    // Fetch public config from backend
    fetch("http://localhost:8000/config/public")
      .then((r) => r.json())
      .then(setConfig);
  }, []);

  const handleChange = (field: string, value: any) => {
    setPreferences((prev) => ({ ...prev, [field]: value }));
  };

  const handleSave = async () => {
    await api.saveUserPreferences(preferences);
    alert("Ko ō kupu kua tiakina - Your preferences saved!");
  };

  if (!config) return <div>Loading...</div>;

  return (
    <div className="tool-selector">
      <h2>Tīpakohia ō kupu - Select Your Tools</h2>

      <div className="preference-group">
        <label>LLM Provider</label>
        <select
          value={preferences.llm_provider}
          onChange={(e) => handleChange("llm_provider", e.target.value)}
        >
          {config.llm_providers.map((p: string) => (
            <option key={p} value={p}>
              {p}
            </option>
          ))}
        </select>
      </div>

      <div className="preference-group">
        <label>PDF Parser</label>
        <select
          value={preferences.pdf_parser}
          onChange={(e) => handleChange("pdf_parser", e.target.value)}
        >
          {config.pdf_parsers.map((p: string) => (
            <option key={p} value={p}>
              {p}
            </option>
          ))}
        </select>
      </div>

      <div className="preference-group">
        <label>Language</label>
        <select
          value={preferences.language}
          onChange={(e) => handleChange("language", e.target.value)}
        >
          {config.language_support.map((lang: string) => (
            <option key={lang} value={lang}>
              {lang}
            </option>
          ))}
        </select>
      </div>

      <div className="preference-group">
        <label>Data Sources</label>
        <div className="checkbox-group">
          {config.data_sources.map((source: string) => (
            <label key={source}>
              <input
                type="checkbox"
                checked={preferences.data_sources.includes(source)}
                onChange={(e) => {
                  handleChange(
                    "data_sources",
                    e.target.checked
                      ? [...preferences.data_sources, source]
                      : preferences.data_sources.filter(
                          (s: string) => s !== source
                        )
                  );
                }}
              />
              {source}
            </label>
          ))}
        </div>
      </div>

      <button onClick={handleSave}>Tiaki (Save)</button>
    </div>
  );
}
```

### Document Upload Handler

```typescript
// src/components/DocumentUpload.tsx
import { useKaitiakiAPI } from "../hooks/useKaitiakiAPI";

export function DocumentUpload() {
  const api = useKaitiakiAPI();

  const handleLandCourtUpload = async (file: File) => {
    const result = await api.uploadLandCourtDocument(file);
    console.log("Land Court extraction:", result);
    // Use result.extraction.people_found, .genealogical_relationships, etc.
  };

  const handlePDFUpload = async (file: File) => {
    const result = await api.summarizePDF(file);
    console.log("PDF genealogy:", result);
    // Use result.extracted_genealogy, .te_reo_summary, .whakapapa_matches
  };

  return (
    <div className="document-upload">
      <input
        type="file"
        accept=".pdf,.doc,.docx"
        onChange={(e) => {
          if (e.target.files?.[0]) {
            if (e.target.files[0].name.includes("Land Court")) {
              handleLandCourtUpload(e.target.files[0]);
            } else {
              handlePDFUpload(e.target.files[0]);
            }
          }
        }}
      />
    </div>
  );
}
```

## Environment Variables

### Frontend (.env)

```env
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_SUPABASE_URL=https://[project].supabase.co
REACT_APP_SUPABASE_ANON_KEY=[anonymous-key]
```

### Backend (.env in backend/)

Automatically pulled from Supabase on container startup. Can be overridden locally:

```env
SUPABASE_URL=https://[project].supabase.co
SUPABASE_ANON_KEY=[anonymous-key]
LLM_PROVIDER=claude
LLM_API_KEY=[your-key]
PDF_PARSER=pdfplumber
LANGUAGE=te-reo
MEMORY_ENCRYPTION=true
```

## Testing the Integration

### 1. Check Backend Health

```bash
curl http://localhost:8000/health
```

Response:

```json
{
  "status": "alive",
  "message": "Te hau flows through Kaitiaki backend",
  "kaitiaki": "watching over the pack"
}
```

### 2. Get Public Config

```bash
curl http://localhost:8000/config/public
```

### 3. Test Search API

```bash
curl -X POST http://localhost:8000/api/whakapapa/search \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "test_user",
    "query": "Te Hikuroa",
    "search_type": "name"
  }'
```

### 4. Upload and Parse Document

```bash
curl -X POST http://localhost:8000/api/land-court/upload \
  -F "user_id=test_user" \
  -F "file=@document.pdf"
```

## Real-Time Updates (WebSocket)

Coming soon - for live collaboration:

```typescript
// Hook up WebSocket for multi-user genealogy editing
const ws = new WebSocket("ws://localhost:8000/ws/collab/project_123");

ws.onmessage = (event) => {
  const update = JSON.parse(event.data);
  // Another kaitiaki added/verified genealogy
  console.log("Collaborator action:", update);
};

ws.send(
  JSON.stringify({
    action: "verify_genealogy",
    genealogy_id: "g_123",
    user_id: "user_1",
  })
);
```

## Debugging

### View Backend Logs

```bash
docker logs -f kaitiaki-backend
```

### Access Swagger UI

Open http://localhost:8000/docs to see all available endpoints with testing interface.

### Check Database

```bash
# Access pgAdmin at http://localhost:5050
# Connect to PostgreSQL:
#   Host: postgres
#   Port: 5432
#   Username: kaitiaki
#   Password: kaitiaki_dev
```

### Monitor Redis

```bash
docker exec -it kaitiaki-redis redis-cli
> KEYS *
> GET user_123:preferences
```

## Error Handling

All API calls return structured responses:

```typescript
interface APIResponse<T> {
  status: "success" | "error";
  data?: T;
  message: string;
  timestamp: string;
  user_id?: string;
  error?: string;
}
```

Handle errors consistently:

```typescript
try {
  const result = await api.searchWhakapapa(query);
  // Handle success
} catch (error: any) {
  if (error.response?.status === 500) {
    console.error("Server error:", error.response.data.message);
  } else if (error.response?.status === 404) {
    console.error("Not found:", error.response.data.message);
  } else {
    console.error("Unknown error:", error);
  }
}
```

## Next Steps

1. **Run the full stack:**

   ```bash
   cd /home/kaitiaki/workspace/pack-dashboard
   docker-compose up -d
   npm run dev
   ```

2. **Frontend will be at:** http://localhost:5173

3. **Backend API docs at:** http://localhost:8000/docs

4. **Start integrating components** - Use examples above to wire up genealogy search, document upload, and tool selection.

---

**Philosophy:** Ko au te awa, ko te awa ko au - The backend flows through the frontend. Users control everything. Never the other way around.
