# Express.js API Generator

Generates production-ready Express.js REST APIs with proper layering, validation, and error handling.

## What It Does

This skill creates Express.js APIs with:
- Proper MVC/layered architecture
- TypeScript support
- Request validation with Joi/Zod
- Error handling middleware
- Authentication and authorization
- API documentation

## Installation

```bash
cp examples/intermediate/framework-skills/express-api-generator/SKILL.md \
   .claude/skills/express-api-generator.md
```

## Usage

Ask Claude to create Express APIs naturally:

```
"create Express API for user management"
"generate REST endpoints for products with CRUD"
"build authentication API with Express and JWT"
```

## Example Output

When you ask: *"create Express API for managing blog posts"*

Claude will generate a complete API structure:

**routes/posts.ts:**
```typescript
import { Router } from 'express'
import { PostController } from '../controllers/PostController'
import { validatePost } from '../middleware/validation'
import { authenticate } from '../middleware/auth'

const router = Router()
const controller = new PostController()

router.get('/', controller.list)
router.get('/:id', controller.getById)
router.post('/', authenticate, validatePost, controller.create)
router.put('/:id', authenticate, validatePost, controller.update)
router.delete('/:id', authenticate, controller.delete)

export default router
```

**controllers/PostController.ts:**
```typescript
import { Request, Response, NextFunction } from 'express'
import { PostService } from '../services/PostService'
import { ApiError } from '../utils/ApiError'

export class PostController {
  private service: PostService

  constructor() {
    this.service = new PostService()
  }

  list = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const { page = 1, limit = 10, search } = req.query
      const posts = await this.service.findAll({
        page: Number(page),
        limit: Number(limit),
        search: search as string
      })
      res.json(posts)
    } catch (error) {
      next(error)
    }
  }

  getById = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const post = await this.service.findById(req.params.id)
      if (!post) {
        throw new ApiError(404, 'Post not found')
      }
      res.json(post)
    } catch (error) {
      next(error)
    }
  }

  create = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const post = await this.service.create({
        ...req.body,
        authorId: req.user.id
      })
      res.status(201).json(post)
    } catch (error) {
      next(error)
    }
  }

  update = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const post = await this.service.update(req.params.id, req.body)
      res.json(post)
    } catch (error) {
      next(error)
    }
  }

  delete = async (req: Request, res: Response, next: NextFunction) => {
    try {
      await this.service.delete(req.params.id)
      res.status(204).send()
    } catch (error) {
      next(error)
    }
  }
}
```

**middleware/validation.ts:**
```typescript
import { Request, Response, NextFunction } from 'express'
import Joi from 'joi'

const postSchema = Joi.object({
  title: Joi.string().required().min(3).max(200),
  content: Joi.string().required(),
  tags: Joi.array().items(Joi.string()),
  published: Joi.boolean().default(false)
})

export const validatePost = (req: Request, res: Response, next: NextFunction) => {
  const { error } = postSchema.validate(req.body, { abortEarly: false })
  if (error) {
    return res.status(400).json({
      message: 'Validation failed',
      errors: error.details.map(d => ({
        field: d.path.join('.'),
        message: d.message
      }))
    })
  }
  next()
}
```

## Features

- ✅ Layered architecture (Routes → Controllers → Services)
- ✅ TypeScript with full typing
- ✅ Request validation
- ✅ Error handling middleware
- ✅ Authentication middleware
- ✅ Pagination and filtering
- ✅ Proper HTTP status codes
- ✅ RESTful conventions

## Use Cases

- Building REST APIs
- Creating microservices
- Implementing authentication systems
- Building CRUD applications
- API-first development

## Best Practices Included

- Separation of concerns (MVC pattern)
- Async/await error handling
- Input validation
- Security middleware
- Consistent error responses
- RESTful route naming
- Status code conventions

## See Also

- [FastAPI Generator](../fastapi-generator/) - Python equivalent
- [API Documentation Generator](../api-documentation-generator/) - Generate OpenAPI docs
- [GraphQL Schema Generator](../graphql-schema-generator/) - GraphQL alternative
