---
title: "MCPJungle | Agent-Native Services"
service_name: "MCPJungle"
description: "Run all your MCP servers behind one endpoint"
permalink: /services/mcpjungle/
page_kind: service
service_slug: "mcpjungle"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/mcpjungle.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcpjungle.md"
tagline: "Run all your MCP servers behind one endpoint"
verified_at: "2026-10-19"
website: "https://docs.mcpjungle.com"
repository: "https://github.com/mcpjungle/MCPJungle"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MPL-2.0 (OSI-approved; not MIT/Apache)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://docs.mcpjungle.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.mcpjungle.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/mcpjungle/MCPJungle" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcpjungle.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MCPJungle is a **self-hosted MCP gateway** for a personal laptop or a team: register stdio and remote MCP servers once, then every client connects to a single `/mcp`. Tool groups expose curated subsets. Development mode is open; **enterprise mode** adds per-client tokens, server-level ACLs, and observability hooks. Upstream static bearer tokens are injected by the gateway (`--bearer-token`); OAuth to upstreams is documented as coming soon.

Last code push as of verification: **2026-08-02**. Still listed because the docs, Compose file, and H1 positioning remain agent-native; operators should note the quieter cadence versus MCPHub/ContextForge.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [MCPHub](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcphub.md) | Node/Docker hub with `$smart` vector routing, dashboard-first ops, Apache-2.0 |
| [ContextForge](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/contextforge.md) | MCP + A2A + REST/gRPC + UAID |
| [MCP Gateway & Registry](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcp-gateway-registry.md) | Org IdP, virtual MCP, 3LO, skill scanning |
| [ToolHive](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhive.md) | Secure container runtime |
| [Toolport](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolport.md) | Local stdio meta-tools + keychain |
| [Obot](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/obot.md) | Hosting + registry + chat client |

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP gateway
- **Catalog protocols:** MCP, CLI, http, API
- **MCP:** ✅ Available — the gateway is one MCP endpoint
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP gateway

```bash
curl -O https://raw.githubusercontent.com/mcpjungle/MCPJungle/refs/heads/main/docker-compose.yaml
docker compose up -d
brew install mcpjungle/mcpjungle/mcpjungle
mcpjungle register --name context7 --url https://mcp.context7.com/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcpjungle.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Docker Compose | default `:8080/mcp` + Postgres |
| CLI | `mcpjungle register`, `start --enterprise`, `init`, client create |
| HTTP MCP | Streamable HTTP `/mcp` |
| HTTP API | documented on docs.mcpjungle.com |
| License | MPL-2.0 |

---

## Verification

Last verified **2026-10-19**.

Sources:
- https://api.github.com/repos/mcpjungle/MCPJungle

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
