# Intermediate Kit - Agents Reference

> **Comprehensive guide to all 6 specialist subagents**
> Expert AI consultants for complex architectural decisions

---

## 📋 Agents Overview

The Intermediate Kit includes **6 specialist subagents** for:
- **API Design** - RESTful and GraphQL architecture
- **Database Design** - Schema design and optimization
- **DevOps** - Infrastructure and deployment
- **Performance** - Optimization and profiling
- **Security** - Vulnerability analysis and hardening
- **System Architecture** - Design patterns and scalability

All agents are located in: `intermediate-kit/.claude/agents/`

---

## 🎨 Specialist Subagents

### 1. api-designer

**File:** `intermediate-kit/.claude/agents/api-designer.md`

**Purpose:** REST/GraphQL API design expert

**Invocation:**
```
"Use api-designer to design the user management API"
"Ask api-designer to review the GraphQL schema"
"api-designer: design a RESTful API for e-commerce"
```

**Expertise:**
- RESTful API design principles
- Resource-oriented architecture
- HTTP method selection (GET, POST, PUT, PATCH, DELETE)
- Status code best practices
- API versioning strategies
- GraphQL schema design
- Query and mutation design
- Authentication/authorization patterns
- Rate limiting and throttling
- API documentation standards

**Available Tools:**
- Read (analyze existing code)
- Write (create API designs)
- Grep (search API patterns)

**Typical Workflows:**
1. **Initial API Design**
   - Analyzes domain models
   - Designs resource endpoints
   - Defines request/response schemas
   - Plans authentication strategy

2. **API Review**
   - Reviews existing endpoints
   - Identifies inconsistencies
   - Suggests improvements
   - Validates REST principles

3. **GraphQL Schema**
   - Designs type system
   - Creates queries and mutations
   - Plans resolver structure
   - Optimizes for N+1 queries

**Example Usage:**
```
You: "Use api-designer to design an API for a blog platform"

api-designer:
→ Analyzes domain: Posts, Comments, Users, Categories
→ Designs RESTful endpoints:
  GET    /api/v1/posts
  GET    /api/v1/posts/:id
  POST   /api/v1/posts
  PUT    /api/v1/posts/:id
  DELETE /api/v1/posts/:id
  GET    /api/v1/posts/:id/comments
  POST   /api/v1/posts/:id/comments

→ Defines request/response schemas
→ Plans authentication (JWT)
→ Adds pagination, filtering, sorting
→ Suggests rate limiting (100 req/min)
→ Recommends API versioning strategy
```

**When to Use:**
- Before starting API implementation
- When designing complex APIs
- For API consistency reviews
- Planning API versioning
- GraphQL schema design

---

### 2. database-architect

**File:** `intermediate-kit/.claude/agents/database-architect.md`

**Purpose:** Database schema design specialist

**Invocation:**
```
"Use database-architect to design the e-commerce database"
"Ask database-architect to optimize the current schema"
"database-architect: review the user relationships"
```

**Expertise:**
- Database normalization (1NF, 2NF, 3NF, BCNF)
- Relational schema design
- Index strategy and optimization
- Foreign key relationships
- Data integrity constraints
- Query optimization
- Denormalization when appropriate
- NoSQL schema design
- Sharding and partitioning strategies
- Migration planning

**Available Tools:**
- Read (analyze current schema)
- Write (create schema designs)
- Grep (search database code)

**Typical Workflows:**
1. **Schema Design**
   - Analyzes business requirements
   - Creates normalized schema
   - Defines relationships
   - Plans indexes
   - Adds constraints

2. **Schema Optimization**
   - Reviews existing schema
   - Identifies inefficiencies
   - Suggests index additions
   - Plans denormalization where needed
   - Optimizes query patterns

3. **Migration Planning**
   - Designs migration strategy
   - Plans backward compatibility
   - Identifies data transformation needs
   - Suggests rollback procedures

