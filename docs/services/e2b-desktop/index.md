---
title: "E2B Desktop | Agent-Native Services"
service_name: "E2B Desktop"
description: "Build AI agents that see, understand, and control virtual Linux desktops using E2B Desktop sandboxes"
permalink: /services/e2b-desktop/
page_kind: service
service_slug: "e2b-desktop"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/e2b-desktop.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/e2b-desktop.md"
tagline: "Build AI agents that see, understand, and control virtual Linux desktops using E2B Desktop sandboxes"
verified_at: "2026-11-12"
website: "https://e2b.dev"
repository: "https://github.com/e2b-dev/desktop"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-12</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://e2b.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.e2b.dev/use-cases/computer-use" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/e2b-dev/desktop" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/e2b-desktop.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

E2B Desktop is an open-source virtual computer for computer-use agents. Each sandbox is a Linux desktop (Ubuntu 22.04, XFCE) with mouse, keyboard, screenshot, window, and bash APIs, plus optional VNC streaming so a person can watch (and, depending on stream settings, interact). The SDK is meant to be wired to any LLM that can look at a screenshot and return a desktop action — the docs mention OpenAI Computer Use and Anthropic Claude as examples.

It shares E2B's account and API key with the code-execution sandbox, but the primitive is a graphical desktop, not a code interpreter.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK (@e2b/desktop / e2b-desktop).
- **Catalog protocols:** SDK, http
- **MCP:** ⚠️ No Desktop-specific MCP server is documented on https://github.com/e2b-dev/desktop or https://docs.e2b.dev/use-cases/computer-use. (The broader E2B platform has a separate MCP server for sandboxes; that is covered on the E2B listing and was not verified here as a Desktop computer-use transport.)
- **Agent Skill:** ⚠️ No official SKILL.md / npx skills add package was found on the Desktop repo or computer-use docs page reviewed.
- **Onboarding type:** `sdk`

## How agents onboard

**Interaction pattern:** SDK (@e2b/desktop / e2b-desktop).

```bash
pip install e2b-desktop
# or: npm i @e2b/desktop
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/e2b-desktop.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install e2b-desktop` — `from e2b_desktop import Sandbox` |
| JS/TS SDK | `npm i @e2b/desktop` — `import { Sandbox } from '@e2b/desktop'` |
| Docs | https://docs.e2b.dev/use-cases/computer-use |
| Example agent | https://github.com/e2b-dev/surf — demo https://surf.e2b.dev |

---

## Verification

Last verified **2026-11-12**.

Sources:
- https://github.com/e2b-dev/desktop

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
