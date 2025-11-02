# /create-golden-path - Platform Engineering

Create standardized "golden path" templates for common development patterns.

---

## Usage

```
/create-golden-path [service-type]
/create-golden-path --list
```

Examples:
- `/create-golden-path rest-api`
- `/create-golden-path microservice`
- `/create-golden-path data-pipeline`
- `/create-golden-path --list`

---

## What This Command Does

Creates a fully configured, production-ready project template with:

1. **Infrastructure as Code**
   - Terraform modules
   - Kubernetes manifests
   - CI/CD pipelines
   - Monitoring config

2. **Application Scaffold**
   - Recommended framework setup
   - Best practice structure
   - Testing setup
   - Documentation templates

3. **Observability**
   - Structured logging
   - Metrics instrumentation
   - Distributed tracing
   - Alerting rules

4. **Security**
   - Authentication setup
   - Authorization patterns
   - Secrets management
   - Security scanning

5. **Developer Experience**
   - Local development setup
   - Hot reload configuration
   - Debugging tools
   - Development scripts

---

## Available Golden Paths

### REST API Service
```
rest-api-service/
├── src/
│   ├── routes/
│   ├── middleware/
│   └── models/
├── tests/
├── .github/workflows/
├── terraform/
├── k8s/
└── docs/
```

### Microservice
```
microservice/
├── cmd/
├── internal/
├── pkg/
├── deploy/
│   ├── k8s/
│   ├── terraform/
│   └── helm/
├── observability/
└── docs/
```

### Data Pipeline
```
data-pipeline/
├── dags/              # Airflow DAGs
├── transforms/        # Data transformations
├── tests/
├── deploy/
└── monitoring/
```

---

## Configuration

Customize golden path defaults in `.platform-config.yaml`:

```yaml
golden_paths:
  rest_api:
    framework: fastapi
    database: postgresql
    cache: redis
    auth: oauth2
    deployment: kubernetes
    observability:
      logging: structured-json
      metrics: prometheus
      tracing: opentelemetry
```

---

**Related Commands:**
- `/scaffold-service` - Quick service scaffolding
- `/generate-docs` - Generate platform documentation
- `/validate-service` - Validate against platform standards
