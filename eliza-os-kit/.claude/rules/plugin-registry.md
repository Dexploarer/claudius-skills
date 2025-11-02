# elizaOS Official Plugin Registry

**Last Updated:** 2025-11-01
**Total Plugins:** 200+ official and community plugins

This is the complete registry of available elizaOS plugins with their GitHub locations. Use this reference when suggesting plugins or building integrations.

---

## 📦 Plugin Categories

### Database Adapters (8 plugins)
Storage and database connectivity plugins

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/adapter-mongodb` | github:elizaos-plugins/adapter-mongodb | MongoDB database adapter |
| `@elizaos/adapter-pglite` | github:elizaos-plugins/adapter-pglite | PGLite (lightweight PostgreSQL) adapter |
| `@elizaos/adapter-postgres` | github:elizaos-plugins/adapter-postgres | PostgreSQL database adapter |
| `@elizaos/adapter-qdrant` | github:elizaos-plugins/adapter-qdrant | Qdrant vector database adapter |
| `@elizaos/adapter-sqlite` | github:elizaos-plugins/adapter-sqlite | SQLite database adapter |
| `@elizaos/adapter-sqljs` | github:elizaos-plugins/adapter-sqljs | SQL.js (in-memory SQLite) adapter |
| `@elizaos/adapter-supabase` | github:elizaos-plugins/adapter-supabase | Supabase database adapter |
| `@elizaos/plugin-storage-s3` | github:elizaos-plugins/plugin-storage-s3 | Amazon S3 storage adapter |

### Platform Clients (15 plugins)
Social media and communication platform integrations

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/client-auto` | github:elizaos-plugins/client-auto | Automatic client detection and routing |
| `@elizaos/client-discord` | github:elizaos-plugins/client-discord | Discord bot integration |
| `@elizaos/client-farcaster` | github:elizaos-plugins/client-farcaster | Farcaster protocol client |
| `@elizaos/client-github` | github:elizaos-plugins/client-github | GitHub integration client |
| `@elizaos/client-lens` | github:elizaos-plugins/client-lens | Lens Protocol social client |
| `@elizaos/client-slack` | github:elizaos-plugins/client-slack | Slack workspace integration |
| `@elizaos/client-telegram` | github:elizaos-plugins/client-telegram | Telegram bot integration |
| `@elizaos/client-twitter` | github:elizaos-plugins/client-twitter | Twitter/X bot integration |
| `@elizaos/client-twitter-api-access` | github:payainetwork/client-twitter-api-access | Twitter API with extended access |
| `@elizaos/client-wechat` | github:aiqubits/client-wechat | WeChat integration |
| `@elizaos/client-xmtp` | github:ephemeraHQ/client-xmtp | XMTP messaging protocol |
| `@elizaos/client-clara` | github:redstone-finance/client-clara | Clara AI client |
| `@elizaos/client-tako` | github:takoprotocol/client-tako | Tako Protocol client |
| `@bealers/plugin-mattermost` | github:bealers/plugin-mattermost | Mattermost team chat integration |
| `@elizaos/plugin-whatsapp` | github:elizaos-plugins/plugin-whatsapp | WhatsApp integration |

