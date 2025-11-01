---
name: github-workflow-generator
description: Generate GitHub Actions workflows for CI/CD, testing, deployment, and automation
allowed-tools: [Read, Write, Edit, Grep, Glob]
---

# GitHub Workflow Generator

Generate production-ready GitHub Actions workflows for continuous integration, deployment, and automation.

## What This Skill Creates

Complete GitHub Actions workflows for:
- ✅ CI/CD pipelines
- ✅ Automated testing (Node.js, Python, Go, Rust, PHP)
- ✅ Code quality checks (linting, formatting)
- ✅ Security scanning
- ✅ Deployment (AWS, Azure, GCP, Vercel, Netlify)
- ✅ Release automation
- ✅ Dependency updates
- ✅ Custom automation workflows

## Usage

```
"Generate a GitHub Actions workflow for Node.js CI with tests and linting"
"Create a deployment workflow for deploying to AWS ECS"
"Build a workflow for automated releases with semantic versioning"
"Generate a security scanning workflow with CodeQL"
```

## Instructions for Claude

When the user requests a GitHub workflow:

### Step 1: Gather Requirements

Ask for:
1. **Workflow purpose**: CI/CD, deployment, automation, etc.
2. **Technology stack**: Node.js, Python, Go, Rust, PHP, etc.
3. **Triggers**: Push, PR, schedule, manual, etc.
4. **Target environment**: AWS, Azure, GCP, Vercel, etc. (for deployments)
5. **Additional requirements**: Matrix builds, caching, secrets, etc.

### Step 2: Create Workflow Directory

```bash
mkdir -p .github/workflows
```

## Common Workflow Templates

### Template 1: Node.js CI/CD

Generate `.github/workflows/node-ci.yml`:

```yaml
name: Node.js CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    name: Test on Node ${{ matrix.node-version }}
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x, 20.x]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run linter
        run: npm run lint

      - name: Run type check
        run: npm run type-check
        if: hashFiles('tsconfig.json') != ''

      - name: Run tests
        run: npm test -- --coverage

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        if: matrix.node-version == '20.x'
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          fail_ci_if_error: true

      - name: Build
        run: npm run build

      - name: Archive production artifacts
        uses: actions/upload-artifact@v3
        if: github.ref == 'refs/heads/main' && matrix.node-version == '20.x'
        with:
          name: dist
          path: dist
          retention-days: 7

  lint:
    name: Lint and Format Check
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run ESLint
        run: npm run lint

      - name: Check Prettier formatting
        run: npm run format:check
        if: hashFiles('.prettierrc*') != ''
```

### Template 2: Python CI/CD

Generate `.github/workflows/python-ci.yml`:

```yaml
name: Python CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    name: Test on Python ${{ matrix.python-version }}
    runs-on: ubuntu-latest

    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install -r requirements-dev.txt

      - name: Run Black (formatter check)
        run: black --check .

      - name: Run isort (import sorting check)
        run: isort --check-only .

      - name: Run Flake8 (linter)
        run: flake8 .

      - name: Run mypy (type checker)
        run: mypy .
        if: hashFiles('mypy.ini') != ''

      - name: Run pytest
        run: |
          pytest --cov=. --cov-report=xml --cov-report=html

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        if: matrix.python-version == '3.12'
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./coverage.xml
          fail_ci_if_error: true

  security:
    name: Security Scan
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install bandit safety

      - name: Run Bandit (security linter)
        run: bandit -r . -f json -o bandit-report.json

      - name: Run Safety (dependency security check)
        run: safety check --json
```

### Template 3: Go CI/CD

Generate `.github/workflows/go-ci.yml`:

```yaml
name: Go CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    name: Test on Go ${{ matrix.go-version }}
    runs-on: ubuntu-latest

    strategy:
      matrix:
        go-version: ['1.21', '1.22']

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: ${{ matrix.go-version }}
          cache: true

      - name: Download dependencies
        run: go mod download

      - name: Verify dependencies
        run: go mod verify

      - name: Run go vet
        run: go vet ./...

      - name: Run golangci-lint
        uses: golangci/golangci-lint-action@v3
        with:
          version: latest

      - name: Run tests
        run: go test -v -race -coverprofile=coverage.txt -covermode=atomic ./...

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        if: matrix.go-version == '1.22'
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./coverage.txt
          fail_ci_if_error: true

      - name: Build
        run: go build -v ./...

  security:
    name: Security Scan
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run Gosec Security Scanner
        uses: securego/gosec@master
        with:
          args: '-no-fail -fmt sarif -out results.sarif ./...'

      - name: Upload SARIF file
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: results.sarif
```

