# Competitive AI Team Simulations Framework

> Multi-agent competitive frameworks for bug hunting, code quality assessment, and user flow testing using Claude Code's extensibility features. **Built with TypeScript** for type safety and modern development.

## ✅ Production Ready - v2.0

**Status:** This framework is now production-ready with real AI agent integration, deep context gathering, and Semgrep SAST scanning.

**New in v2.0:**
- ✅ Real Claude AI agents via Task tool (not just grep)
- ✅ 25+ Semgrep security rules for advanced pattern matching
- ✅ Enhanced subagents with detailed analysis processes
- ✅ Test application with 19 intentional vulnerabilities
- ✅ All dependencies installed and tested
- 📚 See [PRODUCTION_GUIDE.md](./PRODUCTION_GUIDE.md) for complete documentation

## 🎯 Overview

This framework leverages Claude Code's **Five Pillars of Extensibility** to create competitive team-based AI simulations:

1. **Bug Hunting Arena** - 3 teams compete to find vulnerabilities
2. **Code Quality Championship** - Teams race to improve code metrics
3. **User Flow Olympics** - Teams optimize complete user journeys

Each framework uses:
- **Subagents** - Specialized AI team members with unique strategies
- **Skills** - Automated capabilities for analysis and testing
- **Slash Commands** - Quick simulation execution
- **Hooks** - Event-driven scoring and tracking
- **Reinforcement Learning** - Adaptive strategy improvement

## 🏆 Framework Architecture

### Bug Hunting Simulation

**Three Competing Teams:**

- **Team 1: Automated Scanners**
  - Pattern recognition and static analysis
  - SAST/DAST tool integration
  - Dependency vulnerability scanning

- **Team 2: Manual Reviewers**
  - Deep code review and logic flaw detection
  - Business logic vulnerabilities
  - Authentication/authorization issues

- **Team 3: Fuzzers & Behavioral Analysts**
  - Input fuzzing and edge case testing
  - Runtime behavior analysis
  - Race condition detection

**Scoring System:**
- CVSS severity ratings (Critical: 100pts, High: 50pts, Medium: 25pts, Low: 10pts)
- Uniqueness bonus (first to find: +50%)
- False positive penalty (-20 pts)
- Quality of report (0-20 bonus points)
- Time to discovery bonus (faster = higher multiplier)

### Code Quality Championship

**Three Competing Teams:**

- **Team 1: Performance Optimizers**
  - Runtime complexity analysis
  - Memory usage optimization
  - Bundle size reduction

- **Team 2: Maintainability Engineers**
  - Code complexity metrics
  - Documentation coverage
  - Design pattern enforcement

- **Team 3: Best Practices Auditors**
  - Style guide compliance
  - Test coverage analysis
  - Accessibility standards

**Scoring System:**
- Metrics improvement percentage
- Number of issues resolved
- Impact on overall quality score
- Regression prevention

### User Flow Olympics

**Three Competing Teams:**

- **Team 1: Happy Path Optimizers**
  - Core flow completion time
  - Conversion rate optimization
  - UX friction reduction

- **Team 2: Edge Case Handlers**
  - Error state coverage
  - Accessibility compliance
  - Mobile responsiveness

- **Team 3: Integration Specialists**
  - Cross-system flows
  - API integration testing
  - State management validation

**Scoring System:**
- Flow completion success rate
- User experience metrics
- Error handling coverage
- Performance benchmarks

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
cd competitive-ai-frameworks
npm install

# Build TypeScript
npm run build

# Copy to your project
cp -r competitive-ai-frameworks/.claude /path/to/your/project/

# Or use specific framework
cp -r competitive-ai-frameworks/frameworks/bug-hunting /path/to/your/project/
```

### Running Simulations

```bash
# Using slash commands (from your project)
/run-bug-hunt --rounds 5 --target ./src
/run-quality-check --rounds 3 --baseline main
/run-flow-test --rounds 4 --flows user-registration,checkout

# Using TypeScript coordinator
cd competitive-ai-frameworks

# Run bug hunting
npm run bug-hunt -- --target /path/to/codebase --rounds 5

# Run code quality analysis
npm run code-quality -- --target /path/to/codebase --rounds 3

# Run user flow testing
npm run user-flow -- --target /path/to/codebase --rounds 4

