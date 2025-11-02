# Module 2: The 5 Pillars of AI-Assisted Development

**Master the architecture that powers professional AI game development**

---

## Lesson 2.1: Skills - Automatic Code Generation

### What Are Skills?

Imagine having a team of specialist developers who automatically jump in when you need them.

Writing a README? **README specialist appears**
Finding bugs? **Debugging expert appears**
Need tests? **Testing specialist appears**

**That's what Skills do.**

Skills are context-aware AI capabilities that trigger automatically based on what you're doing.

### How Skills Work

Traditional development:
```
You: *manually typing a README*
You: *struggling with formatting*
You: *searching for examples*
You: *copying and pasting*
Result: Mediocre README after 30 minutes
```

With Skills:
```
You: *working on a project*
AI: "I notice you don't have a README. Want me to create one?"
You: "Yes!"
AI: *generates professional README with all sections*
Result: Perfect README in 30 seconds
```

### The 5 Essential Skills for Game Developers

**Skill 1: README Generator**
```
Triggers when: You're in a project without a README
What it does: Creates professional documentation
Includes:
- Project description
- Installation instructions
- Usage examples
- API documentation
- Screenshots and demos
```

**Example output:**
```markdown
# My Awesome Game

A fast-paced 2D platformer built with HTML5 Canvas and AI assistance.

## Features
- Smooth character movement
- 20 unique levels
- Boss battles
- High score system

## Installation
npm install
npm start

## Controls
- Arrow Keys: Move
- Space: Jump
- Shift: Sprint

## Screenshots
[Auto-generated from game]
```

**Skill 2: Code Explainer**
```
Triggers when: You're reading unfamiliar code
What it does: Explains what code does in plain English
Perfect for:
- Understanding game engines
- Learning new frameworks
- Debugging others' code
- Teaching junior developers
```

**Example:**
You see:
```javascript
const deltaTime = (timestamp - lastFrameTime) / 1000;
player.velocity.y += GRAVITY * deltaTime;
player.position.y += player.velocity.y * deltaTime;
```

AI explains:
```
This is a physics simulation using delta time:

1. Calculate time since last frame (in seconds)
2. Apply gravity to vertical velocity
3. Update player's Y position based on velocity

Why delta time? Ensures consistent physics regardless
of frame rate. If the game runs at 30 FPS or 60 FPS,
player falls at the same speed.
```

**Skill 3: Bug Finder**
```
Triggers when: Your game has errors
What it does: Identifies and fixes bugs automatically
Catches:
- Null reference errors
- Memory leaks
- Performance bottlenecks
- Logic errors
- Edge cases
```

**Real example:**
```javascript
// Your code
function spawnEnemy() {
    enemies.push(new Enemy());
}

// Bug Finder detects:
⚠️ Memory leak: Enemies never removed from array
⚠️ No bounds checking: Will slow down over time
⚠️ Missing cleanup: removeEventListener not called

// Suggests fix:
function spawnEnemy() {
    const enemy = new Enemy();
    enemies.push(enemy);

    // Auto-cleanup when enemy dies
    enemy.onDeath = () => {
        const index = enemies.indexOf(enemy);
        if (index > -1) {
            enemies.splice(index, 1);
            enemy.cleanup();
        }
    };
}
```

**Skill 4: Test Helper**
```
Triggers when: You need tests
What it does: Generates comprehensive test suites
Creates:
- Unit tests
- Integration tests
- Edge case tests
- Performance tests
```

**Example:**
Your game code:
```javascript
function calculateDamage(attack, defense) {
    return Math.max(1, attack - defense);
}
```

AI generates tests:
```javascript
describe('calculateDamage', () => {
    it('should deal damage when attack > defense', () => {
        expect(calculateDamage(10, 5)).toBe(5);
    });

    it('should deal minimum 1 damage', () => {
        expect(calculateDamage(5, 10)).toBe(1);
    });

    it('should handle equal values', () => {
        expect(calculateDamage(10, 10)).toBe(1);
    });

    it('should handle zero defense', () => {
        expect(calculateDamage(10, 0)).toBe(10);
    });

    it('should handle negative values', () => {
        expect(calculateDamage(-5, 10)).toBe(1);
    });
});
```

**Skill 5: Git Helper**
```
Triggers when: Working with version control
What it does: Makes Git effortless
Helps with:
- Commit messages
- Branch management
- Merge conflicts
- Rollbacks
```

**Example:**
You made changes to 10 files.

Traditional Git:
```bash
git add .
git commit -m "stuff"  # Lazy commit message
git push
```

