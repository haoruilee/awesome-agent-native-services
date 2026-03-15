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

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official skill published by Skyfire yet.

Skyfire's integration is primarily via its REST API and the KYAPay open protocol. No `SKILL.md`-based skill has been published to the AgentSkills ecosystem as of Q1 2026.

```bash
# No official install command yet — watch the repo:
# https://skyfire.xyz/product
```

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
