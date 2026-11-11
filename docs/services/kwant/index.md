---
title: "kwant | Agent-Native Services"
service_name: "kwant"
description: "Your own team of AI bots in one self-hosted binary: spaces, every account you have, handoffs, approvals and routines. Open-source, self-hosted alternative…"
permalink: /services/kwant/
page_kind: service
service_slug: "kwant"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/kwant.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/kwant.md"
tagline: "Your own team of AI bots in one self-hosted binary: spaces, every account you have, handoffs, approvals and routines. Open-source, self-hosted alternative to Grok Bot, Claude Duet and OpenAI dots"
verified_at: "2026-11-10"
website: "https://kwant.si"
repository: "https://github.com/alexsergivan/kwant"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">AGPL-3.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · CLI · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-10</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://kwant.si" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://kwant.si/docs/quickstart" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/alexsergivan/kwant" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/kwant.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

kwant is a self-hosted operator surface and harness for a team of named AI bots in one Rust binary (`kwnt`). It runs on a Mac, Linux or Windows (beta) computer, or on a VPS. Bots share chats, hand work to each other with an @mention, and continue on a schedule or while the person is away. Work shows up as cards on a Mission board, and a task turns **Verified** only when kwant runs the check itself. Spaces keep separate bots, accounts, approvals, and routines. Live activity streams what a concrete bot turn is doing — thinking, each tool, waiting for approval or for the person — over SSE, and keeps that state on the reply after a reload.

The primary consumer is the human operator of that bot team. The primary interface is the local app or `kwnt serve` plus CLI. This entry is admitted on the **operator-surface track**.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + HTTP/SSE daemon (kwnt serve)
- **Catalog protocols:** MCP, REST, CLI, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published as an npx skills add package
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + HTTP/SSE daemon (kwnt serve)

```bash
curl -fsSL https://kwant.si/install.sh | sh
kwnt serve
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/kwant.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI / daemon | `kwnt serve` starts the HTTP/SSE server and embedded web UI |
| Desktop app | Mac, Linux (beta), and Windows (beta); same `~/.kwnt` data folder as the daemon |
| systemd | `ExecStart=/usr/local/bin/kwnt serve --host 0.0.0.0 --port 8799` |
| HTTP/SSE | Live activity and the embedded UI against the local or VPS server |
| REST (person) | Person-only routes such as approval mode switches; bots' own tools refuse them |
| Inbound MCP | Streamable HTTP at `/api/mcp/agents` with a scoped bearer token |
| Install | `curl -fsSL https://kwant.si/install.sh \| sh`, desktop downloads, or Docker Compose |

---

## Verification

Last verified **2026-11-10**.

Sources:
- https://github.com/alexsergivan/kwant/releases/tag/mac-v0.8.2
- https://kwant.si
- https://github.com/alexsergivan/kwant/commit/2c931968680ce26d65ec79e08cbf2527c0d2d25f

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
