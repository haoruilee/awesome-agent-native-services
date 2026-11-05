---
title: "Context7 | Agent-Native Services"
service_name: "Context7"
description: "Up-to-date Docs for AI Agents"
permalink: /services/context7/
page_kind: service
service_slug: "context7"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/context7.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/context7.md"
tagline: "Up-to-date Docs for AI Agents"
verified_at: "2026-10-30"
website: "https://context7.com"
repository: "https://github.com/upstash/context7"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (MCP server + ctx7 CLI); hosted index is operated by Upstash</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://context7.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://context7.com/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/upstash/context7" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/context7.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Context7 indexes library and framework documentation and serves version-specific snippets to coding agents at the moment they write code, so the agent stops relying on stale training data or hallucinated APIs. Prompts can name a library id (`/supabase/supabase`) or a version and Context7 matches it.

---

## Agent-facing interfaces

- **Interaction pattern:** Remote MCP or CLI + Skill
- **Catalog protocols:** MCP, CLI, http
- **MCP:** ✅ Available — hosted remote MCP and the MIT @upstash/context7-mcp package.
- **Agent Skill:** ✅ ctx7 setup installs a skill that tells the agent when and how to fetch docs with ctx7 CLI commands (no MCP needed).
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** Remote MCP or CLI + Skill

```bash
npx ctx7 setup            # OAuth, mints an API key, installs a skill or MCP config
# targets: --cursor, --claude, --opencode
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/context7.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Remote MCP | `https://mcp.context7.com/mcp` |
| npm | `@upstash/context7-mcp` |
| CLI | `ctx7` (`setup`, `remove`, doc queries) |
| Docs | https://context7.com/docs/resources/all-clients |

---

## Verification

Last verified **2026-10-30**.

Sources:
- https://api.github.com/repos/upstash/context7

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
