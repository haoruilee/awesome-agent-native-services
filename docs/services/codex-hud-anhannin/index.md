---
title: "Codex HUD (anhannin) | Agent-Native Services"
service_name: "Codex HUD (anhannin)"
description: "Codex HUD is an open-source status line HUD for Codex CLI, rendering Claude-HUD style usage and session status directly in the terminal"
permalink: /services/codex-hud-anhannin/
page_kind: service
service_slug: "codex-hud-anhannin"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/codex-hud-anhannin.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/codex-hud-anhannin.md"
tagline: "Codex HUD is an open-source status line HUD for Codex CLI, rendering Claude-HUD style usage and session status directly in the terminal"
website: "https://github.com/anhannin/codex-hud"
repository: "https://github.com/anhannin/codex-hud"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT declared in package metadata; no root or nested LICENSE file as of snapshot</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/anhannin/codex-hud" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/anhannin/codex-hud/tree/master/Codex-HUD" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/anhannin/codex-hud" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/codex-hud-anhannin.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

This independent Codex HUD parses local Codex rollout records and renders model, project, git branch, session usage, and five-hour/seven-day rate-window bars in Codex's terminal footer. It patches Codex to add `[tui].status_line_command`, then configures that command to invoke the local Node.js renderer.

It is distinct from `fwyc0573/codex-hud`: it embeds a compact status line in a patched Codex build rather than wrapping sessions in a managed tmux dashboard. As of the 2026-08-13 snapshot, the repository had 51 stars, no published release/tag, and no commit since 2026-05-10 UTC. It is included as a usable, purpose-built implementation, not as a latest-month momentum pick.

---

## Agent-facing interfaces

- **Interaction pattern:** Patched Codex CLI + status-line command
- **Catalog protocols:** CLI
- **MCP:** ⚠️ No MCP server
- **Agent Skill:** ⚠️ Not published
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** Patched Codex CLI + status-line command

```bash
git clone https://github.com/anhannin/codex-hud.git
cd codex-hud/Codex-HUD
./install.sh

# Start a new session; existing sessions do not pick up the patch.
codex
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/codex-hud-anhannin.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Codex TUI config | `[tui].status_line_command` invokes the local renderer |
| CLI/stdout | `node dist/index.js --status-line --once --no-clear` emits the footer |
| Rollout input | Local `~/.codex/sessions/**/rollout-*.jsonl`, or an explicitly supplied rollout path |
| Git/filesystem | Reads project and branch context from the local working environment |
| Installer | Builds the TypeScript HUD, patches/builds Codex, installs a local binary, and updates config |

There is no REST API, language SDK, MCP server, or published Agent Skill.

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
