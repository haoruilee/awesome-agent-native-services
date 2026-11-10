---
title: "Agents Mail | Agent-Native Services"
service_name: "Agents Mail"
description: "Email for AI Agents"
permalink: /services/agents-mail/
page_kind: service
service_slug: "agents-mail"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/agents-mail.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agents-mail.md"
tagline: "Email for AI Agents"
website: "https://agentsmail.org"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · REST · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentsmail.org" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://agentsmail.org/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agents-mail.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

An agent that has to chase a vendor for a quote, or send a weekly report and read the replies, needs an email address that belongs to it. Borrowing a person's Gmail through a delegated token works until someone asks who actually sent the message. Agents Mail sells the other arrangement. Its homepage calls it "Email for AI Agents," and the dossier describes agent registration, programmatic inbox creation, sending and replying, and message retrieval.

### An inbox the agent signs up for

Onboarding starts with a URL. The agent reads `https://agentsmail.org/skill.md`, follows the registration steps, stores its API credentials, and then provisions inboxes and handles mail through a REST API. The dossier also cites a discovery document at `https://agentsmail.org/.well-known/agent.json` for machine-readable capability metadata. Inbound mail arrives by polling or by receiving updates; the record does not say which mechanism the API exposes, so check the [API docs](https://agentsmail.org/docs) before designing a reply loop around it.

There is no official MCP server as of the dossier's last check, which dates that status to April 2026. The Agent Skill is the `skill.md` file itself. An agent that can fetch a URL and make HTTP calls has everything it needs. An MCP-only client would need a wrapper.

The identity model is the part that differs from a human mail API. Each agent registers its own credentials, mailboxes are scoped to that identity, and send, reply, and read actions are attributable to the registered key. One mailbox per agent role is one of the dossier's use cases, and it maps cleanly onto multi-agent systems where you want to know which worker wrote which message.

### Mail beside mail

The [communication collection](/categories/communication/) has several agent email services, and the [guide to choosing an email API for agents](/guides/choose-an-email-api-for-agents/) walks through them. [MailboxKit](/services/mailboxkit/) gives each agent a real address over REST, with inbound webhooks and custom domains in its dossier. [OpenMail](/services/openmail/) also offers one inbox per agent and pushes inbound mail over webhooks or WebSocket. [ATXP Email](/services/atxp-email/) frames the inbox as an identity for receiving verification codes and notifications. [MCP Agent Mail](/services/mcp-agent-mail/) uses the word mail but is something else: a coordination layer for coding agents with identities, threads, and file leases, over MCP rather than SMTP. [Chimely](/services/chimely/) delivers to an in-app inbox, not to an email address.

Before committing, read the docs for things the dossier leaves open: which domains addresses live on and whether you can bring your own, how deliverability and sender reputation are handled, how attachments are treated, and what happens to an inbox when the agent's credentials are revoked. Those decide whether outside recipients will ever see the mail.

### Editor's take

Agents Mail is a sensible pick for an agent that should bootstrap its own mailbox from a single URL and then work over plain REST. If you want inbound mail pushed to the agent instead of fetched, or need your own sending domain, compare MailboxKit and OpenMail. If the recipients are other coding agents in the same repository, MCP Agent Mail is the better fit. Our view is drawn from the dossier and the vendor's public pages, without having registered an agent or sent a message.

</section>

## What it does

Agents Mail provides mailbox infrastructure specifically for AI agents: programmatic inbox creation, sending/replying to email, message retrieval, and machine-readable onboarding/discovery metadata. The service is explicitly framed as communication infrastructure for autonomous agents rather than as a human mailbox product with add-on APIs.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, Agent Skill, REST, http, API
- **MCP:** ⚠️ Not yet published as an official dedicated MCP server (as of April 15, 2026).
- **Agent Skill:** ✅ Available (URL onboarding)
- **Onboarding type:** `url`

## How agents onboard

```text
https://agentsmail.org/skill.md
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agents-mail.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | https://agentsmail.org/docs |
| URL onboarding | `https://agentsmail.org/skill.md` |
| Agent metadata | `https://agentsmail.org/.well-known/agent.json` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
