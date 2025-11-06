---
name: skill-evaluator
description: Evaluate skill effectiveness using realistic workflows, flexible verification, and evaluation-driven development
trigger: evaluate skill|test skill|skill quality|skill performance|assess skill
---

# Skill Evaluator

## Purpose

Evaluate skill effectiveness following Anthropic's evaluation-driven development approach with realistic workflows, flexible verification, and iterative improvement based on results.

**Source:** https://www.anthropic.com/engineering/writing-tools-for-agents

## When to Activate

This skill activates when:
- Testing new skill before production
- Auditing existing skill performance
- Investigating skill failures or issues
- Measuring skill improvements after updates
- User mentions "evaluate skill", "test skill", or "skill quality"

## Evaluation Levels

### Level 1: Basic Validation ✅

**Quick checks:**
- Skill loads without errors
- YAML frontmatter is valid (`name` and `description`)
- Activation triggers work correctly
- No syntax errors in content

**Checklist:**
```markdown
- [ ] Skill file exists and is readable
- [ ] YAML frontmatter present
- [ ] Has `name` field
- [ ] Has `description` field
- [ ] Description is informative (>10 chars)
- [ ] No markdown syntax errors
- [ ] Activation triggers defined
```

---

### Level 2: Functional Testing ⚙️

**Verify outputs:**
- Skill produces expected results
- Follows project conventions
- Handles common scenarios
- Error handling works

**Test Cases:**
```markdown
## Test Case: [Scenario Name]

**Input:** [What triggers the skill]
**Expected Output:**
- [ ] Creates expected files
- [ ] Follows naming conventions
- [ ] Includes proper types (TypeScript)
- [ ] Has error handling
- [ ] Passes linter

**Actual Output:**
[Record actual behavior]

**Result:** PASS / FAIL
```

---

### Level 3: Realistic Workflows 🔄

**Anthropic Standard:**
> "Create realistic evaluation tasks grounded in actual workflows requiring multiple tool calls—not simplistic 'sandbox' scenarios."

**Multi-step scenarios:**
- Complete feature implementation
- Integration with other tools
- Real codebase constraints
- Performance under realistic conditions

**Workflow Test Example:**
```markdown
## Workflow: Complete Feature Implementation

**Scenario:** Implement login form from mockup to deployment

**Steps:**
1. Explore: Read existing auth, review mockup
2. Plan: Create implementation strategy
3. Code: Implement with tests
4. Verify: Tests pass, linter clean, UI matches mockup
5. Commit: Clear message, docs updated

**Metrics:**
- Time to complete: ______ minutes
- First-time success: YES / NO
- Issues encountered: __________
- Quality score: ____ / 100

**Result:** PASS / FAIL
```

---

### Level 4: Flexible Verification 🎯

**Anthropic Standard:**
> "Use flexible verifiers accepting valid alternative phrasings."

**Anti-pattern:**
```typescript
// ❌ Too rigid - exact string match
expect(output).toBe('export default function Button()');
```

**Best Practice:**
```typescript
// ✅ Flexible - accepts valid variations
const validPatterns = [
  'export default function Button',
  'export default Button',
  'const Button =',
  'function Button'
];
const hasValidExport = validPatterns.some(p => output.includes(p));
expect(hasValidExport).toBe(true);
```

**Verification Principles:**
- ✅ Verify structure, not formatting
- ✅ Accept semantically equivalent alternatives
- ✅ Focus on correctness, not style
- ❌ Don't require exact string matches
- ❌ Don't enforce specific formatting

---

## Evaluation Process

### Step 1: Load and Validate Skill

```
1. Read skill file
2. Parse YAML frontmatter
3. Validate required fields
4. Check for syntax errors
5. Record metadata
```

**Questions:**
- Does the skill load without errors?
- Is the YAML frontmatter valid?
- Are name and description present?

---

### Step 2: Test Activation

```
1. Identify trigger phrases from frontmatter
2. Create test inputs matching triggers
3. Verify skill activates correctly
4. Test edge cases (partial matches, typos)
5. Calculate activation accuracy
```

**Activation Test Cases:**
```markdown
| Input | Should Activate | Actually Activated | Result |
|-------|----------------|-------------------|--------|
| "create react component" | YES | ✓ | PASS |
| "generate component" | YES | ✓ | PASS |
| "delete component" | NO | ✗ | PASS |
| "vue component" | NO | ✗ | PASS |
```

**Metric:** Activation Accuracy = Correct / Total × 100%

---

### Step 3: Functional Testing

```
1. Create representative test cases
2. Execute skill with test inputs
3. Verify outputs match expectations
4. Use flexible verification
5. Calculate quality score
```

**Quality Scoring:**
```markdown
## Output Quality (0-100)

- TypeScript types present: +25
- Error handling included: +25
- Passes linter: +25
- Follows conventions: +25

Total: ____ / 100
```

---

### Step 4: Realistic Workflow Testing

```
1. Design complete feature workflow
2. Execute multi-step scenario
3. Measure time to completion
4. Track issues encountered
5. Verify final output quality
```

**Workflow Metrics:**
- ⏱️ **Time:** How long to complete
- ✅ **Success:** First-time success rate
- 🐛 **Issues:** Problems encountered
- 💯 **Quality:** Output quality score
- 🔄 **Iterations:** Rework needed

---

### Step 5: Generate Report

Present comprehensive evaluation:

