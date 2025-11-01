# Complete Setup Templates

Production-ready complete configurations for different project types.

## Available Setups

### Frontend Setup (`frontend/`)
Complete React/TypeScript frontend development environment

**Includes:**
- React component generation skill
- TypeScript strict mode
- ESLint + Prettier hooks
- Component testing setup
- Build optimization commands
- Deployment workflow

**Best for:** React, Vue, Angular, Svelte projects

### Backend Setup (`backend/`)
Complete Node.js/Express API development environment

**Includes:**
- CRUD generator skill
- API endpoint scaffolding
- Database migration commands
- Test suite generation
- Docker configuration
- CI/CD pipeline

**Best for:** Node.js, Python (FastAPI), Java (Spring Boot) APIs

### Fullstack Setup (`fullstack/`)
Complete MERN/MEAN/PERN stack environment

**Includes:**
- Everything from frontend + backend
- Monorepo configuration
- Shared type definitions
- End-to-end testing
- Full deployment pipeline
- Database + API + Frontend coordination

**Best for:** Full-stack applications, startups, MVPs

## Quick Start

```bash
# Choose your setup
cd templates/complete-setups/frontend

# Copy to your project
cp -r .claude ~/my-project/
cp -r .mcp.json ~/my-project/ (optional)

# Install and test
cd ~/my-project
claude
```

## What's Included

Each setup contains:
- `.claude/skills/` - Pre-configured skills
- `.claude/commands/` - Workflow commands
- `.claude/agents/` - Specialized subagents
- `.claude/settings.json` - Hooks configuration
- `.mcp.json.template` - MCP server config template
- `README.md` - Setup-specific documentation

## Customization

All setups are templates - customize for your needs:
1. Copy to your project
2. Review each file
3. Modify for your stack/preferences
4. Test thoroughly
5. Commit to your repo

## See Also

- Individual templates in `/templates`
- Examples in `/examples`
- Starter kits in `/starter-kit`
