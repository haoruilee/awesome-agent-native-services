# Bifrost

> **"The fastest way to build AI applications that never go down."**

| | |
|---|---|
| **Website** | https://docs.getbifrost.ai |
| **Docs** | https://docs.getbifrost.ai |
| **GitHub** | https://github.com/maximhq/bifrost |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/maximhq/bifrost?style=social)](https://github.com/maximhq/bifrost) |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |
| **License** | Apache-2.0 |
| **Verified at** | 2026-08-25 |

---

## Official Website

https://docs.getbifrost.ai

---

## Official Repo

https://github.com/maximhq/bifrost

---

## How to Use (Agent Onboarding)

**Quickest verified path for a self-hosted gateway:**

```bash
npx -y @maximhq/bifrost
```

The gateway starts on `http://localhost:8080`. Configure providers through the Web UI, API, or `config.json`, then point an OpenAI-compatible client at the gateway. To expose aggregated MCP tools, connect an MCP client to `http://localhost:8080/mcp` and provide a virtual-key header when authentication is enabled:

```json
{
  "mcpServers": {
    "bifrost": {
      "url": "http://localhost:8080/mcp",
      "headers": {
        "Authorization": "Bearer vk_your_virtual_key"
      }
    }
  }
}
```

See the [gateway setup guide](https://docs.getbifrost.ai/quickstart/gateway/setting-up) and [MCP gateway guide](https://docs.getbifrost.ai/mcp/gateway).

---

## Agent Skills

**Status:** ⚠️ No official Agent Skill published by Bifrost yet.

Search community skills: `npx clawhub@latest search bifrost`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

Bifrost can connect to external MCP servers as a client and, in Gateway deployment, expose aggregated tools as an MCP server at `/mcp`. The MCP gateway feature is documented for Bifrost v1.4.0-prerelease1 and above.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/maximhq/bifrost |
| **Transport** | HTTP JSON-RPC 2.0 via `POST /mcp`; Server-Sent Events via `GET /mcp` |
| **Authentication** | Virtual-key/API-key headers or OAuth 2.1, controlled by `mcp_server_auth_mode` |
| **Compatible Clients** | Claude Desktop, Cursor, custom MCP applications, and other MCP-compatible clients |

Sources: [MCP overview](https://docs.getbifrost.ai/mcp/overview), [MCP gateway](https://docs.getbifrost.ai/mcp/gateway), and [gateway authentication](https://docs.getbifrost.ai/mcp/gateway-auth).

---

## What It Does

Bifrost is a high-performance, self-hosted AI gateway that provides one OpenAI-compatible interface to more than 23 model providers. It handles provider configuration, request routing, retries, automatic fallbacks, load balancing, semantic caching, and drop-in integrations for common AI SDKs.

For agent systems, Bifrost adds an MCP client and gateway, opt-in Agent Mode for automatic tool execution, per-virtual-key tool filtering, hierarchical budgets and rate limits, and request observability. The gateway can aggregate tools from multiple MCP servers behind one endpoint while keeping provider credentials and governance policies outside agent code.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Bifrost's official MCP documentation describes Agent Mode as a way to enable autonomous tool execution and transform static chat models into action-capable agents. The project README uses the broader phrase “AI applications” rather than claiming an agent-only audience; that boundary was disclosed in [issue #105](https://github.com/haoruilee/awesome-agent-native-services/issues/105), which the maintainer approved before this PR. |
| **Agent-specific primitive** | The MCP gateway aggregates external tools for MCP clients, while Agent Mode can execute configured tools automatically. Virtual keys can filter which MCP clients and tools are exposed to each caller. |
| **Autonomy-compatible control plane** | Provider retries, fallbacks, and load balancing operate without per-request human intervention. Agent Mode is explicitly opt-in; the safer default keeps tool calls as suggestions that require a separate execution call. |
| **M2M integration surface** | Bifrost exposes an OpenAI-compatible HTTP API, a native Go SDK, an MCP JSON-RPC/SSE gateway, and API-, Web UI-, and file-based configuration. |
| **Identity / delegation** | Virtual keys scope provider/model access, MCP tools, budgets, and rate limits. MCP OAuth can represent a virtual key, development session, or authenticated user. Bifrost documents scoped governance and audit logging, but does not claim a dedicated per-agent identity or KYA system. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **MCP Gateway** | Exposes connected MCP tools through one HTTP/SSE endpoint for external MCP clients. |
| **Agent Mode** | Opt-in automatic execution of configured tools for action-capable agent loops. |
| **Virtual Keys** | Scoped credentials with provider/model filtering, MCP tool permissions, budgets, and rate limits. |
| **Provider Routing** | Unified model access with retries, key rotation, fallback chains, and load balancing. |
| **Hierarchical Budgets** | Cumulative cost limits and rate limits across customers, teams, virtual keys, and provider configurations. |
| **Request Observability** | Asynchronous logs, token and cost data, latency, provider context, tool calls, and Prometheus/distributed tracing integrations. |

---

## Autonomy Model

```text
Agent client connects to Bifrost's OpenAI-compatible API or /mcp endpoint
    ↓
Bifrost authenticates the request and applies virtual-key tool/model policy
    ↓
The agent discovers available models or MCP tools
    ↓
Bifrost routes the model request and retries, rotates keys, or falls back when needed
    ↓
The agent receives a response or an MCP tool call
    ↓
Default MCP mode waits for an explicit execution request; configured Agent Mode can execute allowed tools automatically
    ↓
Budgets, rate limits, logs, metrics, and traces record the operation
```

---

## Identity and Delegation Model

- Virtual keys are the main governance entity and can restrict models, providers, MCP clients, and individual tools.
- Virtual keys can be attached to teams or customers and carry independent budgets and request/token rate limits.
- MCP clients can authenticate with a virtual-key/API-key header or use Bifrost's OAuth 2.1 flow when enabled.
- OAuth consent can bind a grant to a virtual key, an anonymous development session, or an authenticated user through SSO/SCIM.
- Request and tool-operation logs provide operational attribution, while Prometheus and distributed tracing integrations support deployment-level monitoring.
- Bifrost does not present a separate per-agent identity or delegated-credential marketplace; deployments should use scoped virtual keys or OAuth identities when that boundary is required.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| OpenAI-compatible HTTP API | Unified `/v1` API for supported model providers, including chat, responses, streaming, and tool calling where supported. |
| MCP Gateway | `POST /mcp` JSON-RPC tool discovery/execution and `GET /mcp` SSE for external MCP clients. |
| Go SDK | `go get github.com/maximhq/bifrost/core` for direct in-process provider access and tool-calling integrations. |
| Configuration API | Provider, virtual-key, budget, rate-limit, and MCP configuration through the management API. |
| Configuration files | Declarative `config.json` configuration for provider and governance setup. |
| Observability | Request logs, cost/token/latency metadata, Prometheus metrics, and distributed tracing integrations. |

---

## Human-in-the-Loop Support

Bifrost's default MCP tool-calling flow does not execute tools automatically. The model returns a tool-call suggestion, the application can inspect or approve it, and a separate API call executes the approved operation. Agent Mode is an explicit opt-in that allows configured tools to run automatically. Bifrost supplies the execution and policy controls; an application or client remains responsible for any domain-specific approval UX.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Direct provider API** | Exposes one provider and leaves cross-provider fallback, load balancing, MCP aggregation, and unified governance to the agent application. |
| **Generic reverse proxy** | Forwards HTTP traffic but does not provide model-aware routing, virtual-key budgets, MCP tool filtering, Agent Mode, or LLM-specific observability. |
| **Provider-specific SDK** | Requires provider-specific integration code and does not give an agent a common gateway surface across providers and MCP tools. |

---

## Use Cases

- **Self-hosted agent gateway** — expose one OpenAI-compatible endpoint to an agent fleet while keeping provider credentials server-side.
- **MCP tool aggregation** — connect filesystem, web-search, database, and custom MCP servers, then expose them through one governed endpoint.
- **Reliable model routing** — retry, rotate keys, load-balance, and fall back across providers without changing agent code.
- **Budgeted agent workloads** — assign virtual keys to teams or customers with independent cost and rate limits.
- **Auditable tool operations** — retain request, tool-call, cost, latency, and provider metadata for debugging and operational review.
