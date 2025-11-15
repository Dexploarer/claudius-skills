# Competitive AI Frameworks - Claude Code Configuration

> **Multi-Agent Competitive Simulation Framework**
> Three specialized AI teams compete using reinforcement learning to adapt strategies

**Format:** All configurations follow the standard Claudius Skills template format with proper frontmatter, structured sections, and comprehensive documentation.

---

## 🎯 Framework Overview

This directory contains three competitive AI frameworks:

1. **Bug Hunting Championship** - Security vulnerability detection
2. **Code Quality Championship** - Code improvement competition
3. **User Flow Olympics** - User experience optimization

Each framework:
- Uses 3 competing AI teams with different strategies
- Implements reinforcement learning for strategy adaptation
- Scores performance based on results and quality
- Declares winners and extracts best practices

---

## 🏗️ Architecture

### Components

**1. Subagents** (`.claude/subagents/`)
- Specialized AI team members
- Each has unique strategy and focus areas
- Compete independently in each round

**2. Skills** (`.claude/skills/`)
- Automatic activation based on context
- Orchestrate full championship simulations
- Present results and recommendations

**3. Slash Commands** (`.claude/commands/`)
- Manual invocation of championships
- Quick access to specific frameworks
- Configurable parameters

**4. Python Frameworks** (`frameworks/`)
- Coordinators for each championship
- Scoring engines for performance evaluation
- Reinforcement learning for adaptation
- Metrics tracking across rounds

---

## 🎪 Available Frameworks

### 1. Bug Hunting Championship

**Purpose:** Find security vulnerabilities competitively

**Teams:**
- Team 1: Automated Scanners (pattern matching, static analysis)
- Team 2: Manual Reviewers (business logic, auth/authz)
- Team 3: Fuzzers (race conditions, edge cases)

**Activation:**
- Skill: Mention "find vulnerabilities", "security audit"
- Command: `/run-bug-hunt --target <path>`

**Scoring:**
- CVSS-based severity (Critical=100, High=50, Medium=25, Low=10)
- Uniqueness bonus (+50%)
- Quality bonus (+0-20 points)
- False positive penalty (-20 points)

### 2. Code Quality Championship

**Purpose:** Improve code quality metrics competitively

**Teams:**
- Team 1: Performance Optimizers (runtime, memory, bundle size)
- Team 2: Maintainability Engineers (complexity, documentation)
- Team 3: Best Practices Auditors (style, tests, accessibility)

**Activation:**
- Skill: Mention "improve code quality", "refactor"
- Command: `/run-quality-check --target <path>`

**Scoring:**
- Metrics improvement percentage
- Number of issues resolved
- Impact on overall quality score
- Regression prevention

### 3. User Flow Olympics

**Purpose:** Optimize user experience flows competitively

**Teams:**
- Team 1: Happy Path Optimizers (core flows, conversion)
- Team 2: Edge Case Handlers (error states, accessibility)
- Team 3: Integration Specialists (cross-system flows)

**Activation:**
- Skill: Mention "test user flows", "UX testing"
- Command: `/run-flow-test --flows <list>`

**Scoring:**
- Flow completion success rate
- User experience metrics
- Error handling coverage
- Performance benchmarks

---

## 🧠 Reinforcement Learning

### How It Works

Each team maintains strategy weights that adapt based on performance:

```python
new_weight = old_weight + learning_rate * (reward - baseline) * frequency

# Where:
# - reward: Points earned for this vulnerability/issue type
# - baseline: Historical average for this type
# - frequency: How often this type was found
# - learning_rate: 0.15 (how quickly to adapt)
```

### Adaptation Cycle

```
Round N:
1. Teams execute with current strategy weights
2. Scoring engine evaluates results
3. Reinforcement algorithm updates weights
4. Successful patterns strengthened
5. Failed approaches deprioritized

Round N+1:
6. Teams use adapted strategies
7. Repeat cycle with improved tactics
```

### Benefits

- **Automatic optimization:** Strategies improve over time
- **Competitive evolution:** Teams adapt to competition
- **Pattern recognition:** Successful techniques amplified
- **Mistake learning:** False positives reduce over rounds

---

## 🎮 Usage Guide

### Quick Start

