---
title: "acpx | Agent-Native Services"
service_name: "acpx"
description: "Headless CLI client for stateful Agent Client Protocol (ACP) sessions — so AI agents and orchestrators can talk to coding agents over a structured protocol…"
permalink: /services/acpx/
page_kind: service
service_slug: "acpx"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/acpx.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/acpx.md"
tagline: "Headless CLI client for stateful Agent Client Protocol (ACP) sessions — so AI agents and orchestrators can talk to coding agents over a structured protocol instead of PTY scraping"
website: "https://github.com/openclaw/acpx"
repository: "https://github.com/openclaw/acpx"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Not applicable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · CLI · ACP · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/openclaw/acpx" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/openclaw/acpx/blob/main/docs/CLI.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/openclaw/acpx" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/acpx.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

acpx is a **headless CLI client for the Agent Client Protocol (ACP)**. It enables AI agents and orchestrators to delegate work to coding agents (Pi, OpenClaw, Codex, Claude, etc.) over a structured protocol instead of scraping PTY sessions. One command surface for all ACP-compatible agents.

Core value: **typed ACP messages** (thinking, tool calls, diffs) instead of ANSI scraping. Agents get structured, parseable output and can manage persistent sessions, queue prompts, and cancel in-flight work cooperatively.

---

## Agent-facing interfaces

- **Interaction pattern:** Coding-time Skill + CLI
- **Catalog protocols:** URL onboarding, Agent Skill, CLI, ACP, http
- **MCP:** ⚠️ Not applicable — acpx is a CLI client that implements the ACP protocol. Agents invoke it as a subprocess; it does not expose an MCP server.
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** Coding-time Skill + CLI

```bash
# Install acpx globally (recommended for session reuse)
npm install -g acpx@latest

# Install the acpx skill for full command reference
npx acpx@latest --skill install acpx

# Read the skill reference for all commands and workflows
# Read https://raw.githubusercontent.com/openclaw/acpx/main/skills/acpx/SKILL.md

# Delegate to a coding agent via ACP
npx acpx@latest codex "fix the failing tests"
npx acpx@latest claude "refactor the auth module"
npx acpx@latest exec "one-shot: summarize this repo"
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/acpx.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `acpx` — primary interface; agents invoke via subprocess |
| Config | JSON config files: global + project merge; `acpx config show|init` |
| Skill | `npx acpx@latest --skill install acpx` — installs SKILL.md for agent reference |
| Protocol | Implements [Agent Client Protocol (ACP)](https://agentclientprotocol.com) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
