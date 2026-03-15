# Contributing to Awesome Agent-Native Services

Thank you for your interest in contributing! This list applies strict criteria to ensure every entry genuinely represents a service **designed from inception for AI agents**, not adapted from a human-facing product.

Please read this guide in full before submitting a pull request.

---

## The Five Hard Requirements

A service must satisfy **all five** of the following criteria to be eligible for the main list.

### 1. Agent-First Positioning

The official website or documentation must explicitly identify AI agents as the **primary consumer**, not a secondary use case or marketing footnote.

**Pass examples:**
- "Email for AI agents" (AgentMail)
- "A web browser for AI agents & applications" (Browserbase)
- "Human in the Loop for AI Agents" (HumanLayer)

**Fail examples:**
- "Powerful automation platform — now with AI agent support"
- "Build apps, workflows, and AI agents" (positions agents as one of many outputs)

### 2. Agent-Specific Primitives

The API must expose **primitives that only make sense for agents**. If a human developer could use the exact same primitives without modification, the service likely does not qualify.

**Pass examples:**
- Agent inbox with webhook-on-inbound-message
- Approval gate with denial-feedback-to-context-window injection
- Know Your Agent (KYA) identity token
- Remote browser session controlled via natural language

**Fail examples:**
- A standard REST CRUD API that happens to be callable by an agent
- A webhook that any server can receive

### 3. Autonomy-Compatible Control Plane

The service must allow agents to operate **without per-action human confirmation**, while providing agent-appropriate constraint mechanisms (spending limits, policy gates, session isolation, etc.).

### 4. Machine-to-Machine Integration Surface

The **primary interface** must be an SDK, REST API, MCP server, or webhook — not a human-facing UI or dashboard. A management UI is acceptable as a secondary surface.

### 5. Agent Identity / Delegation Semantics

If the service involves external actions (payments, email sending, tool execution), it must distinguish:
- The agent's own identity
- Permissions delegated by the operator/user
- An audit trail attributable to the agent

---

## Bonus Signals (Not Required)

The following signals strengthen an entry but are not individually mandatory:

- Dedicated agent identity model (agent gets its own credential, not reused from a human)
- MCP (Model Context Protocol) or agent protocol support
- Per-agent state / memory / session (not just shared state)
- Specialized audit / trajectory / replay / approval artifacts

---

## Explicit Exclusions

The following categories of products are **not eligible**, regardless of their "AI agent" marketing:

| Category | Reason |
|---|---|
| **Agent builders** | Products where humans configure, orchestrate, or visually assemble agent workflows (e.g., Dify, n8n, Flowise, AutoGen Studio, LangGraph) |
| **RAG studios** | Products that help humans build retrieval pipelines (e.g., LlamaIndex Cloud, Cohere Compass) |
| **Chat workspaces** | Products designed for humans to interact with AI models (e.g., ChatGPT Teams, Claude.ai, Notion AI) |
| **No-code AI platforms** | Products targeting non-technical users for building AI applications |
| **Human-adapted services** | Products originally built for humans that have added an agent interface layer (see `agent-adapted` tag in the README) |

---

## Submission Checklist

Before opening a pull request, confirm all of the following:

- [ ] The service has a public website or documentation page you can link to.
- [ ] The homepage or official docs explicitly name AI agents as the primary consumer.
- [ ] The service exposes at least one primitive with no meaningful human-facing equivalent.
- [ ] The primary interface is an API, SDK, MCP server, or webhook — not exclusively a UI.
- [ ] The service is production-ready (not a demo, proof-of-concept, or invite-only alpha with no public documentation).
- [ ] The entry follows the standard format (see below).
- [ ] You have added the entry to the correct category, or proposed a new category with justification.
- [ ] You have verified the links are live and accurate.

---

## Entry Format

Each entry must follow this format exactly:

```markdown
### [Service Name](https://service-homepage.com)
`agent-native`

**"Official tagline from the homepage."**

One to three sentences describing what the service does and why it is agent-native.

| Field | Detail |
|---|---|
| **Why agent-native** | Specific evidence from the homepage/docs |
| **Primary primitive** | The agent-specific abstraction(s) this service provides |
| **Autonomy model** | How agents operate without per-action human intervention |
| **Identity / delegation** | How agent identity and delegated permissions are modeled |
| **Protocol surface** | SDK, REST API, MCP, webhook, etc. |
| **Human-in-the-loop** | Whether and how human approval is integrated |
| **Why [generic alternative] does not qualify** | Contrast with the obvious non-agent alternative |

**Links:** [Website](https://...) · [Docs](https://...) · [GitHub](https://...) (include only applicable links)
```

---

## Category Guidelines

Use the existing categories where possible:

| Category | What belongs here |
|---|---|
| Communication Services | Agent email, messaging, or notification identity |
| Browser & Web Execution Services | Remote browser or web extraction for agents |
| Tool Access & Integration Services | Agent-runtime tool discovery, auth, and execution |
| Oversight & Approval Services | Human-in-the-loop approval and escalation |
| Commerce & Payment Services | Agent-native payments, wallets, and identity |
| Agent Runtime & Infrastructure Services | Execution, session isolation, secrets, gateway |
| Memory & State Services | Persistent agent memory and session state |
| Search & Web Intelligence Services | Agent-optimized search and content retrieval |
| Code Execution Services | Sandboxed code execution for agent-generated code |
| Observability & Tracing Services | Agent trajectory tracing and evaluation |
| Durable Execution & Scheduling Services | Fault-tolerant long-running agent workflows |
| Meeting & Conversation Services | Agent presence in voice/video/meetings |

To propose a new category, open an issue describing the category, why existing categories don't fit, and provide at least two qualifying services for it.

---

## What to Do If You're Not Sure

If you believe a service is agent-native but are uncertain whether it meets the criteria, open an **issue** (not a PR) with:

1. The service name and homepage URL.
2. A quote from the official docs or homepage positioning it as agent-first.
3. A description of the agent-specific primitive it provides.
4. Your assessment of the five criteria above.

Maintainers will review and respond before you invest time in writing a full PR.

---

## Code of Conduct

- Be respectful of other contributors and maintainers.
- Do not submit entries for services you have a financial interest in without disclosing the relationship.
- Do not submit entries for services that are vaporware, shut down, or have no public documentation.

---

## License

By contributing, you agree that your contributions will be licensed under the [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) license.
