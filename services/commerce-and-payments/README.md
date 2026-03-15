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
| [Payman AI](payman-ai.md) | Agentic AI that does the banking. Under your control. | REST API, SDK, Multi-channel | ❌ |
| [Skyfire](skyfire.md) | Identity and payments for autonomous AI agents | REST API, OAuth2/OIDC, KYAPay Protocol | ❌ |
| [AgentsPay](agentspay.md) | Crypto identity and embedded wallets for AI agents | REST API, MCP-native API Gateway | ✅ |
| [Nevermined](nevermined.md) | The payment layer AI agents actually need | HTTP x402 Protocol, REST API | ❌ |

---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide an **agent-owned or agent-controlled financial account** (not routing through a human's card or bank account).
2. Support **autonomous transaction execution** without per-transaction human confirmation.
3. Implement **operator-defined spend controls** as a first-class primitive.
4. Maintain a **per-agent audit trail** of all transactions.
5. Address **agent identity** in the payment context (KYA, DID, verified credentials, or equivalent).
