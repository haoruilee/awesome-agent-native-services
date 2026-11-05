---
title: "Apify | Agent-Native Services"
service_name: "Apify"
description: "Get real-time web data for your AI"
permalink: /services/apify/
page_kind: service
service_slug: "apify"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/apify.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/apify.md"
tagline: "Get real-time web data for your AI"
website: "https://apify.com"
repository: "https://github.com/apify/crawlee"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://apify.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.apify.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/apify/crawlee" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/apify.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Apify is a **web data platform** for running **Actors** — serverless scrapers, crawlers, and browser automations that return **structured datasets** (JSON, CSV) through an **API**. The homepage explicitly targets **AI apps and agents** that need **fresh web data** (social, maps, e-commerce, generic site content) without operating their own proxy and browser farms.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, http, API
- **MCP:** ⚠️ Apify integrates with MCP clients (per integrations page); the primary surface remains REST + SDK.
- **Agent Skill:** ⚠️ Search community skills for Apify patterns.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
npm install apify-client
# or
pip install apify-client
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/apify.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | https://docs.apify.com/api/v2 |
| JavaScript | `apify-client` npm package |
| Python | `apify-client` PyPI |
| Console | https://console.apify.com |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
