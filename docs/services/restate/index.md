---
title: "Restate | Agent-Native Services"
service_name: "Restate"
description: "Durable execution for AI agents — any framework, any cloud"
permalink: /services/restate/
page_kind: service
service_slug: "restate"
category_slug: "durable-execution-and-scheduling"
category_label: "Durable Execution & Scheduling"
hero_image: "/assets/images/editorial-durable.webp"
image: "/assets/images/editorial-durable.webp"
classification: "agent-native"
dossier_path: "services/durable-execution-and-scheduling/restate.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/restate.md"
tagline: "Durable execution for AI agents — any framework, any cloud"
website: "https://restate.dev"
repository: "https://github.com/restatedev/restate"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Durable Execution &amp; Scheduling</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">BSL 1.1 (open-source) + Restate Cloud</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://restate.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.restate.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/restatedev/restate" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/restate.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Restate is a durable execution runtime that persists every step of an agent's execution — LLM calls, tool invocations, routing decisions — in a journal. If an agent crashes mid-execution, Restate resumes it from exactly where it left off without re-running completed steps or duplicating side effects.

Unlike Trigger.dev or Inngest (which require using their specific task abstraction), Restate works as lightweight middleware on top of existing agent frameworks (Vercel AI SDK, OpenAI Agents SDK, LangGraph, CrewAI) — developers add durable execution with a few lines of code, without rewriting their agents.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, API
- **MCP:** ✅ MCP examples available
- **Agent Skill:** ⚠️ No official skill published by Restate yet.
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install restate-sdk` |
| TypeScript SDK | `npm install @restatedev/restate-sdk` |
| REST API | Agent management and execution control |
| Vercel AI SDK | Native integration guide |
| OpenAI Agents SDK | Native integration guide |
| Restate Cloud | Managed hosted deployment |
| Self-hosted | Open-source Docker deployment |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/durable-execution-and-scheduling/' | relative_url }}"><small>Collection</small><strong>← Durable Execution &amp; Scheduling</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