### LLM Providers (8 plugins)
Language model and AI service providers

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-anthropic` | github:elizaos-plugins/plugin-anthropic | Claude AI by Anthropic |
| `@elizaos/plugin-openai` | github:elizaos-plugins/plugin-openai | OpenAI GPT models |
| `@elizaos/plugin-groq` | github:elizaos-plugins/plugin-groq | Groq fast inference |
| `@elizaos/plugin-google-genai` | github:elizaos-plugins/plugin-google-genai | Google Generative AI (Gemini) |
| `@elizaos/plugin-bedrock` | github:elizaos-plugins/plugin-bedrock | AWS Bedrock AI services |
| `@elizaos/plugin-hyperbolic` | github:elizaos-plugins/plugin-hyperbolic | Hyperbolic AI models |
| `@elizaos/plugin-local-ai` | github:elizaos-plugins/plugin-local-ai | Local AI model support |
| `@elizaos/plugin-ollama` | github:elizaos-plugins/plugin-ollama | Ollama local models |

### Blockchain & Web3 (60+ plugins)
Cryptocurrency, DeFi, and blockchain integrations

#### Layer 1 Blockchains
| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-solana` | github:elizaos-plugins/plugin-solana | Solana blockchain |
| `@elizaos/plugin-ethereum` | github:elizaos-plugins/plugin-evm | Ethereum and EVM chains |
| `@elizaos/plugin-near` | github:elizaos-plugins/plugin-near | NEAR Protocol |
| `@elizaos/plugin-sui` | github:elizaos-plugins/plugin-sui | Sui blockchain |
| `@elizaos/plugin-aptos` | github:elizaos-plugins/plugin-aptos | Aptos blockchain |
| `@elizaos/plugin-cosmos` | github:elizaos-plugins/plugin-cosmos | Cosmos ecosystem |
| `@elizaos/plugin-avalanche` | github:elizaos-plugins/plugin-avalanche | Avalanche blockchain |
| `@elizaos/plugin-bnb` | github:elizaos-plugins/plugin-bnb | BNB Chain (Binance Smart Chain) |
| `@elizaos/plugin-cardano` | github:relipasoft/plugin-cardano | Cardano blockchain |
| `@elizaos/plugin-ton` | github:elizaos-plugins/plugin-ton | TON (The Open Network) |
| `@elizaos/plugin-icp` | github:elizaos-plugins/plugin-icp | Internet Computer Protocol |
| `@esscrypt/plugin-polkadot` | github:Esscrypt/plugin-polkadot | Polkadot ecosystem |
| `@elizaos/plugin-multiversx` | github:elizaos-plugins/plugin-multiversx | MultiversX blockchain |
| `@elizaos/plugin-hedera` | github:elizaos-plugins/plugin-hedera | Hedera Hashgraph |
| `@elizaos/plugin-mina` | github:elizaos-plugins/plugin-mina | Mina Protocol |
| `@elizaos/plugin-fuel` | github:elizaos-plugins/plugin-fuel | Fuel Network |
| `@elizaos/plugin-quai` | github:elizaos-plugins/plugin-quai | Quai Network |

#### Layer 2 & Scaling Solutions
| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-abstract` | github:elizaos-plugins/plugin-abstract | Abstract layer 2 |
| `@elizaos/plugin-starknet` | github:elizaos-plugins/plugin-starknet | StarkNet layer 2 |
| `@elizaos/plugin-zksync-era` | github:elizaos-plugins/plugin-zksync-era | zkSync Era layer 2 |
| `@elizaos/plugin-lightlink` | github:lightlink-network/plugin-lightlink | LightLink layer 2 |
| `@elizaos/plugin-cronoszkevm` | github:elizaos-plugins/plugin-cronoszkevm | Cronos zkEVM |

#### DeFi & Trading
| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-coinbase` | github:elizaos-plugins/plugin-coinbase | Coinbase exchange integration |
| `@elizaos/plugin-binance` | github:elizaos-plugins/plugin-binance | Binance exchange integration |
| `@elizaos/plugin-okx` | github:elizaos-plugins/plugin-okx | OKX exchange integration |
| `@elizaos/plugin-ccxt` | github:pranavjadhav1363/plugin-ccxt | Multi-exchange via CCXT |
| `@elizaos/plugin-hyperliquid` | github:elizaos-plugins/plugin-hyperliquid | Hyperliquid DEX |
| `@elizaos/plugin-orderly` | github:orderlynetwork/plugin-orderly | Orderly Network trading |
| `@elizaos/plugin-merkle` | github:merkle-trade/merkle-eliza-plugin | Merkle Trade integration |
| `@theschein/plugin-polymarket` | github:Okay-Bet/plugin-polymarket | Polymarket prediction markets |
| `@elizaos/plugin-rabbi-trader` | github:elizaos-plugins/plugin-rabbi-trader | Rabbi Trader bot |

