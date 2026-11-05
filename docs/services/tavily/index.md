---
title: "Tavily | Agent-Native Services"
service_name: "Tavily"
description: "Connect your agent to the web"
permalink: /services/tavily/
page_kind: service
service_slug: "tavily"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/tavily.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/tavily.md"
tagline: "Connect your agent to the web"
website: "https://tavily.com"
repository: "https://github.com/tavily-ai/tavily-python"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://tavily.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.tavily.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/tavily-ai/tavily-python" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/tavily.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Tavily is a web intelligence API built specifically for AI agents and RAG pipelines. Unlike general search APIs that return links for a human to click, Tavily returns **ranked, pre-processed content** ready for direct injection into an LLM's context window. It provides multiple specialized endpoints covering search, extraction, crawling, site mapping, and multi-step research.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, SDK, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skills published at tavily-ai/skills — also listed on skills.sh/tavily-ai/tavily-plugins
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Base URL: `https://api.tavily.com` |
| Python SDK | `tavily-python` package |
| LangChain | `TavilySearchResults` tool |
| LlamaIndex | Native tool integration |
| CrewAI | Native tool integration |
| MCP | Model Context Protocol server |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
