# Novu

> **"The open-source notification infrastructure — with an Agent Toolkit for AI agents."**

| | |
|---|---|
| **Website** | https://novu.co |
| **Docs** | https://docs.novu.co |
| **GitHub** | https://github.com/novuhq/novu |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/novuhq/novu?style=social)](https://github.com/novuhq/novu) |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |
| **License** | Open-source (MIT) + Novu Cloud |
| **Stars** | 36,000+ GitHub stars |

---

## Official Website

https://novu.co

---

## Official Repo

https://github.com/novuhq/novu — Core platform (open-source)

https://github.com/novuhq/skills — Official Agent Skills

---

## Agent Skills

**Status:** ✅ Official skills published at [`novuhq/skills`](https://github.com/novuhq/skills)

```bash
npx skills add novuhq/skills
```

| Skill | What It Teaches the Agent |
|---|---|
| `trigger-notification` | Trigger single, bulk, broadcast, and topic-based notifications |
| `manage-subscribers` | Create, update, and manage notification subscribers |
| `manage-topics` | Create and manage subscriber topics for group notifications |
| `in-app-inbox` | Integrate and query the in-app notification inbox |
| `configure-preferences` | Set and query notification preferences per subscriber |

**Compatibility:** Claude Code, Cursor, Codex, and all [AgentSkills](https://agentskills.io/)-compatible tools.

---

## MCP

**Status:** ✅ Available

Novu provides an MCP server enabling agents to trigger notifications and manage subscribers directly through the Model Context Protocol.

| Detail | Value |
|---|---|
| **MCP Docs** | https://docs.novu.co/mcp |
| **Transport** | stdio |
| **Compatible Clients** | Claude Desktop, Cursor, any MCP-compatible client |

---

## What It Does

Novu is an open-source notification infrastructure platform with a dedicated **Agent Toolkit** that exposes notification workflows as tools agents can call. An agent needing to send a notification — via email, SMS, Slack, push, in-app, or any other channel — calls a Novu workflow tool; Novu handles channel selection, template rendering, delivery, and preference enforcement.

The agent does not know or care which channel is used. Novu's workflow engine decides based on subscriber preferences and channel availability.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Dedicated Agent Toolkit product; official Agent Skills published at `novuhq/skills`; workflows explicitly exposed as agent tools |
| **Agent-specific primitive** | Workflows-as-tools (each Novu workflow becomes a callable tool with schema-typed parameters); HITL flows where agents solicit structured user input before acting |
| **Autonomy-compatible control plane** | Agents trigger notifications without knowing channel details; preference enforcement is automatic |
| **M2M integration surface** | Node.js SDK, Python SDK, REST API, MCP server, Agent Skills (`npx skills add novuhq/skills`) |
| **Identity / delegation** | Per-subscriber identity; notification preference model per subscriber; audit log per workflow trigger |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Workflow-as-Tool** | Each Novu workflow exposed as a callable agent tool with schema-typed trigger data |
| **Cross-Channel Delivery** | Agent triggers one workflow; Novu delivers via email, SMS, Slack, push, in-app, or any configured channel |
| **Subscriber Management** | Programmatic subscriber creation, update, and preference management |
| **Topic Notifications** | Broadcast notifications to groups of subscribers via a single tool call |
| **In-App Inbox** | Programmatically manage an in-app notification inbox readable by both agents and users |
| **HITL Notification Flow** | Agent sends a notification requesting structured user input before taking an action |
| **Preference Enforcement** | Delivery channel chosen automatically based on subscriber preferences — agent doesn't need to know |

---

## Autonomy Model

```
Agent needs to notify a user (e.g., "approval required for payment")
    ↓
Agent calls novu.trigger("payment-approval", { subscriberId, payload })
    ↓
Novu looks up subscriber preferences (email preferred, SMS fallback)
    ↓
Novu renders template and delivers via preferred channel
    ↓
User responds (or doesn't within timeout)
    ↓
Agent receives structured response event and continues execution
```

The agent never hardcodes channel logic. Notification infrastructure is fully abstracted.

---

## Identity and Delegation Model

- Subscribers have unique IDs; preferences stored per subscriber
- Notification audit log tracks which agent triggered which workflow, for which subscriber, via which channel
- Topic-based notifications allow agents to address groups without managing member lists

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Node.js SDK | `npm install @novu/node` |
| Python SDK | `pip install novu` |
| REST API | Full workflow management and trigger API |
| MCP Server | Model Context Protocol for direct LLM notification triggering |
| Agent Skills | `npx skills add novuhq/skills` (5 skills covering all notification patterns) |

---

## Human-in-the-Loop Support

First-class pattern. HITL notification flows let agents send a structured prompt to a human and wait for a response before proceeding. This is the agent-initiated equivalent of an approval request — delivered through the user's preferred notification channel.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **SendGrid** | Human-facing email delivery; no notification preference layer, no cross-channel routing, no workflow-as-tool primitive |
| **Twilio** | Human telecom infrastructure; no subscriber preference management, no cross-channel abstraction |
| **Mailchimp** | Marketing email for humans; no programmatic agent trigger, no preference enforcement |
| **Raw email/SMS API** | Agent must hardcode channel logic, template rendering, and preference management |

---

## Use Cases

- **Approval notifications** — agent sends a structured approval request to a manager via their preferred channel and waits for response
- **Status updates** — agent notifies users of task completion, errors, or milestones as workflows execute
- **Multi-channel alerts** — agent triggers an alert; Novu delivers via Slack to team lead, email to manager, SMS to on-call
- **In-app activity feeds** — agent writes notification events to an in-app inbox users can query
- **Escalation workflows** — agent escalates unresolved issues through a notification escalation chain
