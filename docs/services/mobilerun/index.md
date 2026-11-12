---
title: "Mobilerun | Agent-Native Services"
service_name: "Mobilerun"
description: "Give your AI Agent a phone"
permalink: /services/mobilerun/
page_kind: service
service_slug: "mobilerun"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/mobilerun.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mobilerun.md"
tagline: "Give your AI Agent a phone"
verified_at: "2026-11-12"
website: "https://mobilerun.ai"
repository: "https://github.com/droidrun/mobilerun"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (open-source framework)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · SDK · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-12</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mobilerun.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.mobilerun.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/droidrun/mobilerun" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mobilerun.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Mobilerun gives an AI agent a real Android or iOS phone — hosted in the cloud, connected from a desk, or driven locally through the MIT framework. The agent inspects the accessibility tree and screenshots, then taps, swipes, and types. Cloud phones can keep apps and data between sessions, use residential network routing, and optionally attach a receive-only number or inbox for verification messages.

The same framework that runs locally is what powers the cloud. `pip`/`uv` install is enough to try it on a device you already own; moving to hosted devices is a Cloud SDK / MCP configuration change.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI (local framework) + Cloud REST / Python / TypeScript SDK + hosted MCP.
- **Catalog protocols:** Agent Skill, MCP, CLI, SDK, http, API
- **MCP:** ✅ Available (hosted Cloud MCP)
- **Agent Skill:** ✅ Available via the mobile-harness skill (MIT), linked from the framework README. A separate "Mobilerun Agents · MCP skill" is documented at https://docs.mobilerun.ai/skills/assistant-mcp.md for the hosted-agent approval flow.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI (local framework) + Cloud REST / Python / TypeScript SDK + hosted MCP.

```bash
uv tool install mobilerun
mobilerun setup
mobilerun configure
mobilerun run "Open settings and turn on dark mode"
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/mobilerun.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Local CLI / Python | `uv tool install mobilerun` / `uv pip install mobilerun` — https://github.com/droidrun/mobilerun |
| Hosted MCP | `https://cloud.mobilerun.ai/api/mcp` |
| Cloud SDK | `@mobilerun/sdk`, `mobilerun-sdk` (from `llms.txt`) |
| Machine-readable docs | https://mobilerun.ai/llms.txt · https://docs.mobilerun.ai/llms.txt |

---

## Verification

Last verified **2026-11-12**.

Sources:
- https://github.com/droidrun/mobilerun

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
