---
name: dockerfile-generator
description: Generates optimized Dockerfiles for various languages and frameworks with best practices (multi-stage builds, layer caching, security). Use when user asks to "create dockerfile", "dockerize app", "containerize", or "docker setup".
allowed-tools: [Read, Write, Glob, Grep, Bash]
---

# Dockerfile Generator

Generates production-ready Dockerfiles with multi-stage builds, optimized layer caching, and security best practices.

## When to Use

- "Create a Dockerfile"
- "Dockerize my application"
- "Container this app"
- "Setup Docker"
- "Optimize Dockerfile"

## Instructions

### 1. Detect Project Type

Scan for language/framework indicators:

```bash
# Node.js
[ -f "package.json" ] && echo "Node.js/JavaScript"

# Python
[ -f "requirements.txt" ] || [ -f "Pipfile" ] || [ -f "pyproject.toml" ] && echo "Python"

# Go
[ -f "go.mod" ] && echo "Go"

# Java
[ -f "pom.xml" ] || [ -f "build.gradle" ] && echo "Java"

# Ruby
[ -f "Gemfile" ] && echo "Ruby"

# PHP
[ -f "composer.json" ] && echo "PHP"

# Rust
[ -f "Cargo.toml" ] && echo "Rust"

# .NET
[ -f "*.csproj" ] && echo ".NET"
```

Read package files to determine framework (Express, Next.js, Django, Flask, etc.).

### 2. Generate Dockerfile by Language

## Node.js / JavaScript

**Basic Node.js:**
```dockerfile
# Multi-stage build for production
FROM node:20-alpine AS base

# Install dependencies only when needed
FROM base AS deps
WORKDIR /app

# Copy package files
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm ci --only=production

# Development dependencies (for build)
FROM base AS build-deps
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci

# Build stage
FROM build-deps AS build
WORKDIR /app
COPY . .
RUN npm run build

# Production stage
FROM base AS runner
WORKDIR /app

# Don't run as root
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nodejs

# Copy built app
COPY --from=deps --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=build --chown=nodejs:nodejs /app/dist ./dist
COPY --chown=nodejs:nodejs package.json ./

USER nodejs

EXPOSE 3000

ENV NODE_ENV=production
ENV PORT=3000

CMD ["node", "dist/index.js"]
```

**Next.js:**
```dockerfile
FROM node:20-alpine AS base

# Dependencies
FROM base AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm ci

# Builder
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Disable telemetry
ENV NEXT_TELEMETRY_DISABLED 1

RUN npm run build

# Production
FROM base AS runner
WORKDIR /app

ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT 3000

CMD ["node", "server.js"]
```

## Python

**Flask:**
```dockerfile
FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Dependencies
FROM base AS deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Production
FROM base AS runner

# Create non-root user
RUN useradd -m -u 1001 appuser

# Copy dependencies from deps stage
COPY --from=deps /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy application
COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
```

**Django:**
```dockerfile
FROM python:3.11-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Dependencies
FROM base AS deps
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Production
FROM base AS runner

# Create non-root user
RUN useradd -m -u 1001 django

# Copy dependencies
COPY --from=deps /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=deps /usr/bin/pg_* /usr/bin/

# Copy application
COPY --chown=django:django . .

# Collect static files
RUN python manage.py collectstatic --noinput

USER django

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "myproject.wsgi:application"]
```

## Go

**Go application:**
```dockerfile
# Build stage
FROM golang:1.21-alpine AS builder

WORKDIR /app

# Copy go mod files
COPY go.mod go.sum ./
RUN go mod download

# Copy source
COPY . .

# Build binary
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags="-w -s" -o main .

# Production stage (minimal image)
FROM scratch

# Copy CA certificates for HTTPS
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

# Copy binary from builder
COPY --from=builder /app/main /main

# Expose port
EXPOSE 8080

# Run binary
CMD ["/main"]
```

**With CGO (needs libc):**
```dockerfile
FROM golang:1.21-alpine AS builder

RUN apk add --no-cache gcc musl-dev

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN go build -o main .

# Production
FROM alpine:latest

RUN apk --no-cache add ca-certificates
WORKDIR /root/

COPY --from=builder /app/main .

EXPOSE 8080

CMD ["./main"]
```

## Java

**Spring Boot (Gradle):**
```dockerfile
# Build stage
FROM gradle:8-jdk17 AS build

WORKDIR /app

# Copy gradle files
COPY build.gradle settings.gradle ./
COPY gradle ./gradle

# Download dependencies (cached layer)
RUN gradle dependencies --no-daemon

# Copy source and build
COPY src ./src
RUN gradle build --no-daemon -x test

# Production stage
FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

# Create non-root user
RUN addgroup -S spring && adduser -S spring -G spring
USER spring:spring

# Copy jar from build stage
COPY --from=build /app/build/libs/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

**Spring Boot (Maven):**
```dockerfile
FROM maven:3.9-eclipse-temurin-17 AS build

WORKDIR /app

# Copy pom and download dependencies (cached)
COPY pom.xml .
RUN mvn dependency:go-offline

# Copy source and build
COPY src ./src
RUN mvn package -DskipTests

# Production
FROM eclipse-temurin:17-jre-alpine

RUN addgroup -S spring && adduser -S spring -G spring
USER spring:spring

WORKDIR /app

COPY --from=build /app/target/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

