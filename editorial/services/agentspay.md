Midway through a research task, an agent hits a data API that wants payment or a key it does not have. In most setups the run stops there and waits for a human with a credit card. AgentsPay aims to remove that stop. The site describes it as "Crypto identity and embedded wallets for AI agents," and the dossier explains the pieces: a decentralized identifier for each agent, a stablecoin wallet with an operator-set ceiling, and a gateway that tells the agent what a service costs.

### Paying without a human card

The flow in the dossier runs like this. An operator creates the agent's identity and funds its USDC wallet with a spending ceiling. When the agent meets a service that requires payment, it queries the MCP-native gateway to discover the terms, pays from the wallet within the ceiling, and gets access. The transaction is recorded on-chain against the agent's identifier.

The dossier names three surfaces. The gateway is described as built around the Model Context Protocol over HTTP, with the x402 payment protocol named alongside. A REST API handles wallet management and identity operations. The Base L2 chain holds identity and transaction records. Onboarding is to provision a wallet at the [AgentsPay site](https://agentspay.dev) and then use the gateway. No Agent Skill has been published, and the dossier suggests watching the platform repository for one.

### Identity and spend on one chain

The identity is a W3C DID on Base, which the dossier presents as portable and not tied to one provider. Delegation is the ceiling: the operator sets the maximum, and the agent acts freely below it. Audit is the chain itself, which is tamper-evident but also public, a property worth thinking about if payment patterns reveal what your agent is working on.

The record leaves several practical questions to the vendor. How is the wallet's key held, and by whom? Is the ceiling per transaction, per period, or lifetime? Can it be changed or frozen quickly if an agent misbehaves? Which services accept payment through the gateway today? How do refunds work on a chain that does not reverse? Read the site and repository for current answers, and check any fees there rather than assuming.

### Editor's take

The [commerce and payments collection](/categories/commerce-and-payments/) and the [payments guide](/guides/payments-for-autonomous-agents/) cover several approaches to the same stall. [Skyfire](/services/skyfire/) also pairs identity with payments, using verified Know Your Agent identities and its own protocol instead of an on-chain DID. [Circle Agent Stack](/services/circle-agent-stack/) offers wallets, paid-service discovery, and programmable payments with guardrails. [OpenLibx402](/services/openlibx402/) is a library for building x402 integrations yourself, and [402xAgent](/services/402xagent/) is a check an agent runs before paying an x402 endpoint, which could sit in front of a wallet like this one. [Nevermined](/services/nevermined/) is another payment layer pitched at agents.

AgentsPay is a reasonable candidate for an operator who wants agent identity, wallet, and spend limit in one package on Base and is comfortable with on-chain records. If you would rather assemble x402 yourself, start with OpenLibx402. If you want agent identity established through a Know Your Agent check instead of a DID, Skyfire is the comparison, and Circle covers similar wallet and discovery ground. The analysis here relies on the dossier, the vendor site, and the repository; nothing was funded, signed, or spent while writing it.
