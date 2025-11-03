# Railway Deployment Kit

> **Production-Ready Railway.app Deployment Configuration for Claude Code**
>
> Complete toolkit for deploying and managing applications on Railway.app with PostgreSQL, MinIO, Qdrant, and comprehensive automation.

[![Railway](https://img.shields.io/badge/Railway-Ready-success)](https://railway.app)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Extensibility-blue)](https://docs.claude.com/en/docs/claude-code/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🚀 Overview

The **Railway Deployment Kit** is a comprehensive collection of Claude Code skills, commands, and agents specifically designed for deploying and managing applications on Railway.app. It provides production-ready configurations for common Railway services including PostgreSQL, Redis, MinIO object storage, and Qdrant vector databases.

### What's Included

- **5 Production Skills** - Automated capabilities for Railway operations
- **6 Slash Commands** - Quick workflow shortcuts
- **4 Specialized Agents** - Expert consultants for complex scenarios
- **Complete Templates** - Ready-to-use configuration files
- **Best Practices** - Security, performance, and cost optimization

---

## 📦 Contents

### Skills (5)

1. **railway-deployment-automator** - Complete deployment automation
2. **minio-storage-manager** - S3-compatible object storage management
3. **railway-postgres-manager** - PostgreSQL database operations
4. **railway-qdrant-manager** - Vector database for AI applications
5. **railway-environment-manager** - Environment variable & multi-env management

### Commands (6)

1. **deploy-railway** - Deploy application to Railway
2. **railway-db-backup** - Backup PostgreSQL database
3. **railway-env-sync** - Sync environment variables locally
4. **railway-status** - Check all services status
5. **railway-logs** - View and analyze service logs
6. **railway-init-project** - Initialize new Railway project

### Agents (4)

1. **railway-deployment-specialist** - Deployment & infrastructure expert
2. **railway-database-architect** - Database design & optimization specialist
3. **railway-storage-specialist** - MinIO & object storage expert
4. **railway-ai-specialist** - AI/ML & vector database consultant

---

## 🎯 Quick Start

### 1. Install the Kit

```bash
# Copy to your project
cp -r railway-deployment-kit/.claude /path/to/your/project/

# Or symlink for updates
ln -s $(pwd)/railway-deployment-kit/.claude /path/to/your/project/.claude
```

### 2. Install Railway CLI

```bash
# macOS
brew install railway

# npm
npm i -g @railway/cli

# Verify installation
railway --version
```

### 3. Authenticate with Railway

```bash
railway login
```

### 4. Initialize Your Project

Use Claude Code with the initialization command:

```
/railway-init-project
```

This will guide you through:
- Project creation
- Environment setup
- Database provisioning
- Service configuration
- Initial deployment

---

## 💡 Use Cases

### Deploy Next.js App with Postgres

```bash
# Initialize Railway project
railway init

# Add Postgres database
railway add --database postgres

# Configure environment variables (done automatically)
# Deploy
railway up
```

### Set Up Object Storage (MinIO)

```
Ask Claude Code: "Set up MinIO storage for file uploads"
```

The `minio-storage-manager` skill will:
- Deploy MinIO on Railway
- Configure buckets
- Set up access policies
- Provide integration code

### Build RAG System with Qdrant

```
Ask Claude Code: "Set up a RAG system with Qdrant and OpenAI"
```

The `railway-qdrant-manager` and `railway-ai-specialist` will:
- Deploy Qdrant vector database
- Create collections
- Implement RAG pipeline
- Provide complete AI integration

### Multi-Environment Deployment

```bash
# Create staging environment
/railway-init-project

# Deploy to staging
railway environment staging
railway up

# Deploy to production
railway environment production
railway up
```

---

## 🛠️ Detailed Guides

### Railway Deployment Skill

**Activation:**
- "deploy to railway"
- "railway deployment"
- "configure railway project"

**Capabilities:**
- Project initialization and linking
- Environment configuration
- Database setup (Postgres, Redis)
- Private networking configuration
- CI/CD integration
- Deployment verification

**Example:**
```
User: "Deploy my Express API to Railway with Postgres"

Claude Code will:
1. Check Railway CLI installation
2. Initialize/link project
3. Add Postgres database
4. Configure environment variables
5. Create railway.json
6. Deploy application
7. Run migrations
8. Verify deployment
```

### MinIO Storage Management

**Activation:**
- "minio storage"
- "s3 compatible storage"
- "file upload storage"

**Capabilities:**
- MinIO deployment on Railway
- Bucket creation and management
- File upload/download APIs
- Presigned URL generation
- Image processing pipelines
- Access control and security

**Example:**
```
User: "I need to store user uploaded images"

Claude Code will:
1. Deploy MinIO on Railway
2. Create 'uploads' and 'avatars' buckets
3. Generate upload API endpoints
4. Implement image optimization
5. Set up CDN integration
6. Configure security policies
```

### PostgreSQL Database Management

**Activation:**
- "railway postgres"
- "database migration"
- "prisma railway"

**Capabilities:**
- Database provisioning
- ORM integration (Prisma, TypeORM, Drizzle)
- Migration management
- Connection pooling
- Backup and recovery
- Performance optimization

**Example:**
```
User: "Set up Prisma with Railway Postgres"

Claude Code will:
1. Add Postgres to project
2. Configure DATABASE_URL
3. Create Prisma schema
4. Generate migrations
5. Deploy migrations to Railway
6. Set up connection pooling
7. Create backup scripts
```

### Qdrant Vector Database

**Activation:**
- "qdrant railway"
- "vector database"
- "semantic search"

**Capabilities:**
- Qdrant deployment
- Collection management
- Vector operations
- Similarity search
- RAG system implementation
- OpenAI/LangChain integration

**Example:**
```
User: "Build a semantic search for my documentation"

Claude Code will:
1. Deploy Qdrant on Railway
2. Create 'documents' collection
3. Implement chunking strategy
4. Generate embeddings with OpenAI
5. Create search API
6. Build RAG query system
```

### Environment Management

**Activation:**
- "railway environment"
- "environment variables"
- "railway local development"

**Capabilities:**
- Multi-environment setup
- Variable management
- Reference variables
- Local development sync
- Security best practices

**Example:**
```
User: "Set up staging and production environments"

Claude Code will:
1. Create environments
2. Configure environment-specific variables
3. Set up private networking
4. Configure shared variables
5. Provide local development workflow
```

---

## 📖 Specialized Agents

### Railway Deployment Specialist

**When to use:** Complex deployments, architecture design, troubleshooting

**Expertise:**
- Zero-downtime deployments
- Multi-service orchestration
- Performance optimization
- Cost reduction
- Security hardening
- CI/CD pipeline design

**Example engagement:**
```
User: "We're migrating from Heroku to Railway. Help design our infrastructure."

Agent will provide:
- Migration strategy
- Service architecture
- Database migration plan
- Environment configuration
- CI/CD setup
- Monitoring and alerting
- Cost optimization recommendations
```

### Railway Database Architect

**When to use:** Database design, optimization, complex queries

**Expertise:**
- Schema design
- Query optimization
- Index strategies
- Connection pooling
- Backup strategies
- ORM best practices

### Railway Storage Specialist

**When to use:** File storage, image processing, CDN setup

**Expertise:**
- MinIO deployment
- Bucket architecture
- Upload/download optimization
- Image processing
- CDN integration
- Cost optimization

### Railway AI Specialist

**When to use:** AI/ML applications, RAG systems, vector search

**Expertise:**
- Qdrant deployment
- Embedding strategies
- RAG architecture
- LLM integration
- Cost optimization
- Production AI patterns

---

## 🔧 Configuration Templates

### railway.json

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS",
    "buildCommand": "npm run build"
  },
  "deploy": {
    "startCommand": "npm start",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### Environment Variables Template

```env
# Environment
ENVIRONMENT=production
NODE_ENV=production

# Server
PORT=3000

# Database (private network)
DATABASE_URL=${{Postgres.DATABASE_URL}}
DATABASE_POOL_MIN=2
DATABASE_POOL_MAX=10

# Redis Cache
REDIS_URL=${{Redis.REDIS_URL}}

# MinIO Storage
MINIO_ENDPOINT=${{MinIO.RAILWAY_PRIVATE_DOMAIN}}
MINIO_PORT=${{MinIO.PORT}}
MINIO_ROOT_USER=${{MinIO.MINIO_ROOT_USER}}
MINIO_ROOT_PASSWORD=${{MinIO.MINIO_ROOT_PASSWORD}}

# Qdrant Vector DB
QDRANT_URL=http://${{Qdrant.RAILWAY_PRIVATE_DOMAIN}}:${{Qdrant.PORT}}
QDRANT_API_KEY=${{Qdrant.QDRANT__SERVICE__API_KEY}}

# External APIs
OPENAI_API_KEY=sk-...
STRIPE_SECRET_KEY=sk_live_...

# Internal Services (private network)
API_URL=http://${{api.RAILWAY_PRIVATE_DOMAIN}}:${{api.PORT}}
WORKER_URL=http://${{worker.RAILWAY_PRIVATE_DOMAIN}}:${{worker.PORT}}
```

### Docker Configuration (Multi-stage)

```dockerfile
# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY --from=builder /app/dist ./dist
EXPOSE 3000
CMD ["npm", "start"]
```

---

## 🏗️ Architecture Patterns

### Small Application

```
┌──────────────┐
│   Next.js    │
│  (Frontend)  │
└──────┬───────┘
       │
       ▼
┌──────────────┐     ┌──────────────┐
│   Express    │────▶│  PostgreSQL  │
│     API      │     └──────────────┘
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Redis     │
└──────────────┘
```

### Medium Application

```
┌──────────────┐
│   Next.js    │
└──────┬───────┘
       │
       ▼
┌──────────────┐     ┌──────────────┐
│     API      │────▶│  PostgreSQL  │
│   Gateway    │     └──────────────┘
└──────┬───────┘
       │              ┌──────────────┐
       ├─────────────▶│    Redis     │
       │              └──────────────┘
       │
       ▼              ┌──────────────┐
┌──────────────┐────▶│    MinIO     │
│    Worker    │     └──────────────┘
└──────────────┘
```

### Large Application (Microservices)

```
┌─────────┐  ┌─────────┐  ┌─────────┐
│Frontend │  │  Admin  │  │  Mobile │
└────┬────┘  └────┬────┘  └────┬────┘
     │            │            │
     └────────────┼────────────┘
                  │
          ┌───────▼────────┐
          │  API Gateway   │
          └───────┬────────┘
                  │
      ┌───────────┼───────────┐
      │           │           │
      ▼           ▼           ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│   User   │ │  Order   │ │   Auth   │
│ Service  │ │ Service  │ │ Service  │
└────┬─────┘ └────┬─────┘ └────┬─────┘
     │            │            │
     ▼            ▼            ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│Postgres  │ │Postgres  │ │  Redis   │
│ (Users)  │ │ (Orders) │ │          │
└──────────┘ └──────────┘ └──────────┘
                                │
                    ┌───────────┼───────────┐
                    │           │           │
                    ▼           ▼           ▼
              ┌──────────┐ ┌──────────┐ ┌──────────┐
              │  MinIO   │ │  Qdrant  │ │  Worker  │
              └──────────┘ └──────────┘ └──────────┘
```

---

## 🔒 Security Best Practices

### Environment Variables
- ✅ Use Railway's secret management
- ✅ Never commit secrets to git
- ✅ Rotate secrets regularly
- ✅ Use separate secrets per environment
- ❌ Never expose secrets in client-side code

### Private Networking
- ✅ Use private domains for inter-service communication
- ✅ Format: `http://${{service.RAILWAY_PRIVATE_DOMAIN}}:${{service.PORT}}`
- ✅ Use http:// (not https://) for private network
- ✅ Reduces costs (no egress fees)
- ✅ Improves security and performance

### Database Security
- ✅ Enable SSL for all database connections
- ✅ Use connection pooling
- ✅ Implement query timeouts
- ✅ Regular backups (automated)
- ✅ Use least privilege database users

### API Security
- ✅ Implement rate limiting
- ✅ Use API keys for service-to-service auth
- ✅ Validate all inputs
- ✅ Implement CORS properly
- ✅ Use HTTPS for all public endpoints

---

## 💰 Cost Optimization

### Private Networking
```
Using private networking = $0 egress fees
Using public URLs = $0.10/GB egress
```

**Savings:** Up to 100% on inter-service communication costs

### Connection Pooling
```
Without pooling: 100+ database connections
With pooling: 5-20 database connections
```

**Savings:** Reduces resource usage and costs

### Caching Strategy
```
Without caching: 1000 database queries/sec
With Redis: 50 database queries/sec
```

**Savings:** Reduces database load and improves performance

### Resource Right-Sizing
```
Over-provisioned: $50/month per service
Right-sized: $20/month per service
```

**Savings:** 60% cost reduction per service

---

## 📊 Monitoring & Observability

### Built-in Monitoring
- Railway Dashboard metrics
- Service logs via `railway logs`
- Deployment history
- Resource usage tracking

### External Monitoring
```typescript
// Sentry for error tracking
import * as Sentry from '@sentry/node';

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.ENVIRONMENT,
});

// Datadog for metrics
import { StatsD } from 'node-dogstatsd';

const dogstatsd = new StatsD({
  host: process.env.DD_AGENT_HOST,
});
```

### Health Checks
```typescript
// app/api/health/route.ts
export async function GET() {
  const health = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    services: {
      database: await checkDatabase(),
      redis: await checkRedis(),
      minio: await checkMinIO(),
      qdrant: await checkQdrant(),
    },
  };

  const allHealthy = Object.values(health.services).every(s => s === 'healthy');

  return Response.json(health, {
    status: allHealthy ? 200 : 503,
  });
}
```

---

## 🐛 Troubleshooting

### Deployment Fails
```bash
# Check logs
railway logs

# Verify environment variables
railway variables

# Test locally with Railway env
railway run npm start

# Check build configuration
cat railway.json
```

### Database Connection Issues
```bash
# Test connection
railway run node -e "require('pg').Client({connectionString: process.env.DATABASE_URL}).connect().then(() => console.log('Connected!')).catch(console.error)"

# Check DATABASE_URL
railway variables | grep DATABASE_URL

# Verify SSL configuration
# Add to connection: ssl: { rejectUnauthorized: false }
```

### Private Networking Not Working
```bash
# Verify using correct format
# ✅ http://${{service.RAILWAY_PRIVATE_DOMAIN}}:${{service.PORT}}
# ❌ https://${{service.RAILWAY_PRIVATE_DOMAIN}}:${{service.PORT}}

# Check services are in same project and environment
railway status
```

---

## 📚 Additional Resources

### Official Documentation
- [Railway Docs](https://docs.railway.com)
- [Railway CLI Reference](https://docs.railway.com/reference/cli-api)
- [Railway Templates](https://railway.app/templates)

### Community Resources
- [Railway Discord](https://discord.gg/railway)
- [Railway Help Station](https://help.railway.com)
- [Railway Blog](https://blog.railway.com)

### Integration Docs
- [Prisma with Railway](https://www.prisma.io/docs/guides/deployment/deployment-guides/deploying-to-railway)
- [Next.js on Railway](https://railway.app/new/template/nextjs)
- [Express on Railway](https://railway.app/new/template/express)

---

## 🤝 Contributing

This kit is part of the [Claudius Skills](https://github.com/Dexploarer/claudius-skills) project. Contributions are welcome!

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 🙏 Acknowledgments

- Railway.app team for an amazing platform
- Claude Code team for extensibility features
- Open source community for tools and libraries

---

**Built with ❤️ for the Railway and Claude Code communities**

For support and questions, visit the [Claudius Skills repository](https://github.com/Dexploarer/claudius-skills) or Railway Discord.
