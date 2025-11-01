# Deployment Workflow - Intermediate Kit

> **Production deployment best practices and checklists**

---

## 🎯 Pre-Deployment Checklist

- [ ] All tests passing (`npm test`, `pytest`, etc.)
- [ ] Security audit clean (`/security-audit`)
- [ ] Code reviewed and approved (`/pr-creator`)
- [ ] Bundle size acceptable (`/bundle-analyze`)
- [ ] Database migrations ready (`/migration-create`)
- [ ] Environment variables documented (`/env-setup`)
- [ ] CHANGELOG updated (`/changelog-update`)
- [ ] Version bumped (`/version-bump`)
- [ ] Health check passing (`/health-check`)
- [ ] Database backup created (`/db-backup`)

---

## 🚀 Deployment Process

### Step 1: Pre-Deployment Validation

```bash
/security-audit          # Security check
/coverage-report         # Test coverage
/bundle-analyze          # Bundle size
/health-check            # System health
```

### Step 2: Build & Package

```bash
/docker-build --optimize --scan
```

### Step 3: Database Preparation

```bash
/db-backup production_db    # Backup first!
/migration-create           # If needed
```

### Step 4: Deploy

```bash
/deploy staging      # Test on staging first
/deploy production   # Then production
```

### Step 5: Post-Deployment Verification

```bash
/health-check --verbose
```

---

## 🔧 Deployment Strategies

### 1. Blue-Green Deployment

- Zero downtime
- Easy rollback
- Database compatibility required

### 2. Rolling Deployment

- Gradual rollout
- Partial availability during deployment
- Compatible versions required

### 3. Canary Deployment

- Test with small user percentage
- Monitor metrics
- Gradual rollout on success

---

## 🔐 Environment Management

**Development → Staging → Production**

```bash
/env-setup development
/env-setup staging
/env-setup production
```

---

**Related Agents:** `devops-engineer`, `system-architect`
**Related Commands:** `/deploy`, `/docker-build`, `/health-check`

---

**Last Updated:** 2025-11-01
