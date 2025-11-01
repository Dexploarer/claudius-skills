---
name: advanced-architecture-skill
description: Design and implement complete application features including backend API, frontend components, database schema, tests, and documentation. Use when user asks to "implement feature", "build complete system", or "create end-to-end functionality"
allowed-tools: [Write, Read, Edit, Bash, Grep, Glob, Task]
---

# Advanced Architecture Skill - Full-Stack Feature Implementation

A comprehensive skill that handles complete feature implementation across the entire stack with best practices, testing, and documentation.

## When to Use

This skill activates for complex, multi-layered tasks:
- "Implement user authentication feature"
- "Build a complete e-commerce cart system"
- "Create an analytics dashboard with real-time data"
- "Design and implement a multi-tenant system"

## Capabilities

This skill can:
1. 🏗️ Design system architecture
2. 🗄️ Create database schemas
3. 🔧 Implement backend APIs
4. 🎨 Build frontend components
5. ✅ Write comprehensive tests
6. 📚 Generate documentation
7. 🚀 Provide deployment guidance
8. 🔒 Include security best practices

## Workflow

### Phase 1: Requirements Analysis (10 minutes)

**Gather Information:**
```markdown
## Feature Requirements Checklist

### Functional Requirements
- [ ] What is the core functionality?
- [ ] Who are the users?
- [ ] What are the use cases?
- [ ] What data needs to be stored?
- [ ] What are the business rules?

### Non-Functional Requirements
- [ ] Performance requirements? (response time, throughput)
- [ ] Security requirements? (auth, data protection)
- [ ] Scalability requirements? (concurrent users, data volume)
- [ ] Availability requirements? (uptime, disaster recovery)

### Technical Requirements
- [ ] Technology stack constraints?
- [ ] Integration requirements?
- [ ] Data migration needs?
- [ ] Backwards compatibility?
```

**Ask Clarifying Questions:**
```
1. "What's the expected user load?" (1K/10K/100K/1M users)
2. "Any specific security requirements?" (GDPR, HIPAA, etc.)
3. "Preferred database?" (PostgreSQL, MongoDB, etc.)
4. "Frontend framework?" (React, Vue, Angular)
5. "API style?" (REST, GraphQL, gRPC)
```

### Phase 2: Architecture Design (15 minutes)

**Analyze Existing Codebase:**
```bash
# Use Grep and Glob to understand current structure
1. Find existing API patterns
2. Identify database schema conventions
3. Check testing approaches
4. Review error handling patterns
5. Understand auth/security setup
```

**Design System Architecture:**
```markdown
## System Architecture

### High-Level Design
```
┌─────────────┐
│   Client    │ (React/Vue/Angular)
└──────┬──────┘
       │ HTTPS/WSS
┌──────▼──────┐
│  API Gateway│ (Express/FastAPI/Spring)
└──────┬──────┘
       │
   ┌───┴───┐
   │       │
┌──▼──┐ ┌─▼───┐
│Auth │ │ App │
│Svc  │ │Logic│
└──┬──┘ └──┬──┘
   │       │
┌──▼───────▼──┐
│  Database   │ (PostgreSQL/MongoDB)
└─────────────┘
```

### Component Breakdown
1. **Frontend Layer**
   - Components
   - State management
   - API client
   - Routing

2. **API Layer**
   - Endpoints
   - Validation
   - Business logic
   - Error handling

3. **Data Layer**
   - Schema design
   - Migrations
   - Indexes
   - Query optimization

4. **Infrastructure**
   - Caching (Redis)
   - Queue (RabbitMQ/Kafka)
   - Storage (S3/Cloud Storage)
   - Monitoring (Sentry/DataDog)
```