## Ruby

**Rails:**
```dockerfile
FROM ruby:3.2-alpine AS base

# Install system dependencies
RUN apk add --no-cache \
    build-base \
    postgresql-dev \
    nodejs \
    yarn \
    tzdata

WORKDIR /app

# Dependencies
FROM base AS deps

COPY Gemfile Gemfile.lock ./
RUN bundle install --jobs 4 --retry 3

# Production
FROM base AS runner

# Copy dependencies
COPY --from=deps /usr/local/bundle /usr/local/bundle

# Copy application
COPY . .

# Precompile assets
RUN bundle exec rake assets:precompile

# Create non-root user
RUN adduser -D rails
USER rails

EXPOSE 3000

CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]
```

## Rust

**Rust application:**
```dockerfile
# Build stage
FROM rust:1.75-alpine AS builder

RUN apk add --no-cache musl-dev

WORKDIR /app

# Copy manifests
COPY Cargo.toml Cargo.lock ./

# Cache dependencies
RUN mkdir src && \
    echo "fn main() {}" > src/main.rs && \
    cargo build --release && \
    rm -rf src

# Copy source and build
COPY src ./src
RUN touch src/main.rs && cargo build --release

# Production (minimal)
FROM alpine:latest

RUN apk --no-cache add ca-certificates

WORKDIR /root/

COPY --from=builder /app/target/release/app /usr/local/bin/app

EXPOSE 8080

CMD ["app"]
```

## PHP

**Laravel:**
```dockerfile
FROM php:8.2-fpm-alpine AS base

# Install system dependencies
RUN apk add --no-cache \
    postgresql-dev \
    zip \
    unzip

# Install PHP extensions
RUN docker-php-ext-install pdo pdo_pgsql

# Install composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html

# Dependencies
FROM base AS deps
COPY composer.json composer.lock ./
RUN composer install --no-dev --no-scripts --no-autoloader

# Production
FROM base AS runner

# Copy dependencies
COPY --from=deps /var/www/html/vendor ./vendor

# Copy application
COPY . .

# Generate autoloader
RUN composer dump-autoload --optimize

# Set permissions
RUN chown -R www-data:www-data /var/www/html

USER www-data

EXPOSE 9000

CMD ["php-fpm"]
```

### 3. Add .dockerignore

Create .dockerignore to reduce build context:

```dockerignore
# Version control
.git
.gitignore

# Dependencies (will be installed in container)
node_modules
vendor
venv
__pycache__

# Build artifacts
dist
build
*.pyc
*.pyo

# IDE
.vscode
.idea
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
logs
*.log

# Test files
test
tests
**/*.test.js
**/*.spec.js

# Documentation
README.md
docs

# CI/CD
.github
.gitlab-ci.yml

# Environment
.env
.env.local
*.env

# Misc
coverage
.cache
tmp
temp
```

### 4. Optimization Techniques

**Layer caching:**
- Copy dependency files first
- Install dependencies (cached)
- Copy source code (changes frequently)

**Multi-stage builds:**
- Build stage: All tools needed
- Production stage: Only runtime + artifacts

**Minimize layers:**
- Combine RUN commands with &&
- Clean up in same layer

**Use alpine images:**
- Much smaller (5-50MB vs 500MB+)
- Faster pulls and deploys

**Example optimization:**

```dockerfile
# ❌ BAD: Many layers, large image
FROM node:20
WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "start"]

# ✅ GOOD: Optimized
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:20-alpine
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
CMD ["node", "index.js"]
```

### 5. Security Best Practices

**Don't run as root:**
```dockerfile
RUN adduser -D appuser
USER appuser
```

**Use specific versions:**
```dockerfile
# ❌ BAD: Latest can break
FROM node:latest

# ✅ GOOD: Pinned version
FROM node:20.10.0-alpine3.19
```

**Scan for vulnerabilities:**
```bash
docker scan myimage:latest
```

**Multi-stage to exclude dev dependencies:**
```dockerfile
# Build with dev dependencies
FROM node:20 AS build
RUN npm ci  # Includes devDependencies

# Production without dev dependencies
FROM node:20-alpine
COPY --from=build /app/node_modules ./node_modules
```

### 6. Docker Compose (Optional)

Offer to create docker-compose.yml:

```yaml
version: '3.9'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgresql://postgres:password@db:5432/myapp
    depends_on:
      - db
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  postgres_data:
```

### 7. Provide Build Instructions

```bash
# Build image
docker build -t myapp:latest .

# Run container
docker run -p 3000:3000 myapp:latest

# With environment variables
docker run -p 3000:3000 \
  -e DATABASE_URL=postgresql://... \
  myapp:latest

# Using docker-compose
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop
docker-compose down
```

### Best Practices Checklist

- [ ] Multi-stage build (separate build and runtime)
- [ ] Use alpine or slim images
- [ ] Copy package files before source (caching)
- [ ] Don't run as root (create user)
- [ ] Pin specific versions
- [ ] Include .dockerignore
- [ ] Minimize layers (combine RUN commands)
- [ ] Clean up in same layer (apt-get clean, rm -rf)
- [ ] Use COPY instead of ADD
- [ ] Set ENV variables
- [ ] Document EXPOSE ports
- [ ] Health check (optional)
- [ ] Build-time secrets (--secret)
- [ ] Security scan image
