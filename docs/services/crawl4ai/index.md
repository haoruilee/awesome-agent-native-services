---
title: "Crawl4AI | Agent-Native Services"
service_name: "Crawl4AI"
description: "🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper"
permalink: /services/crawl4ai/
page_kind: service
service_slug: "crawl4ai"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/crawl4ai.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/crawl4ai.md"
tagline: "🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper"
website: "https://crawl4ai.com"
repository: "https://github.com/unclecode/crawl4ai"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://crawl4ai.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.crawl4ai.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/unclecode/crawl4ai" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/crawl4ai.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Crawl4AI is an **open-source web crawler and scraper** built for **LLMs and AI agents**: JavaScript rendering, **LLM-friendly markdown** output, extraction strategies, **anti-bot** hooks, **shadow DOM** handling, and **crash recovery**. Agents use it to turn arbitrary URLs into **context-window-sized**, structured text instead of raw HTML soup.

---

## Agent-facing interfaces

- **Interaction pattern:** Python library + Docker + MCP
- **Catalog protocols:** MCP, http
- **MCP:** ✅ MCP server shipped in ecosystem (see repo and *"Crawl4AI MCP Server"* documentation in community/dev posts linked from project).
- **Agent Skill:** ⚠️ No single official npx skills add unclecode/… skill pack required by upstream.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** Python library + Docker + MCP

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/crawl4ai.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python | Primary library |
| Docker | Recommended for MCP / full browser stack |
| MCP | Model Context Protocol integration |
| HTTP | When deployed as a service |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
