---
title: "Keenable | Agent-Native Services"
service_name: "Keenable"
description: "Independent Web Search API for AI"
permalink: /services/keenable/
page_kind: service
service_slug: "keenable"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/keenable.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/keenable.md"
tagline: "Independent Web Search API for AI"
verified_at: "2026-11-19"
website: "https://keenable.ai"
repository: "https://github.com/keenableai/keenable-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · SDK · openapi · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://keenable.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.keenable.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/keenableai/keenable-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/keenable.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Keenable is a web search API whose index, crawler, and ranking are its own. The homepage description is: “Keenable is independent web search infrastructure for AI: our own crawler, index and ranking, and it gets better the more agents use it.”

Agents call it over MCP, a REST API, official SDKs, or a published skill. Search results are ranked pages with titles, URLs, and snippets sized for a citation. Page fetch returns clean Markdown rather than a browser document. There is no consumer search page to operate; the product is the agent interface.

The open-source pieces are the MCP server, the SDKs, and the skill. The hosted index stays closed.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, SDK, openapi, STDIO, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding

```
Read https://docs.keenable.ai/llms.txt and follow the instructions.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/keenable.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| URL onboarding | `Read https://docs.keenable.ai/llms.txt and follow the instructions.` |
| Remote MCP | `https://api.keenable.ai/mcp-public` (no key); `https://api.keenable.ai/mcp` (optional key) |
| REST / OpenAPI | https://api.keenable.ai/openapi.json version 0.1.37 |
| SDKs | https://github.com/keenableai/keenable-sdk (MIT). `npm install keenable`, `pip install keenable` |
| Stdio MCP | `npx -y @keenable/mcp` |
| Agent Skill | `npx skills add keenableai/keenable-mcp` (`keenable-web-search` 1.2.0, MIT) |
| CLI | https://github.com/keenableai/keenable-cli — license not published |

---

## Verification

Last verified **2026-11-19**.

Sources:
- https://keenable.ai
- https://docs.keenable.ai
- https://docs.keenable.ai/llms.txt
- https://api.keenable.ai/mcp-public
- https://api.keenable.ai/openapi.json
- https://github.com/keenableai/keenable-mcp
- https://github.com/keenableai/keenable-sdk
- https://github.com/keenableai/keenable-cli

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
