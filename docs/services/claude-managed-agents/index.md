---
title: "Claude Managed Agents | Agent-Native Services"
service_name: "Claude Managed Agents"
description: "The Claude API is a RESTful API at https://api.anthropic.com that provides programmatic access to Claude models and Claude Managed Agents"
permalink: /services/claude-managed-agents/
page_kind: service
service_slug: "claude-managed-agents"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/claude-managed-agents.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/claude-managed-agents.md"
tagline: "The Claude API is a RESTful API at https://api.anthropic.com that provides programmatic access to Claude models and Claude Managed Agents"
website: "https://docs.anthropic.com/en/api/overview"
repository: "https://github.com/anthropics/anthropic-sdk-python"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://docs.anthropic.com/en/api/overview" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://platform.claude.com/docs/en/managed-agents/quickstart" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/anthropics/anthropic-sdk-python" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/claude-managed-agents.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

**Claude Managed Agents** is Anthropic’s hosted infrastructure for **versioned agent definitions**, **stateful sessions in managed cloud containers**, and **environment templates** that define how those sessions run. It sits alongside the Messages API: you define an agent configuration, create a session, and stream or poll execution — without operating the container fleet yourself. Related beta APIs cover **file uploads** for multi-step workflows and **custom skills** registration.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, SDK, http, API
- **MCP:** ⚠️ No standalone MCP server
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `sdk`

## How agents onboard

```bash
pip install anthropic
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/claude-managed-agents.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | `https://api.anthropic.com` — Messages + beta Managed Agents endpoints |
| Python SDK | `anthropic` package |
| TypeScript SDK | `@anthropic-ai/sdk` |
| Beta access | [Beta headers](https://platform.claude.com/docs/en/api/beta-headers) required for Agents, Sessions, Environments, Skills, Files |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
