# Scalekit

> **"Connect your agents to any tool. Authenticated, scoped, and logged."**

| | |
|---|---|
| **Website** | https://www.scalekit.com |
| **Docs** | https://docs.scalekit.com/agentkit/overview/ |
| **GitHub** | https://github.com/scalekit-inc/scalekit-sdk-python |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/scalekit-inc/scalekit-sdk-python?style=social)](https://github.com/scalekit-inc/scalekit-sdk-python) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **Integrations** | 500+ connectors, 20,000+ tools |
| **Enterprise** | SOC 2 Type II · HIPAA BAA · bring-your-own KMS key · VPC or self-hosted deployment |

This entry covers AgentKit, Scalekit's agent integration product.

---

## Official Website

https://www.scalekit.com

---

## Official Repo

https://github.com/scalekit-inc/scalekit-sdk-python

Also: [Node.js SDK](https://github.com/scalekit-inc/scalekit-sdk-node) · [AgentKit skills](https://github.com/scalekit-inc/authstack/tree/main/kits/agentkit/skills)

---

## How to Use (Agent Onboarding)

**Quickest verified path:**

`npx skills add scalekit-inc/authstack --skill integrate-agentkit`

Installs the AgentKit integration skill (create a connected account, authorize it, call a tool as the user) for Claude Code, Cursor, Codex, and other Agent Skills-compatible agents. To call tools from your own agent code instead, install an SDK (`pip install scalekit-sdk-python` or `npm install @scalekit-sdk/node`) and follow the [quickstart](https://docs.scalekit.com/agentkit/quickstart/).

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ✅ Official AgentKit skills published at [`scalekit-inc/authstack`](https://github.com/scalekit-inc/authstack/tree/main/kits/agentkit/skills)

```bash
npx skills add scalekit-inc/authstack --skill setup-agentkit integrate-agentkit discover-connectors expose-agentkit-mcp integrate-agentkit-host check-agentkit-prod
```

| Skill | What It Teaches the Agent |
|---|---|
| `setup-agentkit` | Configure a project with a Scalekit connection, environment credentials, and a first connector |
| `integrate-agentkit` | Create a connected account for a user, authorize it, then call a tool as that user |
| `discover-connectors` | Find connectors and their tools and schemas from the live catalog |
| `expose-agentkit-mcp` | Expose tools over a Virtual MCP server with a per-run session token |
| `integrate-agentkit-host` | Run AgentKit inside an always-on host (OpenClaw, Hermes) acting as a named user |
| `check-agentkit-prod` | Walk a go-live checklist before production |

**Compatibility:** Claude Code, Cursor, Codex, GitHub Copilot, and all [AgentSkills](https://agentskills.io/)-compatible tools.

---

## MCP

**Status:** ✅ Available

A **Virtual MCP server** is a URL that exposes the tools you choose, from one or more connections, to any MCP client. You create one per agent role (for example a support assistant) and all users share it; before each run you mint a session token bound to one user, so the agent calls tools with that user's credentials only. Every connection also has its own MCP server with all of its tools.

| Detail | Value |
|---|---|
| **MCP Docs** | https://docs.scalekit.com/agentkit/mcp/overview/ |
| **Transport** | Streamable HTTP |
| **Auth** | `Authorization: Bearer <session token>` — one user and one server per token, 60 seconds to 24 hours, optional read-only access level |
| **Compatible Clients** | Claude, Cursor, Windsurf, any MCP client ([HTTP contract](https://docs.scalekit.com/agentkit/mcp/connect-any-client/)) |

---

## What It Does

AgentKit, Scalekit's agent integration product, lets an AI agent act in third-party apps on behalf of each user. A user connects Gmail, Slack, Salesforce, GitHub or any of 500+ connectors once through an authorization link; Scalekit stores and refreshes their tokens (OAuth 2.0, API keys, RSA key pairs, Basic and bearer credentials) in an encrypted, per-tenant token vault that can use the customer's own KMS key, and the agent calls 20,000+ prebuilt tools as that user through the SDKs, the REST API, or a Virtual MCP server. Admins decide which tools each agent role sees, and every tool call is logged for audit and can be streamed to a SIEM.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Connect your agents to any tool. Authenticated, scoped, and logged."* Docs: *"AgentKit lets your AI agent act in third-party apps on behalf of each of your users."* ([overview](https://docs.scalekit.com/agentkit/overview/)) |
| **Agent-specific primitive** | Virtual MCP servers scoped per agent role; per-run session tokens bound to one user; read-only tokens that strip write tools from the agent's tool list ([MCP overview](https://docs.scalekit.com/agentkit/mcp/overview/), [read-only tokens](https://docs.scalekit.com/agentkit/mcp/read-only-tokens/)) |
| **Autonomy-compatible control plane** | After one-time consent, tools run with no per-call confirmation; Scalekit refreshes tokens, and an `EXPIRED` account tells the agent to send a new authorization link ([concepts](https://docs.scalekit.com/agentkit/concepts/)) |
| **M2M integration surface** | Python and Node.js SDKs, REST API with OAuth 2.0 client credentials, Virtual MCP over Streamable HTTP, account-event webhooks, Agent Skills |
| **Identity / delegation** | The calling app authenticates with its own client credentials; each user is a separate `identifier` with their own connected accounts; every tool call is logged with tool, connection, connected account and identifier ([security](https://docs.scalekit.com/agentkit/security/)) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Connected account** | One user's authorized link to one app, keyed by an `identifier` you choose; statuses tell the agent when the user must reconnect |
| **Authorization link** | Hosted consent page (OAuth or credential form, with scope choices) the agent sends a user who hasn't connected yet |
| **Tool execution** | `execute_tool` runs a prebuilt tool as the user; the API proxy calls any endpoint of a connector's API as the user |
| **Virtual MCP server** | Admin-defined tool bundle for one agent role, shared by all users, exposing only the listed tools |
| **Session token** | Per-run bearer token bound to one user and one MCP server, 60 seconds to 24 hours, full or read-only |
| **Tool call logs** | Per-call record of tool, connection, connected account, identifier, status, error code and duration; streamable to a SIEM |

---

## Autonomy Model

**Without Scalekit:** the agent ships with shared API keys or hand-built OAuth flows per app, sees every tool it was given, and fails mid-run when a token expires.

**With Scalekit:**
1. An admin creates a Virtual MCP server for the agent's role with only the tools it needs.
2. Before a run, the app checks the user's connected accounts; if one isn't `ACTIVE`, the agent sends the user an authorization link.
3. The app mints a session token for that user (read-only if the run only needs to read).
4. The agent connects any MCP client with the token and calls tools as that user — no per-call human confirmation; Scalekit refreshes the underlying credentials.
5. If tokens can't be refreshed, the account moves to `EXPIRED` and the agent asks the user to reconnect.

---

## Identity and Delegation Model

- The agent's application authenticates to Scalekit with its own OAuth 2.0 client credentials; end users are separate `identifier`s with their own connected accounts
- What the agent may do for a user is the intersection of the scopes that user granted, the tools on its Virtual MCP server, and the session token's access level
- Session tokens are bound to one user, so one user's run can't act with another user's credentials
- User verification confirms the person who authorized a connection is the user the app intended
- Tokens stay in the vault and are injected at call time — not in agent code, logs, or the LLM context
- Every tool call is logged and can be streamed to a SIEM

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `scalekit-sdk-python` — tools, connected accounts, authorization links, MCP session tokens; LangChain and Google ADK adapters |
| Node.js SDK | `@scalekit-sdk/node` |
| REST API | OAuth 2.0 client credentials; [OpenAPI spec](https://docs.scalekit.com/api/agentkit.scalar.json) |
| MCP | Virtual MCP servers and per-connection MCP servers over Streamable HTTP |
| Webhooks | Connected-account events; triggers (beta) |
| Agent Skills | `npx skills add scalekit-inc/authstack --skill setup-agentkit integrate-agentkit discover-connectors expose-agentkit-mcp integrate-agentkit-host check-agentkit-prod` |
| Framework guides | LangChain, LangGraph, Google ADK, OpenAI Agents SDK, Anthropic, Vercel AI SDK, Mastra, CrewAI |

---

## Human-in-the-Loop Support

A user consents once per app through the authorization link and chooses the scopes they grant; user verification can confirm it was the intended person. After that, tool calls run without human interaction. Write access can be withheld per run with read-only session tokens, and the agent asks the user to reconnect only when credentials can no longer be refreshed.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Hardcoded API keys / shared service accounts** | One credential for every user; no per-user scoping and no record of which user an agent acted for |
| **Hand-rolled OAuth per app** | Each integration needs its own consent flow, token storage and refresh code; nothing limits which tools an agent run can call |
| **Zapier / Make** | Human-facing workflow builders configured in a UI; no per-run session tokens, role-scoped tool lists, or read-only agent runs |

---

## Use Cases

- **Customer-facing assistants** — an agent reads and sends email, updates the CRM, and posts to Slack as each user, with that user's own credentials
- **Team agents with scoped tools** — a support agent's Virtual MCP server exposes only Zendesk and Slack tools, while a sales agent's exposes only CRM tools
- **Read-only research runs** — the same server serves a read-only token so an analysis agent can't send, create, or delete anything
- **Regulated deployments** — audit logs streamed to a SIEM, HIPAA BAA, bring-your-own KMS key, and VPC or self-hosted deployment
