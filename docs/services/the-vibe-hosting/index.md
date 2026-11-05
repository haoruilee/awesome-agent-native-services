---
title: "The Vibe Hosting | Agent-Native Services"
service_name: "The Vibe Hosting"
description: "One prompt → root Linux → your project is live"
permalink: /services/the-vibe-hosting/
page_kind: service
service_slug: "the-vibe-hosting"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/the-vibe-hosting.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/the-vibe-hosting.md"
tagline: "One prompt → root Linux → your project is live"
website: "https://thevibehosting.com"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · REST · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://thevibehosting.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://thevibehosting.com/SKILL.md · https://thevibehosting.com/api" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/the-vibe-hosting.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

The Vibe Hosting gives an AI coding agent a real root Ubuntu server, isolated in a gVisor sandbox, on a live HTTPS subdomain (or on the user's own domain — point a CNAME at it and HTTPS is issued automatically) — created with a single unauthenticated `POST /create`. There is no signup form, dashboard or payment method in the agent's path: the first call mints the account credential (`api_key`) together with the server, and the agent then deploys over SSH, publishes on port 80 (or a static `/root/www`), and manages the server through the same API.

Servers scale to zero when idle and wake on the next HTTP request or SSH connection, so an agent can keep long-lived projects (web apps, bots, workers, MCP servers) without a human managing them. Usage is billed from a prepaid credit with a monthly free allowance; the service itself is closed-source.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, Agent Skill, REST, http, API
- **MCP:** ⚠️ Not yet published — the agent uses the REST API directly with curl.
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

```text
Read https://thevibehosting.com/SKILL.md and follow the instructions to deploy your project.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/the-vibe-hosting.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `POST /create`, `GET/DELETE /servers/{id}`, `/sleep`, `/wake`, `/never-sleep`, `/expose`, `/ssh-key`, `/subdomain`, `/domain`, `GET /account/billing`, `GET /account/usage`, `POST /feedback` — reference at https://thevibehosting.com/api |
| SSH | Root access to each server for deployment and operations |
| URL onboarding | https://thevibehosting.com/SKILL.md |
| Agent Skill | `npx skills add ladik33/thevibehosting-skill` (Claude Code, Cursor, Codex) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
