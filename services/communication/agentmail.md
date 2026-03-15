# AgentMail

> **"Email for AI agents."**

| | |
|---|---|
| **Website** | https://agentmail.to |
| **Docs** | https://docs.agentmail.to |
| **GitHub** | https://github.com/agentmail-to |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |
| **Funding** | $6M seed · Y Combinator |

---

## What It Does

AgentMail is an email inbox API built for AI agents to **own** email identities. Rather than proxying through a human's Gmail or Outlook account, agents create dedicated inboxes via API, receive emails via webhook, participate in threaded conversations, and send replies — all without any human mail client in the loop.

The core abstraction is: **the agent is the first-class internet entity at the email address**. AgentMail makes that concrete.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage declares: *"Email inbox API for AI agents"*; docs state agents are *"first-class users on the internet"* |
| **Agent-specific primitive** | Agent inbox (not a user inbox), threaded conversation scoped to agent context, webhook-on-inbound-email, semantic search across agent mail |
| **Autonomy-compatible control plane** | Inboxes created and deleted via API in milliseconds; no human mail setup required |
| **M2M integration surface** | REST API + Python SDK + TypeScript SDK + MCP server; no human-facing UI required |
| **Identity / delegation** | Each inbox is agent-owned; custom domains supported; inbox ≠ forwarding alias |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent Inbox** | Dedicated email address owned by an agent, provisioned via API |
| **Threaded Conversation** | Full email thread accessible as structured data for context injection |
| **Inbound Webhook** | Real-time push when the agent receives an email |
| **Semantic Search** | Search across agent's email history with natural language |
| **Attachment Handling** | Read and write attachments programmatically |

---

## Autonomy Model

Agents operate fully headlessly. There is no concept of a human inbox owner. An agent can:

1. `POST /inboxes` — create a new inbox (returns `agent@agentmail.to`-style address instantly)
2. Configure webhook URL to receive inbound events
3. `POST /inboxes/{id}/messages` — send outbound email
4. `GET /inboxes/{id}/threads` — read thread history for context

No browser session, no OAuth consent flow, no human confirmation per operation.

---

## Identity and Delegation Model

- Each inbox is a discrete identity. Agents can hold multiple inboxes simultaneously.
- Operators can provision inboxes on behalf of agents or let agents self-provision.
- Custom domain support allows white-labeled agent email identities.
- No delegation to a human account — the inbox is the agent's, not forwarded from a person's.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Full CRUD on inboxes, messages, threads |
| Python SDK | `pip install agentmail` |
| TypeScript SDK | `npm install agentmail` |
| MCP Server | Model Context Protocol integration for direct LLM tool use |
| Webhooks | Push notification on inbound email events |

---

## Human-in-the-Loop Support

By default, none required. HumanLayer or similar can be composed on top if an agent needs to escalate specific emails to a human for review before responding.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Gmail API** | Built for human Gmail accounts; requires OAuth consent from a real user; inbox belongs to a person |
| **SendGrid** | Transactional email for human-authored campaigns; no concept of agent inbox ownership or inbound webhook |
| **Postmark** | Developer email delivery; no per-agent inbox identity, no inbound thread primitives |
| **Mailgun** | Routing for human domains; identity model is domain-based, not agent-based |

---

## Use Cases

- **2FA extraction** — agent creates a temporary inbox, triggers a sign-up, receives the verification code, and discards the inbox
- **Scheduling assistant** — agent owns a calendar-coordination inbox, handles back-and-forth with participants
- **Document processing** — agent receives invoices or contracts via email, extracts data, routes for approval
- **Customer service routing** — agent triages inbound mail, responds to FAQs, escalates edge cases via HumanLayer

---

## Scale and Reliability

- 100+ million emails delivered globally
- Enterprise-grade, multi-region redundant infrastructure
- Inboxes spin up in milliseconds
- Free tier: 3 inboxes + 3,000 emails/month (no credit card required)
