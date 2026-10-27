# send21

> **"Payments for AI agents, without giving them your keys"**

| | |
|---|---|
| **Website** | https://send21.io |
| **Docs** | https://send21.io/docs/mcp |
| **GitHub** | https://github.com/send21io/send21-examples |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Custody** | Non-custodial. send21 never holds private keys or funds, never signs and never broadcasts. The payer signs and sends from their own wallet |
| **Publisher** | send21. The proposal and this PR come from the send21 team (vendor submission, disclosed in [#255](https://github.com/haoruilee/awesome-agent-native-services/issues/255)) |
| **Verified at** | 2026-10-27 |
| **Latest-month signal** | Homepage HTTP 200. Unauthenticated `tools/list` on `POST https://send21.io/mcp` returned 14 tools. https://send21.io/llms-full.txt |

---

## Official Website

https://send21.io

Agent page: https://send21.io/ai-agent-payments

---

## Official Repo

https://github.com/send21io/send21-examples

Examples and framework integrations (LangChain, Vercel AI SDK). The hosted API and MCP server are not open source. Cursor plugin with the MCP server and skills: https://github.com/send21io/send21-plugin

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `MCP`

The account owner creates a scoped `s21_` API key at https://send21.io/api-keys (or signs in through MCP OAuth at `https://send21.io/mcp/oauth`). The agent then connects to the hosted MCP server or calls the REST API.

**Quickest verified path:**

```bash
claude mcp add --transport http send21 https://send21.io/mcp \
  --header "Authorization: Bearer s21_..."
```

REST alternative: OpenAPI at https://send21.io/openapi.json, quickstart at https://send21.io/docs/quickstart. Agent-readable docs: https://send21.io/llms-full.txt. A testnet demo with no account and no key: https://send21.io/demo.

---

## Agent Skills

**Status:** ✅ Available

The [send21 plugin](https://github.com/send21io/send21-plugin) bundles the MCP server with three skills.

| Skill | What It Teaches the Agent |
|---|---|
| `create-pay-link` | Create a fiat-priced pay link or draft to the owner's approved addresses |
| `check-payment` | Track a payment request or draft to confirmation and handle an amount mismatch |
| `verify-webhooks` | Check `X-Send21-Signature-V2` and the timestamp before acting on a webhook |

Search community skills: `npx clawhub@latest search send21`

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Endpoint** | `https://send21.io/mcp` |
| **Transport** | Streamable HTTP, stateless. Bearer `s21_` key or OAuth 2.1 (PKCE, dynamic client registration) at `https://send21.io/mcp/oauth`. `tools/list` and `get_fee_schedule` work without a key |
| **Tools** | `create_payment_request`, `get_payment_request`, `create_draft`, `get_draft`, `get_draft_status`, `list_draft_quotes`, `get_transaction_template`, `submit_lightning_proof`, `list_address_book`, `propose_receiving_address`, `get_account_status`, `create_account`, `get_rate`, `get_fee_schedule` |
| **Registry** | `io.github.send21io/mcp` in the official MCP Registry |
| **Compatible Clients** | Any client that can call a remote Streamable HTTP MCP server, for example Claude Code, Cursor and VS Code |

Every tool carries MCP annotations. The read tools are `readOnlyHint: true`, and no tool is destructive: none can delete anything or move funds.

---

## What It Does

send21 is non-custodial payment software for crypto pay links and payment drafts. An agent creates a payment request (a pay link that offers several currencies) or a draft (one payment to one receiver), priced in a crypto amount or in any of 161 fiat currencies with an exchange rate locked for 15 minutes. send21 watches the chain and reports progress by status endpoint and signed webhook until the payment confirms.

The payment itself is signed in a wallet the agent does not control: the payer's own wallet, or the operator's wallet through a transaction template. Assets per network: BTC on Bitcoin and Lightning; USDC, USDT, EURC, SOL and wrapped BTC on Solana; USDC, USDT, EURC, ETH and WBTC on Ethereum; USDC, EURC and ETH on Base; native USDC and ETH on Arbitrum; native USDC on Polygon.

People use the same product through the web app. The agent surface (scoped keys, MCP, idempotent create and track) is what this entry covers.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Agents are good at preparing payments and bad places to keep money. With send21 an agent creates payment requests and drafts through a scoped API key, and the payment is signed in a wallet the agent does not control." — [send21.io/ai-agent-payments](https://send21.io/ai-agent-payments). send21 also serves people through a web app; see [#255](https://github.com/haoruilee/awesome-agent-native-services/issues/255) |
| **Agent-specific primitive** | Agent proposes, human signs: a scoped key that can create payment requests and drafts but cannot move funds, plus a receiving-address policy where the agent only proposes an address and the owner approves it in the app with a passkey or authenticator code |
| **Autonomy-compatible control plane** | The create, track and reconcile loop runs without a human: `Idempotency-Key` on every create, `reuseOpenForOrder` per order id, status polling and signed webhooks. Signing stays outside the agent by design |
| **M2M integration surface** | REST API with OpenAPI, remote MCP server, signed webhooks, LangChain and Vercel AI SDK packages, `llms.txt` / `llms-full.txt` |
| **Identity / delegation** | Each agent gets its own scoped `s21_` key or OAuth connection, revocable on its own from the owner's API keys page |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Scoped API key** | `drafts:read`, `drafts:write`, `addressbook:read`, `addressbook:write`, `webhooks:manage`. No scope can move funds |
| **Payment request** | Fiat-priced pay link that offers several currencies; the payer scans one standard QR (BIP-21, Solana Pay, EIP-681 or a Lightning invoice) |
| **Draft** | One payment to one receiver. Immutable `core` with `coreSha256` over its RFC 8785 form; a fiat rate lock is a separate `quote` with its own id and `sha256` |
| **Transaction template** | Multi-output template for PSBT wallets, so the operator's own wallet can sign |
| **Approved receiving addresses** | On new accounts, API keys can only use addresses the owner approved; anything else returns 422 `address_not_approved` |
| **Signed webhook** | `X-Send21-Signature-V2: t=<unix>,v1=<hex>` over timestamp, delivery id and raw body; refuse deliveries older than 5 minutes |

---

## Autonomy Model

1. The owner creates a scoped key, or approves an MCP OAuth connection, and approves the receiving addresses.
2. The agent calls `get_account_status` to see what is still missing.
3. The agent calls `create_payment_request` or `create_draft` with an `Idempotency-Key`. The same key with the same request returns the same object; a changed amount, currency or address is refused with 422.
4. The agent hands the pay link or transaction template to whoever holds the funds.
5. The agent waits for `draft.confirmed` (verifying the signature) or polls `get_draft_status`.
6. The agent reconciles on the exact amount, asset, order id and transaction id. A transfer with a different amount raises `draft.amount_mismatch`, and a person decides whether to accept it.

---

## Identity and Delegation Model

- Each agent gets its own `s21_` key or OAuth connection with only the scopes it needs. Keys are shown once and can be revoked one by one.
- No key or scope can move funds, and no key or scope can approve a receiving address.
- An agent without a key can call `create_account` with the owner's email. It gets a bootstrap key at once, but creating anything returns 403 `owner_not_confirmed` until the owner takes the account over from the emailed link (72 hours). Unclaimed accounts are deleted after 7 days.
- Every payment request and draft records amount, asset, rate, rate source and order id. A draft PDF and the quote history (`GET /drafts/{id}/quotes`) serve as the audit trail.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `Authorization: Bearer s21_...`; OpenAPI at https://send21.io/openapi.json; 300 requests per minute per key |
| MCP | `https://send21.io/mcp` (Streamable HTTP, stateless) and `https://send21.io/mcp/oauth` |
| Webhooks | `POST /api/v1/webhooks`; HMAC-SHA256 signatures, up to 8 attempts — [docs](https://send21.io/docs/webhooks) |
| Python | `pip install langchain-send21` |
| TypeScript | `npm install ai-sdk-tool-send21 ai zod` (Vercel AI SDK) |
| Docs | https://send21.io/llms.txt and https://send21.io/llms-full.txt |

---

## Human-in-the-Loop Support

A person, or the operator's own wallet, signs every payment; send21 never signs or broadcasts. The owner approves receiving addresses in the app with a passkey or authenticator code (an emailed code is never enough). A transfer with a different amount waits for the owner to call `POST /drafts/{id}/accept-received`. Each pay link can carry a `declineNote` shown to the payer, and `changeSignals` (`new_address`, `new_asset`, `unusual_amount`) appear on the pay page.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Handing the agent a hot wallet key** | The agent can spend whatever the key controls; there is no scope that creates payments without being able to move funds |
| **Generic crypto checkout plugins** | Built for a shop's checkout page, with no per-agent scoped credential, MCP surface or owner-approved address list |
| **Plain wallet-to-wallet transfers** | No fiat rate lock, order matching, idempotent create or signed confirmation webhook for the agent to reconcile against |

---

## Use Cases

- **Agent invoicing** — an agent creates a fiat-priced pay link for an order and marks it paid only after a verified `draft.confirmed` webhook
- **Payouts prepared by an agent** — an agent prepares drafts or a batch, and the operator signs the transaction template in their own wallet
- **Coding agents building payments** — Claude Code, Cursor or VS Code connect to the MCP server and wire pay links and webhooks into an app
