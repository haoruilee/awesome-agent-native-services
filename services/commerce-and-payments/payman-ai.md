# Payman AI

> **"Agentic AI that does the banking. Under your control."**

| | |
|---|---|
| **Website** | https://paymanai.com |
| **Docs** | https://docs.paymanai.com |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Compliance** | SOC 2 Certified |
| **Backers** | Visa, Coinbase, Circle |

---

## Official Website

https://paymanai.com

---

## Official Repo

https://github.com/PaymanAI/payman-node — Node.js / TypeScript SDK

https://github.com/PaymanAI/payman-python — Python SDK

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ✅ Official documentation MCP skill published at [`@PaymanAI/payman-doc-mcp-server`](https://glama.ai/mcp/servers/%40PaymanAI/payman-doc-mcp-server)

The official skill provides documentation access and code examples. For the payment API skill, a community implementation is available:

```bash
# Install official documentation skill via Smithery
npx @smithery/cli install @PaymanAI/payman-doc-mcp-server

# Community payment API skill
npx skills add hrishi0102/payman_mcp
```

| Skill | What It Teaches the Agent |
|---|---|
| `payman-doc-mcp-server` *(official)* | Access Payman documentation, code examples, and SDK help |
| `payman_mcp` *(community)* | Execute payments, manage payees, check balances via natural language |

**Compatibility:** Claude Desktop, Cursor, and all [AgentSkills](https://agentskills.io/)-compatible tools.

---

## MCP

**Status:** ✅ Available

Payman provides an official documentation MCP server (`@PaymanAI/payman-doc-mcp-server`) and a community payment API MCP server that enables AI assistants to perform payment operations through natural language.

| Detail | Value |
|---|---|
| **Official Doc MCP** | `@PaymanAI/payman-doc-mcp-server` (via Smithery) |
| **Payment API MCP** | https://github.com/hrishi0102/payman_mcp |
| **Transport** | stdio / SSE |
| **Compatible Clients** | Claude Desktop, Cursor, any MCP-compatible client |

---

## What It Does

Payman AI enables AI agents to **execute real banking transactions** — payments, transfers, and multi-step account operations — through natural conversation or API calls. Unlike a chatbot that describes how to make a payment, Payman's agents actually move money. Every transaction is validated against operator-defined policies before execution, with full compliance traces.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Agentic AI that does the banking. Under your control."*; docs explicitly flag `client_credentials` flow as *"for backend apps or AI agents"* |
| **Agent-specific primitive** | Policy-gated transaction execution; multi-step banking workflow reasoning; complete execution trace per transaction |
| **Autonomy-compatible control plane** | Agents execute within operator-defined policy bounds without per-transaction human confirmation |
| **M2M integration surface** | REST API, SDK, multi-channel deployment (voice, mobile, web, SMS) |
| **Identity / delegation** | Policy enforcement per agent; full execution trace captures agent reasoning, policy checks, and authorization flows |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Policy-Gated Transaction** | Every payment validated against operator rules before execution |
| **Intent Reasoning** | Agent understands `"move enough to cover rent"` — not just literal amounts |
| **Multi-Step Workflow** | Agent executes complex banking sequences autonomously (analyze → plan → execute → confirm) |
| **Execution Trace** | Tamper-evident record: request → reasoning → policy check → authorization → timestamp |
| **Multi-Channel Integration** | Same agent logic deployed across voice, mobile, web, SMS |
| **Audit Log** | Explainable, auditable record of every agent-executed transaction |

---

## Autonomy Model

```
User/operator defines policy (e.g., "allow transfers up to $500 for bill payment")
    ↓
Agent receives natural language instruction ("pay the electric bill")
    ↓
Agent reasons about intent and formulates transaction plan
    ↓
Payman validates plan against operator policy
    ↓
If valid: executes transaction → logs trace
If invalid: returns policy violation → agent reasons about alternative
```

No human confirms individual transactions. Policy is the control mechanism, not per-transaction approval.

---

## Identity and Delegation Model

- Agents operate under operator-defined policies — the operator is the delegating authority
- Full execution trace per transaction: which agent, which instruction, which policy was checked, which human (if any) authorized the policy
- SOC 2 certification covers the audit and compliance layer
- Transaction attribution supports regulatory reporting

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Full transaction lifecycle management |
| SDK | Native integration for backend agent deployments |
| Paygent Studio | Operator interface for policy configuration and audit review |
| Multi-channel | Voice (phone), mobile app, web, SMS — same agent logic across channels |
| `client_credentials` OAuth | M2M auth flow explicitly designed for agents and backends |

---

## Human-in-the-Loop Support

Policy-based rather than per-transaction. Operators define rules upfront; individual transactions execute autonomously within those rules. Edge cases outside policy bounds return to the agent for reasoning (not necessarily to a human). Full audit trails support post-hoc human review.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Stripe** | Built for human developers charging human customers; Stripe Checkout requires a human browser session |
| **PayPal** | Human-facing wallet and checkout; no policy-gated agent transaction model |
| **Plaid** | Bank data access for human apps; read-focused, not write/execution-focused for agents |
| **ACH API** | Low-level payment rail with no agent reasoning, policy enforcement, or audit trail |

---

## Use Cases

- **Banking virtual assistants** — agent executes real transfers, bill payments, and account analysis via voice or chat
- **Expense management** — agent autonomously pays pre-approved vendor invoices within policy limits
- **Payroll agents** — agent executes salary disbursements according to defined rules
- **Subscription management** — agent handles recurring payment setup, changes, and cancellation
