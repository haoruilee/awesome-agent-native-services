# 402xAgent

> **"The check an agent calls before paying any x402 endpoint."**

| | |
|---|---|
| **Website** | https://402xagent.com |
| **Docs** | https://402xagent.com/llms.txt and https://api.402xagent.com/openapi.json |
| **GitHub** | https://github.com/withgrokbot/x402-spotcheck (fetch wrapper); service issues https://github.com/withgrokbot/verified-catalog/issues |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Publisher** | withgrokbot. The proposal author disclosed that withgrokbot builds and operates 402xAgent ([issue #205](https://github.com/haoruilee/awesome-agent-native-services/issues/205#issuecomment-6127256522)) |
| **Verified at** | 2026-10-13 |
| **Latest-month signal** | `GET https://api.402xagent.com/health` returned `{"ok":true,"version":"0.26.1"}`. Free check example `GET https://api.402xagent.com/v1/products/endpoint-spot-check?url=https://api.402rates.com/v1/ping` returned `verdict: pay` with receipt `https://402xagent.com/v1/receipts/sc-1373dc485641b938`. MCP `initialize` on `POST https://api.402xagent.com/mcp` returned server name `402xagent`, version `0.26.1`. |

---

## Official Website

https://402xagent.com

API host: https://api.402xagent.com (same routes). Older host https://verified-catalog-lookup.withgrokbot.workers.dev still answers.

---

## Official Repo

Fetch wrapper (drop-in for `@x402/fetch` / `@x402/axios`): https://github.com/withgrokbot/x402-spotcheck

Service issues: https://github.com/withgrokbot/verified-catalog/issues

---

## How to Use (Agent Onboarding)

**Interaction pattern:** HTTP and MCP

**Quickest verified path (free, 1 check per client per UTC day):**

```bash
curl 'https://api.402xagent.com/v1/products/endpoint-spot-check?url=<endpoint>'
```

Real example:

```bash
curl 'https://api.402xagent.com/v1/products/endpoint-spot-check?url=https://api.402rates.com/v1/ping'
```

Example response shape:

```json
{"verdict":"pay","reason":"listed $0.001, payment request matches, details locked","receipt_url":"https://402xagent.com/v1/receipts/sc-1373dc485641b938"}
```

Free dry run (same path): add `&mode=dry-run`. Prior public checks: https://402xagent.com/v1/skips (JSON: https://402xagent.com/v1/skips.json). After the free quota, the same path answers HTTP 402; the paid check ($0.01 to $0.25 USDC on Base via x402, one tenth of the target's quoted price) adds the full payment terms. 402xAgent never pays the URL under test.

**MCP:** `POST https://api.402xagent.com/mcp` (no API key for free tools).

**Drop-in guard for x402 clients:**

```js
const pay = wrapFetchWithPayment(spotCheckFetch(fetch), client);
```

From https://github.com/withgrokbot/x402-spotcheck (blocks the payment when the check says `skip`).

---

## Agent Skills

**Status:** Not yet published

No vendor `SKILL.md` was found for 402xAgent. Onboarding today is URL + OpenAPI + MCP + the fetch wrapper above.

