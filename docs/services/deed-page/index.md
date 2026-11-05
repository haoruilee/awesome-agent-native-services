---
title: "deed.page | Agent-Native Services"
service_name: "deed.page"
description: "Permanent static hosting for AI agents"
permalink: /services/deed-page/
page_kind: service
service_slug: "deed-page"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/deed-page.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/deed-page.md"
tagline: "Permanent static hosting for AI agents"
verified_at: "2026-10-26"
website: "https://deed.page"
repository: "https://github.com/f-o-x11/deed-page-skill"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Agent Skill and plugin manifests: MIT. The hosted service itself is closed-source</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · webhook · CLI · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://deed.page" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://deed.page/docs · https://deed.page/llms.txt · https://deed.page/openapi.json" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/f-o-x11/deed-page-skill" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/deed-page.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

deed.page is static web hosting for AI agents. An agent publishes HTML, a few files or a whole folder (raw HTML, tarball, multipart or a JSON file map) with one PUT or POST and gets a live, permanent `https://<slug>.deed.page/` URL at a slug it picks. There is no account, email code or claim link in the agent's path, and sites do not expire unless the agent sets a TTL. The response carries an owner token, which the agent keeps to update the same slug later. Every publish is a retained, addressable version that can be listed and restored. The service hosts static files only (no server-side code or databases). The Free plan is $0 with 25 sites and 25 MB per site; Hobby is $3/month and Pro $15/month (https://deed.page/pricing).

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, webhook, CLI, openapi, http, API
- **MCP:** ✅ Available — hosted remote server
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding

```
Read https://deed.page/skill.md and follow the instructions to publish a page.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/deed-page.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `PUT/POST /v1/sites`, versions, restore, uploads, manifests, domains, webhooks, analytics, tokens — reference at https://deed.page/docs, OpenAPI 3.1 at https://deed.page/openapi.json |
| MCP | Remote Streamable HTTP server at https://deed.page/mcp (26 tools); ChatGPT variant at https://deed.page/mcp/chatgpt |
| URL onboarding | https://deed.page/skill.md and https://deed.page/llms.txt |
| Agent Skill | `npx skills add f-o-x11/deed-page-skill` (MIT), with plugin manifests for Claude Code, Codex, Cursor, Gemini CLI and Grok Bot |
| Webhooks | Signed (`Deed-Signature`) events: `site.published`, `site.version_restored`, `site.deleted`, `site.taken_down`, `domain.active`, `report.received` |

---

## Verification

Last verified **2026-10-26**.

Sources:
- https://deed.page
- https://deed.page/llms.txt
- https://deed.page/pricing
- https://deed.page/openapi.json
- https://deed.page/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
