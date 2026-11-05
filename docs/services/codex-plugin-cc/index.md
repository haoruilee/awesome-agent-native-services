---
title: "Codex plugin for Claude Code (codex-plugin-cc) | Agent-Native Services"
service_name: "Codex plugin for Claude Code (codex-plugin-cc)"
description: "Use Codex from inside Claude Code for code reviews or to delegate tasks to Codex"
permalink: /services/codex-plugin-cc/
page_kind: service
service_slug: "codex-plugin-cc"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/codex-plugin-cc.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/codex-plugin-cc.md"
tagline: "Use Codex from inside Claude Code for code reviews or to delegate tasks to Codex"
website: "https://github.com/openai/codex-plugin-cc"
repository: "https://github.com/openai/codex-plugin-cc"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Not applicable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/openai/codex-plugin-cc" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/openai/codex-plugin-cc/blob/main/README.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/openai/codex-plugin-cc" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/codex-plugin-cc.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

The **Codex plugin for Claude Code** lets a Claude Code session **invoke OpenAI Codex** for read-only reviews, adversarial design review, and **delegated rescue work** (investigate, patch, resume threads) without leaving the Claude Code workflow. It exposes slash commands (`/codex:review`, `/codex:adversarial-review`, `/codex:rescue`, `/codex:status`, `/codex:result`, `/codex:cancel`, `/codex:setup`) and registers a **Codex subagent** for handoffs.

Background jobs integrate with **status/result/cancel** so an orchestrating agent can run long Codex tasks asynchronously. An optional **review gate** (`/codex:setup --enable-review-gate`) hooks Claude’s stop flow to a targeted Codex review before completion.

---

## Agent-facing interfaces

- **Interaction pattern:** Extension / Plugin (Claude Code marketplace plugin wrapping local Codex CLI + app server)
- **Catalog protocols:** CLI, http
- **MCP:** ⚠️ Not applicable — this is a Claude Code plugin that drives the local Codex CLI and Codex app server. It is not itself an MCP server.
- **Agent Skill:** ⚠️ Not yet published as a standalone SKILL.md install via npx skills add
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** Extension / Plugin (Claude Code marketplace plugin wrapping local Codex CLI + app server)

```bash
# In Claude Code: add marketplace and install plugin (see repo README)
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup

# Optional: ensure Codex CLI is installed and signed in
npm install -g @openai/codex
# then from Claude Code: !codex login

# Typical delegation flow
/codex:review --background
/codex:status
/codex:result

# Delegate a fix or investigation to Codex (subagent)
/codex:rescue investigate why the tests started failing
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/codex-plugin-cc.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Claude Code plugin | Marketplace: `openai/codex-plugin-cc` — package `codex@openai-codex` |
| Slash commands | `/codex:*` as documented in repo README |
| Codex CLI | Global `codex` binary — `config.toml` / `.codex/config.toml` per [Codex config](https://developers.openai.com/codex/config-basic) |
| Codex app server | Used by the plugin for Codex integration — [app server docs](https://developers.openai.com/codex/app-server) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
