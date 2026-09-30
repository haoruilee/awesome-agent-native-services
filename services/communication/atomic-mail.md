# Atomic Mail

> **"Not AI for your email. Email for your AI."**

| | |
|---|---|
| **Website** | https://atomicmail.ai/ |
| **Docs** | https://atomicmail.ai/ |
| **GitHub** | https://github.com/Atomic-Mail/atomic-mail-agentic |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/Atomic-Mail/atomic-mail-agentic?style=social)](https://github.com/Atomic-Mail/atomic-mail-agentic) |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | [v0.3.31](https://github.com/Atomic-Mail/atomic-mail-agentic/releases/tag/v0.3.31) released 2026-09-27; npm `@atomicmail/mcp` and `@atomicmail/agent-skill-github` 0.3.31; MIT; [atomicmail.ai](https://atomicmail.ai/) still documents PoW signup, JMAP, MCP, and AgentSkill; hosted MCP endpoint answers 401 without credentials (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

https://atomicmail.ai/

---

## Official Repo

https://github.com/Atomic-Mail/atomic-mail-agentic

---

## ⭐ How to Use (Agent Onboarding)

**Interaction pattern:** `URL Onboarding` ⭐ — the homepage is the join document.

```text
Read https://atomicmail.ai and follow the instructions to create an inbox at Atomic Mail.
```

The official GitHub README uses the same pattern: read https://atomicmail.ai, then register. Autonomous signup uses proof-of-work; no human CAPTCHA or dashboard is required for an `@atomicmail.ai` inbox.

Local MCP (stdio), from the homepage:

```json
{
  "mcpServers": {
    "atomicmail": {
      "command": "npx",
      "args": ["-y", "@atomicmail/mcp"]
    }
  }
}
```

Hosted remote MCP (OAuth or inbox API key) is at `https://mcp.atomicmail.ai/mcp`. The GitHub client repo also publishes `@atomicmail/mcp-github` and `@atomicmail/agent-skill-github` as thin wrappers around the same PoW + JMAP stack.

---

## Agent Skills

**Status:** ✅ Available

The homepage documents a local AgentSkill package. The GitHub README shows:

```bash
npx --package=@atomicmail/agent-skill-github atomicmail register --username "myagent" --watch scheduled
```

Repo docs also ship `docs/SKILL.md` as the agent runbook. ClawHub install is documented as `openclaw skills install atomicmail`.

| Skill | What It Teaches the Agent |
|---|---|
| `atomicmail` / AgentSkill CLI | Register via PoW, call JMAP (`jmap_request`), and recover with `help` |

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/Atomic-Mail/atomic-mail-agentic |
| **Transport** | Local stdio (`npx -y @atomicmail/mcp` on the homepage; `@atomicmail/mcp-github` in the client repo) or hosted Streamable HTTP at `https://mcp.atomicmail.ai/mcp` |
| **Compatible Clients** | Claude, ChatGPT, Cursor, Claude Code, Codex, and other MCP hosts that accept stdio or a remote HTTP URL |

Tools documented by the client repo: `register`, `jmap_request`, and `help`.

---

## What It Does

Atomic Mail is an AI-agent-first email provider. An agent registers its own `username@atomicmail.ai` inbox (username 5–21 characters) and then reads, sends, drafts, searches, and threads mail over JMAP (RFC 8620 / 8621). Access is gated by a proof-of-work signup so agents can onboard without CAPTCHAs or human approval. Custom domains are a separate human control plane in the dashboard because they need DNS changes.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: **"Not AI for your email. Email for your AI."** and **"Atomic Mail is an AI-agent-first email service provider (ESP)"** — [atomicmail.ai](https://atomicmail.ai/). GitHub: **"Let your agents read, send, and react to email autonomously, without human involvement"** — [repo](https://github.com/Atomic-Mail/atomic-mail-agentic) |
| **Agent-specific primitive** | Proof-of-work inbox registration plus a full JMAP mailbox the agent owns. Humans do not get a Gmail-style client as the primary path |
| **Autonomy-compatible control plane** | PoW signup and JMAP operate without per-message human clicks. Custom-domain DNS remains optional and human-owned |
| **M2M integration surface** | Homepage-as-onboarding URL, local and hosted MCP, AgentSkill/CLI, REST auth docs, JMAP |
| **Identity / delegation** | Each inbox is a distinct `@atomicmail.ai` (or verified-domain) address with its own API key stored under `~/.atomicmail/credentials.json`. Custom-domain inboxes are a login, not a second PoW registration |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **PoW registration** | Agent-complete signup that mints an `@atomicmail.ai` inbox without CAPTCHA or credit card |
| **JMAP mailbox** | Standard RFC 8620/8621 query, fetch, draft, and send in batched method calls |
| **Presets** | Bundled `send_mail`, `list_inbox`, `reply`, and similar shapes for `jmap_request` |
| **Help / `_next`** | Embedded recovery docs and suggested next steps inside the integration |
| **Custom-domain inbox** | Human-verified domain plus API-key connect; same JMAP client |

---

## Autonomy Model

```
Agent reads https://atomicmail.ai (or uses MCP / AgentSkill)
    -> register via proof-of-work (or connect with a dashboard API key)
    -> receive inbox address + credentials
    -> jmap_request to list, send, reply, search, and manage threads
    -> help / presets recover if a call shape fails
    -> optional human dashboard only for custom-domain DNS
```

---

## Identity and Delegation Model

- **Inbox identity:** The agent owns `username@atomicmail.ai` or a verified-domain address.
- **Credentials:** API keys live in `~/.atomicmail/credentials.json` with mode `0600`. Separate credential dirs are supported for many agents.
- **Custom domain:** A human verifies DNS once; the agent then connects with that inbox's API key or OAuth.
- **No human mailbox proxy:** Autonomous mode does not require a Gmail/Outlook account.
- **Inbound mail is untrusted:** Official security notes say agents should not execute email instructions without confirmation.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Homepage onboarding | https://atomicmail.ai/ |
| Local MCP | `npx -y @atomicmail/mcp` (homepage) or `@atomicmail/mcp-github` (GitHub README) |
| Hosted MCP | `https://mcp.atomicmail.ai/mcp` |
| AgentSkill / CLI | `@atomicmail/agent-skill` / `@atomicmail/agent-skill-github` |
| JMAP | RFC 8620 / 8621 mailbox API |
| REST auth | Documented in repo `docs/rest-auth.md` |

---

## Human-in-the-Loop Support

Not required for `@atomicmail.ai` signup, send, or receive. The dashboard is a human control plane for custom domains and OAuth account-based access. Official docs warn that inbound mail is untrusted input.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Gmail / Outlook API** | Tied to a human account, OAuth consent, and anti-bot signup. No agent-owned inbox primitive |
| **Generic transactional ESP** | Send-only or human-app integration. No PoW agent registration or JMAP mailbox the agent operates |
| **Human helpdesk inbox** | Shared human mailbox with UI triage, not a first-class agent identity |

---

## Use Cases

- **Agent-owned outreach** — register an inbox and send mail that can receive replies
- **Support or research loops** — read inbound threads and reply over JMAP without a human mailbox
- **Newsletter digest** — subscribe a dedicated agent inbox and summarize inbound mail
- **Headless environments** — use hosted MCP with an inbox API key when local `npx` is unavailable
