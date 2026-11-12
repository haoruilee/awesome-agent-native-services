---
title: "Phonebox | Agent-Native Services"
service_name: "Phonebox"
description: "The agent-first cloud phone: cloud Android phones that AI agents can see and control, billed per second"
permalink: /services/phonebox/
page_kind: service
service_slug: "phonebox"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/phonebox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/phonebox.md"
tagline: "The agent-first cloud phone: cloud Android phones that AI agents can see and control, billed per second"
verified_at: "2026-11-12"
website: "https://phonebox.dev"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · openapi · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-12</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://phonebox.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://phonebox.dev/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/phonebox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Phonebox provisions cloud Android phones that an agent can see and control. The agent reads the screen as text, taps, types, installs APKs, and parks the phone when it is done. Phones park when idle and keep their apps and sign-ins. Billing is $0.06 per minute, billed per second, with parked phones free, as stated on Phonebox's own guides (check https://phonebox.dev/docs/billing/plans for current plans). A new account starts with a 7-day free week (card required).

---

## Agent-facing interfaces

- **Interaction pattern:** agent-readable setup document + CLI + hosted MCP + REST.
- **Catalog protocols:** Agent Skill, MCP, REST, CLI, openapi, http
- **MCP:** ✅ Available (hosted)
- **Agent Skill:** ✅ Available (hosted SKILL.md, not an npx skills add registry package)
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** agent-readable setup document + CLI + hosted MCP + REST.

```bash
npm install -g https://phonebox.dev/downloads/phonebox-0.1.0.tgz
phonebox setup --no-wait
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/phonebox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Setup | https://phonebox.dev/setup.md — CLI or `POST /v1/setup` |
| MCP | `https://phonebox.dev/mcp` |
| REST | OpenAPI at https://phonebox.dev/openapi.json |
| Skill | https://phonebox.dev/skills/phonebox/SKILL.md |
| CLI | `npm install -g https://phonebox.dev/downloads/phonebox-0.1.0.tgz` |

---

## Verification

Last verified **2026-11-12**.

Sources:
- https://phonebox.dev

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