With Git Helper:
```bash
# AI analyzes your changes
AI: "You've modified:
- Player controller (added double jump)
- Enemy AI (fixed pathfinding bug)
- UI system (updated health bar)

Suggested commit message:
feat: Add double jump mechanic
fix: Resolve enemy pathfinding edge case
style: Update health bar visual styling

Create separate commits for each?"
```

### Installing Skills

**Option 1: Use Starter Kit (Easiest)**
```bash
cp -r starter-kit/.claude /path/to/your/game/
```

Includes all 5 essential skills!

**Option 2: Install Individual Skills**
```bash
# In your game project
mkdir -p .claude/skills

# Copy skills you want
cp path/to/readme-generator.md .claude/skills/
cp path/to/bug-finder.md .claude/skills/
```

**Option 3: Create Custom Skills**

Create `.claude/skills/my-skill.md`:
```markdown
# My Custom Skill

You are an expert in [specific area].

When the user is working on [specific task],
automatically help by [specific action].

## Examples
[Examples of when to trigger]

## Response Format
[How to respond]
```

### Skills in Action: Real Workflow

Watch how skills work together:

```
9:00 AM - Start new game project
  ↓
  README Generator: "Create documentation?"
  ✅ Professional README created

9:05 AM - Write player controller
  ↓
  Code Explainer: Shows examples from similar games
  ✅ Built controller in 5 minutes

9:10 AM - Test the controller
  ↓
  Bug Finder: "Detected jump not working when moving"
  ✅ Fixed edge case automatically

9:15 AM - Ready to commit
  ↓
  Test Helper: "No tests found. Generate?"
  ✅ Full test suite created

9:20 AM - Commit code
  ↓
  Git Helper: "Suggest professional commit message?"
  ✅ Clean git history

Result: 20 minutes, production-ready feature with tests and docs
```

### Advanced Skills (Intermediate/Advanced)

Once you master the basics, unlock these power-ups:

**Performance Skills:**
- Image Optimizer
- Bundle Analyzer
- Database Query Optimizer

**Security Skills:**
- Dependency Scanner
- PII Detector
- Security Header Generator

**Game-Specific Skills:**
- Three.js Scene Builder
- React Native Component Generator
- Smart Contract Generator (Web3)

**We'll cover these in later modules!**

### Community Challenge

**Task:** Install the Starter Kit and use at least 3 skills

**Share:**
1. Which skill saved you the most time?
2. Screenshot of AI-generated output
3. One "wow" moment

**Tag:** #skills-challenge

---

## Lesson 2.2: Slash Commands - One-Command Workflows

### What Are Slash Commands?

Slash commands are your magic shortcuts. One command = complete workflow.

Think of them as your personal assistant who knows exactly what you need.

### The Power of Slash Commands

**Without slash commands:**
```
1. Run linter
2. Fix linting errors
3. Run tests
4. Fix test failures
5. Build project
6. Check for errors
7. Stage files
8. Write commit message
9. Commit
10. Push to GitHub

Time: 15-20 minutes
```

**With slash commands:**
```
/commit

Time: 30 seconds
```

AI automatically does ALL 10 steps!

### Essential Slash Commands

**Command 1: /commit**
```
What it does:
1. Analyzes all changes
2. Runs linter and fixes issues
3. Runs tests
4. Generates commit message
5. Creates commit
6. Pushes to remote

Usage:
/commit

Advanced:
/commit --no-push  # Commit but don't push
/commit --amend    # Amend last commit
```

**Command 2: /debug**
```
What it does:
1. Analyzes error messages
2. Identifies root cause
3. Suggests fixes
4. Optionally applies fix
5. Re-runs to verify

Usage:
/debug

With error:
/debug TypeError: Cannot read property 'x' of undefined
```

**Command 3: /test**
```
What it does:
1. Generates test suite
2. Runs all tests
3. Shows coverage report
4. Identifies untested code
5. Suggests additional tests

Usage:
/test
/test --watch    # Watch mode
/test --coverage # Show coverage
```

**Command 4: /refactor**
```
What it does:
1. Analyzes code quality
2. Identifies improvements
3. Refactors code
4. Maintains functionality
5. Adds tests for changes

Usage:
/refactor
/refactor player-controller.js
```

**Command 5: /docs**
```
What it does:
1. Generates JSDoc comments
2. Creates API documentation
3. Builds documentation site
4. Updates README
5. Adds usage examples

Usage:
/docs
/docs --format markdown
```

### Intermediate Commands (Level 2-3)

