# Self-Hosting Guide: Pack Dashboard

## Why Self-Host?

- **Data Sovereignty**: Your data stays on your server, 100% yours
- **No Supabase Lock-In**: Run locally, on your own hardware or VPS
- **Free**: No subscription, just PostgreSQL + Node.js
- **Community-Friendly**: Perfect for NGOs, cooperatives, libraries, grassroots orgs

---

## Quick Start (Docker)

### Prerequisites

- Docker & Docker Compose installed
- ~2GB disk space for postgres_data volume

### 1. Start PostgreSQL + pgAdmin

```bash
# Copy env example
cp .env.example .env.local

# Start services (creates postgres with schema + seed data)
docker-compose up -d

# Wait for postgres to be healthy
docker-compose ps
```

### 2. Verify Database

```bash
# Connect to postgres
psql postgresql://pack_user:dev_password_change_me@localhost:5432/pack_dashboard

# Check tables
\dt public.*

# List extensions
\dx
```

Should see:

- `pgcrypto` extension ✓
- `vector` extension ✓
- `packs` table with columns: id, name, description, embedding, metadata, created_at ✓

### 3. Update App to Use Local Postgres

Create `.env.local`:

```env
# Local self-hosted PostgreSQL (no Supabase)
VITE_SUPABASE_URL=http://localhost:3001
VITE_SUPABASE_ANON_KEY=local-dev-key-no-auth

# Or use direct PostgreSQL connection (advanced)
DATABASE_URL=postgresql://pack_user:dev_password_change_me@localhost:5432/pack_dashboard
```

### 4. Run App

```bash
npm install
npm run dev

# App runs at http://localhost:5173
```

---

## Production Self-Hosting

### Option A: VPS (DigitalOcean, Linode, etc.)

```bash
# 1. Rent a VPS ($5-20/month for 1GB RAM)
# 2. SSH in
ssh root@your_vps_ip

# 3. Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 4. Clone pack-dashboard repo
git clone https://github.com/awanet/pack-dashboard.git
cd pack-dashboard

# 5. Set production passwords
cat > .env.production << EOF
POSTGRES_PASSWORD=your_secure_password_here
PGADMIN_PASSWORD=your_pgadmin_password_here
EOF

# 6. Start services
docker-compose up -d

# 7. Access app via your VPS IP or domain
# http://your_vps_ip:3001 (Supabase-compatible proxy)
# or http://your_vps_ip:5173 (dev server)
```

### Option B: Kubernetes (k8s) + Helm

For large deployments (optional):

```bash
# Install PostgreSQL via Helm
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install postgres bitnami/postgresql \
  --set auth.postgresPassword=secure_password \
  --set global.postgresql.auth.database=pack_dashboard

# Deploy pack-dashboard pod
kubectl apply -f k8s/deployment.yaml
```

---

## Docker Compose Reference

### Services Included

| Service  | Port | Purpose                     | Password                |
| -------- | ---- | --------------------------- | ----------------------- |
| postgres | 5432 | PostgreSQL DB with pgvector | `POSTGRES_PASSWORD` env |
| pgadmin  | 5050 | Web UI for database admin   | `PGADMIN_PASSWORD` env  |

### Environment Variables

```env
# .env.local or .env.production
POSTGRES_PASSWORD=change_me
PGADMIN_PASSWORD=change_me
```

### Common Commands

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f postgres

# Connect to postgres
docker-compose exec postgres psql -U pack_user -d pack_dashboard

# Backup database
docker-compose exec postgres pg_dump -U pack_user pack_dashboard > backup.sql

# Restore database
cat backup.sql | docker-compose exec -T postgres psql -U pack_user pack_dashboard
```

---

## Migrating from Supabase to Self-Hosted

### 1. Export Data from Supabase

```bash
# Via Supabase CLI
supabase db pull

# Or via psql
pg_dump "postgresql://user:password@project.supabase.co:5432/postgres" > supabase_backup.sql
```

### 2. Import into Local PostgreSQL

```bash
# Copy backup to container
docker cp supabase_backup.sql $(docker-compose ps -q postgres):/tmp/

# Restore
docker-compose exec postgres psql -U pack_user pack_dashboard < /tmp/supabase_backup.sql
```

### 3. Update `.env.local`

Switch from Supabase to local:

```env
# Before (Supabase)
VITE_SUPABASE_URL=https://project.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGc...

# After (Local)
VITE_SUPABASE_URL=http://localhost:3001
VITE_SUPABASE_ANON_KEY=local-dev
```

---

## Security Best Practices

### 1. Change Default Passwords

```bash
# Don't use dev_password_change_me in production!
openssl rand -base64 32
# Use output as POSTGRES_PASSWORD
```

### 2. Use Reverse Proxy (nginx)

```nginx
# /etc/nginx/sites-available/pack-dashboard
server {
    listen 80;
    server_name your.domain.com;

    location / {
        proxy_pass http://localhost:3001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 3. Enable SSL (Let's Encrypt)

```bash
sudo apt install certbot nginx-certbot
sudo certbot --nginx -d your.domain.com
```

### 4. Firewall Rules

```bash
# Only allow SSH, HTTP, HTTPS
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw deny 5432  # Hide postgres from internet
```

---

## Troubleshooting

### "postgres connection refused"

```bash
# Check if postgres is running
docker-compose ps postgres

# View logs
docker-compose logs postgres

# Restart
docker-compose restart postgres
```

### "pgvector extension not found"

```bash
# Verify pgvector image
docker-compose exec postgres psql -U pack_user -d pack_dashboard -c "CREATE EXTENSION vector;"
```

### "packs table already exists"

```bash
# Drop and recreate
docker-compose exec postgres psql -U pack_user -d pack_dashboard -c "DROP TABLE IF EXISTS packs CASCADE;"
docker-compose exec postgres psql -U pack_user -d pack_dashboard < supabase/schema.sql
```

---

## Community Hosting

### For NGOs, Libraries, Cooperatives

If you're a grassroots org (non-profit, community co-op, library):

- **Free tier**: use our hosted version (Supabase)
- **Self-host free**: use docker-compose locally
- **Community server**: reach out to license@awanet.nz for subsidized VPS hosting

We want to empower communities, not lock them in. 🌱

---

## License Note

Self-hosting pack-dashboard is **AGPL-3.0**:

- ✅ Personal/non-profit/grassroots: free, no restrictions
- ⚠️ Commercial deployment as a service: must open-source changes OR buy commercial license
- See `LICENSE` and `OWNERSHIP.md` for details

---

## Next Steps

1. **Start locally**: `docker-compose up -d`
2. **Run app**: `npm run dev`
3. **Create packs** with semantic search (no external API)
4. **Backup regularly**: `docker-compose exec postgres pg_dump ... > backup.sql`
5. **Deploy to VPS** when ready (same docker-compose.yml works everywhere)

**Questions?** See `SUPABASE_SETUP.md` (Supabase hosting) or reach out: community@awanet.nz

---

Keep it sovereign. 🚀
