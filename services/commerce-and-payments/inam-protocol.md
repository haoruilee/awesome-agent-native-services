# INAM Protocol

> **"Check an AI agent or x402 seller before you pay it."**

| | |
|---|---|
| **Website** | https://inamprotocol.org |
| **Docs** | https://docs.inamprotocol.org (spec + API reference from `openapi.yaml`) and https://inamprotocol.org/llms.txt |
| **GitHub** | https://github.com/inamprotocol/inam-protocol |
| **Stars** | [1 star (snapshot: 2026-10-13)](https://github.com/inamprotocol/inam-protocol) |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **License** | Apache-2.0 |
| **Contact** | hello@inamprotocol.org |
| **Publisher** | INAM Protocol. The proposal author disclosed in [issue #195](https://github.com/haoruilee/awesome-agent-native-services/issues/195) that they maintain INAM Protocol |
| **Verified at** | 2026-10-13 |
| **Latest-month signal** | `GET https://api.inamprotocol.org/v1/health` returned `status: ok`, registry `0.12.0`, spec `0.42`, MCP `0.6.0`. `GET https://api.inamprotocol.org/v1/transparency/sth` returned tree size 12. MCP `initialize` on `POST https://api.inamprotocol.org/mcp` returned server name `inam-mcp`, version `0.6.0`. npm `inamprotocol` 0.21.0, PyPI `inamprotocol` 0.13.0 |
| **Status** | **Early-stage.** Launched August 2026, spec is a draft (v0.42), little outside usage so far (12 finalized receipts in the public log on 2026-10-13). Stake is in the data model but cannot be posted yet. |

---

## Official Website

https://inamprotocol.org

API host: https://api.inamprotocol.org. Explorer: https://explorer.inamprotocol.org

---

## Official Repo

https://github.com/inamprotocol/inam-protocol (registry reference server, Cloudflare Worker deployment, TypeScript and Python SDKs, MCP server, `SPEC.md`, `openapi.yaml`)

---

## How to Use (Agent Onboarding)

**Interaction pattern:** HTTP, CLI and MCP

**Quickest verified path (free, no account or key):**

```bash
curl 'https://api.inamprotocol.org/v1/check?target=<x402 endpoint URL | 0x wallet | did:key>'
```

Same check from the CLI:

```bash
npx inamprotocol check https://x402.coinstats.app/markets
```

It returns `PASS`, `CAUTION` or `FAIL` from the x402 payment requirements, ERC-8004 identity and feedback, INAM receipts, the Web Bot Auth key directory and domain age. The hosted response is cached for 10 minutes.

**MCP (read-only, no auth):** `claude mcp add --transport http inam https://api.inamprotocol.org/mcp`

**Give an agent an identity and record work (TypeScript SDK):**

```js
import { InamClient, generateKeypair } from "inamprotocol";
const client = new InamClient("https://api.inamprotocol.org", generateKeypair());
const profile = await client.registerAgent(["document-extraction"]);
const reputation = await client.getReputation(profile.id);
```

Gate an x402 payment on INAM evidence: `withInamX402Gate(fetch, client, { minEvidence: "countersigned" })` ([example](https://github.com/inamprotocol/inam-protocol/blob/main/examples/x402-verify-before-pay.ts)). Python: `pip install inamprotocol`.

---

## Agent Skills

**Status:** ⚠️ Not yet published as an `npx skills` package

The Claude Code plugin bundle in the repository ships one skill:

```
/plugin marketplace add inamprotocol/inam-protocol
/plugin install inam-protocol@inam-protocol-plugins
```

| Skill | What It Teaches the Agent |
|---|---|
| `inam-protocol` | Look up an agent's reputation and receipt history before hiring or paying it, find agents by capability, run a demo job/receipt cycle, register an agent identity |

Search community skills: `npx clawhub@latest search inam`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Endpoint** | `POST https://api.inamprotocol.org/mcp` (hosted, read-only) |
| **Transport** | Streamable HTTP / JSON-RPC, no auth. Unauthenticated `initialize` on 2026-10-13 returned `serverInfo.name` `inam-mcp`, version `0.6.0` |
| **Local server** | `npx -y inam-mcp` (stdio). Read-only by default; pass `INAM_PRIVATE_KEY` to register and sign receipts as the agent |
| **Tools (hosted)** | `inam_check`, `inam_check_reputation`, `inam_search_agents`, `inam_get_receipt`, `inam_verify_receipt`, `inam_hash_content` |
| **Registry** | Official MCP Registry id `io.github.inamprotocol/inam-mcp` |
| **Compatible clients** | Claude Code, Claude Desktop, Cursor, Gemini CLI (extension), and any client that can call a remote MCP URL |

---

## What It Does

INAM Protocol is an open reputation layer for AI agents. After a job, both agents sign an Execution Receipt with their `did:key` (Ed25519) keys; finalized receipts are appended to an RFC 6962-style Merkle transparency log, and an agent's reputation is computed only from those receipts. Every reputation reports an `evidenceLevel` (`none`, `countersigned`, or `independently_verified`).

On the payment side, an agent can check an x402 seller, a `0x` wallet or a `did:key` before paying, either through the free hosted check or by wrapping its x402 fetch so a payment only goes out if the payee's INAM ID proved control of the `payTo` wallet and has countersigned work.

INAM is not an identity or authorization system (it links to AgentPass, AITP, ERC-8004 and similar) and not a messaging protocol. The project is early: the spec is a draft, there is one live independent verifier (an integrity check, not a correctness check), and stake cannot yet be posted.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Check an AI agent or x402 seller before you pay it." and "INAM is: a reputation layer for AI agents" — [inamprotocol.org](https://inamprotocol.org) |
| **Agent-specific primitive** | Two-party signed Execution Receipt between agents' `did:key` identities; evidence-level reputation computed only from receipts; x402 `payTo` wallet binding check (`withInamX402Gate`) |
| **Autonomy-compatible control plane** | The agent looks up the counterparty, pays or refuses via a code-level gate, records a receipt, and the counterparty countersigns, with no human step. Unanchored counterparties lend no reputation weight |
| **M2M integration surface** | REST API (`/v1`, OpenAPI), hosted check, remote MCP, A2A endpoint and agent card, npm `inamprotocol` / `inam-mcp`, PyPI `inamprotocol`; the explorer is optional |
| **Identity / delegation** | The agent's key is separate from its operator; verifiers count only when the registry operator authorizes them; every receipt is signed by both parties, logged, and verifiable offline from `did:key` |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **INAM ID (`did:key`)** | Self-certifying agent identity derived from an Ed25519 public key; can be linked to ERC-8004, AgentPass, AITP or Passport IDs through a proof-of-control challenge |
| **Execution Receipt** | Content-addressed record of one completed interaction, signed by both agents; can be disputed |
| **Reputation** | Counterparty-weighted, time-decayed trust score with an `evidenceLevel`; demo receipts never count |
| **Verification** | Signed verdict on a finalized receipt from an operator-authorized verifier; a rejection scores as a failure |
| **Transparency log** | RFC 6962-style Merkle log of finalized receipts with inclusion and consistency proofs; an external monitor checks tree heads hourly |
| **Pre-payment check** | `PASS` / `CAUTION` / `FAIL` for an x402 endpoint, wallet or `did:key`, and `withInamX402Gate` for gating payments in code |

---

## Autonomy Model

1. The agent is about to pay or hire a counterparty (x402 endpoint, wallet or `did:key`).
2. It calls the check (HTTP, MCP `inam_check`, A2A skill `check`, or the SDK gate).
3. Its own policy decides: pay, escrow or refuse (`checkTrust()` returns allow / escrow / deny; thresholds are the agent's).
4. After the work, the provider submits a signed receipt draft and the requester countersigns it.
5. The finalized receipt is appended to the transparency log and feeds both agents' reputation.
6. An operator-authorized verifier may attest the receipt; either party may dispute it.

---

## Identity and Delegation Model

- Each agent holds its own Ed25519 key; its INAM ID is the `did:key` of that key, separate from the operator.
- External identities (ERC-8004, AgentPass, AITP, Passport) are linked only after a signed proof-of-control challenge.
- Verifier status is granted by the registry operator, not self-service; `provider != verifier` is enforced.
- Every receipt carries both parties' signatures and verifies offline; the Merkle log makes the history tamper-evident.
- An INAM ID can be retired by its own key (one-way revoke).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Hosted check | `GET https://api.inamprotocol.org/v1/check?target=<url \| 0x wallet \| did:key>` |
| CLI | `npx inamprotocol check <target>` |
| REST API | `https://api.inamprotocol.org/v1` (agents, jobs, receipts, verifications, transparency); spec in [`openapi.yaml`](https://github.com/inamprotocol/inam-protocol/blob/main/openapi.yaml) |
| Transparency log | `GET /v1/transparency/sth`, `/entries`, `/proof/inclusion`, `/proof/consistency` |
| MCP | Hosted `https://api.inamprotocol.org/mcp` (read-only); local `npx -y inam-mcp` |
| A2A | Agent card `https://api.inamprotocol.org/.well-known/agent-card.json`, JSON-RPC at `https://api.inamprotocol.org/a2a` |
| SDKs | npm `inamprotocol` (TypeScript), PyPI `inamprotocol` (Python) |

---

## Human-in-the-Loop Support

None is required in the check, payment-gate or receipt loop. A human operator sets the gate thresholds in code and, for a self-hosted registry, authorizes verifiers. The explorer (https://explorer.inamprotocol.org) and the hosted check let a human read the same evidence an agent saw. Disputes are filed by the agents through signed requests.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Review / rating sites** | Ratings are written by people about a business, are not tied to a specific completed job, and cannot be checked by the paying agent at payment time |
| **Self-reported trust score APIs** | A score with no underlying signed evidence; INAM only counts work both agents signed |
| **Identity registries alone (ERC-8004, DIDs)** | Say an agent is registered, not whether it delivered; nothing binds the identity to the x402 `payTo` wallet being paid |

---

## Use Cases

- **Pre-payment check** — check an x402 seller or wallet before the agent signs a payment.
- **Gate x402 payments** — wrap fetch so payments only go to payees with a proven `payTo` binding and countersigned work.
- **Hiring another agent** — look up a `did:key`'s reputation and receipt history before delegating a job.
- **Portable track record** — give an agent a `did:key` identity and accumulate countersigned receipts it can show anywhere.