#### DeFi Protocols
| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-morpho` | github:bowtiedbluefin/plugin-morpho | Morpho lending protocol |
| `@elizaos/plugin-gelato` | github:elizaos-plugins/plugin-gelato | Gelato Network automation |
| `@elizaos/plugin-enso` | github:EnsoBuild/plugin-enso | Enso Finance integration |
| `@elizaos/plugin-holdstation` | github:elizaos-plugins/plugin-holdstation | Holdstation wallet |

#### Cross-Chain & Bridges
| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-debridge` | github:gabrielantonyxaviour/eliza-plugin-debridge | deBridge cross-chain |
| `@elizaos/plugin-squid-router` | github:elizaos-plugins/plugin-squid-router | Squid Router bridging |
| `@elizaos/plugin-relay` | github:elizaos-plugins/plugin-relay | Relay Protocol bridging |
| `@elizaos/plugin-multichain` | github:near-agent/elizaos-plugin-multichain | Multi-chain support |

#### NFT & Digital Assets
| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-nft-generation` | github:elizaos-plugins/plugin-nft-generation | NFT generation and minting |
| `@elizaos/plugin-clanker` | github:elizaos-plugins/plugin-clanker | Clanker NFT platform |
| `@elizaos/plugin-omniflix` | github:elizaos-plugins/plugin-omniflix | OmniFlix NFT marketplace |
| `@elizaos/plugin-stargaze` | github:elizaos-plugins/plugin-stargaze | Stargaze NFT marketplace |

#### Web3 Infrastructure
| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-thirdweb` | github:elizaos-plugins/plugin-thirdweb | Thirdweb Web3 SDK |
| `@elizaos/plugin-goat` | github:elizaos-plugins/plugin-goat | GOAT protocol |
| `@elizaos/plugin-safe` | github:5afe/plugin-safe | Safe (Gnosis Safe) multi-sig |
| `@elizaos/plugin-siwe` | github:DimaKush/plugin-siwe | Sign-In with Ethereum |

#### Specialized Blockchain
| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-movement` | github:elizaos-plugins/plugin-movement | Movement Labs |
| `@elizaos/plugin-story` | github:elizaos-plugins/plugin-story | Story Protocol |
| `@elizaos/plugin-injective` | github:elizaos-plugins/plugin-injective | Injective Protocol |
| `@elizaos/plugin-sei` | github:elizaos-plugins/plugin-sei | Sei Network |
| `@elizaos/plugin-flow` | github:fixes-world/plugin-flow | Flow blockchain |
| `@elizaos/plugin-flow-advanced` | github:fixes-world/plugin-flow-advanced | Advanced Flow features |
| `@elizaos/plugin-kaia` | github:kaiachain/kaia-eliza-plugin | Kaia blockchain |
| `@elizaos/plugin-massa` | github:elizaos-plugins/plugin-massa | Massa blockchain |
| `@elizaos/plugin-conflux` | github:elizaos-plugins/plugin-conflux | Conflux Network |
| `@elizaos/plugin-arthera` | github:elizaos-plugins/plugin-arthera | Arthera blockchain |
| `@elizaos/plugin-viction` | github:BuildOnViction/plugin-viction | Viction blockchain |
| `@elizaos/plugin-xdc` | github:xdc-community/plugin-xdc | XDC Network |
| `@elizaos/plugin-sonic` | github:thopatevijay/plugin-sonic | Sonic blockchain |
| `@elizaos/plugin-trn` | github:Gen3Games/plugin-trn | The Root Network |
| `@elizaos/plugin-lensNetwork` | github:elizaos-plugins/plugin-lensNetwork | Lens Network |

### Data & Analytics (15 plugins)
Market data, blockchain analytics, and data providers

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-coingecko` | github:elizaos-plugins/plugin-coingecko | CoinGecko market data |
| `@elizaos/plugin-coinmarketcap` | github:elizaos-plugins/plugin-coinmarketcap | CoinMarketCap data |
| `@elizaos/plugin-defillama` | github:elizaos-plugins/plugin-defillama | DefiLlama DeFi analytics |
| `@elizaos/plugin-dexpaprika` | github:donbagger/plugin-dexpaprika | DEX analytics |
| `@elizaos/plugin-bitquery` | github:ChuXo/plugin-bitquery | Bitquery blockchain data |
| `@elizaos/plugin-pyth-data` | github:elizaos-plugins/plugin-pyth-data | Pyth Network price feeds |
| `@elizaos/plugin-zerion` | github:elizaos-plugins/plugin-zerion | Zerion portfolio tracking |
| `@elizaos/plugin-zapper` | github:ben-dh3/plugin-zapper | Zapper DeFi portfolio |
| `@elizaos/plugin-goplus` | github:elizaos-plugins/plugin-goplus | GoPlus security data |
| `@elizaos/plugin-messari-ai-toolkit` | github:messari/plugin-messari-ai-toolkit | Messari crypto research |
| `@token-metrics-ai/plugin-tokenmetrics` | github:token-metrics/plugin-tokenmetrics | Token Metrics analytics |
| `@elizaos/plugin-rss3` | github:rss3-network/elizaos-plugin-rss3 | RSS3 decentralized data |
| `@elizaos/plugin-compass` | github:CompassLabs/plugin-compass | Compass analytics |
| `@elizaos/plugin-d.a.t.a` | github:carv-protocol/plugin-d.a.t.a | CARV Protocol data |
| `@elizaos/plugin-ankr` | github:elizaos-plugins/plugin-ankr | Ankr blockchain data |