**Example Usage:**
```
You: "Use database-architect to design a schema for an e-commerce platform"

database-architect:
→ Analyzes requirements: Products, Orders, Users, Inventory

→ Designs normalized schema:

  users
  ├── id (PK)
  ├── email (UNIQUE)
  ├── password_hash
  └── created_at

  products
  ├── id (PK)
  ├── name
  ├── description
  ├── price
  ├── category_id (FK → categories)
  └── created_at

  orders
  ├── id (PK)
  ├── user_id (FK → users)
  ├── status
  ├── total_amount
  └── created_at

  order_items
  ├── id (PK)
  ├── order_id (FK → orders)
  ├── product_id (FK → products)
  ├── quantity
  └── price_snapshot

→ Recommends indexes:
  - users.email (login queries)
  - products.category_id (filtering)
  - orders.user_id (user order history)
  - orders.created_at (date range queries)

→ Suggests constraints:
  - CHECK (quantity > 0)
  - CHECK (price >= 0)

→ Plans for scale:
  - Consider partitioning orders by date
  - Denormalize product name in order_items
```

**When to Use:**
- Before database implementation
- When designing complex relationships
- For performance optimization
- Planning database migrations
- Scaling existing databases

---

### 3. devops-engineer

**File:** `intermediate-kit/.claude/agents/devops-engineer.md`

**Purpose:** DevOps and infrastructure expert

**Invocation:**
```
"Use devops-engineer for deployment strategy"
"Ask devops-engineer to design CI/CD pipeline"
"devops-engineer: help with Docker optimization"
```

**Expertise:**
- CI/CD pipeline design
- Container orchestration (Docker, Kubernetes)
- Infrastructure as Code (Terraform, CloudFormation)
- Deployment strategies (blue-green, canary, rolling)
- Monitoring and observability
- Log aggregation
- Auto-scaling strategies
- Disaster recovery planning
- Cloud platform expertise (AWS, GCP, Azure)
- Security hardening

**Available Tools:**
- Read (analyze infrastructure code)
- Write (create configs and scripts)
- Bash (execute commands)
- Grep (search infrastructure patterns)

**Typical Workflows:**
1. **CI/CD Pipeline Design**
   - Analyzes project structure
   - Designs build pipeline
   - Creates deployment stages
   - Plans testing strategy
   - Implements rollback procedures

2. **Container Optimization**
   - Reviews Dockerfile
   - Implements multi-stage builds
   - Optimizes layer caching
   - Reduces image size
   - Adds security scanning

3. **Infrastructure Design**
   - Plans cloud architecture
   - Designs for high availability
   - Implements auto-scaling
   - Sets up monitoring
   - Plans disaster recovery

**Example Usage:**
```
You: "Use devops-engineer to design a deployment pipeline for our Node.js API"

devops-engineer:
→ Analyzes project: Express.js API with PostgreSQL

→ Designs CI/CD Pipeline:

  1. Build Stage:
     - Install dependencies
     - Run linting (ESLint)
     - Run type checking (TypeScript)
     - Build production bundle

  2. Test Stage:
     - Run unit tests (Jest)
     - Run integration tests
     - Generate coverage report
     - Require 80% coverage

  3. Security Stage:
     - Run npm audit
     - Scan Docker image (Trivy)
     - Check for secrets

  4. Deploy Stage (Staging):
     - Build Docker image
     - Push to registry
     - Deploy to staging
     - Run smoke tests

  5. Deploy Stage (Production):
     - Manual approval required
     - Blue-green deployment
     - Health checks
     - Automatic rollback on failure

→ Creates Dockerfile:
  - Multi-stage build
  - Node.js Alpine base (reduces size)
  - Security scanning
  - Non-root user

→ Suggests infrastructure:
  - Load balancer (health checks)
  - Auto-scaling (2-10 instances)
  - Database (managed PostgreSQL)
  - Redis (caching)
  - CloudWatch monitoring
```

**When to Use:**
- Setting up new projects
- Designing deployment pipelines
- Optimizing Docker images
- Planning infrastructure
- Implementing monitoring
- Disaster recovery planning

---

### 4. performance-optimizer

**File:** `intermediate-kit/.claude/agents/performance-optimizer.md`

**Purpose:** Performance tuning specialist

**Invocation:**
```
"Use performance-optimizer to optimize the application"
"Ask performance-optimizer to analyze slow pages"
"performance-optimizer: help reduce bundle size"
```

**Expertise:**
- Performance profiling
- Frontend optimization (React, Vue)
- Backend optimization (API, database)
- Bundle size optimization
- Code splitting and lazy loading
- Caching strategies
- Database query optimization
- CDN configuration
- Image optimization
- Lighthouse optimization

**Available Tools:**
- Read (analyze code)
- Grep (find performance issues)
- Bash (run profiling tools)

