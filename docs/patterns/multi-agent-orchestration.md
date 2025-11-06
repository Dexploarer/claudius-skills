# Multi-Agent Orchestration Patterns

> **Based on:** [Anthropic's Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system)
>
> **Status:** Production Pattern
> **Level:** Advanced

## Overview

Multi-agent systems use an **orchestrator-worker pattern** where a lead agent coordinates specialized subagents operating in parallel. This architecture avoids bottlenecks present in sequential approaches and enables complex tasks to be decomposed and executed efficiently.

**Key Benefits:**
- 🚀 **90.2% better performance** on complex tasks (Anthropic's research evaluation)
- ⚡ **Parallel execution** reduces latency by up to 90%
- 🎯 **Specialized expertise** with appropriate model tiers
- 🔄 **Clean context windows** for each subagent
- 📊 **Scalable** from simple (1 agent) to complex (10+ agents)

---

## Architecture Pattern

### Orchestrator-Worker Model

```
┌─────────────────────────────────────────────────────────┐
│                   LEAD AGENT (Orchestrator)             │
│                                                          │
│  • Analyzes query                                       │
│  • Develops strategy                                    │
│  • Decomposes into subtasks                            │
│  • Spawns subagents                                     │
│  • Synthesizes results                                  │
│                                                          │
│  Model: Claude Opus 4 (general coordinator)            │
└──────────────┬────────────┬─────────────┬──────────────┘
               │            │             │
               ▼            ▼             ▼
      ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
      │  Subagent 1   │ │  Subagent 2   │ │  Subagent 3   │
      │               │ │               │ │               │
      │  Specialized  │ │  Specialized  │ │  Specialized  │
      │  Task A       │ │  Task B       │ │  Task C       │
      │               │ │               │ │               │
      │  Claude       │ │  Claude       │ │  Claude       │
      │  Sonnet 4     │ │  Sonnet 4     │ │  Sonnet 4     │
      └───────────────┘ └───────────────┘ └───────────────┘
               │            │             │
               └────────────┴─────────────┘
                          │
                          ▼
                   Results Synthesis
```

### Model Tier Strategy

**Lead Agent (Orchestrator):**
- **Model:** Claude Opus 4
- **Role:** General coordination, strategy, synthesis
- **Why:** Needs broad reasoning and decision-making capabilities

**Worker Agents (Specialized):**
- **Model:** Claude Sonnet 4
- **Role:** Focused tasks with clear boundaries
- **Why:** Faster, more cost-effective for specialized work

**Performance:** This combination outperformed single-agent Opus by **90.2%** on breadth-first research queries.

---

## Implementation Pattern

### 1. Task Decomposition

The orchestrator analyzes the query and decomposes it into discrete subtasks:

```markdown
## Lead Agent Prompt Template

You are a lead agent coordinating a multi-agent system.

### Your Responsibilities:
1. Analyze the query for complexity and scope
2. Decompose into discrete, non-overlapping subtasks
3. Define clear boundaries for each subtask
4. Specify output format for each subagent
5. Determine optimal parallelization strategy
6. Synthesize results into coherent response

### Decomposition Guidelines:
- Each subtask must have **explicit boundaries**
- Provide **objective, output format, tools, and sources**
- Avoid task overlap (causes duplicate work)
- Avoid gaps (incomplete coverage)
- Balance load across subagents

### Query Analysis:
[User query here]

### Decomposition:
Create a research plan with:
- Number of subagents needed (1 for simple, 10+ for complex)
- Task specification for each
- Expected output format
- Parallelization strategy
```

**Example Decomposition:**

```
Query: "Analyze React's performance optimizations"

Decomposition:
- Subagent 1: Review React rendering optimizations (useMemo, useCallback)
- Subagent 2: Analyze Virtual DOM and reconciliation
- Subagent 3: Research concurrent features (Suspense, transitions)
- Subagent 4: Investigate production build optimizations
- Subagent 5: Examine profiling and debugging tools

Output: Each subagent returns 1,000-2,000 token summary
Parallelization: All 5 execute simultaneously
```

### 2. Subagent Specification

Each subagent receives detailed instructions:

```markdown
## Subagent Prompt Template

You are a specialized research agent working under a lead coordinator.

### Your Specific Task:
**Objective:** [Clear, focused goal]

**Output Format:**
- 1,000-2,000 token summary
- Key findings with evidence
- Sources used
- Confidence level

**Tools Available:**
[List of relevant tools for this task]

**Sources to Prioritize:**
[Specific documentation, repos, or resources]

**Task Boundaries:**
What to include: [Explicit scope]
What to exclude: [Out of scope]

**Execution:**
1. Use 3+ tools in parallel for efficiency
2. Focus on your specific objective only
3. Do not duplicate work from other subagents
4. Return findings to lead agent for synthesis

### Begin Research:
[Specific query for this subagent]
```

### 3. Communication Flow

**Pattern:** Through orchestrator, **not peer-to-peer**

```
Subagent → Lead Agent (returns findings)
Lead Agent → Synthesis (evaluates completeness)
Lead Agent → User (final response) OR
Lead Agent → New Subagents (if gaps identified)
```

**Anti-pattern:** Direct subagent-to-subagent communication
- Creates coordination complexity
- Loses centralized synthesis
- Hard to track progress

### 4. Parallel Execution

Subagents execute **simultaneously** using parallel tool calls:

```typescript
// Orchestrator spawns subagents in parallel
const results = await Promise.all([
  spawnSubagent('Subagent 1', task1Spec),
  spawnSubagent('Subagent 2', task2Spec),
  spawnSubagent('Subagent 3', task3Spec),
  spawnSubagent('Subagent 4', task4Spec),
  spawnSubagent('Subagent 5', task5Spec)
]);

// Within each subagent, use tools in parallel
const subagentData = await Promise.all([
  readDocs('/react/performance'),
  searchGitHub('react performance issues'),
  fetchBenchmarks('react-benchmarks.json')
]);
```

**Performance Gain:** Up to **90% latency reduction** vs sequential execution

### 5. External Memory

Save research plans and findings to filesystem to avoid context loss:

```markdown
## Memory Pattern

**Before spawning subagents:**
1. Lead agent saves research plan to `RESEARCH_PLAN.md`
2. Saves task specifications to `tasks/` directory
3. Creates `findings/` directory for subagent outputs

**During execution:**
1. Each subagent writes findings to `findings/subagent-{n}.md`
2. Preserves full context without bloating lead agent's window
3. Lead agent reads findings on-demand for synthesis

**Benefits:**
- Multi-hour task coherence
- No information loss during multi-stage processing
- Lead agent maintains clean context
- Subagents return condensed summaries (1,000-2,000 tokens)
```

Example structure:
```
project/
├── RESEARCH_PLAN.md           # Orchestrator's strategy
├── tasks/
│   ├── task-1-spec.md        # Subagent 1 specification
│   ├── task-2-spec.md        # Subagent 2 specification
│   └── ...
└── findings/
    ├── subagent-1-findings.md # Detailed findings
    ├── subagent-2-findings.md
    ├── subagent-3-findings.md
    └── synthesis.md          # Final synthesis
```

---

## Scaling Rules

### Simple Queries (1 agent)
**Characteristics:**
- Straightforward question
- Single domain
- 3-10 tool calls

**Example:** "What's the latest React version?"

**Pattern:** Single agent, no orchestration needed

### Moderate Complexity (2-5 agents)
**Characteristics:**
- Multi-faceted question
- 2-3 domains
- Requires different expertise areas

**Example:** "How do I optimize React app performance?"

**Pattern:**
- Lead agent decomposes into rendering, bundling, profiling
- 3 specialized subagents execute in parallel
- Lead synthesizes recommendations

### High Complexity (10+ agents)
**Characteristics:**
- Breadth-first research
- Multiple domains
- Requires extensive parallel exploration

**Example:** "Comprehensive analysis of modern frontend frameworks"

**Pattern:**
- Lead agent creates detailed research plan
- 10+ subagents each focus on specific aspect
- Parallel execution with 3+ tools per subagent
- Multi-stage synthesis (intermediate → final)

---

## Skill: Multi-Agent Coordinator

Create a skill to guide orchestrator implementation:

```markdown
---
name: multi-agent-coordinator
description: Orchestrate multi-agent systems using lead agent + specialized subagent pattern
trigger: multi agent|orchestrate agents|coordinate subagents|parallel agents
---

# Multi-Agent Coordinator Skill

## Purpose
Guide the implementation of multi-agent systems following Anthropic's orchestrator-worker pattern.

## When to Activate
- Complex queries requiring parallel exploration
- Tasks needing specialized expertise across domains
- Breadth-first research
- Performance-critical workflows

## Workflow

### Step 1: Complexity Analysis
Assess query complexity:
- Simple (1 agent): Straightforward, single domain
- Moderate (2-5 agents): Multi-faceted, 2-3 domains
- Complex (10+ agents): Breadth-first, multiple domains

### Step 2: Decomposition
For moderate/complex:
1. Break into discrete subtasks with clear boundaries
2. Specify objective, output format, tools, sources for each
3. Ensure no overlap or gaps
4. Balance load across subagents

### Step 3: Create Research Plan
Save to `RESEARCH_PLAN.md`:
- Task decomposition
- Subagent specifications
- Parallelization strategy
- Expected outputs

### Step 4: Spawn Subagents
For each subtask:
1. Create task specification in `tasks/task-{n}-spec.md`
2. Spawn subagent with focused prompt
3. Execute in parallel using Promise.all
4. Each subagent writes to `findings/subagent-{n}-findings.md`

### Step 5: Synthesis
1. Read all findings from `findings/` directory
2. Evaluate completeness (any gaps?)
3. Synthesize into coherent response
4. If gaps: spawn additional subagents
5. Final output to user

## Best Practices
- Use Opus for orchestrator, Sonnet for workers
- 3+ tools in parallel per subagent
- Return 1,000-2,000 token summaries from subagents
- Save to filesystem to preserve context
- Clean context windows for each subagent
```

---

## Example: Research Task

### User Query
"Provide comprehensive analysis of authentication methods for modern web apps"

### Lead Agent Decomposition

```markdown
# Research Plan: Modern Web Authentication

## Complexity: High (10+ subagents needed)

## Task Decomposition:

**Subagent 1: Password-Based Auth**
- Objective: Analyze traditional password authentication
- Output: Security considerations, best practices, limitations
- Tools: Search documentation, review security standards
- Scope: Only password-based, exclude MFA

**Subagent 2: Multi-Factor Authentication (MFA)**
- Objective: Review MFA implementations
- Output: Types (TOTP, SMS, hardware keys), security analysis
- Tools: Search standards (FIDO2, WebAuthn)
- Scope: MFA methods, exclude basic passwords

**Subagent 3: OAuth 2.0 / OpenID Connect**
- Objective: Analyze federated identity protocols
- Output: OAuth flows, OIDC integration patterns
- Tools: Review specifications, examine implementations
- Scope: OAuth 2.0 and OIDC only

**Subagent 4: Social Login (Google, Facebook, GitHub)**
- Objective: Evaluate social authentication providers
- Output: Integration patterns, privacy implications, UX
- Tools: Provider documentation, implementation examples
- Scope: Major social providers only

**Subagent 5: Passwordless (Magic Links, WebAuthn)**
- Objective: Analyze passwordless authentication
- Output: Magic link flows, WebAuthn biometrics
- Tools: Standards documentation, browser support
- Scope: Modern passwordless only

**Subagent 6: JSON Web Tokens (JWT)**
- Objective: Token-based session management
- Output: JWT structure, security, refresh patterns
- Tools: JWT.io, security best practices
- Scope: JWT implementation and security

**Subagent 7: Session Management**
- Objective: Server-side session strategies
- Output: Cookie-based, distributed sessions, Redis
- Tools: Framework documentation
- Scope: Session storage and management

**Subagent 8: API Authentication**
- Objective: Securing APIs (API keys, OAuth)
- Output: API auth patterns, rate limiting, scopes
- Tools: API security standards
- Scope: API-specific authentication

**Subagent 9: Security Best Practices**
- Objective: OWASP guidelines, common vulnerabilities
- Output: Security checklist, attack vectors
- Tools: OWASP documentation, security audits
- Scope: Auth-specific security only

**Subagent 10: Framework Implementations**
- Objective: Auth in popular frameworks (Next.js, Django, etc.)
- Output: Library recommendations, integration patterns
- Tools: Framework documentation, auth libraries
- Scope: Top 5 web frameworks

## Parallelization: All 10 execute simultaneously

## Expected Total Time: ~2 minutes (vs 20 minutes sequential)

## Output Format: Each returns 1,500-token summary → Synthesized report
```

### Execution

```typescript
// Lead agent spawns all subagents in parallel
const findings = await Promise.all([
  spawnSubagent('Password-Based Auth', taskSpecs[1]),
  spawnSubagent('MFA', taskSpecs[2]),
  spawnSubagent('OAuth/OIDC', taskSpecs[3]),
  spawnSubagent('Social Login', taskSpecs[4]),
  spawnSubagent('Passwordless', taskSpecs[5]),
  spawnSubagent('JWT', taskSpecs[6]),
  spawnSubagent('Session Mgmt', taskSpecs[7]),
  spawnSubagent('API Auth', taskSpecs[8]),
  spawnSubagent('Security', taskSpecs[9]),
  spawnSubagent('Framework Impls', taskSpecs[10])
]);

// Each subagent uses 3+ tools in parallel
// Example from Subagent 1:
const passwordData = await Promise.all([
  searchDocs('password hashing bcrypt'),
  fetchOWASP('password-storage'),
  readStandard('NIST password guidelines')
]);

// Lead agent synthesizes
const synthesis = synthesizeFindings(findings);
return synthesis; // Comprehensive auth guide
```

### Result
**Time:** ~2 minutes (10 agents in parallel)
**Quality:** 90.2% better than single-agent approach
**Coverage:** Comprehensive across all auth methods

---

## Best Practices

### ✅ Do:

1. **Use Extended Thinking for Planning**
   - Lead agent uses visible thinking to assess tools
   - Determine complexity before spawning subagents
   - Define clear roles and boundaries

2. **Provide Detailed Specifications**
   - Objective, output format, tools, sources
   - Explicit task boundaries (include/exclude)
   - Expected token count for summaries

3. **Save to Filesystem**
   - Research plans before spawning
   - Task specifications for each subagent
   - Findings for preservation

4. **Parallel Tool Execution**
   - Each subagent uses 3+ tools simultaneously
   - Reduces research time by up to 90%

5. **Appropriate Model Tiers**
   - Opus for orchestrator (general reasoning)
   - Sonnet for workers (specialized tasks)

6. **Human Evaluation**
   - Automated systems miss edge cases
   - Review multi-agent outputs for quality

### ❌ Don't:

1. **Don't Allow Peer-to-Peer Communication**
   - All communication through orchestrator
   - Prevents coordination complexity

2. **Don't Create Overlapping Tasks**
   - Causes duplicate work
   - Wastes resources

3. **Don't Leave Gaps**
   - Incomplete coverage from vague boundaries
   - Lead must verify completeness

4. **Don't Use Same Model for All**
   - Opus for workers is overkill
   - Sonnet is faster and cheaper

5. **Don't Skip Research Plan**
   - Ad-hoc decomposition causes gaps
   - Always save plan to filesystem first

6. **Don't Ignore Context Limits**
   - Use external memory (files)
   - Subagents return summaries, not full data

---

## Integration with Claudius Skills

### Existing Multi-Agent Components

**Competitive AI Frameworks:**
- Has coordinator implementations in `frameworks/*/coordinator.ts`
- Bug hunting, code quality, user flow testing
- Already follows orchestrator-worker pattern!

**Subagents (46 total):**
- Performance optimizer, security auditor, test strategist
- Can be used as specialized workers
- Lead agent selects appropriate subagents

**Example Integration:**

```markdown
User: "Perform comprehensive code quality analysis"

Lead Agent:
1. Analyzes repository complexity → High (10+ files)
2. Decomposes into:
   - Code style consistency
   - Security vulnerabilities
   - Performance bottlenecks
   - Test coverage
   - Documentation quality
3. Spawns specialized subagents:
   - `code-quality-analyzer` → Style
   - `security-auditor` → Vulnerabilities
   - `performance-optimizer` → Bottlenecks
   - `test-strategist` → Coverage
   - `documentation-generator` → Docs
4. Synthesizes findings into comprehensive report
```

---

## Performance Metrics

Based on Anthropic's research evaluation:

| Metric | Single Agent | Multi-Agent | Improvement |
|--------|-------------|-------------|-------------|
| Quality Score | 45.2% | 90.2% | **+99.6%** |
| Latency (complex) | 20 min | 2 min | **-90%** |
| Tool Calls | Sequential | 3+ parallel | **~10x faster** |
| Context Efficiency | Bloated | Clean per agent | **Better** |

---

## Related Patterns

- **Context Engineering:** See `docs/patterns/context-management.md`
- **Tool Design:** See `docs/patterns/tool-design-principles.md`
- **Workflows:** See `docs/workflows/explore-plan-code-commit.md`
- **Skills:** See `.claude/skills/multi-agent-coordinator.md`

---

## References

- [Anthropic: Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
- [Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

---

**Pattern Status:** ✅ Production Ready
**Compliance:** Anthropic Standard
**Performance:** +90.2% quality improvement
**Level:** Advanced
