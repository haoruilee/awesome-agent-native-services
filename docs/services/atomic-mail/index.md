---
title: "Atomic Mail | Agent-Native Services"
service_name: "Atomic Mail"
description: "Not AI for your email. Email for your AI"
permalink: /services/atomic-mail/
page_kind: service
service_slug: "atomic-mail"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/atomic-mail.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/atomic-mail.md"
tagline: "Not AI for your email. Email for your AI"
verified_at: "2026-09-30"
website: "https://atomicmail.ai/"
repository: "https://github.com/Atomic-Mail/atomic-mail-agentic"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · CLI · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://atomicmail.ai/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://atomicmail.ai/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Atomic-Mail/atomic-mail-agentic" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/atomic-mail.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Atomic Mail is an AI-agent-first email provider. An agent registers its own `username@atomicmail.ai` inbox (username 5–21 characters) and then reads, sends, drafts, searches, and threads mail over JMAP (RFC 8620 / 8621). Access is gated by a proof-of-work signup so agents can onboard without CAPTCHAs or human approval. Custom domains are a separate human control plane in the dashboard because they need DNS changes.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⭐ — the homepage is the join document.
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, CLI, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⭐ — the homepage is the join document.

```text
Read https://atomicmail.ai and follow the instructions to create an inbox at Atomic Mail.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/atomic-mail.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Homepage onboarding | https://atomicmail.ai/ |
| Local MCP | `npx -y @atomicmail/mcp` (homepage) or `@atomicmail/mcp-github` (GitHub README) |
| Hosted MCP | `https://mcp.atomicmail.ai/mcp` |
| AgentSkill / CLI | `@atomicmail/agent-skill` / `@atomicmail/agent-skill-github` |
| JMAP | RFC 8620 / 8621 mailbox API |
| REST auth | Documented in repo `docs/rest-auth.md` |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://github.com/Atomic-Mail/atomic-mail-agentic/releases/tag/v0.3.31
- https://atomicmail.ai/

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
