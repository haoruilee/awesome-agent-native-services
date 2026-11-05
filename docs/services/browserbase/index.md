---
title: "Browserbase | Agent-Native Services"
service_name: "Browserbase"
description: "A web browser for AI agents & applications"
permalink: /services/browserbase/
page_kind: service
service_slug: "browserbase"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/browserbase.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browserbase.md"
tagline: "A web browser for AI agents & applications"
website: "https://browserbase.com"
repository: "https://github.com/browserbase/stagehand"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://browserbase.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.browserbase.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/browserbase/stagehand" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browserbase.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Browserbase provides managed, cloud-hosted headless browser infrastructure specifically for AI agents. Agents spin up isolated browser sessions via API, control them through Playwright, Puppeteer, or Selenium — or through the Stagehand SDK using natural-language web actions — and destroy them when done. The entire browser lifecycle is agent-controlled, with no human sitting at a keyboard.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skills published at browserbase/skills
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Session lifecycle management (create, list, delete) |
| Playwright | Standard Playwright over CDP pointing to remote session |
| Puppeteer | Standard Puppeteer over CDP pointing to remote session |
| Selenium | Standard Selenium WebDriver pointing to remote session |
| Chrome DevTools Protocol | Low-level CDP access for custom tooling |
| Stagehand SDK | Natural-language action layer built on Browserbase |
| MCP Server | Model Context Protocol for direct LLM browser control |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