# Using skills (automatic)
# Just mention: "I need to find security vulnerabilities in this codebase"
# The bug-hunting-simulator skill will activate automatically
```

## 📊 Reinforcement Learning System

### Learning Mechanism

Each team maintains:
- **Strategy weights** - Adjusted based on success rates
- **Pattern library** - Successful detection patterns
- **False positive memory** - Avoid repeated mistakes
- **Time efficiency metrics** - Optimize discovery speed

### Adaptation Cycle

```
Round N:
1. Teams execute with current strategies
2. Scoring engine evaluates results
3. Reinforcement algorithm updates weights
4. Successful patterns strengthened
5. Failed approaches deprioritized

Round N+1:
6. Teams use adapted strategies
7. Repeat cycle with improved tactics
```

### Strategy Evolution

```typescript
// Simplified reinforcement learning formula
const new_weight = old_weight + learning_rate * (reward - baseline) * action_frequency;

// Rewards:
// - Successful bug discovery: +reward based on severity
// - False positive: -penalty
// - Duplicate finding: 0 (neutral)
// - Quality report: +bonus
```

## 🛠️ Tech Stack

### TypeScript Implementation

This framework is built entirely in **TypeScript** for:
- **Type Safety** - Catch errors at compile time
- **Modern Development** - ES2022+ features with full IDE support
- **Maintainability** - Clear interfaces and strong typing
- **Performance** - Compiled to optimized JavaScript

### Dependencies

```json
{
  "runtime": {
    "Node.js": ">=18.0.0",
    "TypeScript": "^5.3.3"
  },
  "development": {
    "ts-node": "^10.9.2",
    "jest": "^29.7.0",
    "eslint": "^8.56.0",
    "prettier": "^3.1.1"
  }
}
```

### Build & Run

```bash
# Development mode (with ts-node)
npm run dev

# Production build
npm run build

# Run tests
npm test

# Lint code
npm run lint
```

## 🎓 Educational Value

### Learn About:
- Multi-agent coordination
- Competitive AI strategies
- Reinforcement learning basics
- Security vulnerability assessment
- Code quality metrics
- User experience testing
- **TypeScript best practices**
- **Type-safe AI frameworks**

### Use Cases:
- **Security Training** - Learn bug hunting methodologies
- **Code Review** - Improve review processes
- **Testing Strategy** - Optimize testing approaches
- **Team Performance** - Compare different strategies

## 🔧 Configuration

### Customize Team Strategies

Edit subagent configurations in `.claude/subagents/`:

```markdown
# .claude/subagents/team1-automated-scanner.md

You are Team 1: Automated Scanner specialist.

**Your Strategy:**
- Focus on pattern-based vulnerability detection
- Prioritize high-severity issues
- Use static analysis techniques
- Scan dependencies for known CVEs

