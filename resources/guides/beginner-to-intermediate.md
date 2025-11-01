# From Beginner to Intermediate: Your Learning Path

A comprehensive guide to progressing from beginner to intermediate Claude Code proficiency.

## 🎯 Where You Are Now

**Beginner Level:**
- ✅ Completed starter-kit setup
- ✅ Understand the five pillars
- ✅ Created basic skills and commands
- ✅ Set up simple hooks
- ✅ Used subagents
- ✅ Connected MCP servers

**Ready to level up?** Let's go! 🚀

## 📊 Beginner vs Intermediate

| Aspect | Beginner | Intermediate |
|--------|----------|--------------|
| **Skills** | Generic, simple | Framework-specific |
| **Commands** | Single-step | Multi-step workflows |
| **Hooks** | Safety checks | Quality enforcement |
| **Subagents** | General helpers | Domain experts |
| **MCP** | Basic servers | Custom integrations |
| **Integration** | Individual pillars | Combined workflows |

## 🗺️ Your Learning Path

### Phase 1: Deepen Pillar Knowledge (Weeks 1-2)

#### Skills: From Generic to Specialized

**What you know:**
```markdown
---
name: code-explainer
description: Explains code when asked
allowed-tools: [Read]
---
```

**Level up to:**
```markdown
---
name: react-component-generator
description: Generates React components with TypeScript, hooks, tests
allowed-tools: [Read, Write, Grep, Glob]
---

# React Component Generator

Expert at creating production-ready React components.

## Component Patterns
- Functional components with hooks
- TypeScript interfaces
- CSS Modules
- React Testing Library tests
- Proper prop validation

## Best Practices
[Framework-specific guidelines]
```

**Action Items:**
- [ ] Create a framework-specific skill for your stack
- [ ] Add file structure conventions
- [ ] Include testing patterns
- [ ] Enforce team style guides

**Example:** [React Component Generator](../examples/intermediate/framework-skills/react-component-generator/)

#### Commands: From Simple to Workflows

**What you know:**
```markdown
Run a single git command or simple task
```

**Level up to:**
```markdown
# Complete Feature Workflow

1. Create feature branch
2. Implement with tests
3. Review code
4. Generate commit message
5. Create PR with description
6. Deploy to staging
7. Track in project management
```

**Action Items:**
- [ ] Chain multiple operations
- [ ] Add validation steps
- [ ] Include error handling
- [ ] Integrate with external tools

**Example:** [PR Creator](../examples/intermediate/workflow-commands/pr-creator/)

#### Hooks: From Safety to Quality

**What you know:**
```bash
# Block commits with console.log
if grep -r "console.log" .; then
  exit 1
fi
```

**Level up to:**
```bash
# Comprehensive pre-commit quality
1. Run linters (ESLint, Prettier)
2. Execute affected tests
3. Check code coverage
4. Validate commit message format
5. Ensure tests exist for changes
6. Scan for security issues
```

**Action Items:**
- [ ] Integrate linting tools
- [ ] Add test enforcement
- [ ] Include coverage checks
- [ ] Implement custom validations

**Example:** [Pre-Commit Lint Hook](../examples/intermediate/advanced-hooks/pre-commit-lint/)

#### Subagents: From Helpers to Experts

**What you know:**
```markdown
---
name: code-reviewer
description: Reviews code for issues
allowed-tools: [Read]
---

Review this code and find problems.
```

**Level up to:**
```markdown
---
name: api-designer
description: Designs RESTful APIs with OpenAPI specs
allowed-tools: [Read, Write, Grep]
---

# API Designer

Domain expert in REST API design.

## Expertise
- RESTful conventions
- HTTP method selection
- Status code usage
- Request/response schemas
- Error handling patterns
- OpenAPI specification
- Security best practices
- Versioning strategies

## Deliverables
- Complete API specification
- Request/response examples
- Error scenarios
- Authentication flow
- Rate limiting design
```

**Action Items:**
- [ ] Create domain-specific subagents
- [ ] Add deep expertise to prompts
- [ ] Define clear deliverables
- [ ] Include industry standards

**Example:** [API Designer Subagent](../examples/intermediate/domain-subagents/api-designer/)

#### MCP: From Using to Integrating

**What you know:**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    }
  }
}
```

**Level up to:**
```markdown
# Integrated Workflow with Multiple MCP Servers

1. GitHub MCP: Fetch issues
2. Memory MCP: Store analysis
3. SQLite MCP: Track metrics
4. Slack MCP: Notify team

