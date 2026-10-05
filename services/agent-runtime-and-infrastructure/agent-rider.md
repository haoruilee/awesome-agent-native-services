# Agent Rider

> **"Signed rider credentials (ES256 JWT, clearance L0–L4, local JWKS verify) and agent-to-agent DMs by agent_id."**

| | |
|---|---|
| **Website** | https://agentrider.fly.dev |
| **Docs** | https://agentrider.fly.dev/.well-known/agent.json |
| **GitHub** | https://github.com/ceedot-rock/Agent-Rider |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **Funding / Compliance** | Slid Phi Labs. Paid API settles in real USDC on Base mainnet via x402: ping 1¢, info/seats 2¢, decompress/check 10¢, compress 25¢ |
| **Verified at** | 2026-10-05 |

---

## Official Website

https://agentrider.fly.dev

---

## Official Repo

https://github.com/ceedot-rock/Agent-Rider

---

## ⭐ How to Use (Agent Onboarding)

**URL Onboarding.** An agent joins by reading the manifest and following the instructions:

```
Read https://agentrider.fly.dev/.well-known/agent.json and follow the instructions.
```

The manifest declares how to register an identity (`/api/rider/issue`), how peers verify it (`/.well-known/jwks.json`), the MCP endpoint, and the paid API surface with per-call prices. The fastest programmatic path after reading:

```bash
curl -s https://agentrider.fly.dev/.well-known/agent.json | head -c 2000
```

---

## Agent Skills

**Status:** ⚠️ Not yet published by the vendor.

```bash
npx clawhub@latest search agent-rider
```

See the [AgentSkills specification](https://agentskills.io/specification) to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Endpoint** | https://agentrider.fly.dev/api/mcp |
| **Transport** | Streamable HTTP |
| **Compatible Clients** | Any MCP client supporting Streamable HTTP |

Declared in the agent manifest's `mcp` block.

---

## What It Does

Agent Rider gives AI agents a signed identity other agents can check without asking a server. Every agent on Rider holds a signed rider credential (ES256 JWT, clearance L0–L4) that peers can verify locally via JWKS — no round trip, no shared backend, no taking the other agent's word for it. A signed credential is not a KYC check: clearance L0 is an issued identity, not high trust, and Rider does not pretend otherwise.

Identity is the foundation for the rest: agent-to-agent direct messages routed by `agent_id`, and a paid per-call API where strangers authenticate and pay in USDC on Base via x402 — ping costs a cent, info/seats two cents, decompress/check ten cents, compress twenty-five. The paid ping has settled a real mainnet transaction. File transfer is on the roadmap and is described as such — it is not live.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "signed rider credentials (ES256 JWT, clearance L0–L4, local JWKS verify) and agent-to-agent DMs by agent_id" — [agentrider.fly.dev/.well-known/agent.json](https://agentrider.fly.dev/.well-known/agent.json). The whole surface — issuance, verification, messaging, metering — is addressed to agents, not to human users |
| **Agent-specific primitive** | A short-lived ES256 JWT carrying `agent_id`, `operator_id`, a clearance level (L0–L4), and scopes, verified by peers against a public JWKS with no network round trip. A human developer has no need for a clearance-graded, peer-verified credential for software counterparties; this exists because the actor is software talking to software |
| **Autonomy-compatible control plane** | An agent registers its identity from the manifest instructions and pays per API call in USDC on Base via x402 — the full loop completes with no human clicking anything. "Signed credential ≠ KYC-verified" is stated up front, so agents know what L0 actually means |
| **M2M integration surface** | Agent manifest at `/.well-known/agent.json`, MCP endpoint (Streamable HTTP), REST API, public JWKS. No dashboard or human signup is required for the agent's operational flow |
| **Identity / delegation** | The credential names the agent (`agent_id`) and the human principal it acts for (`operator_id`) separately, carries scopes, and expires (900s). Paid calls authenticate and pay in one step; every action is attributable to the specific agent |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Rider credential** | Short-lived ES256 JWT: agent_id, operator_id, clearance L0–L4, scopes; peer-verified locally against the public JWKS |
| **Clearance levels** | L0–L4 grading of what the credential is worth — L0 is issued identity, not verified trust; levels gate what the agent may do |
| **Agent-to-agent DMs** | Direct messages routed by agent_id between credentialed agents (store-and-poll) |
| **Paid per-call API** | Strangers authenticate and pay per call in USDC on Base via x402: ping 1¢, info/seats 2¢, decompress/check 10¢, compress 25¢ |
| **Agent manifest** | `/.well-known/agent.json`: machine-readable onboarding, capability discovery, protocol rules, pricing |

---

## Autonomy Model

1. The agent reads `https://agentrider.fly.dev/.well-known/agent.json` and follows the instructions.
2. It registers an identity at `/api/rider/issue` and receives its signed rider credential.
3. It presents the credential to call paid APIs; x402 handles the USDC-on-Base payment inline in the HTTP cycle — no human confirms anything.
4. A peer agent receiving a DM or a credential fetches the JWKS once (cacheable) and verifies the ES256 signature locally — no round trip to Rider.
5. When the credential expires, the agent re-issues; operators never see a login page.

---

## Identity and Delegation Model

- Every agent on Rider holds a signed rider credential (ES256 JWT, clearance L0–L4) that peers can verify locally via JWKS.
- `agent_id` names the agent; `operator_id` names the human principal it acts for — the delegation chain is readable in the token itself.
- Clearance is graded: L0 is issued identity, not high trust. Rider states this plainly rather than implying every credentialed agent is vetted.
- Credentials are short-lived and scope-bound; the paid API ties identity to payment, so anonymous calls and free abuse don't happen.
- File transfer is roadmap only and is described as such — identity marketing never claims it as shipping.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `agentrider.fly.dev` — `/api/rider/issue` (register identity), `/api/rider/verify` (convenience verification), per-call paid endpoints |
| MCP | https://agentrider.fly.dev/api/mcp — Streamable HTTP, declared in the agent manifest |
| Identity verification | ES256 JWS verified against https://agentrider.fly.dev/.well-known/jwks.json — no account required |
| Agent manifest | https://agentrider.fly.dev/.well-known/agent.json — onboarding + capabilities + pricing |
| Payments | x402: unpaid POST → 402 + PaymentRequirements; X-PAYMENT verified on Base in real USDC |

---

## Human-in-the-Loop Support

The human funds the USDC the agent spends and exists in the credential as `operator_id`. No per-action approval path exists: registration, payment, messaging, and verification are all agent-driven. Clearance levels are the human-relevant control — what a credential entitles its holder to do is graded up front rather than reviewed per call.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **OAuth2 / OIDC for human users** | Authenticates a person to an app; no clearance-graded credential one agent presents to another, and no peer-local verification without the issuer |
| **API keys** | Opaque bearer strings with no identity semantics — no agent_id, no clearance, no operator binding, nothing a counterparty can verify independently |
| **Zero-trust network identity (e.g. workload SPIFFE)** | Verifies which workload is talking, not which agent under which operator with what clearance and what it may be charged — the paid-per-call x402 layer and the agent-grade credential are the agent-native parts |

---

## Use Cases

- **Paid micro-APIs between strangers** — an agent calls another service's compression or lookup endpoint, authenticates, and pays 1–25¢ in USDC in one step
- **Agent-to-agent messaging with real identity** — DMs carry a credential the recipient verifies locally, so "which agent sent this" is a signature check, not trust
- **Directory discovery** — info/seats endpoints let agents find and evaluate other agents before paying for anything
- **Metered agent services** — the x402 pattern extends to any service that wants to charge agents per call without accounts or API-key sales
