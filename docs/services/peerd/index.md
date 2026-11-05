---
title: "peerd | Agent-Native Services"
service_name: "peerd"
description: "peerd: the AI agent harness native to the browser"
permalink: /services/peerd/
page_kind: service
service_slug: "peerd"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/peerd.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/peerd.md"
tagline: "peerd: the AI agent harness native to the browser"
verified_at: "2026-09-20"
website: "https://peerd.ai"
repository: "https://github.com/NotASithLord/peerd"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">A2A · http · documentation</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://peerd.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/NotASithLord/peerd/blob/main/README.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/NotASithLord/peerd" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/peerd.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

peerd is a browser extension that runs a full agent harness *inside* the browser you already use. The agent can drive your tabs and signed-in sessions, run sealed JS notebooks, compiled WASI tools, client-side apps, and WASM Linux VMs, and — on preview builds — talk to other peerd browsers over WebRTC.

The homepage thesis: native and cloud apps drive the browser from outside; peerd lives inside it. No background host process, no sidecar, no peerd cloud, no external tool broker. Model calls go to the provider you configured (or local Ollama / planned WebGPU). Current builds send no product telemetry to peerd.

**Category honesty:** this is a **harness**, not a remote browser-as-a-service. Browser & Web Execution in this catalog is for managed / remote browser sessions. peerd inverts that: the user's browser *is* the runtime, hypervisor, and control plane.

---

## Agent-facing interfaces

- **Interaction pattern:** Browser extension (load unpacked) — local harness, no peerd account
- **Catalog protocols:** A2A, http, documentation
- **MCP:** ⚠️ Not published — and not the architecture.
- **Agent Skill:** ⚠️ Not published as an official npx skills add pack.
- **Onboarding type:** `documentation`

## How agents onboard

**Interaction pattern:** Browser extension (load unpacked) — local harness, no peerd account

```bash
git clone https://github.com/NotASithLord/peerd.git
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/peerd.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Browser extension | Load `extension/` (Chromium) or packaged Firefox XPI |
| Homepage / thesis | https://peerd.ai |
| Source / docs | https://github.com/NotASithLord/peerd — `CLAUDE.md`, `SECURITY.md`, `docs/` |
| Preview A2A | `peerd-distributed` WebRTC mesh (omitted from store builds) |
| MCP | Not shipped |
| Hosted API | None — "no backend" |

---

## Verification

Last verified **2026-09-20**.

Sources:
- https://news.ycombinator.com/item?id=48646165

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
