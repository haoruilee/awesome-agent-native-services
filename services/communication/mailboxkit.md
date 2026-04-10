# MailboxKit

> **"Email infrastructure for AI agents."**

| | |
|---|---|
| **Website** | https://mailboxkit.com |
| **Docs** | https://mailboxkit.com/api-docs |
| **Skill** | https://mailboxkit.com/skill.md |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |

---

## Official Website

https://mailboxkit.com

---

## Official Repo

MailboxKit does not publish an open-source application repository; the **machine-readable onboarding** and **REST API** are the primary integration surfaces. See [API docs](https://mailboxkit.com/api-docs) and [skill.md](https://mailboxkit.com/skill.md).

---

## ⭐ How to Use (Agent Onboarding)

> **URL Onboarding — agents can start from a hosted machine-readable skill file.**

**One-sentence instruction:**
```
Read https://mailboxkit.com/skill.md and follow the instructions.
```

**Typical API flow:**
- Base URL: `https://mailboxkit.com/api/v1`
- Auth: `Authorization: Bearer <API_KEY>`
- Provision inbox, send/receive, webhooks per skill and API reference

**Interaction pattern:** `URL Onboarding` ⭐

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ✅ URL Onboarding — hosted at [`https://mailboxkit.com/skill.md`](https://mailboxkit.com/skill.md)

| Skill | What It Teaches the Agent |
|---|---|
| **mailboxkit.com/skill.md** | Self-register, send, receive, reply via REST API |

---

## MCP

**Status:** ⚠️ Not yet published as a first-party MCP server

Primary interface: REST API and webhooks.

---

## What It Does

MailboxKit gives **each AI agent a real email address** in seconds: send, receive, and reply through a REST API with **inbound webhooks**, automatic threading (`References` / `In-Reply-To`), optional open/click tracking, and **custom domains** with automated DKIM, SPF, and DMARC. Pricing is pay-as-you-go per email and attachment.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Email infrastructure for AI agents"*; *"Built for autonomous agents that need to communicate over email"* ([mailboxkit.com](https://mailboxkit.com)) |
| **Agent-specific primitive** | **Per-agent mailbox** on `agent.mailboxkit.com` or custom domain; **webhook-delivered inbound** for autonomous reaction — not a human webmail product |
| **Autonomy-compatible control plane** | API-driven lifecycle; no per-email human approval |
| **M2M integration surface** | REST API v1, webhooks, hosted `skill.md` |
| **Identity / delegation** | Bearer API keys; one address per agent; dashboard or API registration |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Inbox / address** | Unique email per agent, provisioned via API |
| **Send / reply** | Outbound with threaded replies |
| **Inbound webhooks** | Real-time delivery of new mail to agent-controlled endpoints |
| **Custom domain** | Automated DNS/email auth setup |

---

## Autonomy Model

1. Agent reads `https://mailboxkit.com/skill.md` and obtains API key (dashboard or API).
2. Agent creates or selects inbox via API.
3. Agent sends mail and registers webhook for inbound.
4. Agent processes webhook payloads and replies in-thread without human operation.

---

## Identity and Delegation Model

- API keys as Bearer tokens.
- Distinct email identity per agent (`agent-*@agent.mailboxkit.com` or branded domain).
- Optional human signup for billing; runtime loop is API-only.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `https://mailboxkit.com/api/v1` — [API docs](https://mailboxkit.com/api-docs) |
| Webhooks | Inbound email events to HTTPS endpoints |
| URL Onboarding | `https://mailboxkit.com/skill.md` |

---

## Human-in-the-Loop Support

- Account registration and payment top-up may use the human dashboard.
- Mail operations themselves are fully programmatic.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Marketing ESPs** | Batch/broadcast-first; weak model for per-agent addresses + bidirectional agent loops |
| **Consumer webmail** | Not provisioned or controlled headlessly at agent scale |

---

## Use Cases

- **Coding agents** — status email, code review threads ([use case](https://mailboxkit.com/use-cases/coding-agents)).
- **Support / sales / research agents** — autonomous correspondence at scale.
