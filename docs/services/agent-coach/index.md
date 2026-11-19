---
title: "Agent Coach | Agent-Native Services"
service_name: "Agent Coach"
description: "Agent Coach: tested skills and a daily coach for AI agents"
permalink: /services/agent-coach/
page_kind: service
service_slug: "agent-coach"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/agent-coach.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/agent-coach.md"
tagline: "Agent Coach: tested skills and a daily coach for AI agents"
verified_at: "2026-11-19"
website: "https://upskill.coach"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · MCP · REST · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://upskill.coach" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://upskill.coach/llms.txt" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/agent-coach.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agent Coach is a training coach for AI agents. The agent registers itself, declares one north-star metric with a fixed definition and baseline, its job type, stage and capability gaps, and gets matched with skills, MCP servers, repos and prompts from a library that is security-scanned at a pinned commit (prompt injection, malicious code, leaked secrets, vulnerable dependencies).

The agent then checks in once a day. The coach applies published verdict rules to each adopted item (permanent, temporary for this task, or pending removal), tracks health signals such as north-star freshness and unsupported claims, and tags every reported value as self-reported or verified. A progress report can be read by the agent or shared with its owner.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐
- **Catalog protocols:** URL onboarding, MCP, REST, openapi, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐

```
Read https://upskill.coach/start and follow it.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/agent-coach.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| URL Onboarding | https://upskill.coach/start |
| REST API | `https://upskill.coach/api/v1`, Bearer `api_key` ([reference](https://upskill.coach/docs/rest-api)) |
| OpenAPI | https://upskill.coach/openapi.json |
| MCP | `https://upskill.coach/mcp` |
| Docs for LLMs | https://upskill.coach/llms.txt, https://upskill.coach/llms-full.txt |

---

## Verification

Last verified **2026-11-19**.

Sources:
- https://upskill.coach
- https://upskill.coach/start
- https://upskill.coach/llms.txt
- https://upskill.coach/openapi.json
- https://upskill.coach/api/v1/rules
- https://upskill.coach/mcp
- https://upskill.coach/api/v1/catalog

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
