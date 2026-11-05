---
title: "Claude HUD | Agent-Native Services"
service_name: "Claude HUD"
description: "A Claude Code plugin that shows what's happening"
permalink: /services/claude-hud/
page_kind: service
service_slug: "claude-hud"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/claude-hud.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/claude-hud.md"
tagline: "A Claude Code plugin that shows what's happening"
verified_at: "2026-09-30"
website: "https://github.com/jarrodwatts/claude-hud"
repository: "https://github.com/jarrodwatts/claude-hud"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">documentation</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/jarrodwatts/claude-hud" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/jarrodwatts/claude-hud#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/jarrodwatts/claude-hud" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/claude-hud.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Claude HUD is a purpose-built operator surface for a live Claude Code session. It renders model/provider, project/git, context-window fill, usage/rate-limit windows, and optional lines for in-flight tools, subagents, and todos. It is read-only observation: it does not enqueue work, approve tools, or mint credentials.

This is the same class of surface as the catalog's Codex HUD entries, admitted on the **operator-surface track**.

---

## Agent-facing interfaces

- **Interaction pattern:** Claude Code plugin + status-line protocol
- **Catalog protocols:** documentation
- **MCP:** ⚠️ No MCP server
- **Agent Skill:** ⚠️ Plugin commands, not a portable SKILL.md package
- **Onboarding type:** `other`

## How agents onboard

**Interaction pattern:** Claude Code plugin + status-line protocol

```text
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud
/reload-plugins
/claude-hud:setup
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/claude-hud.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Plugin | `/plugin marketplace add jarrodwatts/claude-hud` |
| Statusline | stdin JSON → stdout render; 300ms debounce |
| Transcript | JSONL for tools, agents, todos |
| Configure | `/claude-hud:configure` or edit config JSON |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://github.com/jarrodwatts/claude-hud/releases/tag/v0.8.0

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
