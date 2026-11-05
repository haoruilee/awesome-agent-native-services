---
title: "Codex HUD (fwyc0573) | Agent-Native Services"
service_name: "Codex HUD (fwyc0573)"
description: "Real-time statusline HUD for OpenAI Codex CLI. Lightweight, zero-config, works inside tmux"
permalink: /services/codex-hud-fwyc0573/
page_kind: service
service_slug: "codex-hud-fwyc0573"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/codex-hud-fwyc0573.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/codex-hud-fwyc0573.md"
tagline: "Real-time statusline HUD for OpenAI Codex CLI. Lightweight, zero-config, works inside tmux"
verified_at: "2026-09-26"
website: "https://github.com/fwyc0573/codex-hud"
repository: "https://github.com/fwyc0573/codex-hud"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT in package.json; no root LICENSE file as of 2026-09-26</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/fwyc0573/codex-hud" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/fwyc0573/codex-hud#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/fwyc0573/codex-hud" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/codex-hud-fwyc0573.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Codex HUD launches Codex inside a managed tmux layout and renders a persistent terminal surface for model and reasoning effort, context fill, token counts, project/git state, session identity, configured extensions/Skills/hooks/instructions, approval and sandbox state, MCP/tool activity, and direct-child/subagent activity. A multi-session view aggregates active root sessions; typed agent paths preserve the visible subagent tree.

Its wrapper also provides bounded session operations: list, attach, create, diagnose, resume, or kill HUD-owned sessions. It observes Codex rather than replacing its reasoning or permission system, and it does not claim to authorize tool calls merely because it displays their state.

---

## Agent-facing interfaces

- **Interaction pattern:** Codex wrapper CLI + tmux operator surface
- **Catalog protocols:** CLI
- **MCP:** ⚠️ No MCP server
- **Agent Skill:** ⚠️ Not published
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** Codex wrapper CLI + tmux operator surface

```text
Install codex-hud (https://github.com/fwyc0573/codex-hud) for the Codex CLI by following the instructions in its README.md.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/codex-hud-fwyc0573.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Wrapper CLI | `codex`, `cx`, `codex-resume`, and passthrough Codex arguments |
| Management CLI | `codex-hud --list|--attach|--new-session|--kill|--self-check` plus sync/upgrade/uninstall helpers |
| Codex inputs | Local `config.toml`, rollout/session JSONL, instruction/Skill/hook configuration, and git state |
| Terminal surface | tmux status pane with single-session and multi-session modes |
| Local state | Update/session state and logs under the XDG state directory or `~/.local/state/codex-hud/` |

There is no REST API, language SDK, or MCP transport.

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/fwyc0573/codex-hud/releases/tag/v1.2
- https://api.github.com/repos/fwyc0573/codex-hud

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
