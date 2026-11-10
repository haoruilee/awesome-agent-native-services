[Skyfire](/services/skyfire/) pairs identity with payments for agents. Nevermined's listing is narrower and sits lower in the stack: an x402 Facilitator that puts payment inside the HTTP exchange itself, so an agent pays for an API call as part of making it.

### Payment inside the request

The dossier walks through the loop. An agent requests a resource. The server answers with HTTP 402 Payment Required and payment terms. The Facilitator pays from the agent's account, the request is retried with cryptographic payment proof attached, and the server delivers the response. There is no checkout page, no redirect, and no human approving each charge.

Around that protocol the dossier lists several billing shapes: prepaid credits that fund an agent's account in advance, usage-based billing per call, token, or request, outcome-based billing that charges on task completion, and dynamic pricing that varies with demand or resource cost. Payment methods named are fiat, crypto, stablecoins including USDC, and prepaid credits. Per-agent accounts carry operator-defined budgets, and transaction history is attributable to each agent.

### SDK and protocol, no MCP

The quickest documented path is the Python SDK, `pip install payments-py`, with source in the [payments repository](https://github.com/nevermined-io/payments) and setup notes in the [SDK getting-started docs](https://docs.nevermined.app/docs/libraries/getting-started/). A REST API covers account management, budget configuration, and transaction history. The catalog has no separate docs URL for Nevermined, so the [Nevermined website](https://nevermined.ai/) is the other starting point.

No standalone MCP server is published, and no Agent Skill. The dossier argues that any MCP-based agent making HTTP calls can benefit from x402 handling transparently. Read that carefully: the 402 response only gets paid if something in the agent's HTTP path understands it.

### What transparent has to mean

In [Commerce & Payments](/categories/commerce-and-payments/), several neighbors work on the same protocol. [OpenLibx402](/services/openlibx402/) is an open-source library for x402 integrations, a lighter dependency if you want the protocol without an account platform. [402xAgent](/services/402xagent/) is the check an agent calls before paying an x402 endpoint, which addresses a risk Nevermined's dossier does not discuss: paying a server you should not trust. [Circle Agent Stack](/services/circle-agent-stack/) describes broader financial infrastructure. The [payments guide](/guides/payments-for-autonomous-agents/) compares these approaches.

Before wiring money into an agent loop, confirm in the vendor's materials which side of the exchange each component runs on, buyer or seller, and what the agent's HTTP client must include to answer a 402. Find out how budgets are enforced when a limit is hit mid-task, how fiat and stablecoin settlement differ, and who decides that an outcome succeeded under outcome-based billing. The dossier does not say. Fees and settlement timing belong to the vendor's current pages.

### Editor's take

Nevermined serves two groups: API and tool sellers who want to charge agents per call inside HTTP, and Python agent builders who want operator budgets around those payments. Teams that only need the protocol should start with OpenLibx402; teams worried about where their agent sends money should add 402xAgent regardless. This is an editor's reading of the dossier, the payments repository, and the SDK docs, and no payment has moved through Nevermined on this project's behalf.
