# MetaMCP

> **"MCP Aggregator, Orchestrator, Middleware, Gateway in one docker"**

| | |
|---|---|
| **Website** | https://docs.metamcp.com |
| **Docs** | https://docs.metamcp.com |
| **GitHub** | https://github.com/metatool-ai/metamcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/metatool-ai/metamcp?style=social)](https://github.com/metatool-ai/metamcp) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push **2026-06-22** ([repo metadata](https://api.github.com/repos/metatool-ai/metamcp)) — quieter than MCPHub/ContextForge; default branch `ai-dev`. README notes maintenance delay while still merging PRs. Still admitted: MIT + clear MCP aggregator/gateway OSS not already listed |
| **Verified at** | 2026-09-04 |

---

## Official Website

https://docs.metamcp.com

Docs H1 area (live 2026-09-04): **“MetaMCP Documentation”** with tagline **“MCP Aggregator, Orchestrator, Middleware, Gateway in one docker”**.

---

## Official Repo

https://github.com/metatool-ai/metamcp

README title (live 2026-09-04): **“MetaMCP (MCP Aggregator, Orchestrator, Middleware, Gateway in one docker)”**

GitHub description matches that tagline exactly. Body: “MetaMCP is a MCP proxy that lets you dynamically aggregate MCP servers into a unified MCP server, and apply middlewares. MetaMCP itself is a MCP server so it can be easily plugged into ANY MCP clients.”

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + MCP gateway

```bash
git clone https://github.com/metatool-ai/metamcp.git
cd metamcp
cp example.env .env
docker compose up -d
```

Create a namespace + endpoint in the UI (or API), then point an MCP client at the Streamable HTTP or SSE URL with `Authorization: Bearer sk_mt_...`.

Cursor `mcp.json` uses the MetaMCP endpoint URL. STDIO-only clients (Claude Desktop) go through `mcp-proxy` (not `mcp-remote` — MetaMCP auth is API-key, not OAuth-to-upstream).

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

```bash
npx clawhub@latest search metamcp
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — the product **is** a meta-MCP server

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/metatool-ai/metamcp |
| **Transport** | Streamable HTTP (standard remote); SSE (compat); STDIO via `mcp-proxy` |
| **Auth** | API keys `sk_mt_...` (`Authorization: Bearer`); session cookies for the dashboard; optional OIDC SSO |
| **Compatible Clients** | Cursor, Claude Desktop (via proxy), Open WebUI (OpenAPI), any MCP client |
| **Docs index** | https://docs.metamcp.com/llms.txt |

---

## What It Does

MetaMCP is a **self-hosted MCP proxy**: register MCP servers, group them into **namespaces**, apply **middleware**, and host them as one meta-MCP with public SSE or Streamable HTTP endpoints. Tool cherry-picking, an inspector, API-key and OIDC auth, multi-tenancy (public/private scopes), and OpenAPI for Open WebUI ship in one Docker Compose stack.

Last code push as of verification: **2026-06-22**. Still listed because the docs, Compose path, MIT license, and H1 positioning remain agent-native; operators should note the quieter cadence versus [MCPHub](mcphub.md) / [ContextForge](contextforge.md).

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [MCPHub](mcphub.md) | Node hub with `$smart` vector routing, Apache-2.0, active 2026-09 |
| [MCPJungle](mcpjungle.md) | Go/Compose one-`/mcp` + enterprise tokens, MPL-2.0 |
| [ContextForge](contextforge.md) | IBM federation of MCP + **A2A + REST/gRPC** + UAID |
| [MCP Gateway & Registry](mcp-gateway-registry.md) | Org IdP, virtual MCP, 3LO, skill scanning |
| [ToolHive](toolhive.md) | Secure **container runtime** for launching MCP servers |
| [Toolport](toolport.md) | Local stdio meta-gateway + OS keychain |
| [Obot](obot.md) | Full MCP platform **plus chat client** |
| Hosted [MCP Gateway](mcpgateway.md) | Commercial one-URL tools/skills/sandboxes |

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs/README/GitHub: **“MCP Aggregator, Orchestrator, Middleware, Gateway in one docker”** — [docs.metamcp.com](https://docs.metamcp.com), [repo](https://github.com/metatool-ai/metamcp). “plugged into ANY MCP clients.” |
| **Agent-specific primitive** | Namespaces as meta-MCPs; middleware around tool lists; public endpoints with API keys; tool overrides/annotations |
| **Autonomy-compatible control plane** | After namespace + `sk_mt_` key, agents call tools through the endpoint with no dashboard click |
| **M2M integration surface** | Docker Compose, Streamable HTTP / SSE MCP, OpenAPI, API keys |
| **Identity / delegation** | Per-user API keys; public vs private scopes; OIDC for dashboard SSO; public keys cannot reach private MetaMCPs |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Namespace** | Group of MCP servers hosted as one meta-MCP |
| **Endpoint** | Public SSE or Streamable HTTP URL + auth |
| **Middleware** | Transform tool lists / requests / responses |
| **Tool overrides** | Cherry-pick and annotate tools when remixing servers |
| **API key** | `sk_mt_...` bearer for agents |
| **OIDC** | Optional enterprise SSO for operators |

---

## Autonomy Model

```
Operator docker compose up -d, registers MCP servers into a namespace
    -> Issues an API key for the agent
    -> Agent connects to the Streamable HTTP / SSE endpoint
    -> MetaMCP aggregates, applies middleware, routes tool calls
    -> Dashboard / inspector stay off the data path
```

---

## Identity and Delegation Model

- **Agent callers:** `Authorization: Bearer sk_mt_...` (query `?api_key=` works for Streamable HTTP/OpenAPI only, not SSE).
- **Scopes:** public vs private MetaMCPs; public keys cannot access private ones.
- **Dashboard users:** session cookies; optional OIDC (Auth0, Keycloak, Azure AD).
- **Upstream secrets:** stored with the registered MCP server config, not in every client `mcp.json`.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Docker Compose | recommended path (`example.env`) |
| HTTP MCP | Streamable HTTP + SSE |
| OpenAPI | Open WebUI-compatible |
| STDIO clients | `mcp-proxy` + API key |
| License | MIT |
| Cadence | Last push 2026-06-22 |

---

## Human-in-the-Loop Support

Web UI for namespaces, inspector, and registration. Tool calls on the meta-MCP endpoint do not require a click. OIDC/SSO is an operator login, not per-tool approval.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **MCPHub / MCPJungle** | Different stacks (Node `$smart` hub; Go enterprise tokens). MetaMCP is namespace+middleware+inspector in one Docker |
| **ContextForge / MCP Gateway & Registry** | Protocol federation + UAID, or org IdP registry |
| **ToolHive / Toolport / Obot** | Runtime, local stdio hub, or chat+hosting platform |
| **nginx alone** | No MCP namespace, middleware, or tool remix |

---

## Use Cases

- **One meta-MCP URL** — Cursor/Claude share a remixed tool set
- **Cherry-pick tools** — hide noisy upstream tools via middleware
- **Self-host with MIT** — Compose + API keys + optional OIDC
- **Open WebUI** — OpenAPI endpoint in front of MCP servers
