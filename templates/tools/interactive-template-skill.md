---
name: interactive-template-generator
description: Interactively guide users through selecting and customizing Claude Code templates when they ask to "generate a template" or "create a new skill/command/agent"
allowed-tools: [Read, Write, Edit, Grep, Glob]
---

# Interactive Template Generator Skill

Guide users through an interactive process to select, customize, and generate Claude Code configurations.

## Activation Triggers

This skill activates when users say:
- "generate a template"
- "create a new skill"
- "create a new command"
- "create a new subagent"
- "help me set up a Claude Code configuration"
- "what template should I use?"

## Instructions

When this skill is activated, follow this interactive process:

### Step 1: Identify What They Need

Ask the user what they want to create:

```
I can help you create:

1. **Skill** - Auto-triggered functionality based on user requests
2. **Command** - Explicit slash commands (e.g., /deploy)
3. **Subagent** - Specialized background workers
4. **Hook** - Event-driven automation
5. **MCP Configuration** - External service integration
6. **Complete Setup** - Full project configuration
7. **Language Service** - Go/Rust/PHP service generator
8. **GitHub Workflow** - CI/CD automation

What would you like to create?
```

### Step 2: Gather Requirements Based on Type

#### For Skills:

Ask these questions:
1. **Level**: "What complexity level?"
   - Beginner (simple, focused tasks like formatters)
   - Intermediate (framework-specific like React generators)
   - Advanced (full-stack features)

2. **Name**: "What should the skill be called? (use kebab-case)"

3. **Description**: "When should this activate? Be specific about the trigger phrases."

4. **Tools**: "Which tools does it need?"
   - Read-only: Read, Grep, Glob
   - Code generation: Read, Write, Edit, Grep, Glob
   - Full access: Read, Write, Edit, Bash, Grep, Glob, Task

5. **Purpose**: "What will this skill do?"

Then:
- Copy the appropriate template (beginner/intermediate/advanced)
- Customize the frontmatter with name, description, tools
- Save to `.claude/skills/{name}.md`
- Provide next steps for customization

#### For Commands:

Ask these questions:
1. **Type**: "What kind of command?"
   - Basic (single operation, quick execution)
   - Workflow (multi-step, with rollback/validation)

2. **Name**: "What should the command be called? (without /)"

3. **Description**: "What does this command do?"

4. **Options**: "Does it need options? (e.g., --dry-run, --env, --force)"

Then:
- Copy the appropriate template
- Customize with name and description
- Save to `.claude/commands/{name}.md`
- Provide usage example: `/{name}`

#### For Subagents:

Ask these questions:
1. **Role**: "What role should the subagent have?"
   - Analyzer (read-only, review/audit)
   - Generator (create files and code)
   - Domain Expert (specialized knowledge)

2. **Name**: "What should the subagent be called?"

3. **Expertise**: "What domain expertise should it have?"

4. **Tools**: Based on role, suggest appropriate tools

Then:
- Copy the appropriate template
- Customize with name, description, expertise
- Save to `.claude/agents/{name}.md`
- Provide usage example: `"use the {name} subagent to..."`

#### For Language Services:

Ask these questions:
1. **Language**: "Which language?"
   - Go
   - Rust
   - PHP (Laravel)

2. **Service name**: "What should the service be called?"

3. **Resource**: "What entity will it manage?" (e.g., users, products, orders)

4. **Database**: "Which database?" (PostgreSQL, MySQL, SQLite)

Then:
- Read the appropriate language template
- Explain what will be generated
- Provide the exact phrase to use for generation
- Show project structure that will be created

#### For GitHub Workflows:

Ask these questions:
1. **Purpose**: "What should the workflow do?"
   - CI (testing, linting)
   - CD (deployment)
   - Security scanning
   - Release automation
   - Performance testing

2. **Technology**: "What's your tech stack?"
   - Node.js
   - Python
   - Go
   - Rust
   - PHP

3. **Triggers**: "When should it run?"
   - On push to specific branches
   - On pull requests
   - On schedule
   - Manual trigger

Then:
- Read the GitHub workflow template
- Show relevant workflow examples
- Explain required secrets
- Provide customization points

### Step 3: Generate the Configuration

After gathering requirements:

1. **Copy the template** from the appropriate location:
   - Skills: `templates/skills/{level}-skill-template.md`
   - Commands: `templates/commands/{type}-command-template.md`
   - Subagents: `templates/subagents/{role}-template.md`

2. **Customize the frontmatter**:
   ```yaml
   ---
   name: {user-provided-name}
   description: {user-provided-description}
   allowed-tools: [{user-selected-tools}]
   ---
   ```

3. **Save to the correct location**:
   - Skills: `.claude/skills/{name}.md`
   - Commands: `.claude/commands/{name}.md`
   - Subagents: `.claude/agents/{name}.md`

4. **Create directories if needed**: Use Write tool to create parent directories

### Step 4: Provide Next Steps

After generation, tell the user:

```
✅ Created {type}: .claude/{type}s/{name}.md

📝 Next steps:
1. Review the generated file
2. Customize the instructions for your specific use case
3. Add examples relevant to your project
4. Test the {type}:
   {usage-example}

💡 Tips:
- Read through the template comments for guidance
- Start simple and add complexity as needed
- Test with different phrasings to ensure it activates correctly

Need help customizing? Just ask!
```

### Step 5: Offer Customization Help

If the user asks for help customizing:

1. **Read the generated file** to see what was created

2. **Ask specific questions**:
   - "What specific functionality do you want to add?"
   - "Do you have an example of what you want it to generate?"
   - "Are there any specific frameworks or libraries to integrate?"

3. **Provide concrete examples** based on their responses

4. **Edit the file** to add the customizations

## Examples

### Example 1: Creating a Beginner Skill

```
User: "I want to create a skill for formatting JSON files"