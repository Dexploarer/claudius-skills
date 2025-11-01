# FastAPI Generator

Creates FastAPI endpoints with Pydantic models, async/await, and automatic OpenAPI documentation.

## What It Does

This skill generates production-ready FastAPI applications with:
- Pydantic models for validation
- Async/await support
- Automatic OpenAPI/Swagger docs
- Dependency injection
- Authentication and authorization
- Database integration patterns

## Installation

```bash
cp examples/intermediate/framework-skills/fastapi-generator/SKILL.md \
   .claude/skills/fastapi-generator.md
```

## Usage

```
"create FastAPI endpoint for user management"
"generate REST API with FastAPI for products"
"build authentication system with FastAPI and JWT"
```

## Example Output

When you ask: *"create FastAPI endpoints for managing tasks"*

**models.py:**
```python
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    priority: int = Field(default=1, ge=1, le=5)

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[int] = Field(None, ge=1, le=5)

class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user_id: int

    class Config:
        orm_mode = True
```

**routes/tasks.py:**
```python
from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Task, TaskCreate, TaskUpdate
from ..services.task_service import TaskService
from ..auth import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[Task])
async def list_tasks(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    status: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    List all tasks for the current user.

    - **skip**: Number of tasks to skip (pagination)
    - **limit**: Maximum number of tasks to return
    - **status**: Filter by task status
    """
    service = TaskService(db)
    return await service.get_tasks(
        user_id=current_user.id,
        skip=skip,
        limit=limit,
        status=status
    )

@router.get("/{task_id}", response_model=Task)
async def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get a specific task by ID."""
    service = TaskService(db)
    task = await service.get_task(task_id, current_user.id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Create a new task."""
    service = TaskService(db)
    return await service.create_task(task, current_user.id)

@router.put("/{task_id}", response_model=Task)
async def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Update an existing task."""
    service = TaskService(db)
    updated_task = await service.update_task(task_id, task, current_user.id)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return updated_task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Delete a task."""
    service = TaskService(db)
    success = await service.delete_task(task_id, current_user.id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
```

## Features

- ✅ Pydantic models with validation
- ✅ Async/await for performance
- ✅ Automatic OpenAPI documentation
- ✅ Type hints everywhere
- ✅ Dependency injection
- ✅ HTTPException handling
- ✅ Response models
- ✅ Query parameter validation

## Use Cases

- Building modern Python APIs
- Microservices development
- Machine learning model serving
- Data processing APIs
- High-performance backends

## Best Practices Included

- Pydantic models for validation
- Separation of concerns (routes/services/models)
- Proper HTTP status codes
- Comprehensive docstrings
- Type safety
- Dependency injection
- Error handling

## See Also

- [Express API Generator](../express-api-generator/) - Node.js equivalent
- [Django Model Helper](../django-model-helper/) - Django ORM models
- [API Documentation Generator](../api-documentation-generator/) - Enhanced docs