**Run Bug Hunting:**
```bash
/run-bug-hunt --target ./src --rounds 5
```

**Run Code Quality:**
```bash
/run-quality-check --target ./src --rounds 3
```

**Run User Flow Testing:**
```bash
/run-flow-test --flows registration,checkout,profile
```

### Automatic Activation

Skills activate automatically on relevant mentions:

```
User: "I need to find security vulnerabilities in this codebase"
→ bug-hunting-simulator skill activates

User: "Help me improve the code quality"
→ code-quality-analyzer skill activates

User: "Test all user flows"
→ user-flow-tester skill activates
```

### Advanced Configuration

**Focus on specific team:**
```bash
/run-bug-hunt --target ./src --team manual
```

**More rounds for better adaptation:**
```bash
/run-quality-check --target ./src --rounds 10
```

**With visualization:**
```bash
/run-bug-hunt --target ./src --visualize
```

---

## 📊 Understanding Results

### Championship Output

Each championship provides:

1. **Final Standings**
   - Winner with total score
   - Runner-up teams
   - Performance breakdown

2. **Top Discoveries**
   - Best findings from all teams
   - Severity/impact ratings
   - Remediation guidance

3. **Strategy Analysis**
   - Why the winner succeeded
   - Key techniques used
   - Performance metrics

4. **Combined Recommendations**
   - Best practices from all teams
   - Optimal approach synthesis
   - Implementation guidance

### Example Output

```
🥇 WINNER: Team 2 - Manual Reviewers
   Score: 1,450 points
   Critical Bugs: 2
   False Positive Rate: 5%

WINNING STRATEGY:
- Focused on business logic flaws
- Deep authentication analysis
- High-quality vulnerability reports

RECOMMENDED APPROACH:
1. Start with automated scanning (Team 1)
2. Follow with manual review (Team 2)
3. Apply fuzzing to critical areas (Team 3)
```

---

## 🔐 Security & Ethics

### Authorized Use Only

**Always confirm:**
- ✅ User has authorization to test
- ✅ Defensive security or educational purpose
- ✅ User's own code or authorized environment

**Never assist with:**
- ❌ Unauthorized penetration testing
- ❌ Malicious exploitation
- ❌ Production system attacks without authorization
- ❌ Evasion of security controls

### Built-in Safety

- Authorization confirmation required
- Read-only analysis by default
- No automatic exploitation
- All activities logged

---

## 📁 Directory Structure

```
competitive-ai-frameworks/
├── .claude/
│   ├── skills/                    # Automatic capabilities
│   │   ├── bug-hunting-simulator.md
│   │   ├── code-quality-analyzer.md
│   │   ├── user-flow-tester.md
│   │   └── github-issue-reporter.md  # GitHub integration (optional)
│   ├── commands/                  # Manual shortcuts
│   │   ├── run-bug-hunt.md
│   │   ├── run-quality-check.md
│   │   ├── run-flow-test.md
│   │   └── create-github-issues.md   # Manual issue creation
│   ├── subagents/                 # Team specialists
│   │   ├── team1-automated-scanner.md
│   │   ├── team2-manual-reviewer.md
│   │   ├── team3-fuzzer.md
│   │   └── [9 more team configs]
│   ├── hooks/                     # Event automation
│   │   └── scoring-tracker.json
│   └── rules/                     # Framework rules
│       └── CLAUDE.md (this file)
├── core/                          # Core modules
│   ├── agent_pool.ts             # Agent management
│   ├── github-integration.ts     # GitHub API integration
│   └── index.ts
├── frameworks/                    # Core implementations
│   ├── bug-hunting/
│   │   ├── coordinator.py
│   │   ├── scoring_engine.py
│   │   ├── metrics.py
│   │   └── reinforcement.py
│   ├── code-quality/
│   └── user-flows/
├── examples/                      # Example targets
├── docs/                          # Documentation
└── README.md                      # Main guide
```

---

## 🎓 Educational Value

### Learn About

**Multi-Agent Systems:**
- Competitive AI coordination
- Strategy differentiation
- Performance comparison

**Reinforcement Learning:**
- Policy gradient methods
- Reward-based adaptation
- Exploration vs exploitation

**Security Testing:**
- Vulnerability detection methodologies
- Bug bounty scoring (CVSS)
- Responsible disclosure