**Command 6: /deploy**
```
Complete deployment workflow:
1. Runs all tests
2. Builds production bundle
3. Optimizes assets
4. Deploys to hosting
5. Updates DNS
6. Sends notification

Usage:
/deploy production
/deploy staging
```

**Command 7: /performance-profile**
```
Performance analysis:
1. Runs benchmarks
2. Identifies bottlenecks
3. Suggests optimizations
4. Shows before/after metrics

Usage:
/performance-profile
/performance-profile --flame-graph
```

**Command 8: /security-audit**
```
Security scanning:
1. Scans dependencies
2. Checks for vulnerabilities
3. Tests for common exploits
4. Generates report
5. Suggests fixes

Usage:
/security-audit
/security-audit --fix
```

### Advanced Commands (Level 4-5)

**Command 9: /release-orchestrator**
```
Full release process:
1. Version bump
2. Changelog generation
3. Build all platforms
4. Run full test suite
5. Create GitHub release
6. Deploy to production
7. Notify team

Usage:
/release-orchestrator patch
/release-orchestrator minor
/release-orchestrator major
```

**Command 10: /compliance-scan**
```
Compliance checking:
1. Scans for GDPR compliance
2. Checks accessibility (WCAG)
3. Security standards
4. Performance budgets
5. Generates report

Usage:
/compliance-scan soc2
/compliance-scan hipaa
```

### Creating Custom Commands

Want your own slash commands? Easy!

Create `.claude/commands/my-command.md`:

```markdown
# My Custom Command

When the user types /my-command:

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Example
User: /my-command
AI: [Response]
```

**Real example - Game Build Command:**

`.claude/commands/game-build.md`:
```markdown
# Game Build Command

When the user types /game-build:

1. Run linter on all game code
2. Optimize all image assets
3. Minify JavaScript
4. Build production bundle
5. Test on all target platforms
6. Generate build report
7. Create downloadable packages

Show progress for each step.
```

Usage:
```
/game-build

Output:
✅ Linted 47 files (0 errors)
✅ Optimized 124 images (saved 2.3 MB)
✅ Minified JavaScript (467 KB → 156 KB)
✅ Built production bundle
✅ Tested on Windows, Mac, Linux
✅ Generated build report
✅ Created packages:
   - game-windows-v1.0.zip
   - game-mac-v1.0.dmg
   - game-linux-v1.0.AppImage
```

### Command Chaining

Combine commands for power combos:

```
/test && /refactor && /commit

Result:
1. Runs all tests
2. Refactors code if tests pass
3. Commits changes with message
```

```
/security-audit && /fix && /test && /commit

Result:
1. Scans for vulnerabilities
2. Fixes issues found
3. Tests fixes
4. Commits secure code
```

### Starter Kit Commands

When you install the Starter Kit, you get 12 commands:

1. `/commit` - Smart git commits
2. `/debug` - Intelligent debugging
3. `/docs` - Documentation generation
4. `/explain` - Code explanations
5. `/quickfix` - Fast bug fixes
6. `/refactor` - Code improvement
7. `/review` - Code review
8. `/setup` - Project setup
9. `/test` - Test generation
10. `/todo` - Task management
11. `/clean` - Code cleanup
12. `/deps` - Dependency management

**Install:**
```bash
cp -r starter-kit/.claude/commands /path/to/your/game/.claude/
```

### Pro Tips

**Tip 1: Use flags**
```
/commit --no-test  # Skip tests
/deploy --dry-run  # Preview only
/refactor --aggressive  # More changes
```

**Tip 2: Context matters**
```
# In a React file
/refactor
→ Applies React best practices

# In a Python file
/refactor
→ Applies Python best practices
```

**Tip 3: Chain wisely**
```
✅ /test && /commit
❌ /commit && /test  # Backwards!
```

### Community Challenge

**Create your own custom command!**

Requirements:
1. Solves a problem you face often
2. Has at least 3 steps
3. Saves you real time

**Share:**
- Command name
- What it does
- Time saved per use
- Tag #custom-command

**Bonus:** Most useful command wins a feature in the official kit!

---

## Lesson 2.3: Hooks - Event-Driven Automation

### What Are Hooks?

Hooks are your safety net. Your automatic quality control. Your "never forget again" system.

They run AUTOMATICALLY when specific events happen.

### Real-World Example: The $10,000 Mistake

True story from our community:

Developer accidentally committed API keys to GitHub.
Bots found them in 4 minutes.
$10,000 AWS bill in 2 days.

**With hooks? This never happens.**

### How Hooks Work

```
Event Happens → Hook Triggers → AI Takes Action
```

