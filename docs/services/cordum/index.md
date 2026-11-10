---
title: "Cordum | Agent-Native Services"
service_name: "Cordum"
description: "The open agent control plane"
permalink: /services/cordum/
page_kind: service
service_slug: "cordum"
category_slug: "oversight-and-approval"
category_label: "Oversight & Approval"
hero_image: "/assets/images/editorial-oversight.webp"
image: "/assets/images/editorial-oversight.webp"
classification: "agent-native"
dossier_path: "services/oversight-and-approval/cordum.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/cordum.md"
tagline: "The open agent control plane"
website: "https://github.com/cordum-io/cordum"
repository: "https://github.com/cordum-io/cordum"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Oversight &amp; Approval</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/cordum-io/cordum" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/cordum-io/cordum" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/cordum.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

An operations agent eventually reaches a step that should not run on its own say-so: a write to production, a payment, a message to a customer. Somebody has to decide before the call goes out, and somebody later has to see what was decided. The Cordum repository describes itself as "The open agent control plane." The dossier turns that into four pieces: pre-execution policy, approval gates, audit trails, and MCP adapters.

### Gates before the tool call

The onboarding line in the dossier is one sentence. An operator deploys Cordum, then connects LangChain, CrewAI, or MCP agents to its policy gates. From then on the agent works through the CLI, API, or MCP surface the project documents. Each bounded action passes policy, waits at an approval gate, or stops. The outcome returns to the agent loop instead of sitting on a dashboard someone has to watch.

MCP is marked as documented. No dedicated Agent Skill is listed, so an agent cannot read one bootstrap file and wire itself in. A person deploys the service first and points the agent at it. The [GitHub repository](https://github.com/cordum-io/cordum) is the only vendor source the catalog cites. There is no separate docs site in the record.

The [oversight and approval collection](/categories/oversight-and-approval/) holds several services with overlapping words, so the shape matters more than the label. [Preloop](/services/preloop/) also presents itself as an open-source control plane for agents and deserves a side-by-side read. [HumanLayer](/services/humanlayer/) and [withHuman](/services/withhuman/) put the human approval request at the center. [Sondera Coding Agent Hooks](/services/sondera-coding-agent-hooks/) wraps a coding agent's session and intercepts its shell, file, and web actions. Cordum's pitch is the combination: policy, approval, and audit held by one deployed service that several agent frameworks can call.

### What the repository has to answer

Parts of the dossier are generic. Its identity section says a session is represented by caller configuration or a policy subject, and that delegation comes from runtime limits, allowlists, approval thresholds, or deployment credentials. That is a menu, not a specification. Before you depend on Cordum, read the repository for which of those it enforces, how a policy is written, what an approval request looks like to the person who receives it, and where audit records live.

Check who runs the process, too. Self-deployment means your team owns its availability. If the gate is unreachable, does the agent fail closed or carry on? The record does not say. The [guide to what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why that question decides whether a control plane is a boundary or a suggestion.

### Editor's take

Cordum fits a team that already runs agents on LangChain, CrewAI, or MCP and wants policy, approvals, and audit in one place it hosts itself. If the real need is a human approval step in front of specific actions, start with HumanLayer or withHuman. If the agent is a coding assistant and the risk is its shell, Sondera is closer to the problem. This opinion comes from reading the catalog entry and the public repository. Nobody on this project has deployed Cordum or routed an agent through its gates.

</section>

## What it does

Cordum provides the open agent control plane. Its agent-facing value is to give autonomous systems a programmatic primitive that can be invoked during a task loop without requiring a human to operate a dashboard for each action.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, http
- **MCP:** ✅ Verified/documented by upstream or MCP server listings.
- **Agent Skill:** ⚠️ No dedicated catalog skill verified in this entry. Search ClawHub or the upstream README for the latest installable skills.
- **Onboarding type:** `mcp`

## Protocol surface

| Interface | Detail |
|---|---|
| **Primary surface** | Pre-execution policy, approval gates, audit trails, MCP adapters |
| **Repository** | https://github.com/cordum-io/cordum |
| **MCP** | ✅ |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/oversight-and-approval/' | relative_url }}"><small>Collection</small><strong>← Oversight &amp; Approval</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
