# SQLite Server - MCP Example

Connect Claude Code to SQLite databases for querying and analyzing data.

## What It Does

The SQLite server lets Claude:
- **Query databases** using SQL
- **Explore schemas** and tables
- **Analyze data** and generate reports
- **Create visualizations** from query results
- **Debug database issues**
- **Generate SQL queries** from natural language

## Why SQLite?

Perfect for learning because:
- ✅ **No server setup** - File-based database
- ✅ **No authentication** - Simple to start
- ✅ **Widely used** - Many apps use SQLite
- ✅ **Great for testing** - Easy to create test databases
- ✅ **Learn SQL** - Standard SQL syntax

## Prerequisites

### Install SQLite (if not already installed)

**macOS:**
```bash
# Already installed!
sqlite3 --version
```

**Linux:**
```bash
sudo apt-get install sqlite3
# or
sudo yum install sqlite
```

**Windows:**
Download from [sqlite.org](https://www.sqlite.org/download.html)

## Installation

### Step 1: Create a Test Database

Let's create a simple database to experiment with:

```bash
# Create a database file
sqlite3 ~/test.db << 'EOF'
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE,
  age INTEGER,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email, age) VALUES
  ('Alice Johnson', 'alice@example.com', 30),
  ('Bob Smith', 'bob@example.com', 25),
  ('Charlie Brown', 'charlie@example.com', 35),
  ('Diana Prince', 'diana@example.com', 28);

CREATE TABLE posts (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  title TEXT NOT NULL,
  content TEXT,
  published_at TEXT,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO posts (user_id, title, content) VALUES
  (1, 'First Post', 'Hello World!'),
  (1, 'Second Post', 'Learning SQLite'),
  (2, 'Bob''s Post', 'My first blog post'),
  (3, 'Data Analysis', 'Working with data');
EOF
```

### Step 2: Create `.mcp.json`

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "/path/to/your/database.db"
      ]
    }
  }
}
```

**Important:** Replace `/path/to/your/database.db` with actual path.

**Example:**
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "/Users/yourname/test.db"
      ]
    }
  }
}
```

### Step 3: Restart Claude Code

```bash
exit
claude
```

### Step 4: Test It!

```bash
"Show me the tables in the database"
"Query all users from the database"
"How many users are there?"
```

## How to Use

### Exploring the Database

```bash
"Show me all tables in the database"
"What's the schema of the users table?"
"Describe the structure of the database"
"List all tables and their columns"
```

### Basic Queries

```bash
"Show me all users"
"Get users older than 30"
"Find user with email alice@example.com"
"Count the total number of posts"
```

### Join Queries

```bash
"Show me all posts with their author names"
"List users and how many posts each has written"
"Find users who haven't written any posts"
```

### Aggregations

```bash
"What's the average age of users?"
"How many posts does each user have?"
"Show me the oldest and youngest users"
"Count users by age range"
```

### Natural Language to SQL

```bash
You: "Show me all users sorted by age"
Claude: "I'll query that: SELECT * FROM users ORDER BY age"
[Results...]
```

## Example Use Cases

### Use Case 1: Data Analysis

**Scenario:** Analyze user activity in your app.

```bash
You: "Show me the database schema"
Claude: "Tables: users, posts, comments, likes"

You: "Which users are most active?"
Claude: "Here's a query:
SELECT u.name, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id
ORDER BY post_count DESC"

You: "Run that and show me the top 5"
Claude: [Results showing top 5 active users]
```

### Use Case 2: Debugging Database Issues

**Scenario:** Find data inconsistencies.

```bash
You: "Are there any posts with invalid user_id?"
Claude: "Let me check:
SELECT p.*
FROM posts p
LEFT JOIN users u ON p.user_id = u.id
WHERE u.id IS NULL"

You: "Found 3 orphaned posts"
Claude: "Here they are: [details]"

You: "Generate SQL to fix these"
Claude: "Here's a DELETE query to remove them..."
```

### Use Case 3: Report Generation

**Scenario:** Generate weekly analytics report.

```bash
You: "Create a weekly report of user activity"
Claude: "I'll gather:
1. New users this week: [query]
2. Total posts: [query]
3. Most active users: [query]
4. Popular topics: [query]"

You: "Save this report to a file"  # Using filesystem server
Claude: "Report saved to ~/reports/weekly-2024-11-01.md"
```

### Use Case 4: Learning SQL

**Scenario:** Practice SQL with real queries.

