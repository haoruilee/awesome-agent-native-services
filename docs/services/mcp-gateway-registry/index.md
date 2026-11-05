---
title: "MCP Gateway & Registry | Agent-Native Services"
service_name: "MCP Gateway & Registry"
description: "Unified Agent & MCP Server Registry – Gateway for AI Development Tools"
permalink: /services/mcp-gateway-registry/
page_kind: service
service_slug: "mcp-gateway-registry"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/mcp-gateway-registry.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcp-gateway-registry.md"
tagline: "Unified Agent & MCP Server Registry – Gateway for AI Development Tools"
verified_at: "2026-10-13"
website: "https://agentic-community.github.io/mcp-gateway-registry/"
repository: "https://github.com/agentic-community/mcp-gateway-registry"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · A2A · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentic-community.github.io/mcp-gateway-registry/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://agentic-community.github.io/mcp-gateway-registry/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/agentic-community/mcp-gateway-registry" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcp-gateway-registry.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

The **MCP Gateway & Registry** (agentic-community) is an open-source control plane for organizational AI assets: MCP servers, A2A agents, skills, and custom entity types. Official docs: it began as one secure entry to many MCP servers and grew into a general AI asset registry on the same access-control and audit model.

The **gateway** is the data plane (nginx: TLS, auth validation, routing). The **registry** is the control plane (FastAPI: inventory, access model, audit, embeddings). An auth server talks to Keycloak, Entra ID, Okta, Auth0, Cognito, or PingFederate. By default, A2A discovery and ACL happen in the registry and agents then talk peer-to-peer; reverse-proxy mode can force A2A through the gateway.

**Distinctness:** hosted [MCP Gateway](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcpgateway.md) is a commercial one-URL tools/skills/sandboxes platform (`mcpgateway-sdk`). [ToolHive](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhive.md) runs MCP servers in secure containers. [ContextForge](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/contextforge.md) federates MCP+A2A+REST/gRPC with UAID routing. This project is the agentic-community **enterprise registry** (IdP, virtual MCP servers, 3LO egress auth, admission scanning, external-registry federation).

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP gateway
- **Catalog protocols:** Agent Skill, MCP, REST, CLI, A2A, openapi, http, API
- **MCP:** ✅ Available — agents and coding assistants connect through the gateway as MCP clients.
- **Agent Skill:** ✅ Available as in-repo skills (not npx skills add).
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP gateway

```bash
git clone https://github.com/agentic-community/mcp-gateway-registry.git
cd mcp-gateway-registry
cp .env.example .env
# Set required secrets (KEYCLOAK_ADMIN_PASSWORD, SECRET_KEY, …) — see docs/configuration.md
./build_and_run.sh --prebuilt
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcp-gateway-registry.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP / HTTPS | nginx data plane |
| REST / OpenAPI | Registry API (`api/openapi.json`) |
| CLI | `registry_management.py`; `./build_and_run.sh --prebuilt` |
| Deploy | Docker Compose, Helm (EKS), Terraform (ECS) |
| A2A | Discovery + optional reverse-proxy mode |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/agentic-community/mcp-gateway-registry

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
