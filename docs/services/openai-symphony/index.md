---
title: "OpenAI Symphony | Agent-Native Services"
service_name: "OpenAI Symphony"
description: "Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents"
permalink: /services/openai-symphony/
page_kind: service
service_slug: "openai-symphony"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/openai-symphony.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/openai-symphony.md"
tagline: "Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents"
verified_at: "2026-09-26"
website: "https://openai.com/index/open-source-codex-orchestration-symphony/"
repository: "https://github.com/openai/symphony"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · API · documentation</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://openai.com/index/open-source-codex-orchestration-symphony/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/openai/symphony/blob/main/SPEC.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/openai/symphony" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/openai-symphony.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Symphony continuously reads eligible work from an issue tracker, claims an issue, creates a deterministic isolated workspace, and launches a Codex app-server session inside it. It keeps the agent working through bounded turns, reconciles tracker state, schedules retries, and exposes structured runtime status. The work policy lives in version-controlled `WORKFLOW.md`, so the prompt, completion rules, proof requirements, and handoff state travel with the codebase.

The language-neutral [SPEC.md](https://github.com/openai/symphony/blob/main/SPEC.md) is the product contract. The included Elixir/OTP implementation is a reference implementation and supports Linear, GitHub Issues, Jira Cloud, Asana, and GitLab.

---

## Agent-facing interfaces

- **Interaction pattern:** Agent-readable specification or Elixir reference service
- **Catalog protocols:** Agent Skill, API, documentation
- **MCP:** ⚠️ No standalone MCP server
- **Agent Skill:** ✅ Repository skills available
- **Onboarding type:** `documentation`

## How agents onboard

**Interaction pattern:** Agent-readable specification or Elixir reference service

```text
Implement Symphony according to the following spec:
https://github.com/openai/symphony/blob/main/SPEC.md
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/openai-symphony.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Specification | `SPEC.md` — language-neutral normative service contract |
| Agent runtime | Codex app-server protocol |
| Tracker integrations | Linear, GitHub Issues, Jira Cloud, Asana, GitLab in the reference |
| Configuration | YAML front matter plus prompt body in repository-owned `WORKFLOW.md` |
| Operations | Structured logs, optional JSON API/dashboard, workspace lifecycle hooks |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/openai/symphony/releases/tag/v0.0.3
- https://api.github.com/repos/openai/symphony

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
