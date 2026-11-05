---
title: "Olostep | Agent-Native Services"
service_name: "Olostep"
description: "Transform websites into clean, LLM-ready data"
permalink: /services/olostep/
page_kind: service
service_slug: "olostep"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/olostep.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/olostep.md"
tagline: "Transform websites into clean, LLM-ready data"
website: "https://www.olostep.com"
repository: "https://github.com/olostep/olostep-mcp-server"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · http · API · documentation</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.olostep.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.olostep.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/olostep/olostep-mcp-server" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/olostep.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Olostep is a **web data API** that turns URLs into **Markdown, HTML, JSON, or plain text** with high reliability, handling proxies, bot mitigation, and JavaScript rendering. It provides **search** (e.g. structured SERP-style results), **crawl**, **map** (URL discovery), **batch** scraping at scale, and an **Agents** API for autonomous research workflows. It is explicitly positioned as infrastructure for **AI and research agents** (see [llms.txt](https://www.olostep.com/llms.txt)).

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, http, API, documentation
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No official npx skills add org/repo bundle located; use llms.txt and docs for machine-readable discovery.
- **Onboarding type:** `documentation`

## How agents onboard

```bash
# See https://docs.olostep.com/get-started/welcome
# Set OLOSTEP_API_KEY and call HTTPS endpoints (scrapes, searches, maps, crawls, batches)
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/olostep.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | https://docs.olostep.com |
| MCP | `npx -y olostep-mcp`, remote `https://mcp.olostep.com/mcp` |
| Docker | `olostep/mcp-server` image (per docs) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