# Create custom MCP server for internal APIs
# Combine servers in workflows
# Build persistent knowledge bases
```

**Action Items:**
- [ ] Use 3+ MCP servers together
- [ ] Build workflows combining MCP
- [ ] Create custom MCP servers
- [ ] Integrate with internal tools

**Example:** [MCP Workflow Tutorial](../examples/beginner/tutorials/mcp-workflow.md)

### Phase 2: Framework Specialization (Weeks 3-4)

#### Choose Your Focus

Pick 1-2 frameworks/domains you work with most:

**Frontend Options:**
- React/Vue/Angular/Svelte
- TypeScript patterns
- State management (Redux, Zustand)
- Component libraries
- Testing (Jest, Vitest, Cypress)

**Backend Options:**
- Django/Flask/FastAPI (Python)
- Express/Nest.js (Node.js)
- Ruby on Rails
- Spring Boot (Java)
- API design patterns

**DevOps/Infrastructure:**
- Docker/Kubernetes
- CI/CD (GitHub Actions, GitLab)
- AWS/GCP/Azure
- Terraform/Ansible
- Monitoring (Prometheus, Grafana)

#### Build Framework-Specific Tools

**React Developer Example:**

```
1. react-component-generator skill
2. storybook-story-generator skill
3. /component command (component + test + story)
4. /refactor-to-hooks command
5. react-best-practices subagent
6. component-accessibility subagent
7. pre-commit: check for deprecated APIs
8. test-enforcement: require tests for components
```

**Action Items:**
- [ ] Create 2-3 framework-specific skills
- [ ] Build 2-3 workflow commands
- [ ] Add framework-specific hooks
- [ ] Create expert subagents

#### Real Project Integration

Apply to actual work:

**Week 1: Set Up**
- Install in work project
- Create basic framework tools
- Test with small tasks

**Week 2: Build**
- Add team-specific patterns
- Create project workflows
- Integrate with existing tools

**Week 3: Refine**
- Get team feedback
- Optimize slow operations
- Document for teammates

**Week 4: Expand**
- Add advanced features
- Create more subagents
- Build complete workflows

### Phase 3: Workflow Integration (Weeks 5-6)

#### Combine All Five Pillars

**Complete Feature Development:**

```
1. Start: /start-feature user-authentication
   └─ Command creates branch, sets up tracking

2. Develop: "Build login endpoint"
   └─ Skill: api-endpoint-generator activates
   └─ Generates: route, controller, validation, tests

3. Test: Automatic
   └─ Hook: test-enforcement runs on save
   └─ Validates coverage threshold

4. Review: "Review this code"
   └─ Subagent: security-auditor checks for vulnerabilities
   └─ Subagent: code-reviewer checks quality

5. Commit: Automatic
   └─ Hook: pre-commit-lint runs ESLint, Prettier
   └─ Subagent: commit-message-generator creates message

6. PR: /create-pr
   └─ Command analyzes changes
   └─ Generates description
   └─ Creates PR via GitHub MCP

7. Track: Automatic
   └─ Memory MCP stores feature progress
   └─ Slack MCP notifies team
