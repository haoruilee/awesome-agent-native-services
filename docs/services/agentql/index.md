---
title: "AgentQL | Agent-Native Services"
service_name: "AgentQL"
description: "Make the web AI‑ready"
permalink: /services/agentql/
page_kind: service
service_slug: "agentql"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/agentql.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/agentql.md"
tagline: "Make the web AI‑ready"
website: "https://agentql.com"
repository: "https://github.com/tinyfish-io/agentql"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentql.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.agentql.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/tinyfish-io/agentql" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/agentql.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AgentQL connects **LLMs and AI agents to the web** through an **AI-assisted query language**: you describe the data shape (or use NL), and AgentQL resolves elements and extracts **JSON** robust to DOM changes (**self-healing**). It supports **authenticated pages**, **PDFs/images**, a **browserless API** for public pages, and **remote Chromium** with CDP for full agent control.

---

## Agent-facing interfaces

- **Interaction pattern:** REST + Python/JS SDK + Playwright + optional remote browser (CDP)
- **Catalog protocols:** REST, SDK, http, API
- **MCP:** ⚠️ Not documented as a first-party MCP server in this entry — integrate via REST/SDK from your MCP host or community servers if published.
- **Agent Skill:** ⚠️ No official AgentSkills registry entry documented as canonical.
- **Onboarding type:** `sdk`

## How agents onboard

**Interaction pattern:** REST + Python/JS SDK + Playwright + optional remote browser (CDP)

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/agentql.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | https://docs.agentql.com/rest-api/api-reference |
| Python | https://docs.agentql.com/python-sdk/installation |
| JavaScript | https://docs.agentql.com/javascript-sdk/installation |
| Browser / CDP | https://docs.agentql.com/browser |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
