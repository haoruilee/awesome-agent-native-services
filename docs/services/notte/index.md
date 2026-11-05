---
title: "Notte | Agent-Native Services"
service_name: "Notte"
description: "Browser infrastructure that lets AI run on the internet at speed"
permalink: /services/notte/
page_kind: service
service_slug: "notte"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/notte.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/notte.md"
tagline: "Browser infrastructure that lets AI run on the internet at speed"
website: "https://www.notte.cc"
repository: "https://github.com/nottelabs/notte"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.notte.cc" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.notte.cc" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/nottelabs/notte" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/notte.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Notte is a **unified browser platform for AI**: remote **browser sessions** (CDP for Playwright, Puppeteer, Selenium, browser-use, Stagehand), **web agents** that complete natural-language tasks in those sessions, **serverless browser functions** (deploy automations next to the browser), AI-assisted **scraping** with structured outputs, and **agent-facing auth** — **vaults** (encrypted credentials the LLM never sees), **agent identities** (email/phone for OTP and 2FA), and **session profiles** that persist browser state. The product also offers **Studio** for building and debugging automations and an **Anything API** for custom engineered endpoints from natural-language task descriptions.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / REST + remote browser via CDP + optional MCP (SSE)
- **Catalog protocols:** MCP, REST, SDK, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No single official npx skills add … registry entry yet — use SDK, Studio, and MCP.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK / REST + remote browser via CDP + optional MCP (SSE)

```bash
pip install notte-sdk
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/notte.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **Python SDK** | `pip install notte-sdk` — [Quickstart](https://docs.notte.cc/quickstart) |
| **Node SDK** | `npm install notte-sdk` (see docs for current coverage) |
| **CDP** | `session.cdp_url()` for Playwright `connect_over_cdp` |
| **REST / Platform API** | https://docs.notte.cc |
| **MCP** | `notte-mcp` — [blog](https://www.notte.cc/blog/mcp-server) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
