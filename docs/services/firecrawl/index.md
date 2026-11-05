---
title: "Firecrawl | Agent-Native Services"
service_name: "Firecrawl"
description: "Turn any website into LLM-ready data"
permalink: /services/firecrawl/
page_kind: service
service_slug: "firecrawl"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/firecrawl.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/firecrawl.md"
tagline: "Turn any website into LLM-ready data"
website: "https://firecrawl.dev"
repository: "https://github.com/firecrawl/firecrawl"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://firecrawl.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.firecrawl.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/firecrawl/firecrawl" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/firecrawl.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Firecrawl is a web extraction API that converts websites into clean, LLM-ready markdown or structured JSON. Its `/agent` endpoint goes further: agents describe *what data they need* in natural language — no URLs required. Firecrawl autonomously searches, navigates, and extracts across multiple sources in parallel, returning structured output directly consumable by an LLM.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skill published at firecrawl/cli
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | All endpoints (agent, scrape, crawl, extract, map) |
| Python SDK | `pip install firecrawl-py`; Pydantic schema support |
| Node.js SDK | `npm install @mendable/firecrawl-js`; Zod schema support |
| MCP Server | Model Context Protocol for direct LLM tool use |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
