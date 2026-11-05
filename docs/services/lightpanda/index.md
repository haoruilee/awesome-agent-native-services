---
title: "Lightpanda | Agent-Native Services"
service_name: "Lightpanda"
description: "The headless browser built from scratch for AI agents and automation"
permalink: /services/lightpanda/
page_kind: service
service_slug: "lightpanda"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/lightpanda.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/lightpanda.md"
tagline: "The headless browser built from scratch for AI agents and automation"
website: "https://lightpanda.io"
repository: "https://github.com/lightpanda-io/browser"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">AGPL-3.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · websocket · CLI · STDIO · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://lightpanda.io" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://lightpanda.io/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/lightpanda-io/browser" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/lightpanda.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Lightpanda is a **from-scratch headless browser** (Zig, V8, not Chromium/WebKit) aimed at **AI agents and automation**. It runs a **Chrome DevTools Protocol (CDP)** server so existing stacks (for example **Puppeteer** via `browserWSEndpoint`) can drive navigation, clicks, and extraction with a small memory footprint versus full Chrome. A **`fetch` CLI** can dump **HTML or markdown** for RAG-style ingestion. A **native MCP mode** exposes browser control directly to MCP clients without a separate adapter process.

---

## Agent-facing interfaces

- **Interaction pattern:** Daemon (CDP) + MCP (stdio) + CLI
- **Catalog protocols:** MCP, websocket, CLI, STDIO, http
- **MCP:** ✅ Available (built into the lightpanda binary)
- **Agent Skill:** ⚠️ No single official npx skills add … bundle from the browser repo; see companion repo for OpenClaw.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** Daemon (CDP) + MCP (stdio) + CLI

```bash
# Nightly binary (see releases) or Docker:
# docker run -d -p 127.0.0.1:9222:9222 lightpanda/browser:nightly

./lightpanda serve --host 127.0.0.1 --port 9222
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/lightpanda.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **CDP** | WebSocket server — connect with `puppeteer.connect({ browserWSEndpoint })` |
| **MCP** | stdio — `lightpanda mcp` — [documentation](https://lightpanda.io/docs/open-source/guides/mcp-server) |
| **CLI** | `lightpanda fetch`, `lightpanda serve` |
| **Docker** | Official image `lightpanda/browser` (see repo README) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
