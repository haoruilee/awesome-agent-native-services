# OpenMail

> **"Built for agents, not marketers."**

| | |
|---|---|
| **Website** | https://openmail.sh |
| **Docs** | https://docs.openmail.sh |
| **Console** | https://console.openmail.sh |
| **GitHub** | https://github.com/openmailsh/cli |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/openmailsh/cli?style=social)](https://github.com/openmailsh/cli) |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |

---

## Official Website

https://openmail.sh

---

## Official Repo

https://github.com/openmailsh/cli — OpenMail CLI (`openmail setup`, credential and skill file generation)

---

## How to Use (Agent Onboarding)

**CLI + REST — provision an agent inbox, then send/receive via API.**

```bash
npm install -g @openmail/cli
openmail setup
```

Then use the REST API with `Authorization: Bearer om_...` per [Quickstart](https://docs.openmail.sh/quickstart). Inbound mail: [Webhooks](https://docs.openmail.sh/guides/webhooks) or [WebSocket](https://docs.openmail.sh/concepts/websockets).

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official `npx skills add` bundle located; `openmail setup` writes a local skill file with credentials.

```bash
npm install -g @openmail/cli && openmail setup
```

| Skill | What It Teaches the Agent |
|---|---|
| *(generated locally)* | Inbox provisioning, API key storage, webhook or WebSocket receive patterns |

Search community skills: `npx clawhub@latest search openmail`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not yet published as a first-party MCP server

Primary interface: REST API, WebSocket, webhooks, CLI.

| Detail | Value |
|---|---|
| **API Base** | `https://api.openmail.sh` (per docs) |
| **Compatible Clients** | Any HTTP-capable agent runtime |

---

## What It Does

OpenMail is **email infrastructure for AI agents**: one inbox per agent, two-way threading with normal email clients, and inbound delivery over **webhooks or WebSocket** (no polling). Attachments are parsed into **LLM-ready text** (PDFs, CSVs, images, office docs). The product explicitly contrasts itself with newsletter-oriented email APIs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage title: *"OpenMail - Email API for AI Agents"*; hero: *"Built for agents, not marketers"*; docs intro: *"Email infrastructure for AI agents"* ([docs.openmail.sh](https://docs.openmail.sh)) |
| **Agent-specific primitive** | **One inbox per agent** with real address; **push inbound** (webhook/WebSocket) for autonomous reaction; **RAG-ready attachment parsing** aimed at LLM consumption — not a human inbox UI |
| **Autonomy-compatible control plane** | After API key / setup, agents send and receive without per-message human approval |
| **M2M integration surface** | REST API, WebSocket, webhooks, CLI (`@openmail/cli`) |
| **Identity / delegation** | Per-inbox `inbox_id` for multi-tenant routing; API keys from [console.openmail.sh](https://console.openmail.sh) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Inbox provisioning** | Create dedicated agent email addresses (hosted or custom domain) |
| **Send / thread** | Outbound mail with normal email threading semantics |
| **Webhook / WebSocket inbound** | Real-time `message.received`-style events without polling |
| **Attachment → LLM text** | Automatic extraction from PDF, CSV, images, XLSX, DOCX, etc. |

---

## Autonomy Model

1. Agent or operator runs `openmail setup` (or creates inbox via API) and stores API key securely.
2. Agent sends mail via REST.
3. Agent subscribes to WebSocket or registers webhook URL.
4. On inbound mail, OpenMail pushes structured payload; agent updates memory or replies without human clicks.

---

## Identity and Delegation Model

- Bearer API keys (`om_...`) scoped to the account; docs warn not to embed keys in prompts.
- Multi-tenant: many inboxes per account; route by `inbox_id`.
- Human may complete console signup once; operational mail loop is unmanned.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | [API reference](https://docs.openmail.sh/api-reference/introduction) |
| WebSocket | [WebSockets](https://docs.openmail.sh/concepts/websockets) |
| Webhooks | [Webhooks](https://docs.openmail.sh/guides/webhooks) |
| CLI | `@openmail/cli` — `openmail setup` |

---

## Human-in-the-Loop Support

- Initial account creation and billing may require human action in the console.
- Ongoing send/receive is programmatic.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **SendGrid / Postmark** | Outbound/marketing-first; not agent-owned two-way inboxes with push-to-agent semantics |
| **Gmail API** | Human Google identity; OAuth consent flows; not agent-first |
| **Shared team inboxes** | No per-agent address + structured push model for autonomous agents |

---

## Use Cases

- **Support agents** — receive and thread customer email without a separate ticketing UI.
- **Signup / OTP flows** — browser agents complete flows; inbox receives verification mail.
- **Document intake** — invoices and attachments land parsed for downstream LLM reasoning.
