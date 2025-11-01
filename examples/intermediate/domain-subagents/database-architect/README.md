# Database Architect Subagent - Intermediate Example

A specialized subagent for designing database schemas with proper normalization, indexes, and relationships.

## What This Teaches

- Database schema design
- Normalization principles
- Index optimization
- Relationship modeling
- Performance considerations

## Installation

```bash
cp subagent.md /path/to/your-project/.claude/agents/database-architect.md
```

## When to Use

- Design new database schema
- Review existing schema
- Optimize database performance
- Plan migrations
- Normalize denormalized data

## Example Output

**You:** "Design a database schema for an e-commerce platform"

**Subagent Response:**

```markdown
# E-Commerce Database Schema

## Tables

### users
\```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
\```

### products
\```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    stock INTEGER DEFAULT 0 CHECK (stock >= 0),
    category_id INTEGER REFERENCES categories(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_name ON products(name);
\```

### orders
\```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    status VARCHAR(20) DEFAULT 'pending',
    total DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_created ON orders(created_at DESC);
\```

### order_items
\```sql
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    price DECIMAL(10, 2) NOT NULL,
    UNIQUE(order_id, product_id)
);

CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_product ON order_items(product_id);
\```

## Normalization

Schema follows 3NF (Third Normal Form):
- ✅ No repeating groups
- ✅ All non-key attributes depend on primary key
- ✅ No transitive dependencies

## Indexes

Strategic indexes for common queries:
- User lookups by email
- Products by category
- Orders by user and status
- Order items by order

## Relationships

- users 1:N orders
- products N:1 categories
- orders 1:N order_items
- products 1:N order_items

## Performance Considerations

1. **Indexes on foreign keys** for join performance
2. **Composite indexes** for common query patterns
3. **Constraints** for data integrity
4. **Timestamps** for audit trails
5. **Decimal** for monetary values (not FLOAT)
```

## Features

- Table design with proper types
- Foreign key relationships
- Indexes for performance
- Constraints for integrity
- Normalization analysis
- Query optimization tips
- Migration strategies

## Customization

Add your database preferences:

```markdown
## Our Database Standards

### Naming Conventions
- Tables: plural, snake_case (users, order_items)
- Columns: snake_case
- Indexes: idx_{table}_{column}
- Foreign keys: fk_{table}_{column}

### Required Fields
All tables must have:
- id (BIGSERIAL PRIMARY KEY)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
- is_deleted (BOOLEAN) for soft deletes
```

## Next Steps

1. Install the subagent
2. Request schema designs
3. Review for your use case
4. Implement with migrations
5. Monitor performance

---

**Pro Tip:** Use with Django/Rails ORM models to ensure database design matches your application models!
