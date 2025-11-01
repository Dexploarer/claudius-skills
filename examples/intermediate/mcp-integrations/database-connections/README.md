# Database Connections MCP Integration

Example MCP configuration for database access.

## What This Provides

Query databases through MCP:
- Execute SELECT queries
- View schema
- Analyze data
- Generate reports

Note: For safety, limit to read-only operations.

## Setup

```json
{
  "mcpServers": {
    "database": {
      "command": "mcp-server-postgres",
      "env": {
        "DATABASE_URL": "${DATABASE_URL}",
        "READ_ONLY": "true"
      }
    }
  }
}
```

## Usage

```
You: "How many users do we have?"

Claude: [Uses MCP to query database]

SELECT COUNT(*) FROM users;

Result: 1,247 users

You: "Show me top 5 products by sales"

Claude: [Uses MCP]

SELECT
  p.name,
  SUM(oi.quantity) as total_sold,
  SUM(oi.subtotal) as revenue
FROM products p
JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id, p.name
ORDER BY revenue DESC
LIMIT 5;

Top Products:
1. Premium Widget - 453 sold - $12,430
2. Starter Kit - 892 sold - $8,920
3. Pro Bundle - 234 sold - $7,020
...
```

## Security

- Use read-only database user
- Limit to specific schemas
- No DELETE/UPDATE/DROP
- Sanitize queries
- Log all access
