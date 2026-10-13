# Lumen Tab

> **"Prepaid USDC tabs for pay-per-call AI agent APIs on Arc."**

| | |
|---|---|
| **Website** | https://dansgit2b.github.io/lumen-tab/ |
| **Docs** | https://github.com/Dansgit2b/lumen-tab#readme |
| **GitHub** | https://github.com/Dansgit2b/lumen-tab |
| **Stars** | [0 stars (snapshot: 2026-10-11)](https://github.com/Dansgit2b/lumen-tab) |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **License** | MIT |
| **Custody** | Non-custodial escrow contract on Arc mainnet (chain id 5042). The provider can only redeem up to the latest voucher the payer signed; the payer can always recover the unspent deposit after the tab's close delay |
| **Publisher** | Lumen Works. The proposal author disclosed in [issue #193](https://github.com/haoruilee/awesome-agent-native-services/issues/193) that they build Lumen Tab |
| **Verified at** | 2026-10-11 |
| **Latest-month signal** | Repository created 2026-10-09, last push 2026-10-09, SDK version 0.1.0; dashboard returned HTTP 200 on 2026-10-11; contract `0xb4a0364c58B2DF53e25FfF0463B5434160Ed2B50` deployed on Arc mainnet with demo transactions listed in [DEPLOYMENTS.md](https://github.com/Dansgit2b/lumen-tab/blob/main/DEPLOYMENTS.md) |
| **Status** | **Early-stage.** Days old, 0 stars, not audited, no production users yet. SDK not yet published to npm (install from GitHub). No MCP server or `SKILL.md`. Start with small deposits. |

---

## Official Website

https://dansgit2b.github.io/lumen-tab/

---

## Official Repo

https://github.com/Dansgit2b/lumen-tab

---

## How to Use (Agent Onboarding)

Install the JS SDK from GitHub (not yet on npm) and wrap `fetch` so the agent answers HTTP 402 challenges with vouchers:

```bash
npm install github:Dansgit2b/lumen-tab
```

```js
import { TabPayer } from "lumen-tab";
const payer = new TabPayer({ account, tabId, provider });
const res = await payer.fetch(PAID_API_URL); // any Lumen Tab–paywalled endpoint: 402 → voucher → retry
```

Providers add the `lumenTabPaywall` Express middleware and run `Settler` to batch-redeem. The repository's [`examples/agent.mjs`](https://github.com/Dansgit2b/lumen-tab/blob/main/examples/agent.mjs) opens a tab (`openTab`) and pays a reference URL → Markdown API at 0.002 USDC per call.

---

## Agent Skills

**Status:** ⚠️ Not yet published

Search community skills: `npx clawhub@latest search lumen-tab`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not yet published

| Detail | Value |
|---|---|
| **MCP Repo** | None |
| **Transport** | Not applicable (HTTP 402 + `x-lumen-tab` header) |
| **Compatible Clients** | Any HTTP client using the JS SDK `TabPayer` fetch wrapper |

---

## What It Does

Lumen Tab is a unidirectional USDC payment channel for pay-per-call HTTP APIs on Arc. An agent opens one prepaid tab with an API provider, then pays each call with a cumulative EIP-712 voucher sent in an `x-lumen-tab` header in reply to an HTTP 402. A paid call needs no transaction and no gas; the provider batch-settles on-chain whenever it wants.

The deposit is a hard spending cap: the provider can never redeem more than the payer signed for, and the payer can exit on its own after the tab's close delay. A tab can name the provider's ERC-8004 agent id.

The project is early-stage: the contract is about 190 lines on OpenZeppelin v5 with 16 Foundry tests and a mainnet demo (3 tabs, 11 paid calls settled in 3 transactions), but it has not been audited and has no production users yet.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Agents are about to buy a lot of very small things… They want to pay $0.001–$0.01 per call." — [README](https://github.com/Dansgit2b/lumen-tab#why) |
| **Agent-specific primitive** | Per-agent prepaid tab (payment channel) plus cumulative EIP-712 vouchers answering HTTP 402 challenges; no gas or transaction per call |
| **Autonomy-compatible control plane** | The agent opens a tab and pays every call with no human confirmation; the deposit caps spend; the payer can exit unilaterally (`requestClose` → `finalize`) after `closeDelay` |
| **M2M integration surface** | Solidity contract on Arc mainnet; JS SDK on viem (`TabPayer`, `lumenTabPaywall`, `Settler`, `openTab`, `signVoucher`); the dashboard is optional and read-only |
| **Identity / delegation** | Payer (treasury) is separate from signer (hot agent key or ERC-1271 smart account); tabs can name the provider's ERC-8004 agent id; opens, redeems and closes are on-chain events |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Tab** | USDC escrow per payer/provider pair with a deposit cap, signer, close delay and optional provider ERC-8004 agent id |
| **Voucher** | `Voucher(uint256 tabId, uint128 cumulative)` signed under EIP-712 domain `LumenTab / 1 / 5042 / <contract>`; cumulative and monotonic, so replays do nothing |
| **402 challenge** | Provider replies `402 {scheme: lumen-tab-v1, price, contract, provider}`; the agent retries with an `x-lumen-tab` voucher header and receives an `x-lumen-tab-receipt` |
| **Batch redeem** | `Settler` redeems the latest voucher in one transaction covering many calls |
| **Exits** | `closeByProvider` (cooperative), or payer `requestClose` → `finalize` after `closeDelay` |

---

## Autonomy Model

1. The agent approves USDC and calls `open(provider, signer, deposit, closeDelay, agentId)`.
2. It requests the paid endpoint and receives an HTTP 402 with the price.
3. `TabPayer` signs a voucher for the new cumulative amount and retries; the provider verifies it against the cached tab and returns 200 with a receipt.
4. Steps 2–3 repeat for many calls with zero gas. Failed calls are rolled back and not charged.
5. The provider redeems the latest voucher on its own schedule.
6. The tab closes cooperatively, or the payer requests close and finalizes after the delay to recover the unspent balance.

---

## Identity and Delegation Model

- **Payer** funds the tab and receives refunds; **signer** (hot agent key or ERC-1271 smart account) only authorizes spending up to the deposit, giving bounded delegated authority.
- Tabs can reference the provider's **ERC-8004** agent id (the reference provider is agent #2315 in Arc's IdentityRegistry).
- Every open, redeem and close is an on-chain event, giving a per-tab and per-agent audit trail.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **Smart contract** | `LumenTab` at `0xb4a0364c58B2DF53e25FfF0463B5434160Ed2B50`, Arc mainnet (chain id 5042) |
| **JS SDK** | viem-based; `signVoucher`, `TabPayer`, `lumenTabPaywall`, `Settler`, `openTab`; install from GitHub (npm publish planned) |
| **HTTP** | HTTP 402 challenge + `x-lumen-tab` voucher header + `x-lumen-tab-receipt` |
| **Dashboard** | Static, read-only page with live tabs, event feed and voucher verifier |
| **MCP** | None |

---

## Human-in-the-Loop Support

None is required in the payment loop. A human (or treasury) sets the bound once by choosing the deposit, signer and close delay when funding the tab; after that the agent pays without confirmation. The dashboard is read-only observation, not an approval gate.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **One on-chain payment per call (plain x402 "exact")** | Puts a transaction and confirmation on every request |
| **API keys and monthly invoices** | Need human accounts, KYC and credit risk |
| **Custodial prepaid credits** | Refunds depend on the provider's goodwill |

---

## Use Cases

- **Pay-per-call data and tool APIs** — agents pay $0.001–$0.01 per request without a transaction per call
- **Monetizing an agent-facing API** — providers add Express middleware and batch-settle in USDC
- **Bounded agent spend** — a treasury funds a tab and hands a hot key spending authority capped by the deposit
