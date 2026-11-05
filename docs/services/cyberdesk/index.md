---
title: "Cyberdesk | Agent-Native Services"
service_name: "Cyberdesk"
description: "Open source virtual desktops for AI agents"
permalink: /services/cyberdesk/
page_kind: service
service_slug: "cyberdesk"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/cyberdesk.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cyberdesk.md"
tagline: "Open source virtual desktops for AI agents"
website: "https://www.cyberdesk.io"
repository: "https://github.com/cyberdesk-hq/cyberdesk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.cyberdesk.io" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.cyberdesk.io" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/cyberdesk-hq/cyberdesk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cyberdesk.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Cyberdesk provides cloud-hosted virtual desktops that AI agents can control programmatically (mouse, keyboard, screenshot, app/browser interaction) with isolated sessions and auditable execution.

---

## Agent-facing interfaces

- **Catalog protocols:** SDK, API
- **MCP:** ⚠️ Not MCP-first.
- **Agent Skill:** ⚠️ No official SKILL.md package published yet.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
pip install cyberdesk
# then create a desktop and execute computer actions via SDK/API
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cyberdesk.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| SDK/API | Desktop lifecycle + computer-use action primitives |
| Session artifacts | Screenshots/logs for replay, debugging, or compliance review |
| Cloud runtime | Remote execution environment for agent browser/desktop tasks |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
