---
name: database-query-optimizer
description: Analyzes and optimizes database queries for PostgreSQL, MySQL, MongoDB with EXPLAIN plans, index suggestions, and N+1 query detection. Use when user asks to "optimize query", "analyze EXPLAIN plan", "fix slow queries", or "suggest database indexes".
allowed-tools: [Read, Write, Bash]
---

# Database Query Optimizer

Analyzes database queries, interprets EXPLAIN plans, suggests indexes, and detects common performance issues like N+1 queries.

## When to Use

- "Optimize my database query"
- "Analyze EXPLAIN plan"
- "Why is my query slow?"
- "Suggest indexes"
- "Fix N+1 queries"
- "Improve database performance"

## Instructions

### 1. PostgreSQL Query Analysis

**Run EXPLAIN:**
```sql
EXPLAIN ANALYZE
SELECT u.name, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.name
ORDER BY post_count DESC
LIMIT 10;
```

**Interpret EXPLAIN output:**
```
QUERY PLAN
-----------------------------------------------------------
Limit  (cost=1234.56..1234.58 rows=10 width=40) (actual time=45.123..45.125 rows=10 loops=1)
  ->  Sort  (cost=1234.56..1345.67 rows=44444 width=40) (actual time=45.122..45.123 rows=10 loops=1)
        Sort Key: (count(p.id)) DESC
        Sort Method: top-N heapsort  Memory: 25kB
        ->  HashAggregate  (cost=1000.00..1200.00 rows=44444 width=40) (actual time=40.456..42.789 rows=45000 loops=1)
              Group Key: u.id
              ->  Hash Left Join  (cost=100.00..900.00 rows=50000 width=32) (actual time=1.234..35.678 rows=100000 loops=1)
                    Hash Cond: (p.user_id = u.id)
                    ->  Seq Scan on posts p  (cost=0.00..500.00 rows=50000 width=4) (actual time=0.010..10.234 rows=50000 loops=1)
                    ->  Hash  (cost=75.00..75.00 rows=2000 width=32) (actual time=1.200..1.200 rows=2000 loops=1)
                          Buckets: 2048  Batches: 1  Memory Usage: 125kB
                          ->  Seq Scan on users u  (cost=0.00..75.00 rows=2000 width=32) (actual time=0.005..0.678 rows=2000 loops=1)
                                Filter: (created_at > '2024-01-01'::date)
                                Rows Removed by Filter: 500
Planning Time: 0.234 ms
Execution Time: 45.234 ms
```

**Key metrics to analyze:**
- **cost**: Estimated cost (first number = startup, second = total)
- **rows**: Estimated rows returned
- **width**: Average row size in bytes
- **actual time**: Real execution time (ms)
- **loops**: Number of times node executed

**Red flags:**
- Sequential Scan on large tables
- High cost values
- Rows estimate far from actual
- Multiple loops
- Slow execution time

### 2. Optimization Strategies

**Add Index:**
```sql
-- Create index on filtered column
CREATE INDEX idx_users_created_at ON users(created_at);

-- Create index on join column
CREATE INDEX idx_posts_user_id ON posts(user_id);

-- Composite index for specific query pattern
CREATE INDEX idx_users_created_name ON users(created_at, name);

-- Partial index for common filter
CREATE INDEX idx_users_recent ON users(created_at) WHERE created_at > '2024-01-01';

-- Covering index (includes all needed columns)
CREATE INDEX idx_users_covering ON users(id, name, created_at);
```

**Rewrite Query:**
```sql
-- ❌ BAD: Subquery in SELECT
SELECT
    u.name,
    (SELECT COUNT(*) FROM posts WHERE user_id = u.id) as post_count
FROM users u;

-- ✅ GOOD: Use JOIN
SELECT
    u.name,
    COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id, u.name;

-- ❌ BAD: OR conditions
SELECT * FROM users WHERE email = 'test@example.com' OR username = 'test';

-- ✅ GOOD: Use UNION (can use separate indexes)
SELECT * FROM users WHERE email = 'test@example.com'
UNION
SELECT * FROM users WHERE username = 'test';

-- ❌ BAD: Function on indexed column
SELECT * FROM users WHERE LOWER(email) = 'test@example.com';

-- ✅ GOOD: Functional index or avoid function
CREATE INDEX idx_users_email_lower ON users(LOWER(email));
-- Or just:
SELECT * FROM users WHERE email = 'test@example.com';
```

### 3. N+1 Query Detection

**Problem:**
```python
# Python/SQLAlchemy example
# ❌ N+1 Query Problem
users = User.query.all()  # 1 query
for user in users:
    posts = user.posts  # N queries (one per user)
    print(f"{user.name}: {len(posts)} posts")
# Total: 1 + N queries
```

