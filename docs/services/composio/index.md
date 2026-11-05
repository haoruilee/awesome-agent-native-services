---
title: "Composio | Agent-Native Services"
service_name: "Composio"
description: "The tool platform built for agents"
permalink: /services/composio/
page_kind: service
service_slug: "composio"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/composio.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/composio.md"
tagline: "The tool platform built for agents"
website: "https://composio.dev"
repository: "https://github.com/ComposioHQ/composio"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · SDK</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://composio.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.composio.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/ComposioHQ/composio" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/composio.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Composio gives AI agents the ability to **discover, authenticate, and call external tools at runtime**. Rather than a developer pre-configuring a fixed set of integrations at build time, agents receive meta-tools at runtime that let them find the right integration, authenticate on behalf of the user, and execute the call — all within the agent loop, without any human clicking an OAuth button.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, SDK
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skills published at composiohq/skills
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `composio_openai`, `composio_anthropic`, `composio_langchain`, etc. |
| TypeScript SDK | `@composio/core`, framework-specific packages |
| MCP Compatible | Works with Claude Desktop, Cursor, OpenAI Agents without framework packages |
| Framework Integrations | LangChain, CrewAI, LangGraph, LlamaIndex, Vercel AI SDK, AutoGen, and more |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
