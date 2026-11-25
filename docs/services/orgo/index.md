---
title: "Orgo | Agent-Native Services"
service_name: "Orgo"
description: "Computers for Agents"
permalink: /services/orgo/
page_kind: service
service_slug: "orgo"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/orgo.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/orgo.md"
tagline: "Computers for Agents"
verified_at: "2026-11-25"
website: "https://www.orgo.ai"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Hosted product closed-source. https://github.com/nickvasilescu/orgo-mcp is MIT and is an API wrapper, not the platform source</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · CLI · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-25</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.orgo.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.orgo.ai/for-agents" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/orgo.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Orgo rents an isolated cloud computer to an agent: Linux or Windows (and Mac when the app has stock), with a desktop, a browser, and a terminal. The agent screenshots, clicks, types, and runs bash. Each computer is its own VM. Docs `llms.txt`: *"A new computer is online in seconds and runs until you stop it."* Orgo does not supply the agent model. The caller brings Claude Computer Use, another computer-use model, or its own loop.

The hosted product is closed-source. API keys begin with `sk_live_` (docs). A computer status moves through creating, running, frozen/stopped, and deleted. `stop` freezes the machine.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐ + REST + hosted MCP. Unclaimed accounts that have added less than $5 expire 72 hours after signup. While signups are busy, verification.required blocks launches until a person opens claim.url or credit is added. The usual claude mcp add sign-in is a person clicking Allow, which is not this URL path.
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, CLI, http, API
- **MCP:** ✅ Available — hosted Streamable HTTP, POST-only
- **Agent Skill:** ✅ Available — Claude Code skill computer
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐ + REST + hosted MCP. Unclaimed accounts that have added less than $5 expire 72 hours after signup. While signups are busy, verification.required blocks launches until a person opens claim.url or credit is added. The usual claude mcp add sign-in is a person clicking Allow, which is not this URL path.

```
Read https://www.orgo.ai/orgo.md and follow the instructions to create an agent account.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/orgo.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Agent signup | `POST https://www.orgo.ai/api/v1/agents` |
| Claim | `POST https://www.orgo.ai/api/v1/agents/claim` |
| REST | `https://www.orgo.ai/api` — bearer `sk_live_…` key |
| CLI | `npx -y orgo@latest init` or https://orgo.ai/install.sh |
| Hosted MCP | `https://www.orgo.ai/mcp` (POST-only) |
| Docs | https://docs.orgo.ai/for-agents · https://docs.orgo.ai/llms.txt · https://www.orgo.ai/orgo.md |

---

## Verification

Last verified **2026-11-25**.

Sources:
- https://www.orgo.ai
- https://www.orgo.ai/orgo.md
- https://docs.orgo.ai/for-agents
- https://docs.orgo.ai/guides/mcp
- https://docs.orgo.ai/llms.txt
- https://orgo.ai/skills/computer/SKILL.md
- https://www.orgo.ai/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