**Create Technical Specification:**
```markdown
## Technical Specification

### API Endpoints

#### POST /api/v1/{resource}
**Purpose:** Create new {resource}

**Request:**
```json
{
  "field1": "string",
  "field2": "number",
  "field3": {
    "nested": "object"
  }
}
```

**Response:** 201 Created
```json
{
  "id": "uuid",
  "created_at": "ISO8601",
  "data": { /* resource data */ }
}
```

**Errors:**
- 400: Validation error
- 401: Unauthorized
- 409: Conflict (duplicate)
- 500: Server error

### Database Schema

```sql
CREATE TABLE {resource} (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  field1 VARCHAR(255) NOT NULL,
  field2 INTEGER DEFAULT 0,
  metadata JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,

  -- Indexes for performance
  INDEX idx_{resource}_user_id (user_id),
  INDEX idx_{resource}_created_at (created_at DESC),

  -- Constraints
  CONSTRAINT unique_field1_per_user UNIQUE (user_id, field1)
);

-- Trigger for updated_at
CREATE TRIGGER update_{resource}_updated_at
  BEFORE UPDATE ON {resource}
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();
```

### State Management (Frontend)

```typescript
interface {Resource}State {
  items: {Resource}[];
  loading: boolean;
  error: Error | null;
  selectedId: string | null;
}

interface {Resource}Actions {
  fetch: () => Promise<void>;
  create: (data: Create{Resource}Input) => Promise<{Resource}>;
  update: (id: string, data: Update{Resource}Input) => Promise<{Resource}>;
  delete: (id: string) => Promise<void>;
  select: (id: string | null) => void;
}
```
```

### Phase 3: Implementation (60-90 minutes)

**Step 1: Database Layer**

```sql
-- migrations/001_create_{resource}_table.sql

-- Create table
CREATE TABLE {resource} (
  -- Schema from design phase
);

-- Create indexes
CREATE INDEX idx_{resource}_lookup ON {resource}(field1, field2);

-- Create views if needed
CREATE VIEW {resource}_summary AS
  SELECT
    user_id,
    COUNT(*) as total,
    MAX(created_at) as last_created
  FROM {resource}
  WHERE deleted_at IS NULL
  GROUP BY user_id;

-- Add comments for documentation
COMMENT ON TABLE {resource} IS 'Stores {description}';
COMMENT ON COLUMN {resource}.field1 IS '{field description}';
```

**Step 2: Backend API**

```typescript
// src/api/routes/{resource}.ts

import { Router } from 'express';
import { authenticate } from '@/middleware/auth';
import { validate } from '@/middleware/validation';
import { {Resource}Controller } from '@/controllers/{resource}';
import { create{Resource}Schema, update{Resource}Schema } from '@/schemas/{resource}';

const router = Router();
const controller = new {Resource}Controller();

// List all (with pagination, filtering, sorting)
router.get(
  '/',
  authenticate,
  controller.list.bind(controller)
);

// Get one by ID
router.get(
  '/:id',
  authenticate,
  controller.getById.bind(controller)
);

// Create new
router.post(
  '/',
  authenticate,
  validate(create{Resource}Schema),
  controller.create.bind(controller)
);

// Update existing
router.put(
  '/:id',
  authenticate,
  validate(update{Resource}Schema),
  controller.update.bind(controller)
);

// Delete (soft delete)
router.delete(
  '/:id',
  authenticate,
  controller.delete.bind(controller)
);

export default router;
```

```typescript
// src/controllers/{resource}.ts

import { Request, Response, NextFunction } from 'express';
import { {Resource}Service } from '@/services/{resource}';
import { AppError } from '@/utils/errors';
import { logger } from '@/utils/logger';

export class {Resource}Controller {
  private service: {Resource}Service;

  constructor() {
    this.service = new {Resource}Service();
  }

  async list(req: Request, res: Response, next: NextFunction) {
    try {
      const { page = 1, limit = 20, sort = '-created_at', filter } = req.query;

      const result = await this.service.list({
        userId: req.user.id,
        page: Number(page),
        limit: Number(limit),
        sort: String(sort),
        filter: filter ? JSON.parse(String(filter)) : {},
      });

      res.json({
        data: result.items,
        pagination: {
          page: result.page,
          limit: result.limit,
          total: result.total,
          pages: Math.ceil(result.total / result.limit),
        },
      });
    } catch (error) {
      next(error);
    }
  }

  async getById(req: Request, res: Response, next: NextFunction) {
    try {
      const { id } = req.params;

      const item = await this.service.getById(id, req.user.id);

      if (!item) {
        throw new AppError(404, 'Resource not found');
      }

      res.json({ data: item });
    } catch (error) {
      next(error);
    }
  }

  async create(req: Request, res: Response, next: NextFunction) {
    try {
      const item = await this.service.create({
        ...req.body,
        userId: req.user.id,
      });

      logger.info(`{Resource} created`, { id: item.id, userId: req.user.id });

      res.status(201).json({ data: item });
    } catch (error) {
      next(error);
    }
  }

  async update(req: Request, res: Response, next: NextFunction) {
    try {
      const { id } = req.params;

      const item = await this.service.update(id, req.user.id, req.body);

      if (!item) {
        throw new AppError(404, 'Resource not found');
      }

      logger.info(`{Resource} updated`, { id, userId: req.user.id });

      res.json({ data: item });
    } catch (error) {
      next(error);
    }
  }

  async delete(req: Request, res: Response, next: NextFunction) {
    try {
      const { id } = req.params;

      await this.service.delete(id, req.user.id);

      logger.info(`{Resource} deleted`, { id, userId: req.user.id });

      res.status(204).send();
    } catch (error) {
      next(error);
    }
  }
}
```

```typescript
// src/services/{resource}.ts

import { db } from '@/database';
import { {Resource} } from '@/types/{resource}';
import { AppError } from '@/utils/errors';
import { cache } from '@/utils/cache';

export class {Resource}Service {
  async list(options: ListOptions): Promise<ListResult<{Resource}>> {
    const { userId, page, limit, sort, filter } = options;

    // Build query
    const query = db.select().from('{resource}')
      .where('user_id', userId)
      .where('deleted_at', null);

    // Apply filters
    Object.entries(filter).forEach(([key, value]) => {
      query.where(key, value);
    });

    // Apply sorting
    const [sortField, sortOrder] = sort.startsWith('-')
      ? [sort.substring(1), 'DESC']
      : [sort, 'ASC'];
    query.orderBy(sortField, sortOrder);

    // Apply pagination
    const offset = (page - 1) * limit;
    query.limit(limit).offset(offset);

    // Execute
    const [items, [{ count }]] = await Promise.all([
      query,
      db.count().from('{resource}')
        .where('user_id', userId)
        .where('deleted_at', null)
    ]);

    return {
      items,
      page,
      limit,
      total: count,
    };
  }

  async getById(id: string, userId: string): Promise<{Resource} | null> {
    // Try cache first
    const cacheKey = `{resource}:${id}`;
    const cached = await cache.get(cacheKey);
    if (cached) return JSON.parse(cached);

    // Query database
    const item = await db.selectOne()
      .from('{resource}')
      .where('id', id)
      .where('user_id', userId)
      .where('deleted_at', null);

    // Cache result
    if (item) {
      await cache.set(cacheKey, JSON.stringify(item), 300); // 5 min TTL
    }

    return item;
  }

  async create(data: Create{Resource}Input): Promise<{Resource}> {
    // Validate business rules
    await this.validateBusinessRules(data);

    // Insert
    const [item] = await db.insert({
      ...data,
      created_at: new Date(),
      updated_at: new Date(),
    }).into('{resource}').returning('*');

    // Invalidate cache
    await cache.del(`{resource}:list:${data.userId}`);

    // Publish event
    await this.publishEvent('created', item);

    return item;
  }

  async update(
    id: string,
    userId: string,
    data: Update{Resource}Input
  ): Promise<{Resource} | null> {
    // Check ownership
    const existing = await this.getById(id, userId);
    if (!existing) return null;

    // Validate business rules
    await this.validateBusinessRules({ ...existing, ...data });

    // Update
    const [item] = await db.update({
      ...data,
      updated_at: new Date(),
    })
      .where('id', id)
      .where('user_id', userId)
      .into('{resource}')
      .returning('*');

    // Invalidate cache
    await cache.del(`{resource}:${id}`);
    await cache.del(`{resource}:list:${userId}`);

    // Publish event
    await this.publishEvent('updated', item);

    return item;
  }

  async delete(id: string, userId: string): Promise<void> {
    // Soft delete
    await db.update({ deleted_at: new Date() })
      .where('id', id)
      .where('user_id', userId)
      .into('{resource}');

    // Invalidate cache
    await cache.del(`{resource}:${id}`);
    await cache.del(`{resource}:list:${userId}`);

    // Publish event
    await this.publishEvent('deleted', { id, userId });
  }

  private async validateBusinessRules(data: Partial<{Resource}>): Promise<void> {
    // Example validation
    if (data.field1 && data.field1.length < 3) {
      throw new AppError(400, 'Field1 must be at least 3 characters');
    }

    // Check for duplicates
    const duplicate = await db.selectOne()
      .from('{resource}')
      .where('user_id', data.userId)
      .where('field1', data.field1)
      .where('deleted_at', null);

    if (duplicate && duplicate.id !== data.id) {
      throw new AppError(409, 'Duplicate resource');
    }
  }

  private async publishEvent(type: string, data: any): Promise<void> {
    // Publish to event bus for async processing
    // await eventBus.publish('{resource}.${type}', data);
  }
}
```

