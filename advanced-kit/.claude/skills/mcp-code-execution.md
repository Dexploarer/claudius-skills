---
name: mcp-code-execution
description: Use filesystem-based MCP code execution pattern for 98.7% token savings
trigger: mcp code execution|filesystem mcp|progressive disclosure|code mode mcp|optimize mcp tokens
---

# MCP Code Execution Skill

## Purpose

Implements Anthropic's filesystem-based MCP code execution pattern, achieving **98.7% token savings** by:
1. **Progressive Disclosure** - Discover tools via filesystem instead of loading all upfront
2. **Code Execution** - Write code that calls MCP tools instead of direct tool calls
3. **Context Efficiency** - Keep intermediate results in execution environment
4. **Skills Pattern** - Save reusable functions to `./skills/` directory

**Source:** https://www.anthropic.com/engineering/code-execution-with-mcp

## When to Activate

This skill activates when:
- User mentions "mcp code execution", "code mode", or "progressive disclosure"
- Working with MCP servers and need to optimize token usage
- Processing large datasets through MCP tools
- Building reusable MCP workflows
- User wants to follow Anthropic's recommended MCP pattern

## Core Concepts

### Traditional Approach (Token Intensive)
```
Claude → Direct Tool Call → MCP Server → Result (150,000 tokens)
Claude → Direct Tool Call → MCP Server → Result (150,000 tokens)
...
Total: 150,000+ tokens for tool definitions
```

### Code Execution Approach (Token Efficient)
```
Claude → Discover servers/ → Read only needed tools (2,000 tokens)
Execute Code → Process in environment → Return final result only
Total: ~2,000 tokens (98.7% savings!)
```

## Implementation Pattern

### Step 1: Filesystem-Based Discovery

Create `./servers/` directory structure:

```
servers/
├── google-drive/
│   ├── index.ts
│   ├── getDocument.ts
│   ├── listFiles.ts
│   └── uploadFile.ts
├── salesforce/
│   ├── index.ts
│   ├── getRecords.ts
│   └── updateRecord.ts
└── github/
    ├── index.ts
    ├── listIssues.ts
    └── createIssue.ts
```

Each server is a directory containing:
- `index.ts` - Server metadata and exports
- Individual tool files - One file per tool

### Step 2: Tool File Pattern

Each tool file exports an async function wrapping MCP calls:

```typescript
// servers/google-drive/getDocument.ts

export interface GetDocumentInput {
  documentId: string;
  format?: 'markdown' | 'html' | 'text';
}

export interface GetDocumentResponse {
  content: string;
  title: string;
  lastModified: string;
}

/**
 * Retrieves a Google Drive document by ID
 * @param input - Document ID and optional format
 * @returns Document content and metadata
 */
export async function getDocument(
  input: GetDocumentInput
): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>(
    'google_drive__get_document',
    input
  );
}
```

### Step 3: Discovery Workflow

1. **List Available Servers:**
   ```typescript
   // Agent discovers servers
   const servers = await listDirectory('./servers');
   // Returns: ['google-drive', 'salesforce', 'github']
   ```

2. **Read Tool Definitions:**
   ```typescript
   // Read only the tool needed
   const toolCode = await readFile('./servers/google-drive/getDocument.ts');
   // Parse to understand interface
   ```

3. **Import and Execute:**
   ```typescript
   import { getDocument } from './servers/google-drive/getDocument';

   const doc = await getDocument({ documentId: '123' });
   // Result stays in execution environment
   ```

### Step 4: Optional Search Function

Add `search_tools` for discovery:

```typescript
// servers/search_tools.ts

export interface SearchToolsOptions {
  query: string;
  detailLevel?: 'name' | 'signature' | 'full';
}

/**
 * Search available MCP tools by keyword
 * Enables progressive disclosure - load only what's needed
 */
export async function searchTools(
  options: SearchToolsOptions
): Promise<ToolDefinition[]> {
  const { query, detailLevel = 'signature' } = options;

  // Search ./servers/ directory
  const results: ToolDefinition[] = [];

  for (const server of listServers()) {
    for (const tool of listTools(server)) {
      if (matches(tool, query)) {
        results.push({
          name: tool.name,
          path: `./servers/${server}/${tool.file}`,
          ...(detailLevel === 'signature' && { signature: tool.signature }),
          ...(detailLevel === 'full' && { fullSchema: tool.schema })
        });
      }
    }
  }

  return results;
}
```

### Step 5: Data Processing in Code

Keep large results in execution environment:

```typescript
// GOOD: Process 10,000 rows in code, return only 5
import { queryDatabase } from './servers/database/query';

const allOrders = await queryDatabase({
  table: 'orders',
  limit: 10000
});

// Filter in code - no token cost for full dataset
const pendingOrders = allOrders.filter(o => o.status === 'pending');

// Return only final result (5 orders, not 10,000)
return pendingOrders;
```

**vs**

```typescript
// BAD: Direct tool call returns all 10,000 rows through model
await callTool('query_database', {
  table: 'orders',
  limit: 10000
});
// Model sees all 10,000 rows (huge token cost!)
```

## Skills Pattern

Save reusable workflows to `./skills/`:

### Creating a Skill

```typescript
// ./skills/analyze-spreadsheet.ts

import { readSpreadsheet } from '../servers/google-drive/readSpreadsheet';

/**
 * Analyzes spreadsheet data and generates insights
 * SKILL.md: Activated when user says "analyze spreadsheet"
 */
export async function analyzeSpreadsheet(spreadsheetId: string) {
  // Load data
  const data = await readSpreadsheet({ id: spreadsheetId });

  // Process in execution environment
  const summary = {
    totalRows: data.rows.length,
    columns: data.headers,
    stats: calculateStats(data),
    insights: generateInsights(data)
  };

  // Save for reuse
  await saveToFile('./cache/last-analysis.json', summary);

  return summary;
}

function calculateStats(data: any) {
  // Complex processing happens here
  // No tokens consumed for intermediate steps
}
```

### Skill Metadata File

Create `./skills/SKILL.md`:

```markdown
# Spreadsheet Analyzer

**Activation:** "analyze spreadsheet", "spreadsheet insights"

**What it does:**
- Loads spreadsheet via Google Drive MCP
- Processes data in code (no token cost)
- Generates statistics and insights
- Caches results for reuse

**Usage:**
```
"Analyze spreadsheet ID abc123"
```

**Returns:**
- Row/column counts
- Statistical summary
- Data insights
- Cached for future reference
```

## Privacy & Security Benefits

### Automatic PII Tokenization

For sensitive data, implement tokenization layer:

```typescript
// servers/utils/tokenize.ts

const tokenMap = new Map<string, string>();

export function tokenizePII(text: string): string {
  // Tokenize emails
  text = text.replace(
    /[\w.-]+@[\w.-]+\.\w+/g,
    (email) => {
      const token = `[EMAIL_${tokenMap.size + 1}]`;
      tokenMap.set(token, email);
      return token;
    }
  );

  // Tokenize phone numbers
  text = text.replace(
    /\b\d{3}-\d{3}-\d{4}\b/g,
    (phone) => {
      const token = `[PHONE_${tokenMap.size + 1}]`;
      tokenMap.set(token, phone);
      return token;
    }
  );

  return text;
}

export function untokenize(token: string): string {
  return tokenMap.get(token) || token;
}
```

**Usage:**

```typescript
import { tokenizePII, untokenize } from './servers/utils/tokenize';

// Model sees tokenized version
const data = await getUserData();
const safe = tokenizePII(data.content);
// Model processes: "Contact [EMAIL_1] at [PHONE_1]"

// When passing to another MCP tool, untokenize
await sendEmail({
  to: untokenize('[EMAIL_1]'),  // Real email address
  subject: 'Follow up'
});
```

## Complete Example Workflow

### Scenario: Analyze GitHub Issues

Traditional approach (token intensive):
```javascript
// Load ALL tool definitions upfront (150,000 tokens)
// Call tool, wait for result
const issues = await callTool('github_list_issues', { repo: 'react' });
// Process one at a time
for (const issue of issues) {
  const details = await callTool('github_get_issue', { number: issue.number });
  // Each call goes through model context
}
```

Code execution approach (2,000 tokens):
```typescript
// Discover what's available
const tools = await searchTools({
  query: 'github issues',
  detailLevel: 'signature'  // Just signatures, not full schemas
});

// Read only the tool we need
import { listIssues, getIssue } from './servers/github';

// Execute in code
const issues = await listIssues({ repo: 'facebook/react' });

// Process in execution environment (no token cost)
const analyzed = issues
  .filter(i => i.labels.includes('bug'))
  .sort((a, b) => b.reactions.total - a.reactions.total)
  .slice(0, 10);

// Get details for top 10 only
const detailed = await Promise.all(
  analyzed.map(i => getIssue({ number: i.number }))
);

// Return only final insights (not all 10,000 issues!)
return {
  totalBugs: analyzed.length,
  topIssues: detailed.slice(0, 5).map(d => ({
    number: d.number,
    title: d.title,
    reactions: d.reactions.total
  }))
};
```