**Solution:**
```python
# ✅ Eager Loading
users = User.query.options(joinedload(User.posts)).all()  # 1 query
for user in users:
    posts = user.posts  # No additional query
    print(f"{user.name}: {len(posts)} posts")
# Total: 1 query
```

**Node.js/Sequelize:**
```javascript
// ❌ N+1 Problem
const users = await User.findAll();
for (const user of users) {
  const posts = await user.getPosts();  // N queries
}

// ✅ Solution: Include associations
const users = await User.findAll({
  include: [{ model: Post }]  // 1 query with JOIN
});
```

**Rails/ActiveRecord:**
```ruby
# ❌ N+1 Problem
users = User.all
users.each do |user|
  puts user.posts.count  # N queries
end

# ✅ Solution: includes
users = User.includes(:posts)
users.each do |user|
  puts user.posts.count  # No additional queries
end
```

### 4. Index Suggestions

**Automated analysis:**
```sql
-- PostgreSQL: Find missing indexes
SELECT schemaname, tablename, attname, n_distinct, correlation
FROM pg_stats
WHERE schemaname = 'public'
  AND n_distinct > 100
  AND correlation < 0.5
ORDER BY n_distinct DESC;

-- Find tables with sequential scans
SELECT schemaname, tablename, seq_scan, seq_tup_read,
       idx_scan, idx_tup_fetch
FROM pg_stat_user_tables
WHERE seq_scan > 0
  AND seq_tup_read / seq_scan > 10000
ORDER BY seq_tup_read DESC;

-- Unused indexes
SELECT schemaname, tablename, indexname, idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
  AND indexrelname NOT LIKE 'pg_toast%'
ORDER BY pg_relation_size(indexrelid) DESC;
```

**MySQL:**
```sql
-- Missing indexes
SELECT * FROM sys.schema_unused_indexes;

-- Duplicate indexes
SELECT * FROM sys.schema_redundant_indexes;

-- Table scan queries
SELECT * FROM sys.statements_with_full_table_scans
LIMIT 10;
```

### 5. Query Optimization Checklist

**Python Script:**
```python
#!/usr/bin/env python3
import psycopg2
import re

class QueryOptimizer:
    def __init__(self, conn):
        self.conn = conn

    def analyze_query(self, query):
        """Analyze query and provide optimization suggestions."""
        suggestions = []

        # Check for SELECT *
        if re.search(r'SELECT\s+\*', query, re.IGNORECASE):
            suggestions.append("❌ Avoid SELECT *. Specify only needed columns.")

        # Check for missing WHERE clause
        if re.search(r'FROM\s+\w+', query, re.IGNORECASE) and \
           not re.search(r'WHERE', query, re.IGNORECASE):
            suggestions.append("⚠️  No WHERE clause. Consider adding filters.")

        # Check for OR in WHERE
        if re.search(r'WHERE.*\sOR\s', query, re.IGNORECASE):
            suggestions.append("⚠️  OR conditions may prevent index usage. Consider UNION.")

        # Check for functions on indexed columns
        if re.search(r'WHERE\s+\w+\([^\)]+\)\s*=', query, re.IGNORECASE):
            suggestions.append("❌ Functions on columns prevent index usage.")

        # Check for LIKE with leading wildcard
        if re.search(r'LIKE\s+[\'"]%', query, re.IGNORECASE):
            suggestions.append("❌ LIKE with leading % cannot use index.")

        # Run EXPLAIN
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"EXPLAIN ANALYZE {query}")
            plan = cursor.fetchall()

            # Check for sequential scans
            plan_str = str(plan)
            if 'Seq Scan' in plan_str:
                suggestions.append("❌ Sequential scan detected. Consider adding index.")

            # Check for high cost
            cost_match = re.search(r'cost=(\d+\.\d+)', plan_str)
            if cost_match:
                cost = float(cost_match.group(1))
                if cost > 10000:
                    suggestions.append(f"⚠️  High query cost: {cost:.2f}")

            return {
                'suggestions': suggestions,
                'explain_plan': plan
            }
        finally:
            cursor.close()

    def suggest_indexes(self, query):
        """Suggest indexes based on query pattern."""
        indexes = []

        # Find WHERE conditions
        where_matches = re.findall(r'WHERE\s+(\w+)\s*[=<>]', query, re.IGNORECASE)
        for col in where_matches:
            indexes.append(f"CREATE INDEX idx_{col} ON table_name({col});")

        # Find JOIN conditions
        join_matches = re.findall(r'ON\s+\w+\.(\w+)\s*=\s*\w+\.(\w+)', query, re.IGNORECASE)
        for col1, col2 in join_matches:
            indexes.append(f"CREATE INDEX idx_{col1} ON table_name({col1});")
            indexes.append(f"CREATE INDEX idx_{col2} ON table_name({col2});")

        # Find ORDER BY
        order_matches = re.findall(r'ORDER BY\s+(\w+)', query, re.IGNORECASE)
        for col in order_matches:
            indexes.append(f"CREATE INDEX idx_{col} ON table_name({col});")

        return list(set(indexes))

# Usage
conn = psycopg2.connect("dbname=mydb user=postgres")
optimizer = QueryOptimizer(conn)

query = """
SELECT u.name, u.email, COUNT(p.id)
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id
ORDER BY COUNT(p.id) DESC
LIMIT 10
"""

result = optimizer.analyze_query(query)
for suggestion in result['suggestions']:
    print(suggestion)

print("\nSuggested indexes:")
for index in optimizer.suggest_indexes(query):
    print(index)
```

