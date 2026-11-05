---
title: "Inferable | Agent-Native Services"
service_name: "Inferable"
description: "Build reliable AI Workflows and Agents with humans in the loop, structured outputs and durable execution"
permalink: /services/inferable/
page_kind: service
service_slug: "inferable"
category_slug: "durable-execution-and-scheduling"
category_label: "Durable Execution & Scheduling"
hero_image: "/assets/images/editorial-durable.webp"
image: "/assets/images/editorial-durable.webp"
classification: "agent-native"
dossier_path: "services/durable-execution-and-scheduling/inferable.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/inferable.md"
tagline: "Build reliable AI Workflows and Agents with humans in the loop, structured outputs and durable execution"
website: "https://github.com/inferablehq/inferable"
repository: "https://github.com/inferablehq/inferable"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Durable Execution &amp; Scheduling</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · CLI · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/inferablehq/inferable" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/inferablehq/inferable" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/inferable.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Inferable is a managed durable-execution runtime built specifically for AI workflows and agents. It provides three tightly integrated primitives that, taken together, distinguish it from generic workflow engines:

1. **Durable execution** — every step is checkpointed; agent crashes resume from the last successful step instead of re-running expensive LLM calls.
2. **First-class HITL** — `await human_approval(...)` suspends the workflow without blocking a process; humans approve via Slack or email; the workflow resumes when they reply.
3. **Structured outputs + versioned workflows** — outputs are schema-validated; workflows are versioned so deployments don't break in-flight runs.

It overlaps in spirit with Trigger.dev / Inngest / Restate (already in this catalog) but takes a more opinionated agent-shaped stance: HITL approval is built in (not a pattern), structured outputs are first-class, and the SDK assumes LLM/tool calls are the work.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, CLI, SDK, API
- **MCP:** ⚠️ Not yet published as a first-party MCP server. The SDK and REST API are the primary surfaces for now; community MCP wrappers exist.
- **Agent Skill:** ⚠️ Not yet published.
- **Onboarding type:** `cli`

## How agents onboard

```
# Self-hosted (Docker Compose) or hosted SaaS — pick one.
# SDK install:
npm install @inferable/sdk
# or
pip install inferable

# Then wrap a function as a durable workflow step:
from inferable import workflow

@workflow.step()
def call_tool(...): ...
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/inferable.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| TypeScript SDK | `@inferable/sdk` |
| Python SDK | `inferable` |
| REST API | Trigger / inspect / cancel runs |
| Slack / email channels | HITL approval surfaces |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/durable-execution-and-scheduling/' | relative_url }}"><small>Collection</small><strong>← Durable Execution &amp; Scheduling</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
