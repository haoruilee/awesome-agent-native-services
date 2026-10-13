# Tollex

> **"The economic control plane for autonomous software."**

| | |
|---|---|
| **Website** | https://tollex.org |
| **Docs** | https://tollex.org/docs/ |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Chains** | Base (USDC), Robinhood Chain (USDG) |
| **Standard** | x402 v2 (`exact`, EIP-3009), EIP-712 receipts |

---

## Official Website

https://tollex.org

---

## Official Repo

The public GitHub repository (previously `ShiftAboveCtrl/tollex`) returned 404 on 2026-10-13. Use the official developer docs instead: https://tollex.org/developers/ and https://tollex.org/docs/getting-started/ (agent-readable summary at https://tollex.org/llms.txt).

---

## How to Use (Agent Onboarding)

**Quickest verified path:**

```
Read https://tollex.org/llms.txt, then follow https://tollex.org/docs/getting-started/
```

Free planning, no wallet needed:

```bash
curl -s https://api.tollex.org/v1/resolve -H 'content-type: application/json' -d '{"need":"latest block on Robinhood Chain"}'
```

First paid call (about 0.008 USD in USDC on Base): answer the HTTP 402 x402 challenge per https://tollex.org/docs/api/ (OpenAPI with `x-payment-info` at https://api.tollex.org/openapi.json). The former GitHub `agent_check.py` example is unavailable while the repository returns 404.

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ Official skill unavailable — its GitHub repository (`ShiftAboveCtrl/tollex`) returned 404 on 2026-10-13

| Skill | What it teaches |
|---|---|
| `tollex` (skill repo currently unavailable; see [developer docs](https://tollex.org/developers/)) | Plan for free, pay one x402 call only within a ceiling the user set, verify the signed receipt, never re-sign a pending payment |

---

## MCP

**Status:** ⚠️ No hosted MCP endpoint

`api.tollex.org` does not host an MCP server. A self-hosted MCP server (stdio or Streamable HTTP) ships with the onboarding packages; the public integration surface is HTTP + x402, OpenAPI and A2A.

---

## What It Does

Tollex sells paid capabilities to software agents: Robinhood Chain reads (blocks, logs, balances, `eth_call` simulation), Stock Token prices and halt status, x402 endpoint inspection and receipt verification. An agent states a need and a cost ceiling, gets a free explained plan, pays per call with x402 v2 in USDC on Base or USDG on Robinhood Chain, and receives the result with an EIP-712 signed execution receipt. Uncertain payments are reconciled from the chain, so a lost response never leads to paying twice.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Instructions for an AI agent or coding agent integrating Tollex" ([tollex.org/llms.txt](https://tollex.org/llms.txt), [developer docs](https://tollex.org/developers/)); the buyer is software, there is no human checkout |
| **Agent-specific primitive** | `POST /v1/resolve`: a need plus typed constraints (max cost, networks, receipt required) returns an explained plan without spending; signed execution receipt per paid call; operation status for recovery |
| **Autonomy-compatible control plane** | The agent pays without per-action confirmation once the operator opts in with a per-call ceiling; Tollex refuses any payment that does not match the live terms exactly |
| **M2M integration surface** | HTTP + x402 v2, OpenAPI 3.1 (`/openapi.json`), A2A JSON-RPC with the a2a-x402 extension, `/.well-known/tollex.json`, `llms.txt` |
| **Identity / delegation** | No accounts or API keys: the payer is the wallet that signs a single-use, exact-amount EIP-3009 authorization; Tollex never holds the payer's key or funds |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Resolve** | Free, deterministic plan: eligible capabilities, rejection reasons, selected route and price |
| **x402 v2 payment per call** | `exact` EIP-3009 in USDC on Base or USDG on Robinhood Chain, same price on both |
| **Signed execution receipt** | EIP-712 receipt binding request, quote, payment and result; keys at `/.well-known/tollex-receipt-keys` |
| **Operation status** | Durable payment and settlement state, so a timeout is checked rather than paid again |
| **First paid call** | `GET /v1/agent-check`: proves a wallet, its signing and receipt handling end to end |

---

## Autonomy Model

```
Operator gives the agent a wallet and a per-call ceiling
    ↓
Agent asks POST /v1/resolve for a need (free, nothing signed)
    ↓
Agent requests the capability, reads the 402 terms (one option per rail)
    ↓
Agent refuses if the amount exceeds its ceiling; otherwise signs one EIP-3009 authorization
    ↓
Tollex verifies, settles on chain, executes, returns the result with a signed receipt
    ↓
Agent verifies the receipt; on a lost response it checks the operation instead of paying again
```

---

## Identity and Delegation Model

- **Wallet as identity**: the payer is whoever signs the authorization; no account, sign-up or API key
- **Exact, single-use authorizations**: each signature moves exactly the quoted amount to the published treasury once
- **Ceiling held by the agent's operator**: spend limits live in the agent's client, never in Tollex
- **Public signing identities**: treasury and receipt signer are published on the activity page

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP + x402 v2 | `402 PAYMENT-REQUIRED` terms, `PAYMENT-SIGNATURE` payment, `PAYMENT-RESPONSE` settlement and receipt |
| OpenAPI 3.1 | `https://api.tollex.org/openapi.json` with `x-payment-info` per paid route |
| A2A | Agent card at `/.well-known/agent-card.json`, JSON-RPC v1.0 and v0.3, a2a-x402 |
| Discovery | `/.well-known/tollex.json`, `/.well-known/x402`, `llms.txt`; indexed on x402scan |

---

## Human-in-the-Loop Support

The operator sets the ceiling and opts in to paying; the agent can be configured to ask before each payment. A public activity page shows operations without payer identity, with explorer links for verification. Tollex has no approval UI of its own.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A public RPC endpoint** | No pricing, no receipt, no plan; an agent cannot prove what it paid for or what it received |
| **Subscription data APIs** | Require a human account, API key and billing setup before the first call |
| **A bare x402 endpoint** | Payment only: no free planning, no signed execution receipt, no reconciliation when a response is lost |

---

## Use Cases

- **Trading and research agents** reading Stock Token prices and halt status before acting
- **Pre-flight checks**: simulate a transaction with `eth_call` before signing it
- **x402 buyers** inspecting a counterparty's live payment terms before paying
- **Audit trails**: signed receipts as evidence of what an agent bought and received
