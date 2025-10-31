Deploy application to specified environment with safety checks.

## Instructions

1. Check which environment (staging/production)
2. Run pre-deployment checks
3. Build application
4. Run tests
5. Deploy
6. Verify deployment
7. Rollback if issues

## Steps

### 1. Pre-Deployment Checks

```bash
# Check branch
BRANCH=$(git branch --show-current)
if [ "$BRANCH" != "main" ] && [ "$ENV" = "production" ]; then
  echo "❌ Cannot deploy to production from $BRANCH"
  exit 1
fi

# Check uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
  echo "⚠️  Uncommitted changes detected"
  exit 1
fi

# Check if tests pass
npm test
```

### 2. Build

```bash
echo "🔨 Building application..."
npm run build

if [ $? -ne 0 ]; then
  echo "❌ Build failed"
  exit 1
fi
```

### 3. Deploy

```bash
echo "🚀 Deploying to $ENV..."

case $ENV in
  staging)
    # Deploy to staging
    deploy-to-staging
    ;;
  production)
    # Deploy to production
    deploy-to-production
    ;;
esac
```

### 4. Verify

```bash
# Health check
curl -f https://$ENV.example.com/health
```

## Usage

```bash
/deploy-script staging
/deploy-script production
```

## Safety Features

- Branch checking
- Test enforcement
- Build verification
- Health checks
- Rollback capability