**Typical Workflows:**
1. **Frontend Optimization**
   - Profiles component renders
   - Identifies unnecessary re-renders
   - Suggests memoization
   - Plans code splitting
   - Optimizes bundle size

2. **Backend Optimization**
   - Analyzes API response times
   - Identifies slow queries
   - Suggests caching
   - Optimizes database indexes
   - Plans horizontal scaling

3. **Full-Stack Optimization**
   - Runs Lighthouse audit
   - Optimizes critical rendering path
   - Implements lazy loading
   - Optimizes images
   - Configures CDN

**Example Usage:**
```
You: "Use performance-optimizer to optimize our React dashboard"

performance-optimizer:
→ Analyzes application...

Performance Issues Found:

1. Bundle Size (High Priority)
   - Total: 2.8MB (target: <500KB)
   - Moment.js: 300KB → Replace with date-fns (-280KB)
   - Lodash: 150KB → Use lodash-es with tree-shaking (-100KB)
   - Chart.js: 400KB → Lazy load only when needed

2. React Re-renders (High Priority)
   - UserList re-renders 50 times per minute
   - Suggestion: Use React.memo
   - Suggestion: Move filtering to useMemo

3. Images (Medium Priority)
   - 15 unoptimized images (total 3MB)
   - Suggestion: Convert to WebP (-60%)
   - Suggestion: Implement lazy loading
   - Suggestion: Use responsive images

4. Database Queries (Medium Priority)
   - /api/users endpoint: 850ms
   - N+1 query detected (100 queries instead of 2)
   - Suggestion: Use JOIN or eager loading

Recommendations:
1. Implement code splitting for routes
2. Add React.memo to expensive components
3. Use useMemo for filtered/sorted data
4. Add database indexes on user.email and user.role
5. Implement Redis caching for /api/users

Expected Improvements:
- Bundle size: 2.8MB → 800KB (-71%)
- Initial load: 4.2s → 1.5s (-64%)
- Time to Interactive: 6.1s → 2.2s (-64%)
```

**When to Use:**
- Slow page loads
- High bundle sizes
- Performance regressions
- Before major releases
- Lighthouse score improvements
- Database performance issues

---

### 5. security-auditor

**File:** `intermediate-kit/.claude/agents/security-auditor.md`

**Purpose:** Security analysis expert

**Invocation:**
```
"Use security-auditor to audit the application"
"Ask security-auditor to review authentication"
"security-auditor: check for vulnerabilities"
```

**Expertise:**
- OWASP Top 10 vulnerabilities
- Authentication and authorization
- Input validation and sanitization
- SQL injection prevention
- XSS prevention
- CSRF protection
- Secure session management
- API security
- Dependency vulnerability scanning
- Security headers configuration
- Secret management
- Encryption best practices

**Available Tools:**
- Read (analyze code for vulnerabilities)
- Grep (search for security issues)
- Bash (run security tools)

**Typical Workflows:**
1. **Security Audit**
   - Scans for OWASP Top 10
   - Reviews authentication
   - Checks authorization
   - Validates input handling
   - Reviews dependency security

2. **Authentication Review**
   - Analyzes password storage
   - Reviews session management
   - Checks token security
   - Validates OAuth implementation
   - Reviews 2FA implementation

3. **API Security**
   - Reviews rate limiting
   - Checks input validation
   - Validates authentication
   - Reviews CORS configuration
   - Checks for injection vulnerabilities

**Example Usage:**
```
You: "Use security-auditor to audit our authentication system"

security-auditor:
→ Analyzing authentication implementation...

Security Issues Found:

❌ CRITICAL: Password Storage
- Passwords hashed with MD5 (weak algorithm)
- No salt used
- Recommendation: Use bcrypt with cost factor 12

❌ CRITICAL: JWT Secret
- JWT secret found in codebase (hardcoded)
- Recommendation: Move to environment variable
- Recommendation: Use strong random secret (32+ chars)

⚠️  HIGH: Session Management
- Sessions don't expire (no TTL)
- Recommendation: Add 24-hour expiration
- Recommendation: Implement refresh tokens

⚠️  HIGH: Input Validation
- Email not validated before DB insertion
- Password requirements too weak (min 6 chars)
- Recommendation: Validate email format
- Recommendation: Enforce strong passwords (min 12 chars)

⚠️  MEDIUM: CORS Configuration
- CORS allows all origins (*)
- Recommendation: Whitelist specific domains

⚠️  MEDIUM: Rate Limiting
- No rate limiting on login endpoint
- Vulnerable to brute force attacks
- Recommendation: Implement rate limiting (5 attempts/minute)

✅ GOOD: HTTPS
- All endpoints use HTTPS
- Secure cookies enabled

Immediate Actions Required:
1. Change password hashing to bcrypt
2. Move JWT secret to environment variable
3. Add session expiration (24 hours)
4. Implement rate limiting on /auth/* endpoints
5. Add input validation for all user inputs

Risk Level: HIGH
Recommendation: Address critical issues before deployment
```

