---
title: "Kitaru | Agent-Native Services"
service_name: "Kitaru"
description: "Traces you can run, not just read. — zenml-io/kitaru README"
permalink: /services/kitaru/
page_kind: service
service_slug: "kitaru"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/kitaru.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/kitaru.md"
tagline: "Traces you can run, not just read. — zenml-io/kitaru README"
verified_at: "2026-10-19"
website: "https://www.zenml.io/product/kitaru"
repository: "https://github.com/zenml-io/kitaru"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache 2.0 (open-source)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · SDK · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.zenml.io/product/kitaru" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.zenml.io/kitaru" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/zenml-io/kitaru" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/kitaru.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Kitaru records or imports production agent runs as **sessions**, then **replays** them against the agent's real code so a team can test a model, prompt, or code change against traffic that already happened. Tool calls are answered from the recording, so replay does not touch live systems.

The live README: *"Kitaru (来る, 'to arrive') gives you replay-based evals for AI agents."* The product page: *"Your agent's best eval data is already in production"* — turn traces into replayable evals.

The loop in docs: record or import → replay → improve (investigations, evaluators, cohorts, experiments). Kitaru sits **beside** an observability stack (Langfuse, LangSmith, Braintrust, Logfire, Arize Phoenix remain the system of record); it re-runs traces rather than replacing dashboards.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, CLI, SDK, http
- **MCP:** ✅ Available (kitaru[mcp] extra)
- **Agent Skill:** ✅ Official
- **Onboarding type:** `agent-skill`

## How agents onboard

```bash
uv add "kitaru[cli,worker,mcp]" kitaru-pydantic-ai    # or: pip install
kitaru login --local                                  # or: kitaru login <your-team-url>
npx skills add zenml-io/kitaru-skills
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/kitaru.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python / TypeScript SDK | Same server; adapters for PydanticAI, LangGraph, OpenAI Agents SDK, Mastra, Vercel AI SDK |
| CLI | `kitaru login`, `kitaru session import`, experiment/replay commands; JSON when a shell is the right tool |
| MCP | `kitaru-mcp` — bounded operations for coding assistants |
| Agent Skills | `npx skills add zenml-io/kitaru-skills` |
| Docs | https://docs.zenml.io/kitaru |

---

## Verification

Last verified **2026-10-19**.

Sources:
- https://github.com/zenml-io/kitaru

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
