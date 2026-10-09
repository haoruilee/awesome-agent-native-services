# Veyra

> **"Let your AI agents make payments — with guardrails you control."**

| | |
|---|---|
| **Website** | https://veyra.money |
| **Docs** | https://veyra.money/docs |
| **GitHub** | https://github.com/zapxlabs/veyra-mcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/zapxlabs/veyra-mcp?style=social)](https://github.com/zapxlabs/veyra-mcp) |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **License** | MIT (`veyra-mcp` and `veyra-examples`) |
| **Custody** | Non-custodial. USDC on Base. The owner signs, or grants a capped ERC-20 allowance to a relayer. Veyra states it never asks for a seed phrase |
| **Publisher** | Zapx Labs. The proposal author disclosed that they work on Veyra there |
| **Verified at** | 2026-10-09 |
| **Latest-month signal** | Homepage HTTP 200. `POST https://veyra.money/api/mcp` `initialize` returned server name `veyra`. Pricing page and `llms.txt` agree on Free £0, Pro £19/month, Team £79/month. https://veyra.money |

---

## Official Website

https://veyra.money

---

## Official Repo

https://github.com/zapxlabs/veyra-mcp

Examples: https://github.com/zapxlabs/veyra-examples

Both repositories are MIT. `https://github.com/iykemoney92/veyra-mcp` and `https://github.com/iykemoney92/veyra-examples` redirect (HTTP 301) to these `zapxlabs` URLs. The hosted policy engine is not in either repository. The README says it is not self-hosted today.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `MCP`

An owner signs up at https://veyra.money, connects a wallet or the simulated source, creates an MCP endpoint, and copies a bearer credential that starts with `veyra_`. The agent then calls the hosted endpoint. Policy is enforced on the server.

**Quickest verified path:**

```bash
claude mcp add --transport http veyra https://veyra.money/api/mcp \
  --header "Authorization: Bearer veyra_..."
```

Hosts that cannot send a bearer header use the stdio bridge, which holds the credential locally and relays to the same endpoint:

```json
{
  "mcpServers": {
    "veyra": {
      "command": "npx",
      "args": ["-y", "veyra-mcp"],
      "env": { "VEYRA_TOKEN": "veyra_..." }
    }
  }
}
```

`npx -y veyra-mcp` matches npm `latest` 0.1.1 on 2026-10-09. The registry name in `server.json` is `io.github.zapxlabs/veyra`.

---

## Agent Skills

**Status:** ⚠️ Not yet published

No vendor `SKILL.md` was found in `zapxlabs/veyra-mcp` or `zapxlabs/veyra-examples`.

```bash
npx clawhub@latest search veyra
```

