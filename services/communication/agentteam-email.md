# AgentTeam Email

> **"Open-source email infrastructure for AI agents."**

| | |
|---|---|
| **Website** | https://www.agentteam.email |
| **Docs** | https://agentteamemail.mintlify.app/get-started/quickstart |
| **GitHub** | https://github.com/agentteamhq/agentteam-email |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/agentteamhq/agentteam-email?style=social)](https://github.com/agentteamhq/agentteam-email) |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push still 2026-08-01; npm `@agentteamhq/email` 0.0.1-beta.1; MIT; `skills/at-email-cli` present. Docs now served at [agentteamemail.mintlify.app](https://agentteamemail.mintlify.app/) (linked from the homepage); the old `agentteamemail.mintlify.app` host no longer resolves (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

https://www.agentteam.email

Product documentation: https://agentteamemail.mintlify.app/get-started/quickstart

---

## Official Repo

https://github.com/agentteamhq/agentteam-email

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + **published Agent Skill**

```bash
npx --yes @agentteamhq/email@latest --version
at-email agent connect
# or
at-email agent trial
at-email agent enroll TOKEN
```

The bundled skill lives in [skills/at-email-cli](https://github.com/agentteamhq/agentteam-email/tree/main/skills/at-email-cli). Official CLI and skill docs: https://agentteamemail.mintlify.app/usage/cli-and-agent-skill

Self-host with Docker Compose or Helm after the [quickstart](https://agentteamemail.mintlify.app/get-started/quickstart). Hosted setup uses Cloudflare OAuth to attach a sending domain.

---

## Agent Skills

**Status:** ✅ Available

The repository ships `skills/at-email-cli`. The website points agents at the AT Email skill on skills.sh.

| Skill | What It Teaches the Agent |
|---|---|
| `at-email-cli` | Connect or enroll, then check mailbox status, review messages, search, and send approved outbound mail |

---

## MCP

**Status:** ⚠️ Not published

No official MCP server is documented in the README or product site as of 2026-08-19. The portable surface is the `at-email` CLI and the bundled skill.

Search community skills: `npx clawhub@latest search agentteam-email`. See: https://agentskills.io/specification to contribute an MCP wrapper.

---

## What It Does

AgentTeam Email (AT Email) is open-source mail infrastructure that provisions a real mailbox per agent on a domain you control. Operators connect Cloudflare for send/receive, keep inbound mail in an R2 bucket before processing, and give agents scoped read/draft/send rights. A web client exists for humans, but the product is built around agent mailboxes, review-before-send, and an `at-email` CLI the agent can run.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | GitHub: **"Open-source email infrastructure for AI agents."** Homepage: **"Give every agent a real mailbox on your domain"** — [repo](https://github.com/agentteamhq/agentteam-email), [site](https://www.agentteam.email) |
| **Agent-specific primitive** | Per-agent mailbox with scoped powers (read, draft, or send) plus safe review of untrusted inbound mail. Not a shared human inbox |
| **Autonomy-compatible control plane** | CLI connect/trial/enroll lets an authorized agent operate a mailbox. Optional human review can gate outbound send |
| **M2M integration surface** | `at-email` CLI (`@agentteamhq/email`), bundled Agent Skill, self-host APIs, Mintlify docs |
| **Identity / delegation** | Each agent address is a distinct mailbox on the connected domain, with permissions and an activity trail of reads, drafts, and approvals |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent mailbox** | Dedicated address for receive, review, and send |
| **Per-agent permissions** | Read-only, draft, or send on a domain-owned identity |
| **Draft review lane** | Humans can approve, edit, schedule, or block outbound mail |
| **Bucket-first receive** | Inbound mail lands in R2 before the app processes it |
| **`at-email` CLI** | Status, review, search, and approved send for agents |

---

## Autonomy Model

```
Operator connects a Cloudflare domain (hosted) or self-hosts Compose/Helm
    -> provision an agent mailbox and scoped permissions
    -> agent runs at-email agent connect / trial / enroll
    -> agent reads, searches, and drafts from the CLI/skill
    -> outbound send is either permitted or held for human review
    -> activity log attributes reads, drafts, and approvals to the agent address
```

---

## Identity and Delegation Model

- **Mailbox identity:** Each agent gets a real address on the operator's domain (for example `research@…`).
- **Scoped powers:** Operators grant read, draft, or send per agent.
- **Audit:** Activity log tracks reads, drafts, replies, and inbound mail per address.
- **Human domain ownership:** Cloudflare OAuth and DNS stay with the operator; agents do not own the zone.
- **Untrusted inbound:** Official docs describe a dedicated review surface for mail the agent should not blindly execute.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `at-email` / `npx --yes @agentteamhq/email@latest` |
| Agent Skill | `skills/at-email-cli` |
| Hosted app | https://www.agentteam.email |
| Docs | https://agentteamemail.mintlify.app |
| Self-host | Docker Compose or Helm |

---

## Human-in-the-Loop Support

First-class. The product markets draft review before send, per-agent permission limits, and an activity trail. Agents can still operate autonomously inside the powers they were granted.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Shared team inbox** | Built for human seats, not per-agent identities and scoped send rights |
| **Forwarding alias** | Routes mail only; no agent CLI, permissions, or review lane |
| **Human ESP dashboard** | Requires a person to operate the mailbox; no agent enroll/connect path |

---

## Use Cases

- **Agent-owned operations** — give a long-running agent its own domain address
- **Human-reviewed sending** — agents draft; people approve or restrict what leaves the domain
- **Shared inbox triage** — route support or alerts to agents that summarize and surface what matters
- **Self-hosted mail control** — run the MIT stack on Compose or Kubernetes
