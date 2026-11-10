---
layout: default
title: "How to choose an email API for AI agents"
description: "Agent-owned inboxes, self-hosted mail, notification workflows, and coordination mail for coding agents."
permalink: /guides/choose-an-email-api-for-agents/
page_kind: document
ads: false
guide_order: 2
---

An agent that "sends email" can mean four different systems. It can own an address and correspond. It can wait for a verification code on a mailbox it just created. It can fire a notification workflow a person already configured. Or it can leave a message for another coding agent in the same repository. Those are all in the [communication collection](/categories/communication/). Picking the first hosted API on the list will be wrong for at least three of the four jobs.

The catalog's line is ownership. Human mail systems assume a person at each end. An agent-native inbox can be created, read, and retired by software, and inbound mail arrives as an event the agent can put into its next step. A token for a person's Gmail account fails that line even if an agent is the process using the token. The contribution guide uses that case as a fail example on purpose.

## Start from the job

Write down which of these you actually need before you compare vendors.

**A correspondent.** Something on the internet emails the agent, or the agent emails a person, and the thread continues. You need an address, structured threads, and a push when mail arrives.

**A disposable identity.** The agent signs up for something else and has to catch a one-time code, or it needs a fresh address per task. Provisioning speed and a "wait for this message" primitive matter more than a custom domain.

**A notification.** A person is the reader. The agent decides that a message should go out, and a system the operator already trusts picks the channel, the template, and the preferences. The agent does not need its own public address.

**Coordination inside a build.** Several coding agents edit one repo and need to talk without using the public internet as their bus. Git and a local mailbox are a better fit than SPF records.

If you need more than one, you will probably use more than one service. Caspian's dossier describes a single agent identity normalized across email and chat channels. That solves a different problem again: one handler, many networks, each network still enforcing its own rules.

## Hosted inboxes

