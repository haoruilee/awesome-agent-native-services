---
title: "Inngest | Agent-Native Services"
service_name: "Inngest"
description: "Durable execution for AI agents in production"
permalink: /services/inngest/
page_kind: service
service_slug: "inngest"
category_slug: "durable-execution-and-scheduling"
category_label: "Durable Execution & Scheduling"
hero_image: "/assets/images/editorial-durable.webp"
image: "/assets/images/editorial-durable.webp"
classification: "agent-native"
dossier_path: "services/durable-execution-and-scheduling/inngest.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/inngest.md"
tagline: "Durable execution for AI agents in production"
website: "https://inngest.com"
repository: "https://github.com/inngest/inngest"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Durable Execution &amp; Scheduling</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · webhook · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://inngest.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.inngest.com/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/inngest/inngest" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/inngest.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

An agent that calls three tools and then crashes on the third should not redo the first two, and it should not lose the reason it called them. Inngest is filed as durable execution for that failure. The tagline is "Durable execution for AI agents in production." The TypeScript surface in the dossier is `inngest.createFunction()`, `step.run()`, `step.sleep()`, and `step.waitForEvent()`. Each `step.run()` is a checkpoint. A retry is supposed to resume the failed step and restore earlier context rather than restart the chain. `step.waitForEvent()` is the human-approval pause. Triggers are events, webhooks, or cron. There is a Python SDK and a REST API for sending events. Docs are [www.inngest.com/docs](https://www.inngest.com/docs). The repo is [inngest/inngest](https://github.com/inngest/inngest). The catalog marks an Agent Skill and MCP as available, on top of the SDK.

The agent resumes from the last checkpoint without a person re-clicking the run. That is the autonomy claim. The human step is explicit and only where you waited for an event. Per-run event IDs are the audit handle. The dossier also describes a low-latency pattern for interactive agents as distinct from batch jobs. It does not include a measurement. Do not plan a user-facing loop on an adjective. A 2025 positioning line is quoted in the entry. It is the vendor's argument that durable execution is how you run agents in production, not a benchmark.

[Durable Execution & Scheduling](/categories/durable-execution-and-scheduling/) is a small collection with a sharp overlap. [Trigger.dev](/services/trigger-dev/) is the other TypeScript runtime, with long-lived tasks, pause and resume, and its own skill, and without MCP in the catalog. [Restate](/services/restate/) is durable execution aimed at any framework and any cloud, which is the self-hosted-shaped neighbor. [Inferable](/services/inferable/) pairs workflows with humans in the loop. Inngest's specific bet in this dossier is the step checkpoint between tool calls plus `waitForEvent` as the approval primitive. If your functions are already TypeScript and you want that step API, start here. If you need the workflow engine embedded in an existing Kubernetes service without a hosted event router, read Restate before assuming the SDK is the only shape. There is no durable-execution guide yet. [What makes a service agent-native](/guides/what-makes-a-service-agent-native/) uses a checkpoint between model calls as one of its examples of an agent primitive, which is the idea this entry is implementing.

### Steps are only durable if you actually step

A model call made outside `step.run()` is not checkpointed, no matter what the product is called. Confirm in the docs how much state is restored, what a step may return, and how MCP is attached, because the catalog flag does not show a config snippet. Approval via `waitForEvent` holds the run until some other system emits the event. The dossier does not say what emits it. Sleep and wait are different. Read which one you are calling. Pricing and retention of event history are on the vendor site, not in this summary.

### Editor's take

Inngest fits TypeScript or Python agents that already think in steps and need a crash to resume at the failed tool call, with an explicit wait when a person must approve. It is the wrong layer for a single request that should stay inside one process. This project has not resumed a failed run. The opinion is from the SDK names in the dossier and the docs URL, and the "low-latency" pattern stays unqualified until those docs put a number on it.

</section>

## What it does

Inngest provides a durable execution platform specifically addressing the production challenges of AI agents. It checkpoints state between tool calls, handles external API failures through intelligent retries that preserve agent context, and maps human-in-the-loop approval patterns to native suspend/resume primitives. In 2025, durable execution became a mainstream requirement as AWS, Cloudflare, and Vercel all launched competing offerings — Inngest was ahead of this trend.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, webhook, SDK, API
- **MCP:** ✅ Available (via dev server)
- **Agent Skill:** ✅ Official skills published at inngest/inngest-skills — launched February 2026
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| TypeScript SDK | `inngest.createFunction()`, `step.run()`, `step.sleep()`, `step.waitForEvent()` |
| Python SDK | Equivalent Python API |
| REST API | Event triggering, function management |
| Webhooks | External event triggers |
| Cron | Native cron schedule support |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/durable-execution-and-scheduling/' | relative_url }}"><small>Collection</small><strong>← Durable Execution &amp; Scheduling</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
