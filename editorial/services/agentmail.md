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
