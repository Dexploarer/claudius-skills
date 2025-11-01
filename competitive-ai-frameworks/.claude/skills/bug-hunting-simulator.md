---
name: bug-hunting-simulator
description: Orchestrate competitive bug hunting where three specialized AI teams compete to find security vulnerabilities. Activates when user wants to find vulnerabilities, run security audits, bug hunts, penetration tests (authorized only), or mentions competitive security testing.
allowed-tools: [Read, Grep, Glob, Bash, Task]
---

# Bug Hunting Championship Simulator

Orchestrates a competitive multi-agent simulation where three specialized AI teams compete to find vulnerabilities in your codebase using different strategies and reinforcement learning to continuously improve.

## When to Use

This skill should be used when:
- User wants to find security vulnerabilities comprehensively
- User requests a security audit or penetration test (authorized only)
- User needs to compare different vulnerability detection approaches
- User mentions bug hunting, security testing, or competitive security analysis
- User wants to leverage multiple AI strategies for better vulnerability coverage

## Instructions

### Step 1: Confirm Authorization

**Before starting any security testing, you MUST confirm:**

```markdown
⚠️  Security Testing Authorization Required

Please confirm:
1. Do you have authorization to test this codebase?
2. Is this for defensive security or educational purposes?
3. Is this your own code or an authorized test environment?

Type 'yes' to proceed or 'no' to cancel.
```

Only proceed if user explicitly confirms authorization.

### Step 2: Gather Configuration

Ask the user for:
- **Target path:** Directory or codebase to analyze (required)
- **Rounds:** Number of competition rounds (default: 5)
- **Focus areas:** Specific vulnerability types to prioritize (optional)
- **Output:** Where to save results (default: ./results)
- **Visualization:** Whether to generate charts and graphs (optional)

Example:
```bash
Target: ./src
Rounds: 5
Focus: authentication, sql-injection
Output: ./security-audit-results
Visualize: yes
```

### Step 3: Initialize Championship

Set up the competitive framework:

1. Load three competing teams:
   - **Team 1:** Automated Scanners (pattern matching, static analysis)
   - **Team 2:** Manual Reviewers (logic flaws, business logic)
   - **Team 3:** Fuzzers (runtime bugs, race conditions)

2. Configure the scoring engine (CVSS-based)

3. Initialize reinforcement learning weights

Example command:
```bash
cd competitive-ai-frameworks/frameworks/bug-hunting
python coordinator.py \
  --target /path/to/codebase \
  --rounds 5 \
  --output ./results \
  --visualize
```

### Step 4: Run Competition Rounds

For each round (typically 5 rounds):

1. **Team 1 hunts** using automated pattern matching
2. **Team 2 hunts** using deep code review
3. **Team 3 hunts** using fuzzing and behavioral analysis
4. **Score bugs** based on:
   - Severity (CVSS score)
   - Uniqueness (first to find bonus)
   - Quality (report completeness)
   - Speed (time to discover)
5. **Update weights** via reinforcement learning
6. **Display progress** to user

### Step 5: Analyze and Present Results

Generate comprehensive report showing:
- 🥇 Winner and final standings
- 📊 Score breakdown by team
- 🔴 Top critical vulnerabilities discovered
- 📈 Strategy analysis (what worked best)
- 💡 Combined recommendations (best of all approaches)

## Best Practices

- ✅ Always confirm authorization before starting security testing
- ✅ Run at least 3-5 rounds to allow reinforcement learning to improve strategies
- ✅ Combine findings from all three teams for comprehensive coverage
- ✅ Verify critical vulnerabilities manually before reporting to stakeholders
- ✅ Use the winning team's strategy as primary approach in future audits
- ✅ Save and review the JSON results for detailed analysis
- ✅ Re-run the championship after fixes to verify remediation
- ✅ Focus on unique discoveries - they often represent the most critical issues

## Examples

### Example 1: Basic Security Audit

