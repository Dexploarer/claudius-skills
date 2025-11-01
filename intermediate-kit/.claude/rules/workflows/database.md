# Database Workflow - Intermediate Kit

> **Database design, migrations, and optimization**

---

## 🎯 Database Development Process

### Phase 1: Design

```
"Use database-architect to design the e-commerce schema"
```

**Outputs:**
- Normalized schema
- Relationships (ForeignKey, ManyToMany)
- Indexes
- Constraints

### Phase 2: Implementation

**Create Models:**
```
"Create Django models for products and orders"
"Create Prisma schema for users and posts"
```

**Create Migrations:**
```bash
/migration-create add_products_table
/migration-create add_orders_table
```

### Phase 3: Optimization

```
"Use database-architect to optimize query performance"
```

**Add Indexes:**
- Frequently queried columns
- Foreign keys
- Composite indexes for multi-column queries

---

## 📊 Migration Best Practices

### Before Running Migrations

1. **Backup database:**
   ```bash
   /db-backup production_db
   ```

2. **Test on development/staging first**

3. **Review migration SQL**

4. **Plan rollback strategy**

### Running Migrations

```bash
# Development
python manage.py migrate

# Production (with confirmation)
python manage.py migrate --database=production
```

---

## 🔧 Database Commands

```bash
/migration-create        # Create migration
/db-backup               # Backup database
```

## 🔧 Database Agents

```
"Use database-architect for schema design"
```

---

**Last Updated:** 2025-11-01
