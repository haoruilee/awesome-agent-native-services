---
title: "ATXP Email | Agent-Native Services"
service_name: "ATXP Email"
description: "Email for AI agents"
permalink: /services/atxp-email/
page_kind: service
service_slug: "atxp-email"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/atxp-email.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/atxp-email.md"
tagline: "Email for AI agents"
website: "https://atxp.email/"
repository: "https://github.com/atxp-dev"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · API · documentation</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://atxp.email/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.atxp.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/atxp-dev" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/atxp-email.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

The onboarding instruction in the dossier is written for the agent itself: `Read https://atxp.email/ and follow the docs to create an agent inbox via CLI/API.` That presumes an agent able to fetch a page and then run a command-line tool or make API calls. MCP status is unknown in the catalog, and the dossier says email is not clearly documented as a standalone MCP server. No Agent Skill package was found.

### An inbox the agent owns

The tagline is "Email for AI agents." The service gives an agent its own inbox identity so it can receive verification codes, notifications, and messages from people without borrowing a human's mailbox. The primitives are inbox creation, inbox and message listing, and reading messages with code extraction.

Code extraction is the detail with the clearest payoff. Many signup flows email a one-time code, and an agent without its own address stalls there. The dossier lists signup and verification for tool accounts as the first use case, then notification handling and asynchronous email with people.

Identity is issued directly to the agent runtime, and the inbox becomes its endpoint on the internet. Human involvement is optional for receiving and reading. The dossier says nothing about sending limits, retention, custom domains, or how the CLI authenticates. The [ATXP docs](https://docs.atxp.ai) are the cited reference, and the [product page](https://atxp.email/) is the onboarding URL.

### Among agent mailboxes

[Communication](/categories/communication/) has several agent email services. [MailboxKit](/services/mailboxkit/) and [Agents Mail](/services/agents-mail/) share the email-for-agents framing. [OpenMail](/services/openmail/) pitches itself against marketing tools. [MCP Agent Mail](/services/mcp-agent-mail/) and its [Rust counterpart](/services/mcp-agent-mail-rust/) are different in kind: coordination between coding agents, with identities, threads, and file leases over MCP rather than internet email.

ATXP Email's dossier is focused on receiving: create, list, read, extract. If your agent mainly needs to send outbound mail or run threaded conversations with customers, compare the sending features of the other listings. The [email API guide](/guides/choose-an-email-api-for-agents/) lays out how to weigh inbound identity against outbound delivery.

### What to verify first

Confirm who owns an inbox if the agent is retired, and whether a person can recover mail sent to it. Check whether the CLI credential is shared with other ATXP products, since a leaked key would then reach more than mail. Find out how long inbound messages are retained and how long codes remain readable. Look for a documented way to delete an inbox when a task ends.

### Editor's take

An agent that keeps hitting email verification walls during signups is the clearest customer here. Teams that need outbound campaigns or human-facing support threads should read MailboxKit or OpenMail first, and coding-agent fleets that want to message each other belong with MCP Agent Mail. Only the dossier and ATXP's published pages informed this view; we have not provisioned an inbox.

</section>

## What it does

ATXP Email gives AI agents their own inbox identity so agents can receive verification codes, notifications, and human messages without relying on a human mailbox.

## Agent-facing interfaces

- **Catalog protocols:** CLI, API, documentation
- **MCP:** ⚠️ Not clearly documented as a standalone MCP server for email only.
- **Agent Skill:** ⚠️ No official AgentSkills package found.
- **Onboarding type:** `documentation`

## Protocol surface

- CLI
- Web/API docs

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
