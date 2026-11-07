---
title: "SerpKite | Agent-Native Services"
service_name: "SerpKite"
description: "The Google SERP API built for AI agents"
permalink: /services/serpkite/
page_kind: service
service_slug: "serpkite"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/serpkite.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/serpkite.md"
tagline: "The Google SERP API built for AI agents"
verified_at: "2026-11-07"
website: "https://serpkite.com"
repository: "https://github.com/serpkite/serpkite-js"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (official SDKs); hosted API is a commercial service</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-07</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://serpkite.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://serpkite.com/docs/mcp · https://serpkite.com/llms.txt · https://serpkite.com/openapi/serp-api.yaml" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/serpkite/serpkite-js" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/serpkite.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

SerpKite turns live search and page content into LLM-ready Markdown or structured JSON. Agents can search Google (and fall back across engines), fetch pages as Markdown, get cited answers, extract schema-shaped JSON, and run async crawl/research jobs. Spend is prepaid credits with per-key caps so a runaway loop stops at a known cost.

---

## Agent-facing interfaces

- **Interaction pattern:** Remote MCP + REST/SDKs
- **Catalog protocols:** MCP, REST, SDK, openapi, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not published as an npx skills add package
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** Remote MCP + REST/SDKs

```
https://api.serpkite.com/v1/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/serpkite.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | https://api.serpkite.com/v1/mcp |
| REST | https://api.serpkite.com/v1/* |
| OpenAPI | https://serpkite.com/openapi/serp-api.yaml |
| SDKs | `serpkite` (TS/Python/Go), langchain-serpkite, `@serpkite/ai-sdk` |
| llms.txt | https://serpkite.com/llms.txt |

---

## Verification

Last verified **2026-11-07**.

Sources:
- https://serpkite.com/llms.txt
- https://api.serpkite.com/v1/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