### Template 4: Rust CI/CD

Generate `.github/workflows/rust-ci.yml`:

```yaml
name: Rust CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

env:
  CARGO_TERM_COLOR: always

jobs:
  test:
    name: Test on Rust ${{ matrix.rust-version }}
    runs-on: ubuntu-latest

    strategy:
      matrix:
        rust-version: [stable, nightly]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install Rust toolchain
        uses: dtolnay/rust-toolchain@master
        with:
          toolchain: ${{ matrix.rust-version }}
          components: rustfmt, clippy

      - name: Cache cargo registry
        uses: actions/cache@v3
        with:
          path: ~/.cargo/registry
          key: ${{ runner.os }}-cargo-registry-${{ hashFiles('**/Cargo.lock') }}

      - name: Cache cargo index
        uses: actions/cache@v3
        with:
          path: ~/.cargo/git
          key: ${{ runner.os }}-cargo-git-${{ hashFiles('**/Cargo.lock') }}

      - name: Cache cargo build
        uses: actions/cache@v3
        with:
          path: target
          key: ${{ runner.os }}-cargo-build-target-${{ hashFiles('**/Cargo.lock') }}

      - name: Check formatting
        run: cargo fmt -- --check
        if: matrix.rust-version == 'stable'

      - name: Run Clippy
        run: cargo clippy --all-targets --all-features -- -D warnings
        if: matrix.rust-version == 'stable'

      - name: Build
        run: cargo build --verbose

      - name: Run tests
        run: cargo test --verbose

      - name: Generate code coverage
        if: matrix.rust-version == 'stable'
        run: |
          cargo install cargo-tarpaulin
          cargo tarpaulin --out Xml

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        if: matrix.rust-version == 'stable'
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./cobertura.xml
          fail_ci_if_error: true

  security:
    name: Security Audit
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run cargo audit
        uses: actions-rs/audit-check@v1
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

### Template 5: PHP Laravel CI/CD

Generate `.github/workflows/php-ci.yml`:

```yaml
name: PHP CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    name: Test on PHP ${{ matrix.php-version }}
    runs-on: ubuntu-latest

    strategy:
      matrix:
        php-version: ['8.1', '8.2', '8.3']

    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_ROOT_PASSWORD: password
          MYSQL_DATABASE: test_db
        ports:
          - 3306:3306
        options: --health-cmd="mysqladmin ping" --health-interval=10s --health-timeout=5s --health-retries=3

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup PHP
        uses: shivammathur/setup-php@v2
        with:
          php-version: ${{ matrix.php-version }}
          extensions: mbstring, dom, fileinfo, mysql
          coverage: xdebug

      - name: Get Composer Cache Directory
        id: composer-cache
        run: echo "dir=$(composer config cache-files-dir)" >> $GITHUB_OUTPUT

      - name: Cache Composer dependencies
        uses: actions/cache@v3
        with:
          path: ${{ steps.composer-cache.outputs.dir }}
          key: ${{ runner.os }}-composer-${{ hashFiles('**/composer.lock') }}
          restore-keys: ${{ runner.os }}-composer-

      - name: Install dependencies
        run: composer install --prefer-dist --no-progress

      - name: Copy .env
        run: php -r "file_exists('.env') || copy('.env.example', '.env');"

      - name: Generate key
        run: php artisan key:generate

      - name: Directory Permissions
        run: chmod -R 777 storage bootstrap/cache

      - name: Run PHP CS Fixer
        run: vendor/bin/pint --test
        if: hashFiles('pint.json') != ''

      - name: Run PHPStan
        run: vendor/bin/phpstan analyse
        if: hashFiles('phpstan.neon') != ''

      - name: Execute tests
        env:
          DB_CONNECTION: mysql
          DB_HOST: 127.0.0.1
          DB_PORT: 3306
          DB_DATABASE: test_db
          DB_USERNAME: root
          DB_PASSWORD: password
        run: php artisan test --coverage --min=80
```

### Template 6: Docker Build and Push

Generate `.github/workflows/docker-build.yml`:

```yaml
name: Docker Build and Push

