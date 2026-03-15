# Infisical Agent Sentinel

> **"Secrets and credential governance for AI agents."**

| | |
|---|---|
| **Website** | https://infisical.com |
| **Agent Docs** | https://infisical.com/docs/infisical-agent/overview |
| **GitHub** | https://github.com/Infisical/infisical |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |

---

## Official Website

https://infisical.com

---

## Official Repo

https://github.com/Infisical/infisical — Core platform

https://github.com/Infisical/infisical-mcp-server — Official MCP server

---

## Skills

| Skill | Description |
|---|---|
| **Dynamic Secret Generation** | Create temporary, time-bounded credentials on demand — never static long-lived secrets |
| **Token Lifecycle Management** | Automatically renew access tokens before expiration via the agent daemon |
| **Templated Secret Delivery** | Render secrets in Go templates and deliver as formatted config files or env vars |
| **Policy-Scoped Access** | Define which secrets each agent class can access via access policies |
| **JIT Credential Access** | Generate just-in-time credentials that expire automatically after use |
| **Secret CRUD** | Create, read, update, and delete secrets and environments via API |
| **Project Management** | Create projects, environments, and folders programmatically |

---

## MCP

**Status:** ✅ Available

Infisical provides an official MCP server (`@infisical/mcp`) that exposes secrets management operations — including CRUD on secrets, project management, and environment operations — as MCP tools.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/Infisical/infisical-mcp-server |
| **NPM Package** | `@infisical/mcp` |
| **Transport** | stdio (run via `npx -y @infisical/mcp`) |
| **Compatible Clients** | Claude Desktop, Cursor, any MCP-compatible client |
| **Auth** | `INFISICAL_UNIVERSAL_AUTH_CLIENT_ID` + `INFISICAL_UNIVERSAL_AUTH_CLIENT_SECRET` |

---

## What It Does

Infisical Agent Sentinel governs how AI agents access external tools and services by centralizing authentication and policy enforcement. The Infisical Agent daemon runs alongside the agent process, manages token lifecycle and automatic renewal, and delivers secrets to the agent at runtime — without the secrets ever appearing in agent code or environment variables. Agent Sentinel specifically extends this to govern *AI agent* access to tools and APIs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Agent Sentinel is a dedicated product for AI agent credential governance, explicitly named as distinct from the developer-facing secret manager |
| **Agent-specific primitive** | Dynamic credential generation (just-in-time, time-bounded secrets); per-agent policy enforcement; token lifecycle managed by a daemon sidecar |
| **Autonomy-compatible control plane** | Agent daemon renews tokens automatically; agents access secrets at runtime without human rotation or re-authentication |
| **M2M integration surface** | Daemon sidecar, REST API, templated secret delivery |
| **Identity / delegation** | Just-in-time credentials with automatic expiration; access policies scoped per agent |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Token Lifecycle Management** | Daemon automatically renews access tokens before expiration |
| **Dynamic Secret Generation** | Create temporary, time-bounded credentials on demand — never static long-lived secrets |
| **Templated Secret Delivery** | Secrets rendered in Go templates and delivered as formatted files or env vars |
| **Per-Agent Policy** | Access policies define which secrets each agent can retrieve |
| **Agent Sentinel** | Governance layer controlling how AI agents access tools and external systems |

---

## Autonomy Model

```
Infisical Agent daemon starts alongside agent process
    ↓
Daemon authenticates with Infisical using machine identity
    ↓
Agent requests secret: daemon fetches from Infisical, renders template, deposits at path
    ↓
Daemon continuously renews tokens before expiration
    ↓
If token expires: daemon re-authenticates and renews automatically
    ↓
Agent never sees raw credentials — only rendered output at the configured path
```

---

## Identity and Delegation Model

- **Machine Identity** — daemon authenticates using a non-human identity (not a developer's username/password)
- **Dynamic secrets** — credentials expire automatically, eliminating the need for human rotation cycles
- **JIT (Just-In-Time) access** — secrets are generated only when needed, reducing the exposure window
- **Policy-scoped access** — each agent's daemon is granted access only to the secrets it needs

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Agent Daemon | Sidecar process managing authentication, renewal, and delivery |
| REST API | Secret retrieval and lifecycle management |
| Go Templates | Secret rendering for environment files, config files, and custom formats |
| SDK | Native language clients for inline secret fetching (when daemon is not used) |

---

## Human-in-the-Loop Support

Policy definition is a human activity (operator defines which secrets each agent class can access). Runtime secret management is fully autonomous — no human rotates credentials or re-authenticates the agent.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Static `.env` files** | Secrets are long-lived, human-managed, often leaked; no automatic rotation or expiration |
| **AWS Secrets Manager (bare)** | Provides secret storage but requires application code to handle retrieval, rotation, and error handling |
| **HashiCorp Vault** | Powerful but requires significant human configuration and integration; not purpose-built for AI agent sidecar deployment |
| **Hardcoded API keys** | No expiration, no rotation, maximum blast radius on compromise |

---

## Use Cases

- **Production agent deployments** — agents in containers or VMs that need credentials refreshed continuously without operator intervention
- **Multi-tenant agent platforms** — each agent tenant gets isolated, dynamically-generated credentials scoped to their resources
- **Regulated environments** — financial, healthcare, or government agents requiring just-in-time credential access and full audit trails
- **CI/CD agent pipelines** — automated agents that need short-lived credentials for each pipeline run