**When to Use:**
- Before production deployment
- After implementing authentication
- Regular security audits
- Compliance requirements (SOC2, PCI-DSS)
- After dependency updates
- Handling sensitive data

---

### 6. system-architect

**File:** `intermediate-kit/.claude/agents/system-architect.md`

**Purpose:** System design and architecture expert

**Invocation:**
```
"Use system-architect for architecture design"
"Ask system-architect to review the system design"
"system-architect: design a scalable e-commerce platform"
```

**Expertise:**
- Software architecture patterns
- Microservices vs monolith decisions
- Design patterns (Gang of Four, Enterprise)
- SOLID principles
- Domain-driven design (DDD)
- Event-driven architecture
- API gateway patterns
- Service mesh concepts
- Scalability patterns
- Data consistency strategies (CAP theorem)

**Available Tools:**
- Read (analyze architecture)
- Grep (search patterns)

**Typical Workflows:**
1. **Architecture Design**
   - Analyzes requirements
   - Suggests architectural patterns
   - Designs service boundaries
   - Plans data flow
   - Identifies scalability challenges

2. **Architecture Review**
   - Reviews existing architecture
   - Identifies anti-patterns
   - Suggests refactoring
   - Plans migration strategy
   - Evaluates scalability

3. **Pattern Selection**
   - Recommends design patterns
   - Suggests architectural styles
   - Evaluates trade-offs
   - Plans implementation

**Example Usage:**
```
You: "Use system-architect to design a scalable SaaS platform"

system-architect:
→ Analyzes requirements...

Architectural Recommendations:

1. Overall Architecture: Modular Monolith (initially)
   - Start with well-organized monolith
   - Clear module boundaries
   - Prepare for future microservices migration
   - Rationale: Faster initial development, easier to refactor

2. Core Modules:
   ┌─────────────────────────────────────┐
   │         API Gateway (Express)        │
   └─────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
   ┌────▼───┐  ┌────▼───┐  ┌────▼────┐
   │  Auth  │  │ Tenant │  │ Billing │
   │ Module │  │ Module │  │ Module  │
   └────────┘  └────────┘  └─────────┘
        │            │            │
        └────────────┼────────────┘
                     │
            ┌────────▼────────┐
            │   PostgreSQL     │
            │ (Multi-tenant)   │
            └─────────────────┘

3. Design Patterns Recommended:
   - Repository Pattern (data access layer)
   - Factory Pattern (tenant creation)
   - Strategy Pattern (payment processors)
   - Observer Pattern (event handling)
   - Circuit Breaker (external APIs)

4. Multi-Tenancy Strategy:
   - Shared database, separate schemas
   - Tenant isolation at application level
   - Per-tenant configuration

5. Scalability Plan:
   - Horizontal scaling (load balancer + multiple instances)
   - Read replicas for database
   - Redis for caching and sessions
   - CDN for static assets
   - Job queue for async tasks (Bull/Redis)

6. Data Flow:
   Request → Load Balancer → API Gateway
          → Auth Middleware → Tenant Resolution
          → Business Logic → Repository Layer
          → Database (with connection pooling)

7. Security Architecture:
   - JWT for authentication
   - Role-based access control (RBAC)
   - API rate limiting per tenant
   - Encryption at rest and in transit
   - Regular security audits

Migration Path (when to scale):
- Phase 1 (0-1000 users): Modular monolith
- Phase 2 (1000-10000): Extract billing microservice
- Phase 3 (10000+): Full microservices migration

Technology Stack:
- Backend: Node.js + Express (TypeScript)
- Database: PostgreSQL (multi-tenant)
- Cache: Redis
- Queue: Bull + Redis
- Monitoring: Prometheus + Grafana
- Logging: Winston + ELK Stack
```