**User Input:**
```
I need to find security vulnerabilities in my web application
```

**Skill Process:**
1. Confirm authorization with user
2. Detect current working directory as target: `./src`
3. Use default configuration (5 rounds, all 3 teams)
4. Run championship with real-time progress updates
5. Present final results with winner, top vulnerabilities, and recommendations

**Output:**
```markdown
🎯 Bug Hunting Championship Results

🥇 Winner: Team 2 - Manual Reviewers (1,450 points)
   - 12 bugs found (2 Critical, 5 High, 5 Medium)
   - 5% false positive rate

Top Vulnerabilities:
1. 🔴 CRITICAL - Authentication Bypass (CVSS 9.8)
   Location: src/auth/middleware.py:78
   Impact: Complete authentication bypass via JWT 'none' algorithm

2. 🟠 HIGH - SQL Injection (CVSS 8.5)
   Location: src/db/queries.py:45
   Impact: Data exfiltration possible

Recommendation: Start with automated scanning, follow with manual review
of authentication/authorization, then apply fuzzing to critical operations.
```

**Explanation:** The championship found critical auth and injection flaws by combining all three team strategies, with Manual Reviewers excelling at finding the most impactful business logic vulnerability.

### Example 2: Focused Security Testing

**User Input:**
```
Run bug hunt on ./api focusing on authentication bugs
```

**Skill Process:**
1. Confirm authorization
2. Target: `./api` directory
3. Focus: authentication vulnerabilities
4. Team 2 (Manual Reviewers) weight increased for auth focus
5. Results emphasize auth-related findings

**Output:**
Focused results showing 8 authentication-related vulnerabilities including IDOR, session fixation, and privilege escalation issues.

## Common Mistakes to Avoid

- ❌ Running bug hunts without proper authorization
- ❌ Testing production systems without approval
- ❌ Ignoring false positives (they'll reduce team effectiveness via RL)
- ❌ Using only one round (prevents reinforcement learning from improving strategies)
- ❌ Not verifying critical findings manually before reporting
- ❌ Skipping the combined approach recommendations
- ✅ Always get authorization, run multiple rounds, verify findings, and use insights from all teams

## Tips

- 💡 **First time users:** Start with 3 rounds on a small codebase to understand the process
- 💡 **Performance:** Increase Team 1 weight for faster scans, Team 2 for deeper analysis
- 💡 **Learning:** Watch how team weights evolve - successful strategies get reinforced
- 💡 **Best results:** 5-7 rounds provides optimal balance of coverage and RL improvement
- 💡 **Prioritization:** Critical CVSS scores (9.0+) should be fixed immediately
- 💡 **Validation:** Use the test application in `examples/bug-hunting/vulnerable-app/` to practice

## Related Skills/Commands

- `/run-bug-hunt` - Quick start bug hunting championship
- `/run-quality-check` - Code quality championship
- `security-auditor` subagent - Security audit specialist
- `code-reviewer` skill - General code review

## Notes

**Scoring System:**
- Critical (CVSS 9.0-10.0): 100 points base
- High (CVSS 7.0-8.9): 50 points
- Medium (CVSS 4.0-6.9): 25 points
- Low (CVSS 0.1-3.9): 10 points
- First discovery bonus: +50%
- Quality report bonus: +0 to +20 points
- False positive penalty: -20 points

**Team Specialties:**
- Team 1 (Automated): Fast pattern matching, good for known vulns (SQL injection, XSS)
- Team 2 (Manual): Best for logic flaws, auth bypasses, business logic
- Team 3 (Fuzzers): Excels at race conditions, memory bugs, runtime issues

**Reinforcement Learning:**
The framework uses Q-learning to adapt team strategies. Successful approaches are reinforced, unsuccessful ones are de-emphasized. This means later rounds are typically more effective than early rounds.

**Integration:**
Uses subagents in `.claude/subagents/team[1-3]-*.md` and Python framework in `frameworks/bug-hunting/`.
