---
title: "Hyperbrowser | Agent-Native Services"
service_name: "Hyperbrowser"
description: "Hyperbrowser - Web Infra for AI Agents"
permalink: /services/hyperbrowser/
page_kind: service
service_slug: "hyperbrowser"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/hyperbrowser.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/hyperbrowser.md"
tagline: "Hyperbrowser - Web Infra for AI Agents"
website: "https://www.hyperbrowser.ai"
repository: "https://github.com/hyperbrowserai/mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.hyperbrowser.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.hyperbrowser.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/hyperbrowserai/mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/hyperbrowser.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Hyperbrowser is **web infrastructure for AI agents**: managed browsers, **scraping/crawling**, **structured extraction**, and **multi-agent backends** (browser-use, OpenAI CUA, Claude computer-use) behind one API. **HyperAgent** is the platform’s agent SDK. The **MCP server** exposes these capabilities directly to LLM clients so agents can research, extract, and automate the web without custom middleware.

---

## Agent-facing interfaces

- **Interaction pattern:** REST API + SDKs + MCP
- **Catalog protocols:** MCP, REST, SDK, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No official npx skills add hyperbrowser/… skill registry entry documented here.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** REST API + SDKs + MCP

```bash
npx hyperbrowser-mcp <YOUR-HYPERBROWSER-API-KEY>
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/hyperbrowser.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | `https://api.hyperbrowser.ai` (see docs) |
| MCP | `hyperbrowserai/mcp` |
| Python | https://github.com/hyperbrowserai/python-sdk |
| Node.js | https://github.com/hyperbrowserai/node-sdk |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
