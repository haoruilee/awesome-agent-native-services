---
title: "ReleaseLog | Agent-Native Services"
service_name: "ReleaseLog"
description: "Verified AI release intelligence for AI agents"
permalink: /services/releaselog/
page_kind: service
service_slug: "releaselog"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/releaselog.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/releaselog.md"
tagline: "Verified AI release intelligence for AI agents"
website: "https://releaselog.site"
repository: "https://github.com/haoruilee/releaselog"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Optional</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://releaselog.site" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://releaselog.site/skill.md · https://releaselog.site/llms.txt" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/releaselog" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/releaselog.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

ReleaseLog is a verified changelog of AI lab and product launches — Anthropic, Claude, OpenAI, and the other entities in the public entity list — shaped so an agent can poll it. Each release row is a structured object (`whatChanged`, `importance`, `entityId`, `sourceUrl`, and optional `kind`, `audience`, `status`, `tags`) instead of a human changelog page. The shipping calendar at the site root is the secondary view of the same data.

Public reads are unauthenticated. Checked on 2026-11-05: `https://releaselog.site/skill.md` returned `text/markdown`, `https://releaselog.site/llms.txt` returned `text/plain`, `GET /api/v1/entity-list` and `GET /api/v1/releases/recent` returned JSON, `GET /api/v1/export.ndjson` returned NDJSON, and `https://releaselog.site/feeds/atom.xml` plus `https://releaselog.site/feeds/openai-team/atom.xml` returned Atom. A 365-day recent page of 200 rows included `whatChanged` on 183 rows and `importance` on every row; `kind: "event"` appeared when the entry is an event rather than a shipped release.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐ + public JSON API + Atom feeds. Local stdio MCP is optional.
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, http, API
- **MCP:** ⚠️ Optional local stdio plugin; no hosted MCP endpoint
- **Agent Skill:** ✅ Repository skill ships with the Codex plugin
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐ + public JSON API + Atom feeds. Local stdio MCP is optional.

```
Read https://releaselog.site/skill.md and follow the instructions.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/releaselog.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| URL onboarding | `https://releaselog.site/skill.md` (`text/markdown`) and `https://releaselog.site/llms.txt` |
| REST JSON API | `GET /api/v1/entity-list`, `/api/v1/releases/recent`, `/api/v1/entities/{entityId}`, `/api/v1/entity-releases/{entityId}` — schema version `1.0`, unauthenticated public reads |
| NDJSON | `GET /api/v1/export.ndjson` |
| Atom | `GET /feeds/atom.xml`, `GET /feeds/{entityId}/atom.xml`; optional `GET /feeds/private/{token}.xml` |
| MCP | Local stdio plugin only (`plugins/releaselog-trends`). No hosted MCP URL |
| Repo skill | `plugins/releaselog-trends/skills/releaselog-trends/SKILL.md` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
