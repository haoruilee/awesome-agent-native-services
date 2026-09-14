# Commerce & Payment Services

> Services that give AI agents a **verified financial identity** and the ability to transact in the real economy — paying for services, moving money, and being recognized as a legitimate, accountable economic actor.

## Why This Category Exists

Human payment infrastructure (Stripe, PayPal, ACH, credit cards) was designed with a human at the initiation point: a person logging in, selecting a payment method, and confirming a transaction. AI agents acting as economic actors — paying for APIs, executing transfers on behalf of users, purchasing resources at runtime — need fundamentally different primitives:

- **Agent wallet** — a financial account owned by the agent (or by the operator on the agent's behalf), not routed through a human's card
- **Know Your Agent (KYA)** — verifiable agent identity that service providers can trust, analogous to KYC for humans
- **Programmable spend controls** — operator-defined budgets and policies enforced at the payment layer, not just in application code
- **Autonomous transaction execution** — payments that complete without a human confirming each one
- **Audit trail per agent** — every payment attributed to the specific agent that initiated it

No legacy payment processor was designed with these requirements. The services in this category are.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Circle Agent Stack](circle-agent-stack.md) | Financial infrastructure for the agentic economy | Agent wallets, marketplace, CLI, x402 gateway, agent skills | ⚠️ |
| [OpenLibx402](openlibx402.md) [![⭐](https://img.shields.io/github/stars/openlibx402/openlibx402?style=social)](https://github.com/openlibx402/openlibx402) | AI-native x402 integrations for autonomous payments | Python/Node SDK, FastAPI/Express middleware, HTTP 402 flow | ⚠️ |
| [CyMetica AI (EventTrader)](cymetica-ai.md) | Agentically engineered financial platform with autonomous AI trading agents | A2A envelopes, MCP descriptor, prediction markets, market-making loops | ✅ |
| [Payman AI](payman-ai.md) | Agentic AI that does the banking. Under your control. | REST API, SDK, Multi-channel | ❌ |
| [Skyfire](skyfire.md) | Identity and payments for autonomous AI agents | REST API, OAuth2/OIDC, KYAPay Protocol | ❌ |
| [AgentsPay](agentspay.md) | Crypto identity and embedded wallets for AI agents | REST API, MCP-native API Gateway | ✅ |
| [Nevermined](nevermined.md) | The payment layer AI agents actually need | HTTP x402 Protocol, REST API | ❌ |
| [Coinbase CDP (x402)](coinbase-x402.md) [![⭐](https://img.shields.io/github/stars/coinbase/x402?style=social)](https://github.com/coinbase/x402) | HTTP-native x402 payments — facilitator, SDKs, Bazaar discovery | HTTP x402, TypeScript/Python/Go SDKs, CDP REST | ❌ |
| [SecondSign Core](secondsign-core.md) [![⭐](https://img.shields.io/github/stars/Bestpart-Irene/secondsign-core?style=social)](https://github.com/Bestpart-Irene/secondsign-core) | Independent transaction co-signer for financial AI agents | Python API, mTLS gateway/approver channels, execute-once rail, hash-chained receipts | ⚠️ |
| [UCP](ucp.md) [![⭐](https://img.shields.io/github/stars/Universal-Commerce-Protocol/ucp?style=social)](https://github.com/Universal-Commerce-Protocol/ucp) | The common language for platforms, agents, and businesses | REST/JSON-RPC, MCP, A2A, `ucp-schema`, checkout capabilities | ⚠️ |
| [AP2](ap2.md) [![⭐](https://img.shields.io/github/stars/google-agentic-commerce/AP2?style=social)](https://github.com/google-agentic-commerce/AP2) | An open protocol for the emerging Agent Economy | VDC mandates, Python/Go/Android samples, A2A/UCP extension | ⚠️ |
| [MPP](mpp.md) [![⭐](https://img.shields.io/github/stars/wevm/mppx?style=social)](https://github.com/wevm/mppx) | MPP lets agents pay for services on the web, extensible to any payment method | HTTP 402 Challenge/Credential/Receipt, mppx SDK/CLI, MCP transport | ⚠️ |
| [AffixIO](affixio.md) [![⭐](https://img.shields.io/github/stars/AffixIO/SDK?style=social)](https://github.com/AffixIO/SDK) | Agentic Pay Kit with x402BeforePay host-side attestation and KYA | npm SDK, x402BeforePay, agenticPay, mcpToolGate, KYA createAgentTrust | ⚠️ |


---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide an **agent-owned or agent-controlled financial account** (not routing through a human's card or bank account).
2. Support **autonomous transaction execution** without per-transaction human confirmation.
3. Implement **operator-defined spend controls** as a first-class primitive.
4. Maintain a **per-agent audit trail** of all transactions.
5. Address **agent identity** in the payment context (KYA, DID, verified credentials, or equivalent).
