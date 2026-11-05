---
title: "MetaMCP | Agent-Native Services"
service_name: "MetaMCP"
description: "MCP Aggregator, Orchestrator, Middleware, Gateway in one docker"
permalink: /services/metamcp/
page_kind: service
service_slug: "metamcp"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/metamcp.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/metamcp.md"
tagline: "MCP Aggregator, Orchestrator, Middleware, Gateway in one docker"
verified_at: "2026-10-20"
website: "https://docs.metamcp.com"
repository: "https://github.com/metatool-ai/metamcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · openapi · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://docs.metamcp.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.metamcp.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/metatool-ai/metamcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/metamcp.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MetaMCP is a **self-hosted MCP proxy**: register MCP servers, group them into **namespaces**, apply **middleware**, and host them as one meta-MCP with public SSE or Streamable HTTP endpoints. Tool cherry-picking, an inspector, API-key and OIDC auth, multi-tenancy (public/private scopes), and OpenAPI for Open WebUI ship in one Docker Compose stack.

Last code push as of verification: **2026-06-22**. Still listed because the docs, Compose path, MIT license, and H1 positioning remain agent-native; operators should note the quieter cadence versus [MCPHub](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcphub.md) / [ContextForge](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/contextforge.md).

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [MCPHub](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcphub.md) | Node hub with `$smart` vector routing, Apache-2.0, active 2026-09 |
| [MCPJungle](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcpjungle.md) | Go/Compose one-`/mcp` + enterprise tokens, MPL-2.0 |
| [ContextForge](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/contextforge.md) | IBM federation of MCP + **A2A + REST/gRPC** + UAID |
| [MCP Gateway & Registry](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcp-gateway-registry.md) | Org IdP, virtual MCP, 3LO, skill scanning |
| [ToolHive](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhive.md) | Secure **container runtime** for launching MCP servers |
| [Toolport](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolport.md) | Local stdio meta-gateway + OS keychain |
| [Obot](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/obot.md) | Full MCP platform **plus chat client** |
| Hosted [MCP Gateway](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcpgateway.md) | Commercial one-URL tools/skills/sandboxes |

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP gateway
- **Catalog protocols:** MCP, openapi, STDIO, http, API
- **MCP:** ✅ Available — the product is a meta-MCP server
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP gateway

```bash
git clone https://github.com/metatool-ai/metamcp.git
cd metamcp
cp example.env .env
docker compose up -d
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/metamcp.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Docker Compose | recommended path (`example.env`) |
| HTTP MCP | Streamable HTTP + SSE |
| OpenAPI | Open WebUI-compatible |
| STDIO clients | `mcp-proxy` + API key |
| License | MIT |
| Cadence | Last push 2026-06-22 |

---

## Verification

Last verified **2026-10-20**.

Sources:
- https://api.github.com/repos/metatool-ai/metamcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
