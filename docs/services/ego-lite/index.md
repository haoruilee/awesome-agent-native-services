---
title: "ego lite | Agent-Native Services"
service_name: "ego lite"
description: "The fastest browser for AI agents to run browser automation"
permalink: /services/ego-lite/
page_kind: service
service_slug: "ego-lite"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/ego-lite.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/ego-lite.md"
tagline: "The fastest browser for AI agents to run browser automation"
verified_at: "2026-10-25"
website: "https://lite.ego.app"
repository: "https://github.com/citrolabs/ego-lite"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (skill, ego-browser CLI package and docs in the repo; the desktop browser itself ships as a free binary)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · CLI</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-25</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://lite.ego.app" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://lite.ego.app/document/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/citrolabs/ego-lite" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/ego-lite.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

ego lite is a Chromium-based browser that a person and their AI agents share. Each agent (Claude Code, Codex, Cursor or a custom CLI agent) works in its own isolated Space inside the browser while the person keeps browsing in theirs. The agent reads pages as structured Snapshots and writes a JavaScript snippet that calls the browser tools in one pass, instead of a command-by-command CLI loop.

---

## Agent-facing interfaces

- **Interaction pattern:** local desktop browser + Agent Skill / CLI
- **Catalog protocols:** Agent Skill, CLI
- **MCP:** ⚠️ No MCP server
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** local desktop browser + Agent Skill / CLI

```bash
npx skills add citrolabs/ego-lite
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/ego-lite.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Agent Skill | `skills/ego-browser/SKILL.md`, installed with `npx skills add citrolabs/ego-lite` or by the app |
| CLI | `ego-browser skill`, `ego-browser upgrade` and the in-page tool runner (`package/ego-browser/`) |
| Plugins | Claude Code (`.claude-plugin/`) and Codex (`.codex/`) manifests in the repo |
| Desktop app | Chromium-based browser for macOS (Apple Silicon, Intel) and Windows x64 |

---

## Verification

Last verified **2026-10-25**.

Sources:
- https://github.com/citrolabs/ego-lite/releases/tag/v2.1.0
- https://cdn.ego.app/setup/windows/x64/egoliteSetup-Y7MbxKIuhzFB.exe
- https://lite.ego.app

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
