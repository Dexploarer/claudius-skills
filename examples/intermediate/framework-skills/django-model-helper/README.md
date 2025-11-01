# Django Model Helper - Intermediate Skill

A framework-specific skill that generates Django ORM models with relationships, indexes, and admin configuration.

## What This Teaches

- Django ORM best practices
- Model relationships (ForeignKey, ManyToMany)
- Database indexing strategies
- Admin interface customization
- Model validation and constraints
- Migration awareness

## Installation

```bash
# Copy to your Django project
cp SKILL.md /path/to/your-project/.claude/skills/django-model-helper.md
```

## When It Activates

- "Create a User model for Django"
- "Generate a Blog Post model with categories"
- "Build an Order model with line items"
- "Create a Product model with inventory tracking"

## What It Generates

For a model request, creates:

```
app/models.py        # Model definition
app/admin.py         # Admin configuration
app/tests.py         # Model tests
app/migrations/      # Migration files (suggested)
```

## Example Usage

### Basic Model

**You:**
```
"Create a Product model with name, description, price, and stock"
```

**Generated:**

```python
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Product(models.Model):
    """Product model for e-commerce catalog."""

    name = models.CharField(
        max_length=200,
        db_index=True,
        help_text="Product name"
    )
    description = models.TextField(
        blank=True,
        help_text="Detailed product description"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Product price"
    )
    stock = models.PositiveIntegerField(
        default=0,
        help_text="Available stock quantity"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name', '-created_at']),
        ]
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def is_in_stock(self):
        """Check if product is available."""
        return self.stock > 0
```

**Admin configuration:**

```python
from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'stock')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
```

**Tests:**

```python
from django.test import TestCase
from decimal import Decimal
from .models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test description",
            price=Decimal('99.99'),
            stock=10
        )

    def test_product_creation(self):
        """Test product is created correctly."""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, Decimal('99.99'))
        self.assertEqual(self.product.stock, 10)

    def test_is_in_stock(self):
        """Test stock availability check."""
        self.assertTrue(self.product.is_in_stock())

        self.product.stock = 0
        self.assertFalse(self.product.is_in_stock())

    def test_string_representation(self):
        """Test string representation."""
        self.assertEqual(str(self.product), "Test Product")
```

### Model with Relationships

**You:**
```
"Create a BlogPost model with author, categories, and tags"
```

**Generated:**

```python
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


User = get_user_model()


class Category(models.Model):
    """Blog post category."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Blog post tag."""
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """Blog post with author, categories, and tags."""

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True, max_length=500)

    # Relationships
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='posts'
    )

    # Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    # Timestamps
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['status', '-published_at']),
            models.Index(fields=['author', '-created_at']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def is_published(self):
        """Check if post is published."""
        return self.status == 'published'
```

## Features

### Field Types Supported
- CharField, TextField
- IntegerField, PositiveIntegerField
- DecimalField, FloatField
- BooleanField
- DateField, DateTimeField
- ForeignKey, ManyToManyField, OneToOneField
- JSONField (PostgreSQL)
- FileField, ImageField
- URLField, EmailField
- And more...

### Best Practices Applied
- ✅ Appropriate field types
- ✅ Database indexes on commonly queried fields
- ✅ Validators for data integrity
- ✅ Help text for documentation
- ✅ `__str__` methods for readability
- ✅ Meta options for ordering
- ✅ Related names for reverse relations
- ✅ Proper on_delete behaviors

### Admin Integration
- List display with relevant fields
- List filters for categorical data
- Search fields for text content
- Readonly fields (timestamps, etc.)
- Fieldsets for organization
- Inlines for related objects

### Testing
- Model creation tests
- Relationship tests
- Validation tests
- Method tests
- String representation tests

## Advanced Patterns

### Abstract Base Models

```python
class TimeStampedModel(models.Model):
    """Abstract base class with created/updated timestamps."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimeStampedModel):
    """Product inherits timestamps from base."""
    name = models.CharField(max_length=200)
    # ... other fields
```

### Custom Managers

```python
class PublishedManager(models.Manager):
    """Manager for published posts only."""
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class BlogPost(models.Model):
    # ... fields ...

    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager

# Usage:
# BlogPost.published.all()  # Only published posts
```

### Signals Integration

```python
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=BlogPost)
def notify_on_publish(sender, instance, created, **kwargs):
    """Send notification when post is published."""
    if instance.status == 'published' and instance.published_at:
        # Send notification
        pass
```

## Customization

### Add Team Conventions

```markdown
## Our Model Standards

All models must include:
1. UUID primary key
2. Soft delete (is_deleted field)
3. Audit fields (created_by, updated_by)

\`\`\`python
import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, ...)
    updated_by = models.ForeignKey(User, ...)

    class Meta:
        abstract = True
\`\`\`
```

## Troubleshooting

**Problem:** Migrations not generating

**Solution:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Problem:** Circular import errors

**Solution:** Use string references:
```python
author = models.ForeignKey(
    'auth.User',  # String reference
    on_delete=models.CASCADE
)
```

## Real-World Examples

### E-Commerce System

```
"Create models for an e-commerce system with Products, Orders, and Customers"
```

Generates complete model structure with:
- Product catalog with categories
- Customer profiles
- Orders with line items
- Payment tracking
- Inventory management

### CMS System

```
"Create models for a content management system"
```

Generates:
- Pages with hierarchical structure
- Media library
- User roles and permissions
- Content versioning
- Publishing workflow

## Next Steps

1. Install in your Django project
2. Generate models for your domain
3. Review and customize
4. Create migrations
5. Test thoroughly

---

**Pro Tip:** Combine with a database-architect subagent to review your model design for normalization and performance!
