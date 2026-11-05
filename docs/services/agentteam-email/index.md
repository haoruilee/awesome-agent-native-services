---
title: "AgentTeam Email | Agent-Native Services"
service_name: "AgentTeam Email"
description: "Open-source email infrastructure for AI agents"
permalink: /services/agentteam-email/
page_kind: service
service_slug: "agentteam-email"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/agentteam-email.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agentteam-email.md"
tagline: "Open-source email infrastructure for AI agents"
verified_at: "2026-09-30"
website: "https://www.agentteam.email"
repository: "https://github.com/agentteamhq/agentteam-email"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · CLI · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.agentteam.email" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://agentteamemail.mintlify.app/get-started/quickstart" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/agentteamhq/agentteam-email" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agentteam-email.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AgentTeam Email (AT Email) is open-source mail infrastructure that provisions a real mailbox per agent on a domain you control. Operators connect Cloudflare for send/receive, keep inbound mail in an R2 bucket before processing, and give agents scoped read/draft/send rights. A web client exists for humans, but the product is built around agent mailboxes, review-before-send, and an `at-email` CLI the agent can run.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + published Agent Skill
- **Catalog protocols:** Agent Skill, CLI, http
- **MCP:** ⚠️ Not published
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** CLI + published Agent Skill

```bash
npx --yes @agentteamhq/email@latest --version
at-email agent connect
# or
at-email agent trial
at-email agent enroll TOKEN
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agentteam-email.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `at-email` / `npx --yes @agentteamhq/email@latest` |
| Agent Skill | `skills/at-email-cli` |
| Hosted app | https://www.agentteam.email |
| Docs | https://agentteamemail.mintlify.app |
| Self-host | Docker Compose or Helm |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://agentteamemail.mintlify.app/

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
