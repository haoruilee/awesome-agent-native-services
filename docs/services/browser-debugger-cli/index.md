---
title: "bdg (Browser Debugger CLI) | Agent-Native Services"
service_name: "bdg (Browser Debugger CLI)"
description: "Give your AI agent a real browser. And the DevTools to go with it"
permalink: /services/browser-debugger-cli/
page_kind: service
service_slug: "browser-debugger-cli"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/browser-debugger-cli.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browser-debugger-cli.md"
tagline: "Give your AI agent a real browser. And the DevTools to go with it"
website: "https://github.com/szymdzum/browser-debugger-cli"
repository: "https://github.com/szymdzum/browser-debugger-cli"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · websocket · CLI</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/szymdzum/browser-debugger-cli" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/szymdzum/browser-debugger-cli/wiki/For-AI-Agents" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/szymdzum/browser-debugger-cli" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browser-debugger-cli.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

bdg keeps a **browser session open in the background** and lets an agent drive it **one shell command at a time**: click, fill, navigate, then read requests, console errors, layout, styles and the accessibility tree. Every DevTools capability is reachable through **raw CDP** (`bdg cdp <Method>`), with search and `--describe` introspection. Output is compact and pipes into `jq`, and semantic DOM output cuts tokens versus raw HTML.

---

## Agent-facing interfaces

- **Interaction pattern:** Structured CLI + Agent Skill
- **Catalog protocols:** Agent Skill, websocket, CLI
- **MCP:** ❌ Not provided by design — the project describes itself as "no screenshots and no MCP needed"; agents call it as a shell CLI.
- **Agent Skill:** ✅ Ships an agent skill
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** Structured CLI + Agent Skill

```bash
npm install -g browser-debugger-cli
bdg localhost:3000              # start a background browser session
bdg --help --json               # machine-readable command map for the agent
bdg cdp --search cookie         # discover raw CDP methods
bdg install-skill               # install the bdg skill for Claude Code, Codex, Gemini CLI, ...
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browser-debugger-cli.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **CLI** | `bdg <url>`, `bdg dom …`, `bdg cdp …`, `--json` output, exit codes |
| **CDP** | Unix socket → worker → Chrome DevTools WebSocket |
| **Skill** | `bdg install-skill` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
