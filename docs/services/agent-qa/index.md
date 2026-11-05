---
title: "Agent QA | Agent-Native Services"
service_name: "Agent QA"
description: "The self-improving QA agent for software teams"
permalink: /services/agent-qa/
page_kind: service
service_slug: "agent-qa"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/agent-qa.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/agent-qa.md"
tagline: "The self-improving QA agent for software teams"
verified_at: "2026-09-30"
website: "https://vostride.com/"
repository: "https://github.com/vostride/agent-qa"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">FSL-1.1-ALv2; converts to Apache-2.0 two years after each version is published</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://vostride.com/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://vostride.com/docs/agent-qa" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/vostride/agent-qa" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/agent-qa.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agent QA is a source-available QA-agent harness with a local live operator surface. Teams write web and mobile journeys in plain-English YAML. The bundled QA agent observes the live UI, plans the next action, executes it, and verifies the result, including re-observation and self-healing when a click, fill, or select fails. Each run can produce file-backed product, suite, and test memory, plus screenshots, logs, artifacts, and model-usage records. Operators and coding agents share the same CLI, dashboard, MCP, and Skill surfaces.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI workspace + MCP + published Agent Skills
- **Catalog protocols:** Agent Skill, MCP, CLI, STDIO, http
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** CLI workspace + MCP + published Agent Skills

```bash
npx agent-qa init
npx agent-qa dashboard --port 3470 --open
codex mcp add agent-qa -- agent-qa mcp
npx skills add vostride/agent-qa --skill agent-qa-authoring --skill agent-qa-debug-fix --skill agent-qa-result-triage
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/agent-qa.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `agent-qa init`, `run`, `dashboard`, `queue list`, `queue cancel`, `validate`, `doctor`, `mcp`, `skills` |
| Dashboard | Local operator UI and dashboard APIs for runs, tests, hooks, suites, memory, insights, and config |
| MCP stdio | `agent-qa mcp` for discovery, authoring, enqueue, inspect, cancel, and failure classification |
| MCP HTTP | Dashboard-backed loopback endpoint, default `http://127.0.0.1:3471/mcp` |
| Agent Skills | Packaged `agent-qa-authoring`, `agent-qa-debug-fix`, and `agent-qa-result-triage` |
| File-backed state | Tests, suites, hooks, config, memory observations, cache, and run artifacts in the workspace |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://vostride.com/
- https://vostride.com/docs/agent-qa

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
