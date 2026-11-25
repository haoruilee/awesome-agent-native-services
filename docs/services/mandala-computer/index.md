---
title: "Mandala Computer | Agent-Native Services"
service_name: "Mandala Computer"
description: "Computers for AI Agents"
permalink: /services/mandala-computer/
page_kind: service
service_slug: "mandala-computer"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/mandala-computer.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mandala-computer.md"
tagline: "Computers for AI Agents"
verified_at: "2026-11-25"
website: "https://mandala.computer"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Hosted service closed-source. Local MCP package mandala-computer-mcp on npm</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · websocket · webhook · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-25</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mandala.computer" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://app.mandala.computer/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mandala-computer.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Mandala Computer is a persistent cloud desktop for an agent. `llms.txt` describes creating a Linux machine, watching the screen, clicking and typing, running commands, opening a terminal, moving files, and snapshotting. Each computer has a websocket event stream, and webhooks can POST the same events. A built-in agent loop can drive a computer from one prompt, with threads and background runs (`POST /computers/{id}/agent/runs` in `llms.txt`). Public HTTPS URLs can front a port inside the computer.

The computer stays. It is not a headless browser session and not a one-shot sandbox that disappears with the process.

---

## Agent-facing interfaces

- **Interaction pattern:** hosted MCP with browser OAuth, or a human-minted API key. Not a one-URL join.
- **Catalog protocols:** MCP, websocket, webhook, http, API
- **MCP:** ✅ Available — hosted Streamable HTTP, plus a local stdio package
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** hosted MCP with browser OAuth, or a human-minted API key. Not a one-URL join.

```bash
# Hosted MCP: https://app.mandala.computer/mcp
# Local stdio: npx mandala-computer-mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mandala-computer.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP API | https://app.mandala.computer/docs |
| Hosted MCP | `https://app.mandala.computer/mcp` |
| Local MCP | `npx mandala-computer-mcp` |
| Index | https://mandala.computer/llms.txt |
| Events | Websocket stream and webhooks (`llms.txt`) |

---

## Verification

Last verified **2026-11-25**.

Sources:
- https://mandala.computer
- https://mandala.computer/llms.txt
- https://app.mandala.computer/docs
- https://app.mandala.computer/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
