---
title: "Agent Sandbox | Agent-Native Services"
service_name: "Agent Sandbox"
description: "The trusted runtime for untrusted code"
permalink: /services/agent-sandbox/
page_kind: service
service_slug: "agent-sandbox"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/agent-sandbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-sandbox.md"
tagline: "The trusted runtime for untrusted code"
website: "https://agentsandbox.co"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentsandbox.co" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://agentsandbox.co/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-sandbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agent Sandbox provides a managed, isolated runtime where AI agents can execute Python and shell commands, install dependencies, and exchange files through a single API. The product is positioned around giving each agent a personal remote computer and drive, with explicit support for sessioned execution and artifact pipelines.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, Agent Skill, REST, SDK, http, API
- **MCP:** ⚠️ Not yet published as a dedicated official MCP server (as of April 15, 2026).
- **Agent Skill:** ✅ Available (URL onboarding at https://agentsandbox.co/skill.md)
- **Onboarding type:** `url`

## How agents onboard

```text
https://agentsandbox.co/skill.md
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-sandbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | https://agentsandbox.co/docs |
| Python SDK | `pip install agentsandbox-sdk` |
| URL Onboarding | `https://agentsandbox.co/skill.md` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
