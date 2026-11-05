---
title: "Cognee | Agent-Native Services"
service_name: "Cognee"
description: "Memory control plane for AI Agents in 6 lines of code"
permalink: /services/cognee/
page_kind: service
service_slug: "cognee"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/cognee.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/cognee.md"
tagline: "Memory control plane for AI Agents in 6 lines of code"
website: "https://www.cognee.ai"
repository: "https://github.com/topoteretes/cognee"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.cognee.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.cognee.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/topoteretes/cognee" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/cognee.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Cognee is a **memory control plane** that ingests an agent's data sources (warehouses, vector stores, files, APIs), automatically extracts ontologies, builds and maintains a **managed world model** (graph + vectors), and serves recall back to agents. The pitch is "model your agent's world" — instead of stuffing raw chunks into a context window, the agent reasons over a structured representation of what it knows.

Three operational stages:

1. **Ingest** — connect Snowflake, Postgres, Slack, PDFs, MD files, REST APIs.
2. **Reason** — Cognee builds the ontology + managed graph + recall tuning that compounds with use.
3. **Act** — agent calls `cognee.search(...)` from Claude Code, LangGraph, OpenClaw, MCP-compatible runtimes, etc.

The library is open-source; Cognee Cloud is the optional managed tier (free locally; pay only when scaling).

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK
- **MCP:** ✅ Available — first-party MCP server.
- **Agent Skill:** ⚠️ No SKILL.md published by Cognee directly, but Cognee is listed as a runtime target by other catalog entries' skills.
- **Onboarding type:** `sdk`

## How agents onboard

```
pip install cognee
# then:
import cognee
await cognee.add(documents)
await cognee.cognify()        # build the world model
results = await cognee.search("...")
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/cognee.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install cognee` |
| 28+ connectors | Snowflake, Postgres, files, REST, Slack, … |
| MCP server | First-party |
| Framework adapters | Claude Code, Codex, Cursor, LangGraph, CrewAI, Continue, Hermes, OpenClaw |
| Cloud + On-Prem tiers | Free local; paid hosted; enterprise on-prem |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
