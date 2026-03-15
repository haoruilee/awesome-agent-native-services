# HumanLayer

> **"Human in the Loop for AI Agents."**

| | |
|---|---|
| **Website** | https://humanlayer.dev |
| **Docs** | https://humanlayer.dev/docs |
| **GitHub** | https://github.com/humanlayer/humanlayer |
| **Classification** | `agent-native` |
| **Category** | [Oversight & Approval Services](README.md) |

---

## Official Website

https://humanlayer.dev

---

## Official Repo

https://github.com/humanlayer/humanlayer

---

## Skills

| Skill | Description |
|---|---|
| **Require Approval** | Gate any function call on asynchronous human approval with `@require_approval()` |
| **Denial Feedback Injection** | Automatically inject a human's denial explanation into the agent's context window |
| **Escalation Routing** | Route approval requests to Slack, email, Discord, Teams, SMS, or RCS by urgency |
| **Agent Webhook** | Launch an agent run in response to an inbound human message |
| **Approval Lifecycle Management** | Create, poll, and resolve approval requests via REST API |
| **Run / Call ID Audit** | Tag every approval event with a run ID and call ID for fine-grained audit |

---

## MCP

**Status:** ⚠️ Not yet available as standalone MCP server

HumanLayer does not currently publish a dedicated MCP server. However, the Python and TypeScript SDKs integrate natively with MCP-based agent frameworks (OpenAI Agents SDK, LangChain, CrewAI) so approval gates work in any MCP-orchestrated agent loop.

| Detail | Value |
|---|---|
| **SDK Docs** | https://humanlayer.dev/docs |
| **GitHub** | https://github.com/humanlayer/humanlayer |
| **Framework Support** | LangChain, CrewAI, OpenAI, Claude, ControlFlow, Vercel AI SDK, Mastra |

---

## What It Does

HumanLayer is an API and SDK that lets AI agents request human approval before executing high-risk functions. The agent annotates specific functions with `@require_approval()`; when called, HumanLayer pauses execution, routes an approval request to a human via Slack, email, SMS, or other channels, and resumes the agent with the human's decision injected into its context window.

The control flow is inverted from all traditional approval workflows: the **agent initiates**, the **human responds**, and the response feeds directly back into machine reasoning.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Product headline: *"Human in the Loop for AI Agents"*; the entire product design assumes an agent is the initiating party |
| **Agent-specific primitive** | Approval gate on function calls; denial-with-feedback injection into context window; agent webhooks for launching agents from human messages |
| **Autonomy-compatible control plane** | Agent runs fully autonomously except at annotated boundaries; no per-step human supervision |
| **M2M integration surface** | Python SDK, TypeScript SDK, REST API, webhooks; Slack/email/SMS are delivery channels, not the primary interface |
| **Identity / delegation** | Run IDs and Call IDs enable per-agent, per-action attribution in the audit trail |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`@require_approval()`** | Function decorator/wrapper that gates execution on human approval |
| **Approval Gate** | Asynchronous pause-and-resume with structured human response |
| **Denial Feedback Injection** | When a human denies an action, their explanation is injected into the agent's context window so it can reason about the refusal |
| **Escalation Channel** | Routing to Slack, email, Discord, Teams, SMS, RCS based on urgency and tier |
| **Agent Webhook** | Agents can be launched in response to incoming human messages |
| **Run ID / Call ID** | Per-agent, per-action identifiers enabling fine-grained audit |

---

## Autonomy Model

```
Agent executes tool calls autonomously
    ↓
Encounters @require_approval() decorated function
    ↓
HumanLayer pauses execution, routes request to human (Slack/email/etc.)
    ↓
Human responds: Approve / Deny / Modify
    ↓
Response injected into agent context window
    ↓
Agent resumes — either executes the action or reasons about the denial
```

The agent is never blocked waiting synchronously — HumanLayer uses async patterns so agents can handle multiple approval requests concurrently.

---

## Identity and Delegation Model

- **Run ID** — identifies the agent run (the entire task execution)
- **Call ID** — identifies the specific function call awaiting approval
- Both IDs appear in approval requests, responses, and audit logs
- Enables tracing of which agent, in which run, requested which action, received which human decision

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `@humanlayer.require_approval()` decorator; async-compatible |
| TypeScript SDK | Equivalent TypeScript API |
| REST API | Programmatic approval lifecycle management |
| Webhooks | Receive human responses as webhook events |
| Slack | Approval requests as interactive Slack messages |
| Email | Approval requests via email with clickable approve/deny links |
| Discord | Approval channel integration |
| Teams / SMS / RCS | Advanced tier channels |

---

## Human-in-the-Loop Support

This **is** the product. HumanLayer is purpose-built for structured, auditable, asynchronous human oversight of agent actions. It is the only service in this list where HITL is not optional — it is the core function.

---

## Framework Compatibility

| Framework | Support |
|---|---|
| LangChain | Native integration |
| CrewAI | Native integration |
| OpenAI (function calling) | Native integration |
| Claude (tool use) | Native integration |
| ControlFlow | Native integration |
| Custom agents | Via SDK or REST API |

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Jira ticket approval** | Human-initiated workflow; no agent context injection; no async agent resume |
| **ServiceNow approval** | Enterprise workflow for humans; no SDK, no context window feedback |
| **Email approval** | Unstructured; no agent resume on response; no audit attribution |
| **Slack message** | Communication channel, not an approval primitive; no structured response, no agent context injection |

---

## Pricing (2025)

| Tier | Price | Volume |
|---|---|---|
| Starter | Free | 100 requests/month, then $20/200 |
| Agent Toolkit | $500/month | 2,000 operations/month + advanced workflows |
| Enterprise | Custom | VPC deployment, RBAC, SSO, custom channels |

---

## Use Cases

- **Financial agents** — require approval before transferring funds, even within operator-defined policy
- **Email agents** — require approval before sending emails on behalf of a user (especially bulk sends)
- **Infrastructure agents** — require approval before deleting resources, scaling down, or modifying production
- **Legal/compliance agents** — require approval before filing documents, signing agreements, or submitting regulatory reports
- **Customer-facing agents** — escalate edge cases to a human supervisor before responding to a high-value customer