### AI & Machine Learning (12 plugins)
AI model integrations, generation, and ML tools

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-image-generation` | github:elizaos-plugins/plugin-image-generation | AI image generation |
| `@elizaos/plugin-3d-generation` | github:elizaos-plugins/plugin-3d-generation | 3D model generation |
| `@elizaos/plugin-video-generation` | github:elizaos-plugins/plugin-video-generation | AI video generation |
| `@elizaos/plugin-video-understanding` | github:elizaos-plugins/plugin-video-understanding | Video analysis and understanding |
| `@elizaos/plugin-tts` | github:elizaos-plugins/plugin-tts | Text-to-speech synthesis |
| `@elizaos/plugin-elevenlabs` | github:elizaos-plugins/plugin-elevenlabs | ElevenLabs voice AI |
| `@elizaos/plugin-venice` | github:elizaos-plugins/plugin-venice | Venice AI platform |
| `@elizaos/plugin-allora` | github:elizaos-plugins/plugin-allora | Allora Network AI |
| `@elizaos/plugin-morpheus` | github:bowtiedbluefin/plugin-morpheus | Morpheus AI network |
| `@elizaos/plugin-openrouter` | github:elizaos-plugins/plugin-openrouter | OpenRouter AI gateway |
| `@elizaos/plugin-vercel-ai-gateway` | github:elizaos-plugins/plugin-vercel-ai-gateway | Vercel AI SDK gateway |
| `@elizaos/plugin-asterai` | github:elizaos-plugins/plugin-asterai | Aster AI integration |

### Developer Tools (20 plugins)
Development, automation, and productivity tools

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-github` | github:elizaos-plugins/plugin-github | GitHub repository management |
| `@elizaos/plugin-linear` | github:elizaos-plugins/plugin-linear | Linear issue tracking |
| `@elizaos/plugin-notion` | github:tskoyo/plugin-notion | Notion workspace integration |
| `@elizaos/plugin-obsidian` | github:elizaos-plugins/plugin-obsidian | Obsidian note-taking |
| `@elizaos/plugin-gitbook` | github:elizaos-plugins/plugin-gitbook | GitBook documentation |
| `@elizaos/plugin-autocoder` | github:elizaos-plugins/plugin-autocoder | Automated code generation |
| `@elizaos/plugin-e2b` | github:elizaos-plugins/plugin-e2b | E2B code execution sandbox |
| `@elizaos/plugin-computer-use` | github:amit0365/plugin-computer-use | Computer automation |
| `@elizaos/plugin-shell` | github:elizaos-plugins/plugin-shell | Shell command execution |
| `@elizaos/plugin-node` | github:elizaos-plugins/plugin-node | Node.js integration |
| `@standujar/plugin-composio` | github:standujar/plugin-composio | Composio automation |
| `@elizaos/plugin-auton8n` | github:elizaos-plugins/plugin-auton8n | Automation workflows |
| `@elizaos/plugin-autonome` | github:elizaos-plugins/plugin-autonome | Autonomous operations |
| `@elizaos/plugin-executor` | github:t3rn/plugin-t3rn-executor | T3rn executor |
| `@elizaos/plugin-action-bench` | github:elizaos-plugins/plugin-action-bench | Action benchmarking |
| `@elizaos/plugin-mcp` | github:elizaos-plugins/plugin-mcp | Model Context Protocol |
| `@elizaos/plugin-livekit` | github:elizaos-plugins/plugin-livekit | LiveKit real-time communication |
| `@elizaos/plugin-twilio` | github:boolkeys/plugin-twilio | Twilio communication APIs |
| `@elizaos/plugin-discord` | github:elizaos-plugins/plugin-discord | Discord bot utilities |
| `@elizaos/plugin-telegram` | github:elizaos-plugins/plugin-telegram | Telegram bot utilities |

