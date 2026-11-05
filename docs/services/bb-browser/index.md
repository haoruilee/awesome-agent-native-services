---
title: "bb-browser | Agent-Native Services"
service_name: "bb-browser"
description: "Your browser is the API. No keys. No bots. No scrapers"
permalink: /services/bb-browser/
page_kind: service
service_slug: "bb-browser"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/bb-browser.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/bb-browser.md"
tagline: "Your browser is the API. No keys. No bots. No scrapers"
website: "https://github.com/epiral/bb-browser"
repository: "https://github.com/epiral/bb-browser"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/epiral/bb-browser" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/epiral/bb-browser" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/bb-browser.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

bb-browser (BadBoy Browser) gives AI agents access to the entire authenticated internet by **routing commands through the user's real Chrome browser** — not a headless bot, not a scraper, not a reverse-engineered API. The agent calls a CLI command or MCP tool; bb-browser runs `fetch()` or `eval()` inside the user's actual browser tab, where the user is already logged in.

The core insight: **99% of websites don't offer public APIs, but they all accept browser requests. The user's authenticated session is the API.**

103 commands across 36 platforms are available instantly. Adding a new website takes an AI agent ~10 minutes to reverse-engineer autonomously.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, CLI, STDIO, http, API
- **MCP:** ✅ Available (built-in)
- **Agent Skill:** ✅ Available on ClawHub
- **Onboarding type:** `cli`

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `bb-browser site <platform>/<command>` — 103 commands, all `--json` |
| MCP Server | `npx -y bb-browser --mcp` — stdio transport |
| HTTP Daemon | `localhost:19824` — local REST API |
| Chrome Extension | SSE bridge from daemon to browser; CDP-level control |
| OpenClaw Mode | `--openclaw` flag for OpenClaw browser integration |
| `--jq` | Inline JSON filtering with jq expressions |
| `--tab <id>` | Concurrent multi-tab operations |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