```bash
You: "Teach me how to use JOIN"
Claude: "Let's learn with examples from your database..."

You: "Show me an INNER JOIN example"
Claude: "Here's an INNER JOIN:
SELECT users.name, posts.title
FROM users
INNER JOIN posts ON users.id = posts.user_id"

You: "Now try a LEFT JOIN"
Claude: "Here's a LEFT JOIN: ..."
```

## Common SQL Patterns

### Pattern 1: Find Top N

```sql
-- Top 5 users by post count
SELECT u.name, COUNT(p.id) as posts
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id
ORDER BY posts DESC
LIMIT 5
```

```bash
"Show me the top 5 users by post count"
```

### Pattern 2: Date Filtering

```sql
-- Posts from last 7 days
SELECT *
FROM posts
WHERE date(created_at) >= date('now', '-7 days')
```

```bash
"Show me posts from the last week"
```

### Pattern 3: Aggregation with Groups

```sql
-- Average age by signup year
SELECT strftime('%Y', created_at) as year,
       AVG(age) as avg_age
FROM users
GROUP BY year
```

```bash
"What's the average age of users by signup year?"
```

### Pattern 4: Subqueries

```sql
-- Users with above-average post count
SELECT u.name, COUNT(p.id) as posts
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id
HAVING posts > (
  SELECT AVG(post_count)
  FROM (
    SELECT COUNT(*) as post_count
    FROM posts
    GROUP BY user_id
  )
)
```

```bash
"Show me users with more posts than average"
```

## Best Practices

### Security

✅ **Do:**
- Use read-only database copies for analysis
- Never expose production database directly
- Make backup before experimenting
- Test queries on sample data first
- Use separate databases for development

❌ **Don't:**
- Connect to production database directly
- Run DELETE/UPDATE without WHERE clause
- Share database files with sensitive data
- Grant write access unnecessarily
- Commit database files to git (if they contain data)

### Query Safety

```bash
# ✅ Safe: Read-only queries
SELECT * FROM users

# ⚠️ Careful: Modifying data
UPDATE users SET age = 31 WHERE id = 1

# ❌ Dangerous: Without WHERE clause
DELETE FROM users  -- Deletes everything!
```

### Database Configuration

```json
{
  "mcpServers": {
    "sqlite-readonly": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "/path/to/database.db",
        "--readonly"  // If server supports it
      ]
    }
  }
}
```

## Multiple Databases

You can connect to multiple databases:

```json
{
  "mcpServers": {
    "sqlite-dev": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "/Users/me/dev-database.db"
      ]
    },
    "sqlite-test": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "/Users/me/test-database.db"
      ]
    }
  }
}
```

Use them:
```bash
"Query the dev database for users"
"Compare user count between dev and test databases"
```

## Creating Practice Databases

### E-commerce Database

```bash
sqlite3 ~/ecommerce.db << 'EOF'
CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  price REAL,
  category TEXT,
  stock INTEGER
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  customer_name TEXT,
  product_id INTEGER,
  quantity INTEGER,
  order_date TEXT DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO products VALUES
  (1, 'Laptop', 999.99, 'Electronics', 50),
  (2, 'Mouse', 29.99, 'Electronics', 200),
  (3, 'Desk', 299.99, 'Furniture', 30),
  (4, 'Chair', 199.99, 'Furniture', 45);

INSERT INTO orders (customer_name, product_id, quantity) VALUES
  ('John Doe', 1, 1),
  ('Jane Smith', 2, 2),
  ('John Doe', 4, 1),
  ('Bob Wilson', 3, 1);
EOF
```

### Blog Database

```bash
sqlite3 ~/blog.db << 'EOF'
CREATE TABLE authors (
  id INTEGER PRIMARY KEY,
  name TEXT,
  email TEXT UNIQUE
);

CREATE TABLE posts (
  id INTEGER PRIMARY KEY,
  author_id INTEGER,
  title TEXT,
  content TEXT,
  published_at TEXT,
  views INTEGER DEFAULT 0,
  FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE comments (
  id INTEGER PRIMARY KEY,
  post_id INTEGER,
  author_name TEXT,
  content TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (post_id) REFERENCES posts(id)
);

-- Insert sample data...
EOF
```

## Troubleshooting

### Issue: "Database not found"

**Cause:** Incorrect path in `.mcp.json`

**Solution:**
```bash
# Check database exists
ls -la ~/test.db

# Use absolute path
{
  "args": [
    "-y",
    "@modelcontextprotocol/server-sqlite",
    "/Users/yourname/test.db"  // Full path
  ]
}
```

### Issue: "Database is locked"

