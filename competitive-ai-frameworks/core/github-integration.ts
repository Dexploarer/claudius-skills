/**
 * GitHub Integration Module
 * Automatically creates GitHub issues for competition findings
 * Requires GITHUB_TOKEN in .env file
 */

import * as fs from 'fs';
import * as path from 'path';

export interface GitHubConfig {
  token: string;
  owner: string;
  repo: string;
  minSeverity: string;
  labels: string[];
  assignees?: string[];
  milestone?: number;
  issueMode: 'auto' | 'manual';
}

export interface CompetitionFinding {
  id: string;
  title: string;
  description: string;
  severity: 'critical' | 'high' | 'medium' | 'low';
  team: string;
  category: string;
  file?: string;
  line?: number;
  score: number;
  recommendation?: string;
  codeSnippet?: string;
}

export interface GitHubIssue {
  title: string;
  body: string;
  labels: string[];
  assignees?: string[];
  milestone?: number;
}

/**
 * Load GitHub configuration from .env file
 */
export function loadGitHubConfig(competitionDir: string = '.'): GitHubConfig | null {
  const envPath = path.join(competitionDir, '.env');

  if (!fs.existsSync(envPath)) {
    return null;
  }

  const envContent = fs.readFileSync(envPath, 'utf-8');
  const env: Record<string, string> = {};

  // Parse .env file
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const [key, ...valueParts] = trimmed.split('=');
      const value = valueParts.join('=').trim();
      env[key.trim()] = value;
    }
  });

  // Check if GitHub token is present
  if (!env.GITHUB_TOKEN || !env.GITHUB_OWNER || !env.GITHUB_REPO) {
    return null;
  }

  return {
    token: env.GITHUB_TOKEN,
    owner: env.GITHUB_OWNER,
    repo: env.GITHUB_REPO,
    minSeverity: env.GITHUB_MIN_SEVERITY || 'high',
    labels: env.GITHUB_LABELS ? env.GITHUB_LABELS.split(',').map(l => l.trim()) : ['automated'],
    assignees: env.GITHUB_ASSIGNEES ? env.GITHUB_ASSIGNEES.split(',').map(a => a.trim()) : undefined,
    milestone: env.GITHUB_MILESTONE ? parseInt(env.GITHUB_MILESTONE, 10) : undefined,
    issueMode: (env.GITHUB_ISSUE_MODE as 'auto' | 'manual') || 'manual',
  };
}

/**
 * Check if a finding meets the severity threshold
 */
export function meetsThreshold(finding: CompetitionFinding, config: GitHubConfig): boolean {
  const severityLevels = ['low', 'medium', 'high', 'critical'];
  const findingSeverityIndex = severityLevels.indexOf(finding.severity);
  const minSeverityIndex = severityLevels.indexOf(config.minSeverity);

  return findingSeverityIndex >= minSeverityIndex;
}

/**
 * Format a competition finding as a GitHub issue
 */
export function formatGitHubIssue(finding: CompetitionFinding, framework: string): GitHubIssue {
  const severityEmoji = {
    critical: '🔴',
    high: '🟠',
    medium: '🟡',
    low: '🟢',
  };

  const title = `[${framework}] ${severityEmoji[finding.severity]} ${finding.severity.toUpperCase()}: ${finding.title}`;

  let body = `## Finding Details\n\n`;
  body += `**Severity:** ${finding.severity.toUpperCase()}\n`;
  body += `**Category:** ${finding.category}\n`;
  body += `**Discovered by:** ${finding.team}\n`;
  body += `**Score Impact:** ${finding.score} points\n\n`;

  body += `## Description\n\n${finding.description}\n\n`;

  if (finding.file) {
    body += `## Location\n\n`;
    body += `**File:** \`${finding.file}\`\n`;
    if (finding.line) {
      body += `**Line:** ${finding.line}\n`;
    }
    body += `\n`;
  }

  if (finding.codeSnippet) {
    body += `## Code Snippet\n\n\`\`\`\n${finding.codeSnippet}\n\`\`\`\n\n`;
  }

  if (finding.recommendation) {
    body += `## Recommendation\n\n${finding.recommendation}\n\n`;
  }

  body += `---\n`;
  body += `*This issue was automatically created by the ${framework} competition framework.*\n`;
  body += `*Finding ID: \`${finding.id}\`*\n`;

  return {
    title,
    body,
    labels: [],
    assignees: undefined,
    milestone: undefined,
  };
}

/**
 * Create a GitHub issue using the REST API
 */
