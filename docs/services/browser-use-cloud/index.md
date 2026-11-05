---
title: "Browser Use Cloud | Agent-Native Services"
service_name: "Browser Use Cloud"
description: "State-of-the-art AI browser automation with stealth browsers, CAPTCHA solving, residential proxies, and managed infrastructure"
permalink: /services/browser-use-cloud/
page_kind: service
service_slug: "browser-use-cloud"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/browser-use-cloud.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browser-use-cloud.md"
tagline: "State-of-the-art AI browser automation with stealth browsers, CAPTCHA solving, residential proxies, and managed infrastructure"
website: "https://browser-use.com"
repository: "https://github.com/browser-use/browser-use"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://browser-use.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.cloud.browser-use.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/browser-use/browser-use" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browser-use-cloud.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Browser Use Cloud provides **managed stealth browsers**, **CAPTCHA solving**, **residential proxies**, and two modes: **Agent** (`run()` / `sessions.create()` with NL tasks) and **Browser** (`browsers.create()` with **CDP** control). It targets agents and automation running where local browsers are unavailable (serverless, CI). The **hosted MCP** exposes session/task tools so coding agents drive cloud browsers without custom glue.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK + hosted MCP (HTTP) + Agent or raw CDP browser modes
- **Catalog protocols:** MCP, REST, SDK, http, API
- **MCP:** ✅ Hosted MCP server (HTTP)
- **Agent Skill:** ⚠️ No official npx skills add browser-use/… skill pack documented as canonical.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK + hosted MCP (HTTP) + Agent or raw CDP browser modes

```bash
pip install browser-use-sdk
# or: npm install browser-use-sdk
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browser-use-cloud.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python | `browser-use-sdk` v3 |
| Node.js | `browser-use-sdk` v3 |
| REST | `https://api.browser-use.com/api/v3` (see API reference in docs) |
| MCP | HTTPS + API key header |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