on:
  push:
    branches: [ main ]
    tags: [ 'v*.*.*' ]
  pull_request:
    branches: [ main ]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build-and-push:
    name: Build and Push Docker Image
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=semver,pattern={{major}}
            type=sha

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          platforms: linux/amd64,linux/arm64
```

### Template 7: Deploy to AWS ECS

Generate `.github/workflows/deploy-aws-ecs.yml`:

```yaml
name: Deploy to AWS ECS

on:
  push:
    branches: [ main ]
  workflow_dispatch:

env:
  AWS_REGION: us-east-1
  ECR_REPOSITORY: my-app
  ECS_SERVICE: my-app-service
  ECS_CLUSTER: my-app-cluster
  ECS_TASK_DEFINITION: my-app-task
  CONTAINER_NAME: my-app

jobs:
  deploy:
    name: Deploy to ECS
    runs-on: ubuntu-latest
    environment: production

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build, tag, and push image to Amazon ECR
        id: build-image
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          IMAGE_TAG: ${{ github.sha }}
        run: |
          docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
          docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
          echo "image=$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG" >> $GITHUB_OUTPUT

      - name: Fill in the new image ID in the Amazon ECS task definition
        id: task-def
        uses: aws-actions/amazon-ecs-render-task-definition@v1
        with:
          task-definition: task-definition.json
          container-name: ${{ env.CONTAINER_NAME }}
          image: ${{ steps.build-image.outputs.image }}

      - name: Deploy Amazon ECS task definition
        uses: aws-actions/amazon-ecs-deploy-task-definition@v1
        with:
          task-definition: ${{ steps.task-def.outputs.task-definition }}
          service: ${{ env.ECS_SERVICE }}
          cluster: ${{ env.ECS_CLUSTER }}
          wait-for-service-stability: true

      - name: Notify deployment success
        if: success()
        run: echo "Deployment to ECS successful!"

      - name: Notify deployment failure
        if: failure()
        run: echo "Deployment to ECS failed!"
```

### Template 8: Deploy to Vercel

Generate `.github/workflows/deploy-vercel.yml`:

```yaml
name: Deploy to Vercel

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  deploy:
    name: Deploy to Vercel
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
          cache: 'npm'

      - name: Install Vercel CLI
        run: npm install --global vercel@latest

      - name: Pull Vercel Environment Information
        run: vercel pull --yes --environment=${{ github.ref == 'refs/heads/main' && 'production' || 'preview' }} --token=${{ secrets.VERCEL_TOKEN }}

      - name: Build Project Artifacts
        run: vercel build ${{ github.ref == 'refs/heads/main' && '--prod' || '' }} --token=${{ secrets.VERCEL_TOKEN }}

      - name: Deploy Project Artifacts to Vercel
        id: deploy
        run: |
          url=$(vercel deploy --prebuilt ${{ github.ref == 'refs/heads/main' && '--prod' || '' }} --token=${{ secrets.VERCEL_TOKEN }})
          echo "url=$url" >> $GITHUB_OUTPUT

      - name: Comment PR with deployment URL
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '✅ Deployed to Vercel: ${{ steps.deploy.outputs.url }}'
            })
```

### Template 9: Semantic Release

Generate `.github/workflows/release.yml`:

```yaml
name: Release

on:
  push:
    branches:
      - main

permissions:
  contents: write
  issues: write
  pull-requests: write

jobs:
  release:
    name: Create Release
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          persist-credentials: false

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Verify the integrity of provenance attestations
        run: npm audit signatures

      - name: Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: npx semantic-release
```

Create `.releaserc.json`:

```json
{
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    "@semantic-release/npm",
    "@semantic-release/github",
    [
      "@semantic-release/git",
      {
        "assets": ["package.json", "CHANGELOG.md"],
        "message": "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
      }
    ]
  ]
}
```

### Template 10: CodeQL Security Scanning

Generate `.github/workflows/codeql.yml`:

```yaml
name: CodeQL Security Scan

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 0 * * 1'  # Run every Monday at midnight

jobs:
  analyze:
    name: Analyze Code
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: [ 'javascript', 'python' ]  # Customize based on your stack

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v2
        with:
          languages: ${{ matrix.language }}
          queries: security-extended,security-and-quality

      - name: Autobuild
        uses: github/codeql-action/autobuild@v2

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v2
        with:
          category: "/language:${{ matrix.language }}"
