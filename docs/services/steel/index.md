---
title: "Steel | Agent-Native Services"
service_name: "Steel"
description: "Browser Infrastructure for AI Agents"
permalink: /services/steel/
page_kind: service
service_slug: "steel"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/steel.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/steel.md"
tagline: "Browser Infrastructure for AI Agents"
website: "https://steel.dev"
repository: "https://github.com/steel-dev/steel-browser"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://steel.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.steel.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/steel-dev/steel-browser" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/steel.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Steel provides **cloud (or self-hosted) browser sessions** exposed through a **Sessions API** so AI agents can automate the web without running infrastructure. Agents create isolated sessions (cookies, storage, and fingerprint per session), connect via **Puppeteer, Playwright, or Selenium** with a one-line `connect` change from local `launch`, and tear down when finished. The product emphasizes **sub-second session start**, **long-running sessions** (up to 24h on cloud per marketing), **CAPTCHA handling**, **proxy and fingerprint controls**, **session viewer** for debugging, and **cookie / storage injection** so agents resume authenticated flows.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / REST + MCP (stdio) + Puppeteer / Playwright / Selenium connect
- **Catalog protocols:** MCP, REST, SDK, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No single official npx skills add steel-dev/skills registry entry yet — use cookbooks and MCP.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK / REST + MCP (stdio) + Puppeteer / Playwright / Selenium connect

```bash
pip install steel-sdk   # PyPI package name: steel-sdk
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/steel.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST / Sessions API | https://docs.steel.dev |
| Python | `pip install steel-sdk` |
| Node.js | `npm install steel-sdk` |
| Puppeteer / Playwright / Selenium | Connect to remote session |
| MCP | `steel-dev/steel-mcp-server` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
