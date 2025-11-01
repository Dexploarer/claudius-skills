# Intermediate Kit - Commands Reference

> **Comprehensive guide to all 15 production-ready slash commands**
> Manual workflow shortcuts for advanced development

---

## 📋 Commands Overview

The Intermediate Kit includes **15 advanced slash commands** organized by category:
- **Development & Build:** 4 commands
- **Database & Deployment:** 4 commands
- **CI/CD & Quality:** 7 commands

All commands are located in: `intermediate-kit/.claude/commands/`

---

## 🔨 Development & Build Commands

### /api-docs-generate

**File:** `intermediate-kit/.claude/commands/api-docs-generate.md`

**Purpose:** Generate comprehensive API documentation (OpenAPI/Swagger)

**Usage:**
```
/api-docs-generate
/api-docs-generate [path/to/api/code]
```

**What It Does:**
1. Scans API endpoints (Express, FastAPI, Django REST)
2. Generates OpenAPI 3.0 specification
3. Creates request/response schemas
4. Adds example payloads
5. Documents authentication
6. Generates Swagger UI setup

**Output:**
- `openapi.yaml` or `openapi.json`
- Interactive Swagger UI configuration
- Example requests and responses
- Authentication schemas

**Use Cases:**
- After creating new API endpoints
- Before API deployment
- For external API consumers
- Team API documentation

**Example:**
```
You: "/api-docs-generate"
Claude:
→ Scans Express routes in src/routes/
→ Generates OpenAPI 3.0 spec
→ Creates openapi.yaml
→ Adds Swagger UI in docs/
```

---

### /bundle-analyze

**File:** `intermediate-kit/.claude/commands/bundle-analyze.md`

**Purpose:** Analyze JavaScript bundle size and composition

**Usage:**
```
/bundle-analyze
/bundle-analyze [production|development]
```

**What It Does:**
1. Runs webpack-bundle-analyzer or similar
2. Identifies large dependencies
3. Detects duplicate packages
4. Suggests optimization opportunities
5. Generates visual bundle report

**Output:**
- Interactive bundle visualization
- Size breakdown by module
- Duplicate dependency report
- Optimization recommendations

**Use Cases:**
- Before production deployment
- Performance optimization sprints
- Investigating slow load times
- Regular bundle health checks

**Example:**
```
You: "/bundle-analyze production"
Claude:
→ Builds production bundle
→ Runs webpack-bundle-analyzer
→ Opens visualization in browser
→ Identifies react-dom as largest dependency (130KB)
→ Suggests code splitting for charts library
```

---

### /performance-profile

**File:** `intermediate-kit/.claude/commands/performance-profile.md`

**Purpose:** Profile application performance and identify bottlenecks

**Usage:**
```
/performance-profile
/performance-profile [component/endpoint]
```

**What It Does:**
1. Runs performance profiling tools
2. Identifies slow functions
3. Measures render times (React/Vue)
4. Analyzes API response times
5. Suggests optimizations

**Output:**
- Performance metrics report
- Slow function identification
- Render time analysis
- Optimization recommendations

**Use Cases:**
- Diagnosing slow pages
- Optimizing critical paths
- Before major releases
- Performance regression testing

**Example:**
```
You: "/performance-profile"
Claude:
→ Runs React Profiler
→ Identifies UserList re-renders 50 times
→ Suggests useMemo for filtered data
→ Recommends React.memo for UserCard
```

---

### /docker-build

**File:** `intermediate-kit/.claude/commands/docker-build.md`

**Purpose:** Build and optimize Docker images

**Usage:**
```
/docker-build
/docker-build [--optimize] [--scan]
```

**What It Does:**
1. Creates/updates Dockerfile
2. Implements multi-stage builds
3. Optimizes layer caching
4. Runs security scanning
5. Builds and tags image
6. Suggests size optimizations

**Output:**
- Optimized Dockerfile
- Built Docker image
- Security scan report
- Size optimization suggestions
- .dockerignore file

**Use Cases:**
- Initial Docker setup
- Optimizing image size
- Before deployment
- Security compliance

**Example:**
```
You: "/docker-build --optimize --scan"
Claude:
→ Creates multi-stage Dockerfile
→ Implements layer caching
→ Builds image: app:latest (150MB)
→ Scans for vulnerabilities (0 critical)
→ Suggests alpine base image (-40MB)
```

---

## 💾 Database & Deployment Commands

### /db-backup

**File:** `intermediate-kit/.claude/commands/db-backup.md`

**Purpose:** Create database backups with versioning

**Usage:**
```
/db-backup
/db-backup [database-name]
/db-backup --restore [backup-file]
```

