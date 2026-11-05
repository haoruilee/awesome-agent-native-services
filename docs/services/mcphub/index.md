---
title: "MCPHub | Agent-Native Services"
service_name: "MCPHub"
description: "One gateway for all your MCP servers"
permalink: /services/mcphub/
page_kind: service
service_slug: "mcphub"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/mcphub.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcphub.md"
tagline: "One gateway for all your MCP servers"
verified_at: "2026-10-19"
website: "https://www.mcphub.app"
repository: "https://github.com/samanhappy/mcphub"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.mcphub.app" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.mcphub.app/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/samanhappy/mcphub" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcphub.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MCPHub is a **self-hosted MCP gateway**: register local and remote MCP servers once, then expose **stable endpoints** with groups, aliases, bearer/OAuth auth, health checks, logs, hot-reload, optional PostgreSQL + pgvector **smart routing**, and tool-result compression. The dashboard is an operator surface; `DISABLE_WEB=true` leaves API + MCP only.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [ContextForge](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/contextforge.md) | IBM federation of MCP + **A2A + REST/gRPC** with UAID. MCPHub is MCP-only connect/organize/control/operate |
| [MCP Gateway & Registry](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcp-gateway-registry.md) | Enterprise IdP registry (Keycloak/Entra), virtual MCP, 3LO egress, skill scanning |
| [ToolHive](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhive.md) | Secure **container runtime** for launching MCP servers |
| [Toolport](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolport.md) | Local stdio meta-gateway + OS keychain — not a hosted/self-hosted HTTP hub |
| [Obot](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/obot.md) | Full MCP platform **plus chat client** |
| Hosted [MCP Gateway](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcpgateway.md) | Commercial one-URL tools/skills/sandboxes (`mcpgateway-sdk`) |

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP gateway
- **Catalog protocols:** MCP, CLI, http
- **MCP:** ✅ Available — the product is the gateway
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP gateway

```bash
docker run -p 3000:3000 \
  -v ./mcp_settings.json:/app/mcp_settings.json \
  -v ./data:/app/data \
  samanhappy/mcphub
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcphub.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Docker | `samanhappy/mcphub` (`latest` / `latest-full`) |
| HTTP MCP | `/mcp`, `/mcp/{group}`, `/mcp/{server}`, `/mcp/$smart` |
| CLI | `mcphub login`, `servers`, `tools`, `call`, `discover`, `install` |
| Config | `mcp_settings.json` or PostgreSQL (database mode) |
| Dashboard | `:3000` — optional (`DISABLE_WEB=true`) |

---

## Verification

Last verified **2026-10-19**.

Sources:
- https://api.github.com/repos/samanhappy/mcphub
- https://demo.mcphub.app/

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
