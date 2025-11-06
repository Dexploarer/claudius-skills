# Skill Evaluation Framework

> **Based on:** [Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents) + [Equipping Agents with Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
>
> **Status:** Production Framework
> **Level:** All Levels

## Overview

Skill evaluation ensures that agent skills perform effectively in realistic workflows. Anthropic emphasizes **evaluation-driven development**: start with representative test cases, iterate based on results, and avoid sandbox scenarios that don't reflect actual usage.

**Key Principles:**
- ✅ **Realistic workflows** not simplistic tests
- ✅ **Representative tasks** based on actual usage
- ✅ **Flexible verifiers** accepting valid alternatives
- ✅ **Iterative improvement** based on failures
- ✅ **Transcript analysis** to identify patterns

---

## Evaluation Framework

### Level 1: Basic Validation

**Purpose:** Ensure skill activates and completes without errors

**Tests:**
- Skill loads without syntax errors
- YAML frontmatter is valid
- Activation triggers work
- Basic execution completes

**Example:**

```typescript
// Test: Skill loads correctly
describe('react-component-generator skill', () => {
  it('should load without errors', () => {
    const skill = loadSkill('react-component-generator');
    expect(skill).toBeDefined();
    expect(skill.name).toBe('react-component-generator');
  });

  it('should have valid frontmatter', () => {
    const skill = loadSkill('react-component-generator');
    expect(skill.description).toBeTruthy();
    expect(skill.description.length).toBeGreaterThan(10);
  });

  it('should activate on trigger phrases', () => {
    const triggers = [
      'create react component',
      'generate component',
      'new react component'
    ];

    for (const trigger of triggers) {
      const activated = shouldActivateSkill('react-component-generator', trigger);
      expect(activated).toBe(true);
    }
  });
});
```

---

### Level 2: Functional Testing

**Purpose:** Verify skill produces expected outputs

**Tests:**
- Skill generates correct file structure
- Output follows conventions
- Edge cases handled
- Error handling works

**Example:**

```typescript
// Test: React component generation
describe('react-component-generator functional tests', () => {
  it('should generate functional component with props', async () => {
    const result = await executeSkill('react-component-generator', {
      componentName: 'UserCard',
      props: ['name', 'email', 'avatar']
    });

    // Verify file created
    expect(result.filesCreated).toContain('UserCard.tsx');

    // Verify content structure
    const content = result.files['UserCard.tsx'];
    expect(content).toContain('interface UserCardProps');
    expect(content).toContain('name: string');
    expect(content).toContain('email: string');
    expect(content).toContain('export default UserCard');
  });

  it('should handle TypeScript types correctly', async () => {
    const result = await executeSkill('react-component-generator', {
      componentName: 'DataTable',
      props: ['data: User[]', 'onSort: (key: string) => void']
    });

    const content = result.files['DataTable.tsx'];
    expect(content).toContain('data: User[]');
    expect(content).toContain('onSort: (key: string) => void');
  });

  it('should create test file when requested', async () => {
    const result = await executeSkill('react-component-generator', {
      componentName: 'Button',
      includeTests: true
    });

    expect(result.filesCreated).toContain('Button.test.tsx');
    expect(result.files['Button.test.tsx']).toContain('describe');
    expect(result.files['Button.test.tsx']).toContain('test');
  });
});
```

---

### Level 3: Realistic Workflows

**Purpose:** Test skill in actual development scenarios

**Anthropic Standard:**
> "Create realistic evaluation tasks grounded in actual workflows requiring multiple tool calls—not simplistic 'sandbox' scenarios."

**Tests:**
- Multi-step workflows
- Integration with other tools
- Real codebase scenarios
- Realistic constraints

**Example:**

```typescript
// Test: Complete feature implementation workflow
describe('complete feature workflow', () => {
  it('should implement login form from mockup to deployment', async () => {
    const workflow = new WorkflowTest('implement-login-form');

    // Step 1: Explore phase
    const exploration = await workflow.explore({
      mockup: 'login-mockup.png',
      existingAuth: 'src/auth/',
      framework: 'Next.js'
    });

    expect(exploration.filesRead).toContain('src/auth/login.ts');
    expect(exploration.patternsIdentified).toContain('OAuth');

    // Step 2: Plan phase
    const plan = await workflow.plan();

    expect(plan.steps).toHaveLength(5); // Reasonable decomposition
    expect(plan.filesTo Modify).toContain('src/pages/login.tsx');
    expect(plan.verificationSteps).toBeDefined();

    // Step 3: Implementation
    const implementation = await workflow.implement();

    expect(implementation.filesCreated).toContain('src/pages/login.tsx');
    expect(implementation.testsCreated).toContain('login.test.tsx');

    // Step 4: Verification
    const verification = await workflow.verify();

    expect(verification.testsPass).toBe(true);
    expect(verification.linterPass).toBe(true);
    expect(verification.typecheck).toBe(true);

    // Step 5: Commit
    const commit = await workflow.commit();

    expect(commit.message).toContain('feat: implement login form');
    expect(commit.docsUpdated).toBe(true);

    // Overall workflow success
    expect(workflow.success).toBe(true);
    expect(workflow.duration).toBeLessThan(300000); // < 5 minutes
  });
});
```

---

### Level 4: Flexible Verification

**Purpose:** Accept valid alternatives, not just exact matches

**Anthropic Standard:**
> "Use flexible verifiers accepting valid alternative phrasings."

**Anti-pattern:**
```typescript
// ❌ Too rigid
expect(result.component).toBe('export default function Button()');
// Fails if formatted differently or uses arrow function
```

**Best Practice:**
```typescript
// ✅ Flexible verification
function verifyReactComponent(content: string, name: string) {
  // Accept any valid export format
  const validExports = [
    `export default function ${name}`,
    `export default ${name}`,
    `function ${name}`,
    `const ${name} =`,
    `export const ${name} =`
  ];

  const hasValidExport = validExports.some(pattern =>
    content.includes(pattern)
  );

  expect(hasValidExport).toBe(true);

  // Accept any valid TypeScript interface
  expect(
    content.includes(`interface ${name}Props`) ||
    content.includes(`type ${name}Props`)
  ).toBe(true);

  // Verify structure, not exact formatting
  expect(content).toMatch(/return\s*\(/); // Has JSX return
  expect(content).toMatch(/import.*React/); // Imports React
}
```

---

## Evaluation Metrics

### Skill Effectiveness Metrics

**1. Activation Accuracy**
- Activates when should: True Positive Rate
- Doesn't activate when shouldn't: True Negative Rate
- Target: >95% accuracy

```typescript
const activationTests = [
  { input: 'create react component', shouldActivate: true },
  { input: 'generate Vue component', shouldActivate: false },
  { input: 'new component for dashboard', shouldActivate: true },
  { input: 'delete component', shouldActivate: false }
];

const accuracy = evaluateActivation('react-component-generator', activationTests);
expect(accuracy).toBeGreaterThan(0.95);
```

**2. Output Quality**
- Follows best practices
- Includes error handling
- Has proper types (TypeScript)
- Passes linter
- Target: >90% quality score

```typescript
function qualityScore(output: string): number {
  let score = 0;

  // Check best practices (25 points each)
  if (hasTypeScript(output)) score += 25;
  if (hasErrorHandling(output)) score += 25;
  if (passesLinter(output)) score += 25;
  if (followsConventions(output)) score += 25;

  return score; // 0-100
}
```

**3. Completeness**
- All required files created
- Tests included (if requested)
- Documentation updated
- Target: 100% completeness

**4. Reliability**
- Consistent outputs
- Handles edge cases
- Recovers from errors
- Target: >98% reliability

---

## Testing Workflows

### Workflow 1: Manual Testing

**Quick validation during development:**

```bash
# Test skill activation
User: "create react component Button"
Expected: react-component-generator skill activates

# Test output
User: "create react component UserCard with props name and email"
Expected:
  - Creates UserCard.tsx
  - Has UserCardProps interface
  - Includes name and email props
  - Follows TypeScript conventions

# Test edge cases
User: "create react component with no props"
Expected: Creates component without props interface
```

### Workflow 2: Automated Testing

**Continuous evaluation:**

```typescript
// tests/skills/react-component-generator.test.ts

import { evaluateSkill } from '@/testing/skill-evaluator';

describe('react-component-generator skill', () => {
  const testCases = [
    {
      name: 'simple component',
      input: { componentName: 'Button' },
      expected: {
        files: ['Button.tsx'],
        hasTypes: true,
        hasExport: true
      }
    },
    {
      name: 'component with props',
      input: {
        componentName: 'UserCard',
        props: ['name', 'email']
      },
      expected: {
        files: ['UserCard.tsx'],
        hasInterface: true,
        propsCount: 2
      }
    },
    {
      name: 'component with tests',
      input: {
        componentName: 'Button',
        includeTests: true
      },
      expected: {
        files: ['Button.tsx', 'Button.test.tsx'],
        testsExist: true
      }
    }
  ];

  testCases.forEach(testCase => {
    it(`should handle ${testCase.name}`, async () => {
      const result = await evaluateSkill(
        'react-component-generator',
        testCase.input
      );

      expect(result.filesCreated).toEqual(testCase.expected.files);

      if (testCase.expected.hasInterface) {
        expect(result.output).toContain('interface');
      }

      if (testCase.expected.testsExist) {
        expect(result.output).toContain('describe');
      }
    });
  });
});
```

### Workflow 3: Transcript Analysis

**Learn from real usage:**

```typescript
// Analyze conversation transcripts
import { analyzeTranscripts } from '@/testing/transcript-analyzer';

const transcripts = loadTranscripts('./logs/2025-11/');

const analysis = analyzeTranscripts(transcripts, {
  skillName: 'react-component-generator',
  metrics: [
    'activation_accuracy',
    'user_satisfaction',
    'error_rate',
    'completion_time'
  ]
});

console.log(`
Skill: react-component-generator
Period: November 2025

Activation Accuracy: ${analysis.activation_accuracy}%
User Satisfaction: ${analysis.user_satisfaction}/5
Error Rate: ${analysis.error_rate}%
Avg Completion Time: ${analysis.avg_completion_time}s

Top Issues:
${analysis.top_issues.map(i => `- ${i}`).join('\n')}

Recommendations:
${analysis.recommendations.map(r => `- ${r}`).join('\n')}
`);
```

---

## Skill Evaluator Tool

### Create Automated Evaluator

```typescript
// src/testing/skill-evaluator.ts

export interface SkillTestCase {
  name: string;
  input: any;
  expected: any;
  verify?: (result: any) => boolean;
}

export interface SkillTestResult {
  passed: boolean;
  failures: string[];
  metrics: {
    activationAccuracy: number;
    outputQuality: number;
    completeness: number;
    reliability: number;
  };
}

export async function evaluateSkill(
  skillName: string,
  testCases: SkillTestCase[]
): Promise<SkillTestResult> {
  const results: SkillTestResult = {
    passed: true,
    failures: [],
    metrics: {
      activationAccuracy: 0,
      outputQuality: 0,
      completeness: 0,
      reliability: 0
    }
  };

  for (const testCase of testCases) {
    try {
      // Execute skill
      const output = await executeSkill(skillName, testCase.input);

      // Verify output
      if (testCase.verify) {
        const passed = testCase.verify(output);
        if (!passed) {
          results.passed = false;
          results.failures.push(`Test "${testCase.name}" failed verification`);
        }
      } else {
        // Use default verification
        const passed = defaultVerify(output, testCase.expected);
        if (!passed) {
          results.passed = false;
          results.failures.push(`Test "${testCase.name}" failed: expected ${JSON.stringify(testCase.expected)}`);
        }
      }

      // Calculate metrics
      results.metrics.outputQuality += qualityScore(output);
      results.metrics.completeness += completenessScore(output, testCase.expected);

    } catch (error) {
      results.passed = false;
      results.failures.push(`Test "${testCase.name}" threw error: ${error.message}`);
      results.metrics.reliability -= 10; // Penalty for errors
    }
  }

  // Average metrics
  results.metrics.outputQuality /= testCases.length;
  results.metrics.completeness /= testCases.length;
  results.metrics.reliability = Math.max(0, 100 + results.metrics.reliability);

  return results;
}
```

---

## Best Practices

### ✅ Do:

1. **Start with Evaluation**
   - Identify capability gaps through testing
   - Create representative test cases first
   - Iterate skill based on failures

2. **Test Realistic Workflows**
   - Multi-step scenarios
   - Integration with other tools
   - Real codebase constraints

3. **Use Flexible Verifiers**
   - Accept valid alternatives
   - Don't require exact string matches
   - Verify structure, not formatting

4. **Analyze Transcripts**
   - Learn from real usage patterns
   - Identify common failure modes
   - Iterate skill improvements

5. **Automate Where Possible**
   - Continuous testing in CI/CD
   - Automated quality metrics
   - Regular effectiveness reviews

6. **Test Edge Cases**
   - Empty inputs
   - Invalid parameters
   - Error conditions
   - Boundary values

### ❌ Don't:

1. **Don't Create Sandbox Scenarios**
   - Unrealistic simplified tests
   - Don't reflect actual usage
   - Miss real-world complexity

2. **Don't Use Rigid Verification**
   - Exact string matching
   - Brittle assertions
   - Formatting-dependent tests

3. **Don't Skip Manual Testing**
   - Automated tests miss UX issues
   - Human judgment important
   - User satisfaction matters

4. **Don't Test in Isolation**
   - Skills interact with other tools
   - Test integration scenarios
   - Verify workflow completeness

5. **Don't Ignore Failures**
   - Every failure is a learning opportunity
   - Update skill based on failures
   - Track improvement over time

---

## Evaluation Templates

### Template 1: New Skill Checklist

```markdown
## Skill Evaluation Checklist

Skill Name: __________________
Date: __________________
Evaluator: __________________

### Basic Validation
- [ ] Skill loads without errors
- [ ] YAML frontmatter is valid
- [ ] Has name and description
- [ ] Activation triggers work

### Functional Testing
- [ ] Produces expected output
- [ ] Handles edge cases
- [ ] Error handling works
- [ ] Follows conventions

### Realistic Workflow
- [ ] Tested in real codebase
- [ ] Multi-step workflow works
- [ ] Integrates with other tools
- [ ] Meets performance targets

### Quality Metrics
- Activation Accuracy: _____%
- Output Quality: _____%
- Completeness: _____%
- Reliability: _____%

### Issues Found
1. _______________________
2. _______________________
3. _______________________

### Recommendations
1. _______________________
2. _______________________
3. _______________________

### Overall Assessment
- [ ] Ready for production
- [ ] Needs minor improvements
- [ ] Requires major refactor
- [ ] Not ready for release

### Notes
_________________________________
_________________________________
_________________________________
```

### Template 2: Transcript Analysis

```markdown
## Skill Usage Analysis

Skill: __________________
Period: __________________
Total Uses: __________________

### Activation Patterns
Most common trigger phrases:
1. _______________________
2. _______________________
3. _______________________

False activations: _____%
Missed activations: _____%

### Success Metrics
Successful completions: _____%
Partial completions: _____%
Failures: _____%

Average completion time: ______ seconds

### User Feedback
Positive: _____%
Neutral: _____%
Negative: _____%

Common complaints:
- _______________________
- _______________________

### Error Analysis
Most common errors:
1. _______________________
2. _______________________
3. _______________________

### Improvement Opportunities
1. _______________________
2. _______________________
3. _______________________

### Action Items
- [ ] _______________________
- [ ] _______________________
- [ ] _______________________
```

---

## Integration with Claudius Skills

### Skill: skill-evaluator

Create skill to automate evaluation:

```markdown
---
name: skill-evaluator
description: Evaluate skill effectiveness using realistic workflows and flexible verification
trigger: evaluate skill|test skill|skill quality|skill performance
---

# Skill Evaluator

## Purpose
Evaluate skill effectiveness following Anthropic's evaluation-driven development approach.

## When to Activate
- Testing new skill
- Auditing existing skill
- Investigating skill failures
- Measuring skill improvements

## Evaluation Process

### Step 1: Basic Validation
1. Load skill file
2. Verify YAML frontmatter
3. Check activation triggers
4. Confirm no syntax errors

### Step 2: Functional Testing
1. Create test cases for common scenarios
2. Execute skill with test inputs
3. Verify outputs match expectations
4. Use flexible verifiers (not exact matches)

### Step 3: Realistic Workflows
1. Test in actual codebase
2. Multi-step workflow scenarios
3. Integration with other tools
4. Performance benchmarks

### Step 4: Calculate Metrics
- Activation Accuracy
- Output Quality
- Completeness
- Reliability

### Step 5: Generate Report
Present results with:
- Metrics summary
- Issues found
- Recommendations
- Overall assessment

## Output Format
```
Skill Evaluation: [skill-name]
====================================

✅ Basic Validation: PASS
✅ Functional Tests: 8/10 PASS
⚠️ Realistic Workflows: 2/3 PASS

Metrics:
- Activation Accuracy: 95%
- Output Quality: 88%
- Completeness: 90%
- Reliability: 98%

Issues:
1. Edge case: empty input not handled
2. Performance: slow on large files (>1000 lines)

Recommendations:
1. Add input validation
2. Optimize for large files
3. Add more edge case tests

Overall: ✅ Production Ready (with minor improvements)
```
```

---

## References

- [Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [Equipping Agents with Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Building Agents with Claude SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)

---

**Framework Status:** ✅ Production Ready
**Compliance:** Anthropic Standard
**Approach:** Evaluation-Driven Development
**Level:** All Levels
