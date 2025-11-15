---
name: github-issue-reporter
description: Automatically report competition findings as GitHub issues when configured
triggers:
  - "create github issues"
  - "report to github"
  - "github integration"
  - "export findings to github"
  - "submit issues"
---

# GitHub Issue Reporter

## Purpose

Automatically create GitHub issues for significant findings discovered during competitive AI simulations (Bug Hunting, Code Quality, User Flow testing). This skill integrates with GitHub's API to streamline issue tracking and team collaboration.

## Activation

This skill activates when:
- User mentions "create github issues" or "report to github"
- User says "export findings to github" or "submit issues"
- User requests "github integration" after a competition
- Competition results include findings worthy of tracking

## Prerequisites

Before this skill can function, the following must be configured:

1. **GitHub Personal Access Token (PAT)**
   - Create at: https://github.com/settings/tokens
   - Required scopes: `repo` (private) or `public_repo` (public only)

2. **Environment Configuration**
   - Copy `.env.example` to `.env` in the competition directory
   - Set `GITHUB_TOKEN`, `GITHUB_OWNER`, `GITHUB_REPO`
   - Configure optional settings (labels, assignees, severity threshold)

3. **Repository Access**
   - Token must have write access to the target repository
   - Repository must exist and be accessible

## Configuration Options

### Required Variables

```bash
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
GITHUB_OWNER=your-username-or-org
GITHUB_REPO=your-repository
```

### Optional Variables

```bash
# Minimum severity to create issues (critical, high, medium, low)
GITHUB_MIN_SEVERITY=high

# Labels to apply to all created issues (comma-separated)
GITHUB_LABELS=bug-hunting,security,automated

# Assignees for created issues (comma-separated GitHub usernames)
GITHUB_ASSIGNEES=developer1,developer2

# Milestone number to assign issues to
GITHUB_MILESTONE=5

# Issue creation mode (auto or manual)
GITHUB_ISSUE_MODE=manual
```

## Workflow

### 1. Check Configuration

First, verify GitHub integration is properly configured:

```typescript
import { getConfigStatus, isGitHubIntegrationEnabled } from './core/github-integration';

if (!isGitHubIntegrationEnabled()) {
  console.log('GitHub integration not configured.');
  console.log('Copy .env.example to .env and set your GITHUB_TOKEN');
  return;
}

console.log(getConfigStatus());
```

### 2. Collect Competition Findings

After a competition completes, extract findings that meet the severity threshold:

```typescript
import { CompetitionFinding } from './core/github-integration';

const findings: CompetitionFinding[] = [
  {
    id: 'bug-001',
    title: 'SQL Injection in login endpoint',
    description: 'User input concatenated directly into SQL query',
    severity: 'critical',
    team: 'Team 2: Manual Reviewers',
    category: 'SQL Injection',
    file: 'src/auth/login.ts',
    line: 42,
    score: 100,
    recommendation: 'Use parameterized queries',
    codeSnippet: 'SELECT * FROM users WHERE ...',
  },
  // ... more findings
];
```

### 3. Process Findings (Dry Run)

First, run in dry-run mode to preview what would be created:

```typescript
import { loadGitHubConfig, processFindings } from './core/github-integration';

const config = loadGitHubConfig();
if (!config) {
  console.error('GitHub configuration not found');
  return;
}

const results = await processFindings(
  findings,
  'Bug Hunting Championship',
  config,
  true // dry-run mode
);

console.log(`Would create: ${results.created} issues`);
console.log(`Would skip: ${results.skipped} findings (below threshold)`);
```

### 4. Create GitHub Issues

If the preview looks good, create the actual issues:

```typescript
const results = await processFindings(
  findings,
  'Bug Hunting Championship',
  config,
  false // live mode
);

console.log(`✅ Created: ${results.created} issues`);
console.log(`⏭️  Skipped: ${results.skipped} findings`);
console.log(`❌ Failed: ${results.failed} issues`);

results.issues.forEach(({ finding, url, error }) => {
  if (url) {
    console.log(`  - ${finding.title}: ${url}`);
  } else {
    console.log(`  - ${finding.title}: ERROR - ${error}`);
  }
});
```

## Issue Format

Created GitHub issues follow this format:

**Title:**
```
[Bug Hunting Championship] 🔴 CRITICAL: SQL Injection in login endpoint
```

**Body:**
```markdown
## Finding Details

**Severity:** CRITICAL
**Category:** SQL Injection
**Discovered by:** Team 2: Manual Reviewers
**Score Impact:** 100 points

## Description

User input concatenated directly into SQL query without sanitization.

## Location

**File:** `src/auth/login.ts`
**Line:** 42

## Code Snippet

```
SELECT * FROM users WHERE username = '${username}'
```

## Recommendation

Use parameterized queries or an ORM to prevent SQL injection attacks.

---
*This issue was automatically created by the Bug Hunting Championship competition framework.*
*Finding ID: `bug-001`*
```

**Labels:** bug-hunting, security, automated (from config)
**Assignees:** (if configured)
**Milestone:** (if configured)