### Content & Media (15 plugins)
Content processing, media handling, and search

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-browser` | github:elizaos-plugins/plugin-browser | Web browser automation |
| `@elizaos/plugin-web-search` | github:elizaos-plugins/plugin-web-search | Web search capabilities |
| `@elizaos/plugin-firecrawl` | github:tobySolutions/plugin-firecrawl | Web scraping with Firecrawl |
| `@elizaos/plugin-pdf` | github:elizaos-plugins/plugin-pdf | PDF processing and generation |
| `@elizaos/plugin-youtube-to-text` | github:wellaios/plugin-youtube-to-text | YouTube transcription |
| `@elizaos/plugin-youtube-transcription` | github:prismadic/elizaos-plugin-youtube-transcription | YouTube video transcription |
| `@elizaos/plugin-giphy` | github:elizaos-plugins/plugin-giphy | Giphy GIF integration |
| `@elizaos/plugin-open-weather` | github:elizaos-plugins/plugin-open-weather | OpenWeather weather data |
| `@elizaos/plugin-wolfram` | github:elizaos-plugins/plugin-wolfram | Wolfram Alpha knowledge |
| `@elizaos/plugin-knowledge` | github:elizaos-plugins/plugin-knowledge | Knowledge base management |
| `@elizaos/plugin-recall` | github:recallnet/plugin-recall | Recall memory management |
| `@elizaos/plugin-membase` | github:unibaseio/plugin-membase | Membase storage |
| `@elizaos/plugin-rss3` | github:rss3-network/elizaos-plugin-rss3 | RSS3 content feeds |
| `@elizaos/plugin-clara-twitter` | github:warp-contracts/plugin-clara-twitter | Clara Twitter integration |
| `@elizaos/plugin-farcaster` | github:elizaos-plugins/plugin-farcaster | Farcaster social protocol |

### Infrastructure & Cloud (15 plugins)
Cloud services, infrastructure, and deployment

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-akash` | github:elizaos-plugins/plugin-akash | Akash decentralized cloud |
| `@elizaos/plugin-spheron` | github:elizaos-plugins/plugin-spheron | Spheron decentralized hosting |
| `@elizaos/plugin-storacha` | github:storacha/elizaos-plugin | Storacha decentralized storage |
| `@elizaos/plugin-irys` | github:elizaos-plugins/plugin-irys | Irys permanent storage |
| `@elizaos/plugin-avail` | github:elizaos-plugins/plugin-avail | Avail data availability |
| `@elizaos/plugin-0g` | github:elizaos-plugins/plugin-0g | 0G decentralized storage |
| `@elizaos/plugin-iexec` | github:iExecBlockchainComputing/plugin-iexec | iExec decentralized computing |
| `@elizaos/plugin-depin` | github:elizaos-plugins/plugin-depin | DePIN infrastructure |
| `@elizaos/plugin-nkn` | github:nknorg/eliza-plugin-nkn | NKN decentralized network |
| `@elizaos/plugin-opacity` | github:elizaos-plugins/plugin-opacity | Opacity storage |
| `@elizaos/plugin-primus` | github:elizaos-plugins/plugin-primus | Primus infrastructure |
| `@elizaos/plugin-anyone` | github:elizaos-plugins/plugin-anyone | Anyone Protocol |
| `@elizaos/plugin-bless` | github:blessnetwork/elizaos-bless-plugin | Bless Network |
| `@elizaos/plugin-xmtp` | github:elizaos-plugins/plugin-xmtp | XMTP messaging |
| `@elizaos/plugin-sql` | github:elizaos-plugins/plugin-sql | SQL database utilities |

