# MPP

> **"MPP lets agents pay for services on the web, extensible to any payment method."**

| | |
|---|---|
| **Website** | https://mpp.dev |
| **Docs** | https://mpp.dev |
| **GitHub** | https://github.com/wevm/mppx (canonical TypeScript SDK) |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/wevm/mppx?style=social)](https://github.com/wevm/mppx) |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **License** | MIT (`wevm/mppx`); protocol/site repos are separate (see Official Repo) |
| **Latest-month signal** | Last `wevm/mppx` push 2026-08-27 ([repo metadata](https://api.github.com/repos/wevm/mppx)); thinner star count than neighboring commerce OSS — still the documented TypeScript SDK |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://mpp.dev

Homepage H1: **"MPP lets agents pay for services on the web, extensible to any payment method."** Designed by **Tempo × Stripe**. Homepage Integrations strip (fetched 2026-08-27): Amazon, Alchemy, Browserbase, Cloudflare, Dune, Parallel, Visa. Do not infer additional partners beyond that list.

Supporting copy: **"Let agents pay for services autonomously"** — [Agentic payments](https://mpp.dev/use-cases/agentic-payments).

---

## Official Repo

There is **no single official monorepo**. Live GitHub surfaces:

| Repo | Role | License (GitHub API) |
|---|---|---|
| [wevm/mppx](https://github.com/wevm/mppx) | Canonical TypeScript SDK / CLI (`npm i mppx`) — use this for the star badge | MIT |
| [tempoxyz/mpp-specs](https://github.com/tempoxyz/mpp-specs) | Protocol specs — "Payment" HTTP authentication scheme; homepage https://paymentauth.org | see repo |
| [tempoxyz/mpp](https://github.com/tempoxyz/mpp) | Website source for https://mpp.dev | Apache-2.0 |

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK` + HTTP 402

```bash
npm i mppx
```

Client (official [quickstart](https://mpp.dev/quickstart/client.md)):

```ts
import { privateKeyToAccount } from 'viem/accounts'
import { Mppx, tempo } from 'mppx/client'

Mppx.create({
  methods: [tempo({ account: privateKeyToAccount('0x...') })],
})

const res = await fetch('https://mpp.dev/api/ping/paid')
```

Prompt-mode onboarding (paste into a coding agent) is published at https://mpp.dev/quickstart/client.md.

MCP client payments: [Official MCP SDK](https://mpp.dev/partner-integrations/mcp-sdk) — `Mppx.create` wraps the TypeScript MCP SDK's Streamable HTTP transport so paid tool calls retry with a Credential.

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package. Docs ship copy-paste **prompt mode** for agents.

| Skill | What It Teaches the Agent |
|---|---|
| Client prompt | https://mpp.dev/quickstart/client.md — add `mppx`, polyfill `fetch` for 402, ping `https://mpp.dev/api/ping/paid` |
| Paid MCP server prompt | https://mpp.dev/guides/monetize-mcp-server.md |
| Docs MCP | `search_docs` on `https://mpp.dev/api/mcp` (documentation search, not the payment protocol itself) |

```bash
npx clawhub@latest search mpp mppx
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ First-class **transport and SDK**, not a single hosted "MPP MCP server."

| Detail | Value |
|---|---|
| **MCP client payments** | [mpp.dev/partner-integrations/mcp-sdk](https://mpp.dev/partner-integrations/mcp-sdk) — payment-aware fetch for Streamable HTTP MCP |
| **MCP server charges** | [Monetize your MCP server](https://mpp.dev/guides/monetize-mcp-server) — JSON-RPC error `-32042`, Credential/Receipt in `_meta` |
| **Transport spec** | https://mpp.dev/protocol/transports/mcp |
| **Compatible Clients** | Official TypeScript MCP SDK plus any client that implements the MPP MCP encoding |

`mppx` can also speak **x402 exact** on HTTP (`PAYMENT-REQUIRED` / `PAYMENT-SIGNATURE`) alongside native MPP Challenges ([mcp-sdk](https://mpp.dev/partner-integrations/mcp-sdk)).

---

## What It Does

MPP (Machine Payments Protocol) is an open **pay-in-the-request** standard. Official `llms.txt`: it standardizes HTTP 402 for machine-to-machine payments. Flow: **Challenge → Credential → Receipt**. A server answers `402 Payment Required` with accepted methods and price; the client pays (Tempo stablecoins, cards/Stripe, Lightning, EVM, and other documented rails) and retries; the server returns a `Payment-Receipt`.

It is designed so agents do not need pre-provisioned API keys or a checkout form ([agentic payments](https://mpp.dev/use-cases/agentic-payments)). Sessions support metered pay-as-you-go (including per-token). `mppx` is the TypeScript interface: client polyfill, server `charge`, CLI, and a payments `Proxy`.

**Distinct from catalog x402 / [OpenLibx402](openlibx402.md):** those are the IETF-adjacent HTTP 402 / `PAYMENT-REQUIRED` crypto rail. MPP adds cards, bank-style Stripe paths, Lightning, Tempo sessions, and can *also* speak x402 exact from one SDK. **Distinct from [AP2](ap2.md) / [UCP](ucp.md):** those are checkout mandates and a commerce language, not inline HTTP 402. **Distinct from [Skyfire](skyfire.md) / [AgentsPay](agentspay.md) / [Circle Agent Stack](circle-agent-stack.md) / [Payman AI](payman-ai.md):** hosted KYA/wallets, not an open pay-in-the-request protocol.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: **"MPP lets agents pay for services on the web, extensible to any payment method."** — [mpp.dev](https://mpp.dev). Use-case page: **"Let agents pay for services autonomously"** — [agentic payments](https://mpp.dev/use-cases/agentic-payments) |
| **Agent-specific primitive** | HTTP 402 Challenge / Credential / `Payment-Receipt`; Tempo sessions; MCP `-32042` paid tools |
| **Autonomy-compatible control plane** | After `Mppx.create`, `fetch` handles 402 without a human checkout. Official: "The agent doesn't need pre-provisioned API keys, an account, or a human in the loop" |
| **M2M integration surface** | `mppx` client/server/proxy/CLI; MCP transport; protocol specs in `mpp-specs` |
| **Identity / delegation** | `Payment-Receipt` on success. Optional **Web Bot Auth** and **Trusted Agent Protocol (TAP)** request attestation on the initial request and paid retries — [Expanding identity support in mppx](https://mpp.dev/blog/mppx-identity-support). Spend limits via documented scoped access keys ([Managing agent spend](https://mpp.dev/guides/managing-agent-spend)) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Challenge** | `402` + accepted methods, amount, and how to pay |
| **Credential** | Client payment proof bound to the challenge |
| **Payment-Receipt** | Success header / MCP `_meta` receipt |
| **Charge / Session / Subscription** | One-time, metered, and recurring intents |
| **Tempo sessions** | Pay-as-you-go channels reused across requests |
| **Multi-rail methods** | Tempo, Stripe/cards, Lightning, EVM (incl. x402 exact), plus other homepage-documented rails |
| **`Mppx.create`** | Client polyfill or server `charge` / session |
| **Attestation** | Optional Web Bot Auth and TAP signers/verifiers |

---

## Autonomy Model

```
Operator funds an account / access key and calls Mppx.create({ methods: [tempo({ account })] })
    -> Agent fetch() hits a paid resource
    -> Server returns 402 Challenge
    -> mppx builds a Credential and retries (including MCP tool retries)
    -> Server verifies, fulfills, returns Payment-Receipt
```

No per-request checkout UI on the documented autonomous path. Manual `preparePayment` / `createCredential` exists when a human UI is desired.

---

## Identity and Delegation Model

- **Payment identity:** The signing account (viem, Privy, Accounts SDK, or scoped access key) is the payer. Receipts carry a reference and timestamp.
- **Agent attestation (optional):** Web Bot Auth (`Signature-Agent` + trusted HTTPS directory) and TAP (`browse` / `payment` intent) sign the first request and each 402 retry ([blog](https://mpp.dev/blog/mppx-identity-support)). MPP leaves the identity protocol to the application.
- **Spend delegation:** Documented access keys with spending limits, call scopes, recipient restrictions, and revocation.
- **Not a hosted wallet product:** Operators bring the rail (Tempo, Stripe, Lightning, …). MPP is the open challenge/credential protocol.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Spec / site | https://mpp.dev — site source [tempoxyz/mpp](https://github.com/tempoxyz/mpp) |
| Protocol drafts | [tempoxyz/mpp-specs](https://github.com/tempoxyz/mpp-specs) — Payment HTTP auth scheme |
| TypeScript SDK | `npm i mppx` — [wevm/mppx](https://github.com/wevm/mppx) |
| CLI | `npx mppx account create` then `mppx example.com` |
| MCP | Client wrap + server `Transport.mcpSdk()` |
| Docs MCP | `https://mpp.dev/api/mcp` |
| x402 interop | Same `mppx` fetch can satisfy x402 exact |

---

## Human-in-the-Loop Support

Not required for the autonomous 402 retry path. Optional: present payment UI via `preparePayment` before creating a Credential; Accounts SDK / Wagmi connectors for a human-held wallet; `--safe`-style spend keys for long-running agents. Checkout mandates are **AP2's** job, not MPP's.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Coinbase x402 / OpenLibx402** | HTTP 402 crypto `PAYMENT-REQUIRED` scheme. MPP is a multi-rail Challenge/Credential protocol that can *also* speak x402 exact |
| **AP2** | Verifiable checkout/payment **mandates** (VDCs). Not inline HTTP 402 settlement |
| **UCP** | Checkout/commerce language. It may use AP2 for payment; it is not pay-in-the-request 402 |
| **Skyfire / AgentsPay / Circle / Payman** | Hosted KYA, wallets, or banking agents. Not an open pay-in-the-request protocol any merchant can speak |
| **A generic Stripe Checkout page** | Human-first hosted pay form. No machine 402 Challenge/Credential loop |

---

## Use Cases

- **Agent pays for an API mid-loop** — LLM, search, image, or data call without a pre-issued API key
- **Paid MCP tools** — charge `-32042` per tool; client SDK retries with a Credential
- **Metered sessions** — per-token or per-request channels
- **One SDK, two dialects** — native MPP and x402 exact from `mppx`
