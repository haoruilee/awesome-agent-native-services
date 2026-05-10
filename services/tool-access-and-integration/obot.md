# Obot

> **"Complete MCP Platform — Hosting, Registry, Gateway, and Chat Client."**

| | |
|---|---|
| **Website** | https://obot.ai |
| **Docs** | https://docs.obot.ai |
| **GitHub** | https://github.com/obot-platform/obot |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration](README.md) |
| **License** | Apache 2.0 |
| **Stars** | 763+ (and growing fast through 2026) |

---

## Official Website

https://obot.ai

---

## Official Repo

https://github.com/obot-platform/obot

---

## How to Use (Agent Onboarding)

```
# Self-hosted (Kubernetes / Docker):
helm install obot obot/obot
# or:
docker run -p 8080:8080 ghcr.io/obot-platform/obot:latest

# Then point any MCP-compatible agent at the gateway URL:
https://<obot-host>/mcp
```

OAuth 2.1 onboarding is built in; agents authenticate with delegated, per-tenant scopes.

---

## Agent Skills

**Status:** ⚠️ Not yet published.

Search:

```bash
npx clawhub@latest search obot
```

---

## MCP

**Status:** ✅ Available — Obot **is** an MCP platform; everything it does is exposed over MCP.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/obot-platform/obot |
| **Transport** | Streamable HTTP |
| **Compatible Clients** | Claude Desktop, Cursor, Windsurf, any MCP-compatible runtime |

---

## What It Does

Obot is a single deployable that bundles four MCP-related concerns into one stack: **hosting** (run MCP servers in a managed sandbox — Node.js, Python, or container-based), **registry** (catalog and discover MCP servers and their tools), **gateway** (front everything with a unified URL with OAuth, RBAC, and usage policies), and an optional **chat client** (a generic agent UI that consumes the gateway).

For teams that want a private, in-cluster MCP plane — instead of stitching together Smithery for the registry, ToolHive for the runtime, and a hand-rolled gateway — Obot gives them all four in one repo with Kubernetes-ready Helm charts and OAuth 2.1 baked in.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repo tagline: *"Complete MCP Platform — Hosting, Registry, Gateway, and Chat Client"* — MCP is purely an agent protocol |
| **Agent-specific primitive** | Federated MCP gateway, per-agent OAuth scopes, sandboxed MCP server hosting with secrets isolation |
| **Autonomy-compatible control plane** | Agents call tools through one URL with policy enforcement; no human approval per call (configurable) |
| **M2M integration surface** | MCP (Streamable HTTP) + REST admin API + OAuth 2.1 |
| **Identity / delegation** | Per-agent OAuth tokens with scoped tool access; audit log per token |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **MCP Hosting** | Run MCP servers (Node, Python, container) in a managed sandbox |
| **MCP Registry** | Discover servers + tools by name, capability, or tag |
| **MCP Gateway** | Single URL fronting many servers with OAuth 2.1, RBAC, rate limits |
| **OAuth 2.1 for Agents** | Issue scoped tokens per agent; supports auth code + client credentials flows |
| **Chat Client** | Optional generic agent UI for testing the gateway |

---

## Autonomy Model

1. Operator deploys Obot to Kubernetes (or Docker for dev).
2. Operator installs MCP servers from the registry (or pushes private ones).
3. Agent obtains an OAuth token (per-tenant, per-scope) from the gateway.
4. Agent connects to the gateway URL via Streamable HTTP MCP.
5. Tool calls flow through the gateway, are policy-checked, and are dispatched to the right backing MCP server.

---

## Identity and Delegation Model

- Per-agent OAuth tokens with scoped capabilities (which servers, which tools, which tenants).
- RBAC at the gateway — group-based access control for fleets of agents.
- Audit log entries attribute every tool call to a token + agent + tenant.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP (Streamable HTTP) | Unified gateway URL for tool discovery + invocation |
| REST admin API | Server registration, token issuance, policy management |
| OAuth 2.1 | Auth code + client credentials flows |
| Helm chart / Docker image | Kubernetes-native deploy |

---

## Human-in-the-Loop Support

Policies at the gateway can require human approval (via webhook to HumanLayer or similar) for specific tool calls. Audit logs are designed for after-the-fact review.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Smithery** | Registry-first; less of a private hosting + gateway story for in-cluster deploys |
| **MCP Gateway (mcpgateway.com)** | Closed-source SaaS; Obot is fully open and self-hostable |
| **Plain reverse proxy + manual OAuth** | No MCP-aware policy plane, no built-in registry, no sandboxed hosting |

---

## Use Cases

- **Private MCP plane for an enterprise** — host all internal MCP servers with one OAuth domain, audit, and RBAC
- **Multi-tenant agent platforms** — issue scoped tokens to customer agents with per-tenant tool isolation
- **MCP server marketplace operator** — bundle registry + hosting + gateway for end users
