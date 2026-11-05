# ReleaseLog

> **"Verified AI release intelligence for AI agents."**

| | |
|---|---|
| **Website** | https://releaselog.site |
| **Docs** | https://releaselog.site/skill.md · https://releaselog.site/llms.txt |
| **GitHub** | https://github.com/haoruilee/releaselog |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/haoruilee/releaselog?style=social)](https://github.com/haoruilee/releaselog) |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |
| **Disclosure** | Maintainer inclusion. ReleaseLog is published by the same curator as this catalog. |

---

## Official Website

https://releaselog.site

---

## Official Repo

https://github.com/haoruilee/releaselog

Public source for the site, curated entity data, JSON and Atom routes, and the local stdio MCP plugin at `plugins/releaselog-trends/`. No `LICENSE` file is published, and `package.json` does not declare a license (confirmed 2026-11-05). The live agent surface is the site, not a clone step.

---

## ⭐ How to Use (Agent Onboarding)

> **⭐ URL Onboarding — an agent starts by reading one URL. Public reads need no API key.**

**Interaction pattern:** URL Onboarding ⭐ + public JSON API + Atom feeds. Local stdio MCP is optional.

**One-sentence instruction:**
```
Read https://releaselog.site/skill.md and follow the instructions.
```

**What the agent gets by reading that URL:** the release-object fields, the no-key read endpoints (`/api/v1/entity-list`, `/api/v1/releases/recent`, `/api/v1/entity-releases/{entityId}`, `/api/v1/entities/{entityId}`, `/api/v1/export.ndjson`), the Atom feeds, and the trending / latest / compare workflow. The human shipping calendar is documented as the secondary view. There is no hosted `/mcp` URL.

Companion discovery file: https://releaselog.site/llms.txt

---

## Agent Skills

**Status:** ✅ Repository skill ships with the Codex plugin

