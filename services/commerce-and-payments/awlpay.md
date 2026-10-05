# AwLPay

> **"The 5-minute stablecoin wallet for AI agents."**

| | |
|---|---|
| **Website** | https://www.npmjs.com/package/awlpay |
| **Docs** | https://pypi.org/project/awlpay/ |
| **GitHub** | https://github.com/ceedot-rock/awlpay (private) |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Funding / Compliance** | Slid Phi Labs. Fee tiers: Free 1.0% + $0.25 per transaction; Pro $39/mo (0% fee under $30k volume or 500 txs/mo); L33t $799/mo unlimited |
| **Verified at** | 2026-10-05 |

---

## Official Website

No standalone homepage. The canonical public home is the npm package page: https://www.npmjs.com/package/awlpay

---

## Official Repo

No public repository — https://github.com/ceedot-rock/awlpay is private. The public artifacts are the published SDKs: [`awlpay` on npm](https://www.npmjs.com/package/awlpay) (0.1.1) and [`awlpay` on PyPI](https://pypi.org/project/awlpay/) (0.1.0), both shipped 2026-10-03.

---

## How to Use (Agent Onboarding)

**SDK.** Install and follow the 5-minute QUICKSTART.md shipped in the package. Testnet is the default, so an agent can practice the whole flow before touching real money.

```bash
npm install awlpay
# or
pip install awlpay
```

The first script: create an `AgentWallet` (encrypted local keys), set a spend cap, then send. Onboarding instructions live in the package README and the QUICKSTART file — no account signup, no dashboard.

---

## Agent Skills

**Status:** ⚠️ Not yet published by the vendor.

```bash
npx clawhub@latest search awlpay
```

See the [AgentSkills specification](https://agentskills.io/specification) to contribute one.

---

## MCP

**Status:** ⚠️ No first-party MCP server is documented. The verified agent surface is the npm/PyPI SDK.

---

## What It Does

AwLPay gives an AI agent its own wallet and the ability to pay on its own. The agent holds encrypted local keys, moves USDC on Base and Solana, and operates under spend caps an operator sets once. There is no human card in the loop and no per-transaction approval screen — the cap is the control, set at wallet creation.

The design is "anything to anything, if it has value": a converter layer quotes cross-chain paths and refuses when the path doesn't exist or the fees eat the payment. Rails are proven with real money — the Base USDC rail passed a live-money escrow/payout/refund cycle reconciled to the cent, and the Bitcoin rail was funded and live-fired with a real 2,000-satoshi broadcast.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "The 5-minute stablecoin wallet for AI agents." — [pypi.org/project/awlpay](https://pypi.org/project/awlpay/). "AwLPay JavaScript/TypeScript SDK — agent wallets for multi-rail x402 stablecoin payments (Base + Solana). 5 minutes, zero crypto background." — [npm](https://www.npmjs.com/package/awlpay) |
| **Agent-specific primitive** | `AgentWallet`: an encrypted local wallet the agent itself owns and controls, with spend caps set at creation and enforced by the SDK. A human with a card needs no delegated spend cap; this exists because the spender is software acting on someone else's money |
| **Autonomy-compatible control plane** | Inside its cap the agent pays with no human in the loop. Testnet is the default so the full loop — wallet creation, capping, sending — runs safely before any real funds move |
| **M2M integration surface** | Published SDKs on npm (`awlpay` 0.1.1) and PyPI (`awlpay` 0.1.0). No dashboard is required for any part of the agent's operational flow |
| **Identity / delegation** | The wallet is per-agent; spend caps bind to the agent's identity, and every spend is attributable to the specific agent that initiated it. The operator sets caps and funds the wallet; the agent cannot exceed them |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **AgentWallet** | Per-agent encrypted local wallet; the agent signs its own transactions without a human-held card |
| **Spend caps** | Operator-defined limits enforced by the SDK at wallet creation — the autonomy control that replaces per-transaction approval |
| **Converter** | Anything-to-anything conversion: quotes a path when the token has verifiable value, the path exists, and it survives fees; refuses otherwise |
| **Fee tiers** | Free 1.0% + $0.25 per transaction; Pro $39/mo (0% fee under $30k volume or 500 txs/mo); L33t $799/mo unlimited |
| **Rails** | USDC on Base and Solana; BTC rail funded and live-fired with a real 2,000-sat broadcast; XRP first in the rail order |

---

## Autonomy Model

1. The operator installs the SDK and funds the wallet once, setting a spend cap.
2. The agent creates its `AgentWallet` with encrypted local keys, in testnet by default.
3. Onboarding takes five minutes per the QUICKSTART.md shipped in the package.
4. To pay, the agent calls the SDK with amount and destination; the cap check runs locally before anything is signed.
5. Above the cap or with no path, the payment refuses cleanly rather than failing halfway.
6. Every spend is attributable to the agent that initiated it.

---

## Identity and Delegation Model

- The wallet belongs to the agent, not to the human: keys are encrypted and local, held by the agent's own runtime.
- Spend caps are the delegation contract — set by the operator at wallet creation, enforced by the SDK, unchangeable by the agent.
- Sub-dollar sends accrue as ledger credit rather than failing on-chain dust limits.
- Testnet by default gives the agent a sandbox where it can practice real flows with no real money at stake.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| npm SDK | `awlpay` 0.1.1 — [npmjs.com/package/awlpay](https://www.npmjs.com/package/awlpay) |
| PyPI SDK | `awlpay` 0.1.0 — [pypi.org/project/awlpay](https://pypi.org/project/awlpay/) |
| Rails | USDC on Base and Solana; BTC rail funded and live-fired with a real 2,000-sat broadcast |
| MCP | ⚠️ None documented |

---

## Human-in-the-Loop Support

The human is the funder and the cap-setter, not a per-transaction approver. Funding happens once; caps constrain everything after. The default testnet removes the need for approval during development entirely. No approval queue exists by design — the cap is the policy.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Stripe / card processors with agent toolkits** | Human-facing rails with an agent interface added later — `agent-adapted` by this repository's own classification. They authorize a human's card, not a delegated wallet the agent owns |
| **Human crypto wallets (browser extensions, exchange accounts)** | Designed for a person to click; no per-agent identity, no SDK-first spend caps, no testnet-first onboarding for software |
| **x402 facilitators alone** | A payment verification protocol, not a wallet: no agent-owned funds, no caps, no converter. AwLPay can settle through x402-style flows but owns the wallet side |

---

## Use Cases

- **Paying for APIs at runtime** — an agent pays per call in USDC from its own capped wallet, with no human clicking approve each time
- **Agent-to-agent payments** — one agent pays another for work or data, both sides machine-native
- **Cross-chain settlement** — the converter moves value across chains when the path survives fees, and refuses honestly when it doesn't
- **Budgeted autonomous buying** — an operator funds a wallet with a cap and lets the agent spend within it for days at a time
