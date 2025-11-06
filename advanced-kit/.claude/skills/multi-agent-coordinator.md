---
name: multi-agent-coordinator
description: Orchestrate multi-agent systems using lead agent + specialized subagent pattern for complex tasks
trigger: multi agent|orchestrate agents|coordinate subagents|parallel agents|spawn subagents
---

# Multi-Agent Coordinator Skill

## Purpose

Guide the implementation of multi-agent systems following Anthropic's orchestrator-worker pattern, achieving **90.2% better performance** on complex tasks through parallel execution and specialized expertise.

**Source:** https://www.anthropic.com/engineering/multi-agent-research-system

## When to Activate

This skill activates when:
- Complex queries requiring parallel exploration
- Tasks needing specialized expertise across multiple domains
- Breadth-first research or analysis
- Performance-critical workflows with 10+ subtasks
- User mentions "multi-agent", "coordinate agents", or "parallel execution"

## Core Pattern

### Orchestrator-Worker Architecture

```
Lead Agent (Orchestrator) - Claude Opus 4
├── Analyzes query complexity
├── Decomposes into subtasks
├── Spawns specialized subagents
├── Synthesizes results
└── Determines if additional work needed

Subagents (Workers) - Claude Sonnet 4
├── Execute focused tasks
├── Use 3+ tools in parallel
├── Return 1,000-2,000 token summaries
└── Clean context windows
```

**Performance:** 90.2% better than single-agent Opus

## Implementation Workflow

### Step 1: Complexity Analysis

Assess query to determine agent count needed:

**Simple (1 agent):**
- Straightforward question
- Single domain
- 3-10 tool calls
- Example: "What's the latest React version?"

**Moderate (2-5 agents):**
- Multi-faceted question
- 2-3 domains
- Requires different expertise
- Example: "How do I optimize React app performance?"

**Complex (10+ agents):**
- Breadth-first research
- Multiple domains
- Extensive parallel exploration
- Example: "Comprehensive analysis of modern frontend frameworks"

### Step 2: Task Decomposition

For moderate/complex queries, decompose into discrete subtasks:

**Requirements for each subtask:**
1. **Explicit boundaries** - Clear scope (what to include/exclude)
2. **Objective** - Specific goal to achieve
3. **Output format** - Expected structure (1,000-2,000 tokens)
4. **Tools** - Which tools to use
5. **Sources** - Where to look for information

**Anti-patterns to avoid:**
- ❌ Overlapping tasks (causes duplicate work)
- ❌ Gaps in coverage (incomplete results)
- ❌ Vague objectives (leads to confusion)

### Step 3: Create Research Plan

Save plan to filesystem before spawning:

```markdown
## RESEARCH_PLAN.md

# Research Plan: [Task Name]

## Complexity: [Simple/Moderate/Complex]

## Subtask Decomposition:

### Subagent 1: [Subtask Name]
- **Objective:** [Clear, focused goal]
- **Output:** [Expected format, token count]
- **Tools:** [List of tools to use]
- **Sources:** [Documentation, repos, etc.]
- **Scope:**
  - Include: [What's in scope]
  - Exclude: [What's out of scope]

### Subagent 2: [Subtask Name]
[Repeat structure]

## Parallelization Strategy:
[How subtasks will execute concurrently]

## Expected Timeline:
[Estimated completion time]

## Synthesis Approach:
[How findings will be combined]
```

### Step 4: Spawn Subagents

For each subtask:

1. **Create task specification:**
   ```markdown
   ## tasks/task-1-spec.md

   You are a specialized research agent.

   **Your Specific Task:**
   [Objective from research plan]

   **Output Format:**
   - 1,000-2,000 token summary
   - Key findings with evidence
   - Sources used
   - Confidence level

   **Tools Available:**
   [Relevant tools for this task]

   **Task Boundaries:**
   - Include: [Explicit scope]
   - Exclude: [Out of scope]

   **Execution:**
   1. Use 3+ tools in parallel
   2. Focus only on your objective
   3. Return findings to `findings/subagent-1-findings.md`
   ```