**Step 3: Frontend Components**

```typescript
// src/features/{resource}/components/{Resource}List.tsx

import React from 'react';
import { use{Resource}List } from '../hooks/use{Resource}List';
import { {Resource}Card } from './{Resource}Card';
import { LoadingSpinner } from '@/components/LoadingSpinner';
import { ErrorMessage } from '@/components/ErrorMessage';
import { Pagination } from '@/components/Pagination';

export const {Resource}List: React.FC = () => {
  const {
    items,
    loading,
    error,
    pagination,
    refetch,
  } = use{Resource}List();

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage error={error} onRetry={refetch} />;
  if (!items.length) return <Empty{Resource}State />;

  return (
    <div className="resource-list">
      <div className="grid">
        {items.map(item => (
          <{Resource}Card key={item.id} item={item} />
        ))}
      </div>

      <Pagination
        page={pagination.page}
        pages={pagination.pages}
        total={pagination.total}
        onPageChange={refetch}
      />
    </div>
  );
};
```

**Step 4: Comprehensive Tests**

```typescript
// tests/integration/{resource}.test.ts

describe('{Resource} API', () => {
  let authToken: string;
  let testUser: User;

  beforeAll(async () => {
    // Setup test database
    await setupTestDb();

    // Create test user
    testUser = await createTestUser();
    authToken = generateToken(testUser);
  });

  afterAll(async () => {
    await cleanupTestDb();
  });

  describe('POST /api/v1/{resource}', () => {
    it('creates a new resource', async () => {
      const response = await request(app)
        .post('/api/v1/{resource}')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          field1: 'test value',
          field2: 42,
        });

      expect(response.status).toBe(201);
      expect(response.body.data).toMatchObject({
        field1: 'test value',
        field2: 42,
        userId: testUser.id,
      });
    });

    it('validates required fields', async () => {
      const response = await request(app)
        .post('/api/v1/{resource}')
        .set('Authorization', `Bearer ${authToken}`)
        .send({});

      expect(response.status).toBe(400);
      expect(response.body.errors).toBeDefined();
    });

    it('prevents duplicate resources', async () => {
      // Create first
      await request(app)
        .post('/api/v1/{resource}')
        .set('Authorization', `Bearer ${authToken}`)
        .send({ field1: 'unique', field2: 1 });

      // Try duplicate
      const response = await request(app)
        .post('/api/v1/{resource}')
        .set('Authorization', `Bearer ${authToken}`)
        .send({ field1: 'unique', field2: 2 });

      expect(response.status).toBe(409);
    });
  });

  describe('GET /api/v1/{resource}', () => {
    it('lists resources with pagination', async () => {
      // Create test data
      await createMultiple{Resource}s(25, testUser.id);

      const response = await request(app)
        .get('/api/v1/{resource}?page=2&limit=10')
        .set('Authorization', `Bearer ${authToken}`);

      expect(response.status).toBe(200);
      expect(response.body.data).toHaveLength(10);
      expect(response.body.pagination).toMatchObject({
        page: 2,
        limit: 10,
        pages: 3,
        total: 25,
      });
    });

    it('filters resources', async () => {
      const response = await request(app)
        .get('/api/v1/{resource}?filter=${encodeURIComponent(JSON.stringify({ field2: 42 }))}')
        .set('Authorization', `Bearer ${authToken}`);

      expect(response.status).toBe(200);
      response.body.data.forEach(item => {
        expect(item.field2).toBe(42);
      });
    });
  });
});
```

