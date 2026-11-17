---
title: "nPubMail | Agent-Native Services"
service_name: "nPubMail"
description: "Email for AI agents. The key is the account"
permalink: /services/npubmail/
page_kind: service
service_slug: "npubmail"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/npubmail.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/npubmail.md"
tagline: "Email for AI agents. The key is the account"
verified_at: "2026-11-16"
website: "https://npubmail.com"
repository: "https://github.com/obvioussummer46/npubmail"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-16</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://npubmail.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://npubmail.com/llms.txt" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/obvioussummer46/npubmail" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/npubmail.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

nPubMail gives an AI agent a real email address whose account is the agent's own Nostr keypair. The agent creates the mailbox itself, receives mail, waits for a verification code or link and gets it back extracted, creates disposable aliases with expiry and sender filters, replies, and sends. Inbound mail carries SPF/DKIM verdicts and prompt-injection warnings, and is stored encrypted to the agent's key.

Receiving, replying to senders who wrote first, and mailing other npubmail addresses are free. Mailing an outside address that never wrote first costs 10 sats per recipient: the API answers HTTP 402 with a Lightning (or Cashu) invoice, the agent pays, then repeats the call with the payment ID.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI
- **Catalog protocols:** Agent Skill, MCP, REST, CLI, STDIO, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI

```
curl -fsSL https://npubmail.com/install | sh && npubmail init myagent
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/npubmail.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| URL Onboarding | https://npubmail.com/llms.txt |
| REST API | https://npubmail.com/api, NIP-98 signed requests |
| CLI | `npubmail` (`init`, `alias`, `code`, `list`, `read`, `send`, `wallet setup`) |
| MCP | `npubmail-mcp` (stdio), registry `com.npubmail/npubmail` |
| Payments | HTTP 402 with Lightning or Cashu invoice, per action |
| Agent Skills | https://npubmail.com/.well-known/skills/npubmail/SKILL.md |

---

## Verification

Last verified **2026-11-16**.

Sources:
- https://npubmail.com
- https://npubmail.com/llms.txt
- https://npubmail.com/api
- https://npubmail.com/setup
- https://npubmail.com/.well-known/skills/npubmail/SKILL.md
- https://github.com/obvioussummer46/npubmail

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
