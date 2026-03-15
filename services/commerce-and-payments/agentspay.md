# AgentsPay

> **"Crypto identity and embedded wallets for AI agents."**

| | |
|---|---|
| **Website** | https://agentspay.dev |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Chain** | Base L2 (Ethereum L2) |
| **Standard** | W3C DID (Decentralized Identifier) |

---

## Official Website

https://agentspay.dev

---

## Official Repo

https://github.com/AgentPayy/AgentPayy — Core platform (TypeScript / Python)

---

## Skills

| Skill | Description |
|---|---|
| **Issue Agent DID** | Create a W3C Decentralized Identifier on Base L2 for a new agent |
| **Bootstrap Agent Wallet** | Provision a non-custodial USDC wallet for an agent without KYC |
| **Execute Payment** | Pay for a service (API, data, tool) from the agent's USDC wallet |
| **Discover Services (MCP Gateway)** | Query the MCP-native gateway to find and access paid services |
| **Set Spending Ceiling** | Configure operator-defined maximum spend for an agent |
| **Query On-Chain Record** | Retrieve an agent's transaction history from Base L2 |

---

## MCP

**Status:** ✅ MCP-Native

AgentsPay's API gateway is designed natively around the Model Context Protocol — service discovery and payment are MCP-native primitives, not an add-on layer.

| Detail | Value |
|---|---|
| **MCP Gateway** | Built into the AgentsPay platform |
| **Transport** | MCP-native (HTTP) |
| **Chain** | Base L2 (Ethereum L2) |
| **Standard** | W3C DID + x402 payment protocol |

---

## What It Does

AgentsPay issues **W3C Decentralized Identifiers (DIDs)** to AI agents on the Base L2 blockchain, embeds USDC wallets with operator-set spending limits, and provides an MCP-native API gateway. Agents can discover which services require payment and pay for them directly — solving the common agent failure mode where execution halts when an API key or payment is needed.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Built from inception for non-human actors; DID issuance and embedded wallets have no human-facing equivalent use case |
| **Agent-specific primitive** | W3C DID on Base L2 (on-chain agent identity); embedded USDC wallet with operator spend limits; MCP-native API gateway for service discovery and payment |
| **Autonomy-compatible control plane** | Agents discover and pay for services without human credential injection; spending ceilings prevent runaway spend |
| **M2M integration surface** | MCP-native API gateway; REST API |
| **Identity / delegation** | On-chain DID provides cryptographically verifiable agent identity; operator-set spending limits define delegation bounds |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **W3C DID on Base L2** | Cryptographically verifiable on-chain agent identity |
| **Embedded USDC Wallet** | Agent-controlled stablecoin wallet with operator-defined spending limits |
| **MCP-Native API Gateway** | Service discovery and payment gateway built for Model Context Protocol |
| **Spending Ceiling** | Operator-defined maximum spend per agent |
| **Service Discovery** | Agents find and access paid services autonomously without human credential management |

---

## Autonomy Model

```
Operator creates agent DID and funds USDC wallet with spending ceiling
    ↓
Agent encounters a service requiring payment or API key
    ↓
Agent queries MCP-native gateway to discover service terms
    ↓
Agent executes payment from USDC wallet (within spending ceiling)
    ↓
Service provides access
    ↓
Transaction recorded on-chain against agent DID
```

---

## Identity and Delegation Model

- **W3C DID** — decentralized, portable agent identity standard not tied to any single provider
- **On-chain** — identity and transaction history are cryptographically verifiable and tamper-evident
- **Base L2** — low-cost Ethereum L2 chain makes per-transaction recording economically viable
- **Spending Ceiling** — operator defines the maximum; agent operates autonomously within that bound

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP-Native API Gateway | Primary interface for service discovery and payment |
| REST API | Wallet management, DID operations |
| Base L2 | On-chain identity and transaction recording |

---

## Human-in-the-Loop Support

Operator sets spending ceilings upfront. Individual service payments are fully autonomous. On-chain records support complete post-hoc audit.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Standard crypto wallets (MetaMask)** | Require human key management and transaction confirmation; not designed for autonomous agent spending |
| **Stripe** | No on-chain identity; no agent DID; checkout requires human browser session |
| **API keys** | Static credentials; no payment primitive; no identity record; expire and require human rotation |

---

## Use Cases

- **Autonomous API consumption** — agents pay for search APIs, LLM inference, data services per-call without human intervention
- **Agent marketplaces** — agents discover and pay peer agents for specialized services
- **Permissionless service access** — agents access services that previously required human sign-up and payment setup