**Code Quality:**
- Quality metrics (complexity, coverage)
- Best practices enforcement
- Technical debt reduction

---

## 🚀 Extending Frameworks

### Add New Team

1. Create subagent config in `.claude/subagents/team4-<name>.md`
2. Define strategy and focus areas
3. Update coordinator to include new team
4. Test and validate

### Customize Scoring

Edit `frameworks/*/scoring_engine.py`:

```python
SEVERITY_SCORES = {
    'critical': 150,  # Increase critical weight
    'high': 75,
    ...
}
```

### Adjust Learning Rate

Edit `frameworks/*/reinforcement.py`:

```python
LEARNING_RATE = 0.2  # Faster adaptation
EXPLORATION_RATE = 0.15  # More exploration
```

---

## 🔗 GitHub Integration (Optional Feature)

### Overview

Competition findings can be automatically submitted as GitHub issues for streamlined bug tracking and team collaboration. This is an **optional feature** that requires user configuration.

### When to Use

Activate GitHub integration when:
- User mentions "create github issues" or "report to github"
- User asks to "export findings to github"
- User requests "github integration" after competition
- User has configured `.env` file with GitHub credentials

### Prerequisites Check

**ALWAYS verify before attempting GitHub integration:**

```typescript
import { isGitHubIntegrationEnabled, getConfigStatus } from './core/github-integration';

// Check if .env exists and has required fields
if (!isGitHubIntegrationEnabled()) {
  console.log('ℹ️  GitHub integration not configured (optional)');
  console.log('To enable: copy .env.example to .env and set GITHUB_TOKEN');
  return;
}

// Display current configuration
console.log(getConfigStatus());
```

### Configuration Requirements

User must create `.env` file with:

**Required:**
- `GITHUB_TOKEN` - Personal Access Token from https://github.com/settings/tokens
- `GITHUB_OWNER` - Repository owner (username or organization)
- `GITHUB_REPO` - Repository name

**Optional:**
- `GITHUB_MIN_SEVERITY` - Minimum severity (critical|high|medium|low)
- `GITHUB_LABELS` - Comma-separated labels
- `GITHUB_ASSIGNEES` - Comma-separated GitHub usernames
- `GITHUB_MILESTONE` - Milestone number
- `GITHUB_ISSUE_MODE` - auto or manual (default: manual)

### Workflow

1. **Check Configuration**
   ```bash
   /create-github-issues --check-config
   ```

2. **Preview Issues (Dry Run)**
   ```bash
   /create-github-issues --framework bug-hunting --dry-run
   ```

3. **Create Actual Issues**
   ```bash
   /create-github-issues --framework bug-hunting
   ```

### Integration Points

**Skills:**
- `github-issue-reporter.md` - Handles automatic GitHub integration
- Activates on user request when `.env` is configured

**Commands:**
- `/create-github-issues` - Manual issue creation command
- Supports dry-run mode and severity filtering

**Core Module:**
- `core/github-integration.ts` - All GitHub API functionality
- Functions for config loading, issue formatting, API calls

### Issue Format

Created issues follow this structure:

**Title:** `[Framework Name] 🔴 SEVERITY: Issue Title`

**Body includes:**
- Finding details (severity, category, team, score)
- Full description
- File location and line number
- Code snippet (if available)
- Remediation recommendations
- Finding ID for tracking

**Metadata:**
- Labels from configuration
- Assignees (if configured)
- Milestone (if configured)

### Security Considerations

**CRITICAL - Never commit `.env` file:**
- Add `.env` to `.gitignore`
- Use `.env.example` for documentation only
- Token must have minimum required scopes
- Review code snippets before submission

**Token Permissions:**
- `repo` scope for private repositories
- `public_repo` scope for public repositories only

### Error Handling

Handle GitHub API errors gracefully:

**Configuration Missing:**
```
❌ GitHub integration not configured
→ Inform user this is optional
→ Show how to set up if desired
→ Continue without GitHub integration
```

**Invalid Token:**
```
❌ GitHub API error (401): Bad credentials
→ Ask user to verify GITHUB_TOKEN
→ Suggest creating new token
→ Provide token creation URL
```

