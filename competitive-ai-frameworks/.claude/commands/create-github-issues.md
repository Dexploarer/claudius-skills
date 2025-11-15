# Create GitHub Issues Command

## Description

Manually create GitHub issues for findings from competitive AI simulations. This command processes competition results and submits qualified findings to GitHub as issues, enabling streamlined bug tracking and team collaboration.

## Usage

```bash
/create-github-issues [options]
```

### Options

- `--framework <name>` - Specify which framework's findings to submit
  - Options: `bug-hunting`, `code-quality`, `user-flows`, `all`
  - Default: Prompt user to select

- `--dry-run` - Preview issues without creating them
  - Shows what would be created
  - Useful for testing configuration

- `--severity <level>` - Override minimum severity threshold
  - Options: `critical`, `high`, `medium`, `low`
  - Overrides `.env` configuration

- `--results <path>` - Path to results JSON file
  - Default: `./results/latest.json`

- `--check-config` - Display current GitHub configuration
  - Shows token status, repository, settings

### Examples

```bash
# Check configuration first
/create-github-issues --check-config

# Preview issues (dry run)
/create-github-issues --framework bug-hunting --dry-run

# Create issues for bug hunting results
/create-github-issues --framework bug-hunting

# Create only critical issues
/create-github-issues --framework all --severity critical

# Create issues from specific results file
/create-github-issues --results ./results/bug-hunt-2024-01-15.json
```

## Prerequisites

### 1. GitHub Configuration

Create a `.env` file in the competition directory:

```bash
# Copy example configuration
cp .env.example .env

# Edit with your details
GITHUB_TOKEN=ghp_your_token_here
GITHUB_OWNER=your-username
GITHUB_REPO=your-repository
```

### 2. Personal Access Token

Create a GitHub PAT at: https://github.com/settings/tokens

Required scopes:
- `repo` (for private repositories)
- `public_repo` (for public repositories only)

### 3. Competition Results

Run a competition first to generate findings:

```bash
/run-bug-hunt --target ./src --rounds 5
# or
/run-quality-check --target ./src --rounds 3
# or
/run-flow-test --flows registration,checkout
```

## Implementation

When this command is executed:

### Step 1: Validate Configuration

```typescript
import { loadGitHubConfig, isGitHubIntegrationEnabled, getConfigStatus } from '../core/github-integration';

// Check if GitHub integration is enabled
if (!isGitHubIntegrationEnabled()) {
  console.error('❌ GitHub integration not configured');
  console.log('\nTo enable GitHub integration:');
  console.log('1. Copy .env.example to .env');
  console.log('2. Set GITHUB_TOKEN from https://github.com/settings/tokens');
  console.log('3. Set GITHUB_OWNER and GITHUB_REPO');
  console.log('\nSee README.md for detailed setup instructions');
  return;
}

// Display current configuration if requested
if (args.includes('--check-config')) {
  console.log(getConfigStatus());
  return;
}
```

### Step 2: Load Competition Results

```typescript
import * as fs from 'fs';
import * as path from 'path';

// Determine results file path
const resultsPath = args.includes('--results')
  ? args[args.indexOf('--results') + 1]
  : './results/latest.json';

// Load results file
if (!fs.existsSync(resultsPath)) {
  console.error(`❌ Results file not found: ${resultsPath}`);
  console.log('\nRun a competition first:');
  console.log('  /run-bug-hunt --target ./src');
  console.log('  /run-quality-check --target ./src');
  console.log('  /run-flow-test --flows registration');
  return;
}

const results = JSON.parse(fs.readFileSync(resultsPath, 'utf-8'));
```

### Step 3: Extract Findings

```typescript
import { CompetitionFinding } from '../core/github-integration';

// Extract findings from results based on framework
let findings: CompetitionFinding[] = [];
const framework = args.includes('--framework')
  ? args[args.indexOf('--framework') + 1]
  : 'all';

if (framework === 'bug-hunting' || framework === 'all') {
  findings.push(...results.bugHunting?.findings || []);
}

if (framework === 'code-quality' || framework === 'all') {
  findings.push(...results.codeQuality?.findings || []);
}

if (framework === 'user-flows' || framework === 'all') {
  findings.push(...results.userFlows?.findings || []);
}

if (findings.length === 0) {
  console.log('ℹ️  No findings to submit');
  return;
}

console.log(`Found ${findings.length} total findings`);
```

