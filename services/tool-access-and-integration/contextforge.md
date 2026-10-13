# ContextForge

> **"An open source registry and proxy that federates MCP, A2A, and REST/gRPC APIs with centralized governance, discovery, and observability. Optimizes Agent & Tool calling, and supports plugins."**

| | |
|---|---|
| **Website** | https://ibm.github.io/mcp-context-forge/ |
| **Docs** | https://ibm.github.io/mcp-context-forge/ |
| **GitHub** | https://github.com/IBM/mcp-context-forge |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/IBM/mcp-context-forge?style=social)](https://github.com/IBM/mcp-context-forge) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-08-25 ([repo metadata](https://api.github.com/repos/IBM/mcp-context-forge)); PyPI `mcp-contextforge-gateway`; image `ghcr.io/ibm/mcp-context-forge` |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://ibm.github.io/mcp-context-forge/

---

## Official Repo

https://github.com/IBM/mcp-context-forge

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + MCP gateway

```bash
# Generate secrets, then start the gateway (official README TLDR)
python3 -m mcpgateway.scripts.init_secrets
export JWT_SECRET_KEY="$(grep '^JWT_SECRET_KEY=' .env.secrets | cut -d= -f2)"
export AUTH_ENCRYPTION_SECRET="$(grep '^AUTH_ENCRYPTION_SECRET=' .env.secrets | cut -d= -f2)"
JWT_SECRET_KEY="$JWT_SECRET_KEY" \
AUTH_ENCRYPTION_SECRET="$AUTH_ENCRYPTION_SECRET" \
MCPGATEWAY_UI_ENABLED=true \
MCPGATEWAY_ADMIN_API_ENABLED=true \
PLATFORM_ADMIN_EMAIL=admin@example.com \
uvx --from mcp-contextforge-gateway mcpgateway --host 0.0.0.0 --port 4444
```

Container path from the official README:

```bash
docker pull ghcr.io/ibm/mcp-context-forge:latest
```

Direct installs (`uvx`, pip, `docker run`) listen on `http://localhost:4444`. This catalog lists ContextForge **once**, under tool access — it is an MCP/A2A registry and proxy, not a second LLM-gateway row.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

```bash
npx clawhub@latest search contextforge mcp-context-forge
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — the gateway **is** a compliant MCP server.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/IBM/mcp-context-forge |
| **Transport** | HTTP, JSON-RPC, WebSocket, SSE, stdio, streamable-HTTP |
| **Compatible Clients** | Any MCP client that can reach the unified gateway endpoint |
| **Also federates** | A2A servers and REST/gRPC APIs virtualized as MCP tools |

---

## What It Does

ContextForge (IBM `mcp-context-forge`) sits in front of MCP servers, A2A agents, and REST/gRPC APIs and exposes **one governed endpoint**. Official docs split the product into a Tools Gateway (MCP, REST, gRPC-to-MCP, TOON compression), an Agent Gateway (A2A plus OpenAI-compatible and Anthropic agent routing), an API Gateway (rate limits, auth, retries), a plugin layer, and OpenTelemetry observability.

It can wrap non-MCP services as virtual MCP servers, federate multiple backends, and route across gateways with **UAID** identifiers. Cross-gateway UAID routing is fail-closed: empty `UAID_ALLOWED_DOMAINS` blocks it; production needs a domain allowlist, shared JWT trust, `AUTH_REQUIRED=true`, and `UAID_FORWARD_AUTH=true`.

Closest catalog peers are ToolHive, the hosted MCP Gateway (`mcpgateway.md`), and Obot. ContextForge is distinct because it federates **MCP + A2A + REST/gRPC** on one registry/proxy with UAID cross-gateway routing.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Official tagline: **"An open source registry and proxy that federates MCP, A2A, and REST/gRPC APIs with centralized governance, discovery, and observability. Optimizes Agent & Tool calling, and supports plugins."** — [docs](https://ibm.github.io/mcp-context-forge/), [README](https://github.com/IBM/mcp-context-forge) |
| **Agent-specific primitive** | Unified MCP endpoint over federated tools/agents/APIs; gRPC-to-MCP translation; A2A agent routing; UAID cross-gateway routing with forwarded bearer tokens |
| **Autonomy-compatible control plane** | After the gateway is up, agents discover and call federated tools through one URL with retries, rate limits, and auth — no per-call human click |
| **M2M integration surface** | `uvx --from mcp-contextforge-gateway mcpgateway`, Docker image, REST/JSON-RPC/WebSocket/SSE/stdio/streamable-HTTP, Admin API |
| **Identity / delegation** | JWT / Basic / custom auth; user-scoped OAuth tokens; UAID routing forwards `Authorization` and records source gateway + user in headers. Empty UAID allowlist fail-closes cross-gateway calls |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Federated MCP endpoint** | One server in front of many MCP, A2A, and REST/gRPC backends |
| **Virtual MCP server** | Wrap a legacy REST/gRPC API as MCP tools, prompts, and resources |
| **gRPC-to-MCP translation** | Reflection-based service discovery and method introspection |
| **A2A / agent routing** | External agents (OpenAI, Anthropic, custom) behind the Agent Gateway |
| **UAID routing** | Cross-gateway tool/agent addressing with domain allowlist and forwarded auth |
| **Plugin layer** | Documented plugin extensibility for extra transports and integrations |
| **OTLP observability** | OpenTelemetry traces to Phoenix, Jaeger, Zipkin, and other backends |

---

## Autonomy Model

```
Operator starts mcpgateway (uvx or Docker) with JWT and encryption secrets
    -> Register or federate MCP servers, A2A agents, and REST/gRPC APIs
    -> Agent connects to the single gateway URL as an MCP (or A2A) client
    -> Gateway authenticates, rate-limits, retries, and routes by registry / UAID
    -> Optional Admin UI watches logs; it is not required for each tool call
