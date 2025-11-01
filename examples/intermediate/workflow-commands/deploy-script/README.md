# Deploy Script Command - Intermediate Example

A production-grade deployment command with safety checks, verification, and rollback capabilities.

## What This Teaches

- Complex multi-step commands
- Error handling and validation
- Environment management
- Health checks
- Rollback procedures

## Installation

```bash
cp command.md /path/to/your-project/.claude/commands/deploy.md
```

## Usage

```bash
/deploy [environment] [options]

# Examples:
/deploy staging
/deploy production
/deploy production --skip-tests
/deploy staging --rollback
```

## What It Does

Complete deployment workflow:
1. **Pre-flight checks** - Git status, dependencies, environment
2. **Build** - Compile, bundle, optimize
3. **Test** - Run test suite
4. **Deploy** - Upload to target environment
5. **Verify** - Health checks, smoke tests
6. **Notify** - Team notifications

## Command Structure

`.claude/commands/deploy.md`:

```markdown
# Deploy Application

Deploy application to specified environment with safety checks.

## Usage
/deploy [staging|production] [--skip-tests] [--rollback]

## Instructions

### Step 1: Validate Environment

Check $ARGUMENTS for target environment:
- staging
- production

If missing, ask: "Which environment? (staging/production)"

### Step 2: Pre-flight Checks

\```bash
# Ensure clean working directory
git status --porcelain

# On production, require main/master branch
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$ENV" = "production" ] && [ "$BRANCH" != "main" ]; then
    echo "❌ Must be on main branch for production"
    exit 1
fi

# Check environment variables exist
if [ -z "$DEPLOY_KEY" ]; then
    echo "❌ DEPLOY_KEY not set"
    exit 1
fi

# Verify dependencies are installed
npm ci  # or pip install -r requirements.txt
\```

### Step 3: Build

\```bash
echo "🔨 Building for $ENV..."

# Set environment
export NODE_ENV=$ENV

# Build
npm run build

# Verify build succeeded
if [ ! -d "dist" ]; then
    echo "❌ Build failed - no dist directory"
    exit 1
fi
\```

### Step 4: Run Tests (unless --skip-tests)

\```bash
if [ "$SKIP_TESTS" != "true" ]; then
    echo "🧪 Running tests..."
    npm test

    # Run integration tests for production
    if [ "$ENV" = "production" ]; then
        npm run test:integration
    fi
fi
\```

### Step 5: Deploy

\```bash
echo "🚀 Deploying to $ENV..."

# Backup current version (for rollback)
BACKUP_DIR=".deploy-backup-$(date +%s)"
mkdir -p $BACKUP_DIR

# Deploy based on environment
if [ "$ENV" = "staging" ]; then
    # Deploy to staging server
    rsync -avz --delete dist/ user@staging-server:/var/www/app/

elif [ "$ENV" = "production" ]; then
    # Production deployment with additional safety
    echo "⚠️  PRODUCTION DEPLOYMENT"
    echo "This will deploy to live users."
    read -p "Continue? (yes/no): " CONFIRM

    if [ "$CONFIRM" != "yes" ]; then
        echo "Deployment cancelled"
        exit 0
    fi

    # Blue-green deployment
    # 1. Deploy to inactive slot
    # 2. Run smoke tests
    # 3. Switch traffic
    # 4. Monitor

    # Simplified example:
    rsync -avz --delete dist/ user@prod-server:/var/www/app-new/
fi
\```

### Step 6: Health Checks

\```bash
echo "🏥 Running health checks..."

# Wait for deployment to stabilize
sleep 5

# Check application is responding
if [ "$ENV" = "staging" ]; then
    HEALTH_URL="https://staging.example.com/health"
else
    HEALTH_URL="https://example.com/health"
fi

HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" $HEALTH_URL)

if [ "$HTTP_STATUS" != "200" ]; then
    echo "❌ Health check failed: $HTTP_STATUS"
    echo "Rolling back..."
    # Rollback procedure here
    exit 1
fi

echo "✅ Health check passed"
\```

### Step 7: Smoke Tests

\```bash
echo "🧪 Running smoke tests..."

# Test critical paths
curl -f $HEALTH_URL/api/status || exit 1
curl -f $HEALTH_URL/api/version || exit 1

echo "✅ Smoke tests passed"
\```

### Step 8: Tag Release (production only)

\```bash
if [ "$ENV" = "production" ]; then
    VERSION=$(node -p "require('./package.json').version")
    git tag -a "v$VERSION" -m "Production release $VERSION"
    git push origin "v$VERSION"
fi
\```

### Step 9: Notifications

\```bash
# Notify team (if Slack MCP available)
MESSAGE="🚀 Deployed to $ENV
Version: $VERSION
Branch: $BRANCH
By: $(git config user.name)
Time: $(date)"

echo "$MESSAGE"

# Use Slack MCP or webhook
# curl -X POST $SLACK_WEBHOOK -d "{\"text\": \"$MESSAGE\"}"
\```

### Step 10: Summary

\```
━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ DEPLOYMENT SUCCESSFUL
━━━━━━━━━━━━━━━━━━━━━━━━━━

Environment: $ENV
Version: $VERSION
URL: $HEALTH_URL
Time: 2m 34s

Health: ✅ Passing
Tests: ✅ All passed
Build: ✅ Successful

🎉 Deployment complete!
\```

## Rollback Procedure

If deployment fails or --rollback flag used:

\```bash
echo "⏮️  Rolling back..."

# Restore previous version
rsync -avz --delete $BACKUP_DIR/ user@$SERVER:/var/www/app/

# Verify rollback
curl -f $HEALTH_URL/health

echo "✅ Rollback complete"
\```
```

