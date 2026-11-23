---
title: "Agent Nexus | Agent-Native Services"
service_name: "Agent Nexus"
description: "Autonomous discovery, verified health cards, and drift alerts for 730+ live MCP servers and agent tools"
permalink: /services/agent-nexus/
page_kind: service
service_slug: "agent-nexus"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/agent-nexus.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/agent-nexus.md"
tagline: "Autonomous discovery, verified health cards, and drift alerts for 730+ live MCP servers and agent tools"
verified_at: "2026-11-22"
website: "https://agentnexus.app"
repository: "https://github.com/Strategiumfinancepartner/AgentNexus"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · MCP · REST · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-22</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentnexus.app" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://agentnexus.app/llms.txt" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Strategiumfinancepartner/AgentNexus" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/agent-nexus.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agent Nexus is an independent registry, discovery engine, and health verification index for autonomous AI agents. Instead of static directory listings that go stale, Agent Nexus runs continuous multi-layered hourly probes (liveness, protocol handshake, capability responses, and tool-schema drift) across 730+ public MCP servers and agent-accessible APIs.

When an agent needs a capability (such as web search, transaction processing, code sandboxes, or communications), it queries Agent Nexus by natural-language intent. Agent Nexus returns verified matching services ranked by active operational health, authentication schema, and retry cost, accompanied by automated failover alternatives if a target service is degraded.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐
- **Catalog protocols:** URL onboarding, MCP, REST, openapi, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐

```
Read https://agentnexus.app/llms.txt and follow it.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/agent-nexus.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| URL Onboarding | https://agentnexus.app/llms.txt |
| REST API | `https://agentnexus.app/api/public`, Bearer or `x-api-key` |
| OpenAPI | https://agentnexus.app/openapi.json |
| MCP | `https://agentnexus.app/api/public/mcp` (Streamable HTTP) |
| Streaming Catalog | `https://agentnexus.app/api/public/entries.ndjson` |
| Docs for LLMs | https://agentnexus.app/llms.txt |

---

## Verification

Last verified **2026-11-22**.

Sources:
- https://agentnexus.app
- https://agentnexus.app/llms.txt
- https://agentnexus.app/openapi.json
- https://agentnexus.app/api/public/discover
- https://agentnexus.app/api/public/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