See the [AgentSkills specification](https://agentskills.io/specification) to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Endpoint** | `POST https://veyra.money/api/mcp` |
| **Transport** | Streamable HTTP / JSON-RPC, bearer auth. Unauthenticated `initialize` on 2026-10-09 returned `serverInfo.name` `veyra`, version `0.1.0`. `GET /api/mcp` lists the same tool names and `auth: Bearer <agent_mcp_credential>` |
| **Bridge** | `npx -y veyra-mcp` (stdio). The README says no policy lives in the bridge |
| **Tools** | `get_capabilities`, `get_budget`, `list_payment_sources`, `create_payment`, `get_payment`, `list_payments`, `cancel_payment` |
| **Compatible clients** | Claude Code, Cursor, Codex, Claude Desktop, and any client that can call the remote URL |

`create_payment` arguments documented on the tool schema are `amount`, `asset`, `recipient`, `network`, `reason`, and `idempotency_key`.

---

## What It Does

Veyra is a permission layer between an agent and a wallet the owner already controls. The owner sets per-transaction and daily caps and auto / ask / block bands on one MCP endpoint. The agent gets payment tools. It does not get a seed phrase, a private key, or a raw card.

Under the auto-approve limit, with auto-pay enabled, the owner has granted a capped USDC allowance on Base to a relayer Veyra operates. The docs say the token contract enforces that ceiling, and the relayer pays the recipient from the owner's wallet rather than from a Veyra balance. In the ask band the payment returns `awaiting_approval` and a one-time link the owner opens in their own wallet. Over the ask band or the daily cap, the payment is blocked. An approval nobody acts on lapses after 24 hours.

The simulated source settles as `confirmed_simulated` and moves no money. The docs say plain `confirmed` means value moved on-chain. Assets in production are USDC on Base only.

On 2026-10-09 the [pricing page](https://veyra.money/pricing) and [llms.txt](https://veyra.money/llms.txt) both list Free at £0 (1 endpoint, 2 sources, manual approval on every payment, 7-day audit log), Pro at £19/month (up to 10 endpoints and sources, 90-day audit log, auto-pay up to 500 on-chain payments a month), and Team at £79/month (up to 50 endpoints and sources, 1-year audit log with CSV export, auto-pay up to 2,000 on-chain payments a month). Those plan limits are separate from the dollar caps on an endpoint.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Veyra is a financial permission layer for AI agents." The docs open with "Ship a hosted MCP payment gateway with wallet-backed spend limits." — [veyra.money/docs](https://veyra.money/docs) and [llms.txt](https://veyra.money/llms.txt) |
| **Agent-specific primitive** | One MCP endpoint per agent, with its own bearer, per-transaction and daily caps, auto / ask / block bands, and an optional recipient allowlist. A human card checkout has no per-agent tool credential |
| **Autonomy-compatible control plane** | Payments under the auto-max proceed without a prompt when auto-pay is on, still inside the caps. The ask band holds the payment. Over the limits it fails with a policy reason. The Free plan does not auto-pay: every payment waits for the owner wallet. [Docs](https://veyra.money/docs) |
| **M2M integration surface** | Remote MCP at `https://veyra.money/api/mcp`, stdio bridge and TypeScript client in `veyra-mcp`, examples for a Claude tool runner, the Vercel AI SDK, and raw JSON-RPC |
| **Identity / delegation** | The endpoint credential is separate from the owner account and can be rotated or revoked from the dashboard. Agents never receive keys. The docs say an ERC-20 allowance caps how much the relayer may move, not the destination; the destination inside that cap is Veyra's policy engine, and a recipient allowlist constrains it further |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **MCP endpoint** | One URL and one `veyra_` bearer per agent, with its own limits |
| **Policy bands** | Auto, ask, and block. Documented order: auto-approve ≤ ask ≤ per-payment ≤ daily |
| **Payment statuses** | `pending`, `awaiting_approval`, `submitted`, `confirmed`, `confirmed_simulated`, `failed`, `cancelled`, `expired` |
| **Approval link** | One-time URL for the ask band. The owner signs USDC in their wallet. No Veyra login on that page. Lapses after 24 hours |
| **Capped allowance** | ERC-20 `approve` to the relayer for unattended auto-pay, revocable from the endpoint page |
| **Simulated source** | Instant settlement that moves no funds, labeled `confirmed_simulated` |
| **Audit log** | Policy decisions, settlements, approvals, and permission changes. Retention follows the plan (7 days, 90 days, or 1 year) |

---

## Autonomy Model

1. The owner connects a wallet or the simulated source and creates an endpoint with caps and bands.
2. The agent, holding only that endpoint's bearer, calls `get_budget` or `get_capabilities`.
3. It calls `create_payment` with amount, asset, recipient, network, reason, and an idempotency key.
4. Under the auto-max, with auto-pay and allowance in place, the relayer submits the USDC transfer. The agent reads `confirmed` and, from `get_payment`, a `tx_ref`.
5. In the ask band the agent receives `awaiting_approval` and `next_action.url` and waits. It does not create a second payment to see whether the first worked.
6. Over the caps the call fails with a policy reason.
7. On the simulated source the status is `confirmed_simulated`. The tool text says not to report that as a real payment.

---

## Identity and Delegation Model

- Each agent endpoint has its own credential, separate from the owner's login. The dashboard can rotate or revoke it.
- `list_payment_sources` returns masked sources. The tool text says never to request secrets.
- The owner wallet remains the rail. Veyra's docs say customer funds do not sit in a Veyra balance.
- Auto-pay delegates a capped amount to a relayer, not an uncapped key. The destination inside that cap is the policy engine unless a recipient allowlist is set.
- An empty allowlist means any recipient within the limits. A populated list is exhaustive and compared case-insensitively.
- The audit log attributes each payment to the endpoint, and records allowance grants, policy edits (limits before and after), and credential rotations.
- The wallet-approval path does not delegate signing. The owner signs, and Veyra checks the on-chain receipt.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | `POST https://veyra.money/api/mcp` with `Authorization: Bearer veyra_…` |
| stdio | `npx -y veyra-mcp` and `VEYRA_TOKEN` |
| TypeScript SDK | `npm install veyra-mcp` — `VeyraClient` in the same package |
| Registry | `io.github.zapxlabs/veyra` in [server.json](https://github.com/zapxlabs/veyra-mcp/blob/main/server.json) |
| Docs | https://veyra.money/docs and https://veyra.money/llms.txt |

---

## Human-in-the-Loop Support

The ask band is the human gate: the agent gets a link, the owner approves or rejects in their own wallet, and a ignored link expires in 24 hours. The docs say the owner is emailed and, if enabled, gets a browser push. Above the auto-approve limit, and for every payment on the Free plan, that wallet path is the one that moves money. Auto-pay is the path with no per-payment prompt, bounded by the allowance, the endpoint caps, and the monthly auto-pay count on the plan. Blocked payments stop with a reason the agent can read.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A private key in the agent** | The agent can sign anything. Veyra's endpoint never receives the key, and the cap is on the server and, for auto-pay, on the token allowance |
| **A human card checkout** | A person confirms a charge. There is no per-agent MCP credential, no auto / ask / block band, and no `confirmed_simulated` rail |
| **An uncapped exchange API key** | The key spends until it is revoked. It does not return `awaiting_approval` for one band and a policy reason for another |

---

## Use Cases

- **Pay a known recipient under a cap** — `create_payment` for USDC on Base; the server applies the endpoint policy.
- **Hold a larger payment for the owner** — the ask band returns a one-time wallet link and does not move funds until they sign.
- **Develop without moving money** — attach the simulated source and treat only `confirmed` as a real transfer.
- **Turn one agent off** — rotate or revoke that endpoint's credential without replacing the owner's wallet.
