---
title: "Exa | Agent-Native Services"
service_name: "Exa"
description: "The search engine designed for AI"
permalink: /services/exa/
page_kind: service
service_slug: "exa"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/exa.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/exa.md"
tagline: "The search engine designed for AI"
website: "https://exa.ai"
repository: "https://github.com/exa-labs/exa-py"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://exa.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.exa.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/exa-labs/exa-py" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/exa.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Exa is a neural search engine that retrieves semantically relevant web content using embeddings rather than keyword matching. Its output is clean, parsed text ready for LLM consumption — not SERP links. Where keyword search fails on complex entity queries (specific people, companies, research topics), Exa's semantic model returns 20× more accurate results. The `exa-code` product specifically targets coding agents with token-efficient code and documentation retrieval.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Community skills available; no official SKILL.md published by Exa yet
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Search, contents, answer, websets endpoints |
| Python SDK | `exa-py` package |
| LangChain | Native tool integration |
| CrewAI | Native tool integration |
| LlamaIndex | Native tool integration |
| Mastra | Native integration |
| MCP | Model Context Protocol server |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
