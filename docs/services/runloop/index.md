---
title: "Runloop | Agent-Native Services"
service_name: "Runloop"
description: "Your AI Agent Accelerator"
permalink: /services/runloop/
page_kind: service
service_slug: "runloop"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/runloop.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/runloop.md"
tagline: "Your AI Agent Accelerator"
website: "https://runloop.ai"
repository: "https://github.com/runloopai/api-client-python"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · CLI · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://runloop.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.runloop.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/runloopai/api-client-python" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/runloop.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Runloop provides **Devboxes**: secure, isolated sandboxes for running **AI-generated code** and long-running agent workflows, with fast startup, optional suspend/resume, **disk snapshots and branching** for agent state, repo-aware environments, secrets/objects stores, and **benchmark jobs** to evaluate coding agents (e.g., SWE-Bench-style runs). The surface area is explicitly marketed for **AI agents** and **AI software engineering** workloads—not generic batch VMs only.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / REST + CLI + MCP
- **Catalog protocols:** MCP, REST, CLI, SDK, http, API
- **MCP:** ✅ Available (via official CLI)
- **Agent Skill:** ⚠️ No official npx skills add … pack from Runloop yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK / REST + CLI + MCP

```bash
pip install runloop-api-client
# or: npm install @runloop/api-client  (see GitHub api-client-ts)
export RUNLOOP_API_KEY=...
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/runloop.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install runloop-api-client` — [api-client-python](https://github.com/runloopai/api-client-python) |
| TypeScript SDK | `@runloop/api-client` — [api-client-ts](https://github.com/runloopai/api-client-ts) |
| REST API | Platform API per [docs.runloop.ai](https://docs.runloop.ai) |
| CLI | `npm install -g @runloop/rl-cli` → `rli` |
| MCP | `rli mcp start` / `rli mcp install` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