| Document | What it teaches the agent |
|---|---|
| [skill.md](https://releaselog.site/skill.md) | URL onboarding: poll JSON and Atom, do not scrape the calendar HTML |
| [plugins/releaselog-trends/skills/releaselog-trends/SKILL.md](https://github.com/haoruilee/releaselog/blob/main/plugins/releaselog-trends/skills/releaselog-trends/SKILL.md) | When to call the local MCP tools versus the public API |

This is not an `npx skills add` package. The hosted `skill.md` is the join path.

---

## MCP

**Status:** ⚠️ Optional local stdio plugin; no hosted MCP endpoint

Do not call `https://releaselog.site/mcp`. The site documents that path as absent.

| Detail | Value |
|---|---|
| **Repo** | https://github.com/haoruilee/releaselog/tree/main/plugins/releaselog-trends |
| **Transport** | stdio (`node scripts/releaselog-mcp.mjs`), registered by `plugins/releaselog-trends/.mcp.json` |
| **Auth** | None for the public API. `RELEASELOG_API_BASE` defaults to `https://releaselog.site` |
| **Tools** | `release_log_trending_now`, `release_log_latest_releases`, `release_log_trends`, `release_log_list_sources`, `release_log_source_releases`, `release_log_source_detail` |
| **Self-test** | `node scripts/releaselog-mcp.mjs --self-test` |

`release_log_trending_now` and `release_log_trends` add a deduped `brief` (`headline`, `summary`, `notableLaunches`, `notableEvents`, `suggestedAnswerBullets`) and `topThemes`. Those summaries are plugin output. `GET /api/v1/releases/recent` returns release rows, not that brief.

---

## What It Does

ReleaseLog is a verified changelog of AI lab and product launches — Anthropic, Claude, OpenAI, and the other entities in the public entity list — shaped so an agent can poll it. Each release row is a structured object (`whatChanged`, `importance`, `entityId`, `sourceUrl`, and optional `kind`, `audience`, `status`, `tags`) instead of a human changelog page. The shipping calendar at the site root is the secondary view of the same data.

Public reads are unauthenticated. Checked on 2026-11-05: `https://releaselog.site/skill.md` returned `text/markdown`, `https://releaselog.site/llms.txt` returned `text/plain`, `GET /api/v1/entity-list` and `GET /api/v1/releases/recent` returned JSON, `GET /api/v1/export.ndjson` returned NDJSON, and `https://releaselog.site/feeds/atom.xml` plus `https://releaselog.site/feeds/openai-team/atom.xml` returned Atom. A 365-day recent page of 200 rows included `whatChanged` on 183 rows and `importance` on every row; `kind: "event"` appeared when the entry is an event rather than a shipped release.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | `llms.txt`: "Verified AI release intelligence for AI agents." `skill.md`: "You are an AI agent. You are a first-class consumer of ReleaseLog" and "Poll structured release objects. Do not scrape human changelog pages or the calendar HTML." README: "AI agents are a primary consumer of this feed." — https://releaselog.site/llms.txt · https://releaselog.site/skill.md · https://github.com/haoruilee/releaselog |
| **Agent-specific primitive** | A release object whose one-line `whatChanged` is documented as "for lists and agent summaries," plus `importance` (1–3), `entityId` / `entityName`, and `kind` of `release` or `event`. Entity summaries expose separate `releaseCount` and `eventCount`. The local trend tools add `brief.suggestedAnswerBullets` so the agent does not rebuild the answer from raw rows. — https://github.com/haoruilee/releaselog/blob/main/data/types.ts · https://releaselog.site/skill.md |
| **Autonomy-compatible control plane** | Public JSON and Atom need no signup, no API key, and no human click. An agent can list entities, pull a window (`days`, `limit`, `offset`, `entity`, `tag`, `audience`, `status`; entity routes also take `from` and `to`), and poll Atom on its own loop. Curation (what gets verified into the log) is upstream of that loop; the agent does not click to read. |
| **M2M integration surface** | Hosted `skill.md` and `llms.txt`, JSON (`/api/v1/entity-list`, `/api/v1/releases/recent`, `/api/v1/entities/{entityId}`, `/api/v1/entity-releases/{entityId}`, `/api/v1/export.ndjson`), and Atom (`/feeds/atom.xml`, `/feeds/{entityId}/atom.xml`). Optional local stdio MCP. No dashboard is required for public reads. |
| **Identity / delegation** | **Partial, stated plainly.** Public reads are anonymous and only read. The service does not mint an agent identity and does not take external actions on a user's behalf. A Pro private Atom token (`/feeds/private/{token}.xml`) is optional and only if a human already issued one; `skill.md` says that token "is a credential for the private feed, not an agent identity." Each public row's `sourceUrl` points at the lab's own page. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Release object** | One verified launch: `id`, `date`, `title`, `whatChanged`, `importance`, `sourceUrl`, `entityId`, `entityName`, plus optional `kind`, `status`, `audience`, `tags`, `shortTitle` |
| **Entity** | A tracked lab or product (`openai-team`, `anthropic-team`, `claude-product`, and the rest of `/api/v1/entity-list`) with separate release and event counts |
| **Recent window** | `GET /api/v1/releases/recent?days=&limit=` for a pollable slice, sorted by date then importance |
| **Entity timeline** | `GET /api/v1/entity-releases/{entityId}?from=&to=` |
| **Atom feed** | `/feeds/atom.xml` and `/feeds/{entityId}/atom.xml` for change detection; entries link back to the calendar |
| **Trend brief** | Local MCP only: deduped `brief` and `topThemes` from `release_log_trending_now` / `release_log_trends` |

---

## Autonomy Model

1. Agent reads `https://releaselog.site/skill.md` (or `llms.txt`).
2. Agent loads `GET /api/v1/entity-list` when it does not already know the entity id.
3. Agent polls `GET /api/v1/releases/recent` or an entity timeline, or watches the Atom feed and fetches JSON when the feed moves.
4. Agent answers from `whatChanged`, dates, entity names, and `sourceUrl`. It keeps `kind: "event"` separate from shipped releases.
5. If the local plugin is installed, the agent calls `release_log_trending_now` (7-day deduped brief) or `release_log_trends` instead of hand-rolling the same requests.
6. No account, key, or approval click sits on the public read path.

---

## Identity and Delegation Model

- Public JSON, NDJSON, and Atom are world-readable. No credential is issued to the agent.
- The optional Pro private feed token is a human-issued secret for `/feeds/private/{token}.xml`. It is not an agent id, and agents are told not to invent one for public reads.
- ReleaseLog does not send mail, pay, or call third parties on the agent's behalf. Weekly digest and Stripe billing are human account features and are outside the public read loop.
- The attributable artifact on a row is `sourceUrl` (the upstream lab page), not a per-agent audit log.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| URL onboarding | `https://releaselog.site/skill.md` (`text/markdown`) and `https://releaselog.site/llms.txt` |
| REST JSON API | `GET /api/v1/entity-list`, `/api/v1/releases/recent`, `/api/v1/entities/{entityId}`, `/api/v1/entity-releases/{entityId}` — schema version `1.0`, unauthenticated public reads |
| NDJSON | `GET /api/v1/export.ndjson` |
| Atom | `GET /feeds/atom.xml`, `GET /feeds/{entityId}/atom.xml`; optional `GET /feeds/private/{token}.xml` |
| MCP | Local stdio plugin only (`plugins/releaselog-trends`). No hosted MCP URL |
| Repo skill | `plugins/releaselog-trends/skills/releaselog-trends/SKILL.md` |

---

## Human-in-the-Loop Support

None on the public read path. Humans curate and verify what enters the log, and humans can subscribe, sign in, or hold a Pro token. An agent polling releases does not wait on those steps. Injection of a private-feed token, if used at all, is something a human already handed over.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Vendor changelog HTML and blogs** | Written for a person to scroll. No stable release object with `whatChanged`, `importance`, and `entityId`, and no instruction to treat the calendar as secondary. |
| **A generic RSS reader** | Can poll a feed, but does not split shipped releases from events, rank by importance, or expose a per-entity JSON window an agent can filter. |
| **General web search** | Returns pages about launches. It does not maintain a verified entity registry or a pollable changelog whose fields are defined for agent summaries. |

---

## Use Cases

- **Context refresh** — before answering "what shipped this week," poll a 7-day window and cite `whatChanged` plus `sourceUrl`
- **Lab comparison** — load the entity list, then query two entity timelines over the same `from` / `to` range
- **Feed-driven polling** — watch `/feeds/atom.xml` and fetch JSON only when the feed updates
- **Trend brief** — with the local plugin, call `release_log_trending_now` and answer from `brief` instead of rebuilding the summary from raw rows
