---
title: "AgentMail | Agent-Native Services"
service_name: "AgentMail"
description: "Email for AI agents"
permalink: /services/agentmail/
page_kind: service
service_slug: "agentmail"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/agentmail.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agentmail.md"
tagline: "Email for AI agents"
website: "https://agentmail.to"
repository: "https://github.com/agentmail-to"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · webhook · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentmail.to" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.agentmail.to" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/agentmail-to" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/agentmail.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

### Who holds the key

The dossier is clear that an AgentMail inbox belongs to the agent rather than forwarding from a person's account. It is less clear about the credential behind it. Operators can provision inboxes for agents or let agents create their own, but nothing in the record says whether an API key can be limited to one inbox, or whether any key that sends from one address can also read every thread in the account. For a fleet where each agent should see only its own mail, that is the first question to put to the [AgentMail docs](https://docs.agentmail.to).

There is also no official Agent Skill. The dossier points to community marketplaces and to the REST reference for anyone who wants to write one. The MCP server is official but listed only with a stdio transport, so it runs as a local process next to the client and holds whatever key you hand it.

### Inbox as the unit

What is documented is small and concrete. Install with `pip install agentmail` or `npm install agentmail`, then `POST /inboxes` returns a new address. The agent sets a webhook URL to hear about inbound mail, sends with `POST /inboxes/{id}/messages`, and reads history with `GET /inboxes/{id}/threads` so a conversation can be put back into context. Attachments can be read and written, and semantic search runs across an agent's mail. Custom domains are supported, and one agent can hold several inboxes at once.

The use cases in the dossier show why the inbox, not the message, is the primitive. An agent can create a throwaway address to catch a sign-up code and then discard it, or keep one long-lived address for scheduling back-and-forth with participants. Escalation to a person is not built in; the dossier suggests composing an approval tool on top when an email needs review before a reply.

### Other mail in the category

The [Communication](/categories/communication/) category holds several email entries, and the guide on [how to choose an email API for agents](/guides/choose-an-email-api-for-agents/) compares them. [ATXP Email](/services/atxp-email/) and [Agents Mail](/services/agents-mail/) use nearly the same tagline as AgentMail's "Email for AI agents.", so the slogans will not separate them; their dossiers will. [MailboxKit](/services/mailboxkit/) describes itself as email infrastructure for agents. [MCP Agent Mail (Rust)](/services/mcp-agent-mail-rust/) is pitched as Gmail for coding agents, which is mail among agents on a project rather than mail to the outside internet. [Chimely](/services/chimely/) is an in-app notification inbox, not email at all.

### Editor's take

AgentMail is the plain choice when an agent needs a real address it can create, read, and reply from through an HTTP API and webhooks, with an SDK in Python or TypeScript. If the mail only ever travels between coding agents in one repository, or the job is an in-app inbox, a neighbor fits better. These notes come from the catalog's dossier and AgentMail's public reference; no inbox was opened for this page.

</section>

## What it does

AgentMail is an email inbox API built for AI agents to **own** email identities. Rather than proxying through a human's Gmail or Outlook account, agents create dedicated inboxes via API, receive emails via webhook, participate in threaded conversations, and send replies — all without any human mail client in the loop.

The core abstraction is: **the agent is the first-class internet entity at the email address**. AgentMail makes that concrete.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, webhook, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No official skill published by AgentMail yet.
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Full CRUD on inboxes, messages, threads |
| Python SDK | `pip install agentmail` |
| TypeScript SDK | `npm install agentmail` |
| MCP Server | Model Context Protocol integration for direct LLM tool use |
| Webhooks | Push notification on inbound email events |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
