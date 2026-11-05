---
title: "Vectoree | Agent-Native Services"
service_name: "Vectoree"
description: "Give your coding agent a backend"
permalink: /services/vectoree/
page_kind: service
service_slug: "vectoree"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/vectoree.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/vectoree.md"
tagline: "Give your coding agent a backend"
website: "https://vectoree.ai"
repository: "https://github.com/VectoreeAI/vectoree-skills"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · CLI · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://vectoree.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://vectoree.ai/SKILL.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/VectoreeAI/vectoree-skills" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/vectoree.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Vectoree is a **backend cloud for coding agents**: models, app-user auth, Postgres, and object storage behind one project key. Agents install the Vectoree skill, log in and link a project with the CLI, then call an OpenAI-compatible gateway (`https://vectoree.ai/api/v1`) or create tables / buckets through the CLI and console.

Model Plaza reaches providers including xAI, OpenAI, Google, Anthropic, and DeepSeek (and other OpenAI-compatible endpoints) with one key. Auth covers email and Google sign-in for the agent's app users. Database is Postgres (dashboard or `vectoree db`). Storage is buckets for avatars, assets, and user content. Tool Hub lets the agent discover and connect agent-callable tools.

Pricing is pay-as-you-go for tokens with no monthly platform fee; new accounts get $5 welcome credit after CLI login and link, then Stripe top-ups into the org wallet.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐ — the highest tier of agent-nativeness.
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, CLI, http, API
- **MCP:** ⚠️ Available via Tool Hub (hosted MCP); configure from the Vectoree console after the project is linked
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐ — the highest tier of agent-nativeness.

```
Read https://vectoree.ai/SKILL.md and follow the instructions to connect this project.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/vectoree.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| URL Onboarding / Skill | https://vectoree.ai/SKILL.md · `npx skills add VectoreeAI/vectoree-skills` |
| CLI | `npx @vectoree/cli` (`login`, `link`, `current`, `ai`, `auth`, `db`, `storage`, `tools`, …) |
| OpenAI-compatible HTTP | `https://vectoree.ai/api/v1` with project API key |
| Tool Hub MCP | Hosted MCP tools configured after project link |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