**Example:**
```
You type: git commit
  ↓
Hook scans for API keys, passwords, tokens
  ↓
Hook finds: OPENAI_API_KEY=sk-abc123
  ↓
Hook STOPS commit and warns you
  ↓
You fix it
  ↓
Saved from $10,000 bill
```

### Essential Hooks

**Hook 1: Secret Detection (PreCommit)**
```
Triggers: Before every git commit
Checks for:
- API keys
- Passwords
- Private keys
- Database credentials
- OAuth tokens

Example:
You: git commit -m "Add feature"
Hook: ⚠️ BLOCKED - Found API key in .env
You: *moves to .gitignore*
Hook: ✅ Safe to commit
```

**Hook 2: Force Push Prevention**
```
Triggers: Before git push --force
Protects:
- main branch
- master branch
- production branch

Example:
You: git push --force origin main
Hook: ⚠️ DANGER - Force push to main!
      This will overwrite team's work.
      Type "I know what I'm doing" to proceed.
```

**Hook 3: Test Failure Alerts (PostTest)**
```
Triggers: After running tests
Actions:
- Shows which tests failed
- Explains why they failed
- Suggests fixes
- Creates issue if critical

Example:
Tests run: 47 passed, 3 failed
  ↓
Hook analyzes failures:
  ↓
Hook: "Player jump test failed because gravity
       constant was changed. Reset to 9.8 or
       update test expectations?"
```

**Hook 4: Build Size Monitoring (PostBuild)**
```
Triggers: After building project
Checks:
- Bundle size
- Asset sizes
- Dependency sizes

Example:
Build complete: 2.4 MB
  ↓
Hook: ⚠️ Bundle size increased 400 KB!

      Largest additions:
      - three.js: +300 KB
      - lodash: +100 KB

      Suggestions:
      - Use three.js core only
      - Replace lodash with native methods
```

**Hook 5: Package Installation Reminders**
```
Triggers: After npm/pip install
Reminds:
- Update .env if needed
- Run migrations
- Rebuild if necessary

Example:
npm install mongoose
  ↓
Hook: ✅ Mongoose installed

      Remember to:
      1. Set MONGODB_URI in .env
      2. Run database migrations
      3. Restart your server
```

### Hook Types

**PreToolUse Hooks** (Run BEFORE action)
- Validate before committing
- Check before pushing
- Confirm before deleting
- Scan before deploying

**PostToolUse Hooks** (Run AFTER action)
- Track what changed
- Alert on failures
- Update documentation
- Notify team

### Installing Hooks

**Option 1: Starter Kit**
```bash
cp -r starter-kit/.claude/hooks /path/to/your/game/.claude/
```

Includes all essential safety hooks!

**Option 2: Custom Hooks**

Create `.claude/hooks/my-hook.json`:
```json
{
  "name": "my-hook",
  "trigger": "before_commit",
  "action": "check for debug code",
  "block_if_found": true
}
```

### Real Hooks Configuration

**Secret Detection Hook:**

`.claude/hooks/secret-detection.json`:
```json
{
  "name": "secret-detection",
  "trigger": "before_commit",
  "patterns": [
    "api[_-]?key",
    "password",
    "secret",
    "token",
    "private[_-]?key"
  ],
  "exclude_files": [
    ".env.example",
    "docs/"
  ],
  "action": "block",
  "message": "⚠️ Potential secret detected! Review before committing."
}
```

**Debug Code Checker:**

`.claude/hooks/debug-checker.json`:
```json
{
  "name": "debug-checker",
  "trigger": "before_commit",
  "patterns": [
    "console.log",
    "debugger;",
    "TODO:",
    "FIXME:"
  ],
  "action": "warn",
  "message": "⚠️ Debug code found. Remove before committing?"
}
```

### Advanced Hook Workflows

**Hook Chain Example:**

```
1. PreCommit: Secret Detection
   ↓ (if clean)
2. PreCommit: Debug Code Check
   ↓ (if clean)
3. PreCommit: Run Tests
   ↓ (if passing)
4. Commit Allowed
   ↓
5. PostCommit: Update Docs
   ↓
6. PostCommit: Notify Team
```

**Deployment Safety:**

```
1. PreDeploy: Run Full Test Suite
2. PreDeploy: Security Scan
3. PreDeploy: Performance Check
4. PreDeploy: Backup Database
5. Deploy (if all pass)
6. PostDeploy: Health Check
7. PostDeploy: Rollback if Failed
```

### Common Hook Patterns

**Pattern 1: Progressive Warnings**
```
1st occurrence: Warn
2nd occurrence: Strong warn
3rd occurrence: Block
```

