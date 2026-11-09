---
title: "Mobbin | Agent-Native Services"
service_name: "Mobbin"
description: "The Design MCP Server for AI Agents"
permalink: /services/mobbin/
page_kind: service
service_slug: "mobbin"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/mobbin.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mobbin.md"
tagline: "The Design MCP Server for AI Agents"
verified_at: "2026-11-08"
website: "https://mobbin.com/mcp"
repository: "https://github.com/mobbin/skills"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Hosted commercial product (Pro / Team / Enterprise); skills repo is public</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-08</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mobbin.com/mcp" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.mobbin.com/mcp/introduction" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/mobbin/skills" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mobbin.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Mobbin MCP turns Mobbin's catalog of real iOS/web UI screens, multi-step flows, and website sections into tools an agent can call mid-build. Agents search in natural language, inspect inline preview images, cite `mobbin_url` links, export crisp assets from `image_url`, and manage private collections with comments. Official skills teach search hygiene and redesign workflows so coding/design agents ground UI in shipped product patterns instead of inventing placeholder layouts.

Honesty: the classic Mobbin website is still a human design library. What qualifies here is the **first-party agent surface** (remote MCP, OAuth, agent-oriented tool schemas, skills, docs `llms.txt`, and search API) — not a claim that every Mobbin web feature was rebuilt for agents.

---

## Agent-facing interfaces

- **Interaction pattern:** Remote MCP (OAuth) + Agent Skills / marketplace plugins
- **Catalog protocols:** Agent Skill, MCP, REST, openapi, http, API
- **MCP:** ✅ Available — remote Streamable HTTP, OAuth
- **Agent Skill:** ✅ Published
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** Remote MCP (OAuth) + Agent Skills / marketplace plugins

```
https://api.mobbin.com/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/mobbin.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | `https://api.mobbin.com/mcp` (Streamable HTTP + OAuth) |
| Docs / llms.txt | https://docs.mobbin.com/llms.txt |
| REST search | Documented under https://docs.mobbin.com/api/quickstart · OpenAPI https://docs.mobbin.com/openapi.json |
| Skills / plugins | `npx skills add mobbin/skills` · https://github.com/mobbin/skills |
| Product page | https://mobbin.com/mcp |

---

## Verification

Last verified **2026-11-08**.

Sources:
- https://mobbin.com/mcp
- https://docs.mobbin.com/llms.txt
- https://api.mobbin.com/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
