---
name: user-flow-tester
description: Orchestrate competitive user flow testing where three specialized AI teams compete to optimize user experience, conversion rates, and accessibility. Activates when user wants to test user flows, optimize UX, improve conversion, test user journeys, or mentions flow optimization or UX testing.
allowed-tools: [Read, Grep, Glob, Bash, Task, Edit]
---

# User Flow Olympics Tester

Orchestrates a competitive multi-agent simulation where three specialized AI teams compete to optimize user flows for completion rate, error handling, and integration reliability using reinforcement learning.

## When to Use

This skill should be used when:
- User wants to test and optimize user flows
- User needs to improve conversion rates or UX
- User requests user journey testing
- User mentions flow optimization or UX improvements
- User wants to test registration, checkout, or other critical flows
- User needs to improve accessibility or error handling in flows

## Instructions

### Step 1: Select Flows to Test

Identify which user flows to optimize:

**Common flows:**
- Registration/signup flow
- Login/authentication flow
- Checkout/purchase flow
- Profile/settings update flow
- Onboarding flow
- Password reset flow

**Custom flows:**
- User can specify any application-specific flows

Ask user:
```markdown
Which user flows would you like to optimize?

Common flows:
1. Registration
2. Login
3. Checkout
4. Profile management
5. Custom (specify)

Enter numbers or names (comma-separated):
```

### Step 2: Configure Olympics

Ask user for:
- **Target flows:** Which flows to test (required)
- **Rounds:** Number of optimization rounds (default: 4)
- **Focus areas:** Conversion, accessibility, performance (optional)
- **Environment:** Production URLs or local testing (required)
- **Metrics:** Which success metrics to track (default: completion rate, time, errors)

Example:
```bash
Flows: registration, checkout
Rounds: 4
Focus: conversion, accessibility
Environment: https://staging.example.com
Metrics: completion_rate, time_to_complete, error_rate, accessibility_score
```

### Step 3: Establish Baseline

Before optimization, measure current performance:

1. **Completion Rate:** % of users who complete the flow
2. **Time to Complete:** Average duration
3. **Friction Points:** Number of obstacles/confusing steps
4. **Error Rate:** % of flows with errors
5. **Accessibility Score:** WCAG compliance level
6. **Mobile Performance:** Mobile vs desktop completion

Example baseline:
```bash
Registration Flow Baseline:
- Completion Rate: 68%
- Avg Time: 3m 45s
- Friction Points: 5
- Error Rate: 12%
- WCAG Score: 65/100
- Mobile Completion: 52%
```

### Step 4: Run Competition Rounds

For each round (typically 4 rounds):

1. **Team 1 (Happy Path)** optimizes for conversion:
   - Reduce form fields
   - Improve call-to-action clarity
   - Minimize friction points
   - A/B test variations

2. **Team 2 (Edge Cases)** handles errors and accessibility:
   - Improve error messages
   - Add WCAG compliance
   - Test mobile/responsive design
   - Handle edge cases gracefully

3. **Team 3 (Integration)** ensures reliability:
   - Optimize API calls
   - Improve state management
   - Test cross-flow integration
   - Ensure performance under load

4. **Measure improvements** and score based on:
   - Completion rate increase
   - Time reduction
   - Error rate decrease
   - Accessibility improvements
   - User satisfaction (if available)

5. **Update strategies** via reinforcement learning

### Step 5: Present Results

Generate comprehensive report:
- 🥇 Winner and scores
- 📊 Before/after flow metrics
- 🎯 Key optimizations made
- 💡 Combined best practices
- 📝 Implementation recommendations

Example command:
```bash
cd competitive-ai-frameworks/frameworks/user-flows
python coordinator.py \
  --flows registration,checkout \
  --rounds 4 \
  --base-url https://staging.example.com \
  --output ./flow-results
```

## Best Practices

- ✅ Test on staging environment first, not production
- ✅ Gather baseline metrics before optimization
- ✅ Test with real user data or realistic test scenarios
- ✅ Include mobile and desktop testing
- ✅ Validate accessibility improvements with actual tools
- ✅ A/B test optimizations before deploying to production
- ✅ Monitor analytics after deploying flow improvements
- ✅ Combine insights from all teams for best results

## Examples

### Example 1: Optimize Registration Flow

**User Input:**
```
I need to test and improve our registration flow
```

**Skill Process:**
1. Identify registration flow as target
2. Measure baseline: 68% completion, 3m 45s avg time
3. Run 4 rounds of competitive optimization
4. Teams apply improvements
5. Measure final metrics