**Token comparison:**
- Traditional: 150,000 (tool defs) + 50,000 (all issues) = 200,000 tokens
- Code execution: 2,000 (discovery) + 500 (final result) = 2,500 tokens
- **Savings: 98.75%** ✨

## Implementation Instructions

### When User Requests MCP Integration:

1. **Check for `./servers/` directory**
   - If missing, offer to create it
   - Explain the benefits of filesystem-based approach

2. **Set Up Directory Structure**
   ```bash
   mkdir -p servers/{server-name}
   ```

3. **Create Tool Files**
   - One file per tool
   - TypeScript with full type definitions
   - Export async function wrapping MCP call

4. **Add Search Function (Optional)**
   - Create `servers/search_tools.ts`
   - Enable progressive disclosure

5. **Create Skills for Common Workflows**
   - Save to `./skills/`
   - Add `SKILL.md` for activation
   - Cache results when appropriate

6. **Implement PII Tokenization (if needed)**
   - Create `servers/utils/tokenize.ts`
   - Auto-tokenize sensitive data
   - Untokenize only when passing to trusted MCP tools

### When User Asks to Optimize Existing MCP:

1. **Analyze Current Approach**
   - Identify direct tool calls
   - Measure token usage
   - Find large datasets passing through context

2. **Propose Migration**
   - Show token savings calculation
   - Explain code execution benefits
   - Offer to refactor

3. **Implement Filesystem Structure**
   - Create `./servers/` from existing MCP config
   - Convert tool calls to imported functions
   - Add type definitions

4. **Add Progressive Disclosure**
   - Implement `search_tools`
   - Enable on-demand loading
   - Document discovery patterns

## Best Practices

### ✅ Do:

- **Use filesystem discovery** instead of loading all tools upfront
- **Process data in code** to keep results out of model context
- **Save reusable workflows** to `./skills/` directory
- **Tokenize PII** automatically before model sees it
- **Cache results** in execution environment for reuse
- **Use TypeScript** with full type definitions
- **Document skills** with SKILL.md files
- **Measure token savings** before and after migration

### ❌ Don't:

- Load all tool definitions upfront (old pattern)
- Pass large datasets through model context
- Make sequential tool calls when batch processing in code is faster
- Expose PII to model unnecessarily
- Forget to document skills for future discovery
- Mix traditional and code execution patterns (choose one)

## Security Considerations

### Execution Environment Safety

**Required safeguards:**
- ✅ Sandboxed execution environment
- ✅ Resource limits (CPU, memory, time)
- ✅ Monitoring for malicious code patterns
- ✅ Network access restrictions
- ✅ File system access controls

**Trade-offs:**
- Code execution requires secure sandbox (operational overhead)
- Direct tool calls simpler but token-intensive
- Choose based on use case:
  - High-volume, data-intensive → Code execution
  - Simple, occasional use → Direct tool calls

### Data Privacy

**Intermediate results stay local:**
```typescript
// GOOD: Model never sees full dataset
const users = await database.query('SELECT * FROM users');  // 10,000 rows
const admins = users.filter(u => u.role === 'admin');  // 5 rows
return admins;  // Model only sees 5 rows

// BAD: Model sees everything
return await database.query('SELECT * FROM users');  // 10,000 rows in context!
```

## Framework Integration

### Next.js / React

```typescript
// app/api/mcp/route.ts
import { analyzeData } from '@/skills/analyze-data';

export async function POST(request: Request) {
  const { datasetId } = await request.json();

  // Execute skill (no tokens for processing)
  const result = await analyzeData(datasetId);

  return Response.json(result);
}
```

### Express.js

```typescript
// routes/mcp.ts
import { processOrders } from '../skills/process-orders';

app.post('/api/process-orders', async (req, res) => {
  const orders = await processOrders(req.body.filter);
  res.json(orders);
});
```

### Python (if using Python for execution)

```python
# servers/github/list_issues.py

from typing import TypedDict, List
from mcp_client import call_mcp_tool

class Issue(TypedDict):
    number: int
    title: str
    labels: List[str]

async def list_issues(repo: str) -> List[Issue]:
    """List GitHub issues for a repository"""
    return await call_mcp_tool('github_list_issues', {'repo': repo})
```

## Monitoring & Debugging

### Token Usage Tracking

```typescript
// utils/metrics.ts

export class MCPMetrics {
  private static tokensUsed = 0;

  static trackToolLoad(toolName: string, tokens: number) {
    this.tokensUsed += tokens;
    console.log(`Loaded ${toolName}: ${tokens} tokens`);
  }

  static getSavings(baseline: number): string {
    const savings = ((baseline - this.tokensUsed) / baseline) * 100;
    return `${savings.toFixed(1)}% token savings`;
  }
}
```

