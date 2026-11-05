---
title: "Vessel Browser | Agent-Native Services"
service_name: "Vessel Browser"
description: "Built from the ground-up for agents, Vessel Browser is an open source AI browser for Linux/Windows that provides a durable state, MCP control, and BYOK with…"
permalink: /services/vessel-browser/
page_kind: service
service_slug: "vessel-browser"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/vessel-browser.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/vessel-browser.md"
tagline: "Built from the ground-up for agents, Vessel Browser is an open source AI browser for Linux/Windows that provides a durable state, MCP control, and BYOK with full autonomous browsing"
website: "https://github.com/unmodeled-tyler/vessel-browser"
repository: "https://github.com/unmodeled-tyler/vessel-browser"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Open source · Linux AppImage / npm · early-stage but agent-first by design</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/unmodeled-tyler/vessel-browser" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/unmodeled-tyler/vessel-browser#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/unmodeled-tyler/vessel-browser" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/vessel-browser.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Vessel Browser is a Chromium-based browser whose primary user is an AI agent. It exposes named, **persistent ("durable") browser sessions** that survive restarts, with a human-visible supervisory UI on top so operators can watch what the agent is doing without taking control. Distinguishing primitives include **action undo** (rewind a misclick the agent made), **checkpoints** (snapshot a tab's state and roll back to it), and **editable bookmarks** that the agent reads and writes.

The browser is BYOK — operators connect their own LLM provider — and the data plane (DOM, screenshots, action calls) is mediated through MCP, so any MCP-compatible agent runtime can drive it without a per-agent integration.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, STDIO
- **MCP:** ✅ Available — MCP control plane is a first-class feature.
- **Agent Skill:** ⚠️ Not yet published.
- **Onboarding type:** `mcp`

## How agents onboard

```
# Linux AppImage:
download AppImage from releases → chmod +x → run

# npm:
npm install -g vessel-browser
vessel-browser --mcp   # exposes MCP server for any MCP-compatible agent
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/vessel-browser.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP (stdio) | Browser control tools: navigate, click, type, screenshot, undo, checkpoint, bookmarks |
| CLI | `vessel-browser` for session lifecycle management |
| Linux AppImage / Windows | Local install; no cloud dependency |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
