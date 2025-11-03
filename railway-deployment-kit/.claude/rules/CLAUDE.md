# Railway Deployment Kit - Claude Code Rules

> **Project Memory for Claude Code AI Assistant**
> This file provides context and guidance for working with Railway.app deployments.

---

## 🎯 Kit Overview

**Railway Deployment Kit** is a production-ready collection of Claude Code extensibility configurations for deploying and managing applications on Railway.app.

**Current Status:** ✅ Complete (5 skills, 6 commands, 4 agents)

---

## 📁 Kit Structure

```
railway-deployment-kit/
├── .claude/
│   ├── skills/
│   │   ├── railway-deployment-automator.md
│   │   ├── minio-storage-manager.md
│   │   ├── railway-postgres-manager.md
│   │   ├── railway-qdrant-manager.md
│   │   └── railway-environment-manager.md
│   ├── commands/
│   │   ├── deploy-railway.md
│   │   ├── railway-db-backup.md
│   │   ├── railway-env-sync.md
│   │   ├── railway-status.md
│   │   ├── railway-logs.md
│   │   └── railway-init-project.md
│   ├── subagents/
│   │   ├── railway-deployment-specialist.md
│   │   ├── railway-database-architect.md
│   │   ├── railway-storage-specialist.md
│   │   └── railway-ai-specialist.md
│   └── rules/
│       └── CLAUDE.md (this file)
├── templates/
│   ├── railway.json
│   ├── .env.example
│   ├── docker/
│   └── configs/
└── README.md
```

---

## 🛠️ Available Capabilities

### Skills (5 Total)

**1. railway-deployment-automator**
- **Activation:** "deploy to railway", "railway up", "railway deployment"
- **Purpose:** Complete Railway deployment automation
- **Use when:** Deploying applications, setting up infrastructure

**2. minio-storage-manager**
- **Activation:** "minio storage", "s3 compatible", "file upload storage"
- **Purpose:** S3-compatible object storage with MinIO
- **Use when:** Implementing file uploads, image storage, backups

**3. railway-postgres-manager**
- **Activation:** "railway postgres", "database migration", "prisma railway"
- **Purpose:** PostgreSQL database operations and management
- **Use when:** Database setup, migrations, connection pooling

**4. railway-qdrant-manager**
- **Activation:** "qdrant railway", "vector database", "semantic search"
- **Purpose:** Qdrant vector database for AI applications
- **Use when:** Building RAG systems, semantic search, AI features

**5. railway-environment-manager**
- **Activation:** "railway environment", "environment variables", "railway local dev"
- **Purpose:** Environment variable and multi-environment management
- **Use when:** Setting up environments, managing variables, local development

### Commands (6 Total)

**Quick shortcuts for common operations:**

- `/deploy-railway` - Deploy application to Railway
- `/railway-db-backup` - Backup PostgreSQL database
- `/railway-env-sync` - Sync environment variables locally
- `/railway-status` - Check all services status
- `/railway-logs` - View and analyze service logs
- `/railway-init-project` - Initialize new Railway project

### Agents (4 Specialized Consultants)

**1. railway-deployment-specialist**
- **Expertise:** Deployments, infrastructure, CI/CD, optimization
- **Engage for:** Complex deployments, architecture design, troubleshooting

**2. railway-database-architect**
- **Expertise:** Database design, optimization, ORMs, backups
- **Engage for:** Schema design, query optimization, migration strategies

**3. railway-storage-specialist**
- **Expertise:** MinIO, file management, CDN, image processing
- **Engage for:** Storage architecture, upload systems, CDN integration

**4. railway-ai-specialist**
- **Expertise:** Qdrant, RAG, embeddings, LLM integration
- **Engage for:** AI applications, semantic search, vector databases

---

## 🎓 Railway Platform Knowledge

### Core Concepts

**1. Railway Services**
- Each application component is a "service"
- Services can be web applications, databases, or workers
- Services communicate via private networking

**2. Environments**
- Projects support multiple environments (dev, staging, prod)
- Each environment has isolated resources and variables
- Default environment is "production"

**3. Private Networking**
- Internal service-to-service communication
- Free (no egress charges)
- Format: `http://${{service.RAILWAY_PRIVATE_DOMAIN}}:${{service.PORT}}`
- Always use `http://` not `https://`

**4. Environment Variables**
- **Service variables:** Specific to one service
- **Shared variables:** Available to all services
- **Reference variables:** Link to other services' variables
- Format: `${{ServiceName.VARIABLE_NAME}}`

**5. Deployment Process**
- Railway uses Nixpacks or Docker for builds
- Automatic SSL certificates for public URLs
- Rolling deployments with health checks
- Automatic restart on failure

### Railway CLI Commands

