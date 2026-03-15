# Awesome Agent-Native Services [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of services **designed from the ground up for AI agents** — not adapted from human-facing products.

Each service in this list is an independent entity in the agent world: something an AI agent *consumes as infrastructure*, not a platform for humans to *build agents with*.

---

## Agent Skills for This Repo

This repository is itself agent-native. Install these skills to let your coding agent (Claude Code, Cursor, Codex, Windsurf) work with this catalog directly:

| Skill | What it does | Install |
|---|---|---|
| `find-agent-service` | Given a task, find the right agent-native service | `npx clawhub@latest install find-agent-service` |
| `evaluate-agent-native` | Evaluate whether a service meets the 5 criteria | `npx clawhub@latest install evaluate-agent-native` |
| `add-to-awesome-list` | Full contribution workflow: criteria → issue → PR | `npx clawhub@latest install add-to-awesome-list` |

Skills are published on [ClawHub](https://clawhub.ai) under [`@haoruilee`](https://clawhub.ai/haoruilee). Source files are in `.skills/` in this repo.

---

## Classification System

Every service in this repository is tagged with one of three labels:

| Label | Meaning |
|---|---|
| `agent-native` | Designed from inception for agents as first-class entities |
| `agent-adapted` | Originally human-facing, later extended with agent interfaces |
| `agent-builder` | For humans to build, orchestrate, and configure agents |

**This list only contains `agent-native` services.** See [Excluded / Boundary Cases](#excluded--boundary-cases) for examples of what does not qualify and why.

---

## Five Hard Criteria

A service must satisfy **all five** to be listed here:

1. **Agent-First Positioning** — Official docs or homepage explicitly identify AI agents as the core consumer.
2. **Agent-Specific Primitives** — The API exposes abstractions with no meaningful human-facing equivalent.
3. **Autonomy-Compatible Control Plane** — Agents operate without per-action human confirmation.
4. **Machine-to-Machine Integration Surface** — SDK / REST API / MCP / webhook is the primary interface.
5. **Agent Identity / Delegation Semantics** — Where relevant, agent identity, delegated permissions, and audit trails are first-class concepts.

For the full criteria and contribution instructions, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Categories

| # | Category | Services | Description |
|---|---|---|---|
| 1 | [Communication](#1-communication-services) | 2 | Give agents a communication identity on the internet |
| 2 | [Browser & Web Execution](#2-browser--web-execution-services) | 4 | Remote browser and web data extraction for agents |
| 3 | [Tool Access & Integration](#3-tool-access--integration-services) | 3 | Runtime tool discovery, auth, and execution |
| 4 | [Oversight & Approval](#4-oversight--approval-services) | 1 | Human-in-the-loop approval and escalation |
| 5 | [Commerce & Payments](#5-commerce--payment-services) | 4 | Agent-native wallets, identity, and transactions |
| 6 | [Agent Runtime & Infrastructure](#6-agent-runtime--infrastructure-services) | 4 | Execution, session isolation, secrets, and gateway |
| 7 | [Memory & State](#7-memory--state-services) | 2 | Persistent agent memory across sessions |
| 8 | [Search & Web Intelligence](#8-search--web-intelligence-services) | 2 | LLM-optimized web search and content retrieval |
| 9 | [Code Execution](#9-code-execution-services) | 1 | Secure sandboxes for AI-generated code |
| 10 | [Observability & Tracing](#10-observability--tracing-services) | 1 | Agent trajectory tracing and evaluation |
| 11 | [Durable Execution & Scheduling](#11-durable-execution--scheduling-services) | 3 | Fault-tolerant long-running agent workflows |
| 12 | [Meeting & Conversation](#12-meeting--conversation-services) | 1 | Agent presence in voice and video meetings |
| 13 | [Voice & Phone](#13-voice--phone-services) | 1 | Agent-controlled voice calls and phone infrastructure |
| 14 | [LLM Gateway & Routing](#14-llm-gateway--routing-services) | 1 | Per-agent budget, routing, caching, and observability for LLM calls |

---

## 1. Communication Services

> Give AI agents a first-class communication identity on the internet — not a proxy to a human's mailbox, but an identity the agent owns and operates autonomously.

→ **[Full category overview and criteria](services/communication/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [AgentMail](services/communication/agentmail.md) | Email for AI agents | Agent inbox · Threaded conversation · Webhook on inbound mail · Semantic search | ✅ |
| [Novu](services/communication/novu.md) | Notification infrastructure with Agent Toolkit | Workflow-as-tool · Cross-channel delivery · HITL notification flow | ✅ |

---

## 2. Browser & Web Execution Services

> Give AI agents a remote, managed browser runtime — so agents can navigate, interact with, and extract data from the web as an autonomous actor.

→ **[Full category overview and criteria](services/browser-and-web-execution/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [Browserbase](services/browser-and-web-execution/browserbase.md) | A web browser for AI agents & applications | Remote browser session · Stagehand NL actions · Session recording · Stealth mode | ✅ |
| [Firecrawl](services/browser-and-web-execution/firecrawl.md) | Turn any website into LLM-ready data | Intent-driven extraction · LLM-ready markdown · Schema-typed JSON output | ✅ |
| [Bright Data Agent Browser](services/browser-and-web-execution/bright-data-agent-browser.md) | Cloud browser for AI agents with built-in website unlocking | Built-in CAPTCHA/fingerprint unlocking · 150M+ proxy IPs · Parallel sessions | ✅ |
| [bb-browser](services/browser-and-web-execution/bb-browser.md) | Your browser is the API — 103 commands, 36 platforms, your real login state | Authenticated session delegation · Site commands · MCP built-in | ✅ |

---

## 3. Tool Access & Integration Services

> Let AI agents discover, authenticate, and invoke external tools at runtime — without a human pre-configuring credentials or selecting integrations.

→ **[Full category overview and criteria](services/tool-access-and-integration/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [Composio](services/tool-access-and-integration/composio.md) | The tool platform built for agents | Runtime tool discovery · Connect Link OAuth · Per-user credential scoping | ✅ |
| [Nango](services/tool-access-and-integration/nango.md) | OAuth and credential layer for AI agents | `getConnection()` · Automatic token refresh · 700+ API integrations | ✅ |
| [Toolhouse](services/tool-access-and-integration/toolhouse.md) | BaaS for AI agents — tools, memory, and execution | Agent endpoint · MCP tool registry · Built-in RAG · Cron scheduling | ✅ |

---

## 4. Oversight & Approval Services

> Give AI agents a structured, programmatic way to request human approval before executing high-stakes actions.

→ **[Full category overview and criteria](services/oversight-and-approval/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [HumanLayer](services/oversight-and-approval/humanlayer.md) | Human in the Loop for AI Agents | `@require_approval()` · Denial-feedback injection · Run/Call ID audit trail | ✅ |

---

## 5. Commerce & Payment Services

> Give AI agents a verified financial identity and the ability to transact in the real economy.

→ **[Full category overview and criteria](services/commerce-and-payments/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [Payman AI](services/commerce-and-payments/payman-ai.md) | Agentic AI that does the banking. Under your control. | Policy-gated transaction · Intent reasoning · Execution trace | ❌ |
| [Skyfire](services/commerce-and-payments/skyfire.md) | Identity and payments for autonomous AI agents | KYA identity token · Agent wallet · KYAPay open protocol | ❌ |
| [AgentsPay](services/commerce-and-payments/agentspay.md) | Crypto identity and embedded wallets for AI agents | W3C DID on Base L2 · USDC wallet · MCP-native API gateway | ✅ |
| [Nevermined](services/commerce-and-payments/nevermined.md) | The payment layer AI agents actually need | HTTP x402 protocol · Inline payment · Usage/outcome-based billing | ❌ |

---

## 6. Agent Runtime & Infrastructure Services

> Provide the secure deployment substrate, session isolation, secret management, identity, gateway, and observability required to run agents in production.

→ **[Full category overview and criteria](services/agent-runtime-and-infrastructure/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [Amazon Bedrock AgentCore](services/agent-runtime-and-infrastructure/amazon-bedrock-agentcore.md) | Purpose-built for deploying and scaling dynamic AI agents and tools | Agent runtime · Long-term memory · Identity tokens · Tool gateway · OTEL tracing | ❌ |
| [Infisical Agent Sentinel](services/agent-runtime-and-infrastructure/infisical-agent-sentinel.md) | Secrets and credential governance for AI agents | Dynamic secret generation · Token lifecycle daemon · Per-agent policy | ✅ |
| [Letta](services/agent-runtime-and-infrastructure/letta.md) | The fastest way to bring stateful agents to production | Stateful agent · Model-agnostic state · Agent templates · Self-editing memory | ✅ |
| [Aembit](services/agent-runtime-and-infrastructure/aembit.md) | Secretless workload identity and access management for AI agents | Agent workload identity · Blended identity · JIT credentials · Anomaly detection | ✅ |

---

## 7. Memory & State Services

> Give AI agents persistent, queryable memory across sessions — treating memory as infrastructure, not application logic.

→ **[Full category overview and criteria](services/memory-and-state/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [Mem0](services/memory-and-state/mem0.md) | The memory layer for your AI agents | Memory extraction · Conflict resolution (ADD/UPDATE/DELETE/NOOP) · Semantic retrieval · 90% token savings | ✅ |
| [Zep](services/memory-and-state/zep.md) | Agent memory powered by a temporal knowledge graph | Temporal knowledge graph · Automatic fact invalidation · Business data fusion · Sub-200ms retrieval | ✅ |

---

## 8. Search & Web Intelligence Services

> Give AI agents optimized, structured access to web information — returning LLM-ready content tuned for context windows, not raw HTML or human-readable SERPs.

→ **[Full category overview and criteria](services/search-and-web-intelligence/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [Tavily](services/search-and-web-intelligence/tavily.md) | Connect your agent to the web | Agent-optimized search · Multi-step research · Source attribution | ✅ |
| [Exa](services/search-and-web-intelligence/exa.md) | The search engine designed for AI | Neural/semantic search · `exa-code` for coding agents · Websets | ✅ |

---

## 9. Code Execution Services

> Give AI agents a secure, isolated runtime for executing generated code — without human-side sandbox setup and with output formatted for LLM consumption.

→ **[Full category overview and criteria](services/code-execution/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [E2B](services/code-execution/e2b.md) | Cloud for AI agents — secure sandboxes for AI-generated code | Ephemeral Linux VM · ~150ms cold start · Stateful execution context · Streaming output | ❌ |

---

## 10. Observability & Tracing Services

> Give teams structured visibility into agent execution — full trajectory tracing, evaluation datasets, and cost attribution.

→ **[Full category overview and criteria](services/observability-and-tracing/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [Langfuse](services/observability-and-tracing/langfuse.md) | Open-source LLM observability, tracing, and evaluation | Typed trace hierarchy · Dataset-based evaluation · Trajectory replay · OTEL-compatible | ❌ |

---

## 11. Durable Execution & Scheduling Services

> Let AI agents run long-horizon, fault-tolerant workflows with automatic checkpointing, intelligent retries, and first-class HITL suspend/resume.

→ **[Full category overview and criteria](services/durable-execution-and-scheduling/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [Trigger.dev](services/durable-execution-and-scheduling/trigger-dev.md) | Build and deploy fully-managed AI agents and workflows | No-timeout tasks · Step checkpointing · HITL waitForApproval · Streaming response | ❌ |
| [Inngest](services/durable-execution-and-scheduling/inngest.md) | Durable execution for AI agents in production | Durable step · Context-preserving retry · HITL suspend/resume · Low-latency interactive mode | ✅ |
| [Restate](services/durable-execution-and-scheduling/restate.md) | Durable execution for AI agents — any framework, any cloud | Durable AI loop · Compensation pattern · A2A exactly-once · Suspend-when-idle | ✅ |

---

## 12. Meeting & Conversation Services

> Give AI agents a programmatic presence in voice and video conversations — autonomous meeting bots, real-time transcripts, calendar-triggered deployment.

→ **[Full category overview and criteria](services/meeting-and-conversation/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [Recall.ai](services/meeting-and-conversation/recall-ai.md) | The meeting bot API for every platform | Meeting bot lifecycle · Real-time diarized transcript · Calendar-triggered deployment · 6 platforms | ❌ |

---

## 13. Voice & Phone Services

> Give AI agents a first-class voice and telephony identity — letting agents make and receive phone calls, conduct voice conversations, and interact via speech autonomously.

→ **[Full category overview and criteria](services/voice-and-phone/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [Vapi](services/voice-and-phone/vapi.md) | Build advanced voice AI agents | Voice assistant lifecycle · Tool-calling mid-call · Webhook per utterance · Voice simulation testing | ✅ |

---

## 14. LLM Gateway & Routing Services

> Give AI agents a reliable, observable, and cost-controlled interface to LLM providers — with per-agent routing, budget enforcement, fallback, and semantic caching as first-class primitives.

→ **[Full category overview and criteria](services/llm-gateway-and-routing/README.md)**

| Service | Tagline | Primitives | MCP |
|---|---|---|---|
| [Portkey](services/llm-gateway-and-routing/portkey.md) | The AI gateway built for production agents | Virtual key · Per-agent budget limit · Automatic fallback · Sticky session routing · Agent trace | ❌ |

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
