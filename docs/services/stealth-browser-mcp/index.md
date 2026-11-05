---
title: "Stealth Browser MCP | Agent-Native Services"
service_name: "Stealth Browser MCP"
description: "Stealth browser automation for MCP-compatible AI agents"
permalink: /services/stealth-browser-mcp/
page_kind: service
service_slug: "stealth-browser-mcp"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/stealth-browser-mcp.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/stealth-browser-mcp.md"
tagline: "Stealth browser automation for MCP-compatible AI agents"
verified_at: "2026-10-13"
website: "https://github.com/vibheksoni/stealth-browser-mcp"
repository: "https://github.com/vibheksoni/stealth-browser-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/vibheksoni/stealth-browser-mcp" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/vibheksoni/stealth-browser-mcp#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/vibheksoni/stealth-browser-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/stealth-browser-mcp.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Stealth Browser MCP is a **local MCP browser** built on [nodriver](https://github.com/ultrafunkamsterdam/nodriver), Chrome DevTools Protocol, and FastMCP. Official copy: navigate Cloudflare challenges, anti-bot checks, and login walls with real Chrome-family browsers. It is not a generic Puppeteer wrapper and not a hosted cloud browser.

Features the README actually claims: anti-bot resistance that has passed Cloudflare and Queue-It style checks in testing (results vary); 97 tools in 11 sections; pixel-accurate element cloning via CDP; network inspection; a restricted Python **dynamic hook** system to intercept, block, redirect, fulfill, or modify request/response flows; CDP/JavaScript execution for trusted local clients.

**Distinctness vs catalog browsers:** [Browser MCP](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browser-mcp.md) is a Puppeteer accessibility-tree server. [Playwright MCP](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/playwright-mcp.md) is Microsoft's Playwright tool surface (the README's own comparison table). [Browserbase](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browserbase.md) / [Browser Use Cloud](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browser-use-cloud.md) are hosted remote browsers. This project is a local stealth/anti-detect MCP with nodriver + CDP hooks.

**Freshness:** last push 2026-07-24 at verification.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP
- **Catalog protocols:** Agent Skill, MCP, CLI, STDIO, http
- **MCP:** ✅ Available — this project is the MCP server.
- **Agent Skill:** ✅ Available in-repo (not npx skills add).
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP

```bash
git clone https://github.com/vibheksoni/stealth-browser-mcp.git
cd stealth-browser-mcp
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/stealth-browser-mcp.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP stdio | `venv/bin/python src/server.py` |
| MCP HTTP | `--transport http` + `STEALTH_BROWSER_MCP_AUTH_TOKEN` |
| Agent skill | `skills/stealth-browser-mcp` |
| CLI flags | `--minimal`, `--disable-*`, `--list-sections`, `--debug` |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/vibheksoni/stealth-browser-mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
