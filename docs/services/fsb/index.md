---
title: "FSB (Full Self Browsing) | Agent-Native Services"
service_name: "FSB (Full Self Browsing)"
description: "DOM-first AI browser automation for Chrome and MCP clients"
permalink: /services/fsb/
page_kind: service
service_slug: "fsb"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/fsb.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/fsb.md"
tagline: "DOM-first AI browser automation for Chrome and MCP clients"
verified_at: "2026-10-20"
website: "https://full-selfbrowsing.com"
repository: "https://github.com/fullselfbrowsing/FSB"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · websocket · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://full-selfbrowsing.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/fullselfbrowsing/FSB/blob/main/mcp/README.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/fullselfbrowsing/FSB" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/fsb.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

FSB is an open-source browser extension plus a local MCP server that lets an AI agent drive the person's own signed-in browser (Chrome, Edge, Brave or Chromium 116+). The agent reads the live page as structure (DOM, element refs, selectors, ARIA labels, form state) instead of screenshots. It acts with clicks, typing, keys, scrolling, navigation, tabs, spreadsheet ranges and real file uploads, and FSB checks each step against the page.

The MCP surface has two modes. In manual mode the agent plans each step itself using about 70 tools ([tool reference](https://github.com/fullselfbrowsing/FSB/blob/main/mcp/README.md#tools-69-total)). In autopilot mode the agent calls `run_task` with a natural-language goal and FSB's own loop picks the steps, sending a progress heartbeat every 30 seconds. A capability catalog covering 128 apps (`search_capabilities` / `invoke_capability`) runs verified first-party API actions inside the person's authenticated session; entries that are not yet verified come back labelled pending instead of executing. Trigger watchers watch one page element for threshold, delta, regex or compound conditions and report back to the calling agent.

FSB also has a standalone mode in which a person types a task into the extension popup or side panel with their own model API key. That is a secondary surface; the MCP path needs no FSB key. FSB is intentionally not a stealth browser or scraper farm, and it works only while the browser and the extension are open.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP + browser extension (local bridge)
- **Catalog protocols:** Agent Skill, MCP, websocket, CLI, STDIO, http
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP + browser extension (local bridge)

```bash
npx -y fsb-mcp-server@latest install --claude-code
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/fsb.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP (stdio) | `npx -y fsb-mcp-server` |
| MCP (Streamable HTTP) | `npx -y fsb-mcp-server@latest serve`; endpoint `http://127.0.0.1:7226/mcp`, health at `http://127.0.0.1:7226/health` |
| Extension bridge | WebSocket on `ws://localhost:7225`; several MCP clients share one hub |
| CLI | `fsb-mcp-server install --<client>`, `doctor`, `--dry-run` |
| Agent Skill | `skills/fsb/SKILL.md` with doctor and config-print scripts |
| Extension UI | Popup and side panel for standalone natural-language runs (secondary surface) |

---

## Verification

Last verified **2026-10-20**.

Sources:
- https://github.com/fullselfbrowsing/FSB/releases/tag/mcp-v0.11.2
- https://registry.npmjs.org/fsb-mcp-server/latest
- https://full-selfbrowsing.com
- https://github.com/fullselfbrowsing/FSB/blob/main/mcp/README.md
- https://clawhub.ai/lakshmanturlapati/full-selfbrowsing

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
