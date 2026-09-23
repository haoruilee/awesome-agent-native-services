# Communication Services

> Services that give AI agents a **first-class communication identity** on the internet — not a proxy to a human's mailbox or messaging account, but an identity the agent owns and operates autonomously.

## Why This Category Exists

Human communication infrastructure (Gmail, Outlook, Slack) was built around the assumption that a person is at each endpoint. An AI agent acting as an email correspondent, notification dispatcher, or asynchronous collaborator needs primitives that simply do not exist in human-facing systems: instant inbox provisioning, webhook-on-receive without polling, threaded context that feeds back into the agent's reasoning loop, and the ability to spin up thousands of independent communication identities in milliseconds.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [ATXP Email](atxp-email.md) | Email for AI agents | CLI, API docs, per-agent inbox workflow | ⚠️ |
| [AgentMail](agentmail.md) | Email for AI agents | REST, Python SDK, TypeScript SDK, Webhooks | ✅ |
| [Novu](novu.md) | Open-source notification infrastructure with Agent Toolkit | Node SDK, Python SDK, REST API, Agent Skills | ✅ |
| [Chimely](chimely.md) [![⭐](https://img.shields.io/github/stars/dodopayments/chimely?style=social)](https://github.com/dodopayments/chimely) | Self-hostable in-app notification inbox | HTTP API, Server-Sent Events, React `<Inbox />`, self-hosted Rust + Postgres + Redis | ⚠️ |
| [mails.dev](mails-dev.md) | Email for AI Agents | CLI, REST API, TypeScript SDK | ⚠️ |
| [OpenMail](openmail.md) | Email API for AI agents | REST API, WebSocket, Webhooks, CLI (`@openmail/cli`) | ⚠️ |
| [OutreachAgent](outreachagent.md) | The Cold Outbound Engine for AI Agents | REST API, TypeScript SDK, Webhooks; MCP documented but unpublished | ⚠️ |
| [MailboxKit](mailboxkit.md) | Email infrastructure for AI agents | REST API v1, Webhooks, URL Onboarding (`skill.md`) | ⚠️ |
| [Agents Mail](agents-mail.md) | Email for AI Agents | REST API, URL Onboarding (`skill.md`), `.well-known/agent.json` discovery | ⚠️ |
| [MCP Agent Mail](mcp-agent-mail.md) | Async coordination layer for AI coding agents | MCP tools/resources, FastMCP, Git + SQLite | ✅ |
| [MCP Agent Mail (Rust)](mcp-agent-mail-rust.md) | "Gmail for coding agents" with high-performance MCP runtime | MCP tools/resources, local HTTP runtime, TUI + robot CLI | ✅ |
| [AgenticMail](agenticmail.md) [![⭐](https://img.shields.io/github/stars/agenticmail/agenticmail?style=social)](https://github.com/agenticmail/agenticmail) | Email & SMS infrastructure for AI agents | REST API (75+ endpoints), self-hosted Stalwart + Google Voice bridge, Webhooks | ⚠️ |
| [Caspian](caspian.md) [![⭐](https://img.shields.io/github/stars/TryCaspian/caspian-sdk?style=social)](https://github.com/TryCaspian/caspian-sdk) | One agent communication identity across human channels | URL onboarding, Python/TypeScript SDKs, CLI, REST events, Webhooks | ⚠️ |
| [Atomic Mail](atomic-mail.md) [![⭐](https://img.shields.io/github/stars/Atomic-Mail/atomic-mail-agentic?style=social)](https://github.com/Atomic-Mail/atomic-mail-agentic) | Not AI for your email. Email for your AI. | Homepage onboarding, JMAP, local/hosted MCP, AgentSkill | ✅ |
| [AgentTeam Email](agentteam-email.md) [![⭐](https://img.shields.io/github/stars/agentteamhq/agentteam-email?style=social)](https://github.com/agentteamhq/agentteam-email) | Open-source email infrastructure for AI agents | `at-email` CLI, Agent Skill, self-host Compose/Helm, draft review | ⚠️ |
| [SendRaven](sendraven.md) | Email infrastructure for AI agents | REST API, OpenAPI, remote + stdio MCP, signed webhooks, per-key guardrails | ✅ |



---

## Criteria Reminder

To qualify for this category, a service must:

1. Give the agent **ownership** of a communication identity (not delegation to a human account).
2. Provide **webhook or push primitives** so the agent reacts to inbound events without polling.
3. Support **programmatic provisioning** — creating/deleting identities via API, not a human-facing UI.
4. Operate **headlessly** — no browser, no human sign-in, no OAuth consent flow per operation.
