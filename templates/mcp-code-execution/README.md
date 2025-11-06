# MCP Code Execution Templates

Templates for implementing Anthropic's filesystem-based MCP code execution pattern.

## Overview

These templates help you achieve **98.7% token savings** by using:
- **Filesystem-based discovery** - `./servers/` directory structure
- **Code execution** - Write code that imports/calls MCP tools
- **Progressive disclosure** - Load only needed tool definitions
- **Skills pattern** - Reusable functions in `./skills/`

**Source:** https://www.anthropic.com/engineering/code-execution-with-mcp

## Templates Included

### 1. Server Directory Structure
```
servers/
├── {server-name}/
│   ├── index.ts        # Exports all tools
│   ├── tool1.ts        # Individual tool wrapper
│   ├── tool2.ts        # Individual tool wrapper
│   └── README.md       # Server documentation
└── utils/
    ├── tokenize.ts     # PII tokenization
    └── metrics.ts      # Token usage tracking
```

### 2. Individual Tool Template
See: `tool-template.ts`

### 3. Search Tools Function
See: `search-tools-template.ts`

### 4. Skills Pattern
See: `skills/` directory

### 5. Complete Example
See: `example-github-integration/`

## Quick Start

### Option 1: Copy Entire Structure

```bash
# Copy to your project
cp -r templates/mcp-code-execution/servers ./servers
cp -r templates/mcp-code-execution/skills ./skills

# Customize for your MCP servers
```

### Option 2: Create Custom Server

```bash
# Use the tool template
cp templates/mcp-code-execution/tool-template.ts servers/my-server/myTool.ts

# Edit and customize
```

### Option 3: Use Skill Activation

In Claude Code:
```
"Set up MCP code execution pattern for GitHub integration"
```

Claude will use the `mcp-code-execution` skill to set up the structure automatically.

## Usage Examples

### Example 1: GitHub Integration

```typescript
// servers/github/listIssues.ts
import { callMCPTool } from '../utils/mcp-client';

export interface ListIssuesInput {
  repo: string;
  state?: 'open' | 'closed' | 'all';
  labels?: string[];
}

export interface Issue {
  number: number;
  title: string;
  state: string;
  labels: string[];
}

export async function listIssues(
  input: ListIssuesInput
): Promise<Issue[]> {
  return callMCPTool<Issue[]>('github_list_issues', input);
}
```

**Usage in code:**
```typescript
import { listIssues } from './servers/github';

// Discover and load only when needed
const issues = await listIssues({
  repo: 'facebook/react',
  state: 'open'
});

// Process in code (no token cost)
const bugIssues = issues.filter(i =>
  i.labels.includes('bug')
);

return bugIssues;  // Only final result to model
```

### Example 2: Data Processing

```typescript
// skills/analyze-spreadsheet.ts
import { readSpreadsheet } from '../servers/google-drive';

export async function analyzeSpreadsheet(id: string) {
  // Load data via MCP
  const data = await readSpreadsheet({ id });

  // Process in code (efficient, no tokens)
  const summary = {
    rows: data.length,
    stats: calculateStatistics(data),
    insights: generateInsights(data)
  };

  // Return only summary
  return summary;
}
```

## Migration from Traditional MCP

### Before (Traditional - 150,000 tokens)

```json
// .mcp.json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    }
  }
}
```

```javascript
// Usage - all tools loaded upfront
const issues = await callTool('github_list_issues', { repo: 'react' });
```

### After (Code Execution - 2,000 tokens)

```json
// .mcp.json (still needed for server config)
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    }
  }
}
```

```typescript
// servers/github/listIssues.ts (new)
export async function listIssues(input: ListIssuesInput) {
  return callMCPTool('github_list_issues', input);
}
```

```typescript
// Usage - progressive disclosure
import { listIssues } from './servers/github';
const issues = await listIssues({ repo: 'facebook/react' });
```

**Token savings:** 98.7%! ✨

## Directory Structure Details

### Recommended Structure

