[OpenMail](/services/openmail/) delivers inbound mail over webhooks or a WebSocket and parses attachments into text for the model. MailboxKit keeps to a smaller surface: a REST API, inbound webhooks, and a hosted skill file, with its extra effort spent on threading headers and custom-domain authentication.

### One address per agent

The dossier's primitive is a real email address for each agent, provisioned through the API. Addresses live either on the shared `agent.mailboxkit.com` domain or on a domain you bring. An agent can send, receive, and reply. Replies are threaded automatically through the standard `References` and `In-Reply-To` headers, which is the detail that makes a conversation display correctly in a human's mail client instead of arriving as a string of unrelated messages.

Custom domains come with automated DKIM, SPF, and DMARC setup, so deliverability work that usually means editing DNS records by hand is handled during onboarding. Optional open and click tracking is available. For an agent writing to a person, consider whether you want tracking pixels in those messages at all.

### Skill file, REST, webhooks

URL onboarding is the documented first step. The one-line instruction is to read `https://mailboxkit.com/skill.md` and follow it; the dossier says that file covers self-registration, sending, receiving, and replying. After that, the agent works against REST API v1 with a Bearer API key, as described in the [MailboxKit API docs](https://mailboxkit.com/api-docs). Inbound mail arrives as webhook events posted to an HTTPS endpoint the agent controls.

No first-party MCP server is published. An MCP client needs its own wrapper around the REST calls, and something has to host the webhook receiver.

On the human side, account registration and payment top-up may go through a dashboard. Once a key exists, mail operations are programmatic. Pricing is usage-based per the dossier; current rates are on the vendor's site.

### Email neighbors and non-email ones

The [Communication](/categories/communication/) category mixes two kinds of service. [ATXP Email](/services/atxp-email/) and [Agents Mail](/services/agents-mail/) share MailboxKit's job of giving agents addresses on the public mail network. [MCP Agent Mail](/services/mcp-agent-mail/) uses the word mail for something else: coordination messages between coding agents in one project, with no SMTP involved. [Chimely](/services/chimely/) is an in-app notification inbox, not email. The [email API guide](/guides/choose-an-email-api-for-agents/) walks through choosing among the address-based options.

Before relying on MailboxKit, check how webhook payloads are authenticated so a forged request cannot impersonate inbound mail; the dossier does not say. Check how long messages are retained, whether an API key can be limited to one inbox, and how the shared domain's sending reputation is managed compared with a custom domain.

### Editor's take

MailboxKit is a good match for an agent that corresponds with people over ordinary email, where correct threading and authenticated custom domains matter more than attachment parsing, and the team already runs a public HTTPS endpoint. If the agent cannot expose a webhook receiver, or needs attachments turned into text, OpenMail's WebSocket and parsing features are the reason to look there. If the real need is agents coordinating edits in one repository, MCP Agent Mail is the right listing. These notes rest on the dossier and the vendor's public pages; no inbox was provisioned in preparing them.