**Pattern 2: Smart Exceptions**
```
Block secrets UNLESS:
- File is .env.example
- File is in docs/
- User confirms "I know what I'm doing"
```

**Pattern 3: Auto-Fix**
```
Find issue → Suggest fix → User approves → AI fixes
```

### Hook Best Practices

**DO:**
- Use hooks for safety (secret detection, force push prevention)
- Use hooks for consistency (code formatting, commit messages)
- Use hooks for automation (update docs, run tests)

**DON'T:**
- Make hooks too aggressive (frustration)
- Block too many things (slow development)
- Skip validation (defeats purpose)

### Debugging Hooks

Hook not working?

**Check 1: Is it enabled?**
```bash
cat .claude/hooks/my-hook.json
# Should exist and be valid JSON
```

**Check 2: Test trigger**
```bash
# Manually trigger hook
claude-code trigger-hook my-hook
```

**Check 3: Check logs**
```bash
# View hook logs
claude-code logs --hooks
```

### Community Challenge

**Create a custom hook for your workflow!**

Ideas:
- Block commits without tests
- Warn on large file additions
- Auto-format code before commit
- Check for copyright headers
- Validate game asset naming

**Share:**
- Hook name
- What it prevents/enables
- JSON configuration
- Tag #hook-master

---

## Lesson 2.4: Subagents - Your AI Specialist Team

### What Are Subagents?

Imagine having a team of expert consultants available 24/7:
- Code review specialist
- Testing expert
- DevOps engineer
- Security auditor
- Performance optimizer
- Database architect

**That's subagents.**

Each subagent is an AI specialist trained in a specific domain.

### Why Subagents Matter

Regular AI: General knowledge about everything
Subagent: Deep expertise in one area

**Example:**
```
Regular AI: "Your code looks okay."
Code Reviewer Subagent:
"Line 47: Potential memory leak - event listener not cleaned up
 Line 82: Race condition in async function
 Line 134: This pattern is O(n²), optimize to O(n log n)
 Line 201: Security issue - user input not sanitized"
```

### The Core 4 Subagents

**Subagent 1: Code Reviewer**
```
Expertise:
- Best practices
- Performance issues
- Security vulnerabilities
- Maintainability
- Code style

Usage:
"Review my player controller code"

Output:
✅ Positives:
- Clean separation of concerns
- Good variable naming
- Proper error handling

⚠️ Issues:
- Movement update should use deltaTime
- Missing input validation
- Consider caching transform component

🔧 Suggestions:
[Specific code improvements]
```

**Subagent 2: Test Writer**
```
Expertise:
- Unit testing
- Integration testing
- Edge cases
- Test coverage
- Mocking strategies

Usage:
"Generate tests for my inventory system"

Output:
Generated 27 tests covering:
- Add/remove items
- Stack limits
- Weight restrictions
- Edge cases (null, overflow)
- Integration with UI
- Performance (1000+ items)

Coverage: 94%
```

**Subagent 3: Doc Writer**
```
Expertise:
- API documentation
- User guides
- Code comments
- README files
- Tutorials

Usage:
"Document my game API"

Output:
Created:
- API Reference (45 endpoints)
- Getting Started Guide
- Integration Examples
- Troubleshooting Guide
- JSDoc comments for all functions
```

**Subagent 4: Debug Helper**
```
Expertise:
- Error analysis
- Root cause identification
- Stack trace interpretation
- Fix suggestions

Usage:
"Why is my game crashing on level 3?"

Output:
Root cause found:
- Enemy spawner creates infinite enemies
- Memory fills up
- Game crashes

Why it happens:
- Level 3 has typo: spawnDelay = 0
- Should be: spawnDelay = 1000

Fix:
[Exact code change needed]

Prevention:
[Validation to add]
```

### Specialist Subagents

**API Designer**
```
Expertise: REST APIs, GraphQL, WebSockets

Example:
"Design an API for my multiplayer game"

Output:
Endpoints:
POST   /api/games/create
GET    /api/games/:id
POST   /api/games/:id/join
POST   /api/games/:id/move
GET    /api/games/:id/state

WebSocket:
ws://api/games/:id/live

Rate Limits:
- Auth: 10 req/sec
- Game state: 60 req/sec
- Moves: 20 req/sec

[Full OpenAPI spec generated]
```