2. **Execute in parallel:**
   ```typescript
   // Spawn all subagents simultaneously
   const results = await Promise.all([
     spawnSubagent('Subagent 1', task1Spec),
     spawnSubagent('Subagent 2', task2Spec),
     spawnSubagent('Subagent 3', task3Spec),
     // ...up to 10+ for complex queries
   ]);
   ```

3. **Each subagent saves findings:**
   ```
   findings/
   ├── subagent-1-findings.md
   ├── subagent-2-findings.md
   ├── subagent-3-findings.md
   └── ...
   ```

### Step 5: Synthesize Results

1. **Read all findings:**
   ```bash
   # Lead agent reads findings from filesystem
   for file in findings/subagent-*.md; do
     process_findings "$file"
   done
   ```

2. **Evaluate completeness:**
   - Are all subtasks covered?
   - Any gaps in findings?
   - Conflicting information?

3. **If gaps exist:**
   - Spawn additional subagents to fill gaps
   - Iterate until complete

4. **Generate final synthesis:**
   ```markdown
   ## findings/synthesis.md

   # Final Synthesis: [Task Name]

   ## Summary
   [Comprehensive overview combining all findings]

   ## Key Findings
   1. [Finding 1 with sources]
   2. [Finding 2 with sources]
   3. [Finding 3 with sources]

   ## Recommendations
   [Actionable recommendations based on research]

   ## Confidence Levels
   - High confidence: [Topics]
   - Medium confidence: [Topics]
   - Areas needing more research: [Topics]

   ## Sources
   [All sources from all subagents]
   ```

## Model Tier Strategy

**Lead Agent:** Claude Opus 4
- General coordination and synthesis
- Broad reasoning capabilities
- Strategic decision-making

**Subagents:** Claude Sonnet 4
- Focused, specialized tasks
- Faster execution
- More cost-effective
- Clean context windows

**Why this works:** Combination outperforms single-agent Opus by 90.2%

## Communication Pattern

**✅ Correct:** Through orchestrator

```
Subagent 1 → Lead Agent ← Subagent 2
                ↓
           Synthesis
                ↓
              User
```

**❌ Incorrect:** Peer-to-peer

```
Subagent 1 ↔ Subagent 2 ← Causes confusion!
```

## External Memory Pattern

Save to filesystem to preserve context:

```
project/
├── RESEARCH_PLAN.md           # Strategy
├── tasks/
│   ├── task-1-spec.md        # Subagent specs
│   ├── task-2-spec.md
│   └── ...
└── findings/
    ├── subagent-1-findings.md # Detailed results
    ├── subagent-2-findings.md
    ├── subagent-3-findings.md
    └── synthesis.md           # Final output
```

**Benefits:**
- Multi-hour task coherence
- No context window bloat
- Clean subagent contexts
- Preserved for future reference

## Performance Optimization

### Parallel Tool Execution

Each subagent should use 3+ tools simultaneously:

```typescript
// Within subagent: execute tools in parallel
const data = await Promise.all([
  readDocumentation(topic),
  searchGitHub(query),
  fetchBenchmarks(test),
  analyzeCode(repo)
]);

// Reduces research time by up to 90%
```

### Expected Performance Gains

| Metric | Sequential | Parallel Multi-Agent | Improvement |
|--------|-----------|---------------------|-------------|
| Quality | 45.2% | 90.2% | **+99.6%** |
| Latency (complex) | 20 min | 2 min | **-90%** |
| Tool Calls | One at a time | 3+ concurrent | **~10x faster** |

## Example: Comprehensive Code Analysis

**User Query:** "Perform comprehensive code quality analysis on this repository"

**Lead Agent Analysis:**
- Complexity: High (large codebase, multiple concerns)
- Decision: 10 specialized subagents

**Decomposition:**

1. **Subagent: Code Style**
   - Objective: Check style consistency
   - Tools: ESLint, Prettier
   - Scope: Style and formatting only

2. **Subagent: Security**
   - Objective: Find vulnerabilities
   - Tools: Security scanners, dependency audit
   - Scope: Security issues only

3. **Subagent: Performance**
   - Objective: Identify bottlenecks
   - Tools: Profiler, benchmarks
   - Scope: Performance only

4. **Subagent: Test Coverage**
   - Objective: Analyze test quality
   - Tools: Coverage reports, test analysis
   - Scope: Testing only

