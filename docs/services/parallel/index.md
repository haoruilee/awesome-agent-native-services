---
title: "Parallel | Agent-Native Services"
service_name: "Parallel"
description: "The highest accuracy web search for your AI"
permalink: /services/parallel/
page_kind: service
service_slug: "parallel"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/parallel.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/parallel.md"
tagline: "The highest accuracy web search for your AI"
website: "https://www.parallel.ai"
repository: "https://github.com/parallel-web/task-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.parallel.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.parallel.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/parallel-web/task-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/parallel.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Parallel provides **web intelligence APIs purpose-built for AIs**: high-accuracy **search** with verifiable excerpts, **structured deep research** tasks, **monitoring** with webhooks, and **OpenAI-compatible** chat for research apps. It targets **agent workflows** that need grounded facts, citations, and predictable per-query pricing rather than raw SERP HTML.

---

## Agent-facing interfaces

- **Interaction pattern:** REST + Python/TypeScript SDK + MCP
- **Catalog protocols:** MCP, REST, http
- **MCP:** ✅ Available (official org repos)
- **Agent Skill:** ⚠️ See GitHub parallel-agent-skills for curated agent skill assets.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** REST + Python/TypeScript SDK + MCP

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/parallel.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | https://docs.parallel.ai |
| Python | `parallel-web` on PyPI |
| TypeScript | `parallel-web` on npm |
| MCP | Hosted Search MCP + `parallel-web/task-mcp` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
