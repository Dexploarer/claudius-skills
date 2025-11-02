# /scaffold-service - Service Scaffolding

Quickly scaffold a new service with all best practices built-in.

---

## Usage

```
/scaffold-service [service-type] [service-name]
```

Examples:
- `/scaffold-service rest-api user-service`
- `/scaffold-service grpc inventory-service`
- `/scaffold-service worker notification-worker`

---

## What This Command Does

1. **Generate Service Structure**
   - Project scaffolding
   - Directory structure
   - Configuration files
   - Environment templates

2. **Add Infrastructure**
   - Dockerfile (multi-stage)
   - Kubernetes manifests
   - Terraform modules
   - CI/CD pipeline

3. **Integrate Observability**
   - Structured logging
   - Prometheus metrics
   - OpenTelemetry tracing
   - Health checks

4. **Security Setup**
   - Authentication middleware
   - Rate limiting
   - Input validation
   - Security headers

5. **Developer Experience**
   - README with getting started
   - Local development setup
   - Pre-commit hooks
   - VS Code settings

---

## Service Types

### REST API
- Express.js or FastAPI
- OpenAPI documentation
- Request validation
- Error handling

### gRPC Service
- Protocol buffers
- Bidirectional streaming
- Load balancing
- Service mesh ready

### Background Worker
- Queue integration (SQS, RabbitMQ)
- Retry logic
- Dead letter queue
- Job monitoring

### GraphQL API
- Schema definition
- Resolvers
- DataLoader
- Subscriptions

---

## Output

```
✅ SERVICE SCAFFOLDED

Name: user-service
Type: REST API
Framework: Express.js + TypeScript

Structure Created:
user-service/
├── src/
│   ├── routes/
│   ├── middleware/
│   ├── services/
│   └── models/
├── tests/
├── deploy/
│   ├── Dockerfile
│   ├── k8s/
│   └── terraform/
├── .github/workflows/
└── README.md

Next Steps:
1. cd user-service
2. npm install
3. npm run dev
4. Start building!

Documentation: ./user-service/README.md
```

---

**Related Commands:**
- `/create-golden-path` - Standardized templates
- `/generate-docs` - API documentation