## Severity Filtering

Only findings meeting or exceeding the configured minimum severity are created:

| Min Severity | Creates Issues For |
|--------------|-------------------|
| `low` | low, medium, high, critical |
| `medium` | medium, high, critical |
| `high` | high, critical |
| `critical` | critical only |

## Auto vs Manual Mode

### Manual Mode (Default)

```bash
GITHUB_ISSUE_MODE=manual
```

Issues are only created when explicitly requested:
- User runs `/create-github-issues` command
- User explicitly asks to "create github issues"

### Auto Mode

```bash
GITHUB_ISSUE_MODE=auto
```

Issues are automatically created after each competition:
- Findings meeting threshold are submitted immediately
- User is notified of created issues
- Useful for continuous integration workflows

## Error Handling

The skill handles common errors gracefully:

**Invalid Token:**
```
❌ GitHub API error (401): Bad credentials
Check that GITHUB_TOKEN is valid and not expired
```

**Repository Not Found:**
```
❌ GitHub API error (404): Not Found
Verify GITHUB_OWNER and GITHUB_REPO are correct
Token must have access to the repository
```

**Rate Limit:**
```
❌ GitHub API error (403): Rate limit exceeded
Wait for rate limit to reset or use a different token
```

**Network Error:**
```
❌ Failed to create issue: Network request failed
Check internet connection and try again
```

## Security Considerations

1. **Token Security**
   - Never commit `.env` file to version control
   - Use `.env.example` for documentation only
   - Rotate tokens periodically
   - Use tokens with minimum required permissions

2. **Data Privacy**
   - Review findings before creating issues
   - Ensure no sensitive data in code snippets
   - Consider using private repositories

3. **Rate Limiting**
   - GitHub API allows 5,000 requests/hour for authenticated users
   - Batch creation of many issues may hit limits
   - Add delays between requests if needed

## Integration with Competitions

### Bug Hunting Championship

```bash
/run-bug-hunt --target ./src --rounds 5

# After competition completes:
/create-github-issues --framework bug-hunting
```

### Code Quality Championship

```bash
/run-quality-check --target ./src --rounds 3

# After competition completes:
/create-github-issues --framework code-quality
```

### User Flow Olympics

```bash
/run-flow-test --flows registration,checkout

# After competition completes:
/create-github-issues --framework user-flows
```

## Testing

Test the integration with sample data:

```typescript
import { generateSampleFindings, processFindings, loadGitHubConfig } from './core/github-integration';

const sampleFindings = generateSampleFindings();
const config = loadGitHubConfig();

if (config) {
  // Dry run first
  const results = await processFindings(sampleFindings, 'Test Framework', config, true);
  console.log('Test results:', results);
}
```

## Best Practices

1. **Start with Dry Run**
   - Always test with `dryRun: true` first
   - Review what would be created
   - Adjust configuration if needed

2. **Use Appropriate Severity Threshold**
   - `critical` - Only most severe issues
   - `high` - Important issues only
   - `medium` - All significant findings
   - `low` - Everything (may create many issues)

3. **Configure Labels**
   - Use labels for filtering and organization
   - Examples: `security`, `performance`, `bug-hunting`, `automated`
   - Helps team prioritize and track

4. **Set Assignees**
   - Assign to relevant team members
   - Ensures issues get attention
   - Can route different severities to different people

5. **Use Milestones**
   - Track issues by sprint/release
   - Organize work across competitions
   - Monitor progress over time

## Troubleshooting

**Issues not being created:**
- Check `.env` file exists and has correct values
- Verify token has write access to repository
- Check severity threshold configuration
- Review console for error messages

**Duplicate issues:**
- Issues are created each time command runs
- Check for existing issues manually
- Consider using finding IDs to detect duplicates
- Future enhancement: duplicate detection

**Wrong repository:**
- Verify `GITHUB_OWNER` and `GITHUB_REPO` in `.env`
- Check token has access to specified repository
- Confirm repository name spelling

## Future Enhancements

Potential improvements:
- Duplicate detection using finding IDs
- Issue update/closure when findings resolved
- Custom issue templates
- Batch processing with rate limiting
- Integration with GitHub Projects
- Comment on existing issues with updates

## Examples

### Complete Workflow

```bash
# 1. Set up configuration
cp .env.example .env
# Edit .env with your GitHub token and repository

# 2. Run a competition
/run-bug-hunt --target ./src --rounds 5

# 3. Review findings in results

# 4. Test issue creation (dry run)
/create-github-issues --framework bug-hunting --dry-run

# 5. Create actual issues
/create-github-issues --framework bug-hunting

# 6. Check GitHub repository for new issues
```

## Related Components

- **Command:** `/create-github-issues` - Manual issue creation
- **Module:** `core/github-integration.ts` - Core functionality
- **Config:** `.env.example` - Configuration template
- **Skills:** `bug-hunting-simulator`, `code-quality-analyzer`, `user-flow-tester`

---

**Status:** Production Ready
**Requires:** GitHub PAT, .env configuration
**Platform:** GitHub API v3
**TypeScript:** Yes
