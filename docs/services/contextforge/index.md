---
title: "ContextForge | Agent-Native Services"
service_name: "ContextForge"
description: "An open source registry and proxy that federates MCP, A2A, and REST/gRPC APIs with centralized governance, discovery, and observability. Optimizes Agent &…"
permalink: /services/contextforge/
page_kind: service
service_slug: "contextforge"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/contextforge.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/contextforge.md"
tagline: "An open source registry and proxy that federates MCP, A2A, and REST/gRPC APIs with centralized governance, discovery, and observability. Optimizes Agent & Tool calling, and supports plugins"
verified_at: "2026-10-13"
website: "https://ibm.github.io/mcp-context-forge/"
repository: "https://github.com/IBM/mcp-context-forge"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · GRPC · websocket · CLI · A2A · json rpc · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://ibm.github.io/mcp-context-forge/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://ibm.github.io/mcp-context-forge/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/IBM/mcp-context-forge" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/contextforge.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

ContextForge (IBM `mcp-context-forge`) sits in front of MCP servers, A2A agents, and REST/gRPC APIs and exposes **one governed endpoint**. Official docs split the product into a Tools Gateway (MCP, REST, gRPC-to-MCP, TOON compression), an Agent Gateway (A2A plus OpenAI-compatible and Anthropic agent routing), an API Gateway (rate limits, auth, retries), a plugin layer, and OpenTelemetry observability.

It can wrap non-MCP services as virtual MCP servers, federate multiple backends, and route across gateways with **UAID** identifiers. Cross-gateway UAID routing is fail-closed: empty `UAID_ALLOWED_DOMAINS` blocks it; production needs a domain allowlist, shared JWT trust, `AUTH_REQUIRED=true`, and `UAID_FORWARD_AUTH=true`.

Closest catalog peers are ToolHive, the hosted MCP Gateway (`mcpgateway.md`), and Obot. ContextForge is distinct because it federates **MCP + A2A + REST/gRPC** on one registry/proxy with UAID cross-gateway routing.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP gateway
- **Catalog protocols:** MCP, REST, GRPC, websocket, CLI, A2A, json rpc, STDIO, http, API
- **MCP:** ✅ Available — the gateway is a compliant MCP server.
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP gateway

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

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/contextforge.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `uvx --from mcp-contextforge-gateway mcpgateway --host 0.0.0.0 --port 4444` |
| Docker | `docker pull ghcr.io/ibm/mcp-context-forge:latest` |
| MCP | HTTP, JSON-RPC, WebSocket, SSE, stdio, streamable-HTTP |
| A2A | Agent Gateway routing |
| REST / gRPC | Native REST plus gRPC-to-MCP virtualization |
| Admin API / UI | Optional; `MCPGATEWAY_ADMIN_API_ENABLED` / `MCPGATEWAY_UI_ENABLED` |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/IBM/mcp-context-forge

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
