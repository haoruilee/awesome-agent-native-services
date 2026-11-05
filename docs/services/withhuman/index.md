---
title: "withHuman | Agent-Native Services"
service_name: "withHuman"
description: "The approval layer for AI agents"
permalink: /services/withhuman/
page_kind: service
service_slug: "withhuman"
category_slug: "oversight-and-approval"
category_label: "Oversight & Approval"
hero_image: "/assets/images/editorial-oversight.webp"
image: "/assets/images/editorial-oversight.webp"
classification: "agent-native"
dossier_path: "services/oversight-and-approval/withhuman.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/withhuman.md"
tagline: "The approval layer for AI agents"
website: "https://withhuman.ai"
repository: "https://github.com/withHumanAI/withHuman"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Oversight &amp; Approval</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Elastic-2.0 (core); Apache-2.0 (Agent Approval Protocol spec and libraries)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · SDK · openapi</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://withhuman.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://withhuman.ai/blog/introducing-withhuman" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/withHumanAI/withHuman" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/withhuman.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

withHuman sits **between agents and their tools** and intercepts every tool call before it runs. **Approval pipelines** approve, deny, ask a model or service, or decide the call needs a person, based on the tool and its arguments. **Escalation paths** route the rest to the right team or person by team, level and working hours, notifying via email, Slack or Discord. Reviewers see the exact arguments and the agent's explanation in a shared review queue and approve or deny with a note the agent reads. Agents speak the open **Agent Approval Protocol (AAP)**, so integrations are portable between providers.

---

## Agent-facing interfaces

- **Interaction pattern:** Hooks (Claude Code, Codex) + SDKs (Python/TypeScript) + AAP HTTP protocol
- **Catalog protocols:** CLI, SDK, openapi
- **MCP:** ⚠️ Gates MCP tool calls (starting point per the launch post) rather than exposing its own MCP server.
- **Agent Skill:** ❌ No Agent Skill; integration is through hooks and SDKs.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** Hooks (Claude Code, Codex) + SDKs (Python/TypeScript) + AAP HTTP protocol

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/withhuman.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **AAP** | Open spec + OpenAPI contract (Apache-2.0) |
| **Hooks** | Claude Code, Codex and other coding agents |
| **SDKs** | Python and TypeScript; framework integrations (LangGraph, Pydantic AI, OpenAI Agents SDK, CrewAI, Mastra) |
| **Notifications** | Email, Slack, Discord |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/oversight-and-approval/' | relative_url }}"><small>Collection</small><strong>← Oversight &amp; Approval</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
