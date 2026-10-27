# Shinjuku Shield

> **"Privacy-only x402 facilitator for AI agents on Solana."**

| | |
|---|---|
| **Website** | https://shinjukustaition.com |
| **Docs** | https://github.com/ShinjukuStaition/shinjuku-shield · docs under that repo |
| **GitHub** | https://github.com/ShinjukuStaition/shinjuku-shield |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/ShinjukuStaition/shinjuku-shield?style=social)](https://github.com/ShinjukuStaition/shinjuku-shield) |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **License** | Proprietary wallet/binary distribution (`SEE LICENSE IN LICENSE.txt` on npm `shinjuku-shield` / `shinjuku-shielded`); docs/setup repo is public |
| **Verified at** | 2026-10-27 |
| **Latest-month signal** | npm `shinjuku-shield@0.3.86` pinned 2026-10-23; site https://shinjukustaition.com HTTP 200; GitHub push 2026-10-27 |

---

## Official Website

https://shinjukustaition.com

---

## Official Repo

https://github.com/ShinjukuStaition/shinjuku-shield — setup guide, docs, changelog, and SHA-256 hashes for wallet releases. Wallet/source binaries ship via npm (`shinjuku-shield` / older name `shinjuku-shielded`); the public repo does not include server, circuit, or wallet source.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** Local self-custody MCP wallet

```bash
npm install -g shinjuku@0.3.86
shinjuku setup
```

Setup creates the wallet, passphrase file, and proof tools, and prints the MCP add line for the agent host. Pin `0.3.86` (or current pinned release in upstream README).

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills bundle located; primary path is the local MCP wallet via `shinjuku setup`.

---

---

## MCP

**Status:** ✅ Local stdio MCP (agent wallet)

| Detail | Value |
|---|---|
| **Install** | `npm install -g shinjuku@0.3.86` then `shinjuku setup` |
| **Transport** | stdio on the agent machine |
| **Custody** | Keys never leave the machine; Shinjuku does not hold funds |
| **Example tools** | `wallet_add_funds`, `wallet_shield`, `x402_discover`, `x402_preview`, pay flows with `request_id` idempotency |
| **Optional** | `--tor`; operator-set spend caps (tools may lower, not raise) |

---

## What It Does

Shinjuku Shield is a **privacy-only x402 facilitator on Solana**. Agents pay any Solana `exact` USDC x402 seller from a **self-custodied shielded balance**; the chain does not show which wallet paid. Sellers keep standard x402 middleware; Shinjuku pays the seller from float after the private agent payment. This is agent payment infrastructure with privacy and local caps — not a generic metered HTTP API behind x402 alone.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first** | Site and README target AI agents; MCP wallet runs inside the agent host |
| **Agent-specific primitive** | Shielded self-custody balance + x402 pay/discover/preview tools with idempotent `request_id` |
| **Spend controls** | Operator-defined caps; tools cannot raise them |
| **M2M** | Local MCP stdio |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Shielded self-custody balance** | Agent-held notes; chain does not show who paid |
| **x402 pay / preview / discover** | MCP tools for Solana `exact` USDC sellers |
| **Spend caps** | Operator-set limits; tools may lower only |
| **Idempotent `request_id`** | Retries resume; do not double-pay |

---

## Autonomy Model

```
Operator runs shinjuku setup and sets optional spend caps
    ↓
Agent MCP: wallet_add_funds → shield → x402_preview → pay
    ↓
Private settle via Shinjuku facilitator; seller sees standard x402 settle from Shinjuku float
```

---

## Identity and Delegation Model

- **Self-custody:** wallet keys stay on the agent machine.
- **Caps:** only the operator raises limits at setup; MCP calls may only lower them.
- **No API key / sign-up** required for the default relay path (per upstream README).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| npm | `shinjuku-shield@0.3.86` / `shinjuku-shielded@0.3.86` / `shinjuku` CLI |
| MCP | stdio after `shinjuku setup` |
| Network | Solana mainnet, USDC |
| Site | https://shinjukustaition.com |

---

## Human-in-the-Loop Support

Humans run setup and optional caps. Paying, shielding, and discovery run in the agent loop under those caps. Funding the shielded balance may involve a human sending USDC to a one-time address from `wallet_add_funds`.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Public x402 facilitator alone** | Payments are attributable on-chain; no agent self-custody shielded balance |
| **Custodial agent wallet SaaS** | Keys/funds held by a third party; Shinjuku keeps keys local |
| **Generic HTTP API + x402 price** | Not private agent payment infrastructure with local MCP caps |

---

## Use Cases

- Pay Solana x402 sellers without revealing the agent wallet on-chain
- Discover and preview x402 listings before paying
- Enforce operator spend caps inside the agent host

---

## Verification Sources

- https://shinjukustaition.com (HTTP 200)
- https://github.com/ShinjukuStaition/shinjuku-shield
- npm `shinjuku-shield@0.3.86`
