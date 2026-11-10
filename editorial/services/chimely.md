When a background agent finishes a report, fails a job, or needs someone to approve the next step, the person it works for is usually inside an application, not watching an email client. The natural place to tell them is a notification in that app. Building that from scratch means a notifications table, an API, a real-time channel, and a front-end inbox. Chimely packages those parts. Its own description is "Open-source, self-hostable in-app notification inbox infrastructure that agents can call through an HTTP API."

### Telling the user inside the app

The dossier describes a Rust service backed by Postgres and Redis, with three surfaces. An HTTP API accepts notifications. A Server-Sent-Events hint plane tells connected clients that something new has arrived. A drop-in `<Inbox />` React component renders the inbox in the application. The flow is direct: the agent calls the API, Chimely stores the notification, emits a hint, and the app shows it.

That is the entire agent-facing story, and the dossier says so. Chimely is not a full agent toolkit or a workflow engine. It does not give the agent its own identity; notifications are addressed to end users inside the application, and the agent's authority is whatever API access the application grants it. MCP is not listed. The catalog marks its status as unknown, and the dossier describes the HTTP API as the agent surface. No Agent Skill is published. Any runtime that can make HTTP calls can use it. The [Chimely docs](https://chimely.dev) have the API reference.

The license split matters for some teams: the server is AGPL-3.0 and the SDKs are MIT, per the dossier. Self-hosting is the model, so you run the Rust service, Postgres, and Redis yourself. The dossier positions Chimely as a self-hosted alternative to hosted notification products such as Knock, Courier, MagicBell, and Novu.

### Not an email service

Chimely sits in the [communication collection](/categories/communication/) next to services with a different job. [Agents Mail](/services/agents-mail/), [MailboxKit](/services/mailboxkit/), and [OpenMail](/services/openmail/) give an agent its own email address that can send to and receive from anyone. [MCP Agent Mail](/services/mcp-agent-mail/) is coordination between coding agents. Chimely is one-way from the agent to users of one application, and replies, if any, happen through the app. The [guide to choosing an email API for agents](/guides/choose-an-email-api-for-agents/) is useful mainly to rule email in or out.

Before adopting it, read the docs for how the API authenticates callers, how a notification identifies its recipient, whether read state and deletion are exposed, and how the SSE channel is secured. The record does not cover delivery to email, SMS, or push, and frames that as the point: the agent does not own those channels.

### Editor's take

Choose Chimely if you already run the application your users live in, want agent status and approval prompts to appear there, and are willing to operate the stack under AGPL terms. If the people you need to reach are outside your app, or the agent needs to receive replies, an agent mailbox from Agents Mail or OpenMail is the right category. We formed this view from the dossier and the public docs and repository. None of the stack was deployed or sent a notification for this page.
