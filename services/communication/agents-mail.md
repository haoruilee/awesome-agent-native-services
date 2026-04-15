# Agents Mail

> **"Email for AI Agents."**

| | |
|---|---|
| **Website** | https://agentsmail.org |
| **Docs** | https://agentsmail.org/docs |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |

---

## Official Website

https://agentsmail.org

---

## Official Repo

Not publicly listed. Official onboarding is hosted at `skill.md` and `.well-known/agent.json`.

---

## ⭐ How to Use (Agent Onboarding)

Read:

```text
https://agentsmail.org/skill.md
```

Then follow the registration and API instructions to provision inboxes and send/receive mail.

---

## Agent Skills

**Status:** ✅ Available (URL onboarding)

| Skill | What It Teaches the Agent |
|---|---|
| `agentsmail` (`skill.md`) | Register an agent, create inboxes, send/reply messages, and monitor inbound mail |

---

## MCP

**Status:** ⚠️ Not yet published as an official dedicated MCP server (as of April 15, 2026).

| Detail | Value |
|---|---|
| **Primary interface** | REST API |
| **Onboarding** | `https://agentsmail.org/skill.md` |
| **Discovery metadata** | `https://agentsmail.org/.well-known/agent.json` |

---

## What It Does

Agents Mail provides mailbox infrastructure specifically for AI agents: programmatic inbox creation, sending/replying to email, message retrieval, and machine-readable onboarding/discovery metadata. The service is explicitly framed as communication infrastructure for autonomous agents rather than as a human mailbox product with add-on APIs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage and docs position the service as “Email for AI Agents” and expose an agent bootstrap URL (`/skill.md`) |
| **Agent-specific primitive** | Agent registration + inbox lifecycle + message send/reply API designed for autonomous tool loops |
| **Autonomy-compatible control plane** | Agent can provision inboxes and process mail headlessly via API without interactive UI steps |
| **M2M integration surface** | REST endpoints plus machine-readable onboarding/discovery URLs (`skill.md`, `.well-known/agent.json`) |
| **Identity / delegation** | Per-agent registration and mailbox scope provide explicit identity boundaries for outbound/inbound actions |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent registration** | Bootstrap an autonomous agent identity for mail operations |
| **Inbox provisioning** | Create/manage agent-owned mailboxes programmatically |
| **Message send/reply** | API actions for outbound and threaded communication |
| **Message retrieval** | Programmatic inbox access for autonomous processing |
| **Discovery metadata** | `.well-known/agent.json` for machine-readable capability discovery |

---

## Autonomy Model

1. Agent reads `https://agentsmail.org/skill.md`.
2. Agent registers and stores its API credentials.
3. Agent provisions an inbox via API.
4. Agent sends/replies to messages and polls or receives inbound updates.
5. Agent logs actions per mailbox scope for traceable communication.

---

## Identity and Delegation Model

- **Agent identity:** Explicit registration flow for agent credentials.
- **Delegation:** Mailbox-level permissions can be scoped to agent-owned identities.
- **Audit trail:** API-driven send/reply/read actions are attributable to registered credentials.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | https://agentsmail.org/docs |
| URL onboarding | `https://agentsmail.org/skill.md` |
| Agent metadata | `https://agentsmail.org/.well-known/agent.json` |

---

## Human-in-the-Loop Support

Optional. Core communication operations are autonomous and API-driven.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Human email APIs (Gmail/Outlook wrappers)** | Typically centered on delegated human inbox access rather than native agent-owned communication identities |
| **General notification APIs** | May send messages but lack agent registration + autonomous mailbox lifecycle primitives |
| **SMTP-only providers** | Transport-level only; no agent-native onboarding and identity/delegation semantics |

---

## Use Cases

- **Agent-to-human updates** — send progress, reports, and follow-ups.
- **Agent inbox operations** — receive and parse customer/vendor responses.
- **Multi-agent communication** — allocate one mailbox per agent role.
- **Async workflows** — trigger downstream automations from inbound email events.
