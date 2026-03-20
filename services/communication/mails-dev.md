# mails.dev

> **"Email for AI Agents."**

| | |
|---|---|
| **Website** | https://mails.dev |
| **Skill** | https://mails.dev/skill.md |
| **GitHub** | https://github.com/chekusu/mails |
| **npm** | https://www.npmjs.com/package/mails |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |

---

## Official Website

https://mails.dev

---

## Official Repo

https://github.com/chekusu/mails

---

## ⭐ How to Use (Agent Onboarding)

> **URL Onboarding — This service can be joined with a single sentence.**

mails.dev hosts a machine-readable `skill.md` that any AI agent can read and execute to claim a mailbox, send and receive emails, and wait for verification codes — the latter being an agent-specific primitive for automated signup flows.

**One-sentence instruction:**
```
Read https://mails.dev/skill.md and follow the instructions.
```

**What the agent gets by reading the URL:**
- CLI install: `npm install -g mails`
- Claim `@mails.dev` mailbox: `mails claim <name>` (one-time human approval via device code)
- Send: `mails send --to ... --subject ... --body ...`
- Inbox: `mails inbox`, `mails inbox --query "..."` (full-text search)
- **Agent-specific**: `mails code --to mailbox@mails.dev --timeout 30` — long-polls for verification codes (no polling loop needed)
- REST API: `https://api.mails.dev/v1/*`

**Interaction pattern:** `URL Onboarding` ⭐ — the highest tier of agent-nativeness.

```bash
# Quick start: claim mailbox (human approves once)
npm install -g mails
mails claim myagent
# Then: mails send, mails inbox, mails code
```

---

## Agent Skills

**Status:** ✅ URL Onboarding via skill.md — agent reads `https://mails.dev/skill.md` and follows instructions

---

## MCP

**Status:** ⚠️ Not yet published

Primary interface: CLI, REST API (`https://api.mails.dev`), TypeScript SDK (`mails` npm package).

---

## What It Does

mails.dev is **email infrastructure for AI agents** — send and receive emails with a free `@mails.dev` mailbox or your own domain. Agents get programmatic inbox provisioning, full-text search across mail, attachment handling, and a first-class primitive that no human email client needs: **wait for verification code** — `mails code` long-polls until an email with a verification code arrives, then returns it to stdout. This eliminates the agent's need to poll, parse HTML, or guess code patterns.

100 free emails/month on hosted; unlimited with Resend API key or self-hosted Worker.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Email Infrastructure for AI Agents"*; meta: *"Built for AI agents"*; skill.md designed for agent onboarding |
| **Agent-specific primitive** | `mails code` / `waitForCode` — long-polls for verification codes; no human email client has this; built for automated signup, 2FA, and OTP flows |
| **Autonomy-compatible control plane** | After one-time claim (device code), agent operates fully: send, inbox, search, code-wait; no per-email human approval |
| **M2M integration surface** | CLI, REST API, TypeScript SDK |
| **Identity / delegation** | Each `@mails.dev` mailbox is agent-owned; API key scoped per mailbox; custom domain supported via self-hosted Worker |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Claim mailbox** | `mails claim <name>` — get `name@mails.dev`; one-time human approval via device code |
| **Send** | Send email with optional attachments |
| **Inbox** | List, search (full-text, relevance-ranked), filter by sender, attachment type, date range |
| **Wait for code** | `mails code` — long-polls for verification code; returns code to stdout; exits if timeout |
| **Sync** | Incremental pull for self-hosted Worker |

---

## Autonomy Model

1. Agent reads `https://mails.dev/skill.md` and installs CLI
2. Agent runs `mails claim myagent` — human approves once (browser or device code)
3. Agent sends emails via `mails send` or REST API
4. Agent searches inbox via `mails inbox --query "..."` or REST
5. Agent waits for verification codes via `mails code` — no polling loop, no HTML parsing

---

## Identity and Delegation Model

- API key (`mk_...`) from claim flow; stored in `~/.mails/config.json`
- Each mailbox is agent-owned; up to 10 per human user
- Self-hosted Worker supports custom domain with `AUTH_TOKEN`

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `mails claim`, `mails send`, `mails inbox`, `mails code`, `mails config` |
| REST API | `https://api.mails.dev/v1/send`, `/v1/inbox`, `/v1/code`, `/v1/claim/*` |
| TypeScript SDK | `mails` npm package — `send()`, `getInbox()`, `searchInbox()`, `waitForCode()` |

---

## Human-in-the-Loop Support

- **Claim flow**: One-time human approval via browser or device code; required to prevent abuse
- After claim: fully autonomous

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Gmail / Outlook API** | Human account; OAuth per user; no `wait for code` primitive; not agent-owned identity |
| **Resend / SendGrid** | Send-only or webhook receive; no agent inbox, no verification-code wait |
| **Mailhooks** | Inbound webhooks; no send, no agent-owned mailbox, no code extraction |

---

## Use Cases

- **Automated signup flows** — Agent signs up for services; `mails code` captures verification email
- **2FA / OTP** — Wait for one-time codes without polling or parsing
- **Agent correspondence** — Send and receive as `agent@mails.dev`
- **Research / scraping** — Receive confirmations, parse attachments, full-text search
