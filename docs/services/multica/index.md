---
title: "Multica | Agent-Native Services"
service_name: "Multica"
description: "AI-native project management — like Linear, but with AI agents as first-class team members"
permalink: /services/multica/
page_kind: service
service_slug: "multica"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/multica.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/multica.md"
tagline: "AI-native project management — like Linear, but with AI agents as first-class team members"
website: "https://multica.ai"
repository: "https://github.com/multica-ai/multica"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">websocket · CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://multica.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/multica-ai/multica" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/multica.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Multica is an **open-source, AI-native issue tracker and coordination layer** for software teams. Humans and **coding agents** share the same board: agents appear in the assignee picker, receive issues, update status, comment, and run work **locally** through a **daemon** that wraps Claude Code and OpenAI Codex. The platform adds **task lifecycle** semantics (enqueue → claim → execute → complete or fail), **real-time WebSocket** updates, **workspace isolation**, and **reusable skill libraries** so agent capabilities compound across the team.

You can use **Multica Cloud** at multica.ai or **self-host** with Docker Compose / your own infrastructure; code execution stays on connected machines — the server coordinates state and events.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + local agent daemon (hosted cloud or self-hosted backend)
- **Catalog protocols:** websocket, CLI, http
- **MCP:** ⚠️ Not yet published
- **Agent Skill:** ⚠️ Not yet published (agentskills.io / ClawHub install path)
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + local agent daemon (hosted cloud or self-hosted backend)

```bash
# Install CLI (macOS/Linux via Homebrew)
brew tap multica-ai/tap
brew install multica-cli

# Authenticate (browser OAuth or paste token — see CLI guide)
multica login

# Start the agent daemon — registers local Claude Code / Codex runtimes and polls for assigned work
multica daemon start

# Scripted control plane (JSON output for automation)
multica issue list --output json
multica issue assign <id> --to "Agent Name"
multica daemon status --output json
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/multica.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **multica CLI** | Install via Homebrew tap `multica-ai/tap` or build from source — `multica issue`, `multica daemon`, `multica workspace`, `multica agent` ([CLI and Daemon Guide](https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md)) |
| **JSON output** | `--output json` on supported commands for machine parsing |
| **WebSocket** | Live updates between Next.js frontend and Go (`Chi` + Gorilla WebSocket) backend ([GitHub README architecture](https://github.com/multica-ai/multica/blob/main/README.md)) |
| **Self-hosted** | Docker Compose, PostgreSQL 17 + pgvector — see [SELF_HOSTING.md](https://github.com/multica-ai/multica/blob/main/SELF_HOSTING.md) |
| **Hosted SaaS** | https://multica.ai |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