### Debug Mode

```typescript
// Enable detailed logging
const DEBUG = process.env.MCP_DEBUG === 'true';

if (DEBUG) {
  console.log('Tools discovered:', tools.map(t => t.name));
  console.log('Token usage:', MCPMetrics.tokensUsed);
}
```

## Migration Guide

### Converting Existing .mcp.json Config

**Before (Traditional):**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
    }
  }
}
```

**After (Code Execution):**

1. Keep `.mcp.json` for MCP server configuration
2. Add `./servers/github/` directory structure:
   ```
   servers/github/
   ├── index.ts         # Export all tools
   ├── listIssues.ts    # Individual tool
   ├── createIssue.ts   # Individual tool
   └── getIssue.ts      # Individual tool
   ```

3. Create tool wrappers:
   ```typescript
   // servers/github/listIssues.ts
   export async function listIssues(input: ListIssuesInput) {
     return callMCPTool('github_list_issues', input);
   }
   ```

4. Use code execution instead of direct calls:
   ```typescript
   import { listIssues } from './servers/github';
   const issues = await listIssues({ repo: 'facebook/react' });
   ```

## Examples

### Example 1: Spreadsheet Analysis (Data-Intensive)

**Traditional approach:** 150,000+ tokens
```javascript
const data = await callTool('read_spreadsheet', { id: '123' });
// All 10,000 rows pass through model context
```

**Code execution:** 2,000 tokens
```typescript
import { readSpreadsheet } from './servers/google-drive';

const data = await readSpreadsheet({ id: '123' });
const summary = {
  totalRows: data.length,
  averages: calculateAverages(data),  // In code, no tokens
  insights: generateInsights(data)     // In code, no tokens
};
return summary;  // Only summary to model
```

### Example 2: Multi-Step Workflow

**Traditional:** Multiple round trips through model
```javascript
const issues = await callTool('list_issues', { repo: 'react' });
// Model processes...
for (const issue of issues) {
  const details = await callTool('get_issue', { number: issue.number });
  // Model processes each...
}
```

**Code execution:** Single execution block
```typescript
import { listIssues, getIssue } from './servers/github';

const issues = await listIssues({ repo: 'facebook/react' });
const detailed = await Promise.all(
  issues.slice(0, 10).map(i => getIssue({ number: i.number }))
);

return analyzeBugs(detailed);  // Process in code
```

### Example 3: Reusable Skill

```typescript
// ./skills/daily-standup.ts

import { listIssues } from '../servers/github';
import { getCalendar } from '../servers/google-calendar';
import { sendMessage } from '../servers/slack';

/**
 * Generates and sends daily standup report
 * SKILL: Activated by "run daily standup"
 */
export async function dailyStandup() {
  // Gather data (in code, efficient)
  const [issues, meetings] = await Promise.all([
    listIssues({ repo: 'our-app', assignee: 'me' }),
    getCalendar({ date: 'today' })
  ]);

  // Process in code (no token cost)
  const report = generateStandupReport(issues, meetings);

  // Send to Slack
  await sendMessage({
    channel: '#daily-standup',
    text: report
  });

  return { sent: true, preview: report };
}
```

**Activation:**
```
User: "Run daily standup"
Claude: [Executes dailyStandup skill]
→ Returns: "Standup report sent to #daily-standup"
```

## Performance Benchmarks

Based on Anthropic's blog post:

| Metric | Traditional | Code Execution | Improvement |
|--------|------------|----------------|-------------|
| Token Usage | 150,000 | 2,000 | 98.7% ↓ |
| Latency | High (multiple roundtrips) | Low (single execution) | 75% ↓ |
| Data Privacy | All data in context | Only results in context | ✅ Better |
| Control Flow | Alternating model/tool | Executes in code | ✅ Faster |

## Related Patterns

- **Cloudflare's "Code Mode":** Independent validation of this approach
- **Skills as Functions:** Reusable code in `./skills/` directory
- **Progressive Disclosure:** Load tool definitions on-demand
- **PII Tokenization:** Privacy-preserving data handling

## References

- **Anthropic Blog Post:** https://www.anthropic.com/engineering/code-execution-with-mcp
- **MCP Specification:** https://modelcontextprotocol.io
- **Cloudflare Code Mode:** (Similar findings independently discovered)

---

**Skill Status:** ✅ Production Ready
**Token Savings:** Up to 98.7%
**Use Cases:** Data-intensive workflows, multi-step processing, privacy-sensitive operations
**Level:** Advanced
