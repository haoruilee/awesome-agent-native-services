# Nevermined

> **"The payment layer AI agents actually need."**

| | |
|---|---|
| **Website** | https://nevermined.io |
| **Blog** | https://nevermined.ai/blog/the-payment-layer-ai-agents-actually-need-introducing-the-nevermined-x402-facilitator |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Protocol** | x402 (HTTP-layer payment standard) |

---

## Official Website

https://nevermined.io

---

## Official Repo

https://github.com/nevermined-io/payments — TypeScript SDK

https://github.com/nevermined-io/payments-py — Python SDK

https://github.com/nevermined-io/protocol — Core smart contracts

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official skill published by Nevermined yet.

Nevermined operates at the HTTP protocol layer (x402), which is transparent to the agent application code. No `SKILL.md`-based skill has been published as of Q1 2026.

```bash
# No official install command yet — watch the repo:
# https://github.com/nevermined-io
```

---

## MCP

**Status:** ⚠️ Not yet published as standalone MCP server

Nevermined integrates at the HTTP protocol layer (x402). Any MCP-based agent that makes HTTP calls can transparently benefit from x402 payment handling. A dedicated MCP server tool has not been published as of Q1 2026.

| Detail | Value |
|---|---|
| **Protocol** | HTTP x402 (RFC-level payment standard) |
| **SDK Docs** | https://docs.nevermined.app/docs/libraries/getting-started/ |
| **GitHub Org** | https://github.com/nevermined-io |

---

## What It Does

Nevermined's **x402 Facilitator** embeds payment directly into the HTTP protocol. When an agent makes an API request, the server responds with HTTP 402 Payment Required; the agent pays via the x402 protocol and the request is fulfilled — all within a single HTTP exchange. No human checkout flow. No redirect. Payment is part of the API call itself.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The x402 protocol is designed specifically for machine-to-machine payments; the blog post explicitly frames it as *"the payment layer AI agents actually need"* |
| **Agent-specific primitive** | HTTP 402 response + inline payment — a primitive that only makes sense for agents (no human reads an HTTP 402 and manually pays) |
| **Autonomy-compatible control plane** | Payment happens within the HTTP request lifecycle; agents never break execution to handle payment |
| **M2M integration surface** | HTTP x402 protocol; REST API; standard HTTP request/response cycle |
| **Identity / delegation** | Per-agent payment accounts; operator-defined budgets; transaction attribution per agent |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **x402 Protocol** | HTTP-layer standard: request → 402 response with payment terms → agent pays → resource delivered |
| **Inline Payment** | Payment completes within the API call; no redirect, no checkout page |
| **Prepaid Credits** | Pre-fund agent accounts; payments deducted without per-call authorization |
| **Usage-Based Billing** | Pay per API call, per token, per request |
| **Outcome-Based Billing** | Pay on successful task completion rather than per-call |
| **Dynamic Pricing** | Prices can vary based on demand, priority, or resource cost |

---

## Autonomy Model

```
Agent makes HTTP request to a service
    ↓
Service responds: HTTP 402 Payment Required + payment terms
    ↓
x402 Facilitator handles payment from agent's account
    ↓
Original request retried with payment proof
    ↓
Service delivers response
```

The entire flow is transparent to the agent's application logic. Payment is infrastructure, not application code.

---

## Identity and Delegation Model

- Per-agent payment accounts with operator-defined budgets
- Payment proof is cryptographically attached to the retried request
- Transaction history attributable per agent
- Supports fiat, crypto, stablecoins, and prepaid credit through unified interface

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP x402 | Standard 402 response with payment terms; agent-side Facilitator handles payment |
| REST API | Account management, budget configuration, transaction history |
| Payment Methods | Fiat, crypto, stablecoins (USDC), prepaid credits |

---

## Human-in-the-Loop Support

Budget limits configured by operator. Individual payments are fully autonomous within those limits.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Stripe Checkout** | Requires human browser session; payment is a separate flow, not inline with the API call |
| **API keys with billing** | Static credentials; billing is separate from request lifecycle; no per-agent accounting |
| **Manual invoicing** | Requires human review and payment authorization; not compatible with autonomous agent loops |

---

## Use Cases

- **LLM API access** — agents pay per-token for inference without pre-negotiated API contracts
- **Data marketplace** — agents pay for specific datasets or search results per query
- **Premium tool access** — agents pay for high-quality tools (web search, code execution, specialized APIs) inline
- **Agent-to-agent payments** — specialist agents charge peer agents for services in a multi-agent architecture