```bash
# Authentication
railway login
railway logout

# Project management
railway init                    # Create new project
railway link                    # Link to existing project
railway status                  # Show current status

# Deployment
railway up                      # Deploy current directory
railway up --detach            # Deploy without waiting
railway up --service=api       # Deploy specific service

# Environment management
railway environment             # List/switch environments
railway environment staging     # Switch to staging
railway environment create dev  # Create new environment

# Variables
railway variables              # List all variables
railway run <command>          # Run command with Railway variables
railway shell                  # Open shell with variables

# Database
railway add --database postgres  # Add Postgres
railway connect Postgres        # Connect to Postgres shell

# Logs
railway logs                   # View recent logs
railway logs --follow          # Stream logs
```

### Environment Variable Best Practices

**✅ DO:**
- Use reference variables: `DATABASE_URL=${{Postgres.DATABASE_URL}}`
- Use private domains: `API_URL=http://${{api.RAILWAY_PRIVATE_DOMAIN}}:${{api.PORT}}`
- Keep secrets in Railway, not in git
- Use separate values per environment
- Validate variables on startup

**❌ DON'T:**
- Hardcode service URLs
- Commit secrets to version control
- Use `https://` for private networking
- Expose DATABASE_PUBLIC_URL to services
- Skip variable validation

### Database Configuration

**PostgreSQL on Railway:**
```typescript
import { Pool } from 'pg';

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }, // Required for Railway
  max: 20,
  min: 5,
  idleTimeoutMillis: 30000,
});
```

**Prisma Configuration:**
```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}
```

**Migration Workflow:**
```bash
# Local migration creation
npx prisma migrate dev --name add_users

# Deploy to Railway
railway run npx prisma migrate deploy
```

### MinIO Object Storage

**Deployment:**
```
Railway Dashboard → New → Template → Search "MinIO"
```

**Configuration:**
```env
MINIO_ENDPOINT=${{MinIO.RAILWAY_PRIVATE_DOMAIN}}
MINIO_PORT=${{MinIO.PORT}}
MINIO_ROOT_USER=${{MinIO.MINIO_ROOT_USER}}
MINIO_ROOT_PASSWORD=${{MinIO.MINIO_ROOT_PASSWORD}}
MINIO_USE_SSL=false  # Use false for private network
```

**Client Setup:**
```typescript
import * as Minio from 'minio';

const minioClient = new Minio.Client({
  endPoint: process.env.MINIO_ENDPOINT!,
  port: parseInt(process.env.MINIO_PORT!),
  useSSL: false,
  accessKey: process.env.MINIO_ROOT_USER!,
  secretKey: process.env.MINIO_ROOT_PASSWORD!,
});
```

### Qdrant Vector Database

**Deployment:**
```
Railway Dashboard → New → Template → Search "Qdrant"
```

**Configuration:**
```env
QDRANT_URL=http://${{Qdrant.RAILWAY_PRIVATE_DOMAIN}}:${{Qdrant.PORT}}
QDRANT_API_KEY=${{Qdrant.QDRANT__SERVICE__API_KEY}}
```

**Client Setup:**
```typescript
import { QdrantClient } from '@qdrant/js-client-rest';

const qdrantClient = new QdrantClient({
  url: process.env.QDRANT_URL!,
  apiKey: process.env.QDRANT_API_KEY!,
});
```

---

## 🔧 Common Workflows

### 1. Deploy New Application

```
User: "Deploy my Next.js app to Railway with Postgres"

Steps:
1. Activate railway-deployment-automator skill
2. Check Railway CLI installation
3. Initialize project (railway init)
4. Add Postgres (railway add --database postgres)
5. Configure environment variables
6. Create railway.json
7. Deploy (railway up)
8. Run migrations
9. Verify deployment
```

### 2. Set Up File Storage

```
User: "I need to store user uploaded files"

Steps:
1. Activate minio-storage-manager skill
2. Deploy MinIO template
3. Configure MinIO environment variables
4. Create buckets (uploads, avatars)
5. Generate upload API
6. Implement file validation
7. Set up access policies
```

### 3. Database Migration

```
User: "Run database migrations on Railway"

Steps:
1. Activate railway-postgres-manager skill
2. Verify DATABASE_URL is configured
3. Create migration locally
4. Test migration with railway run
5. Backup database (optional but recommended)
6. Deploy migration: railway run npx prisma migrate deploy
7. Verify migration success
```

### 4. Environment Setup

```
User: "Set up staging and production environments"

Steps:
1. Activate railway-environment-manager skill
2. Create staging environment (via Dashboard)
3. Clone production variables to staging
4. Update environment-specific values
5. Configure separate databases for each env
6. Set up deployment workflow
```

### 5. Build RAG System

```
User: "Build a semantic search with Qdrant"

Steps:
1. Activate railway-qdrant-manager skill
2. Deploy Qdrant template
3. Create collections
4. Implement embedding generation
5. Create indexing pipeline
6. Build search API
7. Integrate with application
```