**When to Use:**
- Starting new projects
- Planning major refactors
- Scaling existing applications
- Evaluating architectural patterns
- Microservices decisions
- Performance at scale

---

## 🎯 Agent Invocation Patterns

### Direct Invocation
```
"Use [agent-name] to [task]"
"Ask [agent-name] to [task]"
"[agent-name]: [task]"
```

### Examples
```
✅ "Use api-designer to design the user API"
✅ "Ask database-architect to review the schema"
✅ "security-auditor: check for SQL injection vulnerabilities"
✅ "Use devops-engineer for Kubernetes deployment"
```

### Multi-Agent Workflows

Agents can work in sequence:

```
Example 1: Full-Stack Feature Design
1. system-architect: Design overall architecture
2. database-architect: Design database schema
3. api-designer: Design API endpoints
4. security-auditor: Review security
5. performance-optimizer: Plan optimization
6. devops-engineer: Design deployment
```

```
Example 2: Performance Investigation
1. performance-optimizer: Identify bottlenecks
2. database-architect: Optimize queries
3. devops-engineer: Scale infrastructure
```

---

## 💡 Best Practices

### When to Use Agents vs Skills

**Use Agents when:**
- Need expert consultation
- Complex design decisions
- Architecture planning
- Performance optimization
- Security reviews
- Deep analysis required

**Use Skills when:**
- Implementing features
- Generating code
- Auto-invocation preferred
- Standard patterns

**Use Commands when:**
- Specific workflows
- Automation tasks
- CI/CD integration
- Repeatable processes

### Agent Collaboration

Best results when agents work together:

```
Scenario: Building an E-Commerce Platform

1. system-architect
   → Designs overall architecture
   → Recommends patterns

2. database-architect
   → Designs schema based on architecture
   → Plans indexes and relationships

3. api-designer
   → Designs RESTful API
   → Based on database schema

4. security-auditor
   → Reviews entire design
   → Identifies security concerns

5. performance-optimizer
   → Plans caching strategy
   → Identifies potential bottlenecks

6. devops-engineer
   → Designs deployment
   → Plans infrastructure
```

### Getting Maximum Value

1. **Be Specific**
   ```
   ❌ "Use api-designer to help"
   ✅ "Use api-designer to design a RESTful API for user management with CRUD operations"
   ```

2. **Provide Context**
   ```
   ✅ "Use database-architect to design an e-commerce schema with products, orders, and users. Expected scale: 100k users"
   ```

3. **Ask for Specific Deliverables**
   ```
   ✅ "Use devops-engineer to design a CI/CD pipeline with staging and production environments, including rollback strategy"
   ```

4. **Use for Complex Decisions**
   ```
   ✅ "Use system-architect to evaluate: monolith vs microservices for a SaaS platform with 50k users"
   ```

---

## 🔗 Related References

**Skills Reference:**
- See: `@intermediate-kit/.claude/rules/skills-reference.md`
- Skills auto-generate code

**Commands Reference:**
- See: `@intermediate-kit/.claude/rules/commands-reference.md`
- Commands execute workflows

**Hooks Reference:**
- See: `@intermediate-kit/.claude/rules/hooks-reference.md`
- Hooks provide automation

**Framework Rules:**
- React: `@intermediate-kit/.claude/rules/frameworks/react.md`
- Express: `@intermediate-kit/.claude/rules/frameworks/express.md`
- Django: `@intermediate-kit/.claude/rules/frameworks/django.md`

**Workflow Rules:**
- API Development: `@intermediate-kit/.claude/rules/workflows/api-development.md`
- Database Design: `@intermediate-kit/.claude/rules/workflows/database.md`
- Security: `@intermediate-kit/.claude/rules/workflows/security.md`
- Deployment: `@intermediate-kit/.claude/rules/workflows/deployment.md`

---

## 📚 Agent File Locations

All agent files are located in: `intermediate-kit/.claude/agents/`

```
intermediate-kit/.claude/agents/
├── api-designer.md
├── database-architect.md
├── devops-engineer.md
├── performance-optimizer.md
├── security-auditor.md
└── system-architect.md
```

---

**Last Updated:** 2025-11-01
**Total Agents:** 6
**Level:** Intermediate (Production-Ready)