**Database Architect**
```
Expertise: Schema design, optimization, migrations

Example:
"Design database for RPG game"

Output:
Tables:
- users (id, username, created_at)
- characters (id, user_id, level, stats)
- inventory (id, character_id, items)
- quests (id, character_id, progress)

Indexes:
- users.username (unique)
- characters.user_id
- inventory.character_id

Relations:
- User has many Characters
- Character has one Inventory
- Character has many Quests

[SQL migration included]
```

**DevOps Engineer**
```
Expertise: Deployment, CI/CD, infrastructure

Example:
"Set up deployment for my game"

Output:
Created:
1. GitHub Actions workflow
2. Docker multi-stage build
3. Kubernetes manifests
4. Monitoring setup
5. Backup strategy
6. Rollback procedure

[All config files generated]
```

**Performance Optimizer**
```
Expertise: Profiling, optimization, caching

Example:
"My game runs slow on mobile"

Output:
Analyzed 15 performance metrics:

Issues found:
1. Texture atlas not used (-30 FPS)
2. Physics running 120 Hz (-15 FPS)
3. No object pooling (-20 FPS)
4. Shadows too detailed (-10 FPS)

Fixes applied:
[Code changes with before/after metrics]

Expected improvement: 45 → 110 FPS
```

**Security Auditor**
```
Expertise: Vulnerability scanning, exploit prevention

Example:
"Audit my game for security issues"

Output:
Scanned: 47 files, 12,483 lines

Critical (2):
- SQL injection in leaderboard
- XSS in chat system

High (5):
- Weak password hashing
- No rate limiting on login
- CORS misconfigured
- Secrets in frontend code
- Outdated dependencies

[Detailed fixes for each]
```

### Using Subagents

**Method 1: Direct Request**
```
"Hey [subagent name], [request]"

Examples:
"Hey code-reviewer, review my code"
"Hey test-writer, generate tests"
"Hey debug-helper, fix this error"
```

**Method 2: Slash Command**
```
/review        → Triggers code-reviewer
/test          → Triggers test-writer
/debug         → Triggers debug-helper
/security      → Triggers security-auditor
```

**Method 3: Automatic Trigger**
```
[System detects need] → [Triggers appropriate subagent]

Example:
You: "My game has a bug"
→ Debug Helper automatically activated

You: "Need to deploy"
→ DevOps Engineer automatically activated
```

### Advanced Subagents (Levels 3-5)

**Enterprise Architect**
```
Designs large-scale game systems
- Microservices architecture
- Event-driven design
- Scalability planning
- Tech stack decisions
```

**SRE Consultant**
```
Production reliability
- Monitoring setup
- Incident response
- SLA management
- Chaos engineering
```

**Security Architect**
```
Enterprise security
- Compliance frameworks
- Threat modeling
- Security policies
- Audit preparation
```

### Subagent Combos

Use multiple subagents together:

**Combo 1: Ship Production Code**
```
1. Code Reviewer: Review code
2. Test Writer: Generate tests
3. Security Auditor: Check security
4. DevOps Engineer: Deploy
```

**Combo 2: Optimize Performance**
```
1. Performance Optimizer: Profile code
2. Code Reviewer: Review optimizations
3. Test Writer: Add performance tests
4. DevOps Engineer: Deploy optimized version
```

**Combo 3: Debug Production Issue**
```
1. Debug Helper: Identify issue
2. Security Auditor: Check if security-related
3. Code Reviewer: Review fix
4. DevOps Engineer: Hot-fix deployment
```

### Creating Custom Subagents

Want your own specialist? Create one!

`.claude/subagents/game-designer.md`:
```markdown
# Game Designer Subagent

You are an expert game designer with 15 years of experience.

Expertise:
- Game mechanics design
- Balance and pacing
- Player psychology
- Progression systems
- Monetization strategies

When consulted:
1. Analyze current game design
2. Identify improvement opportunities
3. Suggest specific changes
4. Explain impact on player experience
5. Provide implementation guidance

Response format:
- Analysis
- Recommendations (prioritized)
- Expected impact
- Implementation notes
```

### Subagent Best Practices

**DO:**
- Use the right specialist for the job
- Combine subagents for complex tasks
- Trust their expertise
- Review their output

**DON'T:**
- Ask code-reviewer about DevOps (use DevOps subagent)
- Ignore security-auditor warnings
- Skip testing subagent suggestions

### Community Challenge

**Use 3 different subagents on your project!**

**Share:**
1. Which subagents you used
2. What they found/created
3. Time saved
4. Biggest surprise

**Tag:** #subagent-team

**Bonus:** Share a creative subagent combo you discovered!

---

## Lesson 2.5: MCP Servers - Connecting Everything

### What Are MCP Servers?

MCP (Model Context Protocol) servers connect your AI to external services.

