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

<section class="service-essay" aria-label="Editorial" markdown="1">

Durable execution here needs a server that someone runs: Restate Cloud, or the self-hosted Docker deployment a team keeps next to its own services. The agent code stays in your process and reports each step to that server, which writes it to a journal. Whoever operates the journal holds the agent's record of what already happened, and that record is what lets a crashed run resume instead of repeating a payment or an email.

### A journal under an existing agent

The vendor's wording is "Durable execution for AI agents — any framework, any cloud." The dossier explains the mechanism. Every LLM call, tool invocation, and routing decision is persisted. After a crash, the run continues from the last completed entry without re-executing finished steps. Rate-limit errors are retried after backoff without duplicating work.

The other primitives follow from the journal. An agent waiting for a human or an event suspends instead of holding a thread. A human approval gate can carry a timeout, and when it expires a compensation step undoes earlier side effects. Agent-to-agent calls are described as exactly-once. Operators can pause, resume, or restart a running agent from the Restate UI or the REST API.

Integration is through SDKs: `pip install restate-sdk` for Python and `npm install @restatedev/restate-sdk` for TypeScript, plus integration guides for the Vercel AI SDK and the OpenAI Agents SDK. The dossier also names LangGraph and CrewAI as frameworks it can wrap. MCP appears as example code for durable MCP servers in the restatedev ai-examples repository, not as a hosted server. No official Agent Skill exists. Start from the [Restate docs](https://docs.restate.dev).

### Middleware or a task framework

The dossier draws the line itself. [Trigger.dev](/services/trigger-dev/) and [Inngest](/services/inngest/), both in [Durable Execution & Scheduling](/categories/durable-execution-and-scheduling/), ask you to write work in their task abstraction. Restate positions itself as middleware over an agent you already have. That matters if a team has a working LangGraph or Vercel AI SDK agent and does not want to restructure it. [Inferable](/services/inferable/) leans harder on human-in-the-loop workflows and structured outputs. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why a journal tuned to LLM steps counts as an agent primitive.

### Points to verify

The dossier lists the core under a Business Source License, so read the license terms before embedding it in a product you sell. Access control is described as delegated from the host application; Restate itself does not add a user-facing approval system. Ask the docs how the REST API and UI are secured, especially on a self-hosted install where your team owns that boundary.

Exactly-once and no-duplicate claims depend on what counts as a recorded step. Read how side effects outside the journal behave on retry, and how a code change to an agent interacts with runs still waiting in a suspended state.

### Editor's take

A team with a working agent in a supported framework, and a growing list of crash and retry bugs, has the clearest reason to try it. If you are starting fresh and would rather adopt a full task model with a managed runner, Trigger.dev or Inngest ask for more structure up front and organize everything around their own task model. We have read the dossier and Restate's docs and examples, and have not wrapped an agent with it ourselves.

</section>

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
