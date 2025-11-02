# AI Game Development Cheat Sheet

**Your quick reference for building games 10x faster with AI**

---

## The 5 Pillars (Quick Reference)

### 1. Skills (Automatic)

**What:** AI capabilities that trigger automatically
**When:** Based on context (new project, writing code, etc.)

```
✓ README Generator → Missing documentation
✓ Bug Finder → Errors detected
✓ Test Helper → New code without tests
✓ Code Explainer → Reading complex code
✓ Git Helper → Version control operations
```

**Install:** `cp -r starter-kit/.claude/skills ./`

### 2. Slash Commands (Manual)

**What:** One-command workflows
**When:** You explicitly call them

```
/commit          → Smart git commit
/test            → Generate & run tests
/debug           → Fix bugs
/refactor        → Improve code
/deploy          → Ship to production
/docs            → Generate documentation
/review          → Code review
/setup           → Project setup
```

**Install:** `cp -r starter-kit/.claude/commands ./`

### 3. Hooks (Event-Driven)

**What:** Automatic actions on events
**When:** Before/after specific actions

```
PreCommit:  Secret detection, force push prevention
PostTest:   Test failure alerts
PostBuild:  Size monitoring
```

**Install:** `cp -r starter-kit/.claude/hooks ./`

### 4. Subagents (Specialists)

**What:** Expert AI consultants
**When:** Need domain expertise

```
code-reviewer        → Code quality
test-writer          → Test generation
debug-helper         → Bug fixing
api-designer         → API design
database-architect   → DB schema
devops-engineer      → Deployment
performance-optimizer → Speed
security-auditor     → Security
```

**Usage:** `"Hey [agent name], [request]"`

### 5. MCP Servers (Integrations)

**What:** Connect to external services
**When:** Need to access tools/data

```
GitHub     → Issues, PRs, repos
PostgreSQL → Database queries
Docker     → Container management
AWS        → Cloud deployment
Sentry     → Error tracking
```

**Setup:** Configure in `.claude/mcp.json`

---

## Common Prompts for Game Development

### Creating Game Systems

**Player Controller:**
```
Create a 2D player controller with:
- WASD movement
- Space to jump (with double jump)
- Shift to sprint
- Smooth acceleration/deceleration
- Ground detection
- Animation states
```

**Enemy AI:**
```
Create enemy AI with:
- Patrol between waypoints
- Attack when player in range
- Take damage and knockback
- Death animation and loot drop
- Configurable stats (HP, damage, speed)
```

**Inventory System:**
```
Create inventory system with:
- Grid-based (10x5 slots)
- Item stacking (max 99)
- Drag and drop UI
- Weight limit system
- Save/load to localStorage
- Item tooltips
```

**Quest System:**
```
Create quest system with:
- Multiple quest types (kill, collect, explore)
- Multi-stage quests
- Branching dialogue
- Rewards (XP, items, gold)
- Quest log UI
- Save/load progress
```

### Game Genres

**2D Platformer:**
```
Create a 2D platformer with Mario-style movement,
enemies, collectibles, and 5 levels with increasing difficulty
```

**Top-Down Shooter:**
```
Create a top-down shooter with WASD movement,
mouse aim/shoot, waves of enemies, and upgrades
```

**RPG:**
```
Create a turn-based RPG with party system,
enemy encounters, skills, items, and equipment
```

**Puzzle Game:**
```
Create a match-3 puzzle game with swap mechanics,
combos, power-ups, and timed/endless modes
```

**Card Game:**
```
Create a card game with deck building, mana system,
card effects, and AI opponent
```

### 3D Development

**3D Scene:**
```
Create a Three.js scene with:
- Third-person camera
- Character controller
- Environment (terrain, sky, water)
- Lighting (sun, shadows, ambient)
- Physics (Cannon.js)
- Post-processing effects
```

**Shader Effects:**
```
Create a [type] shader with:
- [Effect 1]
- [Effect 2]
- [Effect 3]
- Animated using [method]
```

Examples:
- Water shader (waves, reflections, foam)
- Fire shader (flames, heat distortion, embers)
- Hologram shader (scanlines, glitch, transparency)

---

## Optimization Quick Tips

### Performance

```
/performance-profile
→ Identifies bottlenecks
→ Shows optimization suggestions
```

