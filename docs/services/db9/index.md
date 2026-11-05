---
title: "db9 | Agent-Native Services"
service_name: "db9"
description: "Postgres but for agents"
permalink: /services/db9/
page_kind: service
service_slug: "db9"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/db9.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/db9.md"
tagline: "Postgres but for agents"
website: "https://db9.ai"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · REST · CLI · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://db9.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://db9.ai/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/db9.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

db9 is a **serverless PostgreSQL platform designed for AI agents** — combining a relational database with cloud-native filesystem storage in one unified workspace. Agents get SQL for structured state (metadata, embeddings, run history) and a filesystem for unstructured context (transcripts, reports, artifacts) — no S3 or external vector DB required.

Built-in superpowers: JSONB, pgvector-compatible vector search, HTTP calls from SQL, filesystem queries (fs9), cron jobs (pg_cron), full-text search with Chinese tokenizer, and environment branching that clones entire databases for isolated testing.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐ — the highest tier of agent-nativeness.
- **Catalog protocols:** URL onboarding, Agent Skill, REST, CLI, SDK, http, API
- **MCP:** ⚠️ Not yet published
- **Agent Skill:** ✅ URL Onboarding via skill.md — agent reads https://db9.ai/skill.md and follows instructions
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐ — the highest tier of agent-nativeness.

```
Read https://db9.ai/skill.md and follow the instructions.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/db9.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `db9 create`, `db9 db sql`, `db9 fs`, `db9 token create` |
| REST API | `https://api.db9.ai` — databases, SQL execution, file ops |
| PostgreSQL | Direct pgwire to `pg.db9.io:5433` |
| TypeScript SDK | `get-db9` npm package — `instantDatabase()`, `createDb9Client()` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
