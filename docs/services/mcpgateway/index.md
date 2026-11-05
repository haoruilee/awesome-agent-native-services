---
title: "MCP Gateway | Agent-Native Services"
service_name: "MCP Gateway"
description: "The platform for production AI agents"
permalink: /services/mcpgateway/
page_kind: service
service_slug: "mcpgateway"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/mcpgateway.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcpgateway.md"
tagline: "The platform for production AI agents"
website: "https://mcpgateway.com"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mcpgateway.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://mcpgateway.com (product + blog)" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcpgateway.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

MCP Gateway is an **enterprise control plane** for production agents: it unifies **MCP servers** (tools), **Agent Skills** (how to use tools), and **sandboxes** (where code runs) behind **one API key and URL**. Marketing emphasizes governance — semantic **tool search** across many servers, **automatic OAuth refresh**, **RBAC**, **audit trails**, and **telemetry** — to reduce "shadow AI" from unmanaged MCP sprawl.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, SDK, http, API
- **MCP:** ✅ Core product is an MCP aggregation gateway — multiple MCP servers behind one URL with OAuth token lifecycle, RBAC, audit, and telemetry (per homepage).
- **Agent Skill:** ⚠️ Platform supports Agent Skills as portable instruction packages (create/manage via SDK per marketing examples); no single public npx skills add repo verified here — see vendor docs.
- **Onboarding type:** `mcp`

## How agents onboard

```bash
pip install mcpgateway-sdk
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mcpgateway.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install mcpgateway-sdk` |
| HTTP API | Gateway URL from deployment |
| MCP | Aggregated MCP backend servers |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
