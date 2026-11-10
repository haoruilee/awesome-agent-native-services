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

<section class="service-essay" aria-label="Editorial" markdown="1">

### Cloud versus the open image

Two shapes of Steel exist, and the dossier does not draw the line between them. The `steel-browser` repository is Apache-2.0 and ships a self-hosted Docker image; Steel Cloud is the managed service. CAPTCHA solving, proxy and fingerprint controls, and auto sign-in are described for the product in general, with no note on which of them work outside the cloud. Auto sign-in deserves the closest look. The dossier says it delegates authenticated site access to the platform and that operators must decide which sites agents may reach. Who stores those site credentials, and where, is the question to take to the [Steel docs](https://docs.steel.dev).

There is no official Agent Skill; the dossier points to cookbooks and the MCP server instead.

### Sessions you connect to

The documented primitive is a session: an isolated browser with its own cookies, storage, fingerprint, and connect endpoint. In Python, after `pip install steel-sdk`, the dossier shows `from steel import Steel`, then `client.sessions.create()`, then pointing Playwright, Puppeteer, or Selenium at the session's WebSocket URL. Moving from a local browser means swapping a launch for a connect. The TypeScript SDK installs as `steel-sdk` from npm.

Context injection is the agent-specific part. An agent can save cookies and local storage from one session and inject them into the next, so an authenticated flow resumes without logging in again. A session viewer shows live or recorded sessions for debugging. API keys gate who can create sessions, and the dossier advises against sharing a session across untrusted tenants.

The `steel-mcp-server` runs over stdio and can target either Steel Cloud or a local or self-hosted instance. That is the one place in the dossier where both shapes are plainly supported side by side.

### Among browser services

The [Browser & Web Execution](/categories/browser-and-web-execution/) category and the [browser infrastructure comparison](/guides/browser-infrastructure-for-agents/) cover several similar products. [Browserbase](/services/browserbase/) is the most direct comparison, a web browser for agents and applications. [Browser Use Cloud](/services/browser-use-cloud/) adds a natural-language task mode on top of raw browser control. [Browser MCP](/services/browser-mcp/) and [Vercel Agent Browser](/services/agent-browser/) are lighter tools, an MCP server and a CLI. Steel's tagline, "Browser Infrastructure for AI Agents.", fits; the fact that separates it in the dossier is an open-source browser API you can run yourself.

### Editor's take

Steel is a sensible pick when you want remote browser sessions under Playwright or Puppeteer and need the option to run the same API on your own machines later. If you would rather hand the agent a sentence and get a result back, Browser Use Cloud is closer to that. We have read the dossier and Steel's documentation and repositories, and have not started a session for this page.

</section>

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
