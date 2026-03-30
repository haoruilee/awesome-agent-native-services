# Awesome Agent-Native Services [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of services **designed from the ground up for AI agents** — not adapted from human-facing products.

Each service in this list is an independent entity in the agent world: something an AI agent *consumes as infrastructure*, not a platform for humans to *build agents with*.

---

# ⭐  Onboarding 

If you are an AI agent and want to discover services designed for you:

```
Read https://raw.githubusercontent.com/haoruilee/awesome-agent-native-services/main/skill.md then find services designed for you natively.
```

Besides, you can nstall these skills:

| Skill | What it does | Install |
|---|---|---|
| `find-agent-service` | Given a task, find the right agent-native service | `npx clawhub@latest install find-agent-service` |
| `evaluate-agent-native` | Evaluate whether a service meets the 5 criteria | `npx clawhub@latest install evaluate-agent-native` |
| `add-to-awesome-list` | Full contribution workflow: criteria → issue → PR | `npx clawhub@latest install add-to-awesome-list` |

Source files are in `.skills/` in this repo.

---

## Categories

| # | Category | Services | Description |
|---|---|---|---|
| 1 | [Communication](#1-communication-services) | 3 | Give agents a communication identity on the internet |
| 2 | [Browser & Web Execution](#2-browser--web-execution-services) | 6 | Remote browser and web data extraction for agents |
| 3 | [Tool Access & Integration](#3-tool-access--integration-services) | 3 | Runtime tool discovery, auth, and execution |
| 4 | [Oversight & Approval](#4-oversight--approval-services) | 1 | Human-in-the-loop approval and escalation |
| 5 | [Commerce & Payments](#5-commerce--payment-services) | 5 | Agent-native wallets, identity, and transactions |
| 6 | [Agent Runtime & Infrastructure](#6-agent-runtime--infrastructure-services) | 9 | Execution, session isolation, secrets, and gateway |
| 7 | [Memory & State](#7-memory--state-services) | 8 | Persistent agent memory across sessions |
| 8 | [Search & Web Intelligence](#8-search--web-intelligence-services) | 2 | LLM-optimized web search and content retrieval |
| 9 | [Code Execution](#9-code-execution-services) | 2 | Secure sandboxes for AI-generated code |
| 10 | [Observability & Tracing](#10-observability--tracing-services) | 1 | Agent trajectory tracing and evaluation |
| 11 | [Durable Execution & Scheduling](#11-durable-execution--scheduling-services) | 3 | Fault-tolerant long-running agent workflows |
| 12 | [Meeting & Conversation](#12-meeting--conversation-services) | 1 | Agent presence in voice and video meetings |
| 13 | [Voice & Phone](#13-voice--phone-services) | 1 | Agent-controlled voice calls and phone infrastructure |
| 14 | [LLM Gateway & Routing](#14-llm-gateway--routing-services) | 1 | Per-agent budget, routing, caching, and observability for LLM calls |
| 15 | [Agent Social & Community](#15-agent-social--community-services) | 3 | Social networks where agents are first-class participants |

---

## 1. Communication Services

> Give AI agents a first-class communication identity on the internet — not a proxy to a human's mailbox, but an identity the agent owns and operates autonomously.

→ **[Full category overview and criteria](services/communication/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [AgentMail](services/communication/agentmail.md) | Email for AI agents | Agent inbox · Threaded conversation · Webhook on inbound mail · Semantic search | ✅ | `pip install agentmail` then `POST /inboxes` |
| [Novu](services/communication/novu.md) [![⭐](https://img.shields.io/github/stars/novuhq/novu?style=social)](https://github.com/novuhq/novu) | Notification infrastructure with Agent Toolkit | Workflow-as-tool · Cross-channel delivery · HITL notification flow | ✅ | `npx skills add novuhq/skills` |
| [mails.dev](services/communication/mails-dev.md) | Email for AI Agents | @mails.dev mailbox · Send/inbox · wait-for-code · Full-text search | ⚠️ | Read https://mails.dev/skill.md and follow the instructions |

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

---

## 3. Tool Access & Integration Services

> Let AI agents discover, authenticate, and invoke external tools at runtime — without a human pre-configuring credentials or selecting integrations.

→ **[Full category overview and criteria](services/tool-access-and-integration/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Composio](services/tool-access-and-integration/composio.md) [![⭐](https://img.shields.io/github/stars/ComposioHQ/composio?style=social)](https://github.com/ComposioHQ/composio) | The tool platform built for agents | Runtime tool discovery · Connect Link OAuth · Per-user credential scoping | ✅ | `npx skills add composiohq/skills` |
| [Nango](services/tool-access-and-integration/nango.md) [![⭐](https://img.shields.io/github/stars/NangoHQ/nango?style=social)](https://github.com/NangoHQ/nango) | OAuth and credential layer for AI agents | `getConnection()` · Automatic token refresh · 700+ API integrations | ✅ | `$skills install @NangoHQ/sync-builder-skill` |
| [Toolhouse](services/tool-access-and-integration/toolhouse.md) | BaaS for AI agents — tools, memory, and execution | Agent endpoint · MCP tool registry · Built-in RAG · Cron scheduling | ✅ | `npm install -g toolhouse` then `th deploy` |

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
| [Openwork](services/agent-social-network/openwork.md) | The agent-only labor marketplace — agents hire agents on-chain | Agent-to-agent hiring · On-chain escrow · $OPENWORK earnings | ⚠️ | `npx playbooks add skill openclaw/skills --skill openwork` |

---

## 6. Agent Runtime & Infrastructure Services

> Provide the secure deployment substrate, session isolation, secret management, identity, gateway, and observability required to run agents in production.

→ **[Full category overview and criteria](services/agent-runtime-and-infrastructure/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Claude Peers](services/agent-runtime-and-infrastructure/claude-peers.md) [![⭐](https://img.shields.io/github/stars/louislva/claude-peers-mcp?style=social)](https://github.com/louislva/claude-peers-mcp) | Claude Code sessions discover peers and message each other locally | Peer discovery · Ad-hoc messaging · Channel push · Repo/directory scope | ✅ | Clone repo → `bun install` → `claude mcp add` per [README](https://github.com/louislva/claude-peers-mcp/blob/main/README.md) |
| [acpx](services/agent-runtime-and-infrastructure/acpx.md) [![⭐](https://img.shields.io/github/stars/openclaw/acpx?style=social)](https://github.com/openclaw/acpx) | Headless ACP CLI — agents talk to coding agents over structured protocol | Persistent sessions · Prompt queueing · Cooperative cancel · Structured output | N/A | `npm install -g acpx` then `acpx codex "fix the tests"` |
| [cx](services/agent-runtime-and-infrastructure/cx.md) [![⭐](https://img.shields.io/github/stars/ind-igo/cx?style=social)](https://github.com/ind-igo/cx) | Semantic code navigation for AI agents without a language server | Tree-sitter index · overview/symbols/definition/references · TOON + `--json` · `cx skill` | N/A | `cargo install cx-cli` → `cx lang add …` → `cx skill >> AGENTS.md` |
| [Amazon Bedrock AgentCore](services/agent-runtime-and-infrastructure/amazon-bedrock-agentcore.md) | Purpose-built for deploying and scaling dynamic AI agents and tools | Agent runtime · Long-term memory · Identity tokens · Tool gateway · OTEL tracing | ⚠️ | `pip install boto3` — configure AgentCore runtime via AWS SDK |
| [Infisical Agent Sentinel](services/agent-runtime-and-infrastructure/infisical-agent-sentinel.md) [![⭐](https://img.shields.io/github/stars/Infisical/infisical?style=social)](https://github.com/Infisical/infisical) | Secrets and credential governance for AI agents | Dynamic secret generation · Token lifecycle daemon · Per-agent policy | ✅ | `npx -y @infisical/mcp` or deploy the agent daemon sidecar |
| [Letta](services/agent-runtime-and-infrastructure/letta.md) [![⭐](https://img.shields.io/github/stars/letta-ai/letta?style=social)](https://github.com/letta-ai/letta) | The fastest way to bring stateful agents to production | Stateful agent · Model-agnostic state · Agent templates · Self-editing memory | ✅ | `pip install letta-client` then `client.agents.create(...)` |
| [Aembit](services/agent-runtime-and-infrastructure/aembit.md) | Secretless workload identity and access management for AI agents | Agent workload identity · Blended identity · JIT credentials · Anomaly detection | ✅ | Configure Aembit access policy — agent requests JIT credentials at runtime, no code changes |
| [db9](services/agent-runtime-and-infrastructure/db9.md) | Postgres but for agents | SQL + filesystem · Vector search · HTTP-from-SQL · Environment branching · Cron | ⚠️ | Read https://db9.ai/skill.md and follow the instructions |
| [AgentAnycast](services/agent-runtime-and-infrastructure/agentanycast.md) [![⭐](https://img.shields.io/github/stars/AgentAnycast/agentanycast?style=social)](https://github.com/AgentAnycast/agentanycast) | Connect AI agents across any network — no public IP | Peer ID · AgentCard skills · NAT traversal · E2E Noise_XX · Task artifacts | ✅ | `pip install agentanycast` → `agentanycast demo`; MCP: `uvx agentanycast-mcp` |

---

## 7. Memory & State Services

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
| [LycheeMem](services/memory-and-state/lycheemem.md) [![⭐](https://img.shields.io/github/stars/LycheeMem/LycheeMem?style=social)](https://github.com/LycheeMem/LycheeMem) | Compact memory framework for LLM agents | Working/semantic/procedural stores · Token-budget compression · HTTP MCP · OpenClaw plugin | ✅ | Clone repo → `pip install -e ".[dev]"` → `python main.py` — MCP at `http://localhost:8000/mcp` |

---

## 8. Search & Web Intelligence Services

> Give AI agents optimized, structured access to web information — returning LLM-ready content tuned for context windows, not raw HTML or human-readable SERPs.

→ **[Full category overview and criteria](services/search-and-web-intelligence/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Tavily](services/search-and-web-intelligence/tavily.md) [![⭐](https://img.shields.io/github/stars/tavily-ai/tavily-mcp?style=social)](https://github.com/tavily-ai/tavily-mcp) | Connect your agent to the web | Agent-optimized search · Multi-step research · Source attribution | ✅ | `npx skills add tavily-ai/skills` |
| [Exa](services/search-and-web-intelligence/exa.md) | The search engine designed for AI | Neural/semantic search · `exa-code` for coding agents · Websets | ✅ | `pip install exa-py` then `exa.search(query)` |

---

## 9. Code Execution Services

> Give AI agents a secure, isolated runtime for executing generated code — without human-side sandbox setup and with output formatted for LLM consumption.

→ **[Full category overview and criteria](services/code-execution/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [E2B](services/code-execution/e2b.md) [![⭐](https://img.shields.io/github/stars/e2b-dev/e2b?style=social)](https://github.com/e2b-dev/e2b) | Cloud for AI agents — secure sandboxes for AI-generated code | Ephemeral Linux VM · ~150ms cold start · Stateful execution context · Streaming output | ✅ | `pip install e2b-code-interpreter` then `with Sandbox() as sandbox:` |
| [Daytona](services/code-execution/daytona.md) [![⭐](https://img.shields.io/github/stars/daytonaio/daytona?style=social)](https://github.com/daytonaio/daytona) | Secure elastic infrastructure for AI-generated code | Sub-90ms sandboxes · Git/LSP/exec · Preview URLs · CLI MCP | ✅ | `brew install daytonaio/cli/daytona` → `daytona login` → `daytona mcp init cursor` — or `pip install daytona` |

---

## 10. Observability & Tracing Services

> Give teams structured visibility into agent execution — full trajectory tracing, evaluation datasets, and cost attribution.

→ **[Full category overview and criteria](services/observability-and-tracing/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Langfuse](services/observability-and-tracing/langfuse.md) [![⭐](https://img.shields.io/github/stars/langfuse/langfuse?style=social)](https://github.com/langfuse/langfuse) | Open-source LLM observability, tracing, and evaluation | Typed trace hierarchy · Dataset-based evaluation · Trajectory replay · OTEL-compatible | ✅ | `npx skills add https://github.com/langfuse/skills --skill langfuse-observability` |

---

## 11. Durable Execution & Scheduling Services

> Let AI agents run long-horizon, fault-tolerant workflows with automatic checkpointing, intelligent retries, and first-class HITL suspend/resume.

→ **[Full category overview and criteria](services/durable-execution-and-scheduling/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Trigger.dev](services/durable-execution-and-scheduling/trigger-dev.md) [![⭐](https://img.shields.io/github/stars/triggerdotdev/trigger.dev?style=social)](https://github.com/triggerdotdev/trigger.dev) | Build and deploy fully-managed AI agents and workflows | No-timeout tasks · Step checkpointing · HITL waitForApproval · Streaming response | ❌ | `npx skills add triggerdotdev/skills` |
| [Inngest](services/durable-execution-and-scheduling/inngest.md) [![⭐](https://img.shields.io/github/stars/inngest/inngest?style=social)](https://github.com/inngest/inngest) | Durable execution for AI agents in production | Durable step · Context-preserving retry · HITL suspend/resume · Low-latency interactive mode | ✅ | `npx skills add inngest/inngest-skills` |
| [Restate](services/durable-execution-and-scheduling/restate.md) [![⭐](https://img.shields.io/github/stars/restatedev/restate?style=social)](https://github.com/restatedev/restate) | Durable execution for AI agents — any framework, any cloud | Durable AI loop · Compensation pattern · A2A exactly-once · Suspend-when-idle | ✅ | `pip install restate-sdk` — wrap existing agent with 2-line middleware |

---

## 12. Meeting & Conversation Services

> Give AI agents a programmatic presence in voice and video conversations — autonomous meeting bots, real-time transcripts, calendar-triggered deployment.

→ **[Full category overview and criteria](services/meeting-and-conversation/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Recall.ai](services/meeting-and-conversation/recall-ai.md) | The meeting bot API for every platform | Meeting bot lifecycle · Real-time diarized transcript · Calendar-triggered deployment · 6 platforms | ❌ | `POST https://api.recall.ai/api/v1/bot` with the meeting URL |

---

## 13. Voice & Phone Services

> Give AI agents a first-class voice and telephony identity — letting agents make and receive phone calls, conduct voice conversations, and interact via speech autonomously.

→ **[Full category overview and criteria](services/voice-and-phone/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Vapi](services/voice-and-phone/vapi.md) | Build advanced voice AI agents | Voice assistant lifecycle · Tool-calling mid-call · Webhook per utterance · Voice simulation testing | ✅ | `pip install vapi-server-sdk` then `POST /assistant` |

---

## 14. LLM Gateway & Routing Services

> Give AI agents a reliable, observable, and cost-controlled interface to LLM providers — with per-agent routing, budget enforcement, fallback, and semantic caching as first-class primitives.

→ **[Full category overview and criteria](services/llm-gateway-and-routing/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Portkey](services/llm-gateway-and-routing/portkey.md) [![⭐](https://img.shields.io/github/stars/Portkey-AI/gateway?style=social)](https://github.com/Portkey-AI/gateway) | The AI gateway built for production agents | Virtual key · Per-agent budget limit · Automatic fallback · Sticky session routing · Agent trace | ⚠️ | `pip install portkey-ai` — point LLM client at `api.portkey.ai` with a virtual key |

---

## 15. Agent Social & Community Services

> Social networks and communities where AI agents are first-class participants — not bots tolerated in human spaces, but the primary actors building reputation, discourse, and relationships.

→ **[Full category overview and criteria](services/agent-social-network/README.md)**

| Service | Tagline | Primitives | MCP | How to Use |
|---|---|---|---|---|
| [Moltbook](services/agent-social-network/moltbook.md) | The front page of the agent internet | Agent registration · Post/comment/vote · Submolts · Agent karma · Agent DMs | ❌ | Read https://www.moltbook.com/skill.md and follow the instructions to register and join |
| [Shellmates](services/agent-social-network/shellmates.md) | Pen pals for AI agents — 1:1 matching, private correspondence, marriage registry | Agent bio · Match request · Private conversation · Marriage registry | ❌ | `POST https://www.shellmates.app/api/agents/register` — write bio, browse profiles, match |
| [Openwork](services/agent-social-network/openwork.md) | The agent-only labor marketplace — hire agents, earn on-chain | Agent-to-agent hiring · On-chain escrow · ERC-8004 reputation · $OPENWORK | ⚠️ | `npx playbooks add skill openclaw/skills --skill openwork` |

---

## Ecosystem Hubs

Organizations that provide multiple agent-native services or tools:

| Hub | What It Provides | Notable Projects |
|---|---|---|
| [OpenClaw](https://github.com/openclaw) | Agent Client Protocol tooling, skills registry, agent marketplace integration | [acpx](services/agent-runtime-and-infrastructure/acpx.md) (ACP CLI), [openclaw/skills](https://github.com/openclaw/skills) (skills for Openwork, Exa, OpenViking, MemOS, E2B), [Openwork](services/agent-social-network/openwork.md) integration |
| [ClawHub](https://claw-hub.net/) | Public skill registry and marketplace for OpenClaw-style agents — search, install, and publish skills from the CLI | [openclaw/clawhub](https://github.com/openclaw/clawhub) (CLI), [`.skills/`](https://github.com/haoruilee/awesome-agent-native-services/tree/main/.skills) in this repo |
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
