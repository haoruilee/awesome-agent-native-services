To use paid tools through ATXP, an agent needs an MCP client or a shell that can run the CLI or SDK, and a wallet with a budget set by its operator. The dossier lists CLI, SDK, and MCP-compatible service endpoints, all pointing at [docs.atxp.ai](https://docs.atxp.ai). No Agent Skill package was found.

### Wallet first, tools second

The tagline promises a lot: "Give your AI agent a wallet, email, phone number, and instant access to paid MCP tools." The dossier covers a narrower slice. It describes a runtime and payment layer through which agents discover and call paid MCP tools using agent wallets. The primitives are the agent wallet, paid MCP tool invocation, and per-call pricing and authorization.

Settlement happens in-band. The agent makes a tool call, the payment clears, and no human checkout appears in the loop. Identity is wallet-backed, and constraints come from operator budgets. Budget and policy guardrails are optional.

Email and phone are in the tagline but not in this dossier. Email has a separate catalog listing, ATXP Email, in the Communication category. Phone numbers are not documented in this entry, so check the vendor docs if that is the feature you came for.

### A runtime neighbor that is mostly about money

[Agent Runtime & Infrastructure](/categories/agent-runtime-and-infrastructure/) is broad. [Letta](/services/letta/) and the [Cloudflare Agents SDK](/services/cloudflare-agents-sdk/) are places agents live and keep state. [Modal](/services/modal/) is compute. [Cyberdesk](/services/cyberdesk/) provides virtual desktops. [APort Agent Guardrails](/services/aport-agent-guardrails/) authorizes actions before they run. ATXP sits among them as the layer that lets an agent spend money on tools, and it would fit just as well in a payments list.

The relevant comparison is with pre-action authorization. ATXP's guardrails are budgets. APort describes deterministic checks before an action. A team worried about what an agent buys, and not only how much it spends, may want both. The [agent-native guide](/guides/what-makes-a-service-agent-native/) explains why bundled wallet identity and tool payment count as agent primitives.

### Unanswered by the dossier

Find out which payment rails the wallet uses and who holds its keys. Check how a tool sets its per-call price and how an agent sees that price before calling. Ask what happens when a budget runs out in the middle of a task. Confirm which MCP tools are in the paid catalog today; the dossier names kinds of tool, such as paid search and premium data, not providers.

### Editor's take

ATXP makes sense for an operator who wants an agent to pay for metered MCP tools on its own, under a spending ceiling, without integrating each tool's billing separately. If the need is general agent payments outside MCP, a dedicated payments service is the better starting point. If the worry is authorization, APort is the closer fit. Everything above is taken from the dossier and ATXP's docs; the project has not funded a wallet or made a paid call.
