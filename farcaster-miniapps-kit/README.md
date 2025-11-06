# Farcaster Miniapps Kit

> **Production-ready extensibility kit for building Farcaster miniapps with Claude Code**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D22.11.0-brightgreen)](https://nodejs.org/)

A comprehensive collection of skills, commands, agents, and rules for building Farcaster miniapps using Claude Code. This kit provides everything you need to create native-like apps that integrate seamlessly with the Farcaster social protocol.

## 📋 Table of Contents

- [Features](#features)
- [What's Included](#whats-included)
- [Quick Start](#quick-start)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Skills Reference](#skills-reference)
- [Commands Reference](#commands-reference)
- [Agents Reference](#agents-reference)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **🎯 6 Core Skills**: Complete miniapp development lifecycle
- **⚡ 8 Slash Commands**: Quick workflow shortcuts
- **🤖 4 Specialized Agents**: Expert consultants for architecture, auth, wallets, and debugging
- **🔒 4 Safety Hooks**: Validation and best practice enforcement
- **📚 Framework Rules**: Farcaster-specific patterns and guidelines
- **🎨 Production-Ready**: Battle-tested patterns and security best practices

## 📦 What's Included

### Skills (6)

1. **miniapp-generator** - Scaffold new Farcaster miniapps with proper structure
2. **manifest-builder** - Create and configure `/.well-known/farcaster.json` manifests
3. **embed-creator** - Build shareable `fc:miniapp` embeds for rich social cards
4. **sdk-integration** - Integrate @farcaster/miniapp-sdk for auth and actions
5. **notification-system** - Implement push notifications with webhooks
6. **wallet-integration** - Add Ethereum and Solana wallet support

### Slash Commands (8)

- `/new-miniapp` - Create new miniapp project
- `/add-manifest` - Add manifest configuration
- `/add-embed` - Create embed for page
- `/setup-auth` - Setup Quick Auth
- `/add-notifications` - Add notification system
- `/add-wallet` - Integrate wallet
- `/deploy-miniapp` - Deploy to production
- `/debug-miniapp` - Debug common issues

### Agents (4)

- **miniapp-architect** - Architecture and design consultant
- **authentication-specialist** - Auth implementation expert
- **wallet-consultant** - Web3 wallet integration expert
- **debugging-expert** - Troubleshooting specialist

### Hooks (4)

- **manifest-validation** - Validate manifest before deployment
- **sdk-ready-check** - Ensure `sdk.actions.ready()` is called
- **https-url-check** - Enforce HTTPS URLs (no tunnel URLs in production)
- **node-version-check** - Verify Node.js 22.11.0+ requirement

### Framework Rules

- Farcaster miniapps framework patterns
- SDK integration guidelines
- Security best practices
- Performance optimization

## 🚀 Quick Start

### 1. Copy the Kit

```bash
# Copy to your project
cp -r farcaster-miniapps-kit/.claude /path/to/your/project/

# Or use for learning
cd farcaster-miniapps-kit
```

### 2. Create Your First Miniapp

```bash
# Use Claude Code with the new-miniapp command
/new-miniapp
```

### 3. Add Features

```bash
# Add manifest
/add-manifest

# Setup authentication
/setup-auth

# Add wallet integration
/add-wallet
```

## 📋 Requirements

### Minimum Requirements

- **Node.js**: 22.11.0 or higher (REQUIRED by @farcaster/miniapp-sdk)
- **npm/pnpm/yarn**: Latest version recommended
- **Claude Code**: Latest version

### Development Requirements

- **HTTPS**: Production deployments require HTTPS domains
- **Tunneling Tool**: ngrok or cloudflared for local development
- **Warpcast Account**: For developer tools access

### Optional

- **TypeScript**: Recommended for type safety
- **Next.js**: Recommended framework (App Router preferred)
- **Prisma**: For database management (if using notifications/auth)

## 💿 Installation

### Option 1: Use in Existing Project

```bash
# Navigate to your project
cd my-project

# Copy the .claude directory
cp -r /path/to/farcaster-miniapps-kit/.claude .

# Restart Claude Code
```

### Option 2: Start New Project

```bash
# Use the miniapp-generator skill
# Claude Code will prompt you through setup
```

### Option 3: Clone and Explore

```bash
git clone https://github.com/your-repo/farcaster-miniapps-kit
cd farcaster-miniapps-kit

# Explore skills, commands, and agents
ls -la .claude/
```

## 📖 Usage

### Using Skills

Skills activate automatically based on your requests:

```
You: "Create a new Farcaster miniapp for a game"
Claude: [Activates miniapp-generator skill]

You: "Add a manifest file"
Claude: [Activates manifest-builder skill]

You: "Integrate Ethereum wallet"
Claude: [Activates wallet-integration skill]
```

### Using Commands

Commands provide quick workflows:

```
/new-miniapp          # Start new project
/add-manifest         # Configure manifest
/add-embed           # Create embed
/setup-auth          # Setup authentication
/add-notifications   # Add notifications
/add-wallet          # Integrate wallet
/deploy-miniapp      # Deploy to production
/debug-miniapp       # Troubleshoot issues
```

### Using Agents

Agents provide specialized expertise:

```
You: "How should I architect a real-time game miniapp?"
Claude: [Consults miniapp-architect agent]

You: "Help me debug why notifications aren't sending"
Claude: [Consults debugging-expert agent]

You: "What's the best way to handle wallet transactions?"
Claude: [Consults wallet-consultant agent]
```

## 🎯 Skills Reference

### 1. miniapp-generator

**Purpose**: Scaffold new Farcaster miniapps

**Activation**: "create farcaster miniapp", "new miniapp project"

**Features**:
- Official CLI integration
- Framework selection
- SDK setup
- Development environment configuration
- Best practices enforcement

**Output**: Complete project structure with:
- SDK integration
- MiniAppProvider component
- Manifest configuration
- TypeScript setup
- Development scripts

### 2. manifest-builder

**Purpose**: Create and configure manifest files

**Activation**: "create manifest", "setup manifest"

**Features**:
- Manifest route generation
- Account association signing
- Environment variable setup
- Image asset configuration
- Validation tools

**Output**:
- `minikit.config.ts`
- Manifest API route
- Environment variables template
- Warpcast integration guide

### 3. embed-creator

**Purpose**: Create shareable embeds

**Activation**: "create embed", "make page shareable"

**Features**:
- Embed metadata generation
- OG image configuration
- Dynamic embed creation
- Deep linking support
- Testing tools

**Output**:
- Embed utility functions
- Page metadata configuration
- OG image setup
- Preview testing guide

### 4. sdk-integration

**Purpose**: Integrate Farcaster SDK

**Activation**: "integrate sdk", "setup farcaster sdk"

**Features**:
- SDK initialization
- Context access
- Quick Auth implementation
- Action triggers
- Capability detection

**Output**:
- SDK initialization module
- Provider components
- Authentication flows
- Action handlers

### 5. notification-system

**Purpose**: Implement push notifications

**Activation**: "add notifications", "setup notifications"

**Features**:
- Webhook handler
- Notification service
- Credential management
- Rate limiting
- Analytics tracking

**Output**:
- Webhook endpoint
- Notification service
- Database schema
- Rate limiter
- Usage examples

### 6. wallet-integration

**Purpose**: Add blockchain wallet support

**Activation**: "integrate wallet", "add ethereum wallet"

**Features**:
- Ethereum provider (EIP-1193)
- Solana provider
- Smart contract interaction
- Transaction management
- Multi-chain support

**Output**:
- Wallet service classes
- Provider wrappers
- Contract interfaces
- Transaction handlers
- Security patterns

## ⚡ Commands Reference

| Command | Purpose | Quick Description |
|---------|---------|-------------------|
| `/new-miniapp` | Create project | Scaffold new Farcaster miniapp |
| `/add-manifest` | Add manifest | Configure `/.well-known/farcaster.json` |
| `/add-embed` | Create embed | Make pages shareable as rich cards |
| `/setup-auth` | Setup auth | Implement Quick Auth |
| `/add-notifications` | Add notifications | Setup push notifications |
| `/add-wallet` | Add wallet | Integrate Ethereum/Solana |
| `/deploy-miniapp` | Deploy | Deploy to production |
| `/debug-miniapp` | Debug | Troubleshoot common issues |

## 🤖 Agents Reference

### miniapp-architect

**Expertise**: Architecture, design patterns, scalability

**Use When**:
- Planning new miniapp
- Redesigning architecture
- Choosing tech stack
- Optimizing performance
- Designing data flows

**Key Recommendations**:
- Feature-based organization
- Provider pattern for state
- Security-first design
- Performance optimization
- Framework-specific patterns

### authentication-specialist

**Expertise**: Auth implementation, JWT, session management

**Use When**:
- Implementing authentication
- Securing API endpoints
- Managing sessions
- Troubleshooting auth
- Designing authorization

**Key Recommendations**:
- Quick Auth with verification
- Secure session management
- CSRF protection
- Rate limiting
- Role-based access control

### wallet-consultant

**Expertise**: Web3 wallets, smart contracts, transactions

**Use When**:
- Implementing wallet connections
- Adding on-chain features
- Integrating contracts
- Supporting multi-chain
- Optimizing gas costs

**Key Recommendations**:
- EIP-1193 compliance
- Input validation
- Transaction confirmation
- Error handling
- Multi-chain support

### debugging-expert

**Expertise**: Troubleshooting, performance, error resolution

**Use When**:
- App stuck loading
- SDK errors
- Manifest issues
- Wallet failures
- Performance problems

**Key Recommendations**:
- Systematic debugging
- Logging strategies
- Error boundaries
- Performance profiling
- Testing workflows

## ✅ Best Practices

### Critical Requirements

#### 1. Always Call `sdk.actions.ready()` ⚠️

**MOST COMMON ISSUE**: Forgetting this causes infinite loading screen

```typescript
// ✅ CORRECT
useEffect(() => {
  async function init() {
    await new Promise<void>(resolve => {
      if (document.readyState === 'complete') resolve();
      else window.addEventListener('load', () => resolve());
    });

    await sdk.actions.ready(); // CRITICAL!
  }
  init();
}, []);
```

#### 2. HTTPS URLs Only (Production)

```typescript
// ✅ Production
homeUrl: 'https://myapp.com'

// ❌ Development only (will fail in prod)
homeUrl: 'https://abc-123.ngrok.io'
```

#### 3. Never Trust Context Data

```typescript
// ❌ WRONG - Can be spoofed
if (context.user?.fid === ADMIN_FID) { /* Insecure! */ }

// ✅ CORRECT - Use authenticated token
const token = await quickAuth.getToken();
// Verify on backend
```

#### 4. Node.js Version

```bash
# REQUIRED: 22.11.0 or higher
node --version  # Should be v22.11.0+
```

### Security

- Verify all tokens on backend
- Validate user inputs
- Use HTTPS in production
- Implement rate limiting
- Follow CORS best practices

### Performance

- Call `ready()` quickly
- Optimize images
- Code split heavy features
- Cache when appropriate
- Monitor bundle size

### Testing

- Test in Warpcast preview tool
- Use tunnel for local testing
- Validate manifest with audit tool
- Test all user flows
- Check error scenarios

## 🐛 Troubleshooting

### Common Issues

#### Infinite Loading Screen

**Problem**: App never loads

**Solution**: Ensure `sdk.actions.ready()` is called after page loads

```typescript
await sdk.actions.ready(); // Don't forget this!
```

#### Manifest Not Found

**Problem**: `/.well-known/farcaster.json` returns 404

**Solution**: Check route path

```
Next.js App Router:
app/.well-known/farcaster.json/route.ts
```

#### SDK Actions Fail

**Problem**: `composeCast()` etc. don't work

**Solution**: Use production HTTPS domain (not tunnel URL)

#### Context is Null

**Problem**: `sdk.context` is null

**Solution**: Use provider pattern, check `isReady`

#### Wallet Not Available

**Problem**: `getEthereumProvider()` throws error

**Solution**: Check capabilities first

```typescript
const caps = sdk.getCapabilities();
if (caps.includes('ethereum_provider')) {
  // Safe to use
}
```

For detailed troubleshooting, use `/debug-miniapp` command.

## 📚 Resources

### Official Documentation

- **Farcaster Miniapps**: https://miniapps.farcaster.xyz
- **SDK Reference**: https://miniapps.farcaster.xyz/docs/sdk
- **Specification**: https://miniapps.farcaster.xyz/docs/specification
- **GitHub**: https://github.com/farcasterxyz/miniapps

### Developer Tools

- **Warpcast Developer Tools**: https://warpcast.com/~/settings/developer-tools
- **Create Miniapp CLI**: `npm create @farcaster/mini-app`
- **Tunnel Tools**: cloudflared, ngrok

### Community

- **Warpcast Channel**: /farcaster-dev
- **GitHub Discussions**: https://github.com/farcasterxyz/miniapps/discussions
- **Documentation**: This kit's comprehensive guides

## 🤝 Contributing

Contributions are welcome! This kit is part of the Claudius Skills project.

### How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Areas for Contribution

- Additional skills for specific use cases
- New commands for common workflows
- Specialized agents for niche domains
- Example miniapp projects
- Documentation improvements

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- **Farcaster Team**: For the miniapps platform and SDK
- **Warpcast**: For developer tools and documentation
- **Claude Code**: For the extensibility framework
- **Community**: For feedback and contributions

---

## Quick Reference Card

```
Core Workflow:
1. /new-miniapp          → Create project
2. /add-manifest         → Configure identity
3. /setup-auth           → Add authentication
4. /add-embed            → Enable sharing
5. /add-wallet           → Add blockchain (optional)
6. /add-notifications    → Enable push (optional)
7. /deploy-miniapp       → Go to production

Critical Reminders:
- Node.js 22.11.0+
- Call sdk.actions.ready()
- HTTPS URLs only (production)
- Never trust context for auth
- Test in Warpcast preview
```

---

**Ready to build amazing Farcaster miniapps? Start with `/new-miniapp` or activate the `miniapp-generator` skill!**

For questions, issues, or feedback, please open an issue on GitHub or join the discussion in /farcaster-dev on Warpcast.
