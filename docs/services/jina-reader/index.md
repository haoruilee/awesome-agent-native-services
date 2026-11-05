---
title: "Jina Reader | Agent-Native Services"
service_name: "Jina Reader"
description: "Convert a URL to LLM-friendly input, by simply adding r.jina.ai in front"
permalink: /services/jina-reader/
page_kind: service
service_slug: "jina-reader"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/jina-reader.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/jina-reader.md"
tagline: "Convert a URL to LLM-friendly input, by simply adding r.jina.ai in front"
website: "https://jina.ai/reader"
repository: "https://github.com/jina-ai/reader"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://jina.ai/reader" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://jina.ai/reader (API parameters and examples)" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/jina-ai/reader" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/jina-reader.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Reader turns **URLs and search queries** into **clean, LLM-friendly text**: it renders pages (including dynamic content), strips boilerplate, optionally **captions images** for VLMs, reads **PDFs**, and returns **JSON** shapes agents can parse. **Search mode** returns multiple results with page bodies, not just blue links — optimized for **grounding** and **RAG**.

---

## Agent-facing interfaces

- **Interaction pattern:** HTTP GET/POST + MCP (mcp.jina.ai)
- **Catalog protocols:** MCP, http
- **MCP:** ✅ Documented on Reader page — mcp.jina.ai
- **Agent Skill:** ⚠️ No official ClawHub skill pack required; integration is URL + MCP.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** HTTP GET/POST + MCP (mcp.jina.ai)

```bash
curl "https://r.jina.ai/https://www.example.com"
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/jina-reader.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| HTTPS | `https://r.jina.ai`, `https://s.jina.ai` |
| MCP | `mcp.jina.ai` |
| Open source | Self-host from GitHub |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
