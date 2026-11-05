---
title: "Letta | Agent-Native Services"
service_name: "Letta"
description: "The fastest way to bring stateful agents to production"
permalink: /services/letta/
page_kind: service
service_slug: "letta"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/letta.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/letta.md"
tagline: "The fastest way to bring stateful agents to production"
website: "https://letta.com"
repository: "https://github.com/letta-ai/letta"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://letta.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.letta.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/letta-ai/letta" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/letta.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Letta (evolved from the MemGPT research project at UC Berkeley) is a cloud platform for deploying and managing stateful agents at scale. Each agent deployed on Letta has persistent state, memory, conversation history, and reasoning traces stored in a model-agnostic format in the cloud — surviving restarts, model migrations, and provider changes.

The core abstraction: **the agent is the deployment unit**. Letta Cloud manages 24/7 uptime, auto-scaling, agent templates with versioning, and a visual debugging environment (Agent Development Environment, ADE).

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No official skill published by Letta yet.
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Full agent lifecycle: create, query, update, delete |
| Python SDK | `pip install letta-client` |
| TypeScript SDK | `npm install @letta-ai/letta-client` |
| MCP Server | Expose Letta agents as tools for other agents |
| ADE | Visual Agent Development Environment for debugging |
| Letta Cloud | Fully managed hosted deployment |
| Self-hosted | Open-source Docker deployment |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