### Security & Privacy (10 plugins)
Security tools, TEE, and privacy solutions

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-tee` | github:elizaos-plugins/plugin-tee | Trusted Execution Environment |
| `@elizaos/plugin-tee-log` | github:elizaos-plugins/plugin-tee-log | TEE logging |
| `@elizaos/plugin-tee-marlin` | github:elizaos-plugins/plugin-tee-marlin | Marlin TEE integration |
| `@elizaos/plugin-sgx` | github:elizaos-plugins/plugin-sgx | Intel SGX support |
| `@elizaos/plugin-dcap` | github:elizaos-plugins/plugin-dcap | Data Center Attestation Primitives |
| `@elizaos/plugin-proof-of-agent` | github:automata-network/elizaos-plugin-proof-of-agent | Agent verification |
| `@elizaos/plugin-gitcoin-passport` | github:elizaos-plugins/plugin-gitcoin-passport | Gitcoin Passport identity |
| `@elizaos/plugin-trustgo` | github:TrustaLabs/plugin-trustgo | TrustGo verification |
| `@elizaos/plugin-okto` | github:okto-hq/eliza-plugin | Okto security |
| `@elizaos/plugin-reveel-payid` | github:r3vl/plugin-reveel-payid | Reveel payment identity |

### Gaming & Metaverse (8 plugins)
Gaming, virtual worlds, and entertainment

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-holoworld` | github:mcp-dao/plugin-holoworld | HoloWorld metaverse |
| `@elizaos/plugin-grix` | github:grixprotocol/plugin-grix | Grix gaming protocol |
| `@elizaos/plugin-zytron` | github:zypher-network/plugin-zytron | Zytron gaming |
| `@elizaos/plugin-gigbot` | github:PaymagicXYZ/plugin-gigbot | GigBot task marketplace |
| `@elizaos/plugin-raiinmaker` | github:Coiin-Blockchain/plugin-raiinmaker | Raiinmaker rewards |
| `@elizaos/plugin-para` | github:aipop-fun/plugin-para | Para gaming platform |
| `@elizaos/plugin-intiface` | github:elizaos-plugins/plugin-intiface | Intiface device integration |
| `@elizaos/plugin-letzai` | github:elizaos-plugins/plugin-letzai | LetzAI gaming |

### DeFi Specialized (8 plugins)
Specialized DeFi and financial tools

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-payai` | github:payainetwork/plugin-payai | PayAI payment processing |
| `@nuggetslife/plugin-nuggets` | github:NuggetsLtd/eliza-plugin-nuggets | Nuggets payment identity |
| `@elizaos/plugin-ferePro` | github:elizaos-plugins/plugin-ferePro | Fere Pro trading |
| `@elizaos/plugin-redpill` | github:elizaos-plugins/plugin-redpill | RedPill DeFi analytics |
| `@elizaos/plugin-edwin` | github:elizaos-plugins/plugin-edwin | Edwin trading bot |
| `@elizaos/plugin-solana-agent-kit` | github:elizaos-plugins/plugin-solana-agent-kit | Solana DeFi toolkit |
| `@kudo-dev/plugin-kudo` | github:Kudo-Archi/plugin-kudo | Kudo DeFi operations |
| `@onbonsai/plugin-bonsai` | github:onbonsai/plugin-bonsai | Bonsai DeFi aggregator |

### Identity & Social (10 plugins)
Identity verification, social connections, and profiles

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-bnv-me-id` | github:brand-new-vision/plugin-bnv-me-id | Brand New Vision identity |
| `@elizaos/plugin-di` | github:fixes-world/plugin-di | Decentralized identity |
| `@mascotai/plugin-connections` | github:mascotai/plugin-connections | Social connections |
| `plugin-connections` | github:mascotai/plugin-connections | Connections management |
| `@elizaos/plugin-echochambers` | github:elizaos-plugins/plugin-echochambers | EchoChambers social |
| `@elizaos/plugin-bioagent` | github:bio-xyz/plugin-bioagent | BioAgent identity |
| `@elizaos/plugin-mbd-farcaster` | github:developerfred/mbd-farcaster | MBD Farcaster integration |
| `@elizaos/plugin-isaacx` | github:isaacx0/plugin-isaacx | IsaacX social |
| `@elizaos/plugin-ATTPs` | github:APRO-com/plugin-ATTPs | ATTPs protocol |
| `@elizaos/plugin-bink` | github:Bink-AI/elizaos-plugin-binkai | Bink AI identity |