**What It Does:**
1. Creates timestamped database dump
2. Compresses backup file
3. Stores in backups/ directory
4. Validates backup integrity
5. Lists existing backups
6. Can restore from backup

**Output:**
- Compressed database dump
- Backup metadata file
- Validation report
- Restore instructions

**Use Cases:**
- Before migrations
- Pre-deployment safety
- Regular backup schedules
- Disaster recovery prep

**Example:**
```
You: "/db-backup production_db"
Claude:
→ Creates pg_dump of production_db
→ Compresses to backups/production_db_2025-11-01_14-30.sql.gz
→ Validates backup integrity
→ Backup size: 45MB
→ Backup includes 150,000 rows across 25 tables
```

---

### /migration-create

**File:** `intermediate-kit/.claude/commands/migration-create.md`

**Purpose:** Create new database migration files

**Usage:**
```
/migration-create [description]
/migration-create add_email_verification_to_users
```

**What It Does:**
1. Creates timestamped migration file
2. Generates up/down migrations
3. Includes appropriate ORM syntax
4. Adds migration to version control
5. Provides testing instructions

**Output:**
- Migration file (SQL or ORM)
- Timestamp prefix
- Up and down functions
- Migration test instructions

**Use Cases:**
- Schema changes
- Data transformations
- Index additions
- Constraint modifications

**Example:**
```
You: "/migration-create add_user_roles"
Claude:
→ Creates 20251101143000_add_user_roles.py
→ Adds role field to User model
→ Creates user_roles table
→ Adds foreign key constraint
→ Includes rollback migration
→ Adds migration test checklist
```

---

### /deploy

**File:** `intermediate-kit/.claude/commands/deploy.md`

**Purpose:** Deploy application to production

**Usage:**
```
/deploy
/deploy [staging|production]
/deploy --dry-run
```

**What It Does:**
1. Runs pre-deployment checks
2. Builds production assets
3. Runs tests
4. Creates deployment package
5. Deploys to target environment
6. Runs post-deployment verification

**Output:**
- Build artifacts
- Deployment logs
- Health check results
- Rollback instructions

**Use Cases:**
- Production deployments
- Staging deployments
- Blue-green deployments
- Automated CI/CD

**Example:**
```
You: "/deploy production"
Claude:
→ ✅ Tests passing (125/125)
→ ✅ Security audit clean
→ ✅ Bundle size acceptable (2.3MB)
→ Building production bundle...
→ Deploying to production server...
→ ✅ Deployment successful
→ Health check: All systems operational
```

---

### /env-setup

**File:** `intermediate-kit/.claude/commands/env-setup.md`

**Purpose:** Set up environment configuration

**Usage:**
```
/env-setup
/env-setup [development|staging|production]
```

**What It Does:**
1. Creates .env template
2. Documents required variables
3. Validates existing .env
4. Adds .env to .gitignore
5. Creates .env.example
6. Provides setup instructions

**Output:**
- .env.example template
- Environment variable documentation
- Validation script
- Setup instructions

**Use Cases:**
- Initial project setup
- Onboarding new developers
- Environment migrations
- Security audits

**Example:**
```
You: "/env-setup"
Claude:
→ Creates .env.example with required vars:
  - DATABASE_URL
  - API_KEY
  - JWT_SECRET
  - REDIS_URL
→ Adds .env to .gitignore
→ Creates validation script
→ Documents each variable
```

---

## 🎯 CI/CD & Quality Commands

### /pr-creator

**File:** `intermediate-kit/.claude/commands/pr-creator.md`

**Purpose:** Create comprehensive pull request

**Usage:**
```
/pr-creator
/pr-creator [base-branch]
```

**What It Does:**
1. Analyzes git diff
2. Generates PR title and description
3. Creates change summary
4. Adds test checklist
5. Lists affected files
6. Suggests reviewers

**Output:**
- PR title
- Detailed description with sections
- Change summary
- Test plan
- Review checklist

**Use Cases:**
- Code review preparation
- Team collaboration
- Change documentation
- Release management

**Example:**
```
You: "/pr-creator main"
Claude:
→ Analyzes 15 changed files
→ Generates PR:
  Title: "feat: Add user authentication with JWT"
  Description:
  ## Summary
  - Implements JWT authentication
  - Adds login/register endpoints
  - Includes refresh token mechanism

  ## Changes
  - Added auth middleware
  - Created User model
  - Implemented JWT utilities

  ## Test Plan
  - [ ] Login with valid credentials
  - [ ] Token refresh works
  - [ ] Protected routes require auth
```

---

### /changelog-update

**File:** `intermediate-kit/.claude/commands/changelog-update.md`

**Purpose:** Update CHANGELOG.md with recent changes