```

### Template 11: Dependency Update (Dependabot Alternative)

Generate `.github/workflows/dependency-update.yml`:

```yaml
name: Dependency Update

on:
  schedule:
    - cron: '0 0 * * 1'  # Run every Monday at midnight
  workflow_dispatch:

jobs:
  update-dependencies:
    name: Update Dependencies
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.PAT_TOKEN }}

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
          cache: 'npm'

      - name: Update dependencies
        run: |
          npm update
          npm audit fix || true

      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.PAT_TOKEN }}
          commit-message: 'chore: update dependencies'
          title: 'chore: update dependencies'
          body: |
            This PR updates project dependencies to their latest versions.

            Please review the changes and ensure all tests pass before merging.
          branch: dependency-updates
          delete-branch: true
```

### Template 12: Performance Testing

Generate `.github/workflows/performance.yml`:

```yaml
name: Performance Testing

on:
  pull_request:
    branches: [ main ]
  workflow_dispatch:

jobs:
  lighthouse:
    name: Lighthouse CI
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Run Lighthouse CI
        uses: treosh/lighthouse-ci-action@v10
        with:
          urls: |
            http://localhost:3000
            http://localhost:3000/about
          uploadArtifacts: true
          temporaryPublicStorage: true

  load-test:
    name: Load Testing with k6
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run k6 load test
        uses: grafana/k6-action@v0.3.0
        with:
          filename: tests/load-test.js

      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: k6-results
          path: results/
```

## Customization Guide

When generating workflows:

1. **Replace placeholders**:
   - `{service-name}` → Actual service name
   - `{environment}` → Target environment (staging, production)
   - `{region}` → AWS/Azure/GCP region

2. **Configure secrets** (in GitHub repository settings):
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `CODECOV_TOKEN`
   - `NPM_TOKEN`
   - `VERCEL_TOKEN`
   - `PAT_TOKEN` (Personal Access Token)

3. **Customize triggers**:
   - Add/remove branches
   - Change schedule cron expressions
   - Add path filters for specific files

4. **Adjust matrix builds**:
   - Add/remove language versions
   - Add OS variations (ubuntu, macos, windows)

5. **Configure environment protection**:
   - Set up GitHub Environments for production
   - Add required reviewers
   - Add environment secrets

## Best Practices

### Workflow Organization
- ✅ One workflow per purpose (CI, deploy, release)
- ✅ Use reusable workflows for common tasks
- ✅ Separate test and deploy jobs
- ✅ Use concurrency limits to prevent duplicate runs

### Performance
- ✅ Use caching for dependencies
- ✅ Use artifacts for build outputs
- ✅ Run jobs in parallel when possible
- ✅ Use matrix builds efficiently

### Security
- ✅ Never commit secrets
- ✅ Use GitHub secrets management
- ✅ Limit workflow permissions
- ✅ Use environment protection rules
- ✅ Enable security scanning

### Reliability
- ✅ Add timeout limits
- ✅ Use proper error handling
- ✅ Add retry logic for flaky steps
- ✅ Monitor workflow execution times
- ✅ Set up failure notifications

## Example: Complete CI/CD Pipeline

For a full-stack Node.js application:

```yaml
name: Complete CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  lint-and-test:
    name: Lint and Test
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20.x'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v3

  build:
    name: Build Application
    needs: lint-and-test
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-artifact@v3
        with:
          name: dist
          path: dist

  deploy-staging:
    name: Deploy to Staging
    needs: build
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment: staging

    steps:
      - uses: actions/download-artifact@v3
      - name: Deploy to staging
        run: echo "Deploy to staging..."

  deploy-production:
    name: Deploy to Production
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/download-artifact@v3
      - name: Deploy to production
        run: echo "Deploy to production..."
```

## Troubleshooting

**Workflow not triggering:**
- Check branch filters
- Verify file paths if using path filters
- Ensure workflow file is on the target branch

**Cache not working:**
- Verify cache key includes proper dependencies
- Check cache size limits (10GB per repository)
- Ensure cache restore happens before install

**Secrets not accessible:**
- Verify secret names match exactly
- Check environment-specific secrets
- Ensure proper permissions are set

---

**Generated with GitHub Workflow Generator** 🚀
