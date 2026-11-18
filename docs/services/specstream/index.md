---
title: "SpecStream | Agent-Native Services"
service_name: "SpecStream"
description: "The live web data engine for teams and agents"
permalink: /services/specstream/
page_kind: service
service_slug: "specstream"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/specstream.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/specstream.md"
tagline: "The live web data engine for teams and agents"
website: "https://specstream.ai"
repository: "https://github.com/specstream/specstream-tools"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · MCP · SDK · A2A · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://specstream.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://specstream.ai/agents.md · https://specstream.ai/llms.txt · https://specstream.ai/docs/sdk" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/specstream/specstream-tools" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/specstream.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

SpecStream finds data on the live web and returns each value with its source URL and read time. It has three products: the Search API (`GET /v1/web-search`), the Extract API (`POST /v1/extract`), and Deep Search, which turns a request in plain words into structured rows.

Agents use it through the REST API, the hosted MCP server, an A2A endpoint, or the Python and TypeScript SDKs. A client written for another search API can move to SpecStream by changing its base address and key (drop-in routes).

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding
- **Catalog protocols:** URL onboarding, MCP, SDK, A2A, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding

```
Read https://specstream.ai/agents.md and follow the instructions.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/specstream.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP API | `https://api.specstream.ai` (Search, Extract, Deep Search, research reports) |
| MCP | `https://api.specstream.ai/mcp`, Streamable HTTP, OAuth or API key |
| A2A | Agent Card at `https://api.specstream.ai/.well-known/agent-card.json` |
| x402 / MPP | `https://api.specstream.ai/.well-known/x402` |
| SDKs | `specstream-client` (Python), `@specstream/sdk` (TypeScript) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