**Usage:**
```
/changelog-update
/changelog-update [version]
```

**What It Does:**
1. Analyzes recent commits
2. Categorizes changes (Added, Changed, Fixed)
3. Updates CHANGELOG.md
4. Follows Keep a Changelog format
5. Adds version and date

**Output:**
- Updated CHANGELOG.md
- Categorized changes
- Semantic versioning
- Release date

**Use Cases:**
- Pre-release preparation
- Version bumps
- Release notes
- Change tracking

**Example:**
```
You: "/changelog-update 2.1.0"
Claude:
→ Analyzes commits since v2.0.0
→ Updates CHANGELOG.md:

## [2.1.0] - 2025-11-01

### Added
- JWT authentication system
- User registration endpoint
- Token refresh mechanism

### Changed
- Updated Express to 4.18.2
- Improved error handling

### Fixed
- Fixed memory leak in WebSocket connection
```

---

### /coverage-report

**File:** `intermediate-kit/.claude/commands/coverage-report.md`

**Purpose:** Generate detailed test coverage report

**Usage:**
```
/coverage-report
/coverage-report [--html]
```

**What It Does:**
1. Runs tests with coverage
2. Generates coverage report
3. Identifies uncovered code
4. Suggests tests for low coverage areas
5. Creates HTML report (optional)

**Output:**
- Coverage percentage by file
- Uncovered lines report
- HTML visualization (if requested)
- Coverage trends

**Use Cases:**
- Quality assurance
- Pre-release checks
- Identifying test gaps
- CI/CD quality gates

**Example:**
```
You: "/coverage-report --html"
Claude:
→ Running tests with coverage...
→ ✅ All tests passing (125/125)

Coverage Summary:
- Statements: 87.5% (350/400)
- Branches: 82.3% (141/171)
- Functions: 91.2% (52/57)
- Lines: 88.1% (338/384)

Low Coverage Files:
- src/utils/email.ts: 45% (suggest adding tests)
- src/middleware/cache.ts: 60%

→ HTML report: coverage/index.html
```

---

### /security-audit

**File:** `intermediate-kit/.claude/commands/security-audit.md`

**Purpose:** Run comprehensive security audit

**Usage:**
```
/security-audit
/security-audit [--fix]
```

**What It Does:**
1. Runs npm audit / pip-audit
2. Scans for known vulnerabilities
3. Checks dependency licenses
4. Analyzes code for security issues
5. Suggests fixes
6. Can auto-fix some issues

**Output:**
- Vulnerability report
- Severity breakdown
- Fix recommendations
- License compliance report

**Use Cases:**
- Pre-deployment checks
- Regular security scans
- Compliance requirements
- Dependency updates

**Example:**
```
You: "/security-audit"
Claude:
→ Running npm audit...

Security Issues Found:
- 0 critical
- 1 high: lodash (Prototype Pollution)
- 3 moderate: axios, moment, serialize-javascript
- 5 low

Recommendations:
- Update lodash: 4.17.15 → 4.17.21
- Replace moment with date-fns (smaller, modern)
- Update axios: 0.21.1 → 1.6.0

Run /security-audit --fix to auto-fix
```

---

### /dependency-update

**File:** `intermediate-kit/.claude/commands/dependency-update.md`

**Purpose:** Update and audit dependencies

**Usage:**
```
/dependency-update
/dependency-update [--major|--minor|--patch]
```

**What It Does:**
1. Checks for outdated packages
2. Categorizes updates (major/minor/patch)
3. Runs security audit
4. Updates package.json
5. Runs tests after update
6. Creates git commit

**Output:**
- List of updated packages
- Security audit results
- Breaking change warnings
- Test results

**Use Cases:**
- Regular maintenance
- Security patches
- Major version upgrades
- Dependency cleanup

**Example:**
```
You: "/dependency-update --minor"
Claude:
→ Checking for updates...

Available Updates:
- react: 18.2.0 → 18.3.0 (minor)
- typescript: 5.1.6 → 5.3.0 (minor)
- express: 4.18.2 → 4.19.0 (minor)

→ Updating packages...
→ Running tests... ✅ All passing
→ Security audit... ✅ Clean
→ Creating commit: "chore: update dependencies"
```

---

### /version-bump

**File:** `intermediate-kit/.claude/commands/version-bump.md`

**Purpose:** Bump version number (semantic versioning)

**Usage:**
```
/version-bump [major|minor|patch]
/version-bump patch
```

**What It Does:**
1. Reads current version
2. Increments version (semver)
3. Updates package.json / pyproject.toml
4. Updates CHANGELOG.md
5. Creates git tag
6. Commits version bump

