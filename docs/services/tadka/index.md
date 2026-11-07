---
title: "Tadka | Agent-Native Services"
service_name: "Tadka"
description: "The booking layer for AI agents"
permalink: /services/tadka/
page_kind: service
service_slug: "tadka"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/tadka.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/tadka.md"
tagline: "The booking layer for AI agents"
verified_at: "2026-11-07"
website: "https://tadka.xyz"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-07</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://tadka.xyz" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://tadka.xyz/developers · https://tadka.xyz/llms.txt · https://tadka.xyz/openapi.json" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/tadka.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Tadka publishes structured, agent-ready restaurant profiles (cuisines, price for two, dietary options, amenities, menus, live availability) and an atomic booking engine so agents do not double-book. The open REST API is read-only discovery without a key. Booking, cancel, and waitlist run through MCP under the signed-in diner's permissions. Restaurants can list for free during launch; partner POS sync via signed webhooks is documented under Advanced.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP (OAuth as diner) + open REST directory
- **Catalog protocols:** MCP, REST, openapi, http, API
- **MCP:** ✅ Available — OAuth required for booking tools
- **Agent Skill:** ⚠️ Not yet published as an installable Agent Skills package
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP (OAuth as diner) + open REST directory

```
https://tadka.xyz/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/tadka.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | https://tadka.xyz/mcp (OAuth 2.1) |
| REST | https://tadka.xyz/api/public/v1/restaurants |
| OpenAPI | https://tadka.xyz/openapi.json |
| llms.txt | https://tadka.xyz/llms.txt |

---

## Verification

Last verified **2026-11-07**.

Sources:
- https://tadka.xyz/llms.txt
- https://tadka.xyz/openapi.json
- https://tadka.xyz/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