### Step 4: Filter by Severity

```typescript
import { meetsThreshold } from '../core/github-integration';

const config = loadGitHubConfig()!;

// Override minimum severity if specified
if (args.includes('--severity')) {
  const severityOverride = args[args.indexOf('--severity') + 1];
  config.minSeverity = severityOverride;
}

// Filter findings by severity threshold
const qualifiedFindings = findings.filter(f => meetsThreshold(f, config));

console.log(`${qualifiedFindings.length} findings meet severity threshold (${config.minSeverity}+)`);

if (qualifiedFindings.length === 0) {
  console.log('ℹ️  No findings meet the severity threshold');
  console.log(`   Current threshold: ${config.minSeverity}`);
  console.log('   Lower threshold in .env or use --severity flag');
  return;
}
```

### Step 5: Process Findings

```typescript
import { processFindings } from '../core/github-integration';

// Check if dry run
const dryRun = args.includes('--dry-run');

if (dryRun) {
  console.log('\n🔍 DRY RUN MODE - No issues will be created\n');
}

// Process findings
const results = await processFindings(
  qualifiedFindings,
  framework === 'all' ? 'Multi-Framework Competition' : framework,
  config,
  dryRun
);

// Display results
console.log('\n' + '='.repeat(60));
console.log('GITHUB ISSUE CREATION RESULTS');
console.log('='.repeat(60));
console.log(`✅ Created:  ${results.created} issues`);
console.log(`⏭️  Skipped:  ${results.skipped} findings (below threshold)`);
console.log(`❌ Failed:   ${results.failed} issues`);
console.log('='.repeat(60));

// Display created issues
if (results.created > 0) {
  console.log('\nCreated Issues:');
  results.issues
    .filter(i => i.url)
    .forEach(({ finding, url }) => {
      console.log(`  🔗 ${finding.title}`);
      console.log(`     ${url}\n`);
    });
}

// Display failures
if (results.failed > 0) {
  console.log('\nFailed Issues:');
  results.issues
    .filter(i => i.error)
    .forEach(({ finding, error }) => {
      console.log(`  ❌ ${finding.title}`);
      console.log(`     Error: ${error}\n`);
    });
}

if (dryRun) {
  console.log('\n💡 Run without --dry-run to create these issues on GitHub');
}
```

### Step 6: Summary and Next Steps

```typescript
// Final summary
if (!dryRun && results.created > 0) {
  console.log('\n✨ Next Steps:');
  console.log(`   1. Review issues at: https://github.com/${config.owner}/${config.repo}/issues`);
  console.log('   2. Assign to team members if not auto-assigned');
  console.log('   3. Prioritize based on severity and score');
  console.log('   4. Create pull requests to fix issues');
  console.log('   5. Run competitions again to verify fixes\n');
}
```

## Configuration Reference

### Environment Variables

```bash
# Required
GITHUB_TOKEN=ghp_xxxxxxxxxxxx        # GitHub Personal Access Token
GITHUB_OWNER=username                # Repository owner (user or org)
GITHUB_REPO=repository-name          # Repository name

# Optional
GITHUB_MIN_SEVERITY=high             # Minimum severity (critical|high|medium|low)
GITHUB_LABELS=security,bug           # Comma-separated labels
GITHUB_ASSIGNEES=user1,user2         # Comma-separated assignees
GITHUB_MILESTONE=5                   # Milestone number
GITHUB_ISSUE_MODE=manual             # auto or manual
```

## Error Handling

### Common Errors and Solutions

**Configuration Not Found:**
```
❌ GitHub integration not configured

Solution:
1. Copy .env.example to .env
2. Add your GITHUB_TOKEN
3. Set GITHUB_OWNER and GITHUB_REPO
```

**Invalid Token:**
```
❌ GitHub API error (401): Bad credentials

Solution:
1. Check GITHUB_TOKEN is correct
2. Verify token hasn't expired
3. Create new token at https://github.com/settings/tokens
```

**Repository Access Denied:**
```
❌ GitHub API error (403): Forbidden

