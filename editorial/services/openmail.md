[MailboxKit](/services/mailboxkit/), per its dossier, delivers inbound mail to agents through webhooks. OpenMail adds a WebSocket option, so an agent without a public endpoint can still be pushed new mail, and it parses attachments into text before the agent sees them.

### Push delivery and parsed attachments

The dossier describes one inbox per agent, with a real address on a hosted or custom domain, and two-way threading that behaves normally in ordinary mail clients. Inbound messages arrive as events over a webhook or a WebSocket, which the dossier stresses means no polling. Attachments, including PDFs, CSVs, images, spreadsheets, and word-processor files, are extracted into what the vendor calls LLM-ready text.

The tagline, "Built for agents, not marketers," is a deliberate contrast with newsletter-oriented email APIs. The dossier's use cases follow from that: support agents threading customer mail, browser agents receiving signup and one-time-code messages, and document intake where invoices arrive already parsed.

### Setup writes a skill file

The documented path starts with the CLI: `npm install -g @openmail/cli`, then `openmail setup`. Per the dossier, setup provisions an inbox and writes a local skill file that includes credentials. After that, the agent uses the REST API with a Bearer key beginning `om_`, and subscribes to inbound mail through webhooks or a WebSocket. The [OpenMail docs](https://docs.openmail.sh) have a quickstart, an API reference, and separate pages for both delivery methods.

There is no first-party MCP server and no published skill package beyond the locally generated file. Multi-tenant setups route by `inbox_id`, and many inboxes can sit under one account. Account creation and billing may need a human in the console; the send and receive loop does not.

One detail deserves attention. The docs warn against embedding API keys in prompts, yet the setup command writes a skill file containing credentials. If your agent loads skill files into its context, find out where that file lives and whether the key ends up in the model's input.

### Where it sits among mail services

The [Communication](/categories/communication/) category includes [ATXP Email](/services/atxp-email/) and [Agents Mail](/services/agents-mail/), which also give agents addresses. [Chimely](/services/chimely/) is an in-app notification inbox rather than email. [MCP Agent Mail (Rust)](/services/mcp-agent-mail-rust/) coordinates coding agents and does not touch SMTP. The [email API guide](/guides/choose-an-email-api-for-agents/) compares the address-based options.

Before depending on OpenMail, check which attachment types fail to parse and whether the original file is kept alongside the text. Check how webhook requests are signed, what custom-domain authentication setup involves, and how keys can be scoped below the account level.

### Editor's take

OpenMail is the more natural pick for agents whose mail carries documents, and for setups that cannot host a webhook receiver. Agents running in a browser automation stack that need to catch verification codes fit too. If attachments are rare and you want a smaller surface with automated domain authentication spelled out in the dossier, MailboxKit is worth comparing. This write-up relies on the dossier and OpenMail's public docs; the CLI was never run for it.
