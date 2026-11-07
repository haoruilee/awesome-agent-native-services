# usdc-paywall

> **"Crypto-native paywall for Node. Verify that a USDC payment hit your wallet on Base or Polygon — by tx hash — and unlock content. No Stripe, no accounts, no KYC. You run the wallet."**

| | |
|---|---|
| **Website** | https://www.npmjs.com/package/@josealbertomaquina/usdc-paywall |
| **Docs** | https://github.com/essentoclothes-sudo/usdc-paywall#readme |
| **GitHub** | https://github.com/essentoclothes-sudo/usdc-paywall |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Funding / Compliance** | Core MIT, free; optional Pro tier ($19 USDC one-time). Disclosure: the submitter of this PR/issue is the project maintainer and receives those payments. |

---

## Official Website

https://www.npmjs.com/package/@josealbertomaquina/usdc-paywall

---

## Official Repo

https://github.com/essentoclothes-sudo/usdc-paywall

---

## How to Use (Agent Onboarding)

**The quickest path for an agent to start using this service.**

Pattern: **SDK / REST** (Node library + structured CLI, zero dependencies).

```
# SDK / REST:
npm i @josealbertomaquina/usdc-paywall   # then, on the provider side:
const { verifyPayment } = require('@josealbertomaquina/usdc-paywall')
const r = await verifyPayment({ txHash: '0x…', wallet: '0x…', amount: 3, chain: 'base' })
if (r.ok) res.send(paidContent) else res.status(402).send(r)
```

```
# Structured CLI (exit 0 = paid, non-zero + JSON on stderr = reason):
npx @josealbertomaquina/usdc-paywall --tx 0x… --to 0x… --amount 3 --chain base
```

---

## Agent Skills

**Status:** ⚠️ Not yet published. A `usdc-payments` skill is in preparation for ClawHub; until then, the README above is the full agent-facing protocol.

---

## MCP

**Status:** ⚠️ Not yet published. Integration surface today is the Node SDK and the exit-code CLI (both usable from MCP server wrappers without modification).

---

## What It Does

Host-side paywall for API and content providers: it checks the ERC-20 `Transfer` log of the official USDC contract on Base or Polygon against the provider's own wallet address, by transaction hash, with BigInt decimal math and a confirmation-depth guard. A paying caller — human or autonomous — sends USDC directly wallet-to-wallet and submits the tx hash; the provider's server verifies settlement on-chain and unlocks the endpoint or content. There is no merchant account, no KYC, and no shared secret. A Pro tier adds live payment watching (`eth_getLogs`) and offline Ed25519 license verification.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: "Use it for: paid APIs, license keys, agent-to-agent services (x402-style flows)" — https://github.com/essentoclothes-sudo/usdc-paywall#readme |
| **Agent-specific primitive** | Tx-hash payment proof: a machine-verifiable receipt (ERC-20 Transfer log) that replaces OAuth flows, accounts, and hosted checkout; HTTP 402 as the machine-actionable refusal code |
| **Autonomy-compatible control plane** | Stateless verification — `verifyPayment({txHash, wallet, amount, chain})`; no accounts, API keys, cookies, or rate-limit identities; runs against public RPC endpoints |
| **M2M integration surface** | npm SDK (CJS/ESM, zero deps), structured CLI with exit codes, JSON diagnostics; designed to be embedded behind a 402-returning endpoint |
| **Identity / delegation** | Caller identity is the caller's own wallet (self-custodied); provider identity is the on-chain receiving address; no delegation tokens to leak |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| `verifyPayment(txHash, wallet, amount, chain)` | Confirms an ERC-20 USDC Transfer of ≥ amount, to the provider wallet, on the official USDC contract, past a confirmation-depth guard. Returns `{ok, amount, confirmed, reason}`. |
| 402 refusal convention | Unpaid callers receive HTTP 402 with a JSON body naming chain, wallet, and amount — everything an agent needs to complete payment and retry autonomously |
| `pro watch` | Live `eth_getLogs` subscription over the receiving wallet for incoming USDC transfers (Pro tier) |

---

## Autonomy Model

1. Caller requests a protected resource; provider answers **HTTP 402** with `{chain, wallet, amount}` — machine-readable, no HTML to parse.
2. Caller pays from its own wallet (USDC on Base or Polygon) with no human consent screen.
3. Caller retries the request including the tx hash.
4. Provider verifies the on-chain Transfer log via public RPC (stateless, no session state to manage).
5. Content/endpoint unlocks for that tx hash; the tx itself is the durable receipt.

No step requires a human, a browser, an email, or an account.

---

## Identity and Delegation Model

- Agent identity = self-custodied wallet address; no issued credentials exist to leak or rotate.
- Provider identity = published receiving address; verifiable independently on-chain.
- Audit trail = the payment transactions themselves (public ledger) plus provider logs; tx hash is the unique proof-of-payment handle.
- Pro licenses are Ed25519-signed offline keys — verifiable without network access, no license server.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Node SDK | `require('@josealbertomaquina/usdc-paywall')` — CJS + ESM, zero runtime dependencies |
| CLI | `usdc-paywall --tx … --to … --amount … --chain base|polygon`; exit 0 = paid, JSON reason on stderr otherwise |
| HTTP convention | Designed for `402 Payment Required` + JSON `{chain, wallet, amount}` responses |
| Chains | Base, Polygon (official USDC contract addresses pinned in code) |

---

## Human-in-the-Loop Support

None required — that is the design goal. Humans can pay through the identical flow from any wallet; refunds/chargebacks are manual provider-side wallet operations (there is no custodial reversibility, which is what removes the KYC/account requirement).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Stripe / PayPal** | Merchant accounts, KYC, hosted human checkout and consent screens; an autonomous caller cannot hold or exercise the required credentials |
| **Raw RPC / ethers.js read** | Not a service primitive: no packaging, no 402 semantics, no decimal/confirmation guards, no CLI/SDK contract for agents |

---

## Use Cases

- **Per-call paid APIs** — 402 on unpaid, unlock on verified tx hash.
- **Agent-to-agent services** — x402-style flows where both sides are autonomous and self-custodied.
- **Content / artifact gates** — one-time USDC unlock for datasets, reports, downloads.
- **Offline license gates** — Ed25519 license verification with no license server (Pro).