```

---

## Identity and Delegation Model

- **Caller identity:** JWT or configured auth scheme on the gateway; user-scoped OAuth tokens for upstreams; `X-Upstream-Authorization` is documented as always supported.
- **UAID hops:** Cross-gateway calls forward the bearer token. Remote gateways re-validate and keep RBAC context. Source gateway and user are tracked in headers.
- **Fail-closed federation:** `UAID_ALLOWED_DOMAINS` empty means no cross-gateway routing.
- **No end-user wallet:** This is a tool/agent registry, not a payment identity.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `uvx --from mcp-contextforge-gateway mcpgateway --host 0.0.0.0 --port 4444` |
| Docker | `docker pull ghcr.io/ibm/mcp-context-forge:latest` |
| MCP | HTTP, JSON-RPC, WebSocket, SSE, stdio, streamable-HTTP |
| A2A | Agent Gateway routing |
| REST / gRPC | Native REST plus gRPC-to-MCP virtualization |
| Admin API / UI | Optional; `MCPGATEWAY_ADMIN_API_ENABLED` / `MCPGATEWAY_UI_ENABLED` |

---

## Human-in-the-Loop Support

Admin UI and log viewer are optional operator surfaces. Tool and agent calls on the data plane do not require a human click. Auth, retries, and rate limits are the control plane.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Hosted MCP Gateway (`mcpgateway.md`)** | Commercial one-URL tools/skills/sandboxes platform. ContextForge is IBM's open-source MCP+A2A+REST/gRPC federation proxy with UAID routing |
| **ToolHive** | Secure *runtime* for launching MCP servers in containers. It does not federate A2A and REST/gRPC behind UAID |
| **Obot** | MCP hosting/registry/gateway product with a chat client. ContextForge's distinct claim is protocol federation (MCP + A2A + REST/gRPC) and cross-gateway UAID |
| **A generic API gateway** | Routes HTTP. It has no MCP tool registry, A2A agent routing, or gRPC-to-MCP virtualization |

---

## Use Cases

- **One MCP URL for many backends** — federate internal MCP servers and virtualized REST/gRPC APIs
- **A2A + tools on one hop** — route agent-to-agent traffic and tool calls through the same governance layer
- **Multi-cluster federation** — UAID routing across allowlisted gateways with forwarded auth
- **Observable agent tool calls** — export OTLP traces without replacing the agent runtime
