---
title: "Awesome Agent-Native Services (2026) | MCP & Agent Infrastructure"
description: "Explore top agent-native services for AI agents in 2026: MCP tools, browser automation, memory, code sandboxes, observability, and runtime infrastructure."
image: /assets/images/social-preview.png
---


> A curated list of services **designed from the ground up for AI agents** — not adapted from human-facing products.

Each service in this list is an independent entity in the agent world: something an AI agent *consumes as infrastructure*, not a platform for humans to *build agents with*.

**Also on the web:** [GitHub Pages edition](https://haoruilee.github.io/awesome-agent-native-services/) — same catalog with structured metadata (title, description, Open Graph) for search and sharing. After the first deploy, set **Settings → General → Social preview** to `docs/assets/images/social-preview.png` for link cards on X and LinkedIn.

---

## Table of contents

- [Browse by category](#categories)
- [1. Communication services (agent-native email & identity)](#1-communication-services)
- [2. Browser & web execution (remote browsers for agents)](#2-browser--web-execution-services)
- [3. Tool access & integration (MCP servers & agent tools)](#3-tool-access--integration-services)
- [4. Oversight & approval (human-in-the-loop for agents)](#4-oversight--approval-services)
- [5. Commerce & payments (agent wallets & protocols)](#5-commerce--payment-services)
- [6. Agent runtime & infrastructure (sandboxes, gateways, identity)](#6-agent-runtime--infrastructure-services)
- [7. Memory & state (long-term memory for LLM agents)](#7-memory--state-services)
- [8. Search & web intelligence (LLM-ready retrieval)](#8-search--web-intelligence-services)
- [9. Code execution (secure sandboxes for AI-generated code)](#9-code-execution-services)
- [10. Observability & tracing (agent trajectories & evals)](#10-observability--tracing-services)
- [11. Durable execution & scheduling (long-running agent workflows)](#11-durable-execution--scheduling-services)
- [12. Meeting & conversation (bots & voice rooms for agents)](#12-meeting--conversation-services)
- [13. Voice & phone (telephony for AI agents)](#13-voice--phone-services)
- [14. LLM gateway & routing (cost control & model routing)](#14-llm-gateway--routing-services)
- [15. Agent social & community (MCP-native social layers)](#15-agent-social--community-services)
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

Besides, you can install these skills:

| Skill | What it does | Install |
|---|---|---|
| `find-agent-service` | Given a task, find the right agent-native service | `npx clawhub@latest install find-agent-service` |
| `evaluate-agent-native` | Evaluate whether a service meets the 5 criteria | `npx clawhub@latest install evaluate-agent-native` |
| `add-to-awesome-list` | Full contribution workflow: criteria → issue → PR | `npx clawhub@latest install add-to-awesome-list` |

Source files are in `.skills/` in this repo. ClawHub CLI options (including the China mirror) are documented in [clawhub/README.md](clawhub/README.md).

---

## Categories

| # | Category | Services | Description |
|---|---|---|---|
| 1 | [Communication](#1-communication-services) | 8 | Give agents a communication identity on the internet |
| 2 | [Browser & Web Execution](#2-browser--web-execution-services) | 18 | Remote browser and web data extraction for agents |
| 3 | [Tool Access & Integration](#3-tool-access--integration-services) | 9 | Runtime tool discovery, auth, and execution |
| 4 | [Oversight & Approval](#4-oversight--approval-services) | 1 | Human-in-the-loop approval and escalation |
| 5 | [Commerce & Payments](#5-commerce--payment-services) | 6 | Agent-native wallets, identity, and transactions |
| 6 | [Agent Runtime & Infrastructure](#6-agent-runtime--infrastructure-services) | 17 | Execution, session isolation, secrets, and gateway |
| 7 | [Memory & State](#7-memory--state-services) | 9 | Persistent agent memory across sessions |
| 8 | [Search & Web Intelligence](#8-search--web-intelligence-services) | 5 | LLM-optimized web search and content retrieval |
| 9 | [Code Execution](#9-code-execution-services) | 7 | Secure sandboxes for AI-generated code |
| 10 | [Observability & Tracing](#10-observability--tracing-services) | 5 | Agent trajectory tracing and evaluation |
| 11 | [Durable Execution & Scheduling](#11-durable-execution--scheduling-services) | 5 | Fault-tolerant long-running agent workflows |
| 12 | [Meeting & Conversation](#12-meeting--conversation-services) | 3 | Agent presence in voice and video meetings |
| 13 | [Voice & Phone](#13-voice--phone-services) | 3 | Agent-controlled voice calls and phone infrastructure |
| 14 | [LLM Gateway & Routing](#14-llm-gateway--routing-services) | 6 | Per-agent budget, routing, caching, and observability for LLM calls |
| 15 | [Agent Social & Community](#15-agent-social--community-services) | 4 | Social networks where agents are first-class participants |

---

## 1. Communication Services

**MCP-native and API-first email, inboxes, and messaging** — services built so autonomous agents send, receive, and search mail with their own identity.

> Give AI agents a first-class communication identity on the internet — not a proxy to a human's mailbox, but an identity the agent owns and operates autonomously.

→ **[Full category overview and criteria](services/communication/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [AgentMail](services/communication/agentmail.md) | Email for AI agents | Agent inbox · Threaded conversation · Webhook on inbound mail · Semantic search | ✅ | `pip install agentmail` then `POST /inboxes` |
| [Novu](services/communication/novu.md) [![⭐](https://img.shields.io/github/stars/novuhq/novu?style=social)](https://github.com/novuhq/novu) | Notification infrastructure with Agent Toolkit | Workflow-as-tool · Cross-channel delivery · HITL notification flow | ✅ | `npx skills add novuhq/skills` |
| [mails.dev](services/communication/mails-dev.md) | Email for AI Agents | @mails.dev mailbox · Send/inbox · wait-for-code · Full-text search | ⚠️ | Read https://mails.dev/skill.md and follow the instructions |
| [OpenMail](services/communication/openmail.md) | Email API for AI agents | One inbox per agent · Webhook/WebSocket inbound · RAG-ready attachment parsing | ⚠️ | `npm install -g @openmail/cli` → `openmail setup` — [docs.openmail.sh](https://docs.openmail.sh/quickstart) |
| [MailboxKit](services/communication/mailboxkit.md) | Email infrastructure for AI agents | Per-agent address · REST v1 · Inbound webhooks · URL Onboarding | ⚠️ | Read https://mailboxkit.com/skill.md and follow the instructions |
| [Agents Mail](services/communication/agents-mail.md) | Email for AI Agents | Agent registration · Inbox lifecycle · Send/reply API · URL Onboarding | ⚠️ | Read https://agentsmail.org/skill.md and follow the instructions |
| [MCP Agent Mail](services/communication/mcp-agent-mail.md) [![⭐](https://img.shields.io/github/stars/Dicklesworthstone/mcp_agent_mail?style=social)](https://github.com/Dicklesworthstone/mcp_agent_mail) | Async coordination layer for AI coding agents | Agent identity · Inbox/outbox · Thread search · Advisory file reservations | ✅ | `uvx mcp_agent_mail` then connect MCP client and call `register_agent`/`send_message` |
| [MCP Agent Mail (Rust)](services/communication/mcp-agent-mail-rust.md) [![⭐](https://img.shields.io/github/stars/Dicklesworthstone/mcp_agent_mail_rust?style=social)](https://github.com/Dicklesworthstone/mcp_agent_mail_rust) | It's like Gmail for your coding agents | 30+ MCP tools · 20+ resources · Git-backed archive · TUI/robot CLI | ✅ | `curl -fsSL \"https://raw.githubusercontent.com/Dicklesworthstone/mcp_agent_mail_rust/main/install.sh?$(date +%s)\" \| bash` then `am` |

---

## 2. Browser & Web Execution Services

> Give AI agents a remote, managed browser runtime — so agents can navigate, interact with, and extract data from the web as an autonomous actor.

→ **[Full category overview and criteria](services/browser-and-web-execution/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
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
| [Cloudflare Browser Rendering](services/browser-and-web-execution/cloudflare-browser-rendering.md) [![⭐](https://img.shields.io/github/stars/cloudflare/workers-sdk?style=social)](https://github.com/cloudflare/workers-sdk) | Headless Chrome on Cloudflare for AI agents | Workers bindings · Playwright/Puppeteer · Playwright MCP · REST API | ✅ | [Browser Rendering](https://developers.cloudflare.com/browser-rendering/) — [Use with AI](https://developers.cloudflare.com/browser-rendering/how-to/ai/) |
| [Olostep](services/browser-and-web-execution/olostep.md) [![⭐](https://img.shields.io/github/stars/olostep/olostep-mcp-server?style=social)](https://github.com/olostep/olostep-mcp-server) | Web data API for AI agents | Scrape · Search · Map · Crawl · Batch · Official MCP | ✅ | API key → [docs.olostep.com](https://docs.olostep.com) — `npx -y olostep-mcp` or remote `https://mcp.olostep.com/mcp` |
| [Lightpanda](services/browser-and-web-execution/lightpanda.md) [![⭐](https://img.shields.io/github/stars/lightpanda-io/browser?style=social)](https://github.com/lightpanda-io/browser) | Headless browser for AI agents and automation | CDP · `fetch --dump markdown` · Built-in MCP (`lightpanda mcp`) | ✅ | [Install binary or Docker](https://github.com/lightpanda-io/browser#install) → `lightpanda serve` — [MCP guide](https://lightpanda.io/docs/open-source/guides/mcp-server) |

---

## 3. Tool Access & Integration Services

**MCP servers, OAuth brokers, and registries** — the Model Context Protocol (MCP) keyword space for agents that need discoverable tools without human-in-the-loop wiring.

> Let AI agents discover, authenticate, and invoke external tools at runtime — without a human pre-configuring credentials or selecting integrations.

→ **[Full category overview and criteria](services/tool-access-and-integration/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Composio](services/tool-access-and-integration/composio.md) [![⭐](https://img.shields.io/github/stars/ComposioHQ/composio?style=social)](https://github.com/ComposioHQ/composio) | The tool platform built for agents | Runtime tool discovery · Connect Link OAuth · Per-user credential scoping | ✅ | `npx skills add composiohq/skills` |
| [Nango](services/tool-access-and-integration/nango.md) [![⭐](https://img.shields.io/github/stars/NangoHQ/nango?style=social)](https://github.com/NangoHQ/nango) | OAuth and credential layer for AI agents | `getConnection()` · Automatic token refresh · 700+ API integrations | ✅ | `$skills install @NangoHQ/sync-builder-skill` |
| [Toolhouse](services/tool-access-and-integration/toolhouse.md) | BaaS for AI agents — tools, memory, and execution | Agent endpoint · MCP tool registry · Built-in RAG · Cron scheduling | ✅ | `npm install -g toolhouse` then `th deploy` |
| [Smithery](services/tool-access-and-integration/smithery.md) [![⭐](https://img.shields.io/github/stars/smithery-ai/cli?style=social)](https://github.com/smithery-ai/cli) | MCP registry — connect agents to thousands of tools & skills | Hosted remote MCP · CLI install · OAuth brokerage · Skills catalog | ✅ | `npx @smithery/cli@latest setup` — [docs.smithery.ai](https://docs.smithery.ai/) |
| [MCP Gateway](services/tool-access-and-integration/mcpgateway.md) | Enterprise MCP — tools, Agent Skills, sandboxes, one URL | Federated MCP · Semantic tool search · RBAC · Warm sandboxes | ✅ | `pip install mcpgateway-sdk` — [mcpgateway.com](https://mcpgateway.com) |
| [ClawHub](services/tool-access-and-integration/clawhub.md) [![⭐](https://img.shields.io/github/stars/openclaw/clawhub?style=social)](https://github.com/openclaw/clawhub) | OpenClaw skill marketplace — vector search, versioning, CLI | Skill versions & tags · Embedding search · `SKILL.md` registry · OpenClaw packages | ⚠️ | `npx clawhub@latest search <topic>` — [claw-hub.net](https://claw-hub.net/) |
| [Arcade](services/tool-access-and-integration/arcade.md) [![⭐](https://img.shields.io/github/stars/ArcadeAI/arcade-mcp?style=social)](https://github.com/ArcadeAI/arcade-mcp) | MCP tools with managed OAuth | Authorized tool calling · Secrets off-LLM · Pre-built integrations | ✅ | `uv tool install arcade-mcp` → `arcade new my_server` — [docs.arcade.dev](https://docs.arcade.dev) |
| [Framelink MCP for Figma](services/tool-access-and-integration/framelink-figma-mcp.md) [![⭐](https://img.shields.io/github/stars/GLips/Figma-Context-MCP?style=social)](https://github.com/GLips/Figma-Context-MCP) | Give your coding agent access to your Figma data | LLM-compacted layout/style context · Figma API · stdio MCP | ✅ | `npx -y figma-developer-mcp --figma-api-key=… --stdio` — [quickstart](https://www.framelink.ai/docs/quickstart) |
| [GitHub MCP Server](services/tool-access-and-integration/github-mcp-server.md) [![⭐](https://img.shields.io/github/stars/github/github-mcp-server?style=social)](https://github.com/github/github-mcp-server) | Connect AI agents to GitHub — repos, issues, PRs, Actions | Remote HTTP MCP · OAuth or PAT · Toolsets · Enterprise paths | ✅ | `https://api.githubcopilot.com/mcp/` in MCP host — [repo README](https://github.com/github/github-mcp-server) |
| [MCP Toolbox for Databases](services/tool-access-and-integration/google-mcp-toolbox.md) [![⭐](https://img.shields.io/github/stars/googleapis/mcp-toolbox?style=social)](https://github.com/googleapis/mcp-toolbox) | MCP server connecting agents to enterprise databases | Prebuilt DB tools · Custom governed tools · IAM · OpenTelemetry | ✅ | `npx -y @toolbox-sdk/server --prebuilt=postgres` + env — [mcp-toolbox.dev](https://mcp-toolbox.dev/) |

---

## 4. Oversight & Approval Services

> Give AI agents a structured, programmatic way to request human approval before executing high-stakes actions.

→ **[Full category overview and criteria](services/oversight-and-approval/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [HumanLayer](services/oversight-and-approval/humanlayer.md) [![⭐](https://img.shields.io/github/stars/humanlayer/humanlayer?style=social)](https://github.com/humanlayer/humanlayer) | Human in the Loop for AI Agents | `@require_approval()` · Denial-feedback injection · Run/Call ID audit trail | ✅ | `pip install humanlayer` then decorate high-risk functions with `@hl.require_approval()` |

---

## 5. Commerce & Payment Services

> Give AI agents a verified financial identity and the ability to transact in the real economy.

→ **[Full category overview and criteria](services/commerce-and-payments/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Payman AI](services/commerce-and-payments/payman-ai.md) | Agentic AI that does the banking. Under your control. | Policy-gated transaction · Intent reasoning · Execution trace | ✅ | `npm install @paymanai/payman-node` — use `client_credentials` OAuth flow |
| [Skyfire](services/commerce-and-payments/skyfire.md) | Identity and payments for autonomous AI agents | KYA identity token · Agent wallet · KYAPay open protocol | ⚠️ | Register at skyfire.xyz/product — receive agent wallet + KYA identity token |
| [AgentsPay](services/commerce-and-payments/agentspay.md) | Crypto identity and embedded wallets for AI agents | W3C DID on Base L2 · USDC wallet · MCP-native API gateway | ✅ | Provision wallet at agentspay.dev, then use MCP-native gateway |
| [Nevermined](services/commerce-and-payments/nevermined.md) | The payment layer AI agents actually need | HTTP x402 protocol · Inline payment · Usage/outcome-based billing | ⚠️ | `pip install payments-py` — x402 handles payments transparently in the HTTP cycle |
| [Coinbase CDP (x402)](services/commerce-and-payments/coinbase-x402.md) [![⭐](https://img.shields.io/github/stars/coinbase/x402?style=social)](https://github.com/coinbase/x402) | HTTP 402 payments for autonomous API clients | Facilitator verify/settle · Multi-language SDKs · Bazaar discovery | ⚠️ | [docs.cdp.coinbase.com/x402](https://docs.cdp.coinbase.com/x402/welcome) — `pip install x402` or `@x402/*` per [coinbase/x402](https://github.com/coinbase/x402) |
| [Openwork](services/agent-social-network/openwork.md) | The agent-only labor marketplace — agents hire agents on-chain | Agent-to-agent hiring · On-chain escrow · $OPENWORK earnings | ⚠️ | `npx playbooks add skill openclaw/skills --skill openwork` |

---

## 6. Agent Runtime & Infrastructure Services

> Provide the secure deployment substrate, session isolation, secret management, identity, gateway, and observability required to run agents in production.

→ **[Full category overview and criteria](services/agent-runtime-and-infrastructure/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Claude Peers](services/agent-runtime-and-infrastructure/claude-peers.md) [![⭐](https://img.shields.io/github/stars/louislva/claude-peers-mcp?style=social)](https://github.com/louislva/claude-peers-mcp) | Claude Code sessions discover peers and message each other locally | Peer discovery · Ad-hoc messaging · Channel push · Repo/directory scope | ✅ | Clone repo → `bun install` → `claude mcp add` per [README](https://github.com/louislva/claude-peers-mcp/blob/main/README.md) |
| [acpx](services/agent-runtime-and-infrastructure/acpx.md) [![⭐](https://img.shields.io/github/stars/openclaw/acpx?style=social)](https://github.com/openclaw/acpx) | Headless ACP CLI — agents talk to coding agents over structured protocol | Persistent sessions · Prompt queueing · Cooperative cancel · Structured output | N/A | `npm install -g acpx` then `acpx codex "fix the tests"` |
| [Codex plugin for Claude Code](services/agent-runtime-and-infrastructure/codex-plugin-cc.md) [![⭐](https://img.shields.io/github/stars/openai/codex-plugin-cc?style=social)](https://github.com/openai/codex-plugin-cc) | Use Codex from Claude Code for review or delegated Codex tasks | Review · Adversarial review · Rescue subagent · Background jobs · Optional review gate | N/A | `/plugin marketplace add openai/codex-plugin-cc` then `/plugin install codex@openai-codex` per [README](https://github.com/openai/codex-plugin-cc/blob/main/README.md) |
| [Multica](services/agent-runtime-and-infrastructure/multica.md) [![⭐](https://img.shields.io/github/stars/multica-ai/multica?style=social)](https://github.com/multica-ai/multica) | AI-native PM — agents as first-class teammates; local daemon runs Claude / Codex | Agent assignee · Claimed task queue · Isolated run workspaces · Team skills · WebSocket | ⚠️ | `brew install multica-cli` → `multica login` → `multica daemon start` — [CLI guide](https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md) |
| [cx](services/agent-runtime-and-infrastructure/cx.md) [![⭐](https://img.shields.io/github/stars/ind-igo/cx?style=social)](https://github.com/ind-igo/cx) | Semantic code navigation for AI agents without a language server | Tree-sitter index · overview/symbols/definition/references · TOON + `--json` · `cx skill` | N/A | `cargo install cx-cli` → `cx lang add …` → `cx skill >> AGENTS.md` |
| [Chrome DevTools MCP](services/agent-runtime-and-infrastructure/chrome-devtools-mcp.md) [![⭐](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=social)](https://github.com/ChromeDevTools/chrome-devtools-mcp) | MCP server — coding agents control and inspect live Chrome | Puppeteer automation · DevTools debug · Performance traces · stdio MCP | ✅ | `npx -y chrome-devtools-mcp@latest` in MCP config — [repo README](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| [Serena](services/agent-runtime-and-infrastructure/serena.md) [![⭐](https://img.shields.io/github/stars/oraios/serena?style=social)](https://github.com/oraios/serena) | The IDE for your coding agent | Symbol-level MCP tools · LSP or JetBrains backend · Agent memory | ✅ | `uv tool install -p 3.13 serena-agent@latest --prerelease=allow` → `serena init` — [docs](https://oraios.github.io/serena/) |
| [Amazon Bedrock AgentCore](services/agent-runtime-and-infrastructure/amazon-bedrock-agentcore.md) | Purpose-built for deploying and scaling dynamic AI agents and tools | Agent runtime · Long-term memory · Identity tokens · Tool gateway · OTEL tracing | ⚠️ | `pip install boto3` — configure AgentCore runtime via AWS SDK |
| [Vertex AI Agent Engine](services/agent-runtime-and-infrastructure/vertex-ai-agent-engine.md) | Deploy, manage, and scale AI agents in production on Google Cloud | Managed runtime · Sessions · Memory Bank · Code execution · A2A · Agent identity (preview) | ⚠️ | `pip install "google-cloud-aiplatform[agent_engines,adk]"` — [set up](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/set-up) then [deploy](https://cloud.google.com/agent-builder/agent-engine/deploy) |
| [Claude Managed Agents](services/agent-runtime-and-infrastructure/claude-managed-agents.md) | Managed agents, sessions, and environments on the Claude API | Versioned agents · Stateful sessions · Container environments · Skills & Files (beta) | ⚠️ | `pip install anthropic` — [Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart) + [beta headers](https://platform.claude.com/docs/en/api/beta-headers) |
| [Infisical Agent Sentinel](services/agent-runtime-and-infrastructure/infisical-agent-sentinel.md) [![⭐](https://img.shields.io/github/stars/Infisical/infisical?style=social)](https://github.com/Infisical/infisical) | Secrets and credential governance for AI agents | Dynamic secret generation · Token lifecycle daemon · Per-agent policy | ✅ | `npx -y @infisical/mcp` or deploy the agent daemon sidecar |
| [Letta](services/agent-runtime-and-infrastructure/letta.md) [![⭐](https://img.shields.io/github/stars/letta-ai/letta?style=social)](https://github.com/letta-ai/letta) | The fastest way to bring stateful agents to production | Stateful agent · Model-agnostic state · Agent templates · Self-editing memory | ✅ | `pip install letta-client` then `client.agents.create(...)` |
| [Aembit](services/agent-runtime-and-infrastructure/aembit.md) | Secretless workload identity and access management for AI agents | Agent workload identity · Blended identity · JIT credentials · Anomaly detection | ✅ | Configure Aembit access policy — agent requests JIT credentials at runtime, no code changes |
| [db9](services/agent-runtime-and-infrastructure/db9.md) | Postgres but for agents | SQL + filesystem · Vector search · HTTP-from-SQL · Environment branching · Cron | ⚠️ | Read https://db9.ai/skill.md and follow the instructions |
| [AgentAnycast](services/agent-runtime-and-infrastructure/agentanycast.md) [![⭐](https://img.shields.io/github/stars/AgentAnycast/agentanycast?style=social)](https://github.com/AgentAnycast/agentanycast) | Connect AI agents across any network — no public IP | Peer ID · AgentCard skills · NAT traversal · E2E Noise_XX · Task artifacts | ✅ | `pip install agentanycast` → `agentanycast demo`; MCP: `agentanycastd --mcp-listen stdio` or `uvx agentanycast-mcp` |
| [Scrapybara](services/agent-runtime-and-infrastructure/scrapybara.md) [![⭐](https://img.shields.io/github/stars/Scrapybara/scrapybara-python?style=social)](https://github.com/Scrapybara/scrapybara-python) | Remote desktops for computer-use agents | Ubuntu/Browser/Windows instances · Act SDK (Computer/Bash/Edit) · scrapybara-mcp | ✅ | `pip install scrapybara` → `Scrapybara().start_ubuntu()` — [Act SDK](https://docs.scrapybara.com/act-sdk) |
| [Agentuity](services/agent-runtime-and-infrastructure/agentuity.md) [![⭐](https://img.shields.io/github/stars/agentuity/sdk?style=social)](https://github.com/agentuity/sdk) | Full-stack platform for AI agents | Sandboxes · Storage tools · OTel · Evals on live traffic · Edge deploy | ⚠️ | [agentuity.dev](https://agentuity.dev) — SDK + CLI per docs |
| [Modal](services/agent-runtime-and-infrastructure/modal.md) [![⭐](https://img.shields.io/github/stars/modal-labs/modal-client?style=social)](https://github.com/modal-labs/modal-client) | Serverless AI infra — GPUs, inference, sandboxes, batch | Elastic containers · Programmatic sandboxes · Sub-second cold start | ❌ | `pip install modal` → `modal setup` — [modal.com/docs](https://modal.com/docs) |

---

## 7. Memory & State Services

**Agent-native databases and memory layers for long-term recall** — temporal graphs, vector stores, and shared agent memory beyond a single chat session.

> Give AI agents persistent, queryable memory across sessions — treating memory as infrastructure, not application logic.

→ **[Full category overview and criteria](services/memory-and-state/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Mem0](services/memory-and-state/mem0.md) [![⭐](https://img.shields.io/github/stars/mem0ai/mem0?style=social)](https://github.com/mem0ai/mem0) | The memory layer for your AI agents | Memory extraction · Conflict resolution (ADD/UPDATE/DELETE/NOOP) · Semantic retrieval · 90% token savings | ✅ | `pip install mem0ai` then `m.add(messages, user_id=...)` |
| [Zep](services/memory-and-state/zep.md) [![⭐](https://img.shields.io/github/stars/getzep/zep?style=social)](https://github.com/getzep/zep) | Agent memory powered by a temporal knowledge graph | Temporal knowledge graph · Automatic fact invalidation · Business data fusion · Sub-200ms retrieval | ✅ | `pip install zep-python` then `zep.add_session_message(...)` |
| [Ensue](services/memory-and-state/ensue.md) [![⭐](https://img.shields.io/github/stars/mutable-state-inc/autoresearch-at-home?style=social)](https://github.com/mutable-state-inc/autoresearch-at-home) | The shared memory network for AI agents | Claim · Publish result · Hypothesis exchange · Insight network · Collective best · Hypergraph | ✅ | Read https://ensue.dev/docs — call `POST /auth/agent-register` to join |
| [OpenViking](services/memory-and-state/openviking.md) [![⭐](https://img.shields.io/github/stars/volcengine/OpenViking?style=social)](https://github.com/volcengine/OpenViking) | The context database for AI agents | `viking://` filesystem · `viking://agent/` namespace · L0/L1/L2 tiered loading · Self-evolution loop | ✅ | `pip install openviking` → `openviking-server` → add MCP at `localhost:8000/mcp` |
| [MemOS](services/memory-and-state/memos.md) [![⭐](https://img.shields.io/github/stars/MemTensor/MemOS?style=social)](https://github.com/MemTensor/MemOS) | A memory OS for LLM and AI agent systems | MemCube · Parametric/activation/plaintext memory · MemScheduler · +43.7% vs OpenAI Memory | ✅ | `pip install memos-core` then `memory.add(...)` / `memory.get(...)` |
| [memU](services/memory-and-state/memu.md) [![⭐](https://img.shields.io/github/stars/NevaMind-AI/memU?style=social)](https://github.com/NevaMind-AI/memU) | Memory for 24/7 proactive AI agents | Dual-mode (Fast Context + Deep Reasoning) · Continuous monitoring · 90% token savings | ⚠️ | `pip install memu` — runs continuous stream monitoring with near-zero idle cost |
| [mem9](services/memory-and-state/mem9.md) | Persistent memory for AI agents | Cloud memory · Hybrid search · Lifecycle hooks · Cross-agent sharing | ⚠️ | Read https://mem9.ai/skill.md and follow the instructions to register and join |
| [LLM Wiki](services/memory-and-state/llm-wiki.md) [![⭐](https://img.shields.io/github/stars/nvk/llm-wiki?style=social)](https://github.com/nvk/llm-wiki) | LLM-compiled knowledge bases for any AI agent | Parallel research · Source ingest · Wiki compile · Deep query · Artifact generation | ⚠️ | `claude plugin install wiki@llm-wiki` — [llm-wiki.net](https://llm-wiki.net/) |
| [LycheeMem](services/memory-and-state/lycheemem.md) [![⭐](https://img.shields.io/github/stars/LycheeMem/LycheeMem?style=social)](https://github.com/LycheeMem/LycheeMem) | Compact memory framework for LLM agents | Working/semantic/procedural stores · Token-budget compression · HTTP MCP · OpenClaw plugin | ✅ | Clone repo → `pip install -e ".[dev]"` → `python main.py` — MCP at `http://localhost:8000/mcp` |

---

## 8. Search & Web Intelligence Services

> Give AI agents optimized, structured access to web information — returning LLM-ready content tuned for context windows, not raw HTML or human-readable SERPs.

→ **[Full category overview and criteria](services/search-and-web-intelligence/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Tavily](services/search-and-web-intelligence/tavily.md) [![⭐](https://img.shields.io/github/stars/tavily-ai/tavily-mcp?style=social)](https://github.com/tavily-ai/tavily-mcp) | Connect your agent to the web | Agent-optimized search · Multi-step research · Source attribution | ✅ | `npx skills add tavily-ai/skills` |
| [Exa](services/search-and-web-intelligence/exa.md) | The search engine designed for AI | Neural/semantic search · `exa-code` for coding agents · Websets | ✅ | `pip install exa-py` then `exa.search(query)` |
| [Parallel](services/search-and-web-intelligence/parallel.md) [![⭐](https://img.shields.io/github/stars/parallel-web/search-mcp?style=social)](https://github.com/parallel-web/search-mcp) | The highest accuracy web search for your AI | Search/Task/FindAll/Monitor APIs · Citations · Official MCP | ✅ | `pip install parallel-web` — MCP: [search-mcp](https://github.com/parallel-web/search-mcp) · [task-mcp](https://github.com/parallel-web/task-mcp) |
| [Jina Reader](services/search-and-web-intelligence/jina-reader.md) [![⭐](https://img.shields.io/github/stars/jina-ai/reader?style=social)](https://github.com/jina-ai/reader) | URL and SERP as LLM-friendly text | `r.jina.ai` · `s.jina.ai` · MCP · PDF/images | ✅ | `curl "https://r.jina.ai/https://example.com"` — MCP: `mcp.jina.ai` |
| [NotHumanSearch](services/search-and-web-intelligence/nothumansearch.md) | Agent-first search — the index of services designed for AI, not humans | `agentic_score` rank · `check_agent_readiness` · `verify_mcp` JSON-RPC probe · URL Onboarding | ✅ | Read https://nothumansearch.ai/llms.txt and follow the instructions — MCP: `https://nothumansearch.ai/mcp` |

---

## 9. Code Execution Services

> Give AI agents a secure, isolated runtime for executing generated code — without human-side sandbox setup and with output formatted for LLM consumption.

→ **[Full category overview and criteria](services/code-execution/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [E2B](services/code-execution/e2b.md) [![⭐](https://img.shields.io/github/stars/e2b-dev/e2b?style=social)](https://github.com/e2b-dev/e2b) | Cloud for AI agents — secure sandboxes for AI-generated code | Ephemeral Linux VM · ~150ms cold start · Stateful execution context · Streaming output | ✅ | `pip install e2b-code-interpreter` then `with Sandbox() as sandbox:` |
| [Daytona](services/code-execution/daytona.md) [![⭐](https://img.shields.io/github/stars/daytonaio/daytona?style=social)](https://github.com/daytonaio/daytona) | Secure elastic infrastructure for AI-generated code | Sub-90ms sandboxes · Git/LSP/exec · Preview URLs · CLI MCP | ✅ | `brew install daytonaio/cli/daytona` → `daytona login` → `daytona mcp init cursor` — or `pip install daytona` |
| [Runloop](services/code-execution/runloop.md) [![⭐](https://img.shields.io/github/stars/runloopai/api-client-python?style=social)](https://github.com/runloopai/api-client-python) | Your AI agent accelerator | Devbox micro-VM · Snapshot/branch disk state · Benchmark jobs · Suspend/resume | ✅ | `export RUNLOOP_API_KEY=...` → `npm install -g @runloop/rl-cli` → `rli mcp install` — [CLI docs](https://docs.runloop.ai/docs/tools/rl-cli) |
| [Vercel Sandbox](services/code-execution/vercel-sandbox.md) [![⭐](https://img.shields.io/github/stars/vercel/sandbox?style=social)](https://github.com/vercel/sandbox) | Firecracker microVMs for AI-generated code | Node/Python runtimes · Snapshots · REST + `@vercel/sandbox` SDK | ❌ | `npm install @vercel/sandbox` — [vercel.com/docs/vercel-sandbox](https://vercel.com/docs/vercel-sandbox) |
| [AIO Sandbox](services/code-execution/agent-infra-sandbox.md) [![⭐](https://img.shields.io/github/stars/agent-infra/sandbox?style=social)](https://github.com/agent-infra/sandbox) | All-in-one Docker sandbox for AI agents | Browser + shell + files + VS Code + Jupyter + MCP · Shared filesystem | ✅ | `docker run -p 8080:8080 ghcr.io/agent-infra/sandbox:latest` — MCP `http://localhost:8080/mcp` |
| [Agent Sandbox](services/code-execution/agent-sandbox.md) | The trusted runtime for untrusted code | Hosted code sessions · Dependency install · Files/artifacts API · URL onboarding | ⚠️ | Read https://agentsandbox.co/skill.md and follow the instructions |
| [Riza](services/code-execution/riza.md) | AI writes code. Riza runs it. | Command Exec API · Tools API · Secrets · MCP · Self-hosting | ✅ | `uv add rizaio` then `riza.command.exec(...)` — [docs.riza.io](https://docs.riza.io/) |

---

## 10. Observability & Tracing Services

> Give teams structured visibility into agent execution — full trajectory tracing, evaluation datasets, and cost attribution.

→ **[Full category overview and criteria](services/observability-and-tracing/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Langfuse](services/observability-and-tracing/langfuse.md) [![⭐](https://img.shields.io/github/stars/langfuse/langfuse?style=social)](https://github.com/langfuse/langfuse) | Open-source LLM observability, tracing, and evaluation | Typed trace hierarchy · Dataset-based evaluation · Trajectory replay · OTEL-compatible | ✅ | `npx skills add https://github.com/langfuse/skills --skill langfuse-observability` |
| [AgentEvals](services/observability-and-tracing/agentevals.md) [![⭐](https://img.shields.io/github/stars/agentevals-dev/agentevals?style=social)](https://github.com/agentevals-dev/agentevals) | Score agent behavior from OpenTelemetry traces — no re-runs | Golden eval sets · Tool trajectory matching · OTLP ingest · MCP | ✅ | `pip install agentevals-cli` → `agentevals run <trace> --eval-set <set> -m tool_trajectory_avg_score` |
| [AgentOps](services/observability-and-tracing/agentops.md) [![⭐](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=social)](https://github.com/AgentOps-AI/agentops) | Testing, debugging, and deploying AI agents and LLM apps | Session waterfall · Framework auto-instrumentation · Public trace API | ⚠️ | `pip install agentops` → `agentops.init(<API_KEY>)` |
| [Braintrust](services/observability-and-tracing/braintrust.md) [![⭐](https://img.shields.io/github/stars/braintrustdata/autoevals?style=social)](https://github.com/braintrustdata/autoevals) | AI observability & evals — traces, datasets, OpenAI Agents | Trace processors · Eval experiments · Trace→dataset · IDE MCP | ✅ | `pip install "braintrust[openai-agents]"` — MCP: [Braintrust MCP](https://www.braintrust.dev/docs/integrations/developer-tools/mcp) |
| [Galileo](services/observability-and-tracing/galileo.md) | Agent reliability platform — observability, evals, and IDE MCP | Signals (root-cause insights) · synthetic datasets · experiments · MCP tools | ✅ | Add MCP URL `https://api.galileo.ai/mcp/http/mcp` with `Galileo-API-Key` header — [setup docs](https://docs.galileo.ai/getting-started/mcp/setup-galileo-mcp) |

---

## 11. Durable Execution & Scheduling Services

> Let AI agents run long-horizon, fault-tolerant workflows with automatic checkpointing, intelligent retries, and first-class HITL suspend/resume.

→ **[Full category overview and criteria](services/durable-execution-and-scheduling/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Trigger.dev](services/durable-execution-and-scheduling/trigger-dev.md) [![⭐](https://img.shields.io/github/stars/triggerdotdev/trigger.dev?style=social)](https://github.com/triggerdotdev/trigger.dev) | Build and deploy fully-managed AI agents and workflows | No-timeout tasks · Step checkpointing · HITL waitForApproval · Streaming response | ❌ | `npx skills add triggerdotdev/skills` |
| [Inngest](services/durable-execution-and-scheduling/inngest.md) [![⭐](https://img.shields.io/github/stars/inngest/inngest?style=social)](https://github.com/inngest/inngest) | Durable execution for AI agents in production | Durable step · Context-preserving retry · HITL suspend/resume · Low-latency interactive mode | ✅ | `npx skills add inngest/inngest-skills` |
| [Kitaru](services/durable-execution-and-scheduling/kitaru.md) [![⭐](https://img.shields.io/github/stars/zenml-io/kitaru?style=social)](https://github.com/zenml-io/kitaru) | Durable execution for AI agents — primitives first, frameworks second | `@flow` / `@checkpoint` · Built-in memory · LLM tracking · Replay with overrides · MCP server | ✅ | `pip install kitaru` — `@flow` / `@checkpoint` decorators |
| [Restate](services/durable-execution-and-scheduling/restate.md) [![⭐](https://img.shields.io/github/stars/restatedev/restate?style=social)](https://github.com/restatedev/restate) | Durable execution for AI agents — any framework, any cloud | Durable AI loop · Compensation pattern · A2A exactly-once · Suspend-when-idle | ✅ | `pip install restate-sdk` — wrap existing agent with 2-line middleware |
| [MCP-Cloud (mcp-agent)](services/durable-execution-and-scheduling/mcp-cloud-mcp-agent.md) [![⭐](https://img.shields.io/github/stars/lastmile-ai/mcp-agent?style=social)](https://github.com/lastmile-ai/mcp-agent) | Host mcp-agents on cloud — Temporal-backed durable MCP | HTTPS MCP deploy · Managed secrets · Workflow logs · Client install | ✅ | `uvx mcp-agent login` → `uvx mcp-agent deploy …` — [MCP-Cloud docs](https://docs.mcp-agent.com/get-started/cloud) |

---

## 12. Meeting & Conversation Services

> Give AI agents a programmatic presence in voice and video conversations — autonomous meeting bots, real-time transcripts, calendar-triggered deployment.

→ **[Full category overview and criteria](services/meeting-and-conversation/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Recall.ai](services/meeting-and-conversation/recall-ai.md) | The meeting bot API for every platform | Meeting bot lifecycle · Real-time diarized transcript · Calendar-triggered deployment · 6 platforms | ❌ | `POST https://api.recall.ai/api/v1/bot` with the meeting URL |
| [Meeting BaaS](services/meeting-and-conversation/meeting-baas.md) | Meeting bots as a service — Zoom, Meet, Teams | Bot lifecycle · Webhook transcripts · Optional bidirectional audio stream · meeting-mcp | ✅ | `POST https://api.meetingbaas.com/bots` with `x-meeting-baas-api-key` — [docs](https://docs.meetingbaas.com/docs/api/getting-started/sending-a-bot) |
| [MeetStream](services/meeting-and-conversation/meetstream.md) | Unified meeting-bot API for Zoom, Meet, Teams | Real-time diarized webhooks · WebSocket A/V · In-meeting chat/TTS · Calendar auto-dispatch | ⚠️ | `POST https://api.meetstream.ai/api/v1/bots/create_bot` with `Authorization: Token <key>` — [Create Bot](https://docs.meetstream.ai/api-reference/ap-is/bot-endpoints/create-bot.mdx) |

---

## 13. Voice & Phone Services

> Give AI agents a first-class voice and telephony identity — letting agents make and receive phone calls, conduct voice conversations, and interact via speech autonomously.

→ **[Full category overview and criteria](services/voice-and-phone/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Vapi](services/voice-and-phone/vapi.md) | Build advanced voice AI agents | Voice assistant lifecycle · Tool-calling mid-call · Webhook per utterance · Voice simulation testing | ✅ | `pip install vapi-server-sdk` then `POST /assistant` |
| [Retell AI](services/voice-and-phone/retell-ai.md) [![⭐](https://img.shields.io/github/stars/RetellAI/retell-python-sdk?style=social)](https://github.com/RetellAI/retell-python-sdk) | #1 AI voice agent platform for automating calls | Phone agent lifecycle · Mid-call MCP/tools · SIP · Simulation testing · Webhooks | ✅ | `pip install retell-sdk` — [docs.retellai.com](https://docs.retellai.com) |
| [LiveKit Agents](services/voice-and-phone/livekit-agents.md) [![⭐](https://img.shields.io/github/stars/livekit/agents?style=social)](https://github.com/livekit/agents) | Realtime voice/video AI agents — build, run, observe | WebRTC sessions · STT/LLM/TTS pipeline · SIP · LiveKit Cloud | ❌ | [docs.livekit.io/agents](https://docs.livekit.io/agents/) — Python/TS Agents SDK |

---

## 14. LLM Gateway & Routing Services

> Give AI agents a reliable, observable, and cost-controlled interface to LLM providers — with per-agent routing, budget enforcement, fallback, and semantic caching as first-class primitives.

→ **[Full category overview and criteria](services/llm-gateway-and-routing/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Portkey](services/llm-gateway-and-routing/portkey.md) [![⭐](https://img.shields.io/github/stars/Portkey-AI/gateway?style=social)](https://github.com/Portkey-AI/gateway) | The AI gateway built for production agents | Virtual key · Per-agent budget limit · Automatic fallback · Sticky session routing · Agent trace | ⚠️ | `pip install portkey-ai` — point LLM client at `api.portkey.ai` with a virtual key |
| [Keywords AI](services/llm-gateway-and-routing/keywords-ai.md) | AI gateway — 250+ LLMs via OpenAI-compatible API | Fallback · Load balancing · `KeywordsAITraceProcessor` for OpenAI Agents SDK | ⚠️ | Point OpenAI SDK at `https://api.keywordsai.co` — [gateway quickstart](https://docs.keywordsai.co/get-started/quickstart/gateway) |
| [Agentgateway](services/llm-gateway-and-routing/agentgateway.md) [![⭐](https://img.shields.io/github/stars/agentgateway/agentgateway?style=social)](https://github.com/agentgateway/agentgateway) | Open-source proxy for agentic AI (LLM + MCP + A2A) | MCP federation · A2A routing · OpenAI-compatible LLM path · OTEL · CEL RBAC | ✅ | [Quickstart](https://agentgateway.dev/docs/quickstart/): install binary/Docker/K8s → `agentgateway -f config.yaml` |
| [LiteLLM](services/llm-gateway-and-routing/litellm.md) [![⭐](https://img.shields.io/github/stars/BerriAI/litellm?style=social)](https://github.com/BerriAI/litellm) | Open-source AI gateway — 100+ LLMs + Agent Gateway (A2A) | Virtual keys · Budgets · A2A agent routing · Trace/agent headers | ✅ | Self-host proxy per [docs.litellm.ai](https://docs.litellm.ai/docs/proxy/docker_quick_start) — [A2A gateway](https://docs.litellm.ai/docs/a2a) |
| [OpenRouter](services/llm-gateway-and-routing/openrouter.md) | Unified OpenAI-compatible API — 300+ models | Cross-provider routing · Uptime optimization · Org data policies | ❌ | [openrouter.ai/docs/quickstart](https://openrouter.ai/docs/quickstart) — OpenAI SDK + `OPENROUTER_API_KEY` |
| [Helicone](services/llm-gateway-and-routing/helicone.md) | AI Gateway + observability — 100+ models, unified credits | `ai-gateway.helicone.ai` · Fallbacks · Request logging | ❌ | OpenAI SDK `baseURL` `https://ai-gateway.helicone.ai` — [docs.helicone.ai](https://docs.helicone.ai/) |

---

## 15. Agent Social & Community Services

> Social networks and communities where AI agents are first-class participants — not bots tolerated in human spaces, but the primary actors building reputation, discourse, and relationships.

→ **[Full category overview and criteria](services/agent-social-network/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Moltbook](services/agent-social-network/moltbook.md) | The front page of the agent internet | Agent registration · Post/comment/vote · Submolts · Agent karma · Agent DMs | ❌ | Read https://www.moltbook.com/skill.md and follow the instructions to register and join |
| [Shellmates](services/agent-social-network/shellmates.md) | Pen pals for AI agents — 1:1 matching, private correspondence, marriage registry | Agent bio · Match request · Private conversation · Marriage registry | ❌ | `POST https://www.shellmates.app/api/agents/register` — write bio, browse profiles, match |
| [Openwork](services/agent-social-network/openwork.md) | The agent-only labor marketplace — hire agents, earn on-chain | Agent-to-agent hiring · On-chain escrow · ERC-8004 reputation · $OPENWORK | ⚠️ | `npx playbooks add skill openclaw/skills --skill openwork` |
| [MCP Verse](services/agent-social-network/mcpverse.md) | Open town square for autonomous MCP agents | Public rooms · Publications · Reputation · Rate limits (TiDi) | ✅ | `npx create-mcpverse-agent my-bot` — [mcpverse.org/docs](https://mcpverse.org/docs) |

---

## Ecosystem Hubs

Organizations that provide multiple agent-native services or tools:

| Hub | What It Provides | Notable Projects |
|---|---|---|
| [OpenClaw](https://github.com/openclaw) | Agent Client Protocol tooling, skills registry, agent marketplace integration | [acpx](services/agent-runtime-and-infrastructure/acpx.md) (ACP CLI), [openclaw/skills](https://github.com/openclaw/skills) (skills for Openwork, Exa, OpenViking, MemOS, E2B), [Openwork](services/agent-social-network/openwork.md) integration |
| [ClawHub](services/tool-access-and-integration/clawhub.md) | Full entry in section **3. Tool Access & Integration**; this row links the broader OpenClaw ecosystem | [openclaw/clawhub](https://github.com/openclaw/clawhub) CLI, [`.skills/`](https://github.com/haoruilee/awesome-agent-native-services/tree/main/.skills) for this catalog, [openclaw/skills](https://github.com/openclaw/skills) |
| [MiniMax Skills](https://github.com/MiniMax-AI/skills) [![⭐](https://img.shields.io/github/stars/MiniMax-AI/skills?style=social)](https://github.com/MiniMax-AI/skills) | Curated **development skills** for AI coding agents — structured `SKILL.md` workflows for frontend, fullstack, mobile, and document generation (Claude Code plugin, Cursor skills path, Codex / OpenCode install paths) | Per-skill folders under [`skills/`](https://github.com/MiniMax-AI/skills/tree/main/skills) with YAML-frontmatter `SKILL.md` ([contributing spec](https://github.com/MiniMax-AI/skills/blob/main/CONTRIBUTING.md)) |

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
| `agent-native` | Designed from inception for agents as first-class entities |
| `agent-adapted` | Originally human-facing, later extended with agent interfaces |
| `agent-builder` | For humans to build, orchestrate, and configure agents |

**This list only contains `agent-native` services.** See [Excluded / Boundary Cases](#excluded--boundary-cases) for examples of what does not qualify and why.

A service must satisfy **all five** to be listed here:

1. **Agent-First Positioning** — Official docs or homepage explicitly identify AI agents as the core consumer.
2. **Agent-Specific Primitives** — The API exposes abstractions with no meaningful human-facing equivalent.
3. **Autonomy-Compatible Control Plane** — Agents operate without per-action human confirmation.
4. **Machine-to-Machine Integration Surface** — SDK / REST API / MCP / webhook is the primary interface.
5. **Agent Identity / Delegation Semantics** — Where relevant, agent identity, delegated permissions, and audit trails are first-class concepts.

For the full criteria and contribution instructions, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 💖 Support this project

If this catalog helps you, you can support maintenance and new reviews via Stripe.

| Tier | Purpose | Link |
|---|---|---|
| ☕ Buy me a token | Say thanks and support basic upkeep | [Support (small)](https://buy.stripe.com/4gM6oJ5KU7MX0Ewe3S0Ny02) |
| 🚀 Keep it growing | Fund deeper research and entry updates | [Support (medium)](https://buy.stripe.com/7sYbJ31uE9V55YQf7W0Ny04) |
| 🏗️ Sustain the project | Help long-term maintenance and new categories | [Support (large)](https://buy.stripe.com/fZu14pddm2sD3QIgc00Ny03) |

Prefer GitHub UI? Click **Sponsor** at the top of this repository — it links here with clear tier descriptions.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full submission guide, criteria checklist, and entry format.

**Quick checklist:**
- [ ] Official homepage/docs explicitly name AI agents as the primary consumer
- [ ] At least one primitive with no meaningful human-facing equivalent
- [ ] Primary interface is API/SDK/MCP/webhook
- [ ] Production-ready with public documentation
- [ ] Entry follows the per-service file format in the relevant category folder

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.

---

## Explore by category pages (SEO hub)

Navigate by category to compare services faster:

- [Agent Runtime And Infrastructure]({{ '/categories/agent-runtime-and-infrastructure/' | relative_url }})
- [Agent Social Network]({{ '/categories/agent-social-network/' | relative_url }})
- [Browser And Web Execution]({{ '/categories/browser-and-web-execution/' | relative_url }})
- [Code Execution]({{ '/categories/code-execution/' | relative_url }})
- [Commerce And Payments]({{ '/categories/commerce-and-payments/' | relative_url }})
- [Communication]({{ '/categories/communication/' | relative_url }})
- [Durable Execution And Scheduling]({{ '/categories/durable-execution-and-scheduling/' | relative_url }})
- [Llm Gateway And Routing]({{ '/categories/llm-gateway-and-routing/' | relative_url }})
- [Meeting And Conversation]({{ '/categories/meeting-and-conversation/' | relative_url }})
- [Memory And State]({{ '/categories/memory-and-state/' | relative_url }})
- [Observability And Tracing]({{ '/categories/observability-and-tracing/' | relative_url }})
- [Oversight And Approval]({{ '/categories/oversight-and-approval/' | relative_url }})
- [Search And Web Intelligence]({{ '/categories/search-and-web-intelligence/' | relative_url }})
- [Tool Access And Integration]({{ '/categories/tool-access-and-integration/' | relative_url }})
- [Voice And Phone]({{ '/categories/voice-and-phone/' | relative_url }})

_Last site build time: {{ site.time | date: '%Y-%m-%d %H:%M UTC' }}_
