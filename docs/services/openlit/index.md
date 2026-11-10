---
title: "OpenLIT | Agent-Native Services"
service_name: "OpenLIT"
description: "OpenTelemetry-native observability for LLMs and AI agents"
permalink: /services/openlit/
page_kind: service
service_slug: "openlit"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/openlit.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/openlit.md"
tagline: "OpenTelemetry-native observability for LLMs and AI agents"
website: "https://openlit.io"
repository: "https://github.com/openlit/openlit"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://openlit.io" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.openlit.io" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/openlit/openlit" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/openlit.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

Instrumentation has to go into the agent runtime itself. The dossier lists a Python or JS SDK, OpenTelemetry exporters, and backend APIs, with no MCP server and no Agent Skill. An agent does not call this service. Its code is instrumented, and telemetry flows out while the loop runs.

### Spans for tool calls and tokens

The tagline is "OpenTelemetry-native observability for LLMs and AI agents." According to the dossier, the SDK captures agent traces, tool-call spans, latency, token usage, and cost. The primitives are agent run traces, tool-call spans, and token and cost analytics. The How to Use path has three steps: add the SDK, emit traces and metrics, and connect to the OpenLIT backend for dashboards and analysis.

Attribution relies on per-agent and per-run metadata fields. The human side is review and alerting: teams can read traces and set escalation workflows for anomalous behavior. Nothing in the entry describes evaluation, datasets, or prompt management, so treat it as a telemetry product unless the [OpenLIT docs](https://docs.openlit.io) show more.

### OpenTelemetry as the selling point

Several listings in [Observability & Tracing](/categories/observability-and-tracing/) collect similar data. [Langfuse](/services/langfuse/) and [LangWatch](/services/langwatch/) pair tracing with evaluation, and LangWatch's dossier adds regression monitoring. [Braintrust](/services/braintrust/) presents observability and evaluation together. OpenLIT's dossier stays on instrumentation and cost analytics, and its framing is the standard it emits.

That framing has a practical consequence. If spans follow OpenTelemetry, the same data can go to a backend you already run, and tools that read OTel traces, such as [AgentEvals](/services/agentevals/), can score from it. The dossier describes the instrumentation as OpenTelemetry-style in one place and lists OpenTelemetry exporters in another, so check which semantic conventions are used before assuming another backend will render the spans the way OpenLIT's own does.

The [agent-native guide](/guides/what-makes-a-service-agent-native/) explains why the catalog accepts observability tools at all: the primitives are shaped around agent runs and tool calls rather than generic web requests.

### Before you export

Decide where the backend runs and who can read stored prompts and tool arguments. Find out how cost figures are computed, since they depend on model price tables someone has to keep current. Check which agent frameworks the instrumentation covers out of the box. The dossier does not address sampling, retention, or how the backend authenticates exporters.

### Editor's take

A team already running an OpenTelemetry collector is the natural adopter: add the SDK and route spans wherever they already go, with OpenLIT's backend as one destination among several. Teams that want evaluations and regression tracking in the same product should compare LangWatch, Langfuse, or Braintrust first. We have only read the dossier and OpenLIT's documentation, and have not instrumented an agent with it.

</section>

## What it does

Captures agent traces, tool-call spans, latency, token usage, and cost telemetry via OpenTelemetry-style instrumentation.

## Agent-facing interfaces

- **Catalog protocols:** SDK
- **MCP:** ⚠️ No standalone official MCP server package.
- **Agent Skill:** ⚠️ No official AgentSkills package found.
- **Onboarding type:** `other`

## Protocol surface

Python/JS SDK, OpenTelemetry exporters, backend APIs.

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