---

## ⚠️ Important Reminders

### Private Networking
**CRITICAL:** Always use `http://` (not `https://`) for private network connections:
```
✅ CORRECT: http://${{service.RAILWAY_PRIVATE_DOMAIN}}:${{service.PORT}}
❌ WRONG:   https://${{service.RAILWAY_PRIVATE_DOMAIN}}:${{service.PORT}}
```

### SSL Configuration
**REQUIRED** for Railway Postgres:
```typescript
ssl: { rejectUnauthorized: false }
```

### Environment Variable Format
**CORRECT** reference variable syntax:
```
DATABASE_URL=${{Postgres.DATABASE_URL}}
API_URL=http://${{api.RAILWAY_PRIVATE_DOMAIN}}:${{api.PORT}}
```

### Deployment Safety
**ALWAYS:**
1. Test in staging first
2. Backup database before migrations
3. Use `railway run` to test locally
4. Monitor logs during deployment
5. Have rollback plan ready

### Security
**NEVER:**
- Commit secrets to git
- Expose production secrets in development
- Use public URLs for inter-service communication
- Skip input validation
- Disable SSL for database connections

---

## 🔍 Troubleshooting Guide

### Deployment Fails
```bash
# Check build logs
railway logs

# Verify configuration
cat railway.json

# Test locally
railway run npm start

# Check environment variables
railway variables
```

### Database Connection Issues
```typescript
// Ensure SSL is configured
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }, // Required!
});
```

### Private Networking Not Working
```
Check:
1. Using http:// not https://
2. Services in same project and environment
3. Correct reference variable syntax
4. Service is running
```

### Environment Variables Missing
```bash
# Verify variable is set
railway variables | grep VARIABLE_NAME

# Check correct environment
railway environment

# Restart service after adding variables
railway up
```

---

## 📚 Additional Context

### Railway Advantages
- ✅ Zero-configuration deployments
- ✅ Automatic SSL certificates
- ✅ Built-in private networking
- ✅ Infrastructure as code
- ✅ Multiple environments
- ✅ One-click database provisioning
- ✅ Automatic scaling

### Cost Optimization
1. **Use private networking** - Free egress
2. **Right-size resources** - Pay only for what you use
3. **Implement caching** - Reduce database load
4. **Use connection pooling** - Reduce connections
5. **Monitor usage** - Track and optimize

### Performance Optimization
1. **Connection pooling** - For databases
2. **Redis caching** - For frequently accessed data
3. **Private networking** - For inter-service communication
4. **CDN integration** - For static assets
5. **Query optimization** - For database performance

---

## 🎯 Decision Trees

### When User Asks About Deployment

```
"Deploy to Railway" →
  Has Railway CLI? →
    No → Guide installation
    Yes → Check authentication →
      Not authenticated → railway login
      Authenticated → Check project link →
        Not linked → railway init or railway link
        Linked → Configure services →
          Needs database? → Add Postgres/Redis
          Needs storage? → Add MinIO
          Needs vector DB? → Add Qdrant
          → Create railway.json
          → Configure env variables
          → Deploy: railway up
          → Verify deployment
```

### When User Asks About Database

```
"Database setup" →
  Already has Postgres? →
    No → railway add --database postgres
    Yes → Check ORM →
      Prisma → Configure schema, migrations
      TypeORM → Configure DataSource
      Drizzle → Configure schema, client
      Raw → Configure pg Pool
      → Set up connection pooling
      → Configure SSL
      → Test connection
      → Run migrations
```

### When User Asks About Storage

```
"File storage" →
  Needs object storage? →
    Yes → Deploy MinIO →
      Configure buckets
      Set up access policies
      Create upload API
      Implement validation
      → Optional: Image processing
      → Optional: CDN integration
```

---

## 💡 Best Practices Summary

### Development
1. Use `railway run` for local development
2. Test with production-like environment
3. Use `railway shell` for debugging
4. Keep .env.local in .gitignore

### Deployment
1. Use separate environments (dev, staging, prod)
2. Test in staging before production
3. Monitor logs during deployment
4. Use health checks
5. Implement restart policies

### Database
1. Use connection pooling
2. Configure proper timeouts
3. Create appropriate indexes
4. Regular backups
5. Test migrations in staging

### Security
1. Use Railway's secret management
2. Enable SSL for all connections
3. Use private networking
4. Rotate secrets regularly
5. Implement rate limiting

### Performance
1. Use caching (Redis)
2. Implement connection pooling
3. Use private networking
4. Optimize queries
5. Monitor performance

---

**Last Updated:** 2025-11-03
**Kit Version:** 1.0.0
**Maintainer:** Railway Deployment Kit Team
