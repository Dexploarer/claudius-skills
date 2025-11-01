# Database Migration Helper

Creates database migrations with proper up/down scripts, indexes, and data transformations.

## Installation

```bash
cp examples/intermediate/framework-skills/database-migration-helper/SKILL.md \
   .claude/skills/database-migration-helper.md
```

## Usage

```
"create migration to add user roles table"
"generate schema changes for adding email verification"
"build migration to add indexes on user table"
```

## Features

- ✅ Up/down migration scripts
- ✅ Support for multiple ORMs (Knex, Sequelize, TypeORM, Alembic)
- ✅ Index creation/removal
- ✅ Data transformations
- ✅ Foreign key constraints
- ✅ Rollback support
- ✅ Idempotent migrations

## See Also

- [Django Model Helper](../django-model-helper/)
- [Database Architect Subagent](../../domain-subagents/database-architect/)
