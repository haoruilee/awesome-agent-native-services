---
title: "Skyvern | Agent-Native Services"
service_name: "Skyvern"
description: "AI agents to automate workflows on any website"
permalink: /services/skyvern/
page_kind: service
service_slug: "skyvern"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/skyvern.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/skyvern.md"
tagline: "AI agents to automate workflows on any website"
website: "https://www.skyvern.com"
repository: "https://github.com/Skyvern-AI/skyvern"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · openapi · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.skyvern.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.skyvern.com/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Skyvern-AI/skyvern" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/skyvern.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Skyvern runs **vision-driven browser automation**: an agent describes a goal in natural language; Skyvern drives a real browser, plans actions, and completes multi-step workflows (forms, logins, downloads, structured extraction) without brittle XPath-only scripts. It supports **CAPTCHA handling**, **2FA/TOTP** flows, **geo-targeted proxies**, **persistent browser sessions**, **JSON-schema extraction**, **webhooks**, and **recordings** for audit. **Skyvern Cloud** offers a production API; the core stack is **open source** for self-hosting.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / REST + optional MCP
- **Catalog protocols:** Agent Skill, MCP, REST, SDK, openapi, http, API
- **MCP:** ✅ Documented as MCP-ready — see Skyvern docs integrations section.
- **Agent Skill:** ⚠️ No single official npx skills add … registry entry documented as primary path.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK / REST + optional MCP

```bash
curl -X POST https://api.skyvern.com/v1/run/tasks \
  -H "x-api-key: $SKYVERN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Find the top 3 posts on Hacker News", "url": "https://news.ycombinator.com"}'
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/skyvern.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | `https://api.skyvern.com` — OpenAPI-linked from docs |
| Python SDK | https://www.skyvern.com/docs/sdk-reference/overview |
| TypeScript SDK | https://www.skyvern.com/docs/ts-sdk-reference/overview |
| Self-hosted | Docker / K8s — own LLM keys |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
