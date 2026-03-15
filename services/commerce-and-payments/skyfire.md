# Skyfire

> **"Identity and payments for autonomous AI agents."**

| | |
|---|---|
| **Website** | https://skyfire.xyz |
| **Product** | https://skyfire.xyz/product |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Protocol** | KYAPay (open standard) |

---

## Official Website

https://skyfire.xyz

---

## Official Repo

Not yet publicly released as open-source. API and SDK available to registered developers via the Skyfire developer portal.

---

## Skills

| Skill | Description |
|---|---|
| **Create Agent Identity (KYA)** | Issue a verified Know Your Agent identity token for a new agent |
| **Fund Agent Wallet** | Credit an agent's Skyfire wallet via card, ACH, wire, or USDC |
| **Execute Agent Checkout** | Pay for a service using the standardized KYAPay protocol |
| **Set Spend Limits** | Configure per-agent budget caps and per-transaction maximums |
| **Query Behavioral Record** | Retrieve an agent's immutable transaction history for fraud assessment |
| **Authenticate Agent (OAuth2/OIDC)** | Verify agent identity using OAuth2/OIDC-compatible token flow |
| **Monetize Service (Receiver)** | Accept agent payments by implementing the KYAPay receiver protocol |

---

## MCP

**Status:** ⚠️ Not yet publicly documented

Skyfire does not currently publish a standalone MCP server. Integration is via REST API and the open KYAPay protocol. An agent framework integration (SDK) is available through the developer portal.

| Detail | Value |
|---|---|
| **Developer Portal** | https://skyfire.xyz/product |
| **Protocol** | KYAPay (open standard, OAuth2/OIDC-compatible) |
| **API Docs** | Available after registration at skyfire.xyz |

---

## What It Does

Skyfire is a payment network and identity infrastructure built from the ground up for autonomous AI agents. It provides **Know Your Agent (KYA)** verified identities, agent wallets with programmable spend controls, and an open **KYAPay protocol** — so agents can sign up for services, authenticate, and pay without any human in the transaction loop. Service providers can monetize AI agent access directly, treating agents as a new class of verified customer.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"trusted network for payments at the speed of AI"*; product page: *"create a verified identity for your AI agents"* |
| **Agent-specific primitive** | KYA identity token (no human equivalent); agent wallet with programmable spend limits; KYAPay open protocol for standardized agent transactions |
| **Autonomy-compatible control plane** | Agents sign up, authenticate, and pay with zero human intervention; operator-defined budgets prevent runaway spend |
| **M2M integration surface** | REST API, OAuth2/OIDC-compatible auth, open KYAPay protocol |
| **Identity / delegation** | Immutable behavioral records per agent; verified identity tokens; service providers receive fraud signals and access controls |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **KYA (Know Your Agent)** | Verified agent identity token — the agent equivalent of KYC |
| **Agent Wallet** | Programmatically funded payment account owned by the agent/operator |
| **Programmable Spend Limits** | Per-agent budget and per-transaction caps set by operator |
| **KYAPay Protocol** | Open standard for agent-to-service payment interactions (OAuth2/OIDC-compatible) |
| **Agent Checkout** | Standardized checkout flow agents use to pay for services autonomously |
| **Behavioral Record** | Immutable log of agent transaction history, building a verifiable reputation |

---

## Autonomy Model

```
Operator funds agent wallet and sets spend policies
    ↓
Agent encounters a paid service (API, data, SaaS feature)
    ↓
Agent authenticates via KYA identity token (OAuth2/OIDC)
    ↓
Agent executes payment via KYAPay protocol
    ↓
Service delivers access
    ↓
Transaction logged to agent's immutable behavioral record
```

No human confirms individual payments. Spend limits are the control mechanism.

---

## Identity and Delegation Model

- **KYA Identity Token** — cryptographically verified agent identity analogous to KYC for humans
- **Behavioral Record** — immutable per-agent transaction history that service providers can query for fraud prevention
- **Verified Access** — service providers can grant or deny access based on agent identity, reputation, and spending history
- **Operator Delegation** — operators fund wallets and set policies; agents spend within those bounds autonomously

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Wallet management, payment execution, identity operations |
| OAuth2/OIDC | Standard auth protocol extended for agent identity |
| KYAPay Protocol | Open standard for agent checkout — any service can implement receiver side |
| Agent Checkout | Standardized UI/API flow for agent-to-service transactions |

---

## Funding Sources

Agents can fund their Skyfire wallets via:
- Credit / debit cards
- ACH transfer
- Wire transfer
- USDC on Base (stablecoin)

---

## Human-in-the-Loop Support

Operator-defined budget limits. Individual transactions are fully autonomous within those limits. Audit trails support post-hoc human review. KYA behavioral records allow service providers to flag anomalous agent activity.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Stripe** | No agent identity model; no KYA; checkout requires human browser |
| **PayPal** | Human wallet; no programmatic agent identity or spend controls |
| **Corporate credit cards** | Human-facing financial instrument; no per-agent attribution or automated policy enforcement |
| **Standard OAuth** | Authentication protocol; no payment primitive, no agent identity record |

---

## Use Cases

- **API-consuming agents** — agents pay for LLM inference, data APIs, search APIs autonomously per call
- **Marketplace agents** — agents purchase digital goods, SaaS subscriptions, or data on behalf of operators
- **Service provider monetization** — SaaS companies add KYAPay receiver support to charge AI agent customers
- **Multi-agent systems** — agents pay peer agents for specialized services in a multi-agent economy
