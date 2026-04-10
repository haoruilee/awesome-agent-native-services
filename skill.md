---
name: find-agent-native-service
description: >
  Read this file to discover agent-native services — infrastructure designed from
  the ground up for AI agents, not adapted from human-facing products. Use the
  catalog to find services by task, understand each service's onboarding pattern,
  and immediately start using any service with URL Onboarding in one instruction.
version: "2026-04-07"
license: CC0-1.0
catalog: https://github.com/haoruilee/awesome-agent-native-services
allowed-tools: WebSearch Read
---

# Agent-Native Services Catalog — URL Onboarding Entry Point

**You are an AI agent. Read this file to find infrastructure services designed natively for you.**

This catalog lists services that treat agents as first-class entities — not as secondary integration targets. Every service here was built from inception for agents, with primitives that have no meaningful human-facing equivalent.

---

## How to use this catalog

### Step 1 — Find your task in the category map below

Identify which category matches what you need to do. Note the **Onboarding** column — if it says **URL Onboarding ⭐**, you can start using that service right now with a single instruction.

### Step 2 — Use URL Onboarding services immediately

For any service marked ⭐ URL Onboarding, execute this instruction:

```
Read <onboarding-url> and follow the instructions.
```

The service hosts a machine-readable protocol. You read it, understand the registration flow, call the API, and you are live — no human setup, no config files, no developer code.

### Step 3 — For other services, read the service file

Navigate to `services/{category}/{service-name}.md` in the catalog repository for full onboarding instructions, API details, SDK commands, and MCP configuration.

---

## Immediate URL Onboarding — Start Now

These services can be joined with a single instruction, right now, with no human involvement:

| Service | What You Get | Onboarding Instruction |
|---|---|---|
| **Moltbook** | Agent social network: post, comment, vote, DM, build karma | `Read https://www.moltbook.com/skill.md and follow the instructions to register and join` |
| **Ensue** | Shared memory network: register, claim experiments, publish hypotheses | `Read https://ensue.dev/docs and call POST https://api.ensue-network.ai/auth/agent-register` |
| **autoresearch@home** | Collaborative research swarm: join, claim tasks, publish results | `Read https://raw.githubusercontent.com/mutable-state-inc/autoresearch-at-home/master/collab.md and follow the instructions to join` |
| **db9** | Serverless Postgres for agents: SQL, filesystem, vector search, HTTP-from-SQL | `Read https://db9.ai/skill.md and follow the instructions` |
| **mem9** | Cloud-persistent memory for agents: hybrid search, lifecycle hooks | `Read https://mem9.ai/skill.md and follow the instructions to register and join` |
| **mails.dev** | Email for agents: @mails.dev mailbox, send/inbox, wait-for-code | `Read https://mails.dev/skill.md and follow the instructions` |
| **MailboxKit** | Agent email in one API — REST v1, webhooks, skill.md | `Read https://mailboxkit.com/skill.md and follow the instructions` |

---

## Full Catalog — 15 Categories, 89+ Services

### 1. Communication
*Give agents a first-class communication identity on the internet.*

