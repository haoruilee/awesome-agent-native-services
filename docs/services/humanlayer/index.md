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

<section class="service-essay" aria-label="Editorial" markdown="1">

[withHuman](/services/withhuman/) calls itself the approval layer for AI agents, and HumanLayer works on the same ground. What the HumanLayer dossier adds is a specific mechanism: a decorator on the risky function, an asynchronous pause, and the human's answer written back into the agent's context window.

### Pausing at a decorated function

The developer marks a high-risk function with `@require_approval()`. When the agent calls it, HumanLayer holds execution and routes an approval request to a person over Slack, email, Discord, or, on some tiers, Teams, SMS, or RCS. The person approves, denies, or modifies. The agent then resumes, either executing the action or reasoning about the refusal.

Denial feedback is the detail worth noticing. When a human says no, their explanation goes into the agent's context, so the next attempt can respond to the actual objection instead of retrying blindly. The dossier says the pause is asynchronous, so one agent can have several approval requests outstanding at once.

Agent webhooks reverse the direction: an incoming human message can launch an agent. Run IDs identify the whole task and Call IDs identify the specific function call, and both appear in requests, responses, and audit logs.

### SDKs first

The quickest documented path is `pip install humanlayer` and decorating functions with `@hl.require_approval()`. A TypeScript SDK offers the equivalent, a REST API manages the approval lifecycle, and webhooks deliver human responses. The [HumanLayer docs](https://humanlayer.dev/docs) cover framework support, which the dossier lists as LangChain, CrewAI, OpenAI, Claude, ControlFlow, Vercel AI SDK, and Mastra.

No standalone MCP server is published, and no official Agent Skill. The dossier says the SDKs work inside MCP-orchestrated agent loops, which means the gate lives in your code around a function, not in the MCP client.

### Open questions for adopters

Within [Oversight & Approval](/categories/oversight-and-approval/), neighbors split between human gates and automated policy. [Sondera Coding Agent Hooks](/services/sondera-coding-agent-hooks/) is a reference monitor for coding agents, and [Cordum](/services/cordum/) is an open agent control plane. [Tracekit](/services/tracekit/) is about proving every action an agent takes. HumanLayer's gate depends on a person answering. The [agent-native guide](/guides/what-makes-a-service-agent-native/) explains why an agent-initiated approval request counts as an agent-specific primitive.

The dossier leaves several things unspecified. It does not say what happens when nobody responds: whether a request times out, escalates, or waits indefinitely. It does not say how the approver is authenticated, which matters for email links that anyone holding the message could click. The function's arguments travel to HumanLayer and then into Slack or email, so consider what data appears in an approval message. Which channels your plan includes is a vendor-docs question.

### Editor's take

HumanLayer is the right shape for teams with Python or TypeScript agents where a handful of functions, such as moving money, sending bulk email, or deleting infrastructure, need a person's sign-off and that person already lives in Slack or email. Where a rule can decide without a human, Sondera or Cordum is a closer match. The verdict here leans on the dossier and HumanLayer's public docs; no approval request was routed through it for this page.

</section>

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