Think of them as bridges between Claude Code and the tools you use:
- GitHub
- Databases
- Cloud providers
- Communication tools
- Monitoring services

### Why MCP Matters

**Without MCP:**
```
You: "Check my GitHub issues"
You: *manually opens GitHub*
You: *reads issues*
You: *copy-pastes to AI*
AI: Responds based on what you pasted
```

**With MCP:**
```
You: "Check my GitHub issues"
AI: *connects to GitHub via MCP*
AI: "You have 5 open issues:
     - Bug: Player falls through floor
     - Feature: Add multiplayer
     - Enhancement: Better UI
     [Detailed analysis and suggestions]"
```

### Essential MCP Integrations

**MCP 1: GitHub**
```
Connects to: GitHub repositories, issues, PRs

Enables:
- Create issues from bugs
- Auto-create PRs
- Sync documentation
- Track project progress
- Manage releases

Example:
You: "Create an issue for that bug"
AI: ✅ Created issue #47
    Title: "Player falls through floor on level 3"
    Labels: bug, high-priority
    Assigned to: you
    Link: github.com/user/game/issues/47
```

**MCP 2: PostgreSQL**
```
Connects to: PostgreSQL databases

Enables:
- Query data
- Design schemas
- Optimize queries
- Create migrations
- Backup/restore

Example:
You: "Show me top 10 players by score"
AI: [Executes query, shows results]

    Top Players:
    1. PlayerOne - 15,420 points
    2. GameMaster - 12,390 points
    [...]

    Performance: 0.04ms
    Suggestion: Add index on score column
```

**MCP 3: Docker**
```
Connects to: Docker daemon

Enables:
- Build images
- Run containers
- Manage networks
- View logs
- Deploy services

Example:
You: "Deploy my game in Docker"
AI: Building Docker image...
    ✅ Built: my-game:latest (247 MB)

    Running container...
    ✅ Container started: my-game-prod

    Accessible at: http://localhost:8080
    Logs: docker logs my-game-prod
```

**MCP 4: AWS**
```
Connects to: Amazon Web Services

Enables:
- Deploy to S3
- Manage EC2 instances
- Configure CloudFront
- Monitor costs
- Set up auto-scaling

Example:
You: "Deploy game to AWS"
AI: Created S3 bucket: my-game-assets
    Uploaded 247 files
    Configured CloudFront CDN

    Game URL: https://d1234.cloudfront.net
    Estimated cost: $5/month
```

**MCP 5: Sentry**
```
Connects to: Sentry error tracking

Enables:
- Monitor errors
- Analyze crashes
- Track performance
- Alert on issues

Example:
You: "Any errors in production?"
AI: Found 3 new errors (last 24h):

    1. TypeError at player.js:47
       Affected: 12 users
       First seen: 2h ago

    2. NetworkError at api.js:89
       Affected: 3 users
       First seen: 45m ago

    [Suggested fixes for each]
```

### Setting Up MCP Servers

**Step 1: Install MCP Server**
```bash
npm install @anthropic-ai/mcp-server-github
```

**Step 2: Configure Connection**

`.claude/mcp.json`:
```json
{
  "github": {
    "server": "@anthropic-ai/mcp-server-github",
    "config": {
      "token": "${GITHUB_TOKEN}",
      "owner": "your-username",
      "repo": "your-game"
    }
  }
}
```

**Step 3: Set Environment Variables**

`.env`:
```bash
GITHUB_TOKEN=ghp_your_token_here
```

**Step 4: Use It!**
```
You: "What are my open GitHub issues?"
AI: [Fetches via MCP and responds]
```

### Available MCP Servers

**Source Control:**
- GitHub - Issues, PRs, repos
- GitLab - Similar to GitHub
- Bitbucket - Code hosting

**Databases:**
- PostgreSQL - Relational DB
- MongoDB - Document DB
- MySQL - Relational DB
- SQLite - Embedded DB
- Redis - Cache/store

**Cloud Providers:**
- AWS - S3, EC2, Lambda, etc.
- Google Cloud - GCS, Compute, etc.
- Azure - Blob, VMs, etc.

**Communication:**
- Slack - Team chat
- Discord - Community chat
- Email - Notifications

**Monitoring:**
- Sentry - Error tracking
- Datadog - Metrics/logs
- New Relic - APM
- LogRocket - Session replay

**DevOps:**
- Docker - Containers
- Kubernetes - Orchestration
- Terraform - Infrastructure

### MCP Integration Examples

