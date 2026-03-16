# Rongokarere Backend Batch Trace

## 🐺 Mode: Batch
Rongokarere reads from `backend_manifest.yaml`, carves each route, embeds the code, and indexes to Supabase.

## ✅ Completed Routes
- /upload
- /ingest/{id}
- /summarize/{id}
- /embed/{id}
- /chat/{thread}

## 🔁 Flow
1. Manifest parsed
2. Code carved
3. Embedding generated
4. Supabase indexed
5. Audit logged

## 📜 Next Step
Activate frontend flows in AwaNetStack and test each route.