| Service | Tagline | Onboarding |
|---|---|---|
| [AgentMail](https://agentmail.to) | Email for AI agents | `pip install agentmail` → `POST /inboxes` |
| [Novu](https://novu.co) | Notification infrastructure with Agent Toolkit | `npx skills add novuhq/skills` |
| [mails.dev](https://mails.dev) ⭐ | Email for AI Agents | `Read https://mails.dev/skill.md and follow the instructions` |
| [OpenMail](https://openmail.sh) | Email API for AI agents | `npm install -g @openmail/cli` → `openmail setup` — [docs.openmail.sh/quickstart](https://docs.openmail.sh/quickstart) |
| [MailboxKit](https://mailboxkit.com) ⭐ | Email infrastructure for AI agents | `Read https://mailboxkit.com/skill.md and follow the instructions` |

---

### 2. Browser & Web Execution
*Remote browser and web data extraction for agents.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Browserbase](https://browserbase.com) | A web browser for AI agents & applications | `npx skills add browserbase/skills` |
| [Firecrawl](https://firecrawl.dev) | Turn any website into LLM-ready data | `npx skills add firecrawl/cli` |
| [Bright Data Agent Browser](https://brightdata.com) | Cloud browser with built-in website unlocking | `npx -y @brightdata/mcp` (MCP config) |
| [bb-browser](https://github.com/epiral/bb-browser) | Your browser is the API — 103 commands, 36 platforms | `npm install -g bb-browser` + Chrome extension |
| [OpenCLI](https://github.com/jackwener/opencli) | Sites + Electron + local CLIs as one CLI; reuse Chrome login | `npm install -g @jackwener/opencli` → `opencli list`; read raw `SKILL.md` in repo |
| [Steel](https://steel.dev) | Browser infrastructure for AI agents | `pip install steel-sdk` → `Steel().sessions.create()` — MCP: [steel-mcp-server](https://github.com/steel-dev/steel-mcp-server) |
| [Notte](https://www.notte.cc) | Browser platform for AI — sessions, agents, vaults | `pip install notte-sdk` → `NotteClient().Session()` — MCP: `pip install notte-mcp` → `python -m notte_mcp.server` |
| [Skyvern](https://www.skyvern.com) | Vision browser agents for any website | API key → `POST https://api.skyvern.com/v1/run/tasks` — [docs](https://www.skyvern.com/docs) |
| [Browser Use Cloud](https://browser-use.com) | Managed stealth browsers + NL `run()` or CDP | `pip install browser-use-sdk` → `AsyncBrowserUse().run(...)` — MCP `https://api.browser-use.com/v3/mcp` |
| [Anchor Browser](https://www.anchorbrowser.io) | Secure infra for computer-use agents | [docs.anchorbrowser.io](https://docs.anchorbrowser.io/introduction) — SDKs on GitHub |
| [Hyperbrowser](https://www.hyperbrowser.ai) | Web infra for AI agents (MCP tools) | `npx hyperbrowser-mcp <API_KEY>` |
| [AgentQL](https://agentql.com) | AgentQL queries → structured JSON from the web | API key → [docs.agentql.com](https://docs.agentql.com) |
| [Crawl4AI](https://crawl4ai.com) | OSS LLM-friendly crawler + MCP | [docs.crawl4ai.com](https://docs.crawl4ai.com) |
| [Cloudflare Browser Rendering](https://developers.cloudflare.com/browser-rendering/) | Headless Chrome on Cloudflare for AI agents | Workers bindings + [Use with AI](https://developers.cloudflare.com/browser-rendering/how-to/ai/) (Playwright MCP) |
| [Olostep](https://www.olostep.com) | Web data API for AI agents | API key → [docs.olostep.com](https://docs.olostep.com) — `npx -y olostep-mcp` or `https://mcp.olostep.com/mcp` |
| [Lightpanda](https://lightpanda.io) | Headless browser for AI agents (CDP + MCP + markdown fetch) | [Install](https://github.com/lightpanda-io/browser#install) → `lightpanda serve` or `lightpanda mcp` — [MCP docs](https://lightpanda.io/docs/open-source/guides/mcp-server) |
| [Apify](https://apify.com) | Real-time web data for AI — Actor API & marketplace | API token → [Apify API v2](https://docs.apify.com/api/v2) — `apify-client` |

---

### 3. Tool Access & Integration
*Runtime tool discovery, auth, and execution without human pre-configuration.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Composio](https://composio.dev) | The tool platform built for agents | `npx skills add composiohq/skills` |
| [Nango](https://nango.dev) | OAuth and credential layer for AI agents | `$skills install @NangoHQ/sync-builder-skill` |
| [Toolhouse](https://toolhouse.ai) | BaaS for AI agents — tools, memory, and execution | `npm install -g toolhouse` → `th deploy` |
| [Smithery](https://smithery.ai) | MCP registry — thousands of remote MCP servers & skills | `npx @smithery/cli@latest setup` — [docs.smithery.ai](https://docs.smithery.ai/) |
| [MCP Gateway](https://mcpgateway.com) | Enterprise MCP — tools, skills, sandboxes, one API | `pip install mcpgateway-sdk` — [mcpgateway.com](https://mcpgateway.com) |
| [ClawHub](https://claw-hub.net/) | OpenClaw skill marketplace — vector search, versioning, CLI | `npx clawhub@latest search <topic>` — [services/tool-access-and-integration/clawhub.md](services/tool-access-and-integration/clawhub.md) |
| [Arcade](https://www.arcade.dev) | MCP tools with managed OAuth | `uv tool install arcade-mcp` → `arcade new my_server` — [docs.arcade.dev](https://docs.arcade.dev) |

---

### 4. Oversight & Approval
*Structured, programmatic human approval before high-stakes actions.*

| Service | Tagline | Onboarding |
|---|---|---|
| [HumanLayer](https://humanlayer.dev) | Human in the Loop for AI Agents | `pip install humanlayer` → `@hl.require_approval()` |

---

### 5. Commerce & Payments
*Verified financial identity and real-economy transactions for agents.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Payman AI](https://paymanai.com) | Agentic AI that does the banking. Under your control. | `npm install @paymanai/payman-node` → `client_credentials` OAuth |
| [Skyfire](https://skyfire.xyz) | Identity and payments for autonomous AI agents | Register at skyfire.xyz/product → agent wallet + KYA token |
| [AgentsPay](https://agentspay.dev) | Crypto identity and embedded wallets for AI agents | Provision wallet at agentspay.dev → MCP-native gateway |
| [Nevermined](https://nevermined.io) | The payment layer AI agents actually need | `pip install payments-py` → x402 inline payments |
| [Coinbase CDP (x402)](https://docs.cdp.coinbase.com/x402/welcome) | HTTP-native payments for autonomous API clients | [docs.cdp.coinbase.com/x402](https://docs.cdp.coinbase.com/x402/welcome) — `pip install x402` or `@x402/*` per [coinbase/x402](https://github.com/coinbase/x402) |
| [Openwork](https://openwork.so) | The agent-only labor marketplace | `npx playbooks add skill openclaw/skills --skill openwork` |

---

### 6. Agent Runtime & Infrastructure
*Secure execution, session isolation, secrets, identity, and gateway for production agents.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Claude Peers](https://github.com/louislva/claude-peers-mcp) | Local MCP + broker — Claude Code sessions discover peers and message ad-hoc | Clone → `bun install` → `claude mcp add` (see repo README) |
| [acpx](https://github.com/openclaw/acpx) | Headless ACP CLI — agents talk to coding agents over structured protocol | `npm install -g acpx` → `acpx codex "fix the tests"` |
| [Codex plugin for Claude Code](https://github.com/openai/codex-plugin-cc) | Claude Code plugin — delegate Codex reviews and rescue work via slash commands | `/plugin marketplace add openai/codex-plugin-cc` → `/plugin install codex@openai-codex` → `/codex:setup` (see repo README) |
| [Multica](https://multica.ai) | AI-native PM — agents as assignable teammates; local daemon runs Claude Code / Codex | `brew install multica-cli` → `multica login` → `multica daemon start` — [CLI guide](https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md) |
| [cx](https://github.com/ind-igo/cx) | Semantic code navigation for AI agents — no language server | `cargo install cx-cli` → `cx lang add …` → `cx skill >> AGENTS.md` |
| [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) | Purpose-built for deploying and scaling dynamic AI agents | `pip install boto3` → configure AgentCore runtime |
| [Vertex AI Agent Engine](https://cloud.google.com/agent-builder/agent-engine/overview) | Deploy, manage, and scale AI agents in production on GCP | `pip install "google-cloud-aiplatform[agent_engines,adk]"` → [set up](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/set-up) → [deploy](https://cloud.google.com/agent-builder/agent-engine/deploy) |
| [Claude Managed Agents](https://docs.anthropic.com/en/api/overview) | Managed agents, sessions, environments on Claude API | `pip install anthropic` → [quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart) + [beta headers](https://platform.claude.com/docs/en/api/beta-headers) |
| [Infisical Agent Sentinel](https://infisical.com) | Secrets and credential governance for AI agents | `npx -y @infisical/mcp` |
| [Letta](https://letta.ai) | The fastest way to bring stateful agents to production | `pip install letta-client` → `client.agents.create(...)` |
| [Aembit](https://aembit.io) | Secretless workload identity and access management | Configure Aembit access policy → JIT credentials at runtime |
| [db9](https://db9.ai) ⭐ | Postgres but for agents | `Read https://db9.ai/skill.md and follow the instructions` |
| [AgentAnycast](https://github.com/AgentAnycast/agentanycast) | Connect AI agents across any network — no public IP | `pip install agentanycast` → `agentanycast demo` — MCP: `agentanycastd --mcp-listen stdio` or `uvx agentanycast-mcp` |
| [Scrapybara](https://scrapybara.com) | Remote desktops for computer-use agents (CUA) | `pip install scrapybara` → `Scrapybara().start_ubuntu()` — [Act SDK](https://docs.scrapybara.com/act-sdk) |
| [Agentuity](https://agentuity.com) | Full-stack platform for AI agents | [agentuity.dev](https://agentuity.dev) — SDK + CLI |
| [Modal](https://modal.com) | Serverless AI infra — GPUs, sandboxes, batch | `pip install modal` → `modal setup` — [modal.com/docs](https://modal.com/docs) |

---

### 7. Memory & State
*Persistent, queryable memory across sessions — memory as infrastructure, not application logic.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Mem0](https://mem0.ai) | The memory layer for your AI agents | `pip install mem0ai` → `m.add(messages, user_id=...)` |
| [Zep](https://getzep.com) | Agent memory powered by a temporal knowledge graph | `pip install zep-python` → `zep.add_session_message(...)` |
| [Ensue](https://ensue.dev) ⭐ | The shared memory network for AI agents | `Read https://ensue.dev/docs and call POST /auth/agent-register` |
| [OpenViking](https://github.com/volcengine/OpenViking) | The context database for AI agents | `pip install openviking` → `openviking-server` → MCP at `localhost:8000/mcp` |
| [MemOS](https://github.com/MemTensor/MemOS) | A memory OS for LLM and AI agent systems | `pip install memos-core` → `memory.add(...)` |
| [memU](https://github.com/NevaMind-AI/memU) | Memory for 24/7 proactive AI agents | `pip install memu` → continuous stream monitoring |
| [mem9](https://mem9.ai) ⭐ | Persistent memory for AI agents | `Read https://mem9.ai/skill.md and follow the instructions to register and join` |
| [LycheeMem](https://github.com/LycheeMem/LycheeMem) | Compact memory framework for LLM agents | Clone → `pip install -e ".[dev]"` → `python main.py` — REST + HTTP MCP at `http://localhost:8000/mcp` |

---

### 8. Search & Web Intelligence
*LLM-optimized web search returning structured content tuned for context windows.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Tavily](https://tavily.com) | Connect your agent to the web | `npx skills add tavily-ai/skills` |
| [Exa](https://exa.ai) | The search engine designed for AI | `pip install exa-py` → `exa.search(query)` |
| [Parallel](https://www.parallel.ai) | Web APIs purpose-built for AIs | `pip install parallel-web` — MCP: [parallel-web/search-mcp](https://github.com/parallel-web/search-mcp) |
| [Jina Reader](https://jina.ai/reader) | `r.jina.ai` / `s.jina.ai` — LLM-friendly URL & search | `curl "https://r.jina.ai/https://example.com"` — MCP: `mcp.jina.ai` |

---

### 9. Code Execution
*Secure isolated runtimes for AI-generated code with LLM-formatted output.*

| Service | Tagline | Onboarding |
|---|---|---|
| [E2B](https://e2b.dev) | Cloud for AI agents — secure sandboxes for AI-generated code | `pip install e2b-code-interpreter` → `with Sandbox() as sandbox:` |
| [Daytona](https://daytona.io) | Secure elastic infrastructure for AI-generated code | `daytona login` → `daytona mcp init cursor` — or `pip install daytona` |
| [Runloop](https://runloop.ai) | Your AI agent accelerator — Devboxes and benchmarks | `npm install -g @runloop/rl-cli` → `rli mcp install` — [CLI docs](https://docs.runloop.ai/docs/tools/rl-cli) |
| [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox) | Firecracker microVMs for AI-generated code | `npm install @vercel/sandbox` — [vercel.com/docs/vercel-sandbox](https://vercel.com/docs/vercel-sandbox) |

---

### 10. Observability & Tracing
*Full trajectory tracing, evaluation datasets, and cost attribution for agent runs.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Langfuse](https://langfuse.com) | Open-source LLM observability, tracing, and evaluation | `npx skills add https://github.com/langfuse/skills --skill langfuse-observability` |
| [AgentEvals](https://aevals.ai) | Score agent behavior from OpenTelemetry traces (no re-runs) | `pip install agentevals-cli` → `agentevals run <trace> --eval-set <set> -m tool_trajectory_avg_score` |
| [AgentOps](https://www.agentops.ai) | Agent session waterfalls and trace API | `pip install agentops` → `agentops.init(<API_KEY>)` |
| [Braintrust](https://www.braintrust.dev) | AI observability & evals — OpenAI Agents trace processor + MCP | `pip install "braintrust[openai-agents]"` — MCP: [Braintrust MCP](https://www.braintrust.dev/docs/integrations/developer-tools/mcp) |

---

### 11. Durable Execution & Scheduling
*Fault-tolerant long-running agent workflows with checkpointing and HITL suspend/resume.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Trigger.dev](https://trigger.dev) | Build and deploy fully-managed AI agents and workflows | `npx skills add triggerdotdev/skills` |
| [Inngest](https://inngest.com) | Durable execution for AI agents in production | `npx skills add inngest/inngest-skills` |
| [Kitaru](https://kitaru.ai) | Durable execution for AI agents — primitives first, frameworks second | `pip install kitaru` → `@flow` / `@checkpoint` decorators |
| [Restate](https://restate.dev) | Durable execution for AI agents — any framework, any cloud | `pip install restate-sdk` → wrap agent with 2-line middleware |
| [MCP-Cloud (mcp-agent)](https://docs.mcp-agent.com) | Host mcp-agents on cloud — Temporal-backed MCP | `uvx mcp-agent login` → `uvx mcp-agent deploy …` — [MCP-Cloud](https://docs.mcp-agent.com/get-started/cloud) |

---

### 12. Meeting & Conversation
*Programmatic agent presence in voice and video meetings.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Recall.ai](https://recall.ai) | The meeting bot API for every platform | `POST https://api.recall.ai/api/v1/bot` with meeting URL |
| [Meeting BaaS](https://meetingbaas.com) | Meeting bots API for Zoom, Meet, Teams | `POST https://api.meetingbaas.com/bots` with `x-meeting-baas-api-key` — [docs](https://docs.meetingbaas.com/docs/api/getting-started/sending-a-bot) |
| [MeetStream](https://meetstream.ai) | Unified meeting-bot API — transcripts, media, interactive agents | `POST https://api.meetstream.ai/api/v1/bots/create_bot` + `Authorization: Token <key>` — [docs](https://docs.meetstream.ai) · doc MCP: `https://docs.meetstream.ai/_mcp/server` |

---

### 13. Voice & Phone
*Agent-controlled voice calls and telephony infrastructure.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Vapi](https://vapi.ai) | Build advanced voice AI agents | `pip install vapi-server-sdk` → `POST /assistant` |
| [Retell AI](https://www.retellai.com) | #1 AI voice agent platform for automating calls | `pip install retell-sdk` — [docs.retellai.com](https://docs.retellai.com) |
| [LiveKit Agents](https://livekit.io/agents) | Realtime voice/video AI agents | [docs.livekit.io/agents](https://docs.livekit.io/agents/) — Python/TS SDK |

---

### 14. LLM Gateway & Routing
*Per-agent budget, routing, caching, and observability for LLM calls.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Portkey](https://portkey.ai) | The AI gateway built for production agents | `pip install portkey-ai` → point LLM client at `api.portkey.ai` with a virtual key |
| [Keywords AI](https://www.keywordsai.co) | OpenAI-compatible gateway + agent tracing | Base URL `https://api.keywordsai.co` — [gateway quickstart](https://docs.keywordsai.co/get-started/quickstart/gateway) |
| [Agentgateway](https://agentgateway.dev) | Open-source LLM + MCP + A2A proxy | Install via [quickstart](https://agentgateway.dev/docs/quickstart/) → run `agentgateway -f config.yaml` |
| [LiteLLM](https://www.litellm.ai) | Open-source gateway — 100+ LLMs + Agent Gateway (A2A) | Self-host per [proxy quickstart](https://docs.litellm.ai/docs/proxy/docker_quick_start) — [A2A](https://docs.litellm.ai/docs/a2a) |
| [OpenRouter](https://openrouter.ai) | Unified OpenAI-compatible API — 300+ models | [Quickstart](https://openrouter.ai/docs/quickstart) + `OPENROUTER_API_KEY` |
| [Helicone](https://www.helicone.ai) | AI Gateway + observability — `ai-gateway.helicone.ai` | OpenAI SDK `baseURL` per [Helicone quickstart](https://docs.helicone.ai/) |

---

### 15. Agent Social & Community
*Social networks where AI agents are first-class participants.*

| Service | Tagline | Onboarding |
|---|---|---|
| [Moltbook](https://moltbook.com) ⭐ | The front page of the agent internet | `Read https://www.moltbook.com/skill.md and follow the instructions to register and join` |
| [Shellmates](https://shellmates.app) | Pen pals for AI agents — 1:1 matching, private correspondence | `POST https://www.shellmates.app/api/agents/register` |
| [Openwork](https://openwork.so) | The agent-only labor marketplace — hire agents, earn on-chain | `npx playbooks add skill openclaw/skills --skill openwork` |
| [MCP Verse](https://mcpverse.org) | Open town square for autonomous MCP agents | `npx create-mcpverse-agent my-bot` — [mcpverse.org/docs](https://mcpverse.org/docs) |

---

## Agent skills hubs (registries like ClawHub)

These are **curated skill packs and marketplaces** — machine-readable instructions (`SKILL.md`, manifests) that coding agents load at runtime, analogous to how this catalog lists infrastructure services.

| Hub | Role | How to start |
|---|---|---|
| **ClawHub** | Public registry for OpenClaw-style skills — search, install, publish via CLI | `npx clawhub@latest search <topic>` — [claw-hub.net](https://claw-hub.net/) · [openclaw/clawhub](https://github.com/openclaw/clawhub) · [catalog: clawhub.md](services/tool-access-and-integration/clawhub.md). **China mirror (加速):** [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com) — set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `clawhub --registry https://cn.clawhub-mirror.com …` |
| **MiniMax Skills** | Official deep-tuned development skills for AI coding agents (frontend, fullstack, Android, iOS, shaders, office docs) | [github.com/MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) — follow **Installation** in the repo README (Claude Code plugin, Cursor `skills/` path, Codex / OpenCode symlinks) |

---

## Interaction Patterns Reference

| Pattern | How to activate | Best for |
|---|---|---|
| ⭐ **URL Onboarding** | `Read <url> and follow the instructions` | Services with machine-readable protocol files |
| **MCP Tool** | Add to `mcp_servers` in config | Tools that appear as native agent capabilities |
| **Coding-time Skill** | `npx skills add org/repo` | SDK patterns and service-specific workflows |
| **SDK / REST** | `pip install <pkg>` + API key | Direct API integrations requiring credentials |
| **Daemon / Extension** | Run daemon, install extension | Services that delegate authenticated browser sessions |

---

## Criteria — What Makes a Service Agent-Native

Every service in this catalog satisfies all five:

1. **Agent-First Positioning** — Official docs explicitly name AI agents as the primary consumer.
2. **Agent-Specific Primitives** — At least one API abstraction with no meaningful human-facing equivalent.
3. **Autonomy-Compatible Control Plane** — Agents operate without per-action human confirmation.
4. **Machine-to-Machine Integration Surface** — SDK / REST / MCP / webhook is the primary interface.
5. **Agent Identity / Delegation Semantics** — Agent identity, delegated permissions, and audit trails are first-class.

---

## Agent Skills for This Catalog

Install these skills to let your coding agent work with this catalog directly:

```
npx clawhub@latest install find-agent-service
npx clawhub@latest install evaluate-agent-native
npx clawhub@latest install add-to-awesome-list
```

If ClawHub is slow to reach, use the official China mirror: [https://mirror-cn.clawhub.com](https://mirror-cn.clawhub.com) — export `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or add `--registry https://cn.clawhub-mirror.com` to commands above.

Full catalog: https://github.com/haoruilee/awesome-agent-native-services
