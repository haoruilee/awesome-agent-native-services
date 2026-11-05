---
title: "Modal | Agent-Native Services"
service_name: "Modal"
description: "AI infrastructure that developers love"
permalink: /services/modal/
page_kind: service
service_slug: "modal"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/modal.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/modal.md"
tagline: "AI infrastructure that developers love"
website: "https://modal.com"
repository: "https://github.com/modal-labs/modal-client"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · SDK · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://modal.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://modal.com/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/modal-labs/modal-client" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/modal.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Modal is **serverless infrastructure for AI workloads**: **inference**, **fine-tuning**, **batch** jobs, **notebooks**, and **dynamic sandboxes** with **sub-second cold starts**, **elastic GPU/CPU** scaling, and **unified observability**. It is explicitly marketed for **LLM inference**, **evals**, **RL environments**, and **MCP servers** at scale — workloads that autonomous agents and their orchestrators spawn unpredictably.

---

## Agent-facing interfaces

- **Catalog protocols:** CLI, SDK, http
- **MCP:** ⚠️ Not an MCP product; teams deploy MCP servers on Modal (see customer quotes on modal.com).
- **Agent Skill:** ⚠️ No official AgentSkills bundle located.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
pip install modal
modal setup
# Define Modal app in Python per https://modal.com/docs/guide
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/modal.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install modal` |
| CLI | `modal` — deploy, run, logs |
| HTTP | Function endpoints — see docs |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