### Phase 4: Documentation (15 minutes)

```markdown
# {Feature} Implementation Guide

## Overview

{Brief description of the feature and its purpose}

## Architecture

{High-level architecture diagram and explanation}

## API Documentation

### Endpoints

#### List {Resource}s
```
GET /api/v1/{resource}
```

**Query Parameters:**
- `page` (number, default: 1): Page number
- `limit` (number, default: 20): Items per page
- `sort` (string, default: '-created_at'): Sort field (prefix with - for DESC)
- `filter` (JSON string): Filter criteria

**Response:**
```json
{
  "data": [{Resource}[]],
  "pagination": {
    "page": number,
    "limit": number,
    "total": number,
    "pages": number
  }
}
```

[Continue with all endpoints...]

## Database Schema

{Include schema diagrams and explanations}

## Frontend Components

### Component Tree
```
{Feature}Page
├── {Resource}List
│   ├── {Resource}Card
│   │   ├── {Resource}Actions
│   │   └── {Resource}Details
│   └── Pagination
└── {Resource}Form
    ├── {Resource}Input
    └── {Resource}Submit
```

## Testing

### Running Tests
```bash
# Unit tests
npm test

# Integration tests
npm run test:integration

# E2E tests
npm run test:e2e

# Coverage
npm run test:coverage
```

### Test Coverage Requirements
- Minimum 80% code coverage
- All edge cases covered
- Error scenarios tested
- Performance tests for critical paths

## Deployment

### Prerequisites
- Node.js 18+
- PostgreSQL 14+
- Redis 6+

### Environment Variables
```env
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
REDIS_URL=redis://localhost:6379
API_SECRET=your-secret-key
```

### Deployment Steps
1. Run migrations
2. Build frontend
3. Start backend server
4. Verify health checks

## Security Considerations

- ✅ Authentication required for all endpoints
- ✅ Authorization checks per resource
- ✅ Input validation and sanitization
- ✅ Rate limiting configured
- ✅ SQL injection prevention (parameterized queries)
- ✅ XSS prevention (React escaping)
- ✅ CSRF protection (tokens)
- ✅ Secure headers (helmet.js)

## Performance Optimization

- ✅ Database indexes on frequently queried fields
- ✅ Caching layer (Redis) for read-heavy operations
- ✅ Query optimization (N+1 prevention)
- ✅ Frontend code splitting
- ✅ API response compression
- ✅ CDN for static assets

## Monitoring

### Metrics to Track
- API response times (p50, p95, p99)
- Error rates
- Database query performance
- Cache hit/miss rates
- Active users

### Alerts
- Response time > 500ms
- Error rate > 1%
- Database connections > 80%

## Troubleshooting

### Common Issues

**Issue: Slow query performance**
- Solution: Check explain plan, add indexes

**Issue: High memory usage**
- Solution: Implement pagination, optimize queries

**Issue: Intermittent errors**
- Solution: Check logs, verify network connectivity

## Future Enhancements

- [ ] Real-time updates (WebSocket)
- [ ] Export to CSV/PDF
- [ ] Bulk operations
- [ ] Advanced filtering/search
- [ ] Audit logging
```