See the [AgentSkills specification](https://agentskills.io/specification) to contribute one.

---

## MCP

**Status:** Available

| Detail | Value |
|---|---|
| **Endpoint** | `POST https://api.402xagent.com/mcp` |
| **Transport** | Streamable HTTP / JSON-RPC. Unauthenticated `initialize` on 2026-10-13 returned `serverInfo.name` `402xagent`, version `0.26.1` |
| **Tools** | `endpoint_spot_check`, `search_catalog`, `get_service`, and related catalog/lookup tools exposed on the same MCP server |
| **Compatible clients** | Any client that can call a remote MCP URL (Cursor, Claude, Codex, and similar) |

---

## What It Does

402xAgent is the check an agent calls right before paying an x402 endpoint. It probes the endpoint's 402 payment request without paying, compares it to what the listing said, and returns `pay`, `skip`, or `recheck` with a plain reason plus a public receipt URL. The paid tier adds the exact payment terms (network, asset, pay_to, scheme, quoted price) a router may sign. It never pays the target.

Public surfaces for discovery and audit: skips list https://402xagent.com/v1/skips, receipts https://402xagent.com/v1/receipts, Bazaar sample https://402xagent.com/bazaar, OpenAPI https://api.402xagent.com/openapi.json, and `/.well-known/x402`.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "The check an agent calls before paying any x402 endpoint." Home, `llms.txt`, and OpenAPI open on the free pre-pay check, not a human checkout |
| **Agent-specific primitive** | Unpaid 402 probe + machine-readable `pay` / `skip` / `recheck` verdict an agent can gate signing on, plus a public receipt URL for audit |
| **Autonomy-compatible control plane** | Free check returns a verdict without a human. `skip` is a hard stop for the fetch wrapper. `recheck` tells the agent to try again. Paid check returns signable terms for routers |
| **M2M integration surface** | HTTP GET, remote MCP, OpenAPI, and a one-line wrapper for `@x402/fetch` / `@x402/axios` |
| **Identity / delegation** | No seed phrase, private key, or card is taken. The check never pays the target; the agent's own wallet or facilitator remains the rail for any later payment |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Unpaid 402 probe** | Reads the endpoint's 402 payment requirements without spending the caller's funds |
| **Verdict** | `pay`, `skip`, or `recheck`, with a plain-language reason |
| **Public receipt** | Timestamped receipt URL per check (`/v1/receipts/sc-<id>`), also listed on `/v1/skips` and `/v1/receipts` |
| **Payment-object handoff** | Paid tier returns the exact terms a router may sign (including Base and Solana CAIP-2 where supported) |
| **Drop-in guard** | `spotCheckFetch` wrapper that blocks payment when the verdict is `skip` |

---

## Autonomy Model

1. The agent (or router) is about to pay an x402 endpoint URL.
2. It calls the free check with that URL (HTTP or MCP `endpoint_spot_check`), or uses the fetch wrapper so the check runs before signing.
3. On `pay`, it may proceed to pay the target with its own wallet or facilitator.
4. On `skip`, it aborts that payment (the wrapper blocks signing).
5. On `recheck`, it retries later rather than treating the answer as a permanent skip.
6. If it needs the full payment terms after the free quota, it settles the 402xAgent paid check (USDC on Base via x402). That payment buys the terms object only; it still never pays the URL under test.
7. Every check leaves a public receipt the agent can cite.

---

## Identity and Delegation Model

- Callers identify as x402 clients (client key / free quota). There is no owner dashboard credential for the free check.
- 402xAgent never receives a seed phrase, private key, or card.
- The check does not move funds to the target. Any later payment to the target stays with the agent's own wallet, facilitator, or policy layer.
- Public receipts are the audit trail: URL, verdict, reason, and check metadata, free to read.
- Disclosure: withgrokbot builds and operates the service (see issue #205 comment).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP free check | `GET https://api.402xagent.com/v1/products/endpoint-spot-check?url=<endpoint>` |
| HTTP dry run | same path with `&mode=dry-run` |
| MCP | `POST https://api.402xagent.com/mcp` |
| Fetch wrapper | https://github.com/withgrokbot/x402-spotcheck |
| Skips / receipts | https://402xagent.com/v1/skips , https://402xagent.com/v1/receipts |
| OpenAPI | https://api.402xagent.com/openapi.json |
| Discovery card | https://api.402xagent.com/.well-known/x402 |

---

## Human-in-the-Loop Support

The free and paid checks are built for autonomous callers: a verdict and reason with no human prompt. Humans can open the same URLs in a browser (home page, skips page, receipt URLs) to inspect what an agent saw. There is no owner-approval band inside 402xAgent itself; if a human gate is required, that sits in the agent's own wallet policy or a separate payment permission layer. Dry-run mode (`mode=dry-run`) lets a human or agent rehearse the same verdict path without consuming the free paid-quota slot the same way a live free check does.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Paying the endpoint to "see if it works"** | Spends the agent's funds on a bad listing. 402xAgent probes without paying the target |
| **Reading the listing HTML alone** | Listings drift (wrong network, wrong wallet, wrong price). The check compares listing to the live 402 |
| **A human browsing the seller's docs** | No machine-readable `pay` / `skip` / `recheck`, no public receipt, no MCP or fetch-wrapper hook for routers |

---

## Use Cases

- **Gate a payment** — call the free check; only sign when verdict is `pay`.
- **Block a bad sell** — on `skip`, refuse the payment and keep the reason/receipt.
- **Router preflight** — wrap `@x402/fetch` / `@x402/axios` so every outgoing payment is checked first.
- **Audit / discovery** — read `/v1/skips` and `/v1/receipts` (and `/bazaar`) for public, redacted prior checks without calling the sellers again.
