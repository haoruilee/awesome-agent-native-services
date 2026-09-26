# SecondSign Core

> **"An independent transaction co-signer for AI agents that manage other people's money."**

| | |
|---|---|
| **Website** | https://secondsignruntime.com |
| **Docs** | https://github.com/Bestpart-Irene/secondsign-core#documentation |
| **GitHub** | https://github.com/Bestpart-Irene/secondsign-core |
| **Stars** | [32 stars (snapshot: 2026-09-26)](https://github.com/Bestpart-Irene/secondsign-core) |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Latest-month signal** | Latest release is still [v0.2.0](https://github.com/Bestpart-Irene/secondsign-core/releases/tag/v0.2.0) (2026-08-01); 32 stars; license Apache-2.0; last push 2026-09-04; [secondsignruntime.com](https://secondsignruntime.com) returned HTTP 200 on 2026-09-26 ([repo metadata](https://api.github.com/repos/Bestpart-Irene/secondsign-core)) |
| **Verified at** | 2026-09-26 |
| **Status** | **Pre-1.0 preview.** Interfaces may change; no independent security audit; some gateway control-plane state is not restart-durable. Apache-2.0. |

---

## Official Website

https://secondsignruntime.com

---

## Official Repo

https://github.com/Bestpart-Irene/secondsign-core

---

## How to Use (Agent Onboarding)

Install the engine and run its no-money quickstart through the public API:

```bash
pip install secondsign-core
python examples/quickstart.py
```

The quickstart uses the real `authorize()` / `resolve()` gateway decision path with a mock rail. For the production-faithful two-network topology, use the repository's documented Docker demo:

```bash
git clone https://github.com/Bestpart-Irene/secondsign-core
cd secondsign-core/deploy/reference

python tls/generate.py
docker compose -f compose.yaml -f compose.demo.yaml up --build -d
python demo/run_demo.py
python demo/watch.py
```

The project explicitly warns that importing the library inside the agent's own process is for development/evaluation, not production custody. A real boundary requires the standalone credential-holding gateway and a network topology where the agent cannot reach the payment rail directly.

---

## Agent Skills

**Status:** ⚠️ Not yet published by the project.

```bash
npx clawhub@latest search secondsign
```

See the [AgentSkills specification](https://agentskills.io/specification) to contribute one.

---

## MCP

**Status:** ⚠️ No first-party MCP server is documented. The verified agent surfaces are the Python public API and the standalone gateway's versioned HTTPS authorization protocol.

---

## What It Does

SecondSign Core is a deterministic transaction authorization boundary for financial agents. The agent proposes a structured, immutable intent without raw account or customer data. Policies can only tighten the result to `ALLOW`, `REVIEW`, or `DENY`; reviewed actions receive a one-shot, expiring, proposal-bound human decision; and the execution gateway rechecks the exact intent before dispatching it once with a gateway-derived idempotency key.

The reference deployment separates three trust domains: a credential-free agent client, a gateway that alone holds the rail credential, and an approver on a second mTLS network the agent cannot reach. Redacted receipts form a hash chain. A separate on-chain path can act as one key in a 2-of-2 Safe, but that path is younger, unaudited, and has only run against a local chain.

This is pre-1.0 software, not a production-security endorsement. The official status notes that principal fingerprint data, spend-window state, and pending reviews currently live in process and are forgotten on gateway restart; spending limits are configured as gateway constants rather than state held by an auditable authority.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The project describes itself as an [independent transaction co-signer for AI agents](https://github.com/Bestpart-Irene/secondsign-core#readme) managing money on someone else's behalf. |
| **Agent-specific primitive** | Immutable transaction intent, tightening-only deterministic decision, proposal-bound maker-checker approval, execute-once gateway, and redacted hash-chained receipt sit directly on the agent-to-money path. |
| **Autonomy-compatible control plane** | In-policy requests can execute without human confirmation; policy selects only exceptional `REVIEW` cases, while ambiguous, denied, or unavailable cases fail closed. |
| **M2M integration surface** | Python package/public API plus a standalone HTTPS gateway with a credential-free agent-side wire contract and separate mTLS approval listener. |
| **Identity / delegation** | A client certificate authenticates a workload principal and derives policy scope; the approver uses a separate CA/channel. Receipts record the decision and approver without carrying raw financial data. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **TransactionIntent** | Immutable, fingerprinted, integer-minor-unit proposal with raw account/customer fields excluded |
| **Tightening-only policy** | Multiple rules combine to the strictest result; plugins cannot grant permission core refused |
| **Three-way decision** | `ALLOW`, `REVIEW`, or `DENY`, with closed machine-readable reasons |
| **Maker-checker review** | One-shot, expiring approval bound to the exact proposal rather than an agent/session/action class |
| **Execution gateway** | Re-verifies the decided intent immediately before a single rail dispatch |
| **Gateway idempotency** | Derives the idempotency key internally so the agent cannot choose or replay it as a different action |
| **Audit receipt** | Redacted decision/execution evidence chained by hash so later modification is detectable |
| **Safe co-signer** | Optional 2-of-2 agent-wallet enforcement with live chain-state checks and Solidity integrity guards |

---

## Autonomy Model

1. The agent-side client turns a financial tool call into a versioned structured proposal and sends it to the only reachable gateway route.
2. mTLS authenticates the workload principal; the gateway maps it to policy scope and derives an immutable intent.
3. Deterministic rules combine monotonically: an allowed intent proceeds, a denied intent stops, and a review intent is parked.
4. A human on the separately routed approver network can approve or decline the exact proposal once before expiry.
5. The gateway re-verifies the digest and dispatches exactly once through the credential-holding rail, then returns status and a redacted chained receipt.

If the gateway is unavailable or the request is unclear, the client reports refusal rather than inventing an authorization. For this boundary to be meaningful, disabling SecondSign must also remove the agent's path to the rail.

---

## Identity and Delegation Model

- The agent holds neither the rail credential nor a direct network route to the financial destination in the reference topology.
- Off-loopback gateway access requires mTLS. A workload URI in the client certificate identifies the principal, and an explicit allowlist maps that principal to policy.
- Client leaves are short-lived in the reference design; certificate identity says which workload asked, not whether its request is permissible.
- The approver listener has its own CA, certificate purpose, and network path; agent credentials cannot answer a held review.
- Approval binds to the proposal digest and expires after one use. It does not create a standing grant for the agent.
- Receipts retain fingerprints, verdicts, reasons, approval, and execution outcome while excluding raw account/customer data and credentials.
- Current principal, spend-window, and pending-review state is in memory and is lost at restart. This limitation must be resolved before relying on restart-continuous limits or reviews.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **Python core API** | Contracts, adapters, policies, decisions, maker-checker approval, gateway, audit, and rail adapters |
| **Agent/gateway wire** | Versioned JSON proposal posted to `/authorize`; credential-free client relays the gateway status |
| **Gateway transport** | Loopback for development; mTLS is mandatory when bound off-loopback |
| **Approver transport** | Separate mTLS HTTP listener for listing/resolving held proposals |
| **Rail adapters** | Stripe extra, Alpaca path, generic HTTP executor, and reference mock rail documented upstream |
| **On-chain** | Safe co-signer, provider-held signing key, live chain-state verification, and Solidity transaction/module guards |
| **MCP** | No first-party server verified |

---

## Human-in-the-Loop Support

Policy decides which requests require a second human. A `REVIEW` is parked and shown over a separate mTLS approver channel that the agent cannot reach. Approval or decline applies once to the exact proposal and expires; the gateway rechecks the request at dispatch.

The preview's pending-review store is currently in memory, so a gateway restart forgets unresolved reviews. The approval UI and topology are implemented and tested, but they are not a restart-durable production workflow yet.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Payment SDK inside the agent process** | Gives the agent or its dependency graph the credential and lets it bypass any voluntary safety call. |
| **Prompt rule or model-based guard** | Runs inside the same decision-maker and can be skipped, injected, or behave nondeterministically. |
| **Human checkout confirmation** | Assumes a person initiates every payment instead of allowing bounded autonomous execution with selective review. |
| **Operator-written application logs** | Are produced by the same system being audited and do not provide an independent co-signing boundary or tamper-detectable verdict chain. |

---

## Use Cases

- **Treasury agent** — enforce value, counterparty, time-window, and review policies before client funds move
- **Agentic commerce** — allow routine merchant payments while escalating unusual beneficiaries or amounts
- **Trading agent** — keep broker credentials behind a deterministic gateway and attribute each authorized action
- **Enterprise agent product** — provide a separable pre-dispatch control for customers who will not expose payment credentials to a model runtime
- **Agent-owned Safe** — require a SecondSign co-signature and block unauthorized account-control mutations on both Safe execution paths
