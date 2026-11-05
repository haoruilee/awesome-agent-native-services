---
title: "Braintrust | Agent-Native Services"
service_name: "Braintrust"
description: "Ship quality AI at scale — AI observability and evaluation"
permalink: /services/braintrust/
page_kind: service
service_slug: "braintrust"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/braintrust.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/braintrust.md"
tagline: "Ship quality AI at scale — AI observability and evaluation"
website: "https://www.braintrust.dev"
repository: "https://github.com/braintrustdata/autoevals"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.braintrust.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.braintrust.dev/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/braintrustdata/autoevals" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/braintrust.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Braintrust is an **AI observability and evaluation** platform: **trace** every LLM call, tool invocation, and intermediate step in production; **score** outputs with code, LLM judges, or humans; **compare** prompts and models; and **convert traces to datasets** for regression testing. It explicitly targets **agents** — e.g. native **OpenAI Agents SDK** trace processors — and exposes an **MCP server** so coding agents can query experiments and logs directly.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, http, API
- **MCP:** ✅ Hosted MCP endpoint for coding agents and IDEs.
- **Agent Skill:** ⚠️ No single npx skills add bundle verified; MCP exposes logs, evals, and prompt workflows to compatible hosts.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
pip install "braintrust[openai-agents]"
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/braintrust.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install braintrust` / `braintrust[openai-agents]` |
| TypeScript SDK | `@braintrust/*` packages per docs |
| MCP | HTTPS `api.braintrust.dev/mcp` |
| REST API | https://www.braintrust.dev/docs/api-reference/introduction |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
