# Nango

> **"The OAuth and API credential layer for AI agents."**

| | |
|---|---|
| **Website** | https://nango.dev |
| **Docs** | https://docs.nango.dev |
| **GitHub** | https://github.com/NangoHQ/nango |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **Integrations** | 700+ external APIs |

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
