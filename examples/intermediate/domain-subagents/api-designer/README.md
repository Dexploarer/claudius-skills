# API Designer Subagent - Intermediate Example

A specialized subagent that designs RESTful APIs following industry best practices and conventions.

## What This Teaches

- Creating domain-specific subagents
- Restricting subagent tools for focused analysis
- API design principles
- RESTful conventions
- OpenAPI/Swagger integration
- Subagent output formatting

## Installation

```bash
# Copy to your project
cp subagent.md /path/to/your-project/.claude/agents/api-designer.md
```

## When to Use

Call this subagent when you need to:
- Design a new REST API
- Review existing API design
- Create API documentation
- Plan API endpoints for a feature
- Standardize API across team

## What It Does

The API Designer subagent provides:

1. **Endpoint Design** - Proper HTTP methods, URL structure, naming
2. **Request/Response Schemas** - JSON structure with validation
3. **Status Codes** - Appropriate HTTP status codes
4. **Error Handling** - Consistent error response format
5. **Documentation** - OpenAPI/Swagger specs
6. **Best Practices** - RESTful principles, security, versioning

## Example Usage

### Designing a New API

**You:**
```
"Call the api-designer subagent to design an API for a blog platform"
```

**Subagent Output:**

```markdown
# Blog Platform API Design

## Endpoints

### Posts

#### GET /api/v1/posts
List all blog posts with pagination

**Query Parameters:**
- `page` (number, optional): Page number (default: 1)
- `limit` (number, optional): Items per page (default: 20)
- `status` (string, optional): Filter by status (draft, published)
- `author_id` (number, optional): Filter by author

**Response (200 OK):**
\```json
{
  "data": [
    {
      "id": 1,
      "title": "My First Post",
      "slug": "my-first-post",
      "excerpt": "This is a summary...",
      "status": "published",
      "author": {
        "id": 123,
        "name": "John Doe"
      },
      "published_at": "2024-01-15T10:00:00Z",
      "created_at": "2024-01-14T08:00:00Z",
      "updated_at": "2024-01-15T09:30:00Z"
    }
  ],
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
\```

#### GET /api/v1/posts/{id}
Get a specific post

**Path Parameters:**
- `id` (number): Post ID

**Response (200 OK):**
\```json
{
  "data": {
    "id": 1,
    "title": "My First Post",
    "slug": "my-first-post",
    "content": "Full post content here...",
    "excerpt": "This is a summary...",
    "status": "published",
    "author": {
      "id": 123,
      "name": "John Doe",
      "email": "john@example.com"
    },
    "category": {
      "id": 5,
      "name": "Technology"
    },
    "tags": ["javascript", "tutorial"],
    "published_at": "2024-01-15T10:00:00Z",
    "created_at": "2024-01-14T08:00:00Z",
    "updated_at": "2024-01-15T09:30:00Z"
  }
}
\```

**Response (404 Not Found):**
\```json
{
  "error": {
    "code": "POST_NOT_FOUND",
    "message": "Post with ID 999 not found",
    "status": 404
  }
}
\```

#### POST /api/v1/posts
Create a new post

**Request Headers:**
- `Authorization: Bearer {token}`
- `Content-Type: application/json`

**Request Body:**
\```json
{
  "title": "New Post Title",
  "content": "Full post content...",
  "excerpt": "Brief summary",
  "status": "draft",
  "category_id": 5,
  "tags": ["javascript", "tutorial"]
}
\```

**Validation:**
- `title`: Required, max 200 characters
- `content`: Required
- `status`: One of: draft, published
- `category_id`: Optional, must exist
- `tags`: Optional array of strings

**Response (201 Created):**
\```json
{
  "data": {
    "id": 151,
    "title": "New Post Title",
    ...
  }
}
\```

**Response (400 Bad Request):**
\```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "status": 400,
    "details": {
      "title": ["Title is required"],
      "status": ["Status must be one of: draft, published"]
    }
  }
}
\```

**Response (401 Unauthorized):**
\```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required",
    "status": 401
  }
}
\```

#### PUT /api/v1/posts/{id}
Update a post (full replacement)

#### PATCH /api/v1/posts/{id}
Partially update a post

#### DELETE /api/v1/posts/{id}
Delete a post

**Response (204 No Content)**

**Response (403 Forbidden):**
\```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "You don't have permission to delete this post",
    "status": 403
  }
}
\```

## Design Principles

### 1. Resource-Based URLs
✅ Good: `/api/v1/posts`
❌ Bad: `/api/v1/getPosts`

### 2. HTTP Methods
- GET: Retrieve resource(s)
- POST: Create new resource
- PUT: Replace entire resource
- PATCH: Partial update
- DELETE: Remove resource

### 3. Status Codes
- 200: OK (GET, PUT, PATCH success)
- 201: Created (POST success)
- 204: No Content (DELETE success)
- 400: Bad Request (validation errors)
- 401: Unauthorized (auth required)
- 403: Forbidden (insufficient permissions)
- 404: Not Found
- 500: Internal Server Error

### 4. Pagination
Always paginate list endpoints:
\```json
{
  "data": [...],
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 150
  }
}
\```

### 5. Filtering & Sorting
\```
GET /api/v1/posts?status=published&sort=-created_at
\```

### 6. Versioning
Include version in URL: `/api/v1/...`

### 7. Error Format
Consistent error structure:
\```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "status": 400,
    "details": {}  // Optional validation details
  }
}
\```

## Security Recommendations

1. **Authentication**: Use JWT or OAuth 2.0
2. **Rate Limiting**: Implement per-user/IP limits
3. **Input Validation**: Validate all inputs
4. **HTTPS Only**: Enforce SSL/TLS
5. **CORS**: Configure properly
6. **API Keys**: For third-party integrations
```

