---
title: "CamoFox Browser | Agent-Native Services"
service_name: "CamoFox Browser"
description: "Stealth headless browser for AI agents — bypass Cloudflare, bot detection, and anti-scraping"
permalink: /services/camofox/
page_kind: service
service_slug: "camofox"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/camofox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/camofox.md"
tagline: "Stealth headless browser for AI agents — bypass Cloudflare, bot detection, and anti-scraping"
website: "https://github.com/jo-inc/camofox-browser"
repository: "https://github.com/jo-inc/camofox-browser"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/jo-inc/camofox-browser" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/jo-inc/camofox-browser" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/jo-inc/camofox-browser" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/camofox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

CamoFox Browser is an anti-detection browser server for AI-driven web automation. It wraps a stealth browser runtime with a server/CLI interface so agents can open pages, maintain sessions, capture screenshots, extract content, and complete web tasks without exposing raw credentials or relying on a human-operated browser window.

---

## Agent-facing interfaces

- **Catalog protocols:** CLI
- **MCP:** ⚠️ No official MCP server found in the main repository at time of listing.
- **Agent Skill:** ⚠️ No official portable Agent Skill package found.
- **Onboarding type:** `cli`

## How agents onboard

```bash
npm install -g camofox-browser
camofox-browser --help
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/camofox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | Install and operate browser sessions from terminal workflows |
| Browser server | Programmatic browser automation endpoint for agents |
| Playwright/Puppeteer-style ecosystem | Designed as a drop-in automation browser for existing agent stacks |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