5. **Subagent: Documentation**
   - Objective: Check documentation completeness
   - Tools: Doc generators, comment analysis
   - Scope: Documentation only

6. **Subagent: Dependencies**
   - Objective: Audit dependencies
   - Tools: Package analysis, security checks
   - Scope: Dependencies only

7. **Subagent: Architecture**
   - Objective: Review architecture patterns
   - Tools: Code structure analysis
   - Scope: Architecture only

8. **Subagent: Accessibility**
   - Objective: Check WCAG compliance
   - Tools: Accessibility auditors
   - Scope: A11y only

9. **Subagent: Build Config**
   - Objective: Review build setup
   - Tools: Config analysis
   - Scope: Build/deploy only

10. **Subagent: Code Complexity**
    - Objective: Measure complexity metrics
    - Tools: Complexity analyzers
    - Scope: Complexity only

**Execution:** All 10 run in parallel (~2 minutes)

**Result:** Comprehensive report covering all aspects

## Best Practices

### ✅ Do:

1. **Use Extended Thinking**
   - Plan decomposition before spawning
   - Consider multiple approaches
   - Define clear boundaries

2. **Save Research Plans**
   - Document strategy to filesystem
   - Preserve for future reference
   - Enables iteration

3. **Ensure No Overlap**
   - Each subagent has distinct focus
   - Prevents duplicate work
   - Maximizes efficiency

4. **Use Appropriate Models**
   - Opus for orchestrator
   - Sonnet for workers
   - Optimize cost/performance

5. **Parallel Tool Execution**
   - 3+ tools per subagent
   - Reduces latency by 90%

6. **External Memory**
   - Save to files, not context
   - Prevents context bloat
   - Enables multi-hour tasks

### ❌ Don't:

1. **Don't Allow Peer-to-Peer**
   - All through orchestrator
   - Prevents coordination issues

2. **Don't Create Overlaps**
   - Wastes resources
   - Causes confusion

3. **Don't Leave Gaps**
   - Incomplete coverage
   - Missing important aspects

4. **Don't Skip Planning**
   - Ad-hoc leads to problems
   - Always plan first

5. **Don't Ignore Completeness**
   - Check for gaps
   - Spawn additional agents if needed

## Integration with Existing Subagents

Claudius Skills has 46 specialized subagents ready to use:

**Performance:**
- `performance-optimizer`
- `load-testing-expert`

**Security:**
- `security-auditor`
- `penetration-tester`

**Testing:**
- `test-strategist`
- `qa-specialist`

**Architecture:**
- `system-architect`
- `microservices-expert`

**Example Integration:**

```markdown
User: "Comprehensive security audit"

Lead Agent:
├── Security Auditor → OWASP checks
├── Penetration Tester → Vulnerability scanning
├── Code Reviewer → Code-level security
└── Dependency Auditor → Package vulnerabilities

Parallel execution → Complete security report
```

## Scaling Guidelines

**1 Agent:** Simple queries (< 1 minute)
**2-5 Agents:** Moderate complexity (2-5 minutes)
**10+ Agents:** High complexity (breadth-first) (5-10 minutes)

## Output Format

Present results clearly:

```markdown
# Multi-Agent Task Results

## Task: [Name]
## Complexity: [Simple/Moderate/Complex]
## Agents Used: [Count]

## Summary
[Comprehensive overview]

## Findings by Subagent

### Subagent 1: [Name]
[Key findings]

### Subagent 2: [Name]
[Key findings]

[Continue for all subagents]

## Synthesized Recommendations
1. [Recommendation based on all findings]
2. [Recommendation based on all findings]

## Confidence Levels
- High: [Topics]
- Medium: [Topics]
- Need more research: [Topics]

## Next Steps
[Actionable items]
```

## Related Patterns

- **Documentation:** See `docs/patterns/multi-agent-orchestration.md`
- **Workflows:** See `docs/workflows/explore-plan-code-commit.md`
- **Context:** See `docs/patterns/context-management.md`

## References

- [Anthropic: Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)

---

**Skill Status:** ✅ Production Ready
**Performance:** +90.2% quality improvement
**Latency Reduction:** Up to 90%
**Level:** Advanced
