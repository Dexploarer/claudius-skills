---
description: Run competitive bug hunting championship with 3 AI teams
---

You are running the Bug Hunting Championship command.

## Command Purpose

Execute a competitive bug hunting simulation where three specialized AI teams compete to find vulnerabilities using different strategies and reinforcement learning.

## Arguments

Parse the following arguments from the user's command:

- `--target <path>` - Path to target codebase (required)
- `--rounds <n>` - Number of rounds to run (default: 5)
- `--output <path>` - Output directory for results (default: ./results)
- `--visualize` - Generate visualizations (optional flag)
- `--team <name>` - Run only specific team (optional: automated/manual/fuzzing)

## Execution Steps

1. **Validate Authorization**

   Ask user to confirm:
   ```
   ⚠️  Before starting bug hunting:

   1. Do you have authorization to test this codebase?
   2. Is this for defensive security or educational purposes?
   3. Is this your own code or an authorized test environment?

   Please confirm (yes/no):
   ```

   Only proceed if user confirms.

2. **Parse Arguments**

   Extract target path and options from command.

   If target not provided:
   ```
   Please specify target: /run-bug-hunt --target <path>
   ```

3. **Display Configuration**

   ```
   ╔══════════════════════════════════════════════════════╗
   ║   BUG HUNTING CHAMPIONSHIP                          ║
   ╚══════════════════════════════════════════════════════╝

   Target:    [target path]
   Rounds:    [n]
   Output:    [output path]
   Teams:     [3 teams or specific team]

   Starting championship...
   ```

4. **Execute Championship**

   Run the coordinator:
   ```bash
   cd competitive-ai-frameworks/frameworks/bug-hunting
   python coordinator.py \
     --target [target_path] \
     --rounds [n] \
     --output [output_path] \
     [--visualize]
   ```

   Or for single team:
   ```bash
   python coordinator.py \
     --target [target_path] \
     --rounds [n] \
     --team [team_name]
   ```

5. **Monitor and Display Progress**

   Show live updates for each round:

   ```
   ═══════════════════════════════════════════════════════
   Round 1/5
   ═══════════════════════════════════════════════════════

   ▶ Team 1: Automated Scanners hunting...
     ✓ Found 8 potential vulnerabilities
     ✓ Score: 285 points

   ▶ Team 2: Manual Reviewers hunting...
     ✓ Found 3 potential vulnerabilities
     ✓ Score: 350 points

   ▶ Team 3: Fuzzers hunting...
     ✓ Found 5 potential vulnerabilities
     ✓ Score: 310 points

   Round 1 Leader: Team 2 (Manual Reviewers) - 350 points

   Adapting strategies based on performance...
   ```

6. **Present Final Results**

   Display comprehensive results:

   ```
   ╔══════════════════════════════════════════════════════╗
   ║   CHAMPIONSHIP RESULTS                              ║
   ╚══════════════════════════════════════════════════════╝

   🥇 WINNER: Team 2 - Manual Reviewers
      Total Score: 1,450 points
      Bugs Found: 12 (2 Critical, 5 High, 5 Medium)
      Unique Discoveries: 8
      False Positive Rate: 5%
      Average Time: 12 minutes

   🥈 SECOND: Team 3 - Fuzzers
      Total Score: 1,200 points
      Bugs Found: 18 (1 Critical, 7 High, 10 Medium)
      Unique Discoveries: 6
      False Positive Rate: 10%
      Average Time: 8 minutes

   🥉 THIRD: Team 1 - Automated Scanners
      Total Score: 980 points
      Bugs Found: 25 (0 Critical, 9 High, 16 Medium)
      Unique Discoveries: 4
      False Positive Rate: 20%
      Average Time: 3 minutes

   ════════════════════════════════════════════════════════

   TOP VULNERABILITIES FOUND

   1. 🔴 CRITICAL - Authentication Bypass (CVSS 9.8)
      Location: src/auth/middleware.py:78
      Team: Manual Reviewers

      JWT validation accepts 'none' algorithm, allowing
      complete authentication bypass.

      Impact: Attacker can impersonate any user

   2. 🔴 CRITICAL - Race Condition in Payment (CVSS 9.1)
      Location: src/payment/processor.py:234
      Team: Fuzzers

      Double-spend vulnerability in payment processing
      due to lack of transaction locking.

      Impact: Financial loss, duplicate transactions

   3. 🟠 HIGH - SQL Injection (CVSS 8.5)
      Location: src/db/queries.py:45
      Team: Automated Scanners

      Unsanitized user input in SQL query construction.

      Impact: Data exfiltration, database compromise

   [... more vulnerabilities ...]

   ════════════════════════════════════════════════════════

   WINNING STRATEGY ANALYSIS

   Team 2 (Manual Reviewers) won by:

   ✓ Focusing on critical business logic flaws
   ✓ Deep analysis of authentication and authorization
   ✓ High-quality, actionable vulnerability reports
   ✓ Low false positive rate (5%)
   ✓ Discovering unique, high-impact vulnerabilities

   Key Techniques Used:
   - Authentication flow analysis
   - Authorization boundary testing
   - IDOR vulnerability detection
   - Session management review

   ════════════════════════════════════════════════════════

   RECOMMENDED COMBINED APPROACH

   Based on all teams' performance, the optimal bug
   hunting strategy combines:

   1. START with Team 1's automated scanning
      → Fast coverage of known vulnerability patterns
      → Identifies obvious issues quickly

   2. FOLLOW with Team 2's manual review of critical paths
      → Deep analysis of authentication/authorization
      → Business logic vulnerability detection

   3. APPLY Team 3's fuzzing to identified attack surfaces
      → Test race conditions in critical operations
      → Validate input handling and edge cases

   This three-phase approach maximizes both coverage
   and critical bug discovery while minimizing false
   positives.

   ════════════════════════════════════════════════════════

   Results saved to: ./results/championship_20251101_143022.json
   ```