[AgentMail](https://agentmail.to) is the reference shape in this catalog. The [docs](https://docs.agentmail.to) and the dossier describe inboxes created through the API, threads as data the agent can read back, inbound webhooks, and an MCP server. The positioning line the contribution guide quotes is "Email for AI agents." Custom domains are part of the identity story: the address can be the agent's, on a domain the operator controls, rather than a forward from a person.

[MailboxKit](https://mailboxkit.com) is the same family. Its dossier describes a real address per agent, inbound webhooks, threading via `References` and `In-Reply-To`, and custom domains with the usual mail authentication records. It is also on the catalog's URL-onboarding list: an agent can be pointed at `https://mailboxkit.com/skill.md`. The dossier describes pay-as-you-go pricing. The number changes. Read the current [API docs](https://mailboxkit.com/api-docs) rather than trusting a figure copied into an essay.

[mails.dev](https://mails.dev) is on that same join list. The dossier's distinguishing primitive is small and practical: `mails code` waits until a verification message arrives and returns the code. That is the disposable-identity job stated as a command, plus ordinary send and receive on a `@mails.dev` mailbox or a domain you attach. [Agents Mail](https://agentsmail.org) is another URL-onboarding inbox, with discovery metadata in its dossier, aimed at agents rather than at a human webmail product. [OpenMail](https://openmail.sh) describes one inbox per agent, threads that still work with normal mail clients, inbound delivery over webhooks or WebSocket, and attachments parsed into text. Its tagline in the catalog is "Built for agents, not marketers," which is the contrast with campaign APIs.

[SendRaven](https://sendraven.ai) belongs in this group and has a sharper boundary. The dossier says a person creates the workspace, verifies a sending domain, and adds a payment method before outbound mail exists. An agent cannot self-register, because DNS control is a person's proof. After that, the agent uses REST or an MCP server, including a remote endpoint, and the docs describe per-key guardrails. If your requirement is "the agent signs itself up with no human," SendRaven is the wrong row. If your requirement is "the agent works a domain we already proved we own," the human step is the feature.

[Atomic Mail](https://atomicmail.ai/) takes the opposite signup path. The dossier says an agent registers `username@atomicmail.ai` over a proof-of-work challenge, so the join does not depend on a CAPTCHA or a human approval, and mail is then JMAP. Custom domains stay on a human dashboard because DNS is still DNS. That split, machine signup on the vendor's domain and human setup on yours, is worth noticing. It shows up more than once in this category.

None of these paragraphs is a performance comparison. Deliverability, rate limits, and attachment size are vendor facts. They move. The docs linked from each dossier are the place to read them.

## Mail you run yourself

Hosted inboxes are a dependency. Self-hosted mail is an operator's job that happens to be shaped for agents.

[AgenticMail](https://github.com/agenticmail/agenticmail) is described as a self-hosted platform: a Stalwart server, inbound webhooks, and a bridge toward SMS via Google Voice, so the agent gets an email identity and a phone path from one project. You are running the mail server. That is the trade for not sending your agent's correspondence through a vendor.

[AgentTeam Email](https://www.agentteam.email) is open source and more opinionated about the human. The dossier describes a mailbox per agent on a domain you control, Cloudflare for send and receive, inbound mail landing in R2, and scoped rights so an agent can read and draft, with review before send. A web client exists for the person. The agent-facing surface includes an `at-email` CLI and an Agent Skill. Choose this when a person must be able to stop an outbound message. Do not choose it when the agent must correspond unattended. Review-before-send is a control plane. It is also a click.

[OutreachAgent](https://outreachagent.dev/) is narrower still. The catalog tagline is a cold-outbound engine for agents. That is a campaign-shaped product pointed at agents, not a general inbox. If you do not need sequences, you do not need it. If you do, read its docs for how consent and sending identity work before you point an agent at it. This guide will not summarize outreach law.

## Notifications are not correspondence

[Novu](https://novu.co) is open-source notification infrastructure with an agent toolkit. The dossier's model is a workflow: the agent calls a tool, and Novu renders the template, picks the channel, and honors preferences. The reader is typically a person who already has an inbox, a phone, or a Slack account. [Chimely](https://chimely.dev) is a self-hosted in-app inbox, HTTP in and a React component out, which agents can call. The dossier compares it with notification products such as Knock and Novu, not with mail hosts.

Use these when the agent is emitting a product event. Do not use them when a stranger must be able to reply to the agent's own address and have that reply become the next model turn. A notification inbox and a correspondent inbox can sit in the same application. They should not be the same row in a design doc just because both contain the word "message."

## Mail between coding agents

[MCP Agent Mail](https://github.com/Dicklesworthstone/mcp_agent_mail) is an asynchronous coordination layer. Agents register identities, exchange structured messages, search threads, and coordinate edits with advisory file reservations. The dossier says the artifacts live in Git and the index in SQLite. The Rust service beside it is a separate listing, a different runtime of a similar idea. Neither is trying to be a public SMTP identity.

This is the right shape when the "recipient" is another agent in the same project and the record of the conversation should live with the code. It is the wrong shape when a vendor, a customer, or a login form needs to reach the agent at a domain. People mix them up because both use the word inbox. The protocol surface is MCP tools, not an MX record.

## A way to decide

Walk the questions in order.

Who is the other party? A person or a program on the public internet points you at a hosted or self-hosted SMTP identity. Another coding agent in the repo points you at MCP Agent Mail. A person who already uses your product points you at Novu or Chimely.

Who may create the identity? If the agent must join alone, look for URL onboarding or a documented machine signup, and read what the signup actually provisions. Atomic Mail's proof-of-work path and MailboxKit's skill file are different mechanisms with the same goal. If a person must prove the domain, SendRaven and the custom-domain half of several other products are being honest about DNS.

What happens when mail arrives? A webhook or a socket is the primitive the category notes ask for. Polling a mailbox from a cron loop works until it is late. mails.dev's long-poll for a code is a specialized version of the same idea: the agent blocks on one expected message instead of subscribing to all of them.

What is the agent allowed to send? Unattended send is AgentMail's model and the model of several of its neighbors. Draft and review is AgentTeam Email. Guardrails on a key are SendRaven's dossier. Pick the constraint you want enforced outside the prompt. A sentence in the system prompt that says "do not email the customer" is not a control plane.

Where does the message live? A vendor store is simpler and is their retention policy. A server you run is your retention policy and your deliverability problem. Git is a good log for agent-to-agent notes and a bad log for someone else's personal data.

## What this guide will not pick

It will not name a default vendor. The collection is large because the jobs diverge, not because the index failed to finish a comparison table. Interface details, MCP availability, and onboarding URLs are on each service page and in the dossier. When those drift, the [editorial policy](/editorial-policy/) says to fix the dossier from the vendor's docs, then the essay.

If the next question is how the agent authenticates to a tool that is not email, that is [MCP](/guides/getting-started-with-mcp-servers/). If the next question is how the agent pays for the API it just called, that is [payments](/guides/payments-for-autonomous-agents/). Mail is only the identity. The other loops are other collections.
