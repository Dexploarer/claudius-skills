Run competitive user flow olympics with three specialized AI teams competing to optimize UX, conversion, and accessibility.

## Instructions

1. **Select Flows**
   - Ask user which flows to test (registration, checkout, etc.)
   - Or accept flows as arguments
   - Establish baseline metrics

2. **Parse Arguments**
   - `$1` or `--flows`: Comma-separated flow names (required)
   - `$2` or `--rounds`: Number of rounds (default: 4)
   - `--base-url`: Application URL for testing (required)
   - `--output`: Output directory for results (default: ./flow-results)
   - `--focus`: Specific area (conversion/accessibility/performance)

3. **Execute Olympics**
   ```bash
   cd competitive-ai-frameworks/frameworks/user-flows
   python coordinator.py \
     --flows $FLOWS \
     --rounds $ROUNDS \
     --base-url $BASE_URL \
     --output $OUTPUT \
     ${FOCUS:+--focus $FOCUS}
   ```

4. **Display Progress**
   - Show each round with optimizations applied
   - Display flow metrics improving
   - Show current team scores

5. **Present Results**
   - Winner announcement
   - Before/after flow metrics
   - Key optimizations made
   - Implementation recommendations

## Example Usage

```bash
# Test registration flow
/run-flow-test registration --base-url https://staging.example.com

# Multiple flows
/run-flow-test registration,checkout,profile

# Focus on conversion
/run-flow-test --flows checkout --focus conversion --rounds 5

# Specify everything
/run-flow-test --flows login,signup --base-url http://localhost:3000 --rounds 4
```

## What This Does

1. Measures baseline flow metrics (completion rate, time, errors, accessibility)
2. Initializes three competing AI teams (Happy Path, Edge Cases, Integration)
3. Runs olympics for specified number of rounds
4. Teams optimize flows in their specialty areas
5. Applies reinforcement learning to improve strategies
6. Scores based on completion rate, time reduction, error decrease
7. Presents comprehensive optimization recommendations

## Options

- **--flows <names>:** Which flows to optimize (registration/login/checkout/profile/etc.)
- **--base-url <url>:** Application URL (staging recommended)
- **--rounds <n>:** Number of optimization rounds (default: 4)
- **--focus <area>:** Emphasize conversion/accessibility/performance
- **--output <path>:** Custom output directory

## Output Format

```markdown
🎯 User Flow Olympics Results - Registration

🥇 Winner: Team 1 - Happy Path Optimizers (189 pts)

Improvements:
- Completion Rate: 68% → 92% (+24%)
- Time to Complete: 3m45s → 1m25s (-62%)
- Friction Points: 5 → 1

Key Optimizations:
✅ Reduced form fields: 12 → 6
✅ Added social auth (Google, GitHub)
✅ Improved error messages
✅ Added progress indicator

🥈 Team 2 - Edge Cases (165 pts)
- Error Rate: 12% → 3%
- WCAG Score: 65 → 95
- Mobile Completion: 52% → 86%

🥉 Team 3 - Integration (142 pts)
- API Response Time: -35%
- Fixed 3 race conditions

Recommended Implementation:
1. Deploy form simplification (highest impact)
2. Add accessibility improvements (compliance)
3. Apply API optimizations (reliability)

Expected: ~90%+ completion, <2min avg time

Results: ./flow-results/olympics_*.json
```

## Notes

- **Staging first:** Test on staging, not production
- **Baseline critical:** Measure before/after to prove improvements
- **Teams compete:** Happy Path (conversion), Edge Cases (accessibility), Integration (reliability)
- **Best rounds:** 4-6 rounds optimal for flow optimization
- **A/B test:** Validate major changes before production deployment
- **Metrics:** Completion rate, time, errors, accessibility, mobile performance
- **Follow-up:** Review recommendations, A/B test, deploy incrementally
