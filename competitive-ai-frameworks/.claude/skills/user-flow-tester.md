# User Flow Olympics Tester

## Skill Activation

This skill automatically activates when the user mentions:
- "test user flows"
- "optimize user experience"
- "improve conversion"
- "user journey testing"
- "flow optimization"
- "UX testing"

## Skill Description

Orchestrates a competitive user flow olympics where three specialized AI teams compete to optimize user flows for completion rate, error handling, and integration using reinforcement learning.

## Teams

**Team 1: Happy Path Optimizers**
- Focus: Conversion, friction reduction  
- Best at: Form optimization, checkout flows, CTAs

**Team 2: Edge Case Handlers**
- Focus: Error states, accessibility, mobile
- Best at: WCAG compliance, error handling, responsive design

**Team 3: Integration Specialists**
- Focus: API reliability, state management, cross-flow
- Best at: Integration points, state consistency, performance

## Execution

When activated:

1. **Select Flows** to test
   - Common: registration, login, checkout, profile
   - Custom: user-specified flows

2. **Run Olympics** (default 4 rounds)
   - Teams optimize flows
   - Measure improvements
   - Adapt strategies via RL

3. **Present Results**
   - Winner announcement
   - Flow improvements
   - Combined best practices

## Usage

```bash
/run-flow-test --flows registration,checkout,profile
```

Or mention: "I need to test user flows"

## Output

```
🥇 WINNER: Team 1 - Happy Path Optimizers
   Total Score: 189 points
   - Completion rate: 68% → 92%
   - Time to complete: -62%
   - Friction points: 5 → 1
```
