---
title: "OpenViking | Agent-Native Services"
service_name: "OpenViking"
description: "The context database for AI agents"
permalink: /services/openviking/
page_kind: service
service_slug: "openviking"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/openviking.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/openviking.md"
tagline: "The context database for AI agents"
website: "https://openviking.ai"
repository: "https://github.com/volcengine/OpenViking"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">AGPL-3.0 for the main project; crates/ov_cli and examples are Apache-2.0 (the Hermes plugin is MIT)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://openviking.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://openviking.ai/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/volcengine/OpenViking" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/openviking.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

OpenViking is an open-source **context database** — a unified filesystem for everything an AI agent needs to know: its own accumulated experience (`viking://agent/`), user preferences (`viking://user/`), and external resources (`viking://resources/`).

Instead of managing memory in one system, resources in a vector store, and skills in another, OpenViking maps all three to a hierarchical `viking://` virtual filesystem. Agents navigate it with `ls` and `find` — exactly like a developer navigates a project directory. Each node has L0/L1/L2 tiered content: a one-sentence abstract for quick routing, an overview for planning, and full content for deep reasoning — loaded on demand to reduce token cost by up to 91%.

The killer feature: **self-evolution**. At the end of each session, OpenViking asynchronously extracts agent experience from task execution and writes it to `viking://agent/memories/` — the agent accumulates operational knowledge without any human curation.

**Benchmark (LoCoMo10, 1540 long-range dialogue cases):**

| System | Task Completion | Input Tokens |
|---|---|---|
| OpenClaw (baseline) | 35.65% | 24.6M |
| OpenClaw + LanceDB | 44.55% | 51.6M |
| **OpenClaw + OpenViking** | **52.08%** | **4.3M** |

+49% task completion, -83% token cost versus baseline.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / REST + MCP
- **Catalog protocols:** Agent Skill, MCP, REST, CLI, SDK, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skills published by the OpenClaw community
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK / REST + MCP

```bash
# Install
pip install openviking --upgrade

# Configure (create ~/.openviking/ov.conf with your VLM + embedding keys)
# Then start the server
openviking-server

# Agent connects via MCP (recommended for Claude Code / Cursor)
claude mcp add --transport http openviking http://localhost:8000/mcp

# Or ingest content and query via CLI
ov add ./my-project-docs
ov query "how does the authentication flow work"
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/openviking.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP Server | HTTP StreamableHttp at `localhost:8000/mcp`; tools: `query`, `search`, `add_resource` |
| Python SDK | `pip install openviking` |
| Rust CLI | `curl ... | bash` (ov_cli); commands: `ov add`, `ov query`, `ov find`, `ov grep`, `ov ls` |
| HTTP REST | Direct API at `localhost:8000` |
| OpenClaw Plugin | Memory plugin for OpenClaw agents |
| OpenCode Plugin | Memory plugin for OpenCode agents |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