### 6. MongoDB Optimization

**Analyze Query:**
```javascript
db.users.find({
  created_at: { $gt: ISODate("2024-01-01") },
  status: "active"
}).sort({ created_at: -1 }).explain("executionStats")
```

**Check for issues:**
```javascript
// Check execution stats
const stats = db.users.find({ status: "active" }).explain("executionStats");

// Red flags:
// - totalDocsExamined >> nReturned (scanning many docs)
// - COLLSCAN stage (no index used)
// - High executionTimeMillis

// Create index
db.users.createIndex({ status: 1, created_at: -1 });

// Compound index for specific query
db.users.createIndex({ status: 1, created_at: -1, name: 1 });
```

### 7. ORM Query Optimization

**Django:**
```python
# ❌ N+1 Problem
users = User.objects.all()
for user in users:
    print(user.profile.bio)  # N queries

# ✅ select_related (for ForeignKey/OneToOne)
users = User.objects.select_related('profile').all()

# ✅ prefetch_related (for ManyToMany/reverse ForeignKey)
users = User.objects.prefetch_related('posts').all()

# ❌ Loading all records
users = User.objects.all()  # Loads everything into memory

# ✅ Use iterator for large datasets
for user in User.objects.iterator(chunk_size=1000):
    process(user)

# ❌ Multiple queries
active_users = User.objects.filter(is_active=True).count()
inactive_users = User.objects.filter(is_active=False).count()

# ✅ Single aggregation
from django.db.models import Count, Q
stats = User.objects.aggregate(
    active=Count('id', filter=Q(is_active=True)),
    inactive=Count('id', filter=Q(is_active=False))
)
```

**TypeORM:**
```typescript
// ❌ N+1 Problem
const users = await userRepository.find();
for (const user of users) {
  const posts = await postRepository.find({ where: { userId: user.id } });
}

// ✅ Use relations
const users = await userRepository.find({
  relations: ['posts', 'profile']
});

// ✅ Query Builder for complex queries
const users = await userRepository
  .createQueryBuilder('user')
  .leftJoinAndSelect('user.posts', 'post')
  .where('user.created_at > :date', { date: '2024-01-01' })
  .andWhere('post.status = :status', { status: 'published' })
  .getMany();

// Use select to limit columns
const users = await userRepository
  .createQueryBuilder('user')
  .select(['user.id', 'user.name', 'user.email'])
  .getMany();
```

### 8. Performance Monitoring

**PostgreSQL:**
```sql
-- Top slow queries
SELECT
  query,
  calls,
  total_time,
  mean_time,
  max_time
FROM pg_stat_statements
ORDER BY mean_time DESC
LIMIT 10;

-- Table bloat
SELECT
  schemaname,
  tablename,
  pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size,
  pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename) - pg_relation_size(schemaname||'.'||tablename)) AS external_size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC
LIMIT 10;
```

**MySQL:**
```sql
-- Slow queries
SELECT * FROM mysql.slow_log
ORDER BY query_time DESC
LIMIT 10;

-- Table statistics
SELECT
  TABLE_NAME,
  TABLE_ROWS,
  DATA_LENGTH,
  INDEX_LENGTH,
  DATA_FREE
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'your_database'
ORDER BY DATA_LENGTH DESC;
```

### Best Practices

**DO:**
- Add indexes on foreign keys
- Use EXPLAIN regularly
- Monitor slow query log
- Use connection pooling
- Implement pagination
- Cache frequent queries
- Use appropriate data types
- Regular VACUUM/ANALYZE

**DON'T:**
- Use SELECT *
- Over-index (slows writes)
- Use LIKE with leading %
- Use functions on indexed columns
- Ignore N+1 queries
- Load entire tables
- Skip query analysis
- Use OR excessively

## Checklist

- [ ] Slow queries identified
- [ ] EXPLAIN plans analyzed
- [ ] Indexes added where needed
- [ ] N+1 queries fixed
- [ ] Query rewrites implemented
- [ ] Monitoring setup
- [ ] Connection pool configured
- [ ] Caching implemented
