---
title: "Toolhouse | Agent-Native Services"
service_name: "Toolhouse"
description: "Repetitive tasks, done for you, by AI workers"
permalink: /services/toolhouse/
page_kind: service
service_slug: "toolhouse"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/toolhouse.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhouse.md"
tagline: "Repetitive tasks, done for you, by AI workers"
website: "https://toolhouse.ai"
repository: "https://github.com/toolhouseai/toolhouse-sdk-python"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · CLI · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://toolhouse.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.toolhouse.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/toolhouseai/toolhouse-sdk-python" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhouse.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Toolhouse is a Backend-as-a-Service platform where agents are the deployment unit. Developers define agents as code, publish them with `th deploy`, and Toolhouse exposes each agent as a streaming API endpoint. Each deployed agent automatically connects to Toolhouse's MCP server, gaining access to RAG, memory, code execution, browser use, and custom tools — without managing any infrastructure.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, CLI, http, API
- **MCP:** ✅ Built-in
- **Agent Skill:** ⚠️ No official skill published by Toolhouse yet.
- **Onboarding type:** `cli`

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `th deploy` (publish), `th run` (test locally) |
| MCP Server | Automatic connection to Toolhouse tool registry |
| Streaming REST API | `POST https://agents.toolhouse.ai/{agent_id}` with streaming response |
| Cron Expressions | `@hourly`, `0 9 * * MON`, etc. for scheduled execution |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