**Output:**
- Updated version in package files
- Git tag
- Updated CHANGELOG
- Commit with version

**Use Cases:**
- Release preparation
- Semantic versioning
- Automated releases
- Version tracking

**Example:**
```
You: "/version-bump minor"
Claude:
→ Current version: 2.0.5
→ New version: 2.1.0

Updates:
- package.json: version → 2.1.0
- CHANGELOG.md: Added [2.1.0] section

→ Creating commit: "chore: bump version to 2.1.0"
→ Creating git tag: v2.1.0
→ ✅ Version bumped successfully
```

---

### /health-check

**File:** `intermediate-kit/.claude/commands/health-check.md`

**Purpose:** Check application health and status

**Usage:**
```
/health-check
/health-check [--verbose]
```

**What It Does:**
1. Checks application dependencies
2. Validates environment variables
3. Tests database connectivity
4. Checks external service health
5. Validates configuration
6. Reports overall status

**Output:**
- System status report
- Dependency status
- Service connectivity
- Configuration warnings

**Use Cases:**
- Post-deployment verification
- Development environment setup
- Troubleshooting
- CI/CD health gates

**Example:**
```
You: "/health-check --verbose"
Claude:
→ Running health checks...

✅ Application: Healthy
✅ Database: Connected (PostgreSQL 14.5)
✅ Redis: Connected (6.2.7)
✅ Environment Variables: All required vars present
⚠️  External API: Slow response (1.2s, expected <500ms)
✅ Disk Space: 45GB free (70% available)
✅ Memory: 2.1GB / 8GB used

Overall Status: Healthy with warnings
```

---

## 🎯 Command Usage Patterns

### Pre-Deployment Checklist

```bash
/security-audit          # Check for vulnerabilities
/coverage-report         # Ensure adequate test coverage
/bundle-analyze          # Verify bundle size
/health-check            # Validate system health
/changelog-update 2.1.0  # Update changelog
/version-bump minor      # Bump version
/deploy production       # Deploy to production
```

### Development Workflow

```bash
/env-setup              # Initial environment setup
/migration-create       # Create database migrations
/api-docs-generate      # Document APIs
/pr-creator             # Create pull request
```

### Maintenance Workflow

```bash
/dependency-update --minor  # Update dependencies
/security-audit --fix       # Fix security issues
/db-backup                  # Backup database
/health-check               # Verify system health
```

---

## 💡 Best Practices

### When to Use Commands vs Skills

**Use Commands when:**
- You need explicit control
- Running a specific workflow
- Part of a checklist
- Repeatable process

**Use Skills when:**
- Auto-invocation is preferred
- Context-aware generation
- Building new features
- Natural language flow

### Command Combinations

Many commands work well together:

```
Example: Deployment Preparation
1. /security-audit       → Check vulnerabilities
2. /coverage-report      → Verify test coverage
3. /bundle-analyze       → Optimize bundle
4. /changelog-update     → Document changes
5. /version-bump         → Bump version
6. /pr-creator           → Create release PR
7. /deploy staging       → Deploy to staging
8. /health-check         → Verify deployment
```

### Automation

Commands can be automated in CI/CD:

```yaml
# Example GitHub Actions
- name: Security Audit
  run: claude /security-audit

- name: Test Coverage
  run: claude /coverage-report

- name: Deploy
  run: claude /deploy production
```

---

## 🔗 Related References

**Skills Reference:**
- See: `@intermediate-kit/.claude/rules/skills-reference.md`
- Skills auto-invoke, commands are manual

**Agents Reference:**
- See: `@intermediate-kit/.claude/rules/agents-reference.md`
- Agents provide deep expertise

**Hooks Reference:**
- See: `@intermediate-kit/.claude/rules/hooks-reference.md`
- Hooks provide event-driven automation

**Workflow Rules:**
- Deployment: `@intermediate-kit/.claude/rules/workflows/deployment.md`
- Security: `@intermediate-kit/.claude/rules/workflows/security.md`
- API Development: `@intermediate-kit/.claude/rules/workflows/api-development.md`

---

## 📚 Command File Locations

All command files are located in: `intermediate-kit/.claude/commands/`

```
intermediate-kit/.claude/commands/
├── api-docs-generate.md
├── bundle-analyze.md
├── changelog-update.md
├── coverage-report.md
├── db-backup.md
├── deploy.md
├── dependency-update.md
├── docker-build.md
├── env-setup.md
├── health-check.md
├── migration-create.md
├── performance-profile.md
├── pr-creator.md
├── security-audit.md
└── version-bump.md
```

---

**Last Updated:** 2025-11-01
**Total Commands:** 15
**Level:** Intermediate (Production-Ready)
