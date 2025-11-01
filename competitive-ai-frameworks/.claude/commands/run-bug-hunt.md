Run competitive bug hunting championship with three specialized AI teams competing to find security vulnerabilities.

## Instructions

1. **Confirm Authorization**
   - Verify user has permission to test this codebase
   - Ensure this is for defensive security/education only
   - Confirm target is user's code or authorized test environment

2. **Parse Arguments**
   - `$1` or `--target`: Target directory path (required)
   - `$2` or `--rounds`: Number of rounds (default: 5)
   - `--output`: Output directory for results (default: ./results)
   - `--visualize`: Generate charts and visualizations
   - `--team`: Run specific team only (automated/manual/fuzzing)

3. **Execute Championship**
   ```bash
   cd competitive-ai-frameworks/frameworks/bug-hunting
   python coordinator.py \
     --target $TARGET \
     --rounds $ROUNDS \
     --output $OUTPUT \
     ${VISUALIZE:+--visualize}
   ```

4. **Display Progress**
   - Show each round as it runs
   - Display bugs found per team
   - Show current scores

5. **Present Results**
   - Winner announcement with final scores
   - Top vulnerabilities discovered (with CVSS scores)
   - Strategy analysis (what worked best)
   - Combined recommendations

## Example Usage

```bash
# Basic usage (current directory, 5 rounds)
/run-bug-hunt

# Specify target and rounds
/run-bug-hunt ./src 5

# With visualization
/run-bug-hunt --target ./api --rounds 7 --visualize

# Single team only
/run-bug-hunt --target ./backend --team manual
```

## What This Does

1. Confirms security testing authorization with user
2. Initializes three competing AI teams (Automated, Manual Review, Fuzzing)
3. Runs championship for specified number of rounds
4. Teams hunt for bugs using different strategies
5. Applies reinforcement learning to improve strategies each round
6. Scores bugs based on CVSS severity and uniqueness
7. Presents comprehensive results with winner and recommendations

## Options

- **No arguments:** Uses current directory, 5 rounds, all teams
- **--target <path>:** Specific codebase to scan
- **--rounds <n>:** Number of competition rounds (more = better RL adaptation)
- **--visualize:** Create charts showing team performance over rounds
- **--team <name>:** Run only one team (faster, less comprehensive)
- **--output <path>:** Custom output directory

## Output Format

```markdown
╔══════════════════════════════════════╗
║   BUG HUNTING CHAMPIONSHIP          ║
╚══════════════════════════════════════╝

🥇 Winner: Team 2 - Manual Reviewers (1,450 pts)
   - 12 bugs found (2 Critical, 5 High, 5 Medium)
   - 5% false positive rate

Top Vulnerabilities:
1. 🔴 CRITICAL - Auth Bypass (CVSS 9.8)
   Location: src/auth/middleware.py:78

2. 🟠 HIGH - SQL Injection (CVSS 8.5)
   Location: src/db/queries.py:45

Recommendation: Use automated scanning for coverage,
manual review for critical bugs, fuzzing for edge cases.

Results: ./results/championship_*.json
```

## Notes

- **Safety:** Always confirm authorization before scanning
- **Scoring:** Critical=100pts, High=50pts, Medium=25pts, Low=10pts
- **RL Benefits:** More rounds = better strategy adaptation
- **Teams:** Automated (fast), Manual (critical bugs), Fuzzing (race conditions)
- **Output:** Creates JSON files in output directory with full details
- **Follow-up:** Review findings, prioritize by CVSS, fix, re-run to verify