**Cause:** Another program is using the database.

**Solution:**
```bash
# Check what's using it
lsof ~/test.db

# Close other SQLite connections
# Or use a copy of the database
cp ~/test.db ~/test-copy.db
```

### Issue: "Permission denied"

**Cause:** No read permission on database file.

**Solution:**
```bash
# Check permissions
ls -la ~/test.db

# Fix permissions
chmod 644 ~/test.db
```

### Issue: "SQL syntax error"

**Cause:** Invalid SQL query.

**Solution:**
```bash
# Test query directly
sqlite3 ~/test.db "SELECT * FROM users"

# Ask Claude to fix
You: "This query failed: [query]. Can you fix it?"
```

## Advanced Usage

### Transactions

```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Indexes for Performance

```sql
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_posts_user_id ON posts(user_id);
```

### Views

```sql
CREATE VIEW user_post_counts AS
SELECT u.name, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id;

-- Query the view
SELECT * FROM user_post_counts;
```

### Full-Text Search

```sql
CREATE VIRTUAL TABLE posts_fts USING fts5(title, content);
INSERT INTO posts_fts SELECT title, content FROM posts;

-- Search
SELECT * FROM posts_fts WHERE posts_fts MATCH 'learning';
```

## Tips

1. **Start with SELECT** - Read before writing
2. **Use LIMIT** - Test queries on small datasets first
3. **EXPLAIN queries** - Understand query performance
4. **Backup before experimenting** - `cp database.db database-backup.db`
5. **Use transactions** - For related changes
6. **Create indexes** - For frequently queried columns

## Learning Resources

### Practice Queries

```bash
# Basic
"SELECT all users"
"COUNT the users"
"Find user with id 1"

# Intermediate
"Show users with posts"
"Average age by category"
"Top 5 most active users"

# Advanced
"Complex JOIN with aggregation"
"Subquery to find outliers"
"Window functions for ranking"
```

### SQL Learning Path

1. **Week 1:** SELECT, WHERE, ORDER BY, LIMIT
2. **Week 2:** JOIN (INNER, LEFT, RIGHT)
3. **Week 3:** GROUP BY, aggregations (COUNT, SUM, AVG)
4. **Week 4:** Subqueries, HAVING
5. **Week 5:** Advanced (CTEs, window functions)

## Real-World Examples

### Analytics Query

```bash
You: "Create a dashboard query showing:
1. Total users
2. Total posts
3. Average posts per user
4. Most active hour of day"

Claude: "Here's the analysis:
- Total users: 150
- Total posts: 1,247
- Average posts per user: 8.3
- Most active: 2-3 PM (203 posts)"
```

### Data Export

```bash
You: "Export all user emails to CSV"
Claude: "Here's the query:
.mode csv
.output users.csv
SELECT email FROM users WHERE email IS NOT NULL;
.quit"
```

### Database Migration

```bash
You: "I need to add a 'status' column to users table"
Claude: "Here's the migration:
ALTER TABLE users ADD COLUMN status TEXT DEFAULT 'active';
UPDATE users SET status = 'inactive' WHERE last_login < date('now', '-90 days');
"
```

## FAQ

**Q: Can I modify the database?**
A: Yes, but be careful! Make backups first.

**Q: Does this work with other SQL databases?**
A: This server is SQLite-specific. For PostgreSQL, MySQL, etc., use their respective MCP servers.

**Q: What's the maximum database size?**
A: SQLite can handle databases up to 140TB, but performance depends on your system.

**Q: Can I use this with production databases?**
A: Not recommended. Use read-only copies or database dumps instead.

**Q: Does it support SQLite extensions?**
A: Check server documentation for extension support.

**Q: Can multiple servers access one database?**
A: SQLite allows multiple readers, but only one writer at a time.

## Security Checklist

- [ ] Using test/development database (not production)
- [ ] Database file not in git (if contains sensitive data)
- [ ] Backup created before experimenting
- [ ] No sensitive data in database
- [ ] Understand queries before running them
- [ ] Not using root/admin credentials

## Next Steps

1. ✅ **Create test database** - Use examples above
2. ✅ **Configure `.mcp.json`** - Point to your database
3. ✅ **Practice queries** - Start with SELECT
4. ✅ **Try analysis** - Generate reports
5. ✅ **Combine servers** - Use with memory, filesystem

## Related Examples

- **memory-server** - Store query results/insights
- **filesystem-server** - Export query results to files
- **github-server** - Track database schema changes

---

**Remember:** Always backup databases before experimenting, and never connect directly to production! 🗄️
