---
title: "OpenCLI | Agent-Native Services"
service_name: "OpenCLI"
description: "Make any website, Electron App, or Local Tool your CLI"
permalink: /services/opencli/
page_kind: service
service_slug: "opencli"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/opencli.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/opencli.md"
tagline: "Make any website, Electron App, or Local Tool your CLI"
website: "https://opencli.info/"
repository: "https://github.com/jackwener/opencli"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Not applicable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · CLI</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://opencli.info/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/jackwener/opencli/blob/main/README.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/jackwener/opencli" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/opencli.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

OpenCLI turns websites, **Electron desktop apps** (e.g. Cursor, Codex, Notion, Discord), and **local binaries** into a **unified CLI** with structured output. A Chrome extension plus localhost daemon reuses the user’s real browser session for authenticated sites; public API sites can run without the bridge. It also **passthroughs** external CLIs (`gh`, `docker`, `kubectl`, etc.) and lets users **`opencli register`** custom local tools so `opencli list` exposes one discovery surface for an agent.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI (Bash) + optional repo SKILL.md
- **Catalog protocols:** Agent Skill, CLI
- **MCP:** ⚠️ Not applicable as Model Context Protocol — OpenCLI is a CLI and local browser bridge. (The codebase uses an internal BrowserBridge type historically aliased in mcp.ts; it is not an MCP server.)
- **Agent Skill:** ✅ Published in the upstream repository (AgentSkills-style front matter)
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI (Bash) + optional repo SKILL.md

```bash
npm install -g @jackwener/opencli

# Discover every site command and external CLI passthrough
opencli list
opencli list -f yaml

# Example: structured output for agents
opencli hackernews top --limit 5 -f json
opencli bilibili hot --limit 5 -f json
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/opencli.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `opencli` — primary agent integration |
| npm | `npm install -g @jackwener/opencli` |
| Module | `import … from '@jackwener/opencli/registry'` (see package `exports`) |
| HTTP (local) | Daemon status/logs on configurable port (default `19825`) — operational, not the main agent API |
| Docs | `SKILL.md`, `CLI-EXPLORER.md`, `CLI-ONESHOT.md` in repo |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