**Tools at your disposal:**
- grep/ripgrep for pattern matching
- AST parsing for code structure
- Dependency graph analysis
- OWASP Top 10 checklist
```

### Adjust Scoring Weights

Edit `frameworks/*/scoring_engine.ts`:

```typescript
const SEVERITY_SCORES: Record<Severity, number> = {
  [Severity.CRITICAL]: 100,
  [Severity.HIGH]: 50,
  [Severity.MEDIUM]: 25,
  [Severity.LOW]: 10,
  [Severity.INFO]: 5
};

// Bonus multipliers
const UNIQUENESS_BONUS = 0.5;      // 50% bonus for first discovery
const QUALITY_BONUS_MAX = 20;       // Up to 20 points for report quality
const SPEED_BONUS_MAX = 1.3;        // Up to 30% bonus for fast discovery
```

## 🔗 GitHub Integration (Optional)

### Automatic Issue Creation

Competition findings can be automatically submitted as GitHub issues for streamlined bug tracking and team collaboration.

### Setup

1. **Create a GitHub Personal Access Token**

   Visit: https://github.com/settings/tokens

   Required scopes:
   - `repo` (for private repositories)
   - `public_repo` (for public repositories only)

2. **Configure Environment Variables**

   ```bash
   # Copy the example configuration
   cp .env.example .env

   # Edit .env with your credentials
   GITHUB_TOKEN=ghp_your_token_here
   GITHUB_OWNER=your-username-or-org
   GITHUB_REPO=your-repository-name
   ```

3. **Optional Configuration**

   ```bash
   # Minimum severity to create issues (critical, high, medium, low)
   GITHUB_MIN_SEVERITY=high

   # Labels to apply (comma-separated)
   GITHUB_LABELS=bug-hunting,security,automated

   # Assignees (comma-separated GitHub usernames)
   GITHUB_ASSIGNEES=developer1,developer2

   # Milestone number
   GITHUB_MILESTONE=5

   # Mode: auto (create automatically) or manual (require explicit command)
   GITHUB_ISSUE_MODE=manual
   ```

### Usage

**Check Configuration:**
```bash
/create-github-issues --check-config
```

**Preview Issues (Dry Run):**
```bash
/create-github-issues --framework bug-hunting --dry-run
```

**Create Issues:**
```bash
# After running a competition
/run-bug-hunt --target ./src --rounds 5

# Create GitHub issues for findings
/create-github-issues --framework bug-hunting

# Create only critical severity issues
/create-github-issues --framework bug-hunting --severity critical

# Create issues for all frameworks
/create-github-issues --framework all
```

### Issue Format

Created GitHub issues include:

- **Title:** `[Bug Hunting Championship] 🔴 CRITICAL: SQL Injection in login endpoint`
- **Body:** Detailed description, location, code snippet, and recommendations
- **Labels:** Configured labels (e.g., `bug-hunting`, `security`, `automated`)
- **Assignees:** Configured team members
- **Milestone:** If configured

### Automatic vs Manual Mode

**Manual Mode (Default):**
```bash
GITHUB_ISSUE_MODE=manual
```
- Issues only created when explicitly requested via command
- Safer for testing and review

**Automatic Mode:**
```bash
GITHUB_ISSUE_MODE=auto
```
- Issues automatically created after each competition
- Useful for CI/CD integration

### Security Considerations

- ⚠️ Never commit `.env` file to version control
- ✅ Use `.env.example` for documentation only
- ✅ Rotate tokens periodically
- ✅ Use minimum required token permissions
- ✅ Review code snippets before submission to avoid exposing sensitive data

### Related Components

- **Skill:** `github-issue-reporter` - Handles automatic integration
- **Command:** `/create-github-issues` - Manual issue creation
- **Module:** `core/github-integration.ts` - Core functionality
- **Config:** `.env.example` - Configuration template

## 📁 Project Structure

```
competitive-ai-frameworks/
├── .claude/                          # Claude Code configurations
│   ├── skills/                       # Automated capabilities
│   │   ├── bug-hunting-simulator.md
│   │   ├── code-quality-analyzer.md
│   │   ├── user-flow-tester.md
│   │   └── github-issue-reporter.md # GitHub integration (optional)
│   ├── commands/                     # Manual shortcuts
│   │   ├── run-bug-hunt.md
│   │   ├── run-quality-check.md
│   │   ├── run-flow-test.md
│   │   └── create-github-issues.md  # Manual issue creation
│   ├── subagents/                    # Team AI specialists
│   │   ├── team1-automated-scanner.md
│   │   ├── team2-manual-reviewer.md
│   │   ├── team3-fuzzer.md
│   │   └── [9 more team agents]
│   ├── hooks/                        # Event-driven automation
│   │   └── scoring-tracker.json
│   └── rules/                        # Framework rules
│       └── CLAUDE.md
├── core/                             # Core modules
│   ├── agent_pool.ts                # Agent management
│   ├── github-integration.ts        # GitHub API integration
│   └── index.ts
├── frameworks/                       # Core implementations
│   ├── bug-hunting/
│   │   ├── coordinator.py           # Orchestrates teams
│   │   ├── scoring_engine.py        # Calculates scores
│   │   ├── metrics.py               # Tracks performance
│   │   ├── reinforcement.py         # RL algorithm
│   │   └── teams/                   # Team implementations
│   ├── code-quality/
│   └── user-flows/
├── examples/                         # Example targets
│   ├── bug-hunting/
│   │   ├── vulnerable-app/          # Intentionally buggy
│   │   └── sample-reports/
│   ├── code-quality/
│   │   └── sample-codebases/
│   └── user-flows/
│       └── sample-apps/
├── docs/                             # Documentation
│   ├── bug-hunting-guide.md
│   ├── scoring-system.md
│   ├── reinforcement-learning.md
│   └── extending-frameworks.md
├── scripts/                          # Utility scripts
│   ├── setup.sh
│   ├── run-simulation.sh
│   └── analyze-results.py
├── .env.example                      # GitHub integration config template
├── .gitignore                        # Git ignore rules
├── package.json                      # Node.js dependencies
└── tsconfig.json                     # TypeScript configuration
```

## 📈 Example Results

### Bug Hunting Round 5 Results:

```
┌──────────────────────────────────────────────────────┐
│  Bug Hunting Championship - Final Standings         │
├──────────────────────────────────────────────────────┤
│  🥇 Team 2: Manual Reviewers          Score: 1,250  │
│     - 2 Critical bugs (CVSS 9+)                      │
│     - 5 High severity bugs                           │
│     - 3 Medium severity bugs                         │
│     - False positive rate: 5%                        │
│     - Avg time to discovery: 12 min                  │
├──────────────────────────────────────────────────────┤
│  🥈 Team 3: Fuzzers                   Score: 1,100  │
│     - 1 Critical bug (race condition)                │
│     - 6 High severity bugs                           │
│     - 8 Medium severity bugs                         │
│     - False positive rate: 15%                       │
│     - Avg time to discovery: 8 min                   │
├──────────────────────────────────────────────────────┤
│  🥉 Team 1: Automated Scanners        Score: 950    │
│     - 0 Critical bugs                                │
│     - 8 High severity bugs                           │
│     - 12 Medium severity bugs                        │
│     - False positive rate: 25%                       │
│     - Avg time to discovery: 3 min                   │
└──────────────────────────────────────────────────────┘

Winning Strategy Analysis:
Team 2 excelled by focusing on business logic flaws that
automated tools miss. Key techniques:
- Authentication flow analysis
- Authorization boundary testing
- Input validation deep-dive
- SQL injection in complex queries

Recommended Combined Approach:
1. Start with Team 1's automated scanning (fast coverage)
2. Apply Team 2's manual review to critical paths
3. Use Team 3's fuzzing on identified attack surfaces
```

## 🔬 Advanced Features

### Multi-Round Evolution

Watch strategies improve over 10+ rounds:

```bash
python frameworks/bug-hunting/coordinator.py --rounds 10 --visualize
```

Teams learn:
- Which vulnerability types they excel at
- Time vs quality tradeoffs
- Pattern recognition improvements
- False positive reduction

### Custom Team Creation

Add your own team with unique strategy:

```bash
cp .claude/subagents/team-template.md .claude/subagents/team4-ml-detector.md
# Edit to define ML-based detection strategy
```

### Integration with CI/CD

```yaml
# .github/workflows/security-championship.yml
name: Weekly Bug Hunt Championship

on:
  schedule:
    - cron: '0 0 * * 0'  # Every Sunday

jobs:
  bug-hunt:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Bug Hunting Championship
        run: |
          cd competitive-ai-frameworks
          python frameworks/bug-hunting/coordinator.py --rounds 5
      - name: Post Results
        run: python scripts/post-to-slack.py results.json
```

## 🛡️ Security & Ethics

### Responsible Use

This framework is designed for:
- ✅ Educational purposes
- ✅ Authorized security testing
- ✅ CTF competitions
- ✅ Defensive security research
- ✅ Code quality improvement

**NOT for:**
- ❌ Unauthorized penetration testing
- ❌ Malicious exploitation
- ❌ Production system attacks
- ❌ Privacy violations

### Built-in Safeguards

- Requires explicit target specification
- Logs all activities
- No automatic exploitation
- Read-only analysis by default

## 🤝 Contributing

Want to add new teams or strategies?

1. Fork the repository
2. Create team subagent in `.claude/subagents/`
3. Implement strategy in `frameworks/*/teams/`
4. Add tests and documentation
5. Submit pull request

## 📚 Documentation

- [Bug Hunting Guide](docs/bug-hunting-guide.md) - Detailed methodology
- [Scoring System](docs/scoring-system.md) - How points are calculated
- [Reinforcement Learning](docs/reinforcement-learning.md) - RL algorithm details
- [Extending Frameworks](docs/extending-frameworks.md) - Add your own teams

## 📝 License

MIT License - See LICENSE file

## 🎯 Roadmap

- [ ] Team 4: AI/ML-based detection
- [ ] Web dashboard for live results
- [ ] Multi-language support (currently Python-focused)
- [ ] Cloud deployment templates
- [ ] Real-time collaboration mode
- [ ] Integration with popular security tools

## 💡 Inspiration

This framework demonstrates how Claude Code's extensibility can create sophisticated multi-agent systems that learn and compete, providing both educational value and practical security/quality improvements.

---

**Built with Claude Code's Five Pillars of Extensibility**
**Part of the Claudius Skills Project**
