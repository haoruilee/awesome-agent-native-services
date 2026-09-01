# Agent Payments Protocol (AP2)

> **"An open protocol for the emerging Agent Economy."**

| | |
|---|---|
| **Website** | https://ap2-protocol.org |
| **Docs** | https://ap2-protocol.org |
| **GitHub** | https://github.com/google-agentic-commerce/AP2 |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/google-agentic-commerce/AP2?style=social)](https://github.com/google-agentic-commerce/AP2) |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last *code* push 2026-06-17 ([repo metadata](https://api.github.com/repos/google-agentic-commerce/AP2)); docs/site still served. Quieter than neighboring commerce repos — disclose before treating samples as weekly-fresh |
| **Verified at** | 2026-08-25 |

---

## Official Website

https://ap2-protocol.org

---

## Official Repo

https://github.com/google-agentic-commerce/AP2

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK` + scenario samples

Install the types package from [google-agentic-commerce/AP2](https://github.com/google-agentic-commerce/AP2) (PyPI later; official install is from git):

```bash
# Types package (PyPI later; official install is from git): https://github.com/google-agentic-commerce/AP2
uv pip install git+https://github.com/google-agentic-commerce/AP2.git@main
```

Run a documented scenario from the repo root (needs Python 3.11+, `uv`, and a Gemini/Vertex credential for the *samples*, not for the protocol itself):

```bash
cd AP2
bash code/samples/python/scenarios/a2a/human-present/cards/run.sh
```

Other scenarios live under `code/samples/python/scenarios/`, `code/samples/go/scenarios/`, and `code/samples/android/scenarios/`. Spec and flows: [docs/](https://github.com/google-agentic-commerce/AP2/tree/main/docs). There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official Agent Skills package published.

```bash
npx clawhub@latest search ap2 agent-payments-protocol
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Extension surface, not a hosted MCP server.

Official homepage: AP2 is an open extension for **A2A** and **UCP**, with MCP mentioned as a tool layer agents may already use ("Build agents with ADK (or any framework), equip with MCP (or any tool), collaborate via A2A, and use AP2 to secure payments"). AP2 itself is the mandate/credential protocol.

---

## What It Does

Agent Payments Protocol (AP2) is an open protocol for **verifiable agent payments**. Today's rails assume a human clicked Buy. When an agent pays, merchants cannot answer authorization, authenticity, or accountability from that click model. AP2's answer is **verifiable digital credentials (VDCs)** — tamper-evident, cryptographically signed mandates:

- **Checkout Mandate** — open (constraints before a cart exists) or closed (authorization of a finalized checkout), shared with the merchant.
- **Payment Mandate** — open (budget / allowed instruments) or closed (amount bound to a finalized checkout), shared with the credential provider, networks, and merchant processor.

Mandates chain into a non-repudiable audit trail for human-present and human-not-present transactions. Samples include human-not-present cards, human-not-present **x402**, digital payment credentials on Android, and human-present cards.

This is the **mandate layer next to catalog x402**: x402 is HTTP 402 settlement; AP2 is proof of user intent the merchant and networks can verify. UCP documents AP2 as its secure-payment path.

**Freshness:** `pushed_at` on the GitHub repo was 2026-06-17 at verification. Treat the spec and samples as the source of truth; do not infer weekly release cadence.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: **"Agent Payments Protocol (AP2) is an open protocol for the emerging Agent Economy"** and **"use AP2 to secure payments with gen AI agents"** — [ap2-protocol.org](https://ap2-protocol.org). GitHub: **"Building a Secure and Interoperable Future for AI-Driven Payments."** |
| **Agent-specific primitive** | Open/closed Checkout and Payment **mandates** (VDCs). Trust is **"verifiable intent, not inferred action"** |
| **Autonomy-compatible control plane** | Human-not-present samples show an agent completing a purchase inside mandate constraints without a per-SKU human click |
| **M2M integration surface** | Python/Go/Android samples, Pydantic models + JSON schemas under `code/sdk/python/ap2/`, A2A/UCP extension |
| **Identity / delegation** | Role-based architecture; mandates are signed credentials. Accountability is a first-class design goal (who is liable if the agent hallucinates a purchase) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Checkout Mandate (open/closed)** | Constraints or finalized-cart authorization shared with the merchant |
| **Payment Mandate (open/closed)** | Instrument/budget constraints or bound payment authorization |
| **VDC chain** | Linked, signed credentials forming the audit trail |
| **Human-present / human-not-present flows** | Protocol modes, not product SKUs |
| **x402 sample path** | Same mandate model over an x402 payment rail |

---

## Autonomy Model

```
User (or prior session) issues an open checkout/payment mandate with constraints
    -> Shopping agent negotiates a cart with a merchant (A2A / UCP / sample servers)
    -> Closed checkout mandate binds the finalized cart
    -> Closed payment mandate authorizes the instrument/amount
    -> Credential provider / PSP / merchant processor verify the chain
    -> Human-not-present path completes without another click if mandates allow it
```

---

## Identity and Delegation Model

- **User remains in control:** Official principle. Mandates are the delegation artifact.
- **Roles:** User, shopping agent, merchant, credential provider, networks, merchant payment processor — each sees the mandate types meant for them.
- **Non-repudiation:** Cryptographic audit trail for disputes.
- **Not a wallet product:** AP2 does not replace Skyfire/Circle wallets; it standardizes proof those rails can attach.
- **Standardization path:** Homepage says spec work continues in FIDO Agentic Authentication and Payments working groups.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Spec / docs | https://ap2-protocol.org and repo `docs/` |
| Python types | `uv pip install git+https://github.com/google-agentic-commerce/AP2.git@main` |
| Samples | `code/samples/python`, `go`, `android` + `run.sh` |
| Web demo client | `code/web-client/` (Vite + React) |
| Extensions | A2A, UCP; x402 sample |

---

## Human-in-the-Loop Support

Human-present flows capture closed mandates at checkout time. Human-not-present flows use earlier open mandates (budget, allowed items). AP2 exists *because* inferred "the user would have clicked" is not enough. Optional UX in samples does not replace the credential chain.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **x402** | Pays an HTTP resource. It does not define checkout/payment mandates or merchant-verifiable user intent |
| **UCP** | Commerce/checkout protocol. It *uses* AP2 for payments; it is not the mandate layer |
| **Skyfire / Circle** | Hosted agent wallets and KYA. AP2 is an open credential protocol any compliant agent/merchant can speak |
| **A card-on-file API** | Assumes a human merchant session. It cannot answer agent authorization / hallucination / liability |

---

## Use Cases

- **Human-not-present shopping** — agent buys inside an open mandate's constraints
- **Merchant verification** — prove the cart matches signed user intent
- **x402 + mandates** — attach AP2 proof to an HTTP 402 settlement
- **Dispute evidence** — replay the VDC chain instead of model logs alone
