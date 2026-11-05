---
title: "Laminar | Agent-Native Services"
service_name: "Laminar"
description: "Open-source observability platform for long-running agents. Trace in one line, debug from any step, detect patterns at scale"
permalink: /services/laminar/
page_kind: service
service_slug: "laminar"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/laminar.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/laminar.md"
tagline: "Open-source observability platform for long-running agents. Trace in one line, debug from any step, detect patterns at scale"
website: "https://laminar.sh"
repository: "https://github.com/lmnr-ai/lmnr"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache 2.0 (self-host) · Y Combinator-backed · $3M seed (March 2026)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://laminar.sh" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://laminar.sh/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/lmnr-ai/lmnr" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/laminar.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Laminar is an agent-native observability platform. Where conventional LLM observability tools (Langfuse, LangSmith) optimize for **prompt → completion** pairs, Laminar's data model is **agent-trace-first**: thousands of spans, non-deterministic control flow, nested causality, and session continuity are first-class.

Five capabilities define the product:

1. **One-line tracing** for popular AI frameworks and SDKs.
2. **True agent debugger** — local agent runs visible in the browser; rerun at step N with previous context preserved; tune system prompts and reflect changes instantly.
3. **Browser-agent session replay** — automatic capture and sync with traces (Browser Use, Stagehand, Playwright, Kernel, Browserbase).
4. **Signals** — describe an event in natural language; Laminar extracts it from past and future traces (e.g., "agent failure due to logic error"), with a defined output schema and email/Slack reports.
5. **SQL over traces** — query the entire trace corpus with SQL; feed Evals datasets straight from a query.

Self-host is fully Apache 2.0; the platform is written in Rust and aimed at terabyte-scale trace data.

---

## Agent-facing interfaces

- **Catalog protocols:** CLI, SDK, API
- **MCP:** ⚠️ Not yet published as a first-party MCP server. Laminar's data plane is OpenTelemetry-compatible; tracing is integrated via the SDK.
- **Agent Skill:** ⚠️ Not yet published as an official skill.
- **Onboarding type:** `cli`

## How agents onboard

```
# Self-host:
git clone https://github.com/lmnr-ai/lmnr
cd lmnr && docker compose up -d

# Or hosted: sign up at laminar.sh

# Two lines to integrate:
from lmnr import Laminar
Laminar.initialize()
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/laminar.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| OTLP | Native OpenTelemetry receiver |
| Python SDK | `pip install lmnr` |
| TypeScript SDK | `npm install @lmnr-ai/lmnr` |
| SQL API | Query traces directly |
| Evals SDK | `evaluate({ data, executor, evaluators, config })` |
| Self-host | Docker Compose / Helm |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