### Phase 5: Review and Validation

**Final Checklist:**
```markdown
## Implementation Checklist

### Code Quality
- [ ] No TypeScript errors
- [ ] No ESLint warnings
- [ ] Code formatted (Prettier)
- [ ] Comments for complex logic
- [ ] TODO items documented

### Testing
- [ ] All tests pass
- [ ] Coverage > 80%
- [ ] Edge cases covered
- [ ] Error scenarios tested
- [ ] Performance tests pass

### Security
- [ ] Authentication implemented
- [ ] Authorization checks present
- [ ] Input validation complete
- [ ] No hardcoded secrets
- [ ] Security headers configured

### Documentation
- [ ] API documented
- [ ] README updated
- [ ] Architecture diagram created
- [ ] Deployment guide written
- [ ] Troubleshooting section added

### Performance
- [ ] Database indexes added
- [ ] Caching implemented
- [ ] Queries optimized
- [ ] Frontend optimized
- [ ] Load tested

### Deployment
- [ ] Migrations created
- [ ] Environment variables documented
- [ ] Health checks implemented
- [ ] Rollback plan created
- [ ] Monitoring configured
```

## Success Criteria

A successful implementation includes:
- ✅ All functional requirements met
- ✅ All tests passing
- ✅ Documentation complete
- ✅ Performance benchmarks met
- ✅ Security standards followed
- ✅ Code review approved
- ✅ Deployment successful

## Advanced Patterns

### Event-Driven Architecture

```typescript
// Implement event sourcing for audit trail
class {Resource}EventStore {
  async append(event: {Resource}Event): Promise<void> {
    await db.insert({
      aggregate_id: event.aggregateId,
      event_type: event.type,
      event_data: event.data,
      user_id: event.userId,
      created_at: new Date(),
    }).into('{resource}_events');

    await this.publishToEventBus(event);
  }

  async getHistory(aggregateId: string): Promise<{Resource}Event[]> {
    return db.select()
      .from('{resource}_events')
      .where('aggregate_id', aggregateId)
      .orderBy('created_at', 'ASC');
  }
}
```

### CQRS Pattern

```typescript
// Separate read and write models
class {Resource}WriteModel {
  async execute(command: {Resource}Command): Promise<void> {
    // Handle command, update write database
    // Publish event for read model sync
  }
}

class {Resource}ReadModel {
  async project(event: {Resource}Event): Promise<void> {
    // Update read-optimized database
    // Handle denormalization
  }
}
```

### Microservices Integration

```typescript
// Implement service communication
class {Resource}Gateway {
  async coordinateTransaction(data: TransactionData): Promise<void> {
    const saga = new Saga();

    try {
      // Step 1: Reserve inventory
      await saga.add(() =>
        this.inventoryService.reserve(data.items)
      );

      // Step 2: Process payment
      await saga.add(() =>
        this.paymentService.charge(data.payment)
      );

      // Step 3: Create order
      await saga.add(() =>
        this.orderService.create(data.order)
      );

      await saga.execute();
    } catch (error) {
      await saga.rollback();
      throw error;
    }
  }
}
```

## Notes

This advanced skill template demonstrates:
- Complete full-stack implementation
- Best practices across all layers
- Production-ready code patterns
- Comprehensive testing strategy
- Enterprise-grade architecture
- Scalability considerations
- Security best practices
- Documentation standards

Use this as a reference for implementing complex features that span multiple layers of your application.
