---
title: "Scrapybara | Agent-Native Services"
service_name: "Scrapybara"
description: "A COMPUTER FOR YOUR AI"
permalink: /services/scrapybara/
page_kind: service
service_slug: "scrapybara"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/scrapybara.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/scrapybara.md"
tagline: "A COMPUTER FOR YOUR AI"
website: "https://scrapybara.com"
repository: "https://github.com/Scrapybara/scrapybara-python"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://scrapybara.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.scrapybara.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Scrapybara/scrapybara-python" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/scrapybara.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Scrapybara hosts **remote desktops for computer-use agents** (OpenAI CUA and similar): spin up **Ubuntu**, **browser-only**, or **Windows** VMs in milliseconds, stream the desktop, run **bash**, **file edits**, and **browser automation** via Playwright. It supports **authenticated browser state** (save/load), **pause/resume**, and **hundreds of concurrent instances** for parallel agent workloads.

---

## Agent-facing interfaces

- **Interaction pattern:** Python/TypeScript SDK + Act SDK + MCP
- **Catalog protocols:** MCP, REST
- **MCP:** ✅ Community/org MCP repo
- **Agent Skill:** ⚠️ No official ClawHub skill pack documented as canonical.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** Python/TypeScript SDK + Act SDK + MCP

```bash
pip install scrapybara
# or: npm install scrapybara
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/scrapybara.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python | `scrapybara` on PyPI |
| TypeScript | `scrapybara` on npm |
| REST | Per docs |
| MCP | `scrapybara-mcp` repo |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