```
project/
├── .mcp.json                    # MCP server configuration (keep this)
├── servers/                     # NEW: Filesystem-based tools
│   ├── github/
│   │   ├── index.ts            # Export all GitHub tools
│   │   ├── listIssues.ts       # List issues
│   │   ├── createIssue.ts      # Create issue
│   │   ├── getIssue.ts         # Get issue details
│   │   └── README.md           # GitHub integration docs
│   ├── google-drive/
│   │   ├── index.ts
│   │   ├── getDocument.ts
│   │   ├── listFiles.ts
│   │   └── README.md
│   ├── database/
│   │   ├── index.ts
│   │   ├── query.ts
│   │   └── README.md
│   ├── search_tools.ts         # Progressive disclosure
│   └── utils/
│       ├── mcp-client.ts       # MCP client wrapper
│       ├── tokenize.ts         # PII tokenization
│       └── metrics.ts          # Token tracking
├── skills/                      # NEW: Reusable workflows
│   ├── analyze-spreadsheet.ts
│   ├── daily-standup.ts
│   ├── process-orders.ts
│   └── SKILL.md                # Skill activation patterns
└── src/                         # Your application code
    └── ...
```

### Minimal Structure

```
project/
├── .mcp.json
├── servers/
│   └── {your-server}/
│       ├── index.ts
│       └── tool1.ts
└── skills/
    └── your-skill.ts
```

## Key Benefits

### 1. Token Efficiency (98.7% savings)
- **Before:** 150,000 tokens (all tool definitions)
- **After:** 2,000 tokens (load only what's needed)

### 2. Performance
- **Before:** Multiple roundtrips through model
- **After:** Single code execution block

### 3. Privacy
- **Before:** All data passes through model context
- **After:** Only final results in context, intermediate data stays in execution environment

### 4. Control Flow
- **Before:** Alternate between tool calls and model reasoning
- **After:** Loops, conditionals, error handling in code

## Progressive Disclosure

### Search Function Example

```typescript
// Discover tools by keyword
const tools = await searchTools({
  query: 'github issues',
  detailLevel: 'signature'  // name | signature | full
});

// Returns:
// [
//   {
//     name: 'listIssues',
//     path: './servers/github/listIssues.ts',
//     signature: 'listIssues(input: ListIssuesInput): Promise<Issue[]>'
//   }
// ]

// Load only what you need
import { listIssues } from tools[0].path;
```

## PII Tokenization

Automatically protect sensitive data:

```typescript
import { tokenizePII, untokenize } from './servers/utils/tokenize';

// Model sees tokenized version
const data = await getUserData();
const safe = tokenizePII(data);
// "Contact [EMAIL_1] at [PHONE_1]"

// When passing to MCP tool, untokenize
await sendEmail({
  to: untokenize('[EMAIL_1]'),  // Real email
  subject: 'Follow up'
});
```

## Token Usage Tracking

Monitor savings:

```typescript
import { MCPMetrics } from './servers/utils/metrics';

MCPMetrics.trackToolLoad('listIssues', 500);
MCPMetrics.trackToolLoad('getIssue', 300);

console.log(MCPMetrics.getSavings(150000));
// "99.5% token savings"
```

## Best Practices

### ✅ Do:
- Use filesystem discovery instead of loading all tools
- Process large datasets in code
- Save reusable workflows to `./skills/`
- Tokenize PII before model sees it
- Cache results in execution environment
- Use TypeScript with full type definitions

### ❌ Don't:
- Load all tool definitions upfront (old pattern)
- Pass large datasets through model context
- Make sequential tool calls when batch processing is possible
- Expose PII to model unnecessarily
- Mix traditional and code execution patterns

## Security Considerations

### Required for Code Execution:
- ✅ Sandboxed execution environment
- ✅ Resource limits (CPU, memory, time)
- ✅ Monitoring for malicious code
- ✅ Network access restrictions
- ✅ File system access controls

### Choose Approach Based on Use Case:
- **High-volume, data-intensive** → Code execution (98.7% savings)
- **Simple, occasional use** → Direct tool calls (simpler setup)

## Examples by Use Case

### 1. Data Analysis (Large Datasets)
Best fit: **Code execution** (keeps data in environment)

### 2. Workflow Automation (Multi-step)
Best fit: **Code execution** (reduces roundtrips)

### 3. Simple Queries (Occasional use)
Best fit: **Traditional** (simpler if infrequent)

### 4. Privacy-Sensitive (PII data)
Best fit: **Code execution** (tokenization layer)

## Next Steps

1. **Choose a template** that matches your use case
2. **Copy to your project** and customize
3. **Test with one MCP server** first
4. **Measure token savings** before/after
5. **Expand to more servers** as needed
6. **Create skills** for common workflows

## Support

- **Skill:** Use `mcp-code-execution` skill in Claude Code
- **Documentation:** See `advanced-kit/.claude/skills/mcp-code-execution.md`
- **Anthropic Blog:** https://www.anthropic.com/engineering/code-execution-with-mcp

---

**Template Status:** ✅ Production Ready
**Token Savings:** Up to 98.7%
**Level:** Advanced
