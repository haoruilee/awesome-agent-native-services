# Nango

> **"The OAuth and API credential layer for AI agents."**

| | |
|---|---|
| **Website** | https://nango.dev |
| **Docs** | https://docs.nango.dev |
| **GitHub** | https://github.com/NangoHQ/nango |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/NangoHQ/nango?style=social)](https://github.com/NangoHQ/nango) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **Integrations** | 700+ external APIs |

---

## Official Website

https://nango.dev

---

## Official Repo

https://github.com/NangoHQ/nango

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ✅ Official skills published by NangoHQ on the AgentSkills marketplace

```bash
$skills install @NangoHQ/sync-builder-skill
```

Or via the skills CLI:

```bash
npx skills add NangoHQ/sync-builder-skill
```

| Skill | What It Teaches the Agent |
|---|---|
| `sync-builder-skill` | Create and configure Nango syncs for continuous data synchronization from external APIs |
| `github-oauth-nango-integration` *(community)* | Set up GitHub OAuth and GitHub App authentication flows using Nango |

**Compatibility:** Claude Code, Cursor, Codex, and all [AgentSkills](https://agentskills.io/)-compatible tools.

> See all Nango skills at [agentskills.in/@NangoHQ](https://www.agentskills.in/es/marketplace/%40NangoHQ).

---

## MCP

**Status:** ✅ Available

Nango exposes a built-in MCP server that allows agents to connect to and interact with any of its 700+ integrations via the Model Context Protocol. Agents can call `mcp-generic` for any OAuth 2.0-compatible service with dynamic discovery.

| Detail | Value |
|---|---|
| **MCP Docs** | https://docs.nango.dev/guides/mcp |
| **MCP Generic** | https://nango.dev/docs/integrations/all/mcp-generic |
| **Transport** | stdio / HTTP |
| **Compatible Clients** | Claude Desktop, Cursor, OpenAI Agents SDK, any MCP-compatible client |

---

## What It Does

Nango manages OAuth authentication and credential lifecycle for 700+ external APIs so AI agents can access third-party services without ever handling tokens directly. Agents call `getConnection()` at runtime to receive a valid access token; Nango handles token storage, automatic refresh, and credential validation invisibly.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | First-class OpenAI Agents SDK integration guide; credential lifecycle is designed for agent-time retrieval, not human-time configuration |
| **Agent-specific primitive** | `getConnection()` — agent fetches valid credentials at runtime on demand; `createConnectSession()` — agent-initiated OAuth consent flow |
| **Autonomy-compatible control plane** | Tokens refresh automatically; agents never encounter expired credential errors mid-loop |
| **M2M integration surface** | Node SDK, REST API, MCP-compatible patterns |
| **Identity / delegation** | Per-connection credential isolation; one connection = one user's credentials for one API |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Connect Session** | Hosted OAuth consent flow that agent triggers during conversation |
| **`getConnection()`** | Agent fetches valid credentials for a specific user + API combination at runtime |
| **Automatic Token Refresh** | Credentials remain valid across agent sessions without manual intervention |
| **Connection Management** | Each connection stores one user's credentials for one external API |
| **Auth Observability** | Logged authorization attempts, connection diagnostics, credential failure detection |

---

## Autonomy Model

1. User connects their account once via a Connect Session (one-time OAuth consent)
2. Agent calls `nango.getConnection(integrationId, userId)` at runtime
3. Nango returns a valid, refreshed access token
4. Agent makes the API call using the token
5. If the token expires between calls, Nango refreshes it automatically — the agent never sees an auth error

---

## Identity and Delegation Model

- One `Connection` = one user's credentials for one external API
- Multiple users × multiple APIs → fully isolated connection matrix
- Credentials are stored by Nango; they never appear in agent code or logs
- Nango handles the OAuth state machine (PKCE, token exchange, refresh, revocation)

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Node.js SDK | `@nangohq/node` — `getConnection()`, `createConnectSession()` |
| REST API | Full connection management and credential retrieval |
| OpenAI Agents SDK | First-class integration guide and example |
| MCP-compatible | Patterns work with MCP-based agent frameworks |

---

## Human-in-the-Loop Support

One-time OAuth consent per user per API. After that, all token management is autonomous. Agents never need to re-authenticate unless the user explicitly revokes access.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Hardcoded API keys** | Static secrets that expire, leak, and cannot be per-user scoped |
| **Passport.js** | Human-facing OAuth middleware for web apps; no concept of agent-runtime credential retrieval |
| **Auth0** | User identity platform for human login flows; not designed for per-agent credential scoping at runtime |
| **Manual OAuth flow** | Requires human browser session for consent; token refresh must be coded manually |

---

## Use Cases

- **Productivity agents** — agent calls Google Calendar, Gmail, Notion, GitHub with per-user tokens fetched at runtime
- **Multi-tenant SaaS agents** — one agent deployment serves thousands of users with fully isolated credentials per user
- **Enterprise automation** — agent accesses Salesforce, HubSpot, Jira on behalf of enterprise users with automatic token refresh