7. **Provide Next Steps**

   ```
   NEXT STEPS:

   1. Review and verify all reported vulnerabilities
   2. Prioritize fixes by CVSS score and impact
   3. Apply recommended remediation steps
   4. Re-run championship after fixes to verify

   To see detailed reports:
   - View JSON results: ./results/championship_*.json
   - Generate visualizations: /visualize-bug-hunt
   - Export to report: /generate-security-report
   ```

## Example Usage

```
/run-bug-hunt --target ./src --rounds 5 --visualize
```

```
/run-bug-hunt --target /path/to/repo --rounds 3 --team manual
```

```
/run-bug-hunt --target . --rounds 10 --output ~/security-audit
```

## Quick Mode

If user just runs `/run-bug-hunt` without arguments:

1. Detect current working directory as target
2. Use default settings (5 rounds)
3. Confirm before starting

```
No target specified. Use current directory?

Target: /path/to/current/dir
Rounds: 5 (default)
Teams: All 3

Proceed? (yes/no):
```

## Team-Specific Mode

If `--team` is specified, run only that team:

```
/run-bug-hunt --target ./src --team automated
```

Shows:
```
Running Team 1: Automated Scanners only

This will perform fast pattern-based scanning for:
- SQL injection
- XSS
- Command injection
- Path traversal
- Hardcoded secrets

Starting scan...
```

## Error Handling

**Target doesn't exist:**
```
❌ Error: Target path does not exist: /invalid/path

Please provide a valid directory path.
```

**No authorization confirmed:**
```
❌ Cannot proceed without authorization confirmation.

Bug hunting should only be performed on:
- Your own code
- Code you have written permission to test
- Authorized test environments
- Educational/CTF environments
```

**Championship fails:**
```
❌ Championship execution failed

Error: [error details]

Please check:
- Target path is accessible
- Python dependencies are installed
- Sufficient disk space for results

For help: /help bug-hunting
```

## Integration

This command uses:

- **Python framework:** `frameworks/bug-hunting/coordinator.py`
- **Subagents:** Team 1, 2, 3 configurations
- **Scoring:** `scoring_engine.py` for bug valuation
- **Learning:** `reinforcement.py` for strategy adaptation

## Output Files

Creates:
- `results/championship_[timestamp].json` - Full results
- `results/bugs_[timestamp].json` - All discovered bugs
- `results/metrics_[timestamp].json` - Performance metrics
- `results/visualizations/` - Charts (if --visualize)

## Performance Tips

**Fast scan (fewer rounds):**
```
/run-bug-hunt --target ./src --rounds 2
```

**Thorough analysis (more rounds):**
```
/run-bug-hunt --target ./src --rounds 10
```

**Focus on critical bugs:**
```
/run-bug-hunt --target ./src --team manual --rounds 3
```

**Broad coverage:**
```
/run-bug-hunt --target ./src --team automated --rounds 1
```

## Success Criteria

Command succeeds when:
- ✓ Authorization confirmed
- ✓ Championship completes all rounds
- ✓ Results are generated and displayed
- ✓ Winner is determined
- ✓ Recommendations are provided
- ✓ Output files are created

## Related Commands

- `/security-audit` - Full security audit with reporting
- `/vulnerability-scan` - Quick automated scan only
- `/code-review` - Manual code review without competition
- `/visualize-bug-hunt` - Visualize previous results
- `/generate-security-report` - Create executive report
