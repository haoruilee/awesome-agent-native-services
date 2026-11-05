---
title: "Riza | Agent-Native Services"
service_name: "Riza"
description: "AI writes code. Riza runs it"
permalink: /services/riza/
page_kind: service
service_slug: "riza"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/riza.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/riza.md"
tagline: "AI writes code. Riza runs it"
website: "https://riza.io/"
repository: "https://github.com/riza-io"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://riza.io/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.riza.io/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/riza-io" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/riza.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Riza is a code-execution runtime built for AI systems that need to run untrusted, LLM-generated code safely and quickly. It provides an API-first execution layer with low startup latency, configurable network/env controls, and structured outputs (`stdout`, `stderr`, exit codes).

Riza also supports tool-style execution patterns where agents can create reusable tools and execute them on demand, making it a strong fit for autonomous agents that need repeatable programmable actions.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `other`

## How agents onboard

```bash
uv add rizaio
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/riza.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Primary execution and tooling interface |
| Python SDK | `rizaio` package for command/tool execution |
| TypeScript SDK | Official JS/TS API client |
| Go SDK | Official Go API client |
| MCP | Official `riza-mcp` integration |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
