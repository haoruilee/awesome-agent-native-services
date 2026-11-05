---
title: "NotHumanSearch | Agent-Native Services"
service_name: "NotHumanSearch"
description: "Agent-first search — the index of services designed for AI, not humans"
permalink: /services/nothumansearch/
page_kind: service
service_slug: "nothumansearch"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/nothumansearch.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/nothumansearch.md"
tagline: "Agent-first search — the index of services designed for AI, not humans"
website: "https://nothumansearch.ai"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · MCP · REST · webhook · openapi · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://nothumansearch.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://nothumansearch.ai/llms.txt" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/nothumansearch.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

NotHumanSearch is a search engine whose index only contains sites that are actually usable by AI agents. Every indexed site must ship at least one real agent signal — `llms.txt`, `ai-plugin.json`, OpenAPI spec, MCP server, or a structured REST API with machine-readable schemas. Sites are scored on an agent-readiness scale and ranked so that the most agent-ready result wins, not the one with the most backlinks.

Where general web search returns HTML pages written for humans, NHS returns a ranked list of services an agent can *immediately consume* — with an `agentic_score`, the MCP endpoint URL if present, the `llms.txt` URL if present, and category tags already attached.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, MCP, REST, webhook, openapi, http, API
- **MCP:** ✅ Available — published to the official Model Context Protocol registry as ai.nothumansearch/search (latest v1.5.0).
- **Agent Skill:** ⚠️ No separate official SKILL.md package is published. The hosted
- **Onboarding type:** `url`

## How agents onboard

```
Read https://nothumansearch.ai/llms.txt and follow the instructions.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/nothumansearch.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `GET /api/v1/search`, `/api/v1/check`, `/api/v1/submit`, `/api/v1/monitor/register` — OpenAPI 3.0 |
| MCP | Streamable HTTP transport at `/mcp`; 8 tools; published to MCP registry |
| `llms.txt` | Machine-readable onboarding at `/llms.txt` |
| `ai-plugin.json` | ChatGPT-style plugin manifest |
| Webhook | Per-site change alerts via `/api/v1/monitor/register` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
