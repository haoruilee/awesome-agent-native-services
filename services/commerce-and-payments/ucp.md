# Universal Commerce Protocol (UCP)

> **"The common language for platforms, agents, and businesses."**

| | |
|---|---|
| **Website** | https://ucp.dev |
| **Docs** | https://ucp.dev |
| **GitHub** | https://github.com/Universal-Commerce-Protocol/ucp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/Universal-Commerce-Protocol/ucp?style=social)](https://github.com/Universal-Commerce-Protocol/ucp) |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-08-25 ([repo metadata](https://api.github.com/repos/Universal-Commerce-Protocol/ucp)); spec + docs repo |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://ucp.dev

---

## Official Repo

https://github.com/Universal-Commerce-Protocol/ucp

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK` + protocol spec

UCP is an **open checkout/commerce protocol**, not a wallet. Start from the public spec and samples:

```bash
# Schema tool agents use to resolve ucp_* annotations at runtime
cargo install ucp-schema

# Spec + docs checkout
git clone https://github.com/Universal-Commerce-Protocol/ucp.git
```

Official next steps from the README:

- Documentation and full spec: [ucp.dev](https://ucp.dev)
- [Samples](https://github.com/Universal-Commerce-Protocol/samples)
- [SDKs](https://github.com/orgs/Universal-Commerce-Protocol/repositories)
- [Conformance tests](https://github.com/Universal-Commerce-Protocol/conformance)

There is no URL-onboarding document and no hosted merchant wallet.

---

## Agent Skills

**Status:** ⚠️ No official Agent Skills package published.

```bash
npx clawhub@latest search ucp universal-commerce-protocol
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Documented as a first-class transport — UCP is transport-agnostic.

| Detail | Value |
|---|---|
| **Role** | Businesses can expose Capabilities via REST, MCP, or A2A |
| **MCP product** | Not a single hosted MCP server; implementers publish their own capability endpoints |
| **Related payments** | Built-in support for Agent Payments Protocol (AP2) on the payment path |

---

## What It Does

The Universal Commerce Protocol is an open standard for **agentic commerce**: discovery, cart, identity linking, checkout, and order lifecycle across shopping (and, the homepage says, expanding into lodging and food). Official homepage copy: UCP provides building blocks so platforms, agents, and businesses share one standard instead of custom builds.

Capabilities are modular (Checkout, Identity Linking, Order, Payment Token Exchange) with extensions (discounts, fulfillment). Businesses publish a profile of supported capabilities so platforms can discover them autonomously. Checkout sessions can run with or without a human present. Payments use existing rails plus AP2 mandates and verifiable credentials rather than inventing a new wallet.

This is distinct from catalog x402, Skyfire, and Circle: those are payment/wallet or HTTP-402 settlement layers. UCP is the **checkout and commerce protocol** those rails can plug into.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: **"The common language for platforms, agents, and businesses."** — [ucp.dev](https://ucp.dev). README: **"Designed from the ground up to support AI agents acting on behalf of users to discover products, fill carts, and complete purchases securely."** — [repo](https://github.com/Universal-Commerce-Protocol/ucp) |
| **Agent-specific primitive** | Capability profiles for autonomous discovery; checkout sessions with or without human intervention; OAuth identity linking (`dev.ucp.shopping.checkout` scope in the homepage sample); AP2 payment mandates |
| **Autonomy-compatible control plane** | Agents can discover capabilities, build carts, and complete checkout when the merchant profile and mandates allow human-not-present flow |
| **M2M integration surface** | REST and JSON-RPC transports; MCP and A2A support built-in; `ucp-schema` for operation-specific schemas; SDKs and conformance suite |
| **Identity / delegation** | OAuth 2.0 identity linking so agents act without sharing user credentials; AP2 mandates and verifiable credentials for payment consent. Businesses stay Merchant of Record |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Capability profile** | Business declares Checkout, Identity Linking, Order, and extensions for autonomous discovery |
| **Checkout session** | Cart, tax, fulfillment, and `ready_for_complete` state across merchants |
| **Identity Linking** | OAuth 2.0 authorization for an agent to act on a buyer's behalf |
| **Order + webhooks** | Post-purchase status, shipment, returns |
| **Payment token exchange** | PSP / credential-provider handshake; AP2-compatible |
| **`ucp-schema`** | Resolves `ucp_*` annotations so agents see create/update/read field subsets |

---

## Autonomy Model

```
Agent discovers a business profile (supported Capabilities)
    -> Optional OAuth identity link (scope such as dev.ucp.shopping.checkout)
    -> Create/update checkout session (cart, fulfillment, totals)
    -> Payment via AP2 mandate / token exchange when the profile requires it
    -> Complete checkout; follow order webhooks
```

Human presence is a protocol option (embedded checkout UI, address delegation), not a requirement of every capability.

---

## Identity and Delegation Model

- **Buyer vs agent:** Identity Linking uses OAuth so the agent does not hold the user's password.
- **Merchant of Record:** Official homepage: businesses retain control and customer relationships.
- **Payment consent:** AP2 mandates and verifiable credentials — cryptographic proof of user intent, not inferred clicks.
- **Not a wallet:** UCP does not issue agent USDC wallets. It standardizes checkout and hands payment to AP2 / PSPs / credential providers.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Spec / docs | https://ucp.dev and this repository's `source/` schemas |
| REST / JSON-RPC | Documented transports |
| MCP / A2A | Built-in support for agent frameworks |
| Schema CLI | `cargo install ucp-schema` |
| Samples / SDKs / conformance | Sister repos under [Universal-Commerce-Protocol](https://github.com/Universal-Commerce-Protocol) |

---

## Human-in-the-Loop Support

Identity linking and some embedded checkout UIs need a human once (OAuth, address, or hosted checkout). Autonomous checkout is an explicit protocol goal when mandates and profiles allow it. Lodging and food specs are described on the homepage as coming soon — do not treat those industry payloads as shipped.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **x402 / Coinbase CDP** | HTTP 402 settlement for API calls. Not a cart/checkout/order protocol |
| **Skyfire / Circle Agent Stack** | Agent wallets and KYA/payment execution. Not an open multi-merchant checkout language |
| **AP2** | Mandate / verifiable-credential *payment* layer. UCP consumes AP2; it does not replace it |
| **A generic Stripe Checkout** | Human-first hosted pay page. No capability profile, agent discovery, or transport-agnostic A2A/MCP surface |

---

## Use Cases

- **Agent shopping** — discover a merchant profile, build a cart, complete checkout
- **Platform embedding** — native or embedded business checkout without a per-merchant integration
- **Post-purchase agents** — consume order webhooks for shipping and returns
- **Schema-accurate tool calls** — `ucp-schema` so agents only send fields valid for the current operation
