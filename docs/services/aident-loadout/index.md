---
title: "Aident Loadout | Agent-Native Services"
service_name: "Aident Loadout"
description: "Give your agents real capabilities"
permalink: /services/aident-loadout/
page_kind: service
service_slug: "aident-loadout"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/aident-loadout.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/aident-loadout.md"
tagline: "Give your agents real capabilities"
website: "https://aident.ai"
repository: "https://github.com/Aident-AI/aident-skill"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://aident.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.aident.ai/loadout/overview" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Aident-AI/aident-skill" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/aident-loadout.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Aident Loadout is a capability layer for AI agents. After a human connects accounts once in the browser, agents discover and call actions at runtime through one remote MCP endpoint — search by intent, fetch the live input schema, run a side-effect-free preflight that validates input and quotes cost, then execute. Credentials stay in Aident Vault; Audit records what ran, from which client, and at what cost. It also ships 400+ expert-built Skills as task recipes agents can load.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, Agent Skill, MCP, CLI, http
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

```
Follow https://aident.ai/SETUP.md
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/aident-loadout.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Remote MCP | `https://loadout.aident.ai/mcp` (Streamable HTTP, OAuth) |
| Agent Skill | `npx skills add Aident-AI/aident-skill` |
| CLI | `npm i -g @aident-ai/cli` |
| Official MCP Registry | `io.github.Aident-AI/loadout` |
| Docs / URL onboarding | https://aident.ai/SETUP.md |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
