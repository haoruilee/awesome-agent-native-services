# Awesome Agent-Native Services [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of services that are **designed from the ground up for AI agents**, not adapted from human-facing products.

---

## What Makes a Service "Agent-Native"?

This list applies strict criteria. A service qualifies only if it meets **all five hard requirements**:

1. **Agent-First Positioning** — Official docs or homepage explicitly position AI agents as the core consumer, not a secondary use case.
2. **Agent-Specific Primitives** — The API surface exposes primitives that only make sense for agents (e.g., agent inboxes, approval gates, KYA identity, remote browser sessions).
3. **Autonomy-Compatible Control Plane** — The service allows agents to operate with minimal human intervention while providing agent-appropriate constraint mechanisms.
4. **Machine-to-Machine Integration Surface** — The primary interface is SDK/API/MCP/webhook, not a human dashboard or UI.
5. **Agent Identity / Delegation Semantics** — Where the service involves external actions, it distinguishes the agent's own identity, delegated user permissions, and audit trails.

**Bonus signals** (more = more agent-native):
- Dedicated agent identity model
- MCP or agent protocol support
- Per-agent state / memory / session management
- Specialized audit / trajectory / replay / approval artifacts

---

## Classification System

Each entry is tagged with one of three labels:

| Label | Meaning |
|---|---|
| `agent-native` | Designed from inception for agents as first-class entities |
| `agent-adapted` | Originally human-facing, later extended with agent interfaces |
| `agent-builder` | Tools for *humans* to build and orchestrate agents |

> **This list only includes `agent-native` services.** Agent-adapted and agent-builder products are explicitly excluded from the main catalog.

---

## Table of Contents

