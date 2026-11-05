---
title: "Bright Data Agent Browser | Agent-Native Services"
service_name: "Bright Data Agent Browser"
description: "A cloud browser built for AI agents — with built-in website unlocking"
permalink: /services/bright-data-agent-browser/
page_kind: service
service_slug: "bright-data-agent-browser"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/bright-data-agent-browser.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/bright-data-agent-browser.md"
tagline: "A cloud browser built for AI agents — with built-in website unlocking"
website: "https://brightdata.com/ai/agent-browser"
repository: "https://github.com/brightdata/ai-sdk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://brightdata.com/ai/agent-browser" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.brightdata.com/ai/agents" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/brightdata/ai-sdk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/bright-data-agent-browser.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Bright Data Agent Browser is a cloud-hosted browser automation platform designed specifically for AI agents, combining browser infrastructure with **built-in website unlocking** — fingerprinting, CAPTCHA solving, and bot-detection evasion handled transparently. Agents spin up parallel browser sessions via API or MCP, navigate dynamic sites, and extract data at scale without building any unlocking infrastructure themselves.

Unlike general headless browsers, Bright Data's unlocking layer covers 3M+ domains and is continuously updated against anti-bot measures — solving the most common reason agent web automation fails in production.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, API
- **MCP:** ✅ Available (Web MCP — free tier available)
- **Agent Skill:** ⚠️ No official skill published by Bright Data yet.
- **Onboarding type:** `mcp`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Session management, scraping endpoints, data collection APIs |
| Playwright/Puppeteer/Selenium | Standard drivers pointing at Bright Data's cloud browser |
| `@brightdata/ai-sdk` | Vercel AI SDK tools for scraping, searching, structured extraction |
| Web MCP | Model Context Protocol for LLM direct control (free tier available) |
| Proxy API | Direct proxy network access for custom tooling |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
