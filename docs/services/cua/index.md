---
title: "Cua | Agent-Native Services"
service_name: "Cua"
description: "Scale computer fleets for every agent"
permalink: /services/cua/
page_kind: service
service_slug: "cua"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/cua.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cua.md"
tagline: "Scale computer fleets for every agent"
verified_at: "2026-09-20"
website: "https://cua.ai"
repository: "https://github.com/trycua/cua"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · SDK · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://cua.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://cua.ai/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/trycua/cua" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cua.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Cua gives computer-use agents real machines and a background driver. **Cua Fleets** keep warm pools of Linux, Windows, macOS, and Android desktops that code can claim for evals, RL, data generation, or batch rollouts. **Cua Driver** lets an agent click, type, scroll, read accessibility trees, and capture window state on macOS, Windows, and Linux without stealing the operator's cursor or focus when the platform supports background delivery. **Lume** manages local Apple Silicon VMs. **Cua Bench** authors and scores computer-use tasks. **CUA-S1** is a family of small specialist models for bounded GUI decisions (first profile: forms).

Computer-Use 2.0 in Cua's docs treats the GUI as one tool surface beside code, shell, files, and APIs — not as a standalone "AI browser" product.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP (stdio) + Sandbox / Fleet SDK
- **Catalog protocols:** Agent Skill, MCP, CLI, SDK, http
- **MCP:** ✅ Available (Cua Driver stdio; Cua CLI also documents a CLI MCP server)
- **Agent Skill:** ✅ Available via the Driver binary (filesystem skill + MCP skill://cua-driver/ resources)
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP (stdio) + Sandbox / Fleet SDK

```bash
# macOS / Linux
/bin/bash -c "$(curl -fsSL https://cua.ai/driver/install.sh)"

# Windows (PowerShell)
irm https://cua.ai/driver/install.ps1 | iex

cua-driver --version
cua-driver call list_apps
cua-driver mcp-config --client <client>
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cua.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Cua Driver CLI / MCP | `cua-driver` — https://cua.ai/docs/how-to-guides/driver/install |
| Agent skill | `cua-driver skills install` + embedded `skill://cua-driver/` |
| Sandbox SDK | Python `cua-sandbox` — local and cloud runtimes |
| Fleet SDK | TypeScript `@trycua/fleet`; cloud pools at https://run.cua.ai |
| Lume CLI | https://cua.ai/lume/install.sh |
| Cua Bench | `uv tool install 'cua-bench[browser]'` |
| Docs index | https://cua.ai/docs |

---

## Verification

Last verified **2026-09-20**.

Sources:
- https://news.ycombinator.com/item?id=49767564

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
