---
title: "Ruflo | Agent-Native Services"
service_name: "Ruflo"
description: "An agent meta-harness for Claude Code and Codex"
permalink: /services/ruflo/
page_kind: service
service_slug: "ruflo"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/ruflo.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/ruflo.md"
tagline: "An agent meta-harness for Claude Code and Codex"
verified_at: "2026-10-19"
website: "https://github.com/ruvnet/ruflo"
repository: "https://github.com/ruvnet/ruflo"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/ruvnet/ruflo" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/ruvnet/ruflo/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/ruvnet/ruflo" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/ruflo.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Ruflo is an execution layer around Claude Code and Codex. It adds specialized agents, swarm topologies, background workers, persistent vector memory, self-learning trajectories, model routing, budgets, local/cloud execution, plugins, and a zero-trust federation layer for collaboration across machines or organizations. Codex remains the executor; Ruflo coordinates roles and stores reusable state around it.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI initialization + MCP + plugins/Skills
- **Catalog protocols:** Agent Skill, MCP, CLI
- **MCP:** ✅ Primary control surface
- **Agent Skill:** ✅ Bundled
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI initialization + MCP + plugins/Skills

```bash
# Run in the target project
npx ruflo@latest init --codex

# Optional full skill surface
npx ruflo@latest init --codex --full
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/ruflo.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `npx ruflo@latest` initialization, orchestration, memory, federation, and operations |
| MCP | Full CLI-track server plus namespaced plugin MCP tools |
| Codex adapter | `@claude-flow/codex`; generates guidance and registers MCP |
| Plugins/Skills | Marketplace plugins, agent definitions, commands, and skills |
| Federation | Authenticated cross-node agent messaging and trust lifecycle |

---

## Verification

Last verified **2026-10-19**.

Sources:
- https://api.github.com/repos/ruvnet/ruflo

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
