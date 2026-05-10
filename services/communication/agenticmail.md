# AgenticMail

> **"Email & SMS infrastructure for AI agents — send and receive real email and text messages programmatically."**

| | |
|---|---|
| **Website** | https://github.com/agenticmail/agenticmail |
| **Docs** | https://github.com/agenticmail/agenticmail#readme |
| **GitHub** | https://github.com/agenticmail/agenticmail |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |
| **Status** | Open source · self-hosted · v0.5.x (rapid iteration through 2026) |

---

## Official Website

https://github.com/agenticmail/agenticmail

---

## Official Repo

https://github.com/agenticmail/agenticmail

---

## How to Use (Agent Onboarding)

```
# Self-hosted (Docker):
git clone https://github.com/agenticmail/agenticmail
cd agenticmail && docker compose up -d
# then: POST /api/v1/inboxes  →  receive an @<your-domain> address
# and:  POST /api/v1/sms      →  send/receive SMS via Google Voice
```

---

## Agent Skills

**Status:** ⚠️ Not yet published.

Search community skills:

```bash
npx clawhub@latest search agenticmail
```

If you author a skill, follow the [AgentSkills specification](https://agentskills.io/specification).

---

## MCP

**Status:** ⚠️ Not yet published as a first-party MCP server. The 75+ REST endpoints are designed to be wrapped by any MCP host (Claude Code, Cursor, Gemini CLI). Community wrappers are in progress.

| Detail | Value |
|---|---|
| **MCP Repo** | (community wrappers; not first-party) |
| **Transport** | n/a — primary surface is REST |
| **Compatible Clients** | any HTTP-capable agent runtime |

---

## What It Does

AgenticMail is a self-hosted platform that gives every AI agent a **real email address and a real phone number** — not a forwarder, not an alias on top of a human account, but a stand-alone communication identity owned by the agent. It bundles a local Stalwart mail server (run via Docker), an inbound webhook system, an SMS/voice integration that proxies to Google Voice, and a REST surface of 75+ endpoints covering inboxes, threads, attachments, contacts, message search, and outbound delivery.

The design choice that distinguishes it from existing entries in this category is the unified email + SMS identity: one provisioning call yields both an `@<your-domain>` mailbox and a programmable phone number, so agents can complete sign-ups that require either form of 2FA without dropping into a different vendor.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repo tagline: *"Email & SMS infrastructure for AI agents — send and receive real email and text messages programmatically."* |
| **Agent-specific primitive** | Per-agent email + phone identity bundle, inbound webhook on receive, full-text + verification-code extraction across both channels |
| **Autonomy-compatible control plane** | Inbox + phone number provisioned via API in milliseconds; no human mail client, no carrier portal |
| **M2M integration surface** | 75+ REST endpoints, Docker-Compose deploy, webhook fan-out |
| **Identity / delegation** | Agent owns both the mailbox and the phone number — distinct from any human Google account; custom domain supported |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent Communication Identity** | Bundle of `agent@<domain>` mailbox + programmable phone number, provisioned together |
| **Inbound Webhook** | Push notification fired on inbound mail or SMS |
| **Threaded Conversation** | Full mail thread + SMS conversation history accessible as structured data |
| **Verification-Code Extraction** | Built-in OTP/2FA code parsing across email and SMS |
| **Self-Hosted Mail Server** | Stalwart-based, no third-party SaaS in the path |

---

## Autonomy Model

1. Operator brings up the stack: `docker compose up -d` (Stalwart + API + Google Voice bridge).
2. Agent calls `POST /api/v1/inboxes` → receives an inbox + paired phone number.
3. Agent registers a webhook URL.
4. Inbound email or SMS triggers a webhook with parsed body, attachments, and any extracted verification codes.
5. Agent calls `POST /api/v1/messages` (mail) or `POST /api/v1/sms` (text) to reply or initiate outbound.

No browser session, no OAuth handoff per operation, no human-side mail client.

---

## Identity and Delegation Model

- Each provisioned identity is a discrete agent-owned address + phone number.
- Custom domains supported — operators can run `agent-1@acme.ai` etc.
- Phone number is bound to the agent's inbox identity, not to a human Google Voice account in the operational path.
- Audit log per identity, per channel.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | 75+ endpoints (inboxes, threads, messages, SMS, contacts, search) |
| Webhooks | Inbound mail + SMS push |
| Self-hosted SMTP/IMAP | Stalwart mail server runs in-cluster |
| SMS/Voice Bridge | Google Voice integration for programmable phone numbers |

---

## Human-in-the-Loop Support

By default, none required. An approval gate (HumanLayer or similar) can be composed on top if certain outbound mail/SMS should be queued for a human review before delivery.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Gmail + Google Voice** | Tied to a human Google account; agent cannot own the identity; OAuth consent loops break autonomy |
| **Twilio** | Programmable SMS exists, but no per-agent inbox + phone identity bundle, and the messaging primitives are framed around human marketing/support flows |
| **SendGrid / Mailgun** | Outbound-only; no agent-owned inbox; no SMS coupling |

---

## Use Cases

- **2FA-heavy sign-ups** — agent provisions an identity with both email and phone, completes a flow that requires either form of OTP, then disposes
- **Inbound triage** — agent receives mail and SMS for a product line and routes by content
- **Self-hosted compliance** — teams that cannot use SaaS mail (data residency, regulated industry) run AgenticMail in-cluster and still expose the agent-native primitives
