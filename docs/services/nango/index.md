---
title: "Nango | Agent-Native Services"
service_name: "Nango"
description: "The OAuth and API credential layer for AI agents"
permalink: /services/nango/
page_kind: service
service_slug: "nango"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/nango.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/nango.md"
tagline: "The OAuth and API credential layer for AI agents"
website: "https://nango.dev"
repository: "https://github.com/NangoHQ/nango"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://nango.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.nango.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/NangoHQ/nango" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/nango.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Nango manages OAuth authentication and credential lifecycle for 700+ external APIs so AI agents can access third-party services without ever handling tokens directly. Agents call `getConnection()` at runtime to receive a valid access token; Nango handles token storage, automatic refresh, and credential validation invisibly.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skills published by NangoHQ on the AgentSkills marketplace
- **Onboarding type:** `other`

## Protocol surface

| Interface | Detail |
|---|---|
| Node.js SDK | `@nangohq/node` — `getConnection()`, `createConnectSession()` |
| REST API | Full connection management and credential retrieval |
| OpenAI Agents SDK | First-class integration guide and example |
| MCP-compatible | Patterns work with MCP-based agent frameworks |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
