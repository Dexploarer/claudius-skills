# Workflow Commands - Intermediate Examples

Production-grade slash commands for real development workflows.

## What Are Workflow Commands?

Workflow commands are manual shortcuts for complex, multi-step tasks that developers perform repeatedly in professional environments.

## Available Examples

### PR Creator
- **File**: `pr-creator/command.md`
- **Usage**: `/pr-creator [base-branch]`
- **Purpose**: Create pull requests with auto-generated descriptions
- **Features**:
  - Analyzes commits since branching
  - Generates PR title and description
  - Creates checklist
  - Uses GitHub CLI

### Deploy Script
- **File**: `deploy-script/command.md`
- **Usage**: `/deploy [environment]`
- **Purpose**: Deploy applications with safety checks
- **Features**:
  - Pre-deployment validation
  - Runs tests and linting
  - Environment-specific deployment
  - Post-deployment health checks

## How to Use

1. **Copy to your project**:
   ```bash
   cp examples/intermediate/workflow-commands/pr-creator/command.md \
      .claude/commands/pr-creator.md
   ```

2. **Run the command**:
   ```bash
   /pr-creator main
   ```

3. **Claude executes the workflow**

## Command Patterns

### Validation → Action → Verification
```bash
# 1. Validate inputs and state
check_git_status
validate_environment

# 2. Perform action
run_deployment

# 3. Verify success
health_check
post_deploy_tests
```

### Multi-Step Workflows
```bash
# Chain multiple operations
/version-bump minor
/changelog-update
/pr-creator
```

## Creating Your Own Workflow Command

```markdown
# File: .claude/commands/my-workflow.md

Execute [task description] with [specific steps].

## Instructions

### 1. Pre-flight Checks
- Validate prerequisites
- Check current state

### 2. Main Operations
```bash
# Step 1
command_1

# Step 2
command_2
\```

### 3. Verification
- Confirm success
- Report status
```

## Best Practices

- Validate inputs and state
- Provide clear feedback
- Handle errors gracefully
- Include rollback procedures
- Log important operations
- Confirm dangerous actions
- Report final status
- Document environment variables

## Common Workflow Patterns

### Deployment
- Validate → Build → Test → Deploy → Verify

### Release
- Version → Changelog → Tag → Build → Publish

### Database
- Backup → Migrate → Verify → Cleanup

### Testing
- Build → Lint → Test → Coverage → Report

## See Also

- [Intermediate Kit](../../../intermediate-kit/) - Complete setup
- [Templates](../../../templates/) - Command templates
- [Best Practices](../../../resources/guides/best-practices.md)