**Output:**
```markdown
🎯 User Flow Olympics Results - Registration Flow

🥇 Winner: Team 1 - Happy Path Optimizers (189 points)

Improvements:
- Completion Rate: 68% → 92% (+24% absolute improvement)
- Time to Complete: 3m 45s → 1m 25s (-62% faster)
- Friction Points: 5 → 1 (removed 4 obstacles)
- Form Fields: 12 → 6 (simplified)

Key Optimizations:
✅ Reduced form from 12 to 6 fields (removed redundant questions)
✅ Added social auth options (Google, GitHub)
✅ Improved password requirements messaging
✅ Added progress indicator
✅ Removed CAPTCHA, added invisible verification

🥈 Team 2 - Edge Case Handlers (165 points)
- Error Rate: 12% → 3% (-75% errors)
- WCAG Score: 65 → 95 (+30 points)
- Mobile Completion: 52% → 86% (+34% improvement)

Key Fixes:
✅ Clear inline error messages
✅ ARIA labels for screen readers
✅ Mobile-optimized input types
✅ Graceful API failure handling

🥉 Team 3 - Integration Specialists (142 points)
- API Response Time: -35% improvement
- State Management: Fixed 3 race conditions
- Email Verification: 98% delivery rate

Recommended Implementation:
1. Deploy Team 1's form simplification immediately (highest impact)
2. Add Team 2's accessibility improvements (compliance requirement)
3. Apply Team 3's API optimizations (reliability improvement)

Expected Results: ~90%+ completion rate, <2 minute avg time
```

**Explanation:** Happy Path team won by dramatically improving the core flow, while Edge Case team ensured accessibility and mobile experience, and Integration team made it reliable.

### Example 2: Multi-Flow Optimization

**User Input:**
```
Optimize our checkout and registration flows
```

**Skill Process:**
1. Test both flows simultaneously
2. Teams compete across both flows
3. Measure improvements per flow
4. Identify patterns and best practices

**Output:**
Results showing improvements across both flows with combined recommendations.

## Common Mistakes to Avoid

- ❌ Testing only happy path (miss accessibility and error cases)
- ❌ Not measuring baseline (can't prove improvements)
- ❌ Testing on production without staging validation
- ❌ Ignoring mobile users (often 50%+ of traffic)
- ❌ Deploying all changes at once (can't isolate what worked)
- ❌ Not A/B testing major flow changes
- ✅ Test all paths, measure baseline, use staging, include mobile, A/B test, deploy incrementally

## Tips

- 💡 **First time:** Start with one critical flow (registration or checkout)
- 💡 **Best results:** 4-6 rounds optimal for flow optimization
- 💡 **High impact:** Team 1 (Happy Path) often wins with friction reduction
- 💡 **Accessibility:** Team 2 ensures legal compliance and inclusive design
- 💡 **Reliability:** Team 3 prevents frustrating integration failures
- 💡 **Quick wins:** Reducing form fields and improving error messages have immediate impact
- 💡 **Validation:** Use real user testing or analytics to validate improvements

## Related Skills/Commands

- `/run-flow-test` - Quick start flow olympics
- `/run-quality-check` - Code quality championship
- `a11y-annotation-generator` skill - Accessibility annotations
- `test-helper` skill - Test generation

## Notes

**Scoring System:**
Teams earn points based on:
- Completion rate improvement (high weight)
- Time reduction (medium weight)
- Error rate decrease (high weight)
- Accessibility improvements (medium weight)
- User satisfaction increase (high weight if available)

**Team Specialties:**
- **Team 1 (Happy Path):** Conversion optimization, friction reduction, CTAs, form simplification
- **Team 2 (Edge Cases):** Accessibility, error handling, mobile optimization, edge case testing
- **Team 3 (Integration):** API reliability, state management, performance, cross-flow consistency

**Reinforcement Learning:**
Teams learn which optimizations yield the best completion rate improvements for your specific application. Later rounds focus on high-impact optimizations.

**Testing Methods:**
- Automated flow testing (Playwright/Cypress)
- Analytics review (Google Analytics, Mixpanel)
- Accessibility audits (axe-core, WAVE)
- Performance monitoring (Lighthouse, WebPageTest)

**Integration:**
Uses subagents in `.claude/subagents/team[1-3]-*.md` and Python framework in `frameworks/user-flows/`.
