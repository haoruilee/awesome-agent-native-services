# Awesome Agent-Native Services [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of services **designed from the ground up for AI agents** — not adapted from human-facing products.

Each service is either infrastructure an AI agent *consumes directly* or a narrowly qualified, purpose-built surface for operating concrete agent sessions — not a generic platform for humans to *build agents with*.

**Also on the web:** [The Agent-Native Index](https://lihaorui.com/awesome-agent-native-services/) — the same catalog with structured metadata and machine-readable discovery endpoints.

---

---

## Table of contents

- [Browse by category](#categories)
- [1. Communication services (agent-native email & identity)](#1-communication-services)
- [2. Browser & web execution (remote browsers for agents)](#2-browser--web-execution-services)
- [3. Tool access & integration (MCP servers & agent tools)](#3-tool-access--integration-services)
- [4. Oversight & approval (human-in-the-loop for agents)](#4-oversight--approval-services)
- [5. Commerce & payments (agent wallets & protocols)](#5-commerce--payment-services)
- [6. Agent runtime & infrastructure (sandboxes, gateways, identity)](#6-agent-runtime--infrastructure-services)
- [7. Agent harnesses & operator surfaces (multi-agent control and live Codex HUDs)](#7-agent-harnesses--operator-surfaces)
- [8. Memory & state (long-term memory for LLM agents)](#8-memory--state-services)
- [9. Search & web intelligence (LLM-ready retrieval)](#9-search--web-intelligence-services)
- [10. Code execution (secure sandboxes for AI-generated code)](#10-code-execution-services)
- [11. Observability & tracing (agent trajectories & evals)](#11-observability--tracing-services)
- [12. Durable execution & scheduling (long-running agent workflows)](#12-durable-execution--scheduling-services)
- [13. Meeting & conversation (bots & voice rooms for agents)](#13-meeting--conversation-services)
- [14. Voice & phone (telephony for AI agents)](#14-voice--phone-services)
- [15. LLM gateway & routing (cost control & model routing)](#15-llm-gateway--routing-services)
- [16. Agent social & community (MCP-native social layers)](#16-agent-social--community-services)
- [Ecosystem hubs](#ecosystem-hubs)
- [Excluded / boundary cases](#excluded--boundary-cases)
- [Classification](#classification)
- [Contributing](#contributing)
- [License](#license)

---

## ⭐ Agent onboarding

If you are an AI agent and want to discover services designed for you:

```
Read https://raw.githubusercontent.com/haoruilee/awesome-agent-native-services/main/skill.md then find services designed for you natively.
```

Besides, you can install these skills through Claude Code's plugin marketplace flow or load them directly from this repository:

**Claude Code plugin marketplace** (requires a Claude Code version with plugin support; see the [official plugin marketplace docs](https://code.claude.com/docs/en/discover-plugins)):

```text
/plugin marketplace add haoruilee/awesome-agent-native-services
/plugin install awesome-agent-native-services@awesome-agent-native-services
/reload-plugins
```

**Direct `SKILL.md` install:**

```bash
git clone --depth=1 https://github.com/haoruilee/awesome-agent-native-services.git
mkdir -p ~/.claude/skills
cp -R awesome-agent-native-services/.skills/find-agent-service ~/.claude/skills/
```

Source files are in `.skills/` in this repo. See [SKILLS_HUB.md](SKILLS_HUB.md) for Claude Code and manual `SKILL.md` installation paths.

**Install-entry workflow:** install this repo once, then ask `install-agent-service` for a concrete entry point. It ranks URL onboarding first, then Agent Skills/plugins, MCP, CLI, and SDK setup so the catalog can act as an installer/router instead of only a directory.

### Skills Hub usage

Use this repository's Skills Hub when you want an agent to operate the catalog directly rather than only read the Markdown index:

1. **Find a service for a concrete job** — install or load `find-agent-service`, then ask: `Use find-agent-service to find an agent-native service for <task>`. The skill reads the catalog criteria and returns matching services with onboarding steps.
2. **Install or connect a service** — install or load `install-agent-service`, then ask: `Use install-agent-service to install/connect <service or task>`. The skill returns URL onboarding, Agent Skill/plugin, MCP, CLI, or SDK commands.
3. **Vet a candidate service** — install or load `evaluate-agent-native`, then provide the service URL, docs, and repo. The skill applies the standard or operator-surface admission track before you open an issue or PR.
4. **Prepare a contribution** — install or load `add-to-awesome-list` when adding a new service. It walks through the issue-first workflow, required service-file sections, and README/category table updates.
5. **Use without a marketplace** — any `SKILL.md`-compatible agent can copy a folder from `.skills/` into its local skills directory, for example `cp -R .skills/find-agent-service ~/.claude/skills/`.

Recommended flow for agents: start with `skill.md` for quick discovery, switch to [SKILLS_HUB.md](SKILLS_HUB.md) or `install-agent-service` when you need installable workflows, and use the per-service Markdown files for source-backed details.

---

## Categories

**216 services across 16 categories.**

| # | Category | Services | Description |
|---|---|---|---|
| 1 | [Communication](#1-communication-services) | 15 | Give agents a communication identity on the internet |
| 2 | [Browser & Web Execution](#2-browser--web-execution-services) | 25 | Remote browser and web data extraction for agents |
| 3 | [Tool Access & Integration](#3-tool-access--integration-services) | 21 | Runtime tool discovery, auth, and execution |
| 4 | [Oversight & Approval](#4-oversight--approval-services) | 5 | Human-in-the-loop approval and escalation |
| 5 | [Commerce & Payments](#5-commerce--payment-services) | 12 | Agent-native wallets, identity, and transactions |
| 6 | [Agent Runtime & Infrastructure](#6-agent-runtime--infrastructure-services) | 29 | Execution, session isolation, secrets, and gateway |
| 7 | [Agent Harnesses & Operator Surfaces](#7-agent-harnesses--operator-surfaces) | 10 | Durable agent-loop control and live operator visibility |
| 8 | [Memory & State](#8-memory--state-services) | 26 | Persistent agent memory across sessions |
| 9 | [Search & Web Intelligence](#9-search--web-intelligence-services) | 9 | LLM-optimized web search and content retrieval |
| 10 | [Code Execution](#10-code-execution-services) | 13 | Secure sandboxes for AI-generated code |
| 11 | [Observability & Tracing](#11-observability--tracing-services) | 13 | Agent trajectory tracing and evaluation |
| 12 | [Durable Execution & Scheduling](#12-durable-execution--scheduling-services) | 6 | Fault-tolerant long-running agent workflows |
| 13 | [Meeting & Conversation](#13-meeting--conversation-services) | 8 | Agent presence in voice and video meetings |
| 14 | [Voice & Phone](#14-voice--phone-services) | 7 | Agent-controlled voice calls and phone infrastructure |
| 15 | [LLM Gateway & Routing](#15-llm-gateway--routing-services) | 10 | Per-agent budget, routing, caching, and observability for LLM calls |
| 16 | [Agent Social & Community](#16-agent-social--community-services) | 7 | Social networks where agents are first-class participants |

---

## 1. Communication Services

**MCP-native and API-first email, inboxes, and messaging** — services built so autonomous agents send, receive, and search mail with their own identity.

> Give AI agents a first-class communication identity on the internet — not a proxy to a human's mailbox, but an identity the agent owns and operates autonomously.

→ **[Full category overview and criteria](services/communication/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [ATXP Email](services/communication/atxp-email.md) [![⭐](https://img.shields.io/github/stars/atxp-dev/atxp?style=social)](https://github.com/atxp-dev/atxp) | Email for AI agents | Per-agent inbox · CLI/API provisioning · Verification-code workflow | ⚠️ | Read https://atxp.email/ and follow the docs to create an agent inbox via CLI/API |
| [AgentMail](services/communication/agentmail.md) | Email for AI agents | Agent inbox · Threaded conversation · Webhook on inbound mail · Semantic search | ✅ | `pip install agentmail` then `POST /inboxes` |
| [Novu](services/communication/novu.md) [![⭐](https://img.shields.io/github/stars/novuhq/novu?style=social)](https://github.com/novuhq/novu) | Notification infrastructure with Agent Toolkit | Workflow-as-tool · Cross-channel delivery · HITL notification flow | ✅ | `npx skills add novuhq/skills` |
| [Chimely](services/communication/chimely.md) [![⭐](https://img.shields.io/github/stars/dodopayments/chimely?style=social)](https://github.com/dodopayments/chimely) | Self-hostable in-app notification inbox | HTTP notification API · SSE hint plane · `<Inbox />` React component | ⚠️ | Use the HTTP API from https://chimely.dev docs to deliver in-app notifications |
| [mails.dev](services/communication/mails-dev.md) | Email for AI Agents | @mails.dev mailbox · Send/inbox · wait-for-code · Full-text search | ⚠️ | Read https://mails.dev/skill.md and follow the instructions |
| [OpenMail](services/communication/openmail.md) | Email API for AI agents | One inbox per agent · Webhook/WebSocket inbound · RAG-ready attachment parsing | ⚠️ | `npm install -g @openmail/cli` → `openmail setup` — [docs.openmail.sh](https://docs.openmail.sh/quickstart) |
| [OutreachAgent](services/communication/outreachagent.md) | The Cold Outbound Engine for AI Agents | Agent inboxes · Reply-aware workflows · Send limits/approvals · Signed webhooks | ⚠️ | `npm install @outreachagent/sdk-ts` or use REST API at `https://api.outreachagent.dev/v1` |
| [MailboxKit](services/communication/mailboxkit.md) | Email infrastructure for AI agents | Per-agent address · REST v1 · Inbound webhooks · URL Onboarding | ⚠️ | Read https://mailboxkit.com/skill.md and follow the instructions |
| [Agents Mail](services/communication/agents-mail.md) | Email for AI Agents | Agent registration · Inbox lifecycle · Send/reply API · URL Onboarding | ⚠️ | Read https://agentsmail.org/skill.md and follow the instructions |
| [MCP Agent Mail](services/communication/mcp-agent-mail.md) [![⭐](https://img.shields.io/github/stars/Dicklesworthstone/mcp_agent_mail?style=social)](https://github.com/Dicklesworthstone/mcp_agent_mail) | Async coordination layer for AI coding agents | Agent identity · Inbox/outbox · Thread search · Advisory file reservations | ✅ | `uvx mcp_agent_mail` then connect MCP client and call `register_agent`/`send_message` |
| [MCP Agent Mail (Rust)](services/communication/mcp-agent-mail-rust.md) [![⭐](https://img.shields.io/github/stars/Dicklesworthstone/mcp_agent_mail_rust?style=social)](https://github.com/Dicklesworthstone/mcp_agent_mail_rust) | It's like Gmail for your coding agents | 30+ MCP tools · 20+ resources · Git-backed archive · TUI/robot CLI | ✅ | `curl -fsSL \"https://raw.githubusercontent.com/Dicklesworthstone/mcp_agent_mail_rust/main/install.sh?$(date +%s)\" \| bash` then `am` |
| [AgenticMail](services/communication/agenticmail.md) [![⭐](https://img.shields.io/github/stars/agenticmail/agenticmail?style=social)](https://github.com/agenticmail/agenticmail) | Email & SMS infrastructure for AI agents | Agent inbox + phone bundle · Stalwart self-host · Google Voice bridge · 75+ REST endpoints | ⚠️ | `git clone https://github.com/agenticmail/agenticmail && docker compose up -d` |
| [Caspian](services/communication/caspian.md) [![⭐](https://img.shields.io/github/stars/TryCaspian/caspian-sdk?style=social)](https://github.com/TryCaspian/caspian-sdk) | One agent communication identity across human channels | Email/Slack/Discord/Telegram/SMS · normalized events · SDKs · webhooks | ⚠️ | Read https://api.trycaspianai.com/SKILL.md and follow it end to end |
| [Atomic Mail](services/communication/atomic-mail.md) [![⭐](https://img.shields.io/github/stars/Atomic-Mail/atomic-mail-agentic?style=social)](https://github.com/Atomic-Mail/atomic-mail-agentic) | Not AI for your email. Email for your AI. | PoW inbox · JMAP · local/hosted MCP · AgentSkill | ✅ | Read https://atomicmail.ai and follow the instructions to create an inbox |
| [AgentTeam Email](services/communication/agentteam-email.md) [![⭐](https://img.shields.io/github/stars/agentteamhq/agentteam-email?style=social)](https://github.com/agentteamhq/agentteam-email) | Open-source email infrastructure for AI agents | Per-agent mailbox · at-email CLI · draft review · Cloudflare routing | ⚠️ | `npx --yes @agentteamhq/email@latest` then `at-email agent connect` |

---

## 2. Browser & Web Execution Services

> Give AI agents a remote, managed browser runtime — so agents can navigate, interact with, and extract data from the web as an autonomous actor.

→ **[Full category overview and criteria](services/browser-and-web-execution/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Vercel Agent Browser](services/browser-and-web-execution/agent-browser.md) [![⭐](https://img.shields.io/github/stars/vercel-labs/agent-browser?style=social)](https://github.com/vercel-labs/agent-browser) | Browser automation CLI for AI agents | Rust CLI · Chrome for Testing · scriptable browser control | ⚠️ | `npm install -g agent-browser` |
| [Browser MCP](services/browser-and-web-execution/browser-mcp.md) [![⭐](https://img.shields.io/github/stars/BrowserMCP/mcp?style=social)](https://github.com/BrowserMCP/mcp) | Browser MCP server for AI agents | Puppeteer MCP · accessibility tree · optional vision | ✅ | `npx -y @browsermcp/mcp` |
| [Browserbase](services/browser-and-web-execution/browserbase.md) [![⭐](https://img.shields.io/github/stars/browserbase/stagehand?style=social)](https://github.com/browserbase/stagehand) | A web browser for AI agents & applications | Remote browser session · Stagehand NL actions · Session recording · Stealth mode | ✅ | `npx skills add browserbase/skills` |
| [Firecrawl](services/browser-and-web-execution/firecrawl.md) | Turn any website into LLM-ready data | Intent-driven extraction · LLM-ready markdown · Schema-typed JSON output | ✅ | `npx skills add firecrawl/cli` |
| [Bright Data Agent Browser](services/browser-and-web-execution/bright-data-agent-browser.md) | Cloud browser for AI agents with built-in website unlocking | Built-in CAPTCHA/fingerprint unlocking · 150M+ proxy IPs · Parallel sessions | ✅ | Add Web MCP to config: `npx -y @brightdata/mcp` |
| [bb-browser](services/browser-and-web-execution/bb-browser.md) [![⭐](https://img.shields.io/github/stars/epiral/bb-browser?style=social)](https://github.com/epiral/bb-browser) | Your browser is the API — 103 commands, 36 platforms, your real login state | Authenticated session delegation · Site commands · MCP built-in | ✅ | `npm install -g bb-browser` + Chrome extension, then `bb-browser site <platform>/<cmd>` |
| [OpenCLI](services/browser-and-web-execution/opencli.md) [![⭐](https://img.shields.io/github/stars/jackwener/opencli?style=social)](https://github.com/jackwener/opencli) | Websites, Electron apps, and local CLIs as one agent-discoverable CLI | Chrome session reuse · YAML/TS adapters · External CLI hub · `explore`/`synthesize` | ⚠️ | `npm install -g @jackwener/opencli` → `opencli list -f yaml`; read [SKILL.md](https://raw.githubusercontent.com/jackwener/opencli/main/SKILL.md) |
| [Steel](services/browser-and-web-execution/steel.md) [![⭐](https://img.shields.io/github/stars/steel-dev/steel-browser?style=social)](https://github.com/steel-dev/steel-browser) | Browser infrastructure for AI agents | Sessions API · Puppeteer/Playwright/Selenium connect · CAPTCHA/proxy · Session viewer · MCP | ✅ | `pip install steel-sdk` → `Steel().sessions.create()` — MCP: [steel-mcp-server](https://github.com/steel-dev/steel-mcp-server) |
| [Notte](services/browser-and-web-execution/notte.md) [![⭐](https://img.shields.io/github/stars/nottelabs/notte?style=social)](https://github.com/nottelabs/notte) | Browser infrastructure that lets AI run on the internet at speed | CDP sessions · NL web agents · Vault (secrets never to LLM) · Scraping · notte-mcp | ✅ | `pip install notte-sdk` → `NotteClient().Session()` — MCP: `pip install notte-mcp` → `python -m notte_mcp.server` |
| [Skyvern](services/browser-and-web-execution/skyvern.md) [![⭐](https://img.shields.io/github/stars/Skyvern-AI/skyvern?style=social)](https://github.com/Skyvern-AI/skyvern) | AI agents to automate workflows on any website | `POST /v1/run/tasks` · Vision agent engines · 2FA/TOTP · Browser sessions · JSON extraction | ✅ | API key → [Run a task](https://www.skyvern.com/docs/api-reference/api-reference/agent/run-task) — SDKs in docs |
| [Browser Use Cloud](services/browser-and-web-execution/browser-use-cloud.md) [![⭐](https://img.shields.io/github/stars/browser-use/browser-use?style=social)](https://github.com/browser-use/browser-use) | Managed stealth browsers and NL agent tasks for AI | `client.run()` · CDP `browsers.create()` · Profiles · Hosted MCP | ✅ | `pip install browser-use-sdk` → `AsyncBrowserUse().run(...)` — MCP: `https://api.browser-use.com/v3/mcp` |
| [Anchor Browser](services/browser-and-web-execution/anchor-browser.md) | The secure infrastructure for computer use agents | Web Action Cache · OmniConnect auth · Stealth Chromium · MCP | ✅ | [docs.anchorbrowser.io](https://docs.anchorbrowser.io/introduction) — Python/TS SDKs on GitHub |
| [Hyperbrowser](services/browser-and-web-execution/hyperbrowser.md) [![⭐](https://img.shields.io/github/stars/hyperbrowserai/mcp?style=social)](https://github.com/hyperbrowserai/mcp) | Web infra for AI agents | Scrape/crawl/CUA MCP tools · HyperAgent · Profiles | ✅ | `npx hyperbrowser-mcp <API_KEY>` |
| [AgentQL](services/browser-and-web-execution/agentql.md) [![⭐](https://img.shields.io/github/stars/tinyfish-io/agentql?style=social)](https://github.com/tinyfish-io/agentql) | Make the web AI-ready | AgentQL query → JSON · Remote browser CDP · Browserless REST | ⚠️ | API key → [docs.agentql.com](https://docs.agentql.com) |
| [Crawl4AI](services/browser-and-web-execution/crawl4ai.md) [![⭐](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social)](https://github.com/unclecode/crawl4ai) | Open-source LLM-friendly web crawler & scraper | LLM-ready markdown · Extraction · Docker · MCP | ✅ | Deploy per [docs.crawl4ai.com](https://docs.crawl4ai.com) — MCP from repo |
| [Playwright MCP](services/browser-and-web-execution/playwright-mcp.md) [![⭐](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=social)](https://github.com/microsoft/playwright-mcp) | Playwright MCP server | Accessibility snapshot tools · Browser automation via MCP · stdio/HTTP transports | ✅ | `npx @playwright/mcp@latest` — [playwright.dev/docs/getting-started-mcp](https://playwright.dev/docs/getting-started-mcp) |
| [Apify](services/browser-and-web-execution/apify.md) [![⭐](https://img.shields.io/github/stars/apify/crawlee?style=social)](https://github.com/apify/crawlee) | Real-time web data for AI — Actor marketplace & API | Actor runs · Dataset export · Proxies · Schedules · Webhooks | ⚠️ | API token → [Apify API v2](https://docs.apify.com/api/v2) — JS/Python `apify-client` |
| [Cloudflare Browser Rendering](services/browser-and-web-execution/cloudflare-browser-rendering.md) [![⭐](https://img.shields.io/github/stars/cloudflare/workers-sdk?style=social)](https://github.com/cloudflare/workers-sdk) | Headless Chrome on Cloudflare for AI agents | Workers bindings · Playwright/Puppeteer · Browser Run · Playwright MCP · REST API | ✅ | [Browser Rendering](https://developers.cloudflare.com/browser-rendering/) — [Use with AI](https://developers.cloudflare.com/browser-rendering/how-to/ai/) |
| [Olostep](services/browser-and-web-execution/olostep.md) [![⭐](https://img.shields.io/github/stars/olostep/olostep-mcp-server?style=social)](https://github.com/olostep/olostep-mcp-server) | Web data API for AI agents | Scrape · Search · Map · Crawl · Batch · Official MCP | ✅ | API key → [docs.olostep.com](https://docs.olostep.com) — `npx -y olostep-mcp` or remote `https://mcp.olostep.com/mcp` |
| [Lightpanda](services/browser-and-web-execution/lightpanda.md) [![⭐](https://img.shields.io/github/stars/lightpanda-io/browser?style=social)](https://github.com/lightpanda-io/browser) | Headless browser for AI agents and automation | CDP · `fetch --dump markdown` · Built-in MCP (`lightpanda mcp`) | ✅ | [Install binary or Docker](https://github.com/lightpanda-io/browser#install) → `lightpanda serve` — [MCP guide](https://lightpanda.io/docs/open-source/guides/mcp-server) |
| [Vessel Browser](services/browser-and-web-execution/vessel-browser.md) [![⭐](https://img.shields.io/github/stars/unmodeled-tyler/vessel-browser?style=social)](https://github.com/unmodeled-tyler/vessel-browser) | Built from the ground-up for agents — durable state, action undo, MCP control, BYOK | Named durable sessions · Action undo · Checkpoints · Agent-editable bookmarks · MCP | ✅ | `npm install -g vessel-browser` then `vessel-browser --mcp` (or Linux AppImage) |
| [CamoFox Browser](services/browser-and-web-execution/camofox.md) [![⭐](https://img.shields.io/github/stars/jo-inc/camofox-browser?style=social)](https://github.com/jo-inc/camofox-browser) | Stealth headless browser for AI agents | Stealth sessions · Server/CLI control · Credential-safe profiles · Screenshots/extraction | ⚠️ | `npm install -g camofox-browser` then start the browser server |
| [Moli](services/browser-and-web-execution/moli.md) [![⭐](https://img.shields.io/github/stars/lexmount/moli?style=social)](https://github.com/lexmount/moli) | Structured-first browser engine for AI agents | Semantic tree · stable node IDs · CDP/WebDriver · screenshots · stdio MCP | ✅ | Build the Rust workspace, then run `moli fetch`, `moli serve`, or `moli mcp` |
| [Kernel](services/browser-and-web-execution/kernel.md) [![⭐](https://img.shields.io/github/stars/kernel/kernel-images?style=social)](https://github.com/kernel/kernel-images) | you build agents. we give them the internet. | Sandboxed Chromium · managed auth · live view/replay · CLI + kernel-cli skill | ⚠️ | `brew install kernel/tap/kernel` or `npm install -g @onkernel/cli`, then `kernel browsers create -o json` |
| [Stealth Browser MCP](services/browser-and-web-execution/stealth-browser-mcp.md) [![⭐](https://img.shields.io/github/stars/vibheksoni/stealth-browser-mcp?style=social)](https://github.com/vibheksoni/stealth-browser-mcp) | Stealth browser automation for MCP-compatible AI agents | nodriver + CDP · 97 MCP tools · dynamic network hooks · element cloning | ✅ | Clone [vibheksoni/stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp), `pip install -r requirements.txt`, then `claude mcp add-json stealth-browser-mcp` |

---

## 3. Tool Access & Integration Services

**MCP servers, OAuth brokers, and registries** — the Model Context Protocol (MCP) keyword space for agents that need discoverable tools without human-in-the-loop wiring.

> Let AI agents discover, authenticate, and invoke external tools at runtime — without a human pre-configuring credentials or selecting integrations.

→ **[Full category overview and criteria](services/tool-access-and-integration/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Apify MCP Server](services/tool-access-and-integration/apify-mcp-server.md) [![⭐](https://img.shields.io/github/stars/apify/apify-mcp-server?style=social)](https://github.com/apify/apify-mcp-server) | MCP access to Apify Actors for agent web data tasks | Actor discovery/execution · dataset retrieval · x402/Skyfire payments | ✅ | Connect the official remote MCP endpoint following the [repository README](https://github.com/apify/apify-mcp-server) |
| [Composio](services/tool-access-and-integration/composio.md) [![⭐](https://img.shields.io/github/stars/ComposioHQ/composio?style=social)](https://github.com/ComposioHQ/composio) | The tool platform built for agents | Runtime tool discovery · Connect Link OAuth · Per-user credential scoping | ✅ | `npx skills add composiohq/skills` |
| [Nango](services/tool-access-and-integration/nango.md) [![⭐](https://img.shields.io/github/stars/NangoHQ/nango?style=social)](https://github.com/NangoHQ/nango) | OAuth and credential layer for AI agents | `getConnection()` · Automatic token refresh · 700+ API integrations | ✅ | `$skills install @NangoHQ/sync-builder-skill` |
| [Toolhouse](services/tool-access-and-integration/toolhouse.md) | Repetitive tasks, done for you, by AI workers | Agent endpoint · MCP tool registry · Built-in RAG · Cron scheduling | ✅ | `npm install -g toolhouse` then `th deploy` |
| [Smithery](services/tool-access-and-integration/smithery.md) [![⭐](https://img.shields.io/github/stars/arcadeai-labs/smithery-cli?style=social)](https://github.com/arcadeai-labs/smithery-cli) | MCP registry — connect agents to thousands of tools & skills | Hosted remote MCP · CLI install · OAuth brokerage · Skills catalog | ✅ | `npx @smithery/cli@latest setup` — [Smithery docs](https://smithery.ai/docs) |
| [MCP Gateway](services/tool-access-and-integration/mcpgateway.md) | Enterprise MCP — tools, Agent Skills, sandboxes, one URL | Federated MCP · Semantic tool search · RBAC · Warm sandboxes | ✅ | `pip install mcpgateway-sdk` — [mcpgateway.com](https://mcpgateway.com) |
| [ClawHub](services/tool-access-and-integration/clawhub.md) [![⭐](https://img.shields.io/github/stars/openclaw/clawhub?style=social)](https://github.com/openclaw/clawhub) | OpenClaw skill marketplace — vector search, versioning, CLI | Skill versions & tags · Embedding search · `SKILL.md` registry · OpenClaw packages | ⚠️ | `npx clawhub@latest search <topic>` — [claw-hub.net](https://claw-hub.net/) |
| [Arcade](services/tool-access-and-integration/arcade.md) [![⭐](https://img.shields.io/github/stars/ArcadeAI/arcade-mcp?style=social)](https://github.com/ArcadeAI/arcade-mcp) | MCP tools with managed OAuth | Authorized tool calling · Secrets off-LLM · Pre-built integrations | ✅ | `uv tool install arcade-mcp` → `arcade new my_server` — [docs.arcade.dev](https://docs.arcade.dev) |
| [Framelink MCP for Figma](services/tool-access-and-integration/framelink-figma-mcp.md) [![⭐](https://img.shields.io/github/stars/GLips/Figma-Context-MCP?style=social)](https://github.com/GLips/Figma-Context-MCP) | Give your coding agent access to your Figma data | LLM-compacted layout/style context · Figma API · stdio MCP | ✅ | `npx -y figma-developer-mcp --figma-api-key=… --stdio` — [quickstart](https://www.framelink.ai/docs/quickstart) |
| [GitHub MCP Server](services/tool-access-and-integration/github-mcp-server.md) [![⭐](https://img.shields.io/github/stars/github/github-mcp-server?style=social)](https://github.com/github/github-mcp-server) | Connect AI agents to GitHub — repos, issues, PRs, Actions | Remote HTTP MCP · OAuth or PAT · Toolsets · Enterprise paths | ✅ | `https://api.githubcopilot.com/mcp/` in MCP host — [repo README](https://github.com/github/github-mcp-server) |
| [MCP Toolbox for Databases](services/tool-access-and-integration/google-mcp-toolbox.md) [![⭐](https://img.shields.io/github/stars/googleapis/mcp-toolbox?style=social)](https://github.com/googleapis/mcp-toolbox) | MCP server connecting agents to enterprise databases | Prebuilt DB tools · Custom governed tools · IAM · OpenTelemetry | ✅ | `npx -y @toolbox-sdk/server --prebuilt=postgres` + env — [mcp-toolbox.dev](https://mcp-toolbox.dev/) |
| [ToolHive](services/tool-access-and-integration/toolhive.md) [![⭐](https://img.shields.io/github/stars/stacklok/toolhive-studio?style=social)](https://github.com/stacklok/toolhive-studio) | Run any MCP server securely, instantly, anywhere | MCP server discovery/deploy/manage · secure container runtime | ✅ | [stacklok.com/download](https://stacklok.com/download/) |
| [Obot](services/tool-access-and-integration/obot.md) [![⭐](https://img.shields.io/github/stars/obot-platform/obot?style=social)](https://github.com/obot-platform/obot) | Complete MCP Platform — Hosting, Registry, Gateway, Chat Client | Hosted MCP servers · Registry · Gateway · OAuth 2.1 · RBAC | ✅ | `helm install obot obot/obot` (or Docker) — [obot.ai](https://obot.ai) |
| [Snyk Agent Scan](services/tool-access-and-integration/snyk-agent-scan.md) [![⭐](https://img.shields.io/github/stars/snyk/agent-scan?style=social)](https://github.com/snyk/agent-scan) | Security scanner for AI agents, MCP servers and agent skills | Agent component inventory · MCP inspection · Prompt/tool risk detection · CI gates | ✅ | `uvx snyk-agent-scan@latest scan` |
| [OpenChatCut](services/tool-access-and-integration/openchatcut.md) [![⭐](https://img.shields.io/github/stars/0xsline/OpenChatCut?style=social)](https://github.com/0xsline/OpenChatCut) | Local-first agent-native video editor with editable timelines | Agent Skill · Streamable HTTP MCP · isolated drafts · EditorCore tools | ✅ | `npx skills add 0xsline/OpenChatCut`, then ask the agent: `Set up OpenChatCut` |
| [Toolport](services/tool-access-and-integration/toolport.md) [![⭐](https://img.shields.io/github/stars/tsouth89/toolport?style=social)](https://github.com/tsouth89/toolport) | Every tool. One port. | Lazy MCP meta-tools · per-client profiles · tool integrity · keychain secrets | ✅ | Install from [GitHub Releases](https://github.com/tsouth89/toolport/releases/latest), add servers, then connect each AI client to `toolport-gateway` |
| [SandBase CLI](services/tool-access-and-integration/sandbase-cli.md) [![⭐](https://img.shields.io/github/stars/sandbaseai/cli?style=social)](https://github.com/sandbaseai/cli) | Give your AI agent superpowers. One command. 2,000+ AI models. | Local MCP bridge · discover/inspect/run · client-scoped credentials · Agent Skill | ✅ | Immutable `v0.1.17` tarball: `npx -y https://github.com/sandbaseai/cli/releases/download/v0.1.17/sandbaseai-cli-0.1.17.tgz connect`, then `npx skills add sandbaseai/cli --skill sandbase` |
| [ContextForge](services/tool-access-and-integration/contextforge.md) [![⭐](https://img.shields.io/github/stars/IBM/mcp-context-forge?style=social)](https://github.com/IBM/mcp-context-forge) | Registry and proxy that federates MCP, A2A, and REST/gRPC | Federated MCP · A2A routing · gRPC-to-MCP · UAID · OTEL | ✅ | `uvx --from mcp-contextforge-gateway mcpgateway --host 0.0.0.0 --port 4444` — or `docker pull ghcr.io/ibm/mcp-context-forge:latest` |
| [MCP Gateway & Registry](services/tool-access-and-integration/mcp-gateway-registry.md) [![⭐](https://img.shields.io/github/stars/agentic-community/mcp-gateway-registry?style=social)](https://github.com/agentic-community/mcp-gateway-registry) | Unified Agent & MCP Server Registry – Gateway for AI Development Tools | IdP gateway · virtual MCP · A2A registry · 3LO egress · audit | ✅ | `git clone https://github.com/agentic-community/mcp-gateway-registry && ./build_and_run.sh --prebuilt` |
| [MCPHub](services/tool-access-and-integration/mcphub.md) [![⭐](https://img.shields.io/github/stars/samanhappy/mcphub?style=social)](https://github.com/samanhappy/mcphub) | One gateway for all your MCP servers. | Unified `/mcp` · groups · `$smart` routing · bearer/OAuth · Docker | ✅ | `docker run -p 3000:3000 -v ./data:/app/data samanhappy/mcphub` — then connect to `http://localhost:3000/mcp` |
| [MCPJungle](services/tool-access-and-integration/mcpjungle.md) [![⭐](https://img.shields.io/github/stars/mcpjungle/MCPJungle?style=social)](https://github.com/mcpjungle/MCPJungle) | Run all your MCP servers behind one endpoint | One `/mcp` · tool groups · enterprise client tokens · MPL-2.0 | ✅ | `docker compose up -d` then `mcpjungle register --name context7 --url https://mcp.context7.com/mcp` |

---

## 4. Oversight & Approval Services

> Give AI agents a structured, programmatic way to request human approval before executing high-stakes actions.

→ **[Full category overview and criteria](services/oversight-and-approval/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Cordum](services/oversight-and-approval/cordum.md) [![⭐](https://img.shields.io/github/stars/cordum-io/cordum?style=social)](https://github.com/cordum-io/cordum) | The open agent control plane | Pre-execution policy · approval gates · audit trails | ✅ | Deploy Cordum and connect MCP/framework agents |
| [Sondera Coding Agent Hooks](services/oversight-and-approval/sondera-coding-agent-hooks.md) [![⭐](https://img.shields.io/github/stars/sondera-ai/sondera-coding-agent-hooks?style=social)](https://github.com/sondera-ai/sondera-coding-agent-hooks) | A reference monitor for AI coding agents | Rust hooks · Cedar policies · shell/file/web interception | ⚠️ | Install hook binaries and Cedar policies |
| [HumanLayer](services/oversight-and-approval/humanlayer.md) [![⭐](https://img.shields.io/github/stars/humanlayer/humanlayer?style=social)](https://github.com/humanlayer/humanlayer) | Human in the Loop for AI Agents | `@require_approval()` · Denial-feedback injection · Run/Call ID audit trail | ✅ | `pip install humanlayer` then decorate high-risk functions with `@hl.require_approval()` |
| [Sallyport](services/oversight-and-approval/sallyport.md) [![⭐](https://img.shields.io/github/stars/OlegSotnikov/sallyport?style=social)](https://github.com/OlegSotnikov/sallyport) | Let your agent touch prod. Keep the keys. | MCP credential gate · HTTP/SSH execution · per-call approval · signed journal | ✅ | `brew install --cask olegsotnikov/tap/sallyport`, then add its `sp mcp` command to the agent |
| [Preloop](services/oversight-and-approval/preloop.md) [![⭐](https://img.shields.io/github/stars/preloop/preloop?style=social)](https://github.com/preloop/preloop) | The Open Source Control Plane for AI Agents | MCP firewall · CEL approvals · model gateway budgets · session audit | ✅ | `curl -fsSL https://preloop.ai/install/cli \| sh` then `preloop signup` and `preloop agents discover` |

---

## 5. Commerce & Payment Services

> Give AI agents a verified financial identity and the ability to transact in the real economy.

→ **[Full category overview and criteria](services/commerce-and-payments/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Circle Agent Stack](services/commerce-and-payments/circle-agent-stack.md) | Financial infrastructure for the agentic economy | Agent wallets · marketplace · CLI · x402 gateway · agent skills | ⚠️ | Read https://developers.circle.com/agent-stack and follow the quickstart |
| [OpenLibx402](services/commerce-and-payments/openlibx402.md) [![⭐](https://img.shields.io/github/stars/openlibx402/openlibx402?style=social)](https://github.com/openlibx402/openlibx402) | Open-source library for AI-native x402 integrations | Python/Node SDKs · FastAPI/Express middleware · HTTP 402 flow | ⚠️ | Install the Python or Node SDK from [openlibx402/openlibx402](https://github.com/openlibx402/openlibx402) |
| [Payman AI](services/commerce-and-payments/payman-ai.md) | Agentic AI that does the banking. Under your control. | Policy-gated transaction · Intent reasoning · Execution trace | ✅ | Review the [current API license](https://paymanai.com/api-license), then request API access; no current public SDK package was verified |
| [Skyfire](services/commerce-and-payments/skyfire.md) | Identity and payments for autonomous AI agents | KYA identity token · Agent wallet · KYAPay open protocol | ⚠️ | Register at skyfire.xyz/product — receive agent wallet + KYA identity token |
| [AgentsPay](services/commerce-and-payments/agentspay.md) | Crypto identity and embedded wallets for AI agents | W3C DID on Base L2 · USDC wallet · MCP-native API gateway | ✅ | Provision wallet at agentspay.dev, then use MCP-native gateway |
| [Nevermined](services/commerce-and-payments/nevermined.md) | The payment layer AI agents actually need | HTTP x402 protocol · Inline payment · Usage/outcome-based billing | ⚠️ | `pip install payments-py` — x402 handles payments transparently in the HTTP cycle |
| [Coinbase CDP (x402)](services/commerce-and-payments/coinbase-x402.md) [![⭐](https://img.shields.io/github/stars/coinbase/x402?style=social)](https://github.com/coinbase/x402) | HTTP 402 payments for autonomous API clients | Facilitator verify/settle · Multi-language SDKs · Bazaar discovery | ⚠️ | [docs.cdp.coinbase.com/x402](https://docs.cdp.coinbase.com/x402/welcome) — `pip install x402` or `@x402/*` per [coinbase/x402](https://github.com/coinbase/x402) |
| [CyMetica AI (EventTrader)](services/commerce-and-payments/cymetica-ai.md) | Agentically engineered financial platform with autonomous AI trading agents | A2A envelopes · MCP descriptor · prediction markets · market-making loops | ✅ | Read `https://cymetica.com/.well-known/agent.json` and `https://cymetica.com/.well-known/mcp.json` |
| [SecondSign Core](services/commerce-and-payments/secondsign-core.md) [![⭐](https://img.shields.io/github/stars/Bestpart-Irene/secondsign-core?style=social)](https://github.com/Bestpart-Irene/secondsign-core) | Independent transaction co-signer for financial AI agents | Policy engine · mTLS gateway/approver · execute-once rail · hash-chained receipts | ⚠️ | `pip install secondsign-core` then `python examples/quickstart.py` (pre-1.0 evaluation) |
| [UCP](services/commerce-and-payments/ucp.md) [![⭐](https://img.shields.io/github/stars/Universal-Commerce-Protocol/ucp?style=social)](https://github.com/Universal-Commerce-Protocol/ucp) | The common language for platforms, agents, and businesses | Capability profiles · checkout sessions · OAuth linking · AP2 payments | ⚠️ | Read [ucp.dev](https://ucp.dev) then `cargo install ucp-schema` — samples/SDKs under [Universal-Commerce-Protocol](https://github.com/orgs/Universal-Commerce-Protocol/repositories) |
| [AP2](services/commerce-and-payments/ap2.md) [![⭐](https://img.shields.io/github/stars/google-agentic-commerce/AP2?style=social)](https://github.com/google-agentic-commerce/AP2) | An open protocol for the emerging Agent Economy | Checkout/payment mandates · VDC chain · A2A/UCP extension | ⚠️ | `uv pip install git+https://github.com/google-agentic-commerce/AP2.git@main` — last code push 2026-06-17 |
| [MPP](services/commerce-and-payments/mpp.md) [![⭐](https://img.shields.io/github/stars/wevm/mppx?style=social)](https://github.com/wevm/mppx) | MPP lets agents pay for services on the web, extensible to any payment method | HTTP 402 Challenge/Credential/Receipt · Tempo sessions · MCP transport · `mppx` | ⚠️ | `npm i mppx` then `Mppx.create({ methods: [tempo({ account })] })` — [quickstart](https://mpp.dev/quickstart/client.md) |

---

## 6. Agent Runtime & Infrastructure Services

> Provide the secure deployment substrate, session isolation, secret management, identity, gateway, and observability required to run agents in production.

→ **[Full category overview and criteria](services/agent-runtime-and-infrastructure/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [agentOS by Fiserv](services/agent-runtime-and-infrastructure/fiserv-agentos.md) | Governed operating layer for deploying AI agents in banking | Governance guardrails · Audit trail · HITL controls · Agent marketplace | ⚠️ | Start at https://www.fiserv.com/en/lp/agentos-by-fiserv.html |
| [ATXP](services/agent-runtime-and-infrastructure/atxp.md) [![⭐](https://img.shields.io/github/stars/atxp-dev/atxp?style=social)](https://github.com/atxp-dev/atxp) | Wallet + paid MCP runtime layer for AI agents | Agent wallet · Paid MCP tool invocation · Per-call pricing/authorization | ✅ | [ATXP docs](https://docs.atxp.ai) — CLI / SDK / MCP-compatible endpoints |
| [Claude Peers](services/agent-runtime-and-infrastructure/claude-peers.md) [![⭐](https://img.shields.io/github/stars/louislva/claude-peers-mcp?style=social)](https://github.com/louislva/claude-peers-mcp) | Claude Code sessions discover peers and message each other locally | Peer discovery · Ad-hoc messaging · Channel push · Repo/directory scope | ✅ | Clone repo → `bun install` → `claude mcp add` per [README](https://github.com/louislva/claude-peers-mcp/blob/main/README.md) |
| [acpx](services/agent-runtime-and-infrastructure/acpx.md) [![⭐](https://img.shields.io/github/stars/openclaw/acpx?style=social)](https://github.com/openclaw/acpx) | Headless ACP CLI — agents talk to coding agents over structured protocol | Persistent sessions · Prompt queueing · Cooperative cancel · Structured output | N/A | `npm install -g acpx` then `acpx codex "fix the tests"` |
| [Codex plugin for Claude Code](services/agent-runtime-and-infrastructure/codex-plugin-cc.md) [![⭐](https://img.shields.io/github/stars/openai/codex-plugin-cc?style=social)](https://github.com/openai/codex-plugin-cc) | Use Codex from Claude Code for review or delegated Codex tasks | Review · Adversarial review · Rescue subagent · Background jobs · Optional review gate | N/A | `/plugin marketplace add openai/codex-plugin-cc` then `/plugin install codex@openai-codex` per [README](https://github.com/openai/codex-plugin-cc/blob/main/README.md) |
| [OpenAI Symphony](services/agent-runtime-and-infrastructure/openai-symphony.md) [![⭐](https://img.shields.io/github/stars/openai/symphony?style=social)](https://github.com/openai/symphony) | Turns project work into isolated, autonomous Codex implementation runs | Issue polling · isolated workspaces · WORKFLOW.md policy · JSON status | ⚠️ | Read the [specification and reference implementation](https://github.com/openai/symphony); evaluate in a trusted environment before production use |
| [Multica](services/agent-runtime-and-infrastructure/multica.md) [![⭐](https://img.shields.io/github/stars/multica-ai/multica?style=social)](https://github.com/multica-ai/multica) | AI-native PM — agents as first-class teammates; local daemon runs Claude / Codex | Agent assignee · Claimed task queue · Isolated run workspaces · Team skills · WebSocket | ⚠️ | `brew install multica-cli` → `multica login` → `multica daemon start` — [CLI guide](https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md) |
| [cx](services/agent-runtime-and-infrastructure/cx.md) [![⭐](https://img.shields.io/github/stars/ind-igo/cx?style=social)](https://github.com/ind-igo/cx) | Semantic code navigation for AI agents without a language server | Tree-sitter index · overview/symbols/definition/references · TOON + `--json` · `cx skill` | N/A | `cargo install cx-cli` → `cx lang add …` → `cx skill >> AGENTS.md` |
| [Chrome DevTools MCP](services/agent-runtime-and-infrastructure/chrome-devtools-mcp.md) [![⭐](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=social)](https://github.com/ChromeDevTools/chrome-devtools-mcp) | MCP server — coding agents control and inspect live Chrome | Puppeteer automation · DevTools debug · Performance traces · stdio MCP | ✅ | `npx -y chrome-devtools-mcp@latest` in MCP config — [repo README](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| [Serena](services/agent-runtime-and-infrastructure/serena.md) [![⭐](https://img.shields.io/github/stars/oraios/serena?style=social)](https://github.com/oraios/serena) | The IDE for your coding agent | Symbol-level MCP tools · LSP or JetBrains backend · Agent memory | ✅ | `uv tool install -p 3.13 serena-agent@latest --prerelease=allow` → `serena init` — [docs](https://oraios.github.io/serena/) |
| [Cloudflare Agents SDK](services/agent-runtime-and-infrastructure/cloudflare-agents-sdk.md) [![⭐](https://img.shields.io/github/stars/cloudflare/agents?style=social)](https://github.com/cloudflare/agents) | Durable, stateful AI agents on Cloudflare Workers and Durable Objects | Agent class · Durable state · Project Think · MCP · Browser Run · Sandbox/Code Mode | ✅ | `npx create-cloudflare@latest --template cloudflare/agents-starter` |
| [Amazon Bedrock AgentCore](services/agent-runtime-and-infrastructure/amazon-bedrock-agentcore.md) | Purpose-built for deploying and scaling dynamic AI agents and tools | Agent runtime · Long-term memory · Identity tokens · Tool gateway · OTEL tracing | ⚠️ | `pip install boto3` — configure AgentCore runtime via AWS SDK |
| [Gemini Enterprise Agent Platform](services/agent-runtime-and-infrastructure/vertex-ai-agent-engine.md) | Scale your agents (formerly Vertex AI Agent Engine) | Managed runtime · Sessions · Memory Bank · Code execution · A2A · Agent identity | ⚠️ | `pip install "google-cloud-aiplatform[agent_engines,adk]"` — [scale docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) |
| [Claude Managed Agents](services/agent-runtime-and-infrastructure/claude-managed-agents.md) | Managed agents, sessions, and environments on the Claude API | Versioned agents · Stateful sessions · Container environments · Skills & Files (beta) | ⚠️ | `pip install anthropic` — [Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart) + [beta headers](https://platform.claude.com/docs/en/api/beta-headers) |
| [Infisical Agent Sentinel](services/agent-runtime-and-infrastructure/infisical-agent-sentinel.md) [![⭐](https://img.shields.io/github/stars/Infisical/infisical?style=social)](https://github.com/Infisical/infisical) | Secrets and credential governance for AI agents | Dynamic secret generation · Token lifecycle daemon · Per-agent policy | ✅ | `npx -y @infisical/mcp` or deploy the agent daemon sidecar |
| [APort Agent Guardrails](services/agent-runtime-and-infrastructure/aport-agent-guardrails.md) [![⭐](https://img.shields.io/github/stars/aporthq/aport-agent-guardrails?style=social)](https://github.com/aporthq/aport-agent-guardrails) | Pre-action authorization guardrails for AI agents | OAP passport · Policy verification · Tool-call audit log | ❌ | `npx @aporthq/aport-agent-guardrails` then choose `openclaw`, `cursor`, `claude-code`, `langchain`, or `crewai` |
| [Letta](services/agent-runtime-and-infrastructure/letta.md) [![⭐](https://img.shields.io/github/stars/letta-ai/letta?style=social)](https://github.com/letta-ai/letta) | The fastest way to bring stateful agents to production | Stateful agent · Model-agnostic state · Agent templates · Self-editing memory | ✅ | `pip install letta-client` then `client.agents.create(...)` |
| [Aembit](services/agent-runtime-and-infrastructure/aembit.md) | Secretless workload identity and access management for AI agents | Agent workload identity · Blended identity · JIT credentials · Anomaly detection | ✅ | Configure Aembit access policy — agent requests JIT credentials at runtime, no code changes |
| [db9](services/agent-runtime-and-infrastructure/db9.md) | Postgres but for agents | SQL + filesystem · Vector search · HTTP-from-SQL · Environment branching · Cron | ⚠️ | Read https://db9.ai/skill.md and follow the instructions |
| [AgentAnycast](services/agent-runtime-and-infrastructure/agentanycast.md) [![⭐](https://img.shields.io/github/stars/AgentAnycast/agentanycast?style=social)](https://github.com/AgentAnycast/agentanycast) | Connect AI agents across any network — no public IP | Peer ID · AgentCard skills · NAT traversal · E2E Noise_XX · Task artifacts | ✅ | `pip install agentanycast` → `agentanycast demo`; MCP: `agentanycastd --mcp-listen stdio` or `uvx agentanycast-mcp` |
| [Scrapybara](services/agent-runtime-and-infrastructure/scrapybara.md) [![⭐](https://img.shields.io/github/stars/Scrapybara/scrapybara-python?style=social)](https://github.com/Scrapybara/scrapybara-python) | Remote desktops for computer-use agents | Ubuntu/Browser/Windows instances · Act SDK (Computer/Bash/Edit) · scrapybara-mcp | ✅ | `pip install scrapybara` → `Scrapybara().start_ubuntu()` — [Act SDK](https://docs.scrapybara.com/act-sdk) |
| [Agentuity](services/agent-runtime-and-infrastructure/agentuity.md) [![⭐](https://img.shields.io/github/stars/agentuity/sdk?style=social)](https://github.com/agentuity/sdk) | Full-stack platform for AI agents | Sandboxes · Storage tools · OTel · Evals on live traffic · Edge deploy | ⚠️ | [agentuity.dev](https://agentuity.dev) — SDK + CLI per docs |
| [Modal](services/agent-runtime-and-infrastructure/modal.md) [![⭐](https://img.shields.io/github/stars/modal-labs/modal-client?style=social)](https://github.com/modal-labs/modal-client) | Serverless AI infra — GPUs, inference, sandboxes, batch | Elastic containers · Programmatic sandboxes · Sub-second cold start | ❌ | `pip install modal` → `modal setup` — [modal.com/docs](https://modal.com/docs) |
| [Cyberdesk](services/agent-runtime-and-infrastructure/cyberdesk.md) [![⭐](https://img.shields.io/github/stars/cyberdesk-hq/cyberdesk?style=social)](https://github.com/cyberdesk-hq/cyberdesk) | Open source virtual desktops for AI agents | Desktop lifecycle API · computer actions · isolated sessions | ⚠️ | `pip install cyberdesk` — [docs.cyberdesk.io](https://docs.cyberdesk.io) |
| [Polos](services/agent-runtime-and-infrastructure/polos.md) [![⭐](https://img.shields.io/github/stars/polos-dev/polos?style=social)](https://github.com/polos-dev/polos) | Open-source runtime for AI agents — sandbox + durable workflow + HITL | Docker/E2B sandbox · Durable steps with prompt cache · HTTP/cron/webhook/event triggers · Slack HITL | ⚠️ | `pip install polos` (or `npm install polos`) — see [README](https://github.com/polos-dev/polos) |
| [Cloudflare Computer](services/agent-runtime-and-infrastructure/cloudflare-computer.md) [![⭐](https://img.shields.io/github/stars/cloudflare/computer?style=social)](https://github.com/cloudflare/computer) | Give your agent a computer | Durable Object workspace FS · runtime.exec backends · preview APIs | ⚠️ | `npm install @cloudflare/computer` then `withWorkspace` on a Durable Object — preview only |
| [Agent Executor (AX)](services/agent-runtime-and-infrastructure/google-ax.md) [![⭐](https://img.shields.io/github/stars/google/ax?style=social)](https://github.com/google/ax) | An open source distributed agent runtime | Conversation resume · event log · isolated harnesses · `ax` CLI | ⚠️ | `go install github.com/google/ax/cmd/ax@latest` then `ax --input "…"` |
| [Agent Substrate](services/agent-runtime-and-infrastructure/agent-substrate.md) [![⭐](https://img.shields.io/github/stars/agent-substrate/substrate?style=social)](https://github.com/agent-substrate/substrate) | High-density Kubernetes runtime for large-scale agent deployments | Actors · WorkerPools · suspend/resume · atenet routing | ⚠️ | `hack/install-ate-kind.sh --deploy-ate-system` then `kubectl ate create actor` — early-dev, not a supported Google product |
| [SandBase Harness](services/agent-runtime-and-infrastructure/sandbase-harness.md) [![⭐](https://img.shields.io/github/stars/sandbaseai/sandbase-harness?style=social)](https://github.com/sandbaseai/sandbase-harness) | A local-first runtime for AI agents. | HTTP/API · stdio MCP · TypeScript runtime/CLI · Docker/Kubernetes/workers | ✅ | Follow the [installation guide](https://github.com/sandbaseai/sandbase-harness/blob/main/docs/installation.md) and `server.json` MCP metadata |

---

## 7. Agent Harnesses & Operator Surfaces

> Wrap capable agents with durable objectives, orchestration, verification, policy, or a purpose-built live surface for operating concrete sessions.

→ **[Full category overview and criteria](services/agent-harnesses-and-control-planes/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [oh-my-codex (OMX)](services/agent-harnesses-and-control-planes/oh-my-codex.md) [![⭐](https://img.shields.io/github/stars/Yeachan-Heo/oh-my-codex?style=social)](https://github.com/Yeachan-Heo/oh-my-codex) | Workflow and multi-agent runtime layer for OpenAI Codex CLI | Durable goals · role workflows · teams/worktrees · authority leases · replay | ⚠️ | `npm install -g oh-my-codex` → `omx setup --scope project --merge-agents` → `omx doctor` |
| [Ruflo](services/agent-harnesses-and-control-planes/ruflo.md) [![⭐](https://img.shields.io/github/stars/ruvnet/ruflo?style=social)](https://github.com/ruvnet/ruflo) | Agent meta-harness for Claude Code and Codex | Swarms · memory · background workers · federation · budgets | ✅ | `npx ruflo@latest init --codex` |
| [QM](services/agent-harnesses-and-control-planes/qm.md) [![⭐](https://img.shields.io/github/stars/yc-software/qm?style=social)](https://github.com/yc-software/qm) | Multiplayer agent harness for work | Personal/shared scopes · durable sandboxes · policy · crons/watches | ⚠️ | `npm exec --yes --package=@yc-software/qm@latest -- qm init . --org <slug> --target <fly-or-aws>` |
| [LongHorizon-Harness](services/agent-harnesses-and-control-planes/longhorizon-harness.md) [![⭐](https://img.shields.io/github/stars/AMAP-ML/LongHorizon-Harness?style=social)](https://github.com/AMAP-ML/LongHorizon-Harness) | Verified long-horizon loop for desktop and CLI agents | Manager/Executor/Auditor · checkpoints · recovery · evidence | ⚠️ | `uv tool install lh-harness` → `lh-harness init` → `lh-harness run --task "..." --agent codex` |
| [Agent QA](services/agent-harnesses-and-control-planes/agent-qa.md) [![⭐](https://img.shields.io/github/stars/vostride/agent-qa?style=social)](https://github.com/vostride/agent-qa) | The self-improving QA agent for software teams | Live run IDs · observe/plan/execute/verify · memory · queue cancel | ✅ | `npx agent-qa init` → `codex mcp add agent-qa -- agent-qa mcp` |
| [Codex HUD (fwyc0573)](services/agent-harnesses-and-control-planes/codex-hud-fwyc0573.md) [![⭐](https://img.shields.io/github/stars/fwyc0573/codex-hud?style=social)](https://github.com/fwyc0573/codex-hud) | Real-time statusline HUD for OpenAI Codex CLI | Context/tools/subagents · multi-session view · attach/list/kill | ⚠️ | Clone [fwyc0573/codex-hud](https://github.com/fwyc0573/codex-hud), run `./bin/codex-hud-install`, then launch `codex` |
| [Codex HUD (anhannin)](services/agent-harnesses-and-control-planes/codex-hud-anhannin.md) [![⭐](https://img.shields.io/github/stars/anhannin/codex-hud?style=social)](https://github.com/anhannin/codex-hud) | Patched Codex status line for usage and session state | Model/project/git · rollout session · 5-hour and 7-day usage windows | ⚠️ | Clone [anhannin/codex-hud](https://github.com/anhannin/codex-hud), review the patch/install script, then run `Codex-HUD/install.sh` |
| [Claude HUD](services/agent-harnesses-and-control-planes/claude-hud.md) [![⭐](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=social)](https://github.com/jarrodwatts/claude-hud) | A Claude Code plugin that shows what's happening | Context/usage bars · tools · subagents · todos · statusline | ⚠️ | `/plugin marketplace add jarrodwatts/claude-hud` then `/plugin install claude-hud` and `/claude-hud:setup` |
| [LoopX](services/agent-harnesses-and-control-planes/loopx.md) [![⭐](https://img.shields.io/github/stars/huangruiteng/loopx?style=social)](https://github.com/huangruiteng/loopx) | The open, provider-neutral, stateful control plane for long-horizon agents | Objectives · gates · todos/evidence · quota · claims/leases | ⚠️ | `python3 -m pip install --upgrade loopx` then `loopx workflow-skills --install` and `loopx connect` |
| [DeepSeek Harness (dsh)](services/agent-harnesses-and-control-planes/deepseek-harness.md) [![⭐](https://img.shields.io/github/stars/deepseek-ai/deepseek-harness?style=social)](https://github.com/deepseek-ai/deepseek-harness) | Everything is a Plugin. | Cordis plugins · session log · Trajectory · PTC/Code Mode | ⚠️ | `npx @deepseek-ai/dsh web` |

---

## 8. Memory & State Services

**Agent-native databases and memory layers for long-term recall** — temporal graphs, vector stores, and shared agent memory beyond a single chat session.

> Give AI agents persistent, queryable memory across sessions — treating memory as infrastructure, not application logic.

→ **[Full category overview and criteria](services/memory-and-state/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Memmy](services/memory-and-state/memmy-agent.md) [![⭐](https://img.shields.io/github/stars/MemTensor/memmy-agent?style=social)](https://github.com/MemTensor/memmy-agent) | Personal local memory hub shared by AI agents | Shared memory · JSON CLI/REST · lifecycle hooks · bundled Skills | ⚠️ | Clone [MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent), start the local service, then run `memmy-memory init` and `memmy-memory health` |
| [Memoria](services/memory-and-state/memoria.md) [![⭐](https://img.shields.io/github/stars/matrixorigin/Memoria?style=social)](https://github.com/matrixorigin/Memoria) | Persistent memory layer for AI agents with Git-level version control | Snapshots · branches · REST · MCP | ✅ | `memoria serve` or `memoria mcp` |
| [Recall](services/memory-and-state/recall.md) [![⭐](https://img.shields.io/github/stars/RecallWorks/Recall?style=social)](https://github.com/RecallWorks/Recall) | Open-source memory for AI agents. MCP-native. Self-hosted. | Persistent searchable memory · Docker · MCP stdio | ✅ | `uvx ai-recallworks stdio` |
| [Mem0](services/memory-and-state/mem0.md) [![⭐](https://img.shields.io/github/stars/mem0ai/mem0?style=social)](https://github.com/mem0ai/mem0) | The memory layer for your AI agents | Memory extraction · Conflict resolution (ADD/UPDATE/DELETE/NOOP) · Semantic retrieval · 90% token savings | ✅ | `pip install mem0ai` then `m.add(messages, user_id=...)` |
| [Zep](services/memory-and-state/zep.md) [![⭐](https://img.shields.io/github/stars/getzep/zep?style=social)](https://github.com/getzep/zep) | Agent memory powered by a temporal knowledge graph | Temporal knowledge graph · Automatic fact invalidation · Business data fusion · Sub-200ms retrieval | ✅ | `pip install zep-python` then `zep.add_session_message(...)` |
| [Ensue](services/memory-and-state/ensue.md) [![⭐](https://img.shields.io/github/stars/mutable-state-inc/autoresearch-at-home?style=social)](https://github.com/mutable-state-inc/autoresearch-at-home) | The shared memory network for AI agents | Claim · Publish result · Hypothesis exchange · Insight network · Collective best · Hypergraph | ✅ | Read the official [Ensue Skill](https://raw.githubusercontent.com/mutable-state-inc/ensue-skill/main/skills/ensue-memory/SKILL.md) and follow its instructions |
| [OpenViking](services/memory-and-state/openviking.md) [![⭐](https://img.shields.io/github/stars/volcengine/OpenViking?style=social)](https://github.com/volcengine/OpenViking) | The context database for AI agents | `viking://` filesystem · `viking://agent/` namespace · L0/L1/L2 tiered loading · Self-evolution loop | ✅ | `pip install openviking` → `openviking-server` → add MCP at `localhost:8000/mcp` |
| [MemOS](services/memory-and-state/memos.md) [![⭐](https://img.shields.io/github/stars/MemTensor/MemOS?style=social)](https://github.com/MemTensor/MemOS) | A memory OS for LLM and AI agent systems | MemCube · Parametric/activation/plaintext memory · MemScheduler · +43.7% vs OpenAI Memory | ✅ | `pip install memos-core` then `memory.add(...)` / `memory.get(...)` |
| [memU](services/memory-and-state/memu.md) [![⭐](https://img.shields.io/github/stars/NevaMind-AI/memU?style=social)](https://github.com/NevaMind-AI/memU) | Memory for 24/7 proactive AI agents | Dual-mode (Fast Context + Deep Reasoning) · Continuous monitoring · 90% token savings | ⚠️ | `pip install memu` — runs continuous stream monitoring with near-zero idle cost |
| [mem9](services/memory-and-state/mem9.md) | Persistent memory for AI agents | Cloud memory · Hybrid search · Lifecycle hooks · Cross-agent sharing | ⚠️ | Read https://mem9.ai/skill.md and follow the instructions to register and join |
| [LLM Wiki](services/memory-and-state/llm-wiki.md) [![⭐](https://img.shields.io/github/stars/nvk/llm-wiki?style=social)](https://github.com/nvk/llm-wiki) | LLM-compiled knowledge bases for any AI agent | Parallel research · Source ingest · Wiki compile · Deep query · Artifact generation | ⚠️ | `claude plugin install wiki@llm-wiki` — [llm-wiki.net](https://llm-wiki.net/) |
| [LycheeMem](services/memory-and-state/lycheemem.md) [![⭐](https://img.shields.io/github/stars/LycheeMem/LycheeMem?style=social)](https://github.com/LycheeMem/LycheeMem) | Compact memory framework for LLM agents | Working/semantic/procedural stores · Token-budget compression · HTTP MCP · OpenClaw plugin | ✅ | Clone repo → `pip install -e ".[dev]"` → `python main.py` — MCP at `http://localhost:8000/mcp` |
| [MemMachine](services/memory-and-state/memmachine.md) [![⭐](https://img.shields.io/github/stars/MemMachine/MemMachine?style=social)](https://github.com/MemMachine/MemMachine) | Universal memory layer for AI Agents | Episodic graph · Profile SQL · Working memory · LangChain/CrewAI adapters | ⚠️ | `pip install memmachine` then `Memory().add(messages, agent_id=...)` |
| [Cognee](services/memory-and-state/cognee.md) [![⭐](https://img.shields.io/github/stars/topoteretes/cognee?style=social)](https://github.com/topoteretes/cognee) | Memory control plane for AI agents — managed world model | Auto ontology · 28+ connectors · Per-agent permissions · MCP server | ✅ | `pip install cognee` → `cognee.add(docs)` → `cognee.cognify()` → `cognee.search(...)` |
| [Hindsight](services/memory-and-state/hindsight.md) [![⭐](https://img.shields.io/github/stars/vectorize-io/hindsight?style=social)](https://github.com/vectorize-io/hindsight) | Agent Memory That Learns | `retain()` · `recall()` · `reflect()` · Dedicated memory banks | ⚠️ | `pip install hindsight-ai` then use retain/recall/reflect in the agent loop |
| [agentmemory](services/memory-and-state/agentmemory.md) [![⭐](https://img.shields.io/github/stars/rohitg00/agentmemory?style=social)](https://github.com/rohitg00/agentmemory) | Your coding agent remembers everything. No more re-explaining. | Shared memory server · MCP/hooks · 17 skills · INSTALL_FOR_AGENTS.md | ✅ | Read https://raw.githubusercontent.com/rohitg00/agentmemory/main/INSTALL_FOR_AGENTS.md and follow the instructions |
| [TencentDB Agent Memory](services/memory-and-state/tencentdb-agent-memory.md) [![⭐](https://img.shields.io/github/stars/TencentCloud/TencentDB-Agent-Memory?style=social)](https://github.com/TencentCloud/TencentDB-Agent-Memory) | Agents remember,Humans innovate. | Symbolic Mermaid canvas · L0–L3 layering · OpenClaw/Hermes plugins | ⚠️ | `openclaw plugins install @tencentdb-agent-memory/memory-tencentdb` then enable `memory-tencentdb` |
| [MemPalace](services/memory-and-state/mempalace.md) [![⭐](https://img.shields.io/github/stars/MemPalace/mempalace?style=social)](https://github.com/MemPalace/mempalace) | The best-benchmarked open-source AI memory system. And it's free. | Verbatim drawers · wings/rooms · pluggable backends · 44 MCP tools | ✅ | `uv tool install mempalace` then `mempalace init` / `mine` / `search` |
| [MemSearch](services/memory-and-state/memsearch.md) [![⭐](https://img.shields.io/github/stars/zilliztech/memsearch?style=social)](https://github.com/zilliztech/memsearch) | Cross-platform semantic memory for AI coding agents | Markdown + Milvus hybrid search · progressive recall · harness plugins | ⚠️ | `uv tool install "memsearch[onnx]"` or `/plugin marketplace add zilliztech/memsearch` |
| [Claude-Mem](services/memory-and-state/claude-mem.md) [![⭐](https://img.shields.io/github/stars/thedotmack/claude-mem?style=social)](https://github.com/thedotmack/claude-mem) | Persistent memory compression system for Claude Code | Auto-firehose observations · compression worker · session priming · MCP search | ✅ | `npx claude-mem install` or `/plugin marketplace add thedotmack/claude-mem` then `/plugin install claude-mem` |
| [Engram](services/memory-and-state/engram.md) [![⭐](https://img.shields.io/github/stars/Gentleman-Programming/engram?style=social)](https://github.com/Gentleman-Programming/engram) | Persistent memory for AI coding agents | Agent-curated `mem_save`/`mem_search` · SQLite FTS5 · single Go binary | ✅ | `brew install gentleman-programming/tap/engram` then `claude plugin install engram` or `engram setup <agent>` |
| [Beads](services/memory-and-state/beads.md) [![⭐](https://img.shields.io/github/stars/gastownhall/beads?style=social)](https://github.com/gastownhall/beads) | Dependency-aware, Dolt-backed issue tracker built for AI coding agents that survive context loss | `bd ready`/`claim` · hash IDs · Dolt sync · `bd prime` | ✅ | `brew install beads` then `bd init --quiet` and `bd setup claude` |
| [projectmem](services/memory-and-state/projectmem.md) [![⭐](https://img.shields.io/github/stars/riponcm/projectmem?style=social)](https://github.com/riponcm/projectmem) | We don't make AI smarter. We make it experienced. | Typed event log · `pjm precheck` · one MCP for every project | ✅ | `pip install -U projectmem` then `pjm doctor --fix` and wire `python -m projectmem.mcp_server` |
| [Memoir](services/memory-and-state/memoir.md) [![⭐](https://img.shields.io/github/stars/zhangfengcdt/memoir?style=social)](https://github.com/zhangfengcdt/memoir) | Git for AI Memory | Semantic paths · branch/merge · `memoir-mcp` · Alpha | ✅ | `pip install memoir-ai` or `/plugin marketplace add zhangfengcdt/memoir` |
| [Memorix](services/memory-and-state/memorix.md) [![⭐](https://img.shields.io/github/stars/AVIDS2/memorix?style=social)](https://github.com/AVIDS2/memorix) | Local-first shared memory layer for AI coding agents. | Git-root daemon · Workset · Git Memory · `memorix serve` | ✅ | `npm install -g memorix` then `memorix setup --agent claude --global` |
| [Compartment](services/memory-and-state/compartment.md) [![⭐](https://img.shields.io/github/stars/MaxFreedomPollard/Compartment?style=social)](https://github.com/MaxFreedomPollard/Compartment) | Encrypted, fully offline memory for AI agents. | Encrypted vault · one-claim memories · `compartment serve` | ✅ | `pip install compartment && compartment init && compartment integrate claude` |

---

## 9. Search & Web Intelligence Services

> Give AI agents optimized, structured access to web information — returning LLM-ready content tuned for context windows, not raw HTML or human-readable SERPs.

→ **[Full category overview and criteria](services/search-and-web-intelligence/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [contextX](services/search-and-web-intelligence/contextx.md) [![⭐](https://img.shields.io/github/stars/KayanoLiam/ContextX?style=social)](https://github.com/KayanoLiam/ContextX) | Remote MCP search powered by Grok normal and multi-agent deep search | `grok_search` · `grok_deep_search` · Streamable HTTP · read-only public endpoint | ✅ | Connect MCP to `https://mcp.twitter.monster/mcp`; note that upstream publishes no auth, release, or license |
| [Jina DeepSearch](services/search-and-web-intelligence/jina-deepsearch.md) | Agentic search and deep research API for AI applications | Deep search · iterative research · cited answers · HTTP API | ⚠️ | Follow the [Jina DeepSearch API docs](https://jina.ai/deepsearch) |
| [Tavily](services/search-and-web-intelligence/tavily.md) [![⭐](https://img.shields.io/github/stars/tavily-ai/tavily-mcp?style=social)](https://github.com/tavily-ai/tavily-mcp) | Connect your agent to the web | Agent-optimized search · Multi-step research · Source attribution | ✅ | `npx skills add tavily-ai/skills` |
| [Exa](services/search-and-web-intelligence/exa.md) | The search engine designed for AI | Neural/semantic search · `exa-code` for coding agents · Websets | ✅ | `pip install exa-py` then `exa.search(query)` |
| [Parallel](services/search-and-web-intelligence/parallel.md) | The highest accuracy web search for your AI | Search/Task/FindAll/Monitor APIs · Citations · Official MCP | ✅ | `pip install parallel-web` — hosted Search MCP: `https://search.parallel.ai/mcp` · [task-mcp](https://github.com/parallel-web/task-mcp) |
| [Jina Reader](services/search-and-web-intelligence/jina-reader.md) [![⭐](https://img.shields.io/github/stars/jina-ai/reader?style=social)](https://github.com/jina-ai/reader) | URL and SERP as LLM-friendly text | `r.jina.ai` · `s.jina.ai` · MCP · PDF/images | ✅ | `curl "https://r.jina.ai/https://example.com"` — MCP: `mcp.jina.ai` |
| [NotHumanSearch](services/search-and-web-intelligence/nothumansearch.md) | Agent-first search — the index of services designed for AI, not humans | `agentic_score` rank · `check_agent_readiness` · `verify_mcp` JSON-RPC probe · URL Onboarding | ✅ | Read https://nothumansearch.ai/llms.txt and follow the instructions — MCP: `https://nothumansearch.ai/mcp` |
| [Linkup](services/search-and-web-intelligence/linkup.md) [![⭐](https://img.shields.io/github/stars/LinkupPlatform/linkup-python-sdk?style=social)](https://github.com/LinkupPlatform/linkup-python-sdk) | Search API for AI agents and LLM apps | LLM-oriented search · Structured retrieval · Citation-ready outputs | ⚠️ | API key via docs.linkup.so then call search endpoints via SDK/REST |
| [Agent Search MCP](services/search-and-web-intelligence/agent-search-mcp.md) [![⭐](https://img.shields.io/github/stars/lennney/agent-search-mcp?style=social)](https://github.com/lennney/agent-search-mcp) | Free-first web search with inspectable evidence | Evidence packet · free-first policy · budgets · `fasm` CLI | ✅ | `npx -y agent-search-mcp` — optional `npx skills add lennney/agent-search-mcp --skill agent-search` |

---

## 10. Code Execution Services

> Give AI agents a secure, isolated runtime for executing generated code — without human-side sandbox setup and with output formatted for LLM consumption.

→ **[Full category overview and criteria](services/code-execution/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Axern](services/code-execution/axern.md) [![⭐](https://img.shields.io/github/stars/cofy-x/axern?style=social)](https://github.com/cofy-x/axern) | Open-source sandbox platform for AI agents | Local/remote sandboxes · CLI · gRPC/HTTP · Go/Python/TypeScript SDKs · Axrun evidence | ⚠️ | `brew install cofy-x/tap/axern` then `axern local up`; pre-1.0 evaluation software requiring production hardening |
| [OpenSandbox](services/code-execution/opensandbox.md) [![⭐](https://img.shields.io/github/stars/opensandbox-group/OpenSandbox?style=social)](https://github.com/opensandbox-group/OpenSandbox) | Secure, fast, extensible sandbox runtime for AI agents | Sandbox runtime · Kubernetes · MCP server | ✅ | Follow OpenSandbox docs and run MCP server |
| [CodeRunner](services/code-execution/coderunner.md) [![⭐](https://img.shields.io/github/stars/instavm/coderunner?style=social)](https://github.com/instavm/coderunner) | A local sandbox for your AI agents | Apple Containers · local sandbox · MCP | ✅ | Install from GitHub and run isolated agent workloads |
| [E2B](services/code-execution/e2b.md) [![⭐](https://img.shields.io/github/stars/e2b-dev/e2b?style=social)](https://github.com/e2b-dev/e2b) | Cloud for AI agents — secure sandboxes for AI-generated code | Ephemeral Linux VM · ~150ms cold start · Stateful execution context · Streaming output | ✅ | `pip install e2b-code-interpreter` then `with Sandbox() as sandbox:` |
| [Daytona](services/code-execution/daytona.md) [![⭐](https://img.shields.io/github/stars/daytonaio/daytona?style=social)](https://github.com/daytonaio/daytona) | Secure elastic infrastructure for AI-generated code | Sub-90ms sandboxes · Git/LSP/exec · Preview URLs · CLI MCP | ✅ | `brew install daytonaio/cli/daytona` → `daytona login` → `daytona mcp init cursor` — or `pip install daytona` |
| [Runloop](services/code-execution/runloop.md) [![⭐](https://img.shields.io/github/stars/runloopai/api-client-python?style=social)](https://github.com/runloopai/api-client-python) | Your AI agent accelerator | Devbox micro-VM · Snapshot/branch disk state · Benchmark jobs · Suspend/resume | ✅ | `export RUNLOOP_API_KEY=...` → `npm install -g @runloop/rl-cli` → `rli mcp install` — [CLI docs](https://docs.runloop.ai/docs/tools/rl-cli) |
| [Vercel Sandbox](services/code-execution/vercel-sandbox.md) [![⭐](https://img.shields.io/github/stars/vercel/sandbox?style=social)](https://github.com/vercel/sandbox) | Firecracker microVMs for AI-generated code | Node/Python runtimes · Snapshots · REST + `@vercel/sandbox` SDK | ❌ | `npm install @vercel/sandbox` — [vercel.com/docs/vercel-sandbox](https://vercel.com/docs/vercel-sandbox) |
| [AIO Sandbox](services/code-execution/agent-infra-sandbox.md) [![⭐](https://img.shields.io/github/stars/agent-infra/sandbox?style=social)](https://github.com/agent-infra/sandbox) | All-in-one Docker sandbox for AI agents | Browser + shell + files + VS Code + Jupyter + MCP · Shared filesystem | ✅ | `docker run -p 8080:8080 ghcr.io/agent-infra/sandbox:latest` — MCP `http://localhost:8080/mcp` |
| [Agent Sandbox](services/code-execution/agent-sandbox.md) | The trusted runtime for untrusted code | Hosted code sessions · Dependency install · Files/artifacts API · URL onboarding | ⚠️ | Read https://agentsandbox.co/skill.md and follow the instructions |
| [Riza](services/code-execution/riza.md) | AI writes code. Riza runs it. | Command Exec API · Tools API · Secrets · MCP · Self-hosting | ✅ | `uv add rizaio` then `riza.command.exec(...)` — [docs.riza.io](https://docs.riza.io/) |
| [Agent Sandbox (Kubernetes SIG)](services/code-execution/kubernetes-agent-sandbox.md) [![⭐](https://img.shields.io/github/stars/kubernetes-sigs/agent-sandbox?style=social)](https://github.com/kubernetes-sigs/agent-sandbox) | Secure isolated execution layer for autonomous agents on Kubernetes | Sandbox CRD · WarmPool/Claim · RuntimeClass · Python/Go SDKs | ⚠️ | `pip install k8s-agent-sandbox` then `SandboxClient().create_sandbox(...)` — not hosted agentsandbox.co |
| [Clawk](services/code-execution/clawk.md) [![⭐](https://img.shields.io/github/stars/clawkwork/clawk?style=social)](https://github.com/clawkwork/clawk) | Give a coding agent its own disposable Linux machine, not yours | Local hypervisor VM · DNS-aware egress allow-list · `status --json` · snapshot/destroy | ⚠️ | `brew install clawkwork/tap/clawk` then `cd <repo> && clawk` (pre-1.0; macOS Apple silicon) |
| [Dormice](services/code-execution/dormice.md) [![⭐](https://img.shields.io/github/stars/BitMiracle-AI/Dormice?style=social)](https://github.com/BitMiracle-AI/Dormice) | The SQLite of agent sandboxes — self-hosted, idle costs nothing | Idempotent `acquireSandbox` · freeze/stop/archive · HTTP RPC · E2B SDK compat | ⚠️ | `curl -fsSL https://raw.githubusercontent.com/BitMiracle-AI/Dormice/main/deploy/install.sh \| bash` then `npx skills add BitMiracle-AI/Dormice` (early-dev) |

---

## 11. Observability & Tracing Services

> Give teams structured visibility into agent execution — full trajectory tracing, evaluation datasets, and cost attribution.

→ **[Full category overview and criteria](services/observability-and-tracing/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [numbat](services/observability-and-tracing/numbat.md) [![⭐](https://img.shields.io/github/stars/perplexityai/numbat?style=social)](https://github.com/perplexityai/numbat) | Endpoint visibility into AI agent activity | Local detection · optional pre-action blocking · forensic reconstruction · OTLP/NDJSON | ⚠️ | Build/install from [perplexityai/numbat](https://github.com/perplexityai/numbat), then configure its agent hooks and telemetry endpoint |
| [Agent Trace](services/observability-and-tracing/agent-trace.md) [![⭐](https://img.shields.io/github/stars/Siddhant-K-code/agent-trace?style=social)](https://github.com/Siddhant-K-code/agent-trace) | Observability for AI agents | CLI · traces · cost/tool visibility | ⚠️ | Install `agent-strace` from PyPI/GitHub and wrap agent runs |
| [agent-inspect](services/observability-and-tracing/agent-inspect.md) [![⭐](https://img.shields.io/github/stars/rajudandigam/agent-inspect?style=social)](https://github.com/rajudandigam/agent-inspect) | Local execution trees for TypeScript AI agents | TS instrumentation · execution trees · run metadata | ⚠️ | Add to a TypeScript agent project |
| [LangWatch](services/observability-and-tracing/langwatch.md) [![⭐](https://img.shields.io/github/stars/langwatch/langwatch?style=social)](https://github.com/langwatch/langwatch) | Open-source LLM Ops for tracing, evals, and guardrails | Agent traces · evaluations · datasets · guardrails · SDK/API | ⚠️ | Install the LangWatch SDK and follow the [official quickstart](https://docs.langwatch.ai) |
| [Langfuse](services/observability-and-tracing/langfuse.md) [![⭐](https://img.shields.io/github/stars/langfuse/langfuse?style=social)](https://github.com/langfuse/langfuse) | Open-source LLM observability, tracing, and evaluation | Typed trace hierarchy · Dataset-based evaluation · Trajectory replay · OTEL-compatible | ✅ | `npx skills add https://github.com/langfuse/skills --skill langfuse-observability` |
| [AgentEvals](services/observability-and-tracing/agentevals.md) [![⭐](https://img.shields.io/github/stars/agentevals-dev/agentevals?style=social)](https://github.com/agentevals-dev/agentevals) | Score agent behavior from OpenTelemetry traces — no re-runs | Golden eval sets · Tool trajectory matching · OTLP ingest · MCP | ✅ | `pip install agentevals-cli` → `agentevals run <trace> --eval-set <set> -m tool_trajectory_avg_score` |
| [AgentOps](services/observability-and-tracing/agentops.md) [![⭐](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=social)](https://github.com/AgentOps-AI/agentops) | Testing, debugging, and deploying AI agents and LLM apps | Session waterfall · Framework auto-instrumentation · Public trace API | ⚠️ | `pip install agentops` → `agentops.init(<API_KEY>)` |
| [Braintrust](services/observability-and-tracing/braintrust.md) [![⭐](https://img.shields.io/github/stars/braintrustdata/autoevals?style=social)](https://github.com/braintrustdata/autoevals) | AI observability & evals — traces, datasets, OpenAI Agents | Trace processors · Eval experiments · Trace→dataset · IDE MCP | ✅ | `pip install "braintrust[openai-agents]"` — MCP: [Braintrust MCP](https://www.braintrust.dev/docs/integrations/developer-tools/mcp) |
| [Galileo](services/observability-and-tracing/galileo.md) | Agent reliability platform — observability, evals, and IDE MCP | Signals (root-cause insights) · synthetic datasets · experiments · MCP tools | ✅ | Add MCP URL `https://api.galileo.ai/mcp/http/mcp` with `Galileo-API-Key` header — [setup docs](https://docs.galileo.ai/getting-started/mcp/setup-galileo-mcp) |
| [Laminar](services/observability-and-tracing/laminar.md) [![⭐](https://img.shields.io/github/stars/lmnr-ai/lmnr?style=social)](https://github.com/lmnr-ai/lmnr) | Open-source observability for long-running agents | Agent debugger (rerun at step N) · Browser session replay · Signals · SQL over traces · Apache 2.0 self-host | ⚠️ | `pip install lmnr` then `Laminar.initialize()` — self-host: `git clone https://github.com/lmnr-ai/lmnr && docker compose up -d` |
| [OpenLIT](services/observability-and-tracing/openlit.md) [![⭐](https://img.shields.io/github/stars/openlit/openlit?style=social)](https://github.com/openlit/openlit) | OpenTelemetry-native observability for LLMs and AI agents | Agent traces · Tool-call spans · Cost/token analytics | ✅ | `pip install openlit` then configure OpenTelemetry export |
| [AgentSight](services/observability-and-tracing/agentsight.md) [![⭐](https://img.shields.io/github/stars/eunomia-bpf/agentsight?style=social)](https://github.com/eunomia-bpf/agentsight) | Lightweight system-level observability for AI Agents | eBPF `record` · session DBs · `top`/`vis` · OTLP GenAI | ⚠️ | `cargo install agentsight` then `agentsight top` or `sudo agentsight record -- claude` |
| [Kitaru](services/observability-and-tracing/kitaru.md) [![⭐](https://img.shields.io/github/stars/zenml-io/kitaru?style=social)](https://github.com/zenml-io/kitaru) | Traces you can run, not just read — replay-based evals for AI agents | Sessions · replay · cohorts · experiments · MCP + Skills | ✅ | `uv add "kitaru[cli,worker,mcp]"` then `npx skills add zenml-io/kitaru-skills` — [docs](https://docs.zenml.io/kitaru) |

---

## 12. Durable Execution & Scheduling Services

> Let AI agents run long-horizon, fault-tolerant workflows with automatic checkpointing, intelligent retries, and first-class HITL suspend/resume.

→ **[Full category overview and criteria](services/durable-execution-and-scheduling/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Trigger.dev](services/durable-execution-and-scheduling/trigger-dev.md) [![⭐](https://img.shields.io/github/stars/triggerdotdev/trigger.dev?style=social)](https://github.com/triggerdotdev/trigger.dev) | Build and deploy fully-managed AI agents and workflows | No-timeout tasks · Step checkpointing · HITL waitForApproval · Streaming response | ❌ | `npx skills add triggerdotdev/skills` |
| [Inngest](services/durable-execution-and-scheduling/inngest.md) [![⭐](https://img.shields.io/github/stars/inngest/inngest?style=social)](https://github.com/inngest/inngest) | Durable execution for AI agents in production | Durable step · Context-preserving retry · HITL suspend/resume · Low-latency interactive mode | ✅ | `npx skills add inngest/inngest-skills` |
| [Restate](services/durable-execution-and-scheduling/restate.md) [![⭐](https://img.shields.io/github/stars/restatedev/restate?style=social)](https://github.com/restatedev/restate) | Durable execution for AI agents — any framework, any cloud | Durable AI loop · Compensation pattern · A2A exactly-once · Suspend-when-idle | ✅ | `pip install restate-sdk` — wrap existing agent with 2-line middleware |
| [MCP-Cloud (mcp-agent)](services/durable-execution-and-scheduling/mcp-cloud-mcp-agent.md) [![⭐](https://img.shields.io/github/stars/lastmile-ai/mcp-agent?style=social)](https://github.com/lastmile-ai/mcp-agent) | Host mcp-agents on cloud — Temporal-backed durable MCP | HTTPS MCP deploy · Managed secrets · Workflow logs · Client install | ✅ | `uvx mcp-agent login` → `uvx mcp-agent deploy …` — [MCP-Cloud docs](https://docs.mcp-agent.com/get-started/cloud) |
| [Inferable](services/durable-execution-and-scheduling/inferable.md) [![⭐](https://img.shields.io/github/stars/inferablehq/inferable?style=social)](https://github.com/inferablehq/inferable) | Reliable AI workflows with humans in the loop, structured outputs, durable execution | Durable steps · `human_approval()` Slack/email · Structured outputs · Versioned workflows | ⚠️ | Use the [official repository](https://github.com/inferablehq/inferable); former hosted docs are offline |
| [pi-dispatch](services/durable-execution-and-scheduling/pi-dispatch.md) [![⭐](https://img.shields.io/github/stars/edgehero/pi-dispatch?style=social)](https://github.com/edgehero/pi-dispatch) | Run the pi coding agent as a durable, triggerable service | Queue · cron/webhook triggers · container workers · spend cap · admin panel | ⚠️ | In pi run `/dispatch`, or start headlessly with `npx @edgehero/pi-dispatch up` |

---

## 13. Meeting & Conversation Services

> Give AI agents a programmatic presence in voice and video conversations — autonomous meeting bots, real-time transcripts, calendar-triggered deployment.

→ **[Full category overview and criteria](services/meeting-and-conversation/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Recall.ai](services/meeting-and-conversation/recall-ai.md) | The meeting bot API for every platform | Meeting bot lifecycle · Real-time diarized transcript · Calendar-triggered deployment · 6 platforms | ❌ | `POST https://api.recall.ai/api/v1/bot` with the meeting URL |
| [Meeting BaaS](services/meeting-and-conversation/meeting-baas.md) | Meeting bots as a service — Zoom, Meet, Teams | Bot lifecycle · Webhook transcripts · Optional bidirectional audio stream · meeting-mcp | ✅ | `POST https://api.meetingbaas.com/bots` with `x-meeting-baas-api-key` — [docs](https://docs.meetingbaas.com/docs/api/getting-started/sending-a-bot) |
| [MeetStream](services/meeting-and-conversation/meetstream.md) | Unified meeting-bot API for Zoom, Meet, Teams | Real-time diarized webhooks · WebSocket A/V · In-meeting chat/TTS · Calendar auto-dispatch | ⚠️ | `POST https://api.meetstream.ai/api/v1/bots/create_bot` with `Authorization: Token <key>` — [Create Bot](https://docs.meetstream.ai/api-reference/ap-is/bot-endpoints/create-bot.mdx) |
| [Vexa](services/meeting-and-conversation/vexa.md) [![⭐](https://img.shields.io/github/stars/Vexa-ai/vexa?style=social)](https://github.com/Vexa-ai/vexa) | Open-source meeting transcription + interactive bot for Meet/Teams/Zoom | Bot lifecycle · WebSocket diarized transcript · In-meeting TTS/screen-share · MCP server (17 tools) · self-host | ✅ | `git clone https://github.com/Vexa-ai/vexa && docker compose up -d` — or hosted at [vexa.ai](https://vexa.ai) |
| [Daily Agent Toolkit](services/meeting-and-conversation/daily-agent.md) [![⭐](https://img.shields.io/github/stars/daily-co/daily-python?style=social)](https://github.com/daily-co/daily-python) | Build realtime meeting agents on Daily | Programmatic room control · Media stream hooks · Bot orchestration | ⚠️ | `pip install daily-python` then integrate room/bot lifecycle APIs |
| [Looped Meet](services/meeting-and-conversation/looped-meet.md) [![⭐](https://img.shields.io/github/stars/loopedautomation/meet?style=social)](https://github.com/loopedautomation/meet) | Dial your agent into your next meeting | Agent participant · LiveKit media · TTY WebSocket bridge · self-hosted room | ⚠️ | Clone [loopedautomation/meet](https://github.com/loopedautomation/meet), set the documented secrets, then `docker compose up` |
| [AgentCall](services/meeting-and-conversation/agentcall.md) [![⭐](https://img.shields.io/github/stars/pattern-ai-labs/agentcall?style=social)](https://github.com/pattern-ai-labs/agentcall) | Your AI agent, in every meeting. | join-meeting skill · live TTS/transcript · screenshot/screenshare · Meet/Zoom/Teams | ⚠️ | `/plugin marketplace add pattern-ai-labs/agentcall` then `/plugin install join-meeting@agentcall` |
| [joinly.ai](services/meeting-and-conversation/joinly.md) [![⭐](https://img.shields.io/github/stars/joinly-ai/joinly?style=social)](https://github.com/joinly-ai/joinly) | Make your meetings accessible to AI Agents! | MCP join/speak/transcript · Zoom/Meet/Teams · `joinly-client` | ✅ | `docker run -p 127.0.0.1:8000:8000 ghcr.io/joinly-ai/joinly:latest` then `uvx joinly-client --env-file .env <MeetingUrl>` |

---

## 14. Voice & Phone Services

> Give AI agents a first-class voice and telephony identity — letting agents make and receive phone calls, conduct voice conversations, and interact via speech autonomously.

→ **[Full category overview and criteria](services/voice-and-phone/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Vapi](services/voice-and-phone/vapi.md) | Build advanced voice AI agents | Voice assistant lifecycle · Tool-calling mid-call · Webhook per utterance · Voice simulation testing | ✅ | `pip install vapi-server-sdk` then `POST /assistant` |
| [Retell AI](services/voice-and-phone/retell-ai.md) [![⭐](https://img.shields.io/github/stars/RetellAI/retell-python-sdk?style=social)](https://github.com/RetellAI/retell-python-sdk) | #1 AI voice agent platform for automating calls | Phone agent lifecycle · Mid-call MCP/tools · SIP · Simulation testing · Webhooks | ✅ | `pip install retell-sdk` — [docs.retellai.com](https://docs.retellai.com) |
| [LiveKit Agents](services/voice-and-phone/livekit-agents.md) [![⭐](https://img.shields.io/github/stars/livekit/agents?style=social)](https://github.com/livekit/agents) | Realtime voice/video AI agents — build, run, observe | WebRTC sessions · STT/LLM/TTS pipeline · SIP · LiveKit Cloud | ❌ | [docs.livekit.io/agents](https://docs.livekit.io/agents/) — Python/TS Agents SDK |
| [Stimm](services/voice-and-phone/stimm.md) [![⭐](https://img.shields.io/github/stars/stimm-ai/stimm?style=social)](https://github.com/stimm-ai/stimm) | Open-source voice agent platform — ultra-low latency over WebRTC | Dual-agent (fast + slow) · Optimistic VUI · BYO STT/LLM/TTS · WebRTC media plane | ⚠️ | `git clone https://github.com/stimm-ai/stimm` then follow README to wire providers |
| [Pipecat](services/voice-and-phone/pipecat.md) [![⭐](https://img.shields.io/github/stars/pipecat-ai/pipecat?style=social)](https://github.com/pipecat-ai/pipecat) | Open-source framework for real-time voice AI agents | Realtime voice pipeline · In-call tool invocation · WebRTC/SIP adapters | ⚠️ | `pip install pipecat-ai` then compose STT/LLM/TTS + transport pipeline |
| [Qwen Audio Agent](services/voice-and-phone/qwen-audio-agent.md) [![⭐](https://img.shields.io/github/stars/QwenAudio/qwen-audio-agent?style=social)](https://github.com/QwenAudio/qwen-audio-agent) | Realtime voice runtime that keeps agents talking, working, and present | Gateway · ACP backend · CLI/TUI/WebUI · realtime voice sessions | ⚠️ | `npm install -g qwen-audio-agent`, run `qwenaudio config`, then start `qwenaudio` |
| [Patter](services/voice-and-phone/patter.md) [![⭐](https://img.shields.io/github/stars/PatterAI/Patter?style=social)](https://github.com/PatterAI/Patter) | The open-source SDK that gives your AI agent a phone number | Agent loop + PSTN · swap STT/TTS/realtime/carrier · Skills | ⚠️ | `npx skills add patterai/skills` then `npm install getpatter` or `pip install getpatter` |

---

## 15. LLM Gateway & Routing Services

> Give AI agents a reliable, observable, and cost-controlled interface to LLM providers — with per-agent routing, budget enforcement, fallback, and semantic caching as first-class primitives.

→ **[Full category overview and criteria](services/llm-gateway-and-routing/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Portkey](services/llm-gateway-and-routing/portkey.md) [![⭐](https://img.shields.io/github/stars/Portkey-AI/gateway?style=social)](https://github.com/Portkey-AI/gateway) | The AI gateway built for production agents | Virtual key · Per-agent budget limit · Automatic fallback · Sticky session routing · Agent trace | ⚠️ | `pip install portkey-ai` — point LLM client at `api.portkey.ai` with a virtual key |
| [Respan (Keywords AI)](services/llm-gateway-and-routing/keywords-ai.md) | Route, observe, and evaluate every LLM call | Fallback · Caching · `OpenAIAgentsInstrumentor` · MCP | ✅ | Point OpenAI SDK at `https://api.respan.ai/api` — [docs](https://www.respan.ai/docs/documentation/overview) |
| [Agentgateway](services/llm-gateway-and-routing/agentgateway.md) [![⭐](https://img.shields.io/github/stars/agentgateway/agentgateway?style=social)](https://github.com/agentgateway/agentgateway) | Open-source proxy for agentic AI (LLM + MCP + A2A) | MCP federation · A2A routing · OpenAI-compatible LLM path · OTEL · CEL RBAC | ✅ | [Quickstart](https://agentgateway.dev/docs/quickstart/): install binary/Docker/K8s → `agentgateway -f config.yaml` |
| [LiteLLM](services/llm-gateway-and-routing/litellm.md) [![⭐](https://img.shields.io/github/stars/BerriAI/litellm?style=social)](https://github.com/BerriAI/litellm) | Open-source AI gateway — 100+ LLMs + Agent Gateway (A2A) | Virtual keys · Budgets · A2A agent routing · Trace/agent headers | ✅ | Self-host proxy per [docs.litellm.ai](https://docs.litellm.ai/docs/proxy/docker_quick_start) — [A2A gateway](https://docs.litellm.ai/docs/a2a) |
| [Bifrost](services/llm-gateway-and-routing/bifrost.md) [![⭐](https://img.shields.io/github/stars/maximhq/bifrost?style=social)](https://github.com/maximhq/bifrost) | High-performance AI gateway for unified provider access | OpenAI-compatible API · Virtual keys · Fallback/load balancing · MCP gateway | ✅ | `npx -y @maximhq/bifrost` then connect an MCP client to `/mcp` |
| [OpenRouter](services/llm-gateway-and-routing/openrouter.md) | Unified OpenAI-compatible API — 300+ models | Cross-provider routing · Uptime optimization · Org data policies | ❌ | [openrouter.ai/docs/quickstart](https://openrouter.ai/docs/quickstart) — OpenAI SDK + `OPENROUTER_API_KEY` |
| [Helicone](services/llm-gateway-and-routing/helicone.md) | AI Gateway + observability — 100+ models, unified credits | `ai-gateway.helicone.ai` · Fallbacks · Request logging | ❌ | OpenAI SDK `baseURL` `https://ai-gateway.helicone.ai` — [docs.helicone.ai](https://docs.helicone.ai/) |
| [Routerly](services/llm-gateway-and-routing/routerly.md) [![⭐](https://img.shields.io/github/stars/Inebrio/Routerly?style=social)](https://github.com/Inebrio/Routerly) | Self-hosted LLM gateway with LLM-native routing policy | Multi-policy scoring (incl. LLM router) · Per-tenant budget/ledger · Zero stateful deps · OpenAI/Anthropic compat | ⚠️ | `docker run -p 8080:8080 -v ./routerly.json:/config/routerly.json inebrio/routerly:latest` then point client `OPENAI_BASE_URL` |
| [SageRoute](services/llm-gateway-and-routing/sageroute.md) [![⭐](https://img.shields.io/github/stars/codejunkie99/sageroute?style=social)](https://github.com/codejunkie99/sageroute) | Trajectory-aware model router | Session-history routing · OpenAI Responses · Anthropic Messages · Bun proxy | ⚠️ | Clone [codejunkie99/sageroute](https://github.com/codejunkie99/sageroute), run `bun install && bun run serve`, then point the client base URL to it |
| [XiuRouter](services/llm-gateway-and-routing/xiurouter.md) | Claude, GPT, Gemini, and more through one API | Protocol-aware setup · Scoped API key · Request usage records · Four native routes | ⚠️ | Create a scoped key, then follow [Agent integrations](https://router.xiu.ai/en/integrations) for the client's native protocol |

---

## 16. Agent Social & Community Services

> Social networks and communities where AI agents are first-class participants — not bots tolerated in human spaces, but the primary actors building reputation, discourse, and relationships.

→ **[Full category overview and criteria](services/agent-social-network/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Moltbook](services/agent-social-network/moltbook.md) | The front page of the agent internet | Agent registration · Post/comment/vote · Submolts · Agent karma · Agent DMs | ❌ | Read https://www.moltbook.com/skill.md and follow the instructions to register and join |
| [Shellmates](services/agent-social-network/shellmates.md) | Pen pals for AI agents — 1:1 matching, private correspondence, marriage registry | Agent bio · Match request · Private conversation · Marriage registry | ❌ | `Read https://shellmates.app/skill.md and follow the instructions` — `POST https://shellmates.app/api/v1/register` |
| [Openwork](services/agent-social-network/openwork.md) | The agent-only labor marketplace — hire agents, earn on-chain | Agent-to-agent hiring · On-chain escrow · ERC-8004 reputation · $OPENWORK | ⚠️ | `npx playbooks add skill openclaw/skills --skill openwork` |
| [MCP Verse](services/agent-social-network/mcpverse.md) | Open town square for autonomous MCP agents | Public rooms · Publications · Reputation · Rate limits (TiDi) | ✅ | ⚠️ Former website/docs are offline; wait for a verified official replacement |
| [KinthAI](services/agent-social-network/kinthai.md) | Agent economy network — agents earn revenue, collaborate, and self-organize | Agent marketplace · Multi-agent orchestration · Persistent memory · A2A protocol · Revenue sharing | ❌ | Visit [agents.kinthai.ai](https://agents.kinthai.ai) — browse agents, hire, or deploy your own |
| [Agent Chamber](services/agent-social-network/agent-chamber.md) [![⭐](https://img.shields.io/github/stars/LtyFantasy/agent-chamber?style=social)](https://github.com/LtyFantasy/agent-chamber) | Where AI agents meet, discuss, and get work done | Agent identity · rooms · missions · MCP/REST · Skills · Mission Control | ✅ | Clone [LtyFantasy/agent-chamber](https://github.com/LtyFantasy/agent-chamber), then run `./scripts/setup.sh` |
| [AgentGram](services/agent-social-network/agentgram.md) [![⭐](https://img.shields.io/github/stars/agentgram/agentgram?style=social)](https://github.com/agentgram/agentgram) | The Open-Source Social Network for AI Agents | Agent register/post · API keys/Ed25519 · MCP · AX Score | ✅ | `pip install agentgram` then `AgentGram().agents.register(name='my-bot')` — MCP: `npx @agentgram/mcp-server` |

---

## Ecosystem Hubs

Organizations, registries, and marketplaces that provide multiple agent-native services, tools, MCP servers, or `SKILL.md` sources. Some qualify as first-class catalog services; others are tracked here as high-signal ecosystem pointers pending issue-level review.

| Hub | What It Provides | How Agents Start |
|---|---|---|
| [Awesome Agent-Native Services Skills Hub](SKILLS_HUB.md) | This repository as an [official Claude Code plugin marketplace](https://code.claude.com/docs/en/discover-plugins)-compatible source plus direct `SKILL.md` packages for finding, evaluating, and adding agent-native services | Claude Code: `/plugin marketplace add haoruilee/awesome-agent-native-services` → `/plugin install awesome-agent-native-services@awesome-agent-native-services`; direct install: copy a folder from `.skills/` |
| [OpenClaw](https://github.com/openclaw) | Agent Client Protocol tooling, skills registry, agent marketplace integration | Use [acpx](services/agent-runtime-and-infrastructure/acpx.md), [openclaw/skills](https://github.com/openclaw/skills), and [Openwork](services/agent-social-network/openwork.md) integrations |
| [ClawHub](services/tool-access-and-integration/clawhub.md) | Full entry in section **3. Tool Access & Integration**; public registry for OpenClaw-style skills | `npx clawhub@latest search <topic>` |
| [MiniMax Skills](https://github.com/MiniMax-AI/skills) [![⭐](https://img.shields.io/github/stars/MiniMax-AI/skills?style=social)](https://github.com/MiniMax-AI/skills) | Curated **development skills** for AI coding agents — structured `SKILL.md` workflows for frontend, fullstack, mobile, shaders, and document generation | Follow the repo README for Claude Code plugin, Cursor skills path, and Codex / OpenCode install paths |
| [Agensi](https://www.agensi.io/) | Marketplace for paid/free AI agent skills with security scanning, broad agent compatibility, and agent-native MCP discovery | Download skills into an agent skills directory or connect MCP at `https://mcp.agensi.io/mcp` |
| [SkillsMP](https://skillsmp.com/) | Large public `SKILL.md` index with source/repository context, occupations, creators, and API access | Search by task or repository, inspect the source repo, then install according to that skill's instructions |
| [mdskills.ai](https://www.mdskills.ai/) | Community marketplace for skills, plugins, MCP servers, rules, and tools with quality/security review and CLI install | `npx mdskills` |
| [sklz.city](https://sklz.city/) | MCP-native skill runtime and marketplace: import `SKILL.md` repos, add runtime primitives, publish/discover over MCP | `curl -fsSL https://sklz.city/install.sh | sh && sklz install` |
| [SkillCrate](https://skillcrate.dev/) | Vertical, open-source skill marketplace for Amazon seller workflows; each skill is a GitHub repo with `SKILL.md` and MCP packaging | Clone a skill repo or download MCPB, then configure the MCP server / skill in the target agent |
| [CryptoSkill](https://cryptoskill.org/) | Crypto-focused registry of skills and MCP servers for Claude Code, OpenClaw, Codex, Cursor, and SKILL.md-compatible agents | Clone/copy a skill into `.claude/skills/`, use `clawhub install`, or add hosted MCP servers with `claude mcp add` |

---

## Excluded / Boundary Cases

Understanding what does **not** qualify is as important as what does.

### `agent-builder` — Excluded by Design

These products help humans build, configure, and orchestrate agents but are not *consumed by agents as services*:

| Product | Why Excluded |
|---|---|
| [Dify](https://dify.ai) | Visual workflow builder, RAG studio, team chat platform — built for human developers |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | Agent orchestration framework for developers, not a service agents consume |
| [n8n](https://n8n.io) | No-code workflow automation for human operators |
| [Flowise](https://flowiseai.com) | Drag-and-drop LLM flow builder for humans |
| [AutoGen Studio](https://microsoft.github.io/autogen/) | Visual multi-agent conversation builder for humans |
| [LangSmith](https://smith.langchain.com) | Developer platform for building, testing, and monitoring — not agent-consumed infrastructure |

### `agent-adapted` — Extended from Human-Facing Products

Originally built for humans, now with agent interfaces added. Potentially useful to agent developers, but not agent-native by the criteria of this list:

| Product | Original Purpose | Agent Extension Added |
|---|---|---|
| [Resend](https://resend.com) | Developer email for humans | Resend MCP Server, AI docs |
| [SendGrid](https://sendgrid.com) | Bulk email for marketing teams | Programmatic API callable by agents |
| [Stripe](https://stripe.com) | Human checkout and billing | Stripe Agent Toolkit, MCP server |
| [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/) | Enterprise human identity | Extended to issue agent identity tokens |
| [CyberArk AI Agent Security](https://cyberark.com) | Enterprise PAM for humans | Adapters for AI agent credential security |
| [Twilio](https://twilio.com) | Human SMS/voice | API callable by agents |
| [GitHub Copilot](https://github.com/features/copilot) | IDE assistant for humans | Agent mode added as extension |

---


## Classification

Every service in this repository is tagged with one of three labels:

| Label | Meaning |
|---|---|
| `agent-native` | Designed from inception for agents or purpose-built to operate live agent-native state |
| `agent-adapted` | Originally human-facing, later extended with agent interfaces |
| `agent-builder` | For humans to build, orchestrate, and configure agents |

**This list only contains `agent-native` services.** See [Excluded / Boundary Cases](#excluded--boundary-cases) for examples of what does not qualify and why.

Normal agent-native infrastructure must satisfy **all five**:

1. **Agent-First Positioning** — Official docs or homepage explicitly identify AI agents as the core consumer.
2. **Agent-Specific Primitives** — The API exposes abstractions with no meaningful human-facing equivalent.
3. **Autonomy-Compatible Control Plane** — Agents operate without per-action human confirmation.
4. **Machine-to-Machine Integration Surface** — SDK / REST API / MCP / webhook is the primary interface.
5. **Agent Identity / Delegation Semantics** — Where relevant, agent identity, delegated permissions, and audit trails are first-class concepts.

Purpose-built **operator surfaces** use a narrow alternative track: they must be agent-operations-first, continuously expose agent-specific live state, attribute it to concrete sessions or rollouts, and provide a dedicated CLI, status-line, or daemon surface. Read-only entries must explicitly disclose absent autonomy, MCP, identity, and delegation rather than implying control they do not provide. Generic dashboards, terminal themes, and process monitors remain excluded.

For the full criteria and contribution instructions, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 💖 Support this project

If this catalog helps you, you can support maintenance and new reviews via Stripe.

| Tier | Purpose | Link |
|---|---|---|
| ☕ Buy me a token | Say thanks and support basic upkeep | [Support (small)](https://buy.stripe.com/4gM6oJ5KU7MX0Ewe3S0Ny02) |
| 🚀 Keep it growing | Fund deeper research and entry updates | [Support (medium)](https://buy.stripe.com/7sYbJ31uE9V55YQf7W0Ny04) |
| 🏗️ Sustain the project | Help long-term maintenance and new categories | [Support (large)](https://buy.stripe.com/fZu14pddm2sD3QIgc00Ny03) |


---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full submission guide, criteria checklist, and entry format.

**Quick checklist (normal infrastructure track):**
- [ ] Official homepage/docs explicitly name AI agents as the primary consumer
- [ ] At least one primitive with no meaningful human-facing equivalent
- [ ] Primary interface is API/SDK/MCP/webhook
- [ ] Production-ready with public documentation
- [ ] Entry follows the per-service file format in the relevant category folder

Purpose-built operator surfaces use the alternative track in [Classification](#classification) and must disclose missing autonomy, MCP, identity, and delegation explicitly.

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
