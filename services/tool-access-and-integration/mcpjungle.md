# MCPJungle

> **"Run all your MCP servers behind one endpoint"**

| | |
|---|---|
| **Website** | https://docs.mcpjungle.com |
| **Docs** | https://docs.mcpjungle.com |
| **GitHub** | https://github.com/mcpjungle/MCPJungle |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/mcpjungle/MCPJungle?style=social)](https://github.com/mcpjungle/MCPJungle) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | **MPL-2.0** (OSI-approved; not MIT/Apache) |
| **Latest-month signal** | Last GitHub push **2026-08-02** ([repo metadata](https://api.github.com/repos/mcpjungle/MCPJungle)) — quieter than neighboring gateways; docs site and Docker Compose path still live as of 2026-09-03 |
| **Verified at** | 2026-09-03 |

---

## Official Website

https://docs.mcpjungle.com

Docs H1 quote (live 2026-09-03): **"Run all your MCP servers behind one endpoint"**

AI clients can also read the docs via MCP at `https://docs.mcpjungle.com/mcp`.

---

## Official Repo

https://github.com/mcpjungle/MCPJungle

README repeats the same H1. GitHub description: **"One place to manage & connect to all your MCP servers"**

**License:** Mozilla Public License 2.0 — OSI-approved copyleft (file-level), not MIT or Apache-2.0. Disclose that to operators who need a permissive relicensing story.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + MCP gateway

```bash
curl -O https://raw.githubusercontent.com/mcpjungle/MCPJungle/refs/heads/main/docker-compose.yaml
docker compose up -d
brew install mcpjungle/mcpjungle/mcpjungle
mcpjungle register --name context7 --url https://mcp.context7.com/mcp
```

Default Streamable HTTP endpoint: `http://localhost:8080/mcp`. Claude Desktop example uses `npx mcp-remote http://localhost:8080/mcp --allow-http`.

Enterprise mode (`mcpjungle start --enterprise` or `SERVER_MODE=enterprise`) then `mcpjungle init` writes an admin token to `~/.mcpjungle.conf` and mints per-client bearer tokens.

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

```bash
npx clawhub@latest search mcpjungle
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — the gateway **is** one MCP endpoint

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/mcpjungle/MCPJungle |
| **Transport** | Streamable HTTP at `/mcp` (stdio and remote upstreams register behind it) |
| **Compatible Clients** | Claude, Cursor, Codex, Copilot, custom agents |
| **Docs MCP** | `https://docs.mcpjungle.com/mcp` (documentation only) |

---

## What It Does

MCPJungle is a **self-hosted MCP gateway** for a personal laptop or a team: register stdio and remote MCP servers once, then every client connects to a single `/mcp`. Tool groups expose curated subsets. Development mode is open; **enterprise mode** adds per-client tokens, server-level ACLs, and observability hooks. Upstream static bearer tokens are injected by the gateway (`--bearer-token`); OAuth to upstreams is documented as coming soon.

Last code push as of verification: **2026-08-02**. Still listed because the docs, Compose file, and H1 positioning remain agent-native; operators should note the quieter cadence versus MCPHub/ContextForge.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [MCPHub](mcphub.md) | Node/Docker hub with `$smart` vector routing, dashboard-first ops, Apache-2.0 |
| [ContextForge](contextforge.md) | MCP + A2A + REST/gRPC + UAID |
| [MCP Gateway & Registry](mcp-gateway-registry.md) | Org IdP, virtual MCP, 3LO, skill scanning |
| [ToolHive](toolhive.md) | Secure container runtime |
| [Toolport](toolport.md) | Local stdio meta-tools + keychain |
| [Obot](obot.md) | Hosting + registry + chat client |

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs/README H1: **"Run all your MCP servers behind one endpoint"** — [docs.mcpjungle.com](https://docs.mcpjungle.com), [repo](https://github.com/mcpjungle/MCPJungle). Copy: Claude, Cursor, Codex, or **your own agents** connect to one MCP URL |
| **Agent-specific primitive** | Single `/mcp` over many registered servers; tool groups; enterprise per-client tokens |
| **Autonomy-compatible control plane** | After register (+ token in enterprise), agents call tools with no UI click |
| **M2M integration surface** | Docker Compose, `mcpjungle` CLI, HTTP `/mcp`, HTTP API, docs MCP |
| **Identity / delegation** | Dev mode is open (local trust). **Enterprise:** admin init token in `~/.mcpjungle.conf`; `mcpjungle create client` mints `Authorization: Bearer` tokens and optional custom tokens from an identity server. Upstream SaaS tokens stay in the gateway. OAuth *to* upstreams is not shipped yet |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **One `/mcp` endpoint** | Streamable HTTP for every client |
| **Server registry** | stdio + remote MCP, CLI `register` |
| **Tool groups** | Curated tool subsets per client |
| **Enterprise client token** | Per-client bearer; optional `--access-token` |
| **Upstream bearer inject** | `--bearer-token` on register |
| **Local vs enterprise mode** | Open laptop vs shared-team ACLs |

---

## Autonomy Model

```
docker compose up -d → mcpjungle register <server>
    -> Agent connects to http://localhost:8080/mcp
    -> (Enterprise) agent sends the minted bearer token
    -> Gateway routes tools/prompts/resources; dashboard optional
```

---

## Identity and Delegation Model

- **Development:** no client auth — treat as a trusted local endpoint.
- **Enterprise:** admin user + per-client tokens; which servers a client may reach is explicit.
- **Upstream secrets:** stored on the gateway, not in every IDE config.
- **Custom tokens:** `--access-token` / `access_token_ref` for an external identity server.
- **C5 note:** solid in enterprise mode; weak in default local mode (intentional).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Docker Compose | default `:8080/mcp` + Postgres |
| CLI | `mcpjungle register`, `start --enterprise`, `init`, client create |
| HTTP MCP | Streamable HTTP `/mcp` |
| HTTP API | documented on docs.mcpjungle.com |
| License | MPL-2.0 |

---

## Human-in-the-Loop Support

Optional dashboard UI. Tool calls on `/mcp` do not require a click. Admin creates clients and tool groups in enterprise mode (README: only admin can create tool groups today).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **MCPHub** | Different stack (Node hub, `$smart`, Apache-2.0). MCPJungle is Go/Compose + MPL + enterprise client tokens |
| **ContextForge / MCP Gateway & Registry** | Protocol federation + UAID, or org IdP registry — not this one-`/mcp` team gateway |
| **ToolHive / Toolport / Obot** | Runtime, local stdio hub, or chat+hosting platform |
| **nginx alone** | No MCP registry, tool groups, or enterprise client tokens |

---

## Use Cases

- **Clean local MCP** — one endpoint instead of per-client server lists
- **Team gateway** — enterprise tokens and server ACLs
- **Hide SaaS MCP keys** — upstream bearer stays on the gateway
- **MPL shops** — OSI license that is not MIT/Apache