## Features

### Comprehensive API Coverage
- CRUD operations
- Filtering and pagination
- Sorting and search
- Relationships and nesting
- Batch operations
- File uploads

### Documentation Generation
- OpenAPI 3.0 specs
- Swagger UI compatible
- Example requests/responses
- Schema definitions
- Authentication docs

### Best Practices
- RESTful conventions
- Proper HTTP methods
- Appropriate status codes
- Consistent error handling
- Security considerations
- Performance tips

## Customization

Add your team's standards to the subagent:

```markdown
## Our API Standards

### URL Structure
All URLs must follow: `/api/v{version}/{resource}/{id}/{sub-resource}`

### Response Envelope
All responses wrapped in:
\```json
{
  "success": true,
  "data": {...},
  "meta": {...},
  "errors": null
}
\```

### Authentication
Use API key in header:
\```
X-API-Key: your-api-key
\```
```

## Real-World Use Cases

### 1. Microservices Design
```
"Design an API for a payment microservice"
```
Subagent provides complete API design with transactions, refunds, webhooks.

### 2. Mobile App Backend
```
"Design a RESTful API for a mobile todo app"
```
Includes offline sync considerations, optimistic updates.

### 3. Third-Party Integration
```
"Design a webhook API for order notifications"
```
Webhook registration, payload format, retry logic.

## Troubleshooting

**Problem:** Subagent provides generic design

**Solution:** Be specific:
```
"Design an API for a blog platform with:
- Multi-author support
- Categories and tags
- Draft/published states
- Comments system
- User authentication"
```

## Best Practices

### ✅ Do:
- Provide detailed requirements
- Specify authentication needs
- Mention performance requirements
- Ask about versioning strategy
- Request documentation format

### ❌ Don't:
- Ask for implementation code
- Mix API design with database design
- Skip security discussion
- Forget about error cases

## Next Steps

1. Copy subagent to your project
2. Call it for your next API design
3. Review and customize the design
4. Implement following the spec
5. Generate OpenAPI documentation

---

**Pro Tip:** Combine with a security-auditor subagent to review the API design for security vulnerabilities!