**Rate Limit:**
```
❌ GitHub API error (403): Rate limit exceeded
→ Inform user to wait or use different token
→ Suggest reducing issue creation frequency
```

### Modes

**Manual Mode (Default):**
```bash
GITHUB_ISSUE_MODE=manual
```
- Issues only created on explicit command
- Safer for testing and review
- User has full control

**Auto Mode:**
```bash
GITHUB_ISSUE_MODE=auto
```
- Issues created automatically after competition
- Useful for CI/CD pipelines
- User should be notified of created issues

### Best Practices

1. **Always offer dry-run first**
   - Preview issues before creating
   - User can review and adjust configuration

2. **Respect user's severity threshold**
   - Only create issues meeting configured minimum
   - Allow override via command flag

3. **Provide clear feedback**
   - Show how many issues created/skipped/failed
   - Display URLs of created issues
   - Report any errors clearly

4. **Handle absence gracefully**
   - GitHub integration is OPTIONAL
   - Never block core functionality if not configured
   - Simply inform user it's available if interested

### Example Usage

```typescript
// After bug hunting competition completes
if (isGitHubIntegrationEnabled()) {
  const config = loadGitHubConfig();

  if (config.issueMode === 'auto') {
    console.log('📤 Creating GitHub issues (auto mode)...');
    const results = await processFindings(findings, 'Bug Hunting', config);
    console.log(`✅ Created ${results.created} GitHub issues`);
  } else {
    console.log('💡 GitHub integration available.');
    console.log('   Run: /create-github-issues --framework bug-hunting');
  }
} else {
  console.log('💡 Optional: Configure GitHub integration to auto-create issues');
  console.log('   See .env.example for setup instructions');
}
```

### Integration Module API

**Key Functions:**

```typescript
// Check if enabled
isGitHubIntegrationEnabled(): boolean

// Load configuration
loadGitHubConfig(): GitHubConfig | null

// Get status display
getConfigStatus(): string

// Check severity threshold
meetsThreshold(finding, config): boolean

// Format issue
formatGitHubIssue(finding, framework): GitHubIssue

// Create issue
createGitHubIssue(issue, config): Promise<Result>

// Process batch
processFindings(findings, framework, config, dryRun): Promise<Results>
```

### Related Components

- **Skill:** `.claude/skills/github-issue-reporter.md`
- **Command:** `.claude/commands/create-github-issues.md`
- **Module:** `core/github-integration.ts`
- **Config:** `.env.example`

---

## 🐛 Troubleshooting

**Issue:** Too many false positives
**Solution:** Increase validation, raise false positive penalty

**Issue:** Not finding critical bugs
**Solution:** Increase manual review team weight, add more rounds

**Issue:** Simulation too slow
**Solution:** Reduce rounds, focus on specific team

**Issue:** Strategies not improving
**Solution:** Increase exploration rate, verify reward signals

---

## 📚 Documentation

Full documentation:
- `README.md` - Complete project guide
- `docs/bug-hunting-guide.md` - Bug hunting details
- `docs/scoring-system.md` - Scoring methodology
- `docs/reinforcement-learning.md` - RL algorithm details
- `docs/extending-frameworks.md` - Customization guide

---

## 🎯 Success Metrics

Frameworks succeed when:
- All rounds complete successfully
- Clear winner determined
- Actionable recommendations provided
- Strategies demonstrably improve over rounds
- User understands results and next steps

---

## 💡 Tips for Best Results

1. **Run multiple rounds** (5-10) for strategy adaptation
2. **Use visualization** to see improvement over time
3. **Focus teams** on their strengths
4. **Combine approaches** for optimal coverage
5. **Iterate** - run again after fixes to verify

---

## 🔗 Integration

These frameworks integrate with:

**Claude Code Tools:**
- `Grep` - Pattern matching and searching
- `Read` - Code file analysis
- `Bash` - Running tests and tools
- `Edit` - Applying fixes (if requested)

**External Tools:**
- Static analysis tools (bandit, eslint, etc.)
- Testing frameworks (pytest, jest, etc.)
- Security scanners (if available)
- Performance profilers

---

**Built with Claude Code's Five Pillars of Extensibility**
**Part of the Claudius Skills Project**
**Educational • Defensive Security • Code Quality**
