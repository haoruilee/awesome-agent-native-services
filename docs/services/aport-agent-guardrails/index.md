---
title: "APort Agent Guardrails | Agent-Native Services"
service_name: "APort Agent Guardrails"
description: "Deterministic pre-action authorization for AI agents"
permalink: /services/aport-agent-guardrails/
page_kind: service
service_slug: "aport-agent-guardrails"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/aport-agent-guardrails.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/aport-agent-guardrails.md"
tagline: "Deterministic pre-action authorization for AI agents"
website: "https://aport.io"
repository: "https://github.com/aporthq/aport-agent-guardrails"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://aport.io" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://aport.io/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/aporthq/aport-agent-guardrails" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/aport-agent-guardrails.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

APort Agent Guardrails verifies AI agent actions before tool execution. It checks each proposed tool call or sensitive action against an Open Agent Passport policy and records allow/deny decisions, reducing reliance on prompt-only safety instructions.

---

## Agent-facing interfaces

- **Catalog protocols:** CLI, API
- **MCP:** ❌ Not a standalone MCP server
- **Agent Skill:** ⚠️ No standalone Agent Skill listed in this catalog yet.
- **Onboarding type:** `cli`

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `npx @aporthq/aport-agent-guardrails` |
| Node runtime | npm package and framework-specific setup |
| Python runtime | PyPI package and framework-specific callbacks/providers |
| API mode | Optional hosted policy evaluation through APort API |
| Local mode | Offline policy subset for local/bash guardrail paths |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
