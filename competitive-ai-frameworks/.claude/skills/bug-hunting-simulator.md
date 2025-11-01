# Bug Hunting Championship Simulator

## Skill Activation

This skill automatically activates when the user mentions:
- "find security vulnerabilities"
- "hunt for bugs"
- "security audit"
- "penetration test" (authorized only)
- "run bug hunt"
- "competitive bug hunting"

## Skill Description

Orchestrates a competitive bug hunting simulation where three specialized AI teams compete to find vulnerabilities in a target codebase using reinforcement learning to adapt their strategies.

## When to Use

Activate this skill when:
- User wants to find security vulnerabilities comprehensively
- User requests a security audit or assessment
- User wants to compare different vulnerability detection approaches
- User mentions bug hunting or security testing

## How It Works

1. **Initialize Championship**
   - Set up three competing teams (Automated, Manual, Fuzzing)
   - Configure target codebase
   - Initialize scoring engine

2. **Run Rounds**
   - Each team searches for vulnerabilities independently
   - Teams use their specialized strategies
   - Bugs are scored based on severity, uniqueness, quality

3. **Apply Reinforcement Learning**
   - Successful strategies are strengthened
   - False positives are penalized
   - Weights adapt based on performance

4. **Declare Winner**
   - Aggregate scores across rounds
   - Identify best overall team
   - Extract winning strategies
   - Generate recommendations

## Execution Steps

When activated:

1. **Confirm Authorization**
   ```
   Before starting, confirm:
   - User has authorization to test this codebase
   - This is for defensive security/education
   - Target is user's own code or authorized test environment
   ```

2. **Get Configuration**
   ```
   Ask user:
   - Target directory/codebase path
   - Number of rounds (default: 5)
   - Specific focus areas (optional)
   - Visualization preference
   ```

3. **Launch Championship**
   ```python
   cd competitive-ai-frameworks/frameworks/bug-hunting
   python coordinator.py \
     --target /path/to/codebase \
     --rounds 5 \
     --output ./results \
     --visualize
   ```

4. **Monitor Progress**
   ```
   Display real-time updates:
   - Round number and progress
   - Bugs found per team
   - Current scores
   - Time remaining
   ```

5. **Present Results**
   ```
   Show final results:
   - Winner announcement
   - Score breakdown
   - Top vulnerabilities found
   - Strategy analysis
   - Combined recommendations
   ```

## Team Strategies

### Team 1: Automated Scanners
- **Strength:** Speed and coverage
- **Focus:** Pattern matching, known vulnerabilities
- **Tools:** grep, static analysis, dependency scanning
- **Best at:** SQL injection, XSS, command injection

### Team 2: Manual Reviewers
- **Strength:** Critical logic flaws
- **Focus:** Business logic, auth/authz
- **Tools:** Deep code review, flow analysis
- **Best at:** Auth bypasses, IDOR, privilege escalation

### Team 3: Fuzzers
- **Strength:** Runtime bugs and edge cases
- **Focus:** Race conditions, memory issues
- **Tools:** Fuzzing, concurrency testing
- **Best at:** Race conditions, buffer overflows, DoS

## Scoring System

**Base Scores:**
- Critical (CVSS 9.0-10.0): 100 points
- High (CVSS 7.0-8.9): 50 points
- Medium (CVSS 4.0-6.9): 25 points
- Low (CVSS 0.1-3.9): 10 points

**Bonuses:**
- First discovery: +50%
- Quality report: +0 to +20 points
- Fast discovery: +0 to +30%

**Penalties:**
- False positive: -20 points

## Output Format

Present results as:

```markdown
# Bug Hunting Championship Results

## Final Standings

🥇 **Winner: [Team Name]**
   - Total Score: [score]
   - Bugs Found: [count]
   - Critical Bugs: [count]
   - False Positive Rate: [percentage]

🥈 **Second Place: [Team Name]**
   ...

🥉 **Third Place: [Team Name]**
   ...

## Top Vulnerabilities Discovered

1. **[Vulnerability Type]** (CVSS [score])
   - Location: [file:line]
   - Discovered by: [Team]
   - Impact: [description]

2. ...

## Winning Strategy Analysis

[Team Name] won by:
- [Key success factor 1]
- [Key success factor 2]
- [Key success factor 3]

## Recommended Combined Approach

Based on all teams' performance:

1. [Best practice from analysis]
2. [Best practice from analysis]
3. [Best practice from analysis]
```

## Example Usage

**User:** "I need to find security vulnerabilities in my application"

**Assistant:**
```
I'll run a competitive bug hunting championship with three specialized teams!

🎯 Bug Hunting Championship Initialized

Configuration:
- Target: ./src
- Rounds: 5
- Teams: 3 (Automated, Manual Review, Fuzzing)

Starting Round 1/5...

[Shows progress and results]
```

## Integration with Claude Code

This skill uses:

**Subagents:**
- `.claude/subagents/team1-automated-scanner.md` - Team 1 strategy
- `.claude/subagents/team2-manual-reviewer.md` - Team 2 strategy
- `.claude/subagents/team3-fuzzer.md` - Team 3 strategy

**Tools:**
- `Grep` - Pattern matching for Team 1
- `Read` - Code analysis for Team 2
- `Bash` - Running tests for Team 3

**Frameworks:**
- `frameworks/bug-hunting/coordinator.py` - Main orchestrator
- `frameworks/bug-hunting/scoring_engine.py` - Scoring logic
- `frameworks/bug-hunting/reinforcement.py` - Strategy adaptation

## Safety and Ethics

**Always:**
- ✅ Confirm user has authorization
- ✅ Verify defensive/educational purpose
- ✅ Target only user's own code or authorized systems
- ✅ Follow responsible disclosure for findings

**Never:**
- ❌ Test unauthorized systems
- ❌ Provide exploitation assistance for malicious purposes
- ❌ Bypass security controls without authorization
- ❌ Assist with attacks on production systems

## Advanced Features

**Multi-Round Evolution:**
- Watch strategies improve over rounds
- See reinforcement learning in action
- Track weight adaptations

**Custom Configuration:**
- Adjust team weights
- Focus on specific vulnerability types
- Set custom scoring rules

**Detailed Reporting:**
- Export results to JSON
- Generate visualizations
- Create executive summaries

## Troubleshooting

**Issue:** Teams finding too many false positives
**Solution:** Increase validation strictness, penalize false positives more

**Issue:** Not enough critical bugs found
**Solution:** Increase Team 2 (Manual Review) weight, add more rounds

**Issue:** Simulation too slow
**Solution:** Reduce rounds, increase Team 1 (Automated) weight

## Related Commands

- `/run-bug-hunt` - Quick start bug hunting
- `/security-audit` - Focused security audit
- `/vulnerability-scan` - Fast automated scan only

## Success Criteria

Skill succeeds when:
- All rounds complete successfully
- Results are clearly presented
- Winner is determined
- Recommendations are actionable
- User understands findings
