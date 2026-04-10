# Coinbase Developer Platform (x402)

> **HTTP-native payments for the machine web — verify, settle, discover.**

| | |
|---|---|
| **Website** | https://docs.cdp.coinbase.com/x402/welcome |
| **Protocol** | https://x402.org |
| **GitHub** | https://github.com/coinbase/x402 |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/coinbase/x402?style=social)](https://github.com/coinbase/x402) |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |

---

## Official Website

https://docs.cdp.coinbase.com/x402/welcome

---

## Official Repo

https://github.com/coinbase/x402 — reference protocol implementation and multi-language SDKs (`@x402/*`, Python `x402`, Go, etc.)

---

## How to Use (Agent Onboarding)

**SDK + CDP Facilitator — handle HTTP 402 responses and payment proofs programmatically.**

```bash
# Example: Python SDK per coinbase/x402 README
pip install x402
```

Follow [Welcome to x402](https://docs.cdp.coinbase.com/x402/welcome) for client/server patterns, **facilitator** `verify` / `settle` APIs, and **Bazaar** discovery.

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official AgentSkills bundle located; integration is SDK + HTTP middleware.

```bash
npx clawhub@latest search x402
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not a standalone MCP product — any MCP agent that performs HTTP can participate in x402 payment flows.

---

## What It Does

**x402** revives **HTTP 402 Payment Required** for **machine-to-machine** payments: a client requests a resource, the server responds with payment terms, the client pays (typically stablecoin on EVM or Solana via facilitator), and retries with proof. Coinbase **Developer Platform** provides a **facilitator** (verify/settle), **SDKs**, and **Bazaar** as a discovery layer for x402-enabled endpoints — aimed at **AI agents** and autonomous API consumers paying per call without human checkout.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | x402 docs and launch materials describe **AI agents** and **autonomous clients** paying for APIs over HTTP ([CDP x402 welcome](https://docs.cdp.coinbase.com/x402/welcome)); protocol is M2M-first |
| **Agent-specific primitive** | **HTTP 402 + inline payment proof** — no human-facing checkout; payment is part of the request cycle |
| **Autonomy-compatible control plane** | Client libraries handle 402 challenge/response without per-payment human clicks |
| **M2M integration surface** | HTTP, TypeScript/Python/Go SDKs in [coinbase/x402](https://github.com/coinbase/x402), CDP REST facilitator APIs |
| **Identity / delegation** | Wallets, API keys, and facilitator records provide **attributable settlement** per payer |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **402 challenge** | Server advertises price and payment method |
| **Facilitator verify/settle** | CDP-hosted payment verification and on-chain settlement |
| **Bazaar** | Discovery/catalog of x402-enabled resources |
| **Multi-network** | EVM (e.g. Base, Polygon) and Solana support per docs |

---

## Autonomy Model

1. Agent HTTP client calls a paid API.
2. Server returns 402 with terms.
3. Agent SDK uses wallet + facilitator to pay and attach proof.
4. Agent retries; server returns the resource.

---

## Identity and Delegation Model

- Cryptographic wallet identity for payer; optional CDP API keys for facilitator usage.
- Settlement records on-chain and via CDP for audit.
- Distinct from human card checkout — designed for software agents.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP | x402 challenge/response on any compliant host |
| SDKs | https://github.com/coinbase/x402 |
| CDP REST | Facilitator endpoints per [docs](https://docs.cdp.coinbase.com/x402/docs/facilitator) |

---

## Human-in-the-Loop Support

- Wallet funding and CDP project setup may involve a human once.
- Per-request payment is automated.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Stripe Checkout** | Human-oriented redirect flows; not HTTP-402-native M2M |
| **Prepaid API keys only** | No dynamic per-resource pricing handshake in-band |

---

## Use Cases

- **Pay-per-call APIs** for LLM tool use.
- **Agent marketplaces** where agents spend wallet balance autonomously.
- **Micropayment-gated data** without accounts per agent.