```markdown
# Skill Evaluation Report

## Skill: [skill-name]
## Date: [evaluation-date]
## Evaluator: Claude (Skill Evaluator)

---

## Summary

✅ **Overall Result:** PASS / NEEDS IMPROVEMENT / FAIL

---

## Level 1: Basic Validation

| Check | Result |
|-------|--------|
| Skill loads | ✅ PASS |
| YAML valid | ✅ PASS |
| Has name | ✅ PASS |
| Has description | ✅ PASS |
| No syntax errors | ✅ PASS |

**Result:** 5/5 PASS

---

## Level 2: Functional Testing

| Test Case | Result |
|-----------|--------|
| Simple component | ✅ PASS |
| Component with props | ✅ PASS |
| With TypeScript | ✅ PASS |
| Error handling | ⚠️  PARTIAL |

**Result:** 3.5/4 = 87.5%

**Issues:**
- Error handling could be more comprehensive

---

## Level 3: Realistic Workflows

| Workflow | Time | Success | Quality | Result |
|----------|------|---------|---------|--------|
| Complete feature | 12 min | ✅ YES | 92/100 | ✅ PASS |
| Integration test | 8 min | ✅ YES | 88/100 | ✅ PASS |

**Result:** 2/2 workflows successful

---

## Metrics

| Metric | Score | Target | Status |
|--------|-------|--------|--------|
| **Activation Accuracy** | 95% | >90% | ✅ PASS |
| **Output Quality** | 90% | >85% | ✅ PASS |
| **Completeness** | 95% | >90% | ✅ PASS |
| **Reliability** | 98% | >95% | ✅ PASS |

---

## Issues Found

1. **Error handling** - Could be more comprehensive
   - Severity: Minor
   - Recommendation: Add more edge case handling

2. **Documentation** - Missing usage examples
   - Severity: Minor
   - Recommendation: Add 2-3 examples

---

## Recommendations

1. ✅ **Production Ready** - Skill performs well
2. 🔧 **Minor Improvements:**
   - Enhance error handling for edge cases
   - Add more usage examples
   - Consider adding tests generation
3. 📈 **Future Enhancements:**
   - Support for styled-components
   - Add accessibility props by default

---

## Overall Assessment

**Status:** ✅ **Production Ready** (with minor improvements)

The skill performs well across all evaluation levels. Basic validation and realistic workflows both pass. Minor improvements recommended for error handling and documentation, but skill is ready for production use.

**Confidence:** High
**Recommendation:** Approve for production with tracked improvements
```

---

## Evaluation Metrics

### Key Metrics

**1. Activation Accuracy**
- True Positives: Activates when should
- True Negatives: Doesn't when shouldn't
- Target: >95%

**2. Output Quality**
- Best practices followed: 25%
- Error handling: 25%
- Type safety: 25%
- Conventions: 25%
- Target: >85%

**3. Completeness**
- All required files created
- Documentation included
- Tests present (if requested)
- Target: >90%

**4. Reliability**
- Consistent outputs
- Handles edge cases
- Recovers from errors
- Target: >95%

---

## Best Practices

### ✅ Do:

1. **Test Realistic Workflows**
   - Multi-step scenarios
   - Real codebase constraints
   - Integration with other tools

2. **Use Flexible Verification**
   - Accept valid alternatives
   - Verify structure, not formatting
   - Semantic equivalence

3. **Measure Multiple Metrics**
   - Activation accuracy
   - Output quality
   - Completeness
   - Reliability

4. **Provide Actionable Feedback**
   - Specific issues
   - Clear recommendations
   - Severity levels

5. **Track Improvements**
   - Before/after metrics
   - Trend analysis
   - Effectiveness over time

### ❌ Don't:

1. **Don't Use Sandbox Tests**
   - Simplistic scenarios
   - Unrealistic conditions
   - No integration testing

2. **Don't Use Rigid Verification**
   - Exact string matching
   - Formatting dependencies
   - Brittle assertions

3. **Don't Test in Isolation**
   - Skills interact with tools
   - Need integration scenarios
   - Workflow context matters

4. **Don't Ignore Failures**
   - Every failure teaches something
   - Update skill based on failures
   - Track improvement over time

---

## Integration with Claudius Skills

### Evaluate Any Skill

```
User: "Evaluate the react-component-generator skill"
Claude: [Activates skill-evaluator]

1. Basic Validation ✅
2. Functional Testing ✅
3. Realistic Workflows ✅
4. Generate comprehensive report
```

### Batch Evaluation

```
User: "Evaluate all skills in starter-kit"
Claude: [Evaluates each skill]

Summary:
- Total skills: 5
- Passing: 4
- Need improvement: 1
- Failing: 0

Detailed reports for each skill...
```

---

## Evaluation Templates

### Quick Evaluation Checklist

```markdown
## Quick Skill Evaluation

Skill: __________________

### Basic (1 minute)
- [ ] Loads without errors
- [ ] Valid YAML
- [ ] Has name & description
- [ ] Triggers work

### Functional (5 minutes)
- [ ] Produces expected output
- [ ] Handles edge cases
- [ ] Quality score: ____ / 100

### Realistic (15 minutes)
- [ ] Complete workflow: PASS / FAIL
- [ ] Time: ____ minutes
- [ ] Issues: __________

### Overall
- [ ] Production ready
- [ ] Needs minor improvements
- [ ] Requires major refactor
```

---

## Related Resources

- **Documentation:** See `docs/testing/skill-evaluation.md`
- **Workflows:** See `docs/workflows/explore-plan-code-commit.md`
- **Best Practices:** See Anthropic blog posts

---

**Skill Status:** ✅ Production Ready
**Approach:** Evaluation-Driven Development
**Compliance:** Anthropic Standard
**Level:** Intermediate
