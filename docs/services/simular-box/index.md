---
title: "box by Simular | Agent-Native Services"
service_name: "box by Simular"
description: "Give your agents a computer"
permalink: /services/simular-box/
page_kind: service
service_slug: "simular-box"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/simular-box.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/simular-box.md"
tagline: "Give your agents a computer"
verified_at: "2026-11-25"
website: "https://box.simular.ai"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Hosted service closed-source. https://github.com/simular-ai/box-plugin is MIT and contains connectors only</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-25</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://box.simular.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://box.simular.ai/docs/mcp" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/simular-box.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

box is one cloud Linux desktop for the account. The agent opens a browser, clicks, types, reads the screen, and runs shell commands. The desktop sleeps when idle (the M plan is the exception that does not sleep, per `llms.txt`) and wakes when the agent connects. A person can watch and take over at https://box.simular.ai/box. Takeover is optional.

`llms.txt` says a box asleep 14 days in a row is deleted with its files (30 days if the account has ever paid; not while an S or M plan is active). Any wake resets that count. The agent's own model bill stays on the agent's plan. box credits pay for awake time.

---

## Agent-facing interfaces

- **Interaction pattern:** remote MCP after a person's Simular login, or a human-created cb_ key. Not a one-URL join.
- **Catalog protocols:** MCP, http
- **MCP:** ✅ Available — hosted Streamable HTTP
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** remote MCP after a person's Simular login, or a human-created cb_ key. Not a one-URL join.

```text
https://mcp.box.simular.ai/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/simular-box.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Hosted MCP | `https://mcp.box.simular.ai/mcp` |
| Auth | https://box.simular.ai/auth.md |
| Install | https://box.simular.ai/install.md |
| Docs | https://box.simular.ai/docs/mcp |
| Index | https://box.simular.ai/llms.txt |
| Server card | https://box.simular.ai/.well-known/mcp/server-card.json |
| Connectors | https://github.com/simular-ai/box-plugin (MIT, not the desktop) |

---

## Verification

Last verified **2026-11-25**.

Sources:
- https://box.simular.ai
- https://box.simular.ai/llms.txt
- https://box.simular.ai/auth.md
- https://box.simular.ai/install.md
- https://box.simular.ai/docs/mcp
- https://mcp.box.simular.ai/mcp
- https://box.simular.ai/.well-known/mcp/server-card.json
- https://github.com/simular-ai/box-plugin

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