**Common fixes:**
- Use object pooling for frequently created/destroyed objects
- Implement sprite atlases
- Reduce draw calls
- Use requestAnimationFrame
- Debounce expensive operations
- Cache calculations

### Bundle Size

```
/bundle-analyze
→ Shows what's taking up space
```

**Common fixes:**
- Tree-shaking unused code
- Code splitting
- Lazy loading
- Compress images
- Use CDN for libraries

### Mobile Performance

```
Ask: "Optimize for mobile devices"
```

**AI applies:**
- Reduced particle counts
- Simplified shaders
- Touch controls
- Responsive layout
- Battery-efficient code

---

## Testing Patterns

### Unit Tests

```
/test
→ Generates comprehensive unit tests
```

**Example request:**
```
"Generate tests for my player controller including:
- Movement in all directions
- Jump mechanics
- Edge cases (boundaries, no input)
- Performance benchmarks"
```

### Integration Tests

```
"Create integration tests for:
- Player attacking enemies
- Collecting items
- Level transitions
- Save/load functionality"
```

### Edge Cases

```
"Add edge case tests for:
- Null/undefined inputs
- Extremely large numbers
- Negative values
- Concurrent operations"
```

---

## Deployment Checklist

### Pre-Deploy

```
[ ] Run /test (all tests pass)
[ ] Run /security-audit
[ ] Run /performance-profile
[ ] Optimize images
[ ] Remove console.logs
[ ] Update version number
[ ] Test in production mode
[ ] Check cross-browser compatibility
```

### Deploy

```
/deploy [environment]

Options:
- /deploy staging
- /deploy production
- /deploy --dry-run (preview)
```

### Post-Deploy

```
[ ] Health check endpoint responding
[ ] Error tracking configured (Sentry)
[ ] Analytics tracking
[ ] Performance monitoring
[ ] Backup database
[ ] Update documentation
[ ] Notify team/users
```

---

## Debugging Workflow

### Step 1: Identify Error

```
Copy the full error message
Include stack trace if available
```

### Step 2: Debug Command

```
/debug [error message]

Or:

"This error is occurring: [paste error]
It happens when: [describe scenario]"
```

### Step 3: Apply Fix

```
AI provides:
1. Root cause explanation
2. Suggested fix
3. Prevention for future

Confirm to apply
```

### Step 4: Verify

```
/test
→ Ensures fix works and doesn't break anything
```

---

## Git Workflow with AI

### Smart Commits

```
/commit

AI automatically:
1. Analyzes changes
2. Runs linter
3. Runs tests
4. Generates descriptive commit message
5. Creates commit
6. (Optional) Pushes to remote
```

### Branch Management

```
"Create a feature branch for [feature name]"
"Merge [branch] into main with proper PR"
"Resolve merge conflicts in [file]"
```

### PR Creation

```
"Create a pull request with:
- Summary of changes
- Test plan
- Screenshots
- Breaking changes noted"
```

---

## Framework-Specific Prompts

### React

```
"Create a React component for [feature] with:
- TypeScript
- Hooks (useState, useEffect)
- Props interface
- CSS modules
- Unit tests"
```

### Vue

```
"Create a Vue 3 component for [feature] with:
- Composition API
- TypeScript
- Scoped styles
- Emits and props
- Tests"
```

### Three.js

```
"Create a Three.js [object] with:
- Custom geometry/imported model
- Material with [properties]
- Lighting
- Animation
- Physics
- Performance optimized"
```

### Phaser

```
"Create a Phaser scene for [level/feature] with:
- Tilemap
- Player sprite
- Enemies
- Collectibles
- Physics
- UI overlay"
```

---

## Monetization Integration

### Ads

```
"Integrate AdSense/AdMob with:
- Banner ads
- Interstitial ads (between levels)
- Rewarded ads (for bonuses)
- Non-intrusive placement
- GDPR compliance"
```

### In-App Purchases

```
"Add IAP system with:
- Product catalog
- Purchase flow
- Receipt validation
- Restore purchases
- Currency system (coins/gems)"
```

### Patreon/Subscriptions

```
"Integrate Patreon with:
- OAuth login
- Tier checking
- Exclusive content unlocking
- Thank you message for supporters"
```

---

## Security Best Practices

### Input Validation

```
"Add input validation for:
- Username (alphanumeric, 3-20 chars)
- Email (proper format)
- Score (prevent manipulation)
- API requests (rate limiting)"
```

