---
title: "Obscura | Agent-Native Services"
service_name: "Obscura"
description: "The open-source headless browser for AI agents and web scraping"
permalink: /services/obscura/
page_kind: service
service_slug: "obscura"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/obscura.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/obscura.md"
tagline: "The open-source headless browser for AI agents and web scraping"
website: "https://obscura.sh"
repository: "https://github.com/h4ckf0r0day/obscura"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://obscura.sh" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.obscura.sh" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/h4ckf0r0day/obscura" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/obscura.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Obscura is a **from-scratch headless browser engine written in Rust** that runs real JavaScript via V8 and speaks the **Chrome DevTools Protocol**, so it works as a drop-in replacement for headless Chrome with Puppeteer and Playwright. The project reports ~30 MB memory per instance versus 200+ MB for headless Chrome. Release builds include a native rendering engine (screenshots, screencast, PDF export without Chromium), and an optional stealth build adds anti-detection. A built-in **MCP server** keeps a live browser session and exposes snapshot/act tools with element references to agents.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP (stdio or HTTP) + Daemon (CDP) + CLI
- **Catalog protocols:** MCP, CLI, STDIO, http
- **MCP:** ✅ Available (built into the obscura binary)
- **Agent Skill:** ⚠️ No official Agent Skill bundle; agents use the built-in MCP server or CDP.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP (stdio or HTTP) + Daemon (CDP) + CLI

```bash
# Download a release binary or Docker image (see GitHub releases), then:
obscura mcp                         # stdio MCP for Claude Desktop / Cursor / Claude Code
obscura mcp --http --port 3000      # Streamable HTTP MCP at http://127.0.0.1:3000/mcp
obscura serve                       # CDP server at ws://127.0.0.1:9222 for Puppeteer/Playwright
obscura fetch https://example.com   # one-shot fetch
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/obscura.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **MCP** | `obscura mcp` (stdio) or `obscura mcp --http --port 3000` (`/mcp`) |
| **CDP** | `obscura serve` — `ws://127.0.0.1:9222` |
| **CLI** | `obscura fetch <url>` with `--eval`, `--screenshot`, `--output` |
| **Library** | Rust crate via git dependency |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