- [Communication Services](#communication-services)
- [Browser & Web Execution Services](#browser--web-execution-services)
- [Tool Access & Integration Services](#tool-access--integration-services)
- [Oversight & Approval Services](#oversight--approval-services)
- [Commerce & Payment Services](#commerce--payment-services)
- [Agent Runtime & Infrastructure Services](#agent-runtime--infrastructure-services)
- [Memory & State Services](#memory--state-services)
- [Search & Web Intelligence Services](#search--web-intelligence-services)
- [Code Execution Services](#code-execution-services)
- [Observability & Tracing Services](#observability--tracing-services)
- [Durable Execution & Scheduling Services](#durable-execution--scheduling-services)
- [Meeting & Conversation Services](#meeting--conversation-services)
- [Excluded / Boundary Cases](#excluded--boundary-cases)
- [Contributing](#contributing)

---

## Communication Services

> Services that give AI agents a **first-class communication identity** on the internet.

### [AgentMail](https://agentmail.to)
`agent-native`

**"Email for AI agents."**

AgentMail is an email inbox API built specifically for AI agents to **own** email identities. Agents can create inboxes in milliseconds, send, receive, and act on emails programmatically, with full thread management, real-time webhooks, and semantic search across conversations.

| Field | Detail |
|---|---|
| **Why agent-native** | Agents are the *owner* of inboxes, not a proxy for a human mailbox; the core abstraction is "agent as first-class internet entity" |
| **Primary primitive** | Agent inbox, threaded conversation, webhook on inbound mail |
| **Autonomy model** | Fully headless; no human mailbox required |
| **Identity / delegation** | Each inbox is agent-owned; custom domains supported |
| **Protocol surface** | REST API, Python SDK, TypeScript SDK, MCP server |
| **Human-in-the-loop** | Optional; agents operate fully autonomously by default |
| **Why Gmail API does not qualify** | Gmail was built for humans; AgentMail's core abstraction is agent ownership of inbox identity |

**Links:** [Website](https://agentmail.to) · [Docs](https://docs.agentmail.to) · [GitHub](https://github.com/agentmail-to)

---

## Browser & Web Execution Services

> Services that give AI agents a **remote browser runtime** to interact with the web as a first-class actor.

### [Browserbase](https://browserbase.com)
`agent-native`

**"A web browser for AI agents & applications."**

Browserbase provides managed, cloud-hosted headless browser infrastructure where agents run Playwright/Puppeteer/Selenium sessions in isolated, scalable environments. Designed so agents can navigate, click, extract, and fill forms without any human-side browser.

| Field | Detail |
|---|---|
| **Why agent-native** | Homepage explicitly positions agents as the primary actor; Stagehand SDK, MCP server, and agent integration guides are first-class products |
| **Primary primitive** | Remote browser session, natural-language web action (via Stagehand), session recording |
| **Autonomy model** | Agents spin up and tear down browser sessions programmatically; thousands in parallel |
| **Identity / delegation** | Per-session isolation; proxy and fingerprint configuration per agent |
| **Protocol surface** | REST API, Playwright/Puppeteer/Selenium integration, MCP server, Chrome DevTools Protocol |
| **Human-in-the-loop** | None required; optional session replay for debugging |
| **Why Selenium Grid does not qualify** | Selenium was built for human QA engineers; Browserbase's primitives (session isolation, stealth, agent SDK) are purpose-built for autonomous agents |

**Links:** [Website](https://browserbase.com) · [Docs](https://docs.browserbase.com) · [MCP](https://www.browserbase.com/mcp) · [GitHub](https://github.com/browserbase)

### [Firecrawl](https://firecrawl.dev)
`agent-native`

**"Turn any website into LLM-ready data."**

Firecrawl exposes an `/agent` endpoint where agents describe *what data they need* in natural language — no URLs required. The service autonomously searches, navigates, and extracts structured data at web scale, returning clean markdown or JSON directly consumable by LLMs.

| Field | Detail |
|---|---|
| **Why agent-native** | The `/agent` endpoint requires no human URL input; agents drive extraction through intent |
| **Primary primitive** | Autonomous web agent extraction, LLM-ready markdown output, schema-driven structured JSON |
| **Autonomy model** | Agent specifies intent; service autonomously plans and executes web navigation |
| **Identity / delegation** | API key scoped per integration |
| **Protocol surface** | REST API, Python SDK, Node.js SDK, MCP server |
| **Human-in-the-loop** | None required |
| **Why BeautifulSoup does not qualify** | BeautifulSoup is a human-operated parsing library; Firecrawl's agent endpoint replaces the human URL-gathering step entirely |

**Links:** [Website](https://firecrawl.dev) · [Docs](https://docs.firecrawl.dev) · [GitHub](https://github.com/mendableai/firecrawl)

---

## Tool Access & Integration Services

> Services that let AI agents **discover, authenticate, and call external tools** at runtime without human credential management.

### [Composio](https://composio.dev)
`agent-native`

**"The tool platform built for agents."**

Composio provides agents with runtime tool discovery, OAuth credential management, and execution across 250+ integrations. Agents get meta-tools that let them discover, authenticate, and execute the right tool at runtime — without a human pre-configuring credentials.

| Field | Detail |
|---|---|
| **Why agent-native** | Docs explicitly state "agent gets meta tools that discover, authenticate, and execute the right tools at runtime" |
| **Primary primitive** | Tool search, runtime authentication, execution, context management, per-user tool scoping |
| **Autonomy model** | Agents handle OAuth flows and credential refresh autonomously |
| **Identity / delegation** | Per-user, per-agent credential isolation; OAuth token lifecycle managed by Composio |
| **Protocol surface** | Python SDK, TypeScript SDK, MCP compatible, 10+ framework integrations (LangChain, CrewAI, etc.) |
| **Human-in-the-loop** | OAuth consent flows can be initiated by agent during conversation |
| **Why Zapier does not qualify** | Zapier is a human-facing workflow builder; Composio's primitives are designed for programmatic agent-time tool discovery |

**Links:** [Website](https://composio.dev) · [Docs](https://docs.composio.dev) · [GitHub](https://github.com/ComposioHQ/composio)

### [Nango](https://nango.dev)
`agent-native`

**"The OAuth and API credential layer for AI agents."**

Nango manages OAuth authentication for 700+ APIs so agents can access external services without handling credentials directly. Agents retrieve valid tokens at runtime; Nango handles token refresh, storage, and rotation invisibly.

| Field | Detail |
|---|---|
| **Why agent-native** | Provides first-class OpenAI Agents SDK integration; credential lifecycle is agent-driven at runtime |
| **Primary primitive** | Connect session, credential retrieval (`getConnection()`), automatic token refresh |
| **Autonomy model** | Agents fetch credentials on demand; no human re-authentication required |
| **Identity / delegation** | Per-connection credential isolation; each connection = one user's credentials for one API |
| **Protocol surface** | REST API, Node SDK, MCP-compatible patterns |
| **Human-in-the-loop** | Initial OAuth consent; subsequent calls are fully autonomous |
| **Why manual OAuth does not qualify** | Manual OAuth requires human browser interaction; Nango enables agent-side credential management |

**Links:** [Website](https://nango.dev) · [Docs](https://docs.nango.dev) · [GitHub](https://github.com/NangoHQ/nango)

### [Toolhouse](https://toolhouse.ai)
`agent-native`

**"BaaS for AI agents — tools, memory, and execution in one."**

Toolhouse is a Backend-as-a-Service where agents are defined as code and deployed as streaming API endpoints. Agents automatically connect to an MCP server providing access to RAG, memory, code execution, browser use, and custom tools.

| Field | Detail |
|---|---|
| **Why agent-native** | Agents are the deployment unit; `th deploy` publishes an agent as an API endpoint |
| **Primary primitive** | Agent endpoint, MCP tool access, built-in RAG, scheduled execution |
| **Autonomy model** | Globally distributed runtime; agents run headlessly with built-in observability |
| **Identity / delegation** | Public/private agent endpoints with optional authentication |
| **Protocol surface** | CLI (`th deploy`, `th run`), MCP server, streaming REST API |
| **Human-in-the-loop** | Optional; agents support cron-scheduled autonomous execution |
| **Why AWS Lambda does not qualify** | Lambda is a general compute primitive; Toolhouse's abstractions (agent identity, tool discovery, memory) are agent-specific |

**Links:** [Website](https://toolhouse.ai) · [Docs](https://docs.toolhouse.ai)

---

## Oversight & Approval Services

> Services that give AI agents a structured, programmatic way to **request human approval** before taking high-stakes actions.

### [HumanLayer](https://humanlayer.dev)
`agent-native`

**"Human in the Loop for AI Agents."**

HumanLayer provides an API/SDK that agents call before executing high-risk functions, routing approval requests to humans via Slack, email, SMS, and other channels. Denial feedback is automatically injected back into the agent's context window. Designed as an agent-initiated, asynchronous outer-loop pattern.

| Field | Detail |
|---|---|
| **Why agent-native** | Product is explicitly "human in the loop *for AI agents*"; the control flow inversion (agent initiates) is a fundamentally agent-specific primitive |
| **Primary primitive** | Approval gate, escalation channel, denial-with-feedback injection, agent webhook |
| **Autonomy model** | Agent operates fully autonomously except at annotated high-risk function boundaries |
| **Identity / delegation** | Run IDs and call IDs track agent-level and action-level provenance |
| **Protocol surface** | Python SDK, TypeScript SDK, REST API, webhooks, Slack/email/SMS channels |
| **Human-in-the-loop** | Core product feature — structured, auditable, asynchronous approval |
| **Why generic approval tools do not qualify** | Enterprise approval workflows (e.g., Jira, ServiceNow) are built for humans initiating requests; HumanLayer inverts the flow so agents are the initiating party |

**Links:** [Website](https://humanlayer.dev) · [Docs](https://humanlayer.dev/docs) · [GitHub](https://github.com/humanlayer/humanlayer)

---

## Commerce & Payment Services

> Services that give AI agents a **verified financial identity** and the ability to transact in the real economy.

### [Payman AI](https://paymanai.com)
`agent-native`

**"Agentic AI that does the banking. Under your control."**

Payman AI enables AI agents to execute real banking transactions — payments, transfers, and account analysis — through natural conversation. Policy-driven execution ensures every transaction is validated against operator-defined rules before execution, with full audit trails.

| Field | Detail |
|---|---|
| **Why agent-native** | Docs explicitly flag `client_credentials` flow as "for backend apps or AI agents"; agents are economic actors, not assistants |
| **Primary primitive** | Payment execution, policy-gated transaction, multi-step banking workflow, audit trail |
| **Autonomy model** | Agents execute transactions within operator-defined policy bounds; no human confirmation per transaction |
| **Identity / delegation** | Policy-driven spend controls; complete execution trace per transaction |
| **Protocol surface** | REST API, SDK, multi-channel (voice, mobile, web, SMS) |
| **Human-in-the-loop** | Policy-based guardrails replace per-transaction approval; auditable by default |
| **Why Stripe does not qualify** | Stripe was built for human developers charging human customers; Payman's primitives are specifically for agent-executed banking |

**Links:** [Website](https://paymanai.com) · [Docs](https://docs.paymanai.com)

### [Skyfire](https://skyfire.xyz)
`agent-native`

**"Identity and payments for autonomous AI agents."**

Skyfire is a payment network and identity infrastructure purpose-built for autonomous AI agents. It provides Know Your Agent (KYA) verified identities, programmable payment tokens, per-agent spending controls, and a standardized KYAPay protocol so agents can transact with any online service without human intermediation.

| Field | Detail |
|---|---|
| **Why agent-native** | Homepage statement: "trusted network for payments at the speed of AI" and "create a verified identity for your AI agents" |
| **Primary primitive** | Agent wallet, KYA identity token, programmable spend limit, KYAPay protocol (open standard) |
| **Autonomy model** | Agents sign up, authenticate, and pay for services with zero human intervention |
| **Identity / delegation** | Immutable behavioral records per agent; service providers get verified agent identity + fraud signals |
| **Protocol surface** | REST API, OAuth2/OIDC-compatible, open KYAPay protocol |
| **Human-in-the-loop** | Operator-defined budget limits; individual transactions are autonomous |
| **Why PayPal does not qualify** | PayPal was built for humans; Skyfire's KYA model, agent wallets, and KYAPay protocol have no human-facing equivalent |

**Links:** [Website](https://skyfire.xyz) · [Product](https://skyfire.xyz/product) · [KYAPay Protocol](https://www.businesswire.com/news/home/20250626772489/en/Skyfire-Launches-Open-KYAPay-Protocol-With-Agent-Checkout)

### [AgentsPay](https://agentspay.dev)
`agent-native`

**"Crypto identity and embedded wallets for AI agents."**

AgentsPay issues W3C Decentralized Identifiers (DIDs) to agents on Base L2, embeds USDC wallets with operator-set spending limits, and provides an MCP-native API gateway. Agents can discover and pay for services independently, bypassing the common failure mode where agents halt when API keys are required.

| Field | Detail |
|---|---|
| **Why agent-native** | Agent DID issuance and programmable wallets are built from the ground up for non-human actors |
| **Primary primitive** | W3C DID on Base L2, embedded USDC wallet, MCP-native API gateway |
| **Autonomy model** | Agents discover and pay for services without human credential injection |
| **Identity / delegation** | On-chain agent DID; operator-set spending limits |
| **Protocol surface** | MCP-native API gateway, REST API |
| **Human-in-the-loop** | Operator-configured spending ceilings |
| **Why standard crypto wallets do not qualify** | Standard wallets require human key management; AgentsPay embeds wallets with agent-appropriate spend controls |

**Links:** [Website](https://agentspay.dev)

### [Nevermined](https://nevermined.io)
`agent-native`

**"The payment layer AI agents actually need."**

Nevermined's x402 Facilitator standardizes payments at the HTTP layer using the x402 protocol. AI agents can pay for API access, data, or services using fiat, crypto, stablecoins, or prepaid credits through a single integration, with usage-based, outcome-based, and dynamic pricing models.

| Field | Detail |
|---|---|
| **Why agent-native** | Payments are embedded in the HTTP protocol itself — agent makes a request, payment is handled transparently |
| **Primary primitive** | x402 HTTP payment protocol, prepaid credits, usage-based billing per agent call |
| **Autonomy model** | Agents pay for services within the API call lifecycle; no human checkout flow |
| **Identity / delegation** | Per-agent payment accounts; operator-defined budgets |
| **Protocol surface** | HTTP x402 protocol, REST API |
| **Human-in-the-loop** | Budget limits; individual payments are fully autonomous |
| **Why Stripe Checkout does not qualify** | Stripe Checkout requires a human browser session; x402 embeds payment in the HTTP request itself |

**Links:** [Website](https://nevermined.io) · [Blog](https://nevermined.ai/blog/the-payment-layer-ai-agents-actually-need-introducing-the-nevermined-x402-facilitator)

---

## Agent Runtime & Infrastructure Services

> Services that provide **the deployment substrate, session isolation, identity, and observability** for running agents in production.

### [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
`agent-native`

**"Purpose-built for deploying and scaling dynamic AI agents and tools."**

Amazon Bedrock AgentCore is a modular agent runtime suite covering Runtime (execution), Memory (short-term and long-term), Identity (verified agent identity), Gateway (tool access routing), and Observability (OpenTelemetry-based tracing). Each module solves a problem specific to running agents at scale.

| Field | Detail |
|---|---|
| **Why agent-native** | AWS explicitly built AgentCore as a separate, agent-specific product suite distinct from Bedrock's human-facing features |
| **Primary primitive** | Agent runtime, session isolation, long-term memory extraction, identity tokens, tool gateway, OTEL traces |
| **Autonomy model** | Fully managed execution with per-agent session isolation; no human-in-the-loop required by default |
| **Identity / delegation** | Built-in AgentCore Identity with verified agent tokens and audit-capable CloudWatch traces |
| **Protocol surface** | AWS SDK, REST API, OpenTelemetry, CloudWatch integration |
| **Human-in-the-loop** | Optional; observability layer captures all agent actions |
| **Why standard AWS Lambda does not qualify** | Lambda is a general compute primitive; AgentCore's memory, identity, and gateway modules are agent-specific abstractions |

**Links:** [AWS Page](https://aws.amazon.com/bedrock/agentcore/) · [Docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/)

### [Infisical Agent Sentinel](https://infisical.com)
`agent-native`

**"Secrets and credential governance for AI agents."**

Infisical Agent Sentinel governs how AI agents access tools and external systems, centralizing authentication and policy enforcement. The agent daemon manages token lifecycle, automatic renewal, and secret delivery without credentials ever passing through agent code directly.

| Field | Detail |
|---|---|
| **Why agent-native** | Agent Sentinel is a dedicated product for AI agent credential governance, distinct from Infisical's developer-facing secret manager |
| **Primary primitive** | Token lifecycle management, templated secret delivery, per-agent policy enforcement, dynamic credential generation |
| **Autonomy model** | Agent daemon renews tokens automatically; agents access secrets at runtime without human rotation |
| **Identity / delegation** | Just-in-time credential generation; time-bounded, automatically expiring secrets |
| **Protocol surface** | Daemon sidecar, REST API, Go template secret rendering |
| **Human-in-the-loop** | Policy-defined access rules; agent runtime is autonomous |
| **Why plain env vars do not qualify** | Static secrets require human rotation; Infisical's dynamic credentials are purpose-built for non-human runtime actors |

**Links:** [Website](https://infisical.com) · [Agent Docs](https://infisical.com/docs/infisical-agent/overview)

---

## Memory & State Services

> Services that give AI agents **persistent, queryable memory** across sessions — treating memory as infrastructure, not application logic.

### [Mem0](https://mem0.ai)
`agent-native`

**"The memory layer for your AI agents."**

Mem0 provides a self-improving, adaptive memory system for LLM-powered agents. It extracts salient facts from conversations, resolves conflicts with existing memories, and retrieves relevant context at query time — reducing token costs by 90% versus full context injection while improving accuracy by 26%.

| Field | Detail |
|---|---|
| **Why agent-native** | Memory is positioned as agent infrastructure, not a chat feature; agents call the memory API as an external service |
| **Primary primitive** | Memory extraction, deduplication, semantic retrieval, episodic/semantic/procedural memory types |
| **Autonomy model** | Memory updated and retrieved autonomously during agent execution |
| **Identity / delegation** | Per-user, per-agent memory namespacing; graph-based relational memory available |
| **Protocol surface** | Python SDK, REST API, MCP server |
| **Human-in-the-loop** | None required; memory management is fully automated |
| **Why a vector database does not qualify** | A vector DB is a storage primitive; Mem0 adds agent-specific extraction, deduplication, and lifecycle management |

**Links:** [Website](https://mem0.ai) · [Docs](https://docs.mem0.ai) · [GitHub](https://github.com/mem0ai/mem0)

---

## Search & Web Intelligence Services

> Services that give AI agents **optimized, structured access** to web information — returning AI-ready content rather than human-readable SERPs.

### [Tavily](https://tavily.com)
`agent-native`

**"Connect your agent to the web."**

Tavily is a web intelligence API built specifically for AI agents and RAG pipelines. Unlike traditional search APIs, it returns AI-ready ranked sources with content snippets, not raw SERP HTML. It provides Search, Extract, Crawl, Map, and Research endpoints, each returning content structured for direct LLM consumption.

| Field | Detail |
|---|---|
| **Why agent-native** | Explicitly built for AI agents and RAG; output format is optimized for LLM consumption, not human reading |
| **Primary primitive** | Agent-optimized search results, content extraction, multi-step research with source attribution |
| **Autonomy model** | Agents call search and receive structured, LLM-ready data without preprocessing |
| **Identity / delegation** | API key authentication; rate limits by tier |
| **Protocol surface** | REST API, Python SDK, LangChain/LlamaIndex/CrewAI native integrations, MCP |
| **Human-in-the-loop** | None required |
| **Why Google Search API does not qualify** | Google's API returns human-formatted SERP data; Tavily returns ranked, pre-processed content tuned for LLM context windows |

**Links:** [Website](https://tavily.com) · [Docs](https://docs.tavily.com) · [GitHub](https://github.com/tavily-ai/tavily-python)

### [Exa](https://exa.ai)
`agent-native`

**"The search engine designed for AI."**

Exa uses neural/embedding-based search to retrieve semantically relevant web content. It returns clean, parsed content ready for LLM processing — 20x more accurate than keyword search for complex entity queries. The `exa-code` product specifically targets coding agents with token-efficient code and documentation retrieval.

| Field | Detail |
|---|---|
| **Why agent-native** | Designed explicitly for AI consumption; the output format, ranking model, and content parsing all optimize for LLM context |
| **Primary primitive** | Semantic search, clean content extraction, agent-specific corpus (`exa-code`), Websets |
| **Autonomy model** | Agents call the API and receive LLM-ready content with no postprocessing |
| **Identity / delegation** | API key per integration |
| **Protocol surface** | REST API, Python SDK, native LangChain/CrewAI/LlamaIndex/Mastra integrations |
| **Human-in-the-loop** | None required |
| **Why DuckDuckGo API does not qualify** | DuckDuckGo returns HTML/SERP for human consumption; Exa's embeddings and content parsing are purpose-built for AI consumption |

**Links:** [Website](https://exa.ai) · [Docs](https://docs.exa.ai) · [GitHub](https://github.com/exa-labs/exa-py)

---

## Code Execution Services

> Services that give AI agents a **secure, isolated runtime** to execute generated code without human-side sandbox management.

### [E2B](https://e2b.dev)
`agent-native`

**"Cloud for AI agents — secure sandboxes for AI-generated code."**

E2B provides isolated Linux cloud sandboxes that start in ~150ms, designed specifically for agents to run AI-generated code. Each agent or user session gets its own sandbox with filesystem access, internet connectivity, and stateful execution contexts. Used by companies running AI data analysis, autonomous coding, and agent playgrounds.

| Field | Detail |
|---|---|
| **Why agent-native** | E2B's GitHub org is literally "Cloud for AI Agents"; the sandbox model (ephemeral, per-session, agent-controlled) is fundamentally agent-specific |
| **Primary primitive** | Ephemeral cloud VM, stateful code context, file upload/download, chart/stdout streaming |
| **Autonomy model** | Agents spin up sandboxes, execute code, and tear them down programmatically |
| **Identity / delegation** | Per-session sandbox isolation; API key scoped per integration |
| **Protocol surface** | Python SDK, TypeScript SDK, REST API, compatible with LangChain/AutoGen/CrewAI |
| **Human-in-the-loop** | None required |
| **Why AWS Lambda does not qualify** | Lambda is a general serverless compute primitive; E2B's sandbox semantics (interactive stateful execution, streaming output, agent-controlled lifecycle) are agent-specific |

**Links:** [Website](https://e2b.dev) · [Docs](https://e2b.dev/docs) · [GitHub](https://github.com/e2b-dev/e2b)

---

## Observability & Tracing Services

> Services that give teams **structured visibility into agent execution** — traces, trajectories, evaluations, and cost attribution.

### [Langfuse](https://langfuse.com)
`agent-native`

**"Open-source LLM observability, tracing, and evaluation for AI agents."**

Langfuse provides structured tracing for multi-step agent workflows — capturing tool calls, retriever steps, guardrail checks, latency, cost, and error rates in a typed observation hierarchy. Production traces can be converted to evaluation datasets, and OpenTelemetry integration allows existing monitoring stacks to receive agent telemetry.

| Field | Detail |
|---|---|
| **Why agent-native** | Agent trajectory tracing (nested tool calls, multi-step decision chains) is the core product, not a bolt-on |
| **Primary primitive** | Typed trace hierarchy (span → tool call → LLM call), dataset-based evaluation, trajectory replay |
| **Autonomy model** | Passive observation of autonomous agent execution; no intervention required |
| **Identity / delegation** | Per-agent run IDs; trace metadata supports multi-agent attribution |
| **Protocol surface** | OpenTelemetry SDK, Python SDK, TypeScript SDK, native integrations with OpenAI Agents, Claude SDK, LangChain |
| **Human-in-the-loop** | Tracing is passive; humans review captured trajectories in the UI |
| **Why CloudWatch Logs does not qualify** | CloudWatch captures generic log streams; Langfuse understands agent-specific semantic structure (tool calls, LLM calls, context injections) |

**Links:** [Website](https://langfuse.com) · [Docs](https://langfuse.com/docs) · [GitHub](https://github.com/langfuse/langfuse)

---

## Durable Execution & Scheduling Services

> Services that let AI agents run **long-horizon, fault-tolerant workflows** with automatic checkpointing, retries, and human-in-the-loop suspend/resume.

### [Trigger.dev](https://trigger.dev)
`agent-native`

**"Build and deploy fully-managed AI agents and workflows."**

Trigger.dev provides a durable execution runtime for long-running agent tasks with no timeouts, type-safe TypeScript agents, human-in-the-loop pause/resume primitives, full observability, and streaming responses. Agents can run multi-step workflows that survive infrastructure failures by checkpointing state between steps.

| Field | Detail |
|---|---|
| **Why agent-native** | AI agents are the primary product use case; the human-in-the-loop pause/resume and long-running task model are agent-specific primitives |
| **Primary primitive** | Durable task, suspend/resume for HITL, type-safe agent definition, streaming frontend response |
| **Autonomy model** | Agents run without timeouts; checkpointing handles partial failures automatically |
| **Identity / delegation** | Per-run task IDs; full execution trace |
| **Protocol surface** | TypeScript SDK, REST API, cron scheduling |
| **Human-in-the-loop** | Native first-class suspend/resume for approval workflows |
| **Why plain cron does not qualify** | Cron has no concept of agent state, LLM checkpointing, or HITL; Trigger.dev's primitives are purpose-built for probabilistic agent execution |

**Links:** [Website](https://trigger.dev) · [Docs](https://trigger.dev/docs) · [GitHub](https://github.com/triggerdotdev/trigger.dev)

### [Inngest](https://inngest.com)
`agent-native`

**"Durable execution for AI agents in production."**

Inngest provides a durable execution platform with low-latency patterns for interactive, real-time AI agents. It checkpoints state between tool calls, handles external API failures through automatic retries, and maps human-in-the-loop patterns to suspend/resume primitives. Designed to address the compounding failure problem in multi-step agent workflows.

| Field | Detail |
|---|---|
| **Why agent-native** | 2025 blog explicitly frames durable execution as "the key to harnessing AI agents in production"; primitives designed around agent-specific failure modes |
| **Primary primitive** | Durable step, checkpoint between tool calls, HITL suspend/resume, retry with agent context preservation |
| **Autonomy model** | Agents resume automatically from last checkpoint after failure |
| **Identity / delegation** | Per-run event IDs; full execution history |
| **Protocol surface** | TypeScript SDK, Python SDK, REST API |
| **Human-in-the-loop** | Suspend/resume primitive maps naturally to agent approval gates |
| **Why AWS SQS does not qualify** | SQS is a message queue; Inngest understands agent-specific step semantics and preserves reasoning context across retries |

**Links:** [Website](https://inngest.com) · [Docs](https://www.inngest.com/docs) · [GitHub](https://github.com/inngest/inngest)

---

## Meeting & Conversation Services

> Services that give AI agents a **programmatic presence** in video meetings and voice conversations.

### [Recall.ai](https://recall.ai)
`agent-native`

**"The meeting bot API for every platform."**

Recall.ai provides a unified API for deploying bots into Zoom, Google Meet, Microsoft Teams, Webex, and Slack Huddles. Agents receive real-time speaker-diarized transcripts, audio/video streams, and meeting metadata within 10 seconds — with no requirement for a human to be present or install client software.

| Field | Detail |
|---|---|
| **Why agent-native** | The bot *is* the agent's presence in the meeting; the API is designed for programmatic bot lifecycle management, not human meeting participation |
| **Primary primitive** | Meeting bot lifecycle, real-time diarized transcript, audio/video stream, calendar event trigger |
| **Autonomy model** | Bots join, record, and process meetings entirely without human intervention |
| **Identity / delegation** | Per-bot session; calendar V2 provides per-event bot configuration |
| **Protocol surface** | REST API, webhook on transcript events, calendar integration API |
| **Human-in-the-loop** | None required; optional human review of transcripts post-meeting |
| **Why recording a Zoom call yourself does not qualify** | A human recording is a human-in-the-loop by definition; Recall.ai's bot is the agent's autonomous meeting presence |

**Links:** [Website](https://recall.ai) · [Docs](https://docs.recall.ai) · [Meeting Bot API](https://www.recall.ai/product/meeting-bot-api)

---

## Excluded / Boundary Cases

Understanding what does **not** qualify is as important as what does.

### `agent-builder` — Excluded by Design

These products help humans build agent workflows but are not consumed by agents as services:

| Product | Why Excluded |
|---|---|
| [Dify](https://dify.ai) | Visual workflow builder, teams platform, RAG studio — built for human developers |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | Agent orchestration framework for developers, not an agent-consumed service |
| [n8n](https://n8n.io) | No-code workflow automation for human operators |
| [Flowise](https://flowiseai.com) | Drag-and-drop LLM flow builder for human developers |
| [AutoGen Studio](https://microsoft.github.io/autogen/) | Visual multi-agent conversation builder for human developers |

### `agent-adapted` — Extended from Human-Facing Products

These products were not built for agents originally but have added agent interfaces. They may be useful to agent developers but do not belong in this list:

| Product | Original Purpose | Agent Extension |
|---|---|---|
| [Resend](https://resend.com) | Developer email infrastructure for humans | Resend MCP Server, AI docs |
| [SendGrid](https://sendgrid.com) | Bulk email platform for marketing teams | Programmatic API usable by agents |
| [Stripe](https://stripe.com) | Human checkout and billing | Stripe Agent Toolkit, MCP server |
| [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/) | Enterprise identity for humans | Extended to issue agent identity tokens |
| [CyberArk AI Agent Security](https://cyberark.com) | Enterprise PAM for humans | Adapters for AI agent credential security |
| [Twilio](https://twilio.com) | Human SMS/voice communications | Agent-usable APIs |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full submission checklist.

**Quick criteria for a new entry:**

1. Official homepage or docs explicitly name AI agents as the primary consumer.
2. The service exposes at least one primitive that has no meaningful human-facing equivalent.
3. The service has a machine-to-machine API/SDK/MCP/webhook as its primary interface.
4. The service is production-ready (not just a demo or prototype).

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
