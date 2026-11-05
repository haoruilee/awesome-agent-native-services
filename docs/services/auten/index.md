---
title: "Auten | Agent-Native Services"
service_name: "Auten"
description: "Give your AI agent hands. It clicks, types and sees your screen"
permalink: /services/auten/
page_kind: service
service_slug: "auten"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/auten.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/auten.md"
tagline: "Give your AI agent hands. It clicks, types and sees your screen"
verified_at: "2026-10-11"
website: "https://auten.ai"
repository: "https://github.com/auten-ai/auten-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT for the docs, client configs and @autenai/mcp launcher; the runner is closed source (terms)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-11</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://auten.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/auten-ai/auten-mcp" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/auten-ai/auten-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/auten.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Auten lets an MCP client operate the user's real computer: macOS, Windows 10/11 or Linux (X11), plus an Android phone over USB (beta). The agent reads the frontmost app as numbered accessibility elements with the visible text, then clicks, types, fills forms and reads the screen in apps that have no API.

When the agent has worked a task out once, it can save the run as a skill with parameters and replay it later without calling the model. If the app changes and a step breaks, the agent repairs that skill from the failing step. The site reports 17 s for a task done with the model versus 9 s replayed.

Passwords are typed locally from the system keychain (or a private local vault on Linux) and never reach the model.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP (stdio) + local runner (installer)
- **Catalog protocols:** MCP, CLI, STDIO, http
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published as an npx skills package
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP (stdio) + local runner (installer)

```bash
curl -fsSL https://auten.ai/install | bash
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/auten.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP (stdio) | `npx -y @autenai/mcp` — https://github.com/auten-ai/auten-mcp |
| CLI | `auten` (`auten connect`, `auten mcp-bridge`, `auten key add` for your own model key) |
| Claude Code plugin | `/plugin marketplace add auten-ai/auten-mcp` |
| Agent setup file | https://github.com/auten-ai/auten-mcp/blob/main/llms-install.md |
| Installers | https://auten.ai/install (macOS/Linux), `install.ps1` (Windows) |

---

## Verification

Last verified **2026-10-11**.

Sources:
- https://github.com/auten-ai/auten-mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
