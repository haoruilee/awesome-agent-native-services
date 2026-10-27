# Priors

> **"Reputation for AI agents that is earned, public and recomputable."**

| | |
|---|---|
| **Website** | https://priors.trade |
| **Docs** | https://github.com/priors-agents/priors · https://priors.trade/agent |
| **GitHub** | https://github.com/priors-agents/priors |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/priors-agents/priors?style=social)](https://github.com/priors-agents/priors) |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **License** | MIT |
| **Verified at** | 2026-10-27 |
| **Latest-month signal** | Hosted MCP `https://mcp.priors.trade/mcp` initializes as `priors-read` v0.3.0; repo last push 2026-10-26; CreditPool v2 live on Robinhood Chain (4663) |

---

## Official Website

https://priors.trade

---

## Official Repo

https://github.com/priors-agents/priors — contracts, SDK/CLI, MCP server, x402 helpers, and agent skill. Related demos: [agent001](https://github.com/priors-agents/agent001), [agent002](https://github.com/priors-agents/agent002).

---

## How to Use (Agent Onboarding)

**Interaction pattern:** Hosted read-only MCP (no key) + optional SDK/CLI for on-chain actions

```bash
claude mcp add --transport http priors https://mcp.priors.trade/mcp
```

Or add `https://mcp.priors.trade/mcp` to any MCP client. npm packages: `@priors/mcp`, `@priors/x402`.

---

## Agent Skills

**Status:** ✅ Official skill folder at [`skills/priors`](https://github.com/priors-agents/priors/tree/main/skills/priors) (plus `.claude-plugin`). Prefer hosted MCP for read-only score/credit checks.

---

---

## MCP

**Status:** ✅ Hosted read-only MCP

| Detail | Value |
|---|---|
| **URL** | https://mcp.priors.trade/mcp |
| **Server** | `priors-read` (verified initialize → v0.3.0) |
| **Auth** | None for read-only credit/score queries |
| **Scope** | Agent credit records, scores, pool figures, recent borrows/repays on Robinhood Chain |

Write paths (borrow/repay/backing) use the SDK/CLI and an agent wallet — not the read-only MCP.

---

## What It Does

Priors is an **on-chain credit pool for ERC-8004 AI agents** on Robinhood Chain. Agents borrow and repay USDG; every repayment and default is a public event. Score v2 is rebuilt from debt that someone else put at risk. The catalog entry covers the credit/reputation surface and MCP — not generic x402 middleware alone.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first** | Credit lines and scores are for ERC-8004 agents; demos ship agent wallets |
| **Agent-specific primitive** | Credit-backed trust score and public repayment history for agents |
| **M2M** | Hosted MCP + npm MCP/x402 packages + CLI |
| **Beyond paywall** | Reputation/credit ledger, not a metered generic API |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Credit-backed score** | Score v2 from on-chain debt others put at risk |
| **Credit pool** | ERC-8004 agents borrow/repay USDG on Robinhood Chain |
| **Public record** | Repayments and defaults are public events anyone can recompute |
| **Read-only MCP** | Query scores and pool state without a key |

---

## Autonomy Model

```
Counterparty or agent queries MCP/API for another agent's score and credit record
    ↓
Agent with a wallet uses SDK/CLI to borrow/repay within pool rules (backed lines)
    ↓
On-chain events update the public record anyone can recompute
```

---

## Identity and Delegation Model

- Agents are identified via **ERC-8004** registration on Robinhood Chain.
- Credit lines require **owner consent** and are **100% backed** by a backer's locked pool shares (v2); defaults burn backing shares.
- Read-only MCP exposes public state; spending/signing stays with the agent wallet operator.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Hosted MCP | `https://mcp.priors.trade/mcp` |
| npm | `@priors/mcp`, `@priors/x402` |
| HTTP check | `https://priors.trade/api/check?agent=<id>` |
| Chain | Robinhood Chain `eip155:4663` |

---

## Human-in-the-Loop Support

Operators fund/back lines and hold agent wallets. Read-only reputation checks need no human per call. Borrow/repay require a configured agent wallet and on-chain consent rules.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Star ratings / text reviews** | Cheap to fake; Priors ties score to repaid risk-backed debt |
| **Generic x402 paywall API** | Metering alone is not agent credit/reputation infrastructure |
| **Off-chain KYC databases** | Not an agent-native public recomputable ledger for machine counterparties |

---

## Use Cases

- Check another agent's credit score before trusting or paying it
- Build repayment history for an ERC-8004 agent wallet
- Back or lend against agent credit lines on Robinhood Chain

---

## Verification Sources

- https://github.com/priors-agents/priors (MIT)
- MCP initialize at https://mcp.priors.trade/mcp → `priors-read` 0.3.0
- https://priors.trade/api/check?agent=1 (HTTP 200)