```

**Action Items:**
- [ ] Map your complete workflow
- [ ] Identify automation opportunities
- [ ] Create integrated commands
- [ ] Test end-to-end flow

#### Build Team-Wide Configurations

Share with your team:

```
your-project/
├── .claude/
│   ├── skills/
│   │   ├── react-component.md
│   │   ├── api-endpoint.md
│   │   └── test-generator.md
│   ├── commands/
│   │   ├── start-feature.md
│   │   ├── finish-feature.md
│   │   └── deploy.md
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   ├── security-auditor.md
│   │   └── api-designer.md
│   ├── hooks/
│   │   └── pre-commit.sh
│   └── settings.json
├── .mcp.json
└── README-CLAUDE.md  # Team documentation
```

**Document for team:**
- When to use each skill/command
- Required MCP server setup
- Hook behavior explanation
- Best practices guide

## 📚 Study Plan

### Week-by-Week Breakdown

#### Week 1-2: Framework Deep Dive
- **Monday-Tuesday:** Study framework-specific skill examples
- **Wednesday-Thursday:** Create your first framework skill
- **Friday:** Test and refine
- **Weekend:** Read intermediate examples, plan next week

#### Week 3-4: Workflow Building
- **Monday-Tuesday:** Map your current development workflow
- **Wednesday-Thursday:** Build multi-step commands
- **Friday:** Integrate with hooks
- **Weekend:** Review and optimize

#### Week 5-6: Integration & Sharing
- **Monday-Tuesday:** Combine all pillars
- **Wednesday-Thursday:** Test complete workflows
- **Friday:** Document for team
- **Weekend:** Gather feedback, plan improvements

## 🎓 Learning Resources

### Must-Read Examples

**Skills:**
- [React Component Generator](../examples/intermediate/framework-skills/react-component-generator/)
- [Django Model Helper](../examples/intermediate/framework-skills/django-model-helper/)

**Commands:**
- [PR Creator](../examples/intermediate/workflow-commands/pr-creator/)
- [Deploy Script](../examples/intermediate/workflow-commands/deploy-script/)

**Hooks:**
- [Pre-Commit Lint](../examples/intermediate/advanced-hooks/pre-commit-lint/)
- [Test Enforcement](../examples/intermediate/advanced-hooks/test-enforcement/)

**Subagents:**
- [API Designer](../examples/intermediate/domain-subagents/api-designer/)
- [Database Architect](../examples/intermediate/domain-subagents/database-architect/)

### Practice Projects

#### Project 1: Personal Blog Platform
Build complete Claude Code setup for a blog:
- Post creation skill
- Admin command workflow
- Pre-publish hooks
- SEO review subagent
- GitHub + Memory MCP

**Difficulty:** Medium
**Time:** 2-3 days

#### Project 2: E-Commerce API
Create API development environment:
- API endpoint generator skill
- Database migration commands
- Security validation hooks
- API designer subagent
- PostgreSQL MCP integration

**Difficulty:** Hard
**Time:** 4-5 days

#### Project 3: Team Workflow Automation
Build complete CI/CD integration:
- Feature workflow commands
- Code quality hooks
- Multiple review subagents
- Full MCP integration (GitHub, Slack, Jira)

**Difficulty:** Expert
**Time:** 1 week

## ✅ Readiness Checklist

You're ready for intermediate level when you can:

### Skills
- [ ] Create framework-specific skills
- [ ] Include file organization patterns
- [ ] Add language/framework best practices
- [ ] Generate multiple related files
- [ ] Enforce team conventions

### Commands
- [ ] Build multi-step workflows
- [ ] Add error handling and validation
- [ ] Integrate with external tools
- [ ] Create environment-aware commands
- [ ] Chain commands together

### Hooks
- [ ] Integrate linting tools
- [ ] Run tests automatically
- [ ] Check code coverage
- [ ] Validate multiple conditions
- [ ] Provide actionable error messages

### Subagents
- [ ] Create domain-specific experts
- [ ] Define clear deliverables
- [ ] Add industry best practices
- [ ] Restrict tools appropriately
- [ ] Format output consistently

### MCP
- [ ] Use 3+ servers simultaneously
- [ ] Create integrated workflows
- [ ] Store persistent knowledge
- [ ] Build cross-service automations

### Integration
- [ ] Combine all five pillars
- [ ] Create end-to-end workflows
- [ ] Share configurations with team
- [ ] Document for others
- [ ] Optimize for performance

## 🚀 Next Steps

### This Week
1. Pick one framework/domain to specialize in
2. Create your first framework-specific skill
3. Build a multi-step command
4. Add a quality enforcement hook

### This Month
1. Complete all intermediate examples for your domain
2. Build 2-3 complete workflows
3. Integrate 3+ MCP servers
4. Share with your team

### This Quarter
1. Build team-wide configuration
2. Create custom MCP server
3. Contribute examples back to community
4. Help other developers learn

## 🎯 Success Metrics

You're intermediate when:
- ✅ You have framework-specific tools
- ✅ Your workflow is mostly automated
- ✅ You use multiple pillars together
- ✅ Your team uses your configurations
- ✅ You rarely do manual repetitive tasks
- ✅ You can create complex integrations
- ✅ You contribute back to community

## 💡 Pro Tips

1. **Start small** - Don't rebuild everything at once
2. **Test thoroughly** - Broken automation is worse than none
3. **Document well** - Your future self will thank you
4. **Share early** - Get feedback from teammates
5. **Iterate often** - Refine based on actual usage
6. **Stay focused** - Master your stack before expanding
7. **Give back** - Share your best examples

## 📞 Need Help?

- **Stuck on something?** Review the troubleshooting sections in examples
- **Want inspiration?** Browse intermediate-kit for complete setup
- **Have questions?** Ask in GitHub Discussions
- **Found a better way?** Contribute back!

## 🎉 Congratulations!

You're on the path from beginner to intermediate. Take it step by step, practice regularly, and you'll be building advanced Claude Code workflows in no time!

**Remember:** The goal isn't perfection—it's continuous improvement and practical automation that makes your development work more enjoyable and productive.

**Happy coding!** 🚀

---

*Next: Check out [Intermediate Kit](../../intermediate-kit/) for a complete production-ready setup!*