**Example 1: Complete Deployment Workflow**
```
You: "Deploy to production"

AI (uses multiple MCP servers):
1. GitHub MCP: Pull latest code
2. Docker MCP: Build image
3. AWS MCP: Push to ECR
4. Kubernetes MCP: Deploy to cluster
5. Slack MCP: Notify team
6. Sentry MCP: Enable monitoring

Result: Deployed in 2 minutes (vs 30 manual)
```

**Example 2: Player Analytics**
```
You: "Show player retention stats"

AI (uses MCP):
1. PostgreSQL MCP: Query player data
2. Generates analysis
3. Creates visualizations
4. Identifies trends
5. Suggests improvements

Result: Complete analytics report instantly
```

**Example 3: Incident Response**
```
Sentry MCP: ⚠️ New critical error!

AI (automatic response):
1. Fetches error details (Sentry MCP)
2. Checks related code (GitHub MCP)
3. Identifies root cause
4. Creates fix
5. Deploys hotfix (Docker + AWS MCP)
6. Notifies team (Slack MCP)

Result: Issue resolved in 5 minutes
```

### Creating Custom MCP Servers

Want to connect to your own service?

**Example: Game Analytics MCP**

`my-analytics-server.js`:
```javascript
import { MCPServer } from '@anthropic-ai/mcp';

const server = new MCPServer({
  name: 'game-analytics',
  version: '1.0.0',

  tools: {
    getPlayerStats: async ({ playerId }) => {
      // Fetch from your analytics API
      const stats = await fetch(`/api/stats/${playerId}`);
      return stats.json();
    },

    getRetention: async ({ period }) => {
      // Calculate retention
      const data = await fetch(`/api/retention?period=${period}`);
      return data.json();
    }
  }
});

server.listen();
```

Configuration:
```json
{
  "game-analytics": {
    "server": "./my-analytics-server.js",
    "config": {
      "apiKey": "${ANALYTICS_API_KEY}"
    }
  }
}
```

### MCP Security Best Practices

**DO:**
- Store credentials in .env
- Use read-only tokens when possible
- Limit scope of access
- Rotate keys regularly
- Monitor usage

**DON'T:**
- Commit API keys to git
- Use admin tokens for simple tasks
- Share MCP configurations
- Skip authentication

### Troubleshooting MCP

**Issue: "MCP server not found"**
```bash
# Check installation
npm list @anthropic-ai/mcp-server-github

# Reinstall if needed
npm install @anthropic-ai/mcp-server-github
```

**Issue: "Authentication failed"**
```bash
# Check .env file
cat .env | grep GITHUB_TOKEN

# Verify token works
curl -H "Authorization: token $GITHUB_TOKEN" \
     https://api.github.com/user
```

**Issue: "Connection timeout"**
```json
// Increase timeout in mcp.json
{
  "github": {
    "timeout": 30000  // 30 seconds
  }
}
```

### Community Challenge

**Connect at least 1 MCP server to your project!**

**Options:**
- GitHub (easiest)
- Database
- Docker
- Cloud provider
- Custom server (advanced)

**Share:**
- Which MCP you connected
- What you used it for
- Coolest automation you created
- Tag #mcp-connected

**Bonus:** Create a custom MCP server and share the code!

---

## Module 2 Complete: The 5 Pillars Mastered!

**🎉 Congratulations! You now understand the complete AI development architecture!**

**What you've learned:**

✅ **Skills** - Automatic code generation that triggers when you need it
✅ **Slash Commands** - One-command workflows for complex tasks
✅ **Hooks** - Event-driven automation and safety nets
✅ **Subagents** - Specialist AI consultants for every domain
✅ **MCP Servers** - Connect AI to all your tools and services

**The Power Combo:**

These 5 pillars work together:

1. **Skill** automatically detects you need tests
2. **Subagent** (Test Writer) generates comprehensive test suite
3. **Hook** runs tests before commit
4. **MCP** pushes to GitHub if tests pass
5. **Slash command** (`/deploy`) handles everything

**Result:** Production deployment in 30 seconds

**What's Next?**

Module 3: Building Your First Complete Game with AI
- Put all 5 pillars into action
- Build a full 2D platformer
- From idea to deployed game
- In under 2 hours

**Community Challenge:**

**Complete the 5 Pillars Challenge:**
1. Use at least 1 skill
2. Try 3 slash commands
3. Set up 1 hook
4. Consult 2 subagents
5. Connect 1 MCP server

**Share:**
- Screenshots of each
- What you built
- Biggest time-saver
- Tag #5pillars-master

**You're now equipped with the complete AI development framework. Let's build something amazing! 🚀**