### Specialized Tools (10 plugins)
Miscellaneous specialized functionality

| Plugin | GitHub | Purpose |
|--------|--------|---------|
| `@elizaos/plugin-bootstrap` | github:elizaos-plugins/plugin-bootstrap | Core bootstrap functionality |
| `@elizaos/plugin-genlayer` | github:elizaos-plugins/plugin-genlayer | GenLayer protocol |
| `@elizaos/plugin-pundiai-dataset` | github:PundiAI/plugin-pundiai-dataset | PundiAI dataset management |
| `@mazzz/plugin-elizaos-compchembridge` | github:Mazzz-zzz/plugin-elizaos-compchembridge | Computational chemistry bridge |
| `plugin-octav` | github:wpoulin/plugin-octav | Octav audio processing |
| `@elizaos/plugin-clanker` | github:elizaos-plugins/plugin-clanker | Clanker utilities |
| `@elizaos/plugin-redpill` | github:elizaos-plugins/plugin-redpill | RedPill tooling |
| `@elizaos/plugin-primus` | github:elizaos-plugins/plugin-primus | Primus framework |
| `@elizaos/plugin-anyone` | github:elizaos-plugins/plugin-anyone | Anyone Protocol tools |
| `@elizaos/plugin-autonome` | github:elizaos-plugins/plugin-autonome | Autonome automation |

---

## 🔍 Plugin Installation

### NPM Installation
```bash
npm install @elizaos/plugin-{name}
```

### GitHub Direct Installation
```json
{
  "dependencies": {
    "@elizaos/plugin-{name}": "github:elizaos-plugins/plugin-{name}"
  }
}
```

### Character Configuration
```typescript
import { Character } from '@elizaos/core';

export const character: Character = {
  // ... other config

  plugins: [
    // Core (always include)
    '@elizaos/plugin-bootstrap',

    // Database adapter (choose one)
    '@elizaos/adapter-postgres',
    // or '@elizaos/adapter-pglite',
    // or '@elizaos/adapter-sqlite',

    // LLM provider (at least one required)
    '@elizaos/plugin-openai',
    // or '@elizaos/plugin-anthropic',

    // Platform clients (as needed)
    '@elizaos/client-discord',
    '@elizaos/client-telegram',
    '@elizaos/client-twitter',

    // Additional capabilities
    '@elizaos/plugin-web-search',
    '@elizaos/plugin-knowledge',

    // Blockchain (if needed)
    '@elizaos/plugin-solana',
    '@elizaos/plugin-evm',

    // Conditional loading
    ...(process.env.DISCORD_TOKEN ? ['@elizaos/client-discord'] : []),
    ...(process.env.OPENAI_API_KEY ? ['@elizaos/plugin-openai'] : []),
  ]
};
```

---

## 📊 Plugin Categories Summary

