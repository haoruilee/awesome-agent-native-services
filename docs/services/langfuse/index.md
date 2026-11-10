---
title: "Langfuse | Agent-Native Services"
service_name: "Langfuse"
description: "Open-source LLM observability, tracing, and evaluation for AI agents"
permalink: /services/langfuse/
page_kind: service
service_slug: "langfuse"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/langfuse.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/langfuse.md"
tagline: "Open-source LLM observability, tracing, and evaluation for AI agents"
website: "https://langfuse.com"
repository: "https://github.com/langfuse/langfuse"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Open-source (MIT / enterprise)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://langfuse.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://langfuse.com/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/langfuse/langfuse" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/langfuse.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

When an agent run is a tree of model calls and tool calls, a flat request log is the wrong picture. Langfuse is the open-source tracing and evaluation system filed for that tree. The tagline is "Open-source LLM observability, tracing, and evaluation for AI agents." The dossier describes a typed hierarchy from session and run down to spans, model calls, and tool calls, plus which memories or documents were injected. Production traces can be turned into evaluation datasets. OpenTelemetry is an integration path, alongside Python and TypeScript SDKs. The Python surface named is `langfuse.trace()` and an `@observe()` decorator. Native integrations listed include the OpenAI Agents SDK, the Claude SDK, and LangChain. Docs are [langfuse.com/docs](https://langfuse.com/docs). The repo is [langfuse/langfuse](https://github.com/langfuse/langfuse). The catalog marks both an Agent Skill and MCP as available. Observation is passive: the agent is not supposed to stop and ask to be logged.

Cost and token attribution per run, per tool, and per model call are primitives in the entry. No formula and no currency are stated, so the docs are where a number would have to be checked, and this page will not invent one. Trajectory replay is the ability to inspect a path after the fact. It is not a claim that you can resume the agent from that path. Skill evaluation is listed as its own primitive beside dataset evaluation. Confirm in the docs whether that means evaluation of Agent Skills files or evaluation of capabilities you define. The words are close and the features may not be.

[Observability & Tracing](/categories/observability-and-tracing/) has three open-source neighbors people shortlist together. [OpenLIT](/services/openlit/) leads with OpenTelemetry-native SDKs and exporters. Langfuse also speaks OTel and adds the dataset and replay vocabulary. [LangWatch](/services/langwatch/) centers eval datasets and regression monitoring, with MCP not primary. [agent-inspect](/services/agent-inspect/) keeps execution trees local for TypeScript and does not ask you to run a collector. [Braintrust](/services/braintrust/) is the hosted evaluation listing. If you will self-host the trace store, Langfuse's repository is the artifact. If you refuse to add a second SDK and your stack is already pure OTel, read OpenLIT before assuming the decorator is required. The criterion essay is [What makes a service agent-native](/guides/what-makes-a-service-agent-native/).

### What gets stored when you decorate a function

`@observe()` will capture whatever the docs say it captures, which may include prompts and tool payloads. That is the point of a trace and the reason to read the retention and self-hosting notes before you turn it on against customer data. Per-agent metadata is only as good as the fields you set. The dossier says multi-agent attribution is possible. It does not show the attribute names. MCP and the Agent Skill are catalog flags. Open the docs for how the MCP server is installed rather than assuming the Python decorator and the MCP server are the same integration.

### Editor's take

Langfuse fits a team that wants hierarchical traces of tool-using agents and a path from those traces to an eval set, with the option to self-host. It is more product than you need if a local TypeScript tree is enough, and it overlaps OpenLIT if OpenTelemetry export is the only requirement. This project has not shipped a trace. The judgement follows the primitive table and the docs URL, and it treats latency and cost fields as labels until the docs define them.

</section>

## What it does

Langfuse provides structured tracing for multi-step agent workflows. It captures the full execution trajectory of an agent — LLM calls, tool invocations, retriever steps, guardrail checks — organized in a typed, hierarchical trace structure. Production traces can be converted to evaluation datasets with one click, and OpenTelemetry integration allows existing monitoring infrastructure to receive agent telemetry.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skill published at langfuse/skills — listed on skills.sh/langfuse/skills
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `langfuse.trace()`, `@observe()` decorator, context manager |
| TypeScript SDK | Equivalent TypeScript API |
| OpenTelemetry | OTEL-compatible; works with any OTEL-instrumented agent framework |
| OpenAI Agents SDK | Native auto-instrumentation |
| Claude SDK | Native auto-instrumentation |
| LangChain | Native callback integration |
| LangGraph | Native integration |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
