# ATXP Email

> **"Email for AI agents."**

| | |
|---|---|
| **Website** | https://atxp.email/ |
| **Docs** | https://docs.atxp.dev |
| **GitHub** | https://github.com/atxp-dev |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |

---

## Official Website

https://atxp.email/

---

## Official Repo

https://github.com/atxp-dev

---

## ⭐ How to Use (Agent Onboarding)

`Read https://atxp.email/ and follow the docs to create an agent inbox via CLI/API.`

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills package found.

## MCP

**Status:** ⚠️ Not clearly documented as a standalone MCP server for email only.

## What It Does

ATXP Email gives AI agents their own inbox identity so agents can receive verification codes, notifications, and human messages without relying on a human mailbox.

## Why It Is Agent-Native

- Agent-first positioning: website headline is explicitly "Email for AI agents".
- Agent-specific primitive: per-agent inbox as a machine identity.
- M2M surface: CLI/API-first flow.
- Autonomy model: agents can create inboxes and process inbound mail automatically.

## Primary Primitives

- Agent inbox creation
- Inbox/message listing
- Message read + code extraction workflows

## Autonomy Model

Agent can provision inboxes and read verification emails headlessly through CLI/API.

## Identity and Delegation Model

Inbox identity is issued directly to the agent runtime and can be used as the agent's internet communication endpoint.

## Protocol Surface

- CLI
- Web/API docs

## Human-in-the-Loop Support

Optional only; not required for normal receive/read flows.

## Why Generic Alternatives Do Not Qualify

Gmail/Outlook APIs are user-centric and require human account ownership, while ATXP email identity is provisioned for agent autonomy.

## Use Cases

- Signup + verification for agent tool accounts
- Autonomous notification handling
- Agent↔human async email communication