| Category | Count | Examples |
|----------|-------|----------|
| Database Adapters | 8 | PostgreSQL, MongoDB, SQLite, Supabase |
| Platform Clients | 15 | Discord, Telegram, Twitter, Slack |
| LLM Providers | 8 | OpenAI, Anthropic, Groq, Ollama |
| Blockchain & Web3 | 60+ | Solana, Ethereum, NEAR, Cosmos |
| Data & Analytics | 15 | CoinGecko, DefiLlama, Messari |
| AI & ML | 12 | Image Gen, Video Gen, TTS, Voice AI |
| Developer Tools | 20 | GitHub, Linear, Notion, Code Execution |
| Content & Media | 15 | Web Search, PDF, YouTube, Browser |
| Infrastructure | 15 | Akash, Spheron, Irys, Storage |
| Security & Privacy | 10 | TEE, SGX, Identity, Verification |
| Gaming & Metaverse | 8 | HoloWorld, Gaming Protocols |
| DeFi Specialized | 8 | Trading, Payments, Analytics |
| Identity & Social | 10 | Identity, Social Connections |
| Specialized Tools | 10 | Bootstrap, Datasets, Utilities |

**Total: 200+ Plugins**

---

## 🎯 Common Plugin Combinations

### Basic Chat Bot
```typescript
plugins: [
  '@elizaos/plugin-bootstrap',
  '@elizaos/adapter-pglite',
  '@elizaos/plugin-openai',
  '@elizaos/client-discord',
]
```

### DeFi Trading Agent
```typescript
plugins: [
  '@elizaos/plugin-bootstrap',
  '@elizaos/adapter-postgres',
  '@elizaos/plugin-anthropic',
  '@elizaos/plugin-solana',
  '@elizaos/plugin-coinbase',
  '@elizaos/plugin-coingecko',
  '@elizaos/plugin-defillama',
]
```

### Content Creation Bot
```typescript
plugins: [
  '@elizaos/plugin-bootstrap',
  '@elizaos/adapter-sqlite',
  '@elizaos/plugin-openai',
  '@elizaos/client-twitter',
  '@elizaos/plugin-image-generation',
  '@elizaos/plugin-web-search',
  '@elizaos/plugin-knowledge',
]
```

### Multi-Platform Support Agent
```typescript
plugins: [
  '@elizaos/plugin-bootstrap',
  '@elizaos/adapter-postgres',
  '@elizaos/plugin-anthropic',
  '@elizaos/client-discord',
  '@elizaos/client-telegram',
  '@elizaos/client-slack',
  '@elizaos/plugin-knowledge',
  '@elizaos/plugin-github',
  '@elizaos/plugin-linear',
]
```

### Web3 NFT Agent
```typescript
plugins: [
  '@elizaos/plugin-bootstrap',
  '@elizaos/adapter-postgres',
  '@elizaos/plugin-openai',
  '@elizaos/plugin-solana',
  '@elizaos/plugin-nft-generation',
  '@elizaos/plugin-image-generation',
  '@elizaos/client-twitter',
  '@elizaos/plugin-irys',
]
```

---

## 📝 Notes

- **Always include** `@elizaos/plugin-bootstrap` - it provides core functionality
- **Choose one database adapter** based on your needs
- **At least one LLM provider** required for agent intelligence
- **Platform clients** enable multi-platform deployment
- **Conditional loading** recommended for optional plugins
- **GitHub sources** allow latest development versions
- **Community plugins** may have different maintenance levels

---

## 🔄 Keeping Updated

This registry is based on the official elizaOS plugin ecosystem. New plugins are added regularly. To check for updates:

1. Visit [elizaOS GitHub](https://github.com/elizaos-plugins)
2. Check [elizaOS Discord](https://discord.gg/elizaos) announcements
3. Review plugin documentation for version compatibility

---

## 🤝 Contributing Plugins

To add your plugin to the ecosystem:

1. Follow the [plugin development guide](https://docs.elizaos.ai/plugins)
2. Publish to GitHub under `elizaos-plugins` org or your own
3. Submit to the plugin registry
4. Share in elizaOS community

---

**Last Updated:** 2025-11-01
**Plugin Count:** 200+
**Source:** Official elizaOS Plugin Ecosystem