## Features

### Safety Checks
- Git status verification
- Branch requirements
- Environment validation
- Confirmation prompts
- Health checks

### Deployment Strategies
- **Simple**: Direct file copy
- **Blue-Green**: Zero-downtime switches
- **Canary**: Gradual rollout
- **Rolling**: Incremental updates

### Error Handling
- Automatic rollback on failure
- Backup before deployment
- Health check verification
- Clear error messages

### Monitoring
- Deployment metrics
- Health endpoint checks
- Performance monitoring
- Error rate tracking

## Customization

### Add Docker Deployment

```markdown
### Deploy with Docker

\```bash
# Build image
docker build -t myapp:$VERSION .

# Push to registry
docker push myapp:$VERSION

# Deploy to Kubernetes
kubectl set image deployment/myapp myapp=myapp:$VERSION

# Watch rollout
kubectl rollout status deployment/myapp
\```
```

### Add Database Migrations

```markdown
### Run Migrations

\```bash
echo "🗄️  Running migrations..."

# Backup database first
pg_dump mydb > backup-$(date +%s).sql

# Run migrations
npm run migrate

# Verify
npm run migrate:status
\```
```

### Add Performance Tests

```markdown
### Performance Tests

\```bash
echo "⚡ Running performance tests..."

# Lighthouse CI
lhci autorun

# Load testing
artillery run load-test.yml

# Check response times
curl -w "@curl-format.txt" -o /dev/null -s $HEALTH_URL
\```
```

## Best Practices

### ✅ Do:
- Always run tests before deploy
- Require confirmation for production
- Implement health checks
- Create backups for rollback
- Log all deployments
- Notify team
- Tag releases

### ❌ Don't:
- Deploy without tests
- Skip health checks
- Deploy from feature branches to production
- Forget rollback procedures
- Deploy manually (use the command!)

## Troubleshooting

**Problem:** Deployment hangs

**Solution:** Add timeouts:
```bash
timeout 300 npm run build || {
    echo "Build timed out"
    exit 1
}
```

**Problem:** Rollback needed

**Solution:**
```bash
/deploy production --rollback
```

**Problem:** Health check fails

**Solution:** Automatic rollback triggers, check logs

## Next Steps

1. Install deploy command
2. Configure for your infrastructure
3. Test in staging first
4. Add team-specific steps
5. Integrate with CI/CD

---

**Pro Tip:** Combine with a deployment-tracker skill that stores deployment history in Memory MCP!
