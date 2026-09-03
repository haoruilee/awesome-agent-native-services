# MCPHub

> **"One gateway for all your MCP servers."**

| | |
|---|---|
| **Website** | https://www.mcphub.app |
| **Docs** | https://docs.mcphub.app/ |
| **GitHub** | https://github.com/samanhappy/mcphub |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/samanhappy/mcphub?style=social)](https://github.com/samanhappy/mcphub) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-09-03 ([repo metadata](https://api.github.com/repos/samanhappy/mcphub)); Docker `samanhappy/mcphub`; demo https://demo.mcphub.app/ |
| **Verified at** | 2026-09-03 |

---

## Official Website

https://www.mcphub.app

Homepage H1 (live 2026-09-03): **"One gateway for all your MCP servers."** Supporting line: “Connect, organize, control, and operate your MCP servers through a self-hosted unified gateway.”

---

## Official Repo

https://github.com/samanhappy/mcphub

README lead: **"A self-hosted MCP gateway and management platform for connecting, managing, and operating MCP servers."** GitHub description matches that sentence.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + MCP gateway

```bash
docker run -p 3000:3000 \
  -v ./mcp_settings.json:/app/mcp_settings.json \
  -v ./data:/app/data \
  samanhappy/mcphub
```

Point an MCP client at a stable URL (auth on by default):

```
http://localhost:3000/mcp           # all servers
http://localhost:3000/mcp/{group}   # group
http://localhost:3000/mcp/{server}  # one server
http://localhost:3000/mcp/$smart    # semantic tool discovery
```

CLI against a running hub: `mcphub login --url http://localhost:3000 --username admin` then `mcphub servers add …` / `mcphub call …`. Headless: `DISABLE_WEB=true`. First-run admin password is random in logs unless `ADMIN_PASSWORD` is set.

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

```bash
npx clawhub@latest search mcphub
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — the product **is** the gateway

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/samanhappy/mcphub |
| **Transport** | Streamable HTTP (and SSE) at `/mcp`, `/mcp/{group}`, `/mcp/{server}`, `/mcp/$smart` |
| **Compatible Clients** | Claude Desktop, Claude Code, Cursor, Cline, Continue, Windsurf, Zed, Cherry Studio, OpenWebUI, custom agents |
| **Upstreams** | stdio, SSE, Streamable HTTP MCP servers |

---

## What It Does

MCPHub is a **self-hosted MCP gateway**: register local and remote MCP servers once, then expose **stable endpoints** with groups, aliases, bearer/OAuth auth, health checks, logs, hot-reload, optional PostgreSQL + pgvector **smart routing**, and tool-result compression. The dashboard is an operator surface; `DISABLE_WEB=true` leaves API + MCP only.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [ContextForge](contextforge.md) | IBM federation of MCP + **A2A + REST/gRPC** with UAID. MCPHub is MCP-only connect/organize/control/operate |
| [MCP Gateway & Registry](mcp-gateway-registry.md) | Enterprise IdP registry (Keycloak/Entra), virtual MCP, 3LO egress, skill scanning |
| [ToolHive](toolhive.md) | Secure **container runtime** for launching MCP servers |
| [Toolport](toolport.md) | Local stdio meta-gateway + OS keychain — not a hosted/self-hosted HTTP hub |
| [Obot](obot.md) | Full MCP platform **plus chat client** |
| Hosted [MCP Gateway](mcpgateway.md) | Commercial one-URL tools/skills/sandboxes (`mcpgateway-sdk`) |

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage H1: **"One gateway for all your MCP servers."** — [mcphub.app](https://www.mcphub.app). README: unified endpoints for Claude Code, Cursor, and other MCP-compatible applications |
| **Agent-specific primitive** | One MCP URL over many backends; `$smart` semantic tool discovery; group/server routes; OAuth 2.0 client+server modes |
| **Autonomy-compatible control plane** | After register + token, agents call tools through `/mcp` with no dashboard click. Hot-swap config without downtime |
| **M2M integration surface** | Docker, `mcphub` CLI, HTTP MCP, REST/API, marketplace `discover`/`install` |
| **Identity / delegation** | JWT + bcrypt local users; **bearer keys**; OAuth 2.0 (client and server); server/group visibility. MCP auth is **on by default**. Social login (GitHub/Google) is optional dashboard SSO (Better Auth, database mode) — not the agent data-plane identity |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Unified `/mcp`** | Aggregate, group, single-server, or `$smart` routes |
| **Server groups / aliases** | Per-team or per-project tool subsets |
| **Smart routing** | Vector index over tool descriptions |
| **Bearer + OAuth** | Keys for agents; OAuth 2.0 for clients and upstreams |
| **Hot-swappable config** | `mcp_settings.json` or PostgreSQL — no restart required |
| **Health + logs** | Per-server status, latency, tool-call inspect |

---

## Autonomy Model

```
Operator starts Docker (or pnpm) and registers MCP servers
    -> Issues a bearer key (or OAuth client) for the agent
    -> Agent connects to http://localhost:3000/mcp (or $smart / group)
    -> Gateway routes, meters, and logs; dashboard is optional
```

---

## Identity and Delegation Model

- **Agent callers:** bearer keys (`mcphub keys create`) or OAuth tokens on the MCP endpoints.
- **Upstream credentials:** stored in hub config / DB — not in every client’s `mcp.json`.
- **Visibility:** server and group ACLs decide which tools a key can see.
- **Dashboard users** (admin / social login) are a separate control-plane identity.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Docker | `samanhappy/mcphub` (`latest` / `latest-full`) |
| HTTP MCP | `/mcp`, `/mcp/{group}`, `/mcp/{server}`, `/mcp/$smart` |
| CLI | `mcphub login`, `servers`, `tools`, `call`, `discover`, `install` |
| Config | `mcp_settings.json` or PostgreSQL (database mode) |
| Dashboard | `:3000` — optional (`DISABLE_WEB=true`) |

---

## Human-in-the-Loop Support

Web UI for connect/organize/operate. Data-plane tool calls do not require a click. First-time OAuth to an upstream may need a human browser once.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **ContextForge** | MCP+A2A+REST/gRPC federation + UAID — different protocol claim |
| **MCP Gateway & Registry** | Org IdP / 3LO / skill admission registry |
| **ToolHive** | Container runtime, not a multi-route HTTP hub with `$smart` |
| **Toolport / Obot / hosted MCP Gateway** | Local stdio hub, chat+hosting platform, and commercial one-URL SaaS respectively |
| **A generic reverse proxy** | No MCP tool index, smart routing, or group ACLs |

---

## Use Cases

- **One URL for every IDE** — Claude, Cursor, Cline share the same hub
- **Semantic tool pick** — `$smart` returns a small matching set
- **Self-hosted MCP ops** — health, logs, hot-reload, optional Postgres
- **CI tool calls** — `mcphub call … --json` with a scoped key