### Data Protection

```
"Implement:
- Password hashing (bcrypt)
- HTTPS enforcement
- CORS configuration
- XSS prevention
- SQL injection prevention
- API key protection"
```

### Audit

```
/security-audit

Reviews:
- Dependencies for vulnerabilities
- Code for security issues
- API endpoints
- Data handling
- Authentication
```

---

## AI Development Best Practices

### DO:

✅ Be specific in requests
✅ Iterate and refine
✅ Test AI-generated code
✅ Understand what code does
✅ Use version control
✅ Ask for explanations
✅ Combine multiple pillars
✅ Share learnings with community

### DON'T:

❌ Accept first result without testing
❌ Use code you don't understand
❌ Skip security checks
❌ Ignore performance issues
❌ Forget to commit regularly
❌ Over-complicate requests
❌ Skip documentation
❌ Work without backups

---

## Time-Saving Combos

### Full Feature Development

```
1. Describe feature
2. AI generates code
3. /test
4. /refactor (if needed)
5. /commit
6. /deploy

Time: 15-30 minutes
Traditional: 2-8 hours
```

### Bug Fix Sprint

```
1. /debug [error]
2. /test to verify fix
3. /commit with fix
4. /deploy hotfix

Time: 5-10 minutes
Traditional: 30-120 minutes
```

### Performance Optimization

```
1. /performance-profile
2. AI suggests optimizations
3. Apply changes
4. /test performance benchmarks
5. /commit improvements

Time: 20-40 minutes
Traditional: 4-8 hours
```

---

## Emergency Commands

### Production is Down

```
1. /rollback-emergency
2. /incident-declare
3. Check error tracking (Sentry MCP)
4. /debug [critical error]
5. /deploy hotfix
6. /postmortem-generate
```

### Major Bug Found

```
1. /debug [bug description]
2. /test to verify fix
3. /security-audit (if security-related)
4. /deploy --fast
5. Notify users
```

### Performance Crisis

```
1. /performance-profile
2. Apply critical optimizations
3. /test performance
4. /deploy optimized version
5. Monitor metrics
```

---

## Community Resources

### Get Help

**In Skool Community:**
- Tag: #help-needed
- Describe issue clearly
- Include error messages
- Share relevant code (use code blocks)

**Common Tags:**
- #bug-help
- #feature-help
- #optimization-help
- #deployment-help

### Share Your Work

**When Posting:**
- Live demo link
- Screenshots/GIF
- Brief description
- Unique features
- What you learned

**Tags:**
- #showcase
- #game-complete
- #ai-powered
- [Genre tag]

### Level Up

**Beginner → Intermediate:**
- Complete Modules 1-4
- Build 3+ games
- Help 5+ community members
- Share your projects

**Intermediate → Advanced:**
- Complete Modules 5-9
- Master performance optimization
- Implement complex systems
- Contribute custom skills/commands

**Advanced → Master:**
- Complete Modules 10-15
- Build enterprise-scale games
- Create tutorials for others
- Become community mentor

---

## Quick Reference Cards

### Game Feature Time Estimates

| Feature | Traditional | AI-Assisted | Savings |
|---------|-------------|-------------|---------|
| Player Controller | 4-8h | 10-20m | 95% |
| Inventory System | 16-24h | 30-60m | 96% |
| Quest System | 24-40h | 1-2h | 95% |
| Dialogue System | 12-20h | 30-60m | 95% |
| Save/Load | 8-12h | 20-30m | 96% |
| UI System | 12-16h | 1-2h | 92% |
| Enemy AI | 6-10h | 15-30m | 95% |
| Boss Battle | 12-16h | 1-2h | 92% |
| Multiplayer | 40-80h | 4-8h | 90% |
| Full Game | 200-400h | 20-40h | 90-95% |

### Command Shortcuts

| Need | Command | Time |
|------|---------|------|
| Commit code | `/commit` | 30s |
| Fix bug | `/debug` | 2-5m |
| Add tests | `/test` | 1-2m |
| Deploy | `/deploy` | 2-5m |
| Optimize | `/performance-profile` | 5m |
| Review | `/review` | 2m |
| Refactor | `/refactor` | 3-10m |

---

**Save this cheat sheet! Reference it daily! 🚀**

**Questions? Post in community with #cheat-sheet**
