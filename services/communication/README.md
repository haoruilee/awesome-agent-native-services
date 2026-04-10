# Communication Services

> Services that give AI agents a **first-class communication identity** on the internet — not a proxy to a human's mailbox or messaging account, but an identity the agent owns and operates autonomously.

## Why This Category Exists

Human communication infrastructure (Gmail, Outlook, Slack) was built around the assumption that a person is at each endpoint. An AI agent acting as an email correspondent, notification dispatcher, or asynchronous collaborator needs primitives that simply do not exist in human-facing systems: instant inbox provisioning, webhook-on-receive without polling, threaded context that feeds back into the agent's reasoning loop, and the ability to spin up thousands of independent communication identities in milliseconds.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [AgentMail](agentmail.md) | Email for AI agents | REST, Python SDK, TypeScript SDK, Webhooks | ✅ |
| [Novu](novu.md) | Open-source notification infrastructure with Agent Toolkit | Node SDK, Python SDK, REST API, Agent Skills | ✅ |
| [mails.dev](mails-dev.md) | Email for AI Agents | CLI, REST API, TypeScript SDK | ⚠️ |
| [OpenMail](openmail.md) | Email API for AI agents | REST API, WebSocket, Webhooks, CLI (`@openmail/cli`) | ⚠️ |
| [MailboxKit](mailboxkit.md) | Email infrastructure for AI agents | REST API v1, Webhooks, URL Onboarding (`skill.md`) | ⚠️ |

---

## Criteria Reminder

To qualify for this category, a service must:

1. Give the agent **ownership** of a communication identity (not delegation to a human account).
2. Provide **webhook or push primitives** so the agent reacts to inbound events without polling.
3. Support **programmatic provisioning** — creating/deleting identities via API, not a human-facing UI.
4. Operate **headlessly** — no browser, no human sign-in, no OAuth consent flow per operation.
