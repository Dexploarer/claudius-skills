# Create New Farcaster Miniapp

Create a new Farcaster miniapp project with the official CLI and proper structure.

## Steps

1. Verify Node.js version (22.11.0+):
```bash
node --version
```

2. Create new project:
```bash
npm create @farcaster/mini-app
```

3. Follow CLI prompts for:
   - Project name
   - Framework choice (Next.js recommended)
   - Manifest setup (can skip for now)

4. Navigate to project:
```bash
cd <project-name>
```

5. Install dependencies:
```bash
npm install
```

6. Start development server:
```bash
npm run dev
```

7. Setup HTTPS tunnel for local testing:
```bash
cloudflared tunnel --url localhost:3000
```

## Next Steps

- Configure manifest with `/add-manifest`
- Setup authentication with `/setup-auth`
- Add embeds with `/add-embed`
- Test in Warpcast preview tool
