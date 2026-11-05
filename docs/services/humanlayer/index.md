---
title: "HumanLayer | Agent-Native Services"
service_name: "HumanLayer"
description: "Human in the Loop for AI Agents"
permalink: /services/humanlayer/
page_kind: service
service_slug: "humanlayer"
category_slug: "oversight-and-approval"
category_label: "Oversight & Approval"
hero_image: "/assets/images/editorial-oversight.webp"
image: "/assets/images/editorial-oversight.webp"
classification: "agent-native"
dossier_path: "services/oversight-and-approval/humanlayer.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/humanlayer.md"
tagline: "Human in the Loop for AI Agents"
website: "https://humanlayer.dev"
repository: "https://github.com/humanlayer/humanlayer"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Oversight &amp; Approval</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · webhook · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://humanlayer.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://humanlayer.dev/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/humanlayer/humanlayer" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/humanlayer.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

HumanLayer is an API and SDK that lets AI agents request human approval before executing high-risk functions. The agent annotates specific functions with `@require_approval()`; when called, HumanLayer pauses execution, routes an approval request to a human via Slack, email, SMS, or other channels, and resumes the agent with the human's decision injected into its context window.

The control flow is inverted from all traditional approval workflows: the **agent initiates**, the **human responds**, and the response feeds directly back into machine reasoning.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, webhook, SDK, API
- **MCP:** ⚠️ Not yet available as standalone MCP server
- **Agent Skill:** ⚠️ No official skill published by HumanLayer yet.
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `@humanlayer.require_approval()` decorator; async-compatible |
| TypeScript SDK | Equivalent TypeScript API |
| REST API | Programmatic approval lifecycle management |
| Webhooks | Receive human responses as webhook events |
| Slack | Approval requests as interactive Slack messages |
| Email | Approval requests via email with clickable approve/deny links |
| Discord | Approval channel integration |
| Teams / SMS / RCS | Advanced tier channels |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/oversight-and-approval/' | relative_url }}"><small>Collection</small><strong>← Oversight &amp; Approval</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