export async function createGitHubIssue(
  issue: GitHubIssue,
  config: GitHubConfig
): Promise<{ success: boolean; url?: string; error?: string }> {
  try {
    const apiUrl = `https://api.github.com/repos/${config.owner}/${config.repo}/issues`;

    const payload: any = {
      title: issue.title,
      body: issue.body,
      labels: [...issue.labels, ...config.labels],
    };

    if (config.assignees && config.assignees.length > 0) {
      payload.assignees = config.assignees;
    }

    if (config.milestone) {
      payload.milestone = config.milestone;
    }

    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Accept': 'application/vnd.github+json',
        'Authorization': `Bearer ${config.token}`,
        'X-GitHub-Api-Version': '2022-11-28',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errorText = await response.text();
      return {
        success: false,
        error: `GitHub API error (${response.status}): ${errorText}`,
      };
    }

    const data = await response.json();
    return {
      success: true,
      url: data.html_url,
    };
  } catch (error) {
    return {
      success: false,
      error: error instanceof Error ? error.message : String(error),
    };
  }
}

/**
 * Process competition findings and create GitHub issues
 */
export async function processFindings(
  findings: CompetitionFinding[],
  framework: string,
  config: GitHubConfig,
  dryRun: boolean = false
): Promise<{
  created: number;
  skipped: number;
  failed: number;
  issues: Array<{ finding: CompetitionFinding; url?: string; error?: string }>;
}> {
  const results = {
    created: 0,
    skipped: 0,
    failed: 0,
    issues: [] as Array<{ finding: CompetitionFinding; url?: string; error?: string }>,
  };

  for (const finding of findings) {
    // Check if finding meets threshold
    if (!meetsThreshold(finding, config)) {
      results.skipped++;
      continue;
    }

    // Format as GitHub issue
    const issue = formatGitHubIssue(finding, framework);

    if (dryRun) {
      console.log(`[DRY RUN] Would create issue: ${issue.title}`);
      results.issues.push({ finding, url: '(dry-run)' });
      results.created++;
      continue;
    }

    // Create issue on GitHub
    const result = await createGitHubIssue(issue, config);

    if (result.success) {
      console.log(`✅ Created issue: ${result.url}`);
      results.created++;
      results.issues.push({ finding, url: result.url });
    } else {
      console.error(`❌ Failed to create issue for "${finding.title}": ${result.error}`);
      results.failed++;
      results.issues.push({ finding, error: result.error });
    }
  }

  return results;
}

/**
 * Check if GitHub integration is enabled
 */
export function isGitHubIntegrationEnabled(competitionDir: string = '.'): boolean {
  const config = loadGitHubConfig(competitionDir);
  return config !== null;
}

/**
 * Get GitHub configuration status for display
 */
export function getConfigStatus(competitionDir: string = '.'): string {
  const config = loadGitHubConfig(competitionDir);

  if (!config) {
    return '❌ GitHub integration not configured (no .env file with GITHUB_TOKEN)';
  }

  let status = '✅ GitHub integration enabled\n';
  status += `   Repository: ${config.owner}/${config.repo}\n`;
  status += `   Mode: ${config.issueMode}\n`;
  status += `   Min Severity: ${config.minSeverity}\n`;
  status += `   Labels: ${config.labels.join(', ')}\n`;

  if (config.assignees && config.assignees.length > 0) {
    status += `   Assignees: ${config.assignees.join(', ')}\n`;
  }

  if (config.milestone) {
    status += `   Milestone: #${config.milestone}\n`;
  }

  return status;
}

/**
 * Generate a sample findings array for testing
 */
export function generateSampleFindings(): CompetitionFinding[] {
  return [
    {
      id: 'finding-001',
      title: 'SQL Injection vulnerability in user login',
      description: 'The login endpoint concatenates user input directly into SQL queries without proper sanitization.',
      severity: 'critical',
      team: 'Team 2: Manual Reviewers',
      category: 'SQL Injection',
      file: 'src/auth/login.ts',
      line: 42,
      score: 100,
      recommendation: 'Use parameterized queries or an ORM to prevent SQL injection attacks.',
      codeSnippet: 'const query = `SELECT * FROM users WHERE username = \'${username}\' AND password = \'${password}\'`;',
    },
    {
      id: 'finding-002',
      title: 'Weak password hashing algorithm',
      description: 'Passwords are hashed using MD5, which is cryptographically broken.',
      severity: 'high',
      team: 'Team 1: Automated Scanners',
      category: 'Cryptography',
      file: 'src/auth/password.ts',
      line: 15,
      score: 50,
      recommendation: 'Use bcrypt, scrypt, or Argon2 for password hashing.',
    },
  ];
}