Solution:
1. Verify token has 'repo' or 'public_repo' scope
2. Check repository exists and is accessible
3. Confirm GITHUB_OWNER and GITHUB_REPO are correct
```

**Rate Limited:**
```
❌ GitHub API error (403): Rate limit exceeded

Solution:
1. Wait for rate limit reset (check headers)
2. Create fewer issues per batch
3. Use different token if available
```

**Network Error:**
```
❌ Failed to create issue: Network request failed

Solution:
1. Check internet connection
2. Verify GitHub is accessible
3. Check firewall/proxy settings
4. Retry the command
```

## Best Practices

### 1. Always Dry Run First

```bash
# Preview before creating
/create-github-issues --framework bug-hunting --dry-run
```

### 2. Use Appropriate Severity Thresholds

```bash
# Critical issues only for production
GITHUB_MIN_SEVERITY=critical

# All significant issues for development
GITHUB_MIN_SEVERITY=medium
```

### 3. Organize with Labels

```bash
# Framework-specific labels
GITHUB_LABELS=bug-hunting,security,automated

# Add priority labels
GITHUB_LABELS=high-priority,security,P1
```

### 4. Assign to Team Members

```bash
# Route to security team
GITHUB_ASSIGNEES=security-lead,dev-lead

# Rotate assignments
GITHUB_ASSIGNEES=dev1  # Week 1
GITHUB_ASSIGNEES=dev2  # Week 2
```

### 5. Track with Milestones

```bash
# Assign to current sprint
GITHUB_MILESTONE=12

# Security audit milestone
GITHUB_MILESTONE=5
```

## Integration Examples

### CI/CD Pipeline

```yaml
# .github/workflows/security-scan.yml
name: Security Scan

on:
  push:
    branches: [main]
  schedule:
    - cron: '0 0 * * 0'  # Weekly

jobs:
  bug-hunt:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run Bug Hunt
        run: /run-bug-hunt --target ./src --rounds 5

      - name: Create GitHub Issues
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          /create-github-issues --framework bug-hunting --severity high
```

### Development Workflow

```bash
# 1. Run competition before commit
/run-bug-hunt --target ./src --rounds 3

# 2. Review findings
cat results/latest.json

# 3. Create issues for high-priority findings
/create-github-issues --framework bug-hunting --severity high --dry-run
/create-github-issues --framework bug-hunting --severity high

# 4. Fix issues
# ... make fixes ...

# 5. Verify fixes
/run-bug-hunt --target ./src --rounds 3

# 6. Commit if no critical issues found
git commit -m "fix: security improvements"
```

### Scheduled Audits

```bash
# Weekly comprehensive audit
0 0 * * 0  /run-bug-hunt --target . --rounds 10 && \
           /create-github-issues --framework bug-hunting --severity medium
```

## Security Considerations

1. **Token Security**
   - Never commit `.env` file
   - Use secrets management in CI/CD
   - Rotate tokens regularly
   - Minimum required permissions only

2. **Data Privacy**
   - Review code snippets before submission
   - Redact sensitive information
   - Use private repositories for sensitive findings

3. **Access Control**
   - Limit token scope to specific repositories
   - Review assignee permissions
   - Monitor issue creation logs

## Related Components

- **Skill:** `github-issue-reporter` - Automatic integration
- **Module:** `core/github-integration.ts` - Core functionality
- **Config:** `.env.example` - Configuration template
- **Commands:** `/run-bug-hunt`, `/run-quality-check`, `/run-flow-test`

## Troubleshooting Checklist

- [ ] `.env` file exists in competition directory
- [ ] `GITHUB_TOKEN` is set and valid
- [ ] `GITHUB_OWNER` and `GITHUB_REPO` are correct
- [ ] Token has required scopes (`repo` or `public_repo`)
- [ ] Repository exists and is accessible
- [ ] Competition results file exists
- [ ] Findings meet severity threshold
- [ ] Internet connection is working
- [ ] GitHub API is accessible

---

**Command Type:** Manual Workflow Shortcut
**Requires:** GitHub PAT, .env configuration
**Output:** GitHub issues
**Status:** Production Ready
