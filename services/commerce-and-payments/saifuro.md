# Saifuro

> **"The financial OS for the AI agent economy."**

| | |
|---|---|
| **Website** | https://saifuro.com |
| **Docs** | https://docs.saifuro.com |
| **GitHub** | None — no public repository; the TypeScript SDK is private and issued at onboarding |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |
| **Funding / Compliance** | Non-custodial by design: customer funds are never held, and card data is tokenized by VGS before it reaches Saifuro. Settlement is executed by the customer's own licensed payment providers |
| **Verified at** | 2026-10-05 |
| **Status** | **Closed access.** Keys are issued per organization at onboarding; there is no public sandbox signup, because the product authorizes spending on behalf of a paying organization. Escrow is simulated in the sandbox. Documented gaps are maintained by the vendor at [Known gaps](https://docs.saifuro.com/reference/not-built-yet) |

---

## Official Website

https://saifuro.com

---

## Official Repo

No public repository. The REST API at `api.saifuro.com` is the integration surface, documented at [docs.saifuro.com](https://docs.saifuro.com); the TypeScript SDK is private and issued with the keys at onboarding. The one artifact that needs no account is the verdict key set: https://verdicts.saifuro.com/.well-known/jwks.json

---

## How to Use (Agent Onboarding)

**SDK / REST.** Keys are issued per organization at onboarding — request access at [saifuro.com](https://saifuro.com) — and arrive in two classes: an org key (`sk_`) that writes policy, and per-agent keys (`ak_`) that may only ask for authorization. The first call from the agent's own key:

```bash
curl -s https://api.saifuro.com/v1/authorizations \
  -H "Authorization: Bearer $SAIFURO_AGENT_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "amount": 120.00, "currency": "USD", "recipient": "vendor:acme_saas", "category": "saas" }'
```

The response carries a verdict and a `verdict_token`. The full loop — write a mandate, ask to spend, read the verdict, then force a denial, a review and a revocation — is [first authorization](https://docs.saifuro.com/guides/first-authorization); forcing each of the eight decision codes on purpose is [sandbox](https://docs.saifuro.com/guides/sandbox).

A counterparty that is handed a `verdict_token` needs no account to check it: see [verifying a verdict](https://docs.saifuro.com/reference/verify-a-verdict). Verdicts expire five minutes after issue, so verify a fresh one.

---

## Agent Skills

**Status:** ⚠️ Not yet published by the vendor.

```bash
npx clawhub@latest search saifuro
```

See the [AgentSkills specification](https://agentskills.io/specification) to contribute one.

---

## MCP

**Status:** ⚠️ No first-party MCP server is documented. The verified agent surface is the versioned REST API plus webhooks; the private TypeScript SDK wraps the same endpoints.

---

## What It Does

Saifuro is an authorization layer that sits between an organization's agents and its payment providers. The operator writes a mandate per agent — who the agent acts for, how much it may spend per transaction and per month, in which categories, above which amount a human must approve, and when the mandate expires. Every spend request is evaluated against that mandate synchronously, before money moves, and the answer is one of eight decision codes carried in a signed token.

The signature is the part that makes this usable between two parties that do not share a backend. A verdict is an ES256 JWT bound to the request that produced it — amount, recipient, mandate, policy version and a nonce are covered by the signature — so a seller's agent can verify that the buyer's agent was actually authorized for this amount, offline, against a public JWKS, without an account and without taking the buyer's word for it. Every decision, whatever the verdict, lands in an append-only log that exports as NDJSON.

Saifuro is deliberately not in the money path: it holds no customer funds, takes no custody, and routes settlement through the customer's own licensed providers. For conditional agent-to-agent deals it deploys escrow contracts on Base and Solana settling in USDC, where the funds sit in the contract rather than with Saifuro — in the sandbox those escrows are simulated rather than deployed.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Saifuro is B2B financial infrastructure for AI agent payments. It sits between your agents and your payment providers. You define what each agent may spend, on what, under whose authority, and within which limits." — [docs.saifuro.com](https://docs.saifuro.com) |
| **Agent-specific primitive** | A mandate bound to one agent identity, plus a per-request signed verdict. A human paying with their own card has no delegated mandate to check and no need for a signed record of who authorized them; this exists because the spender is software acting on someone else's authority. [API reference](https://docs.saifuro.com/api/authorizations) |
| **Autonomy-compatible control plane** | Inside its mandate the agent receives `allow` and proceeds with no human in the loop. Only requests above the mandate's `review_above` threshold produce `review`, and the decision names the identity it waits for. [Decision codes](https://docs.saifuro.com/concepts/decision-codes) |
| **M2M integration surface** | Versioned REST API at `api.saifuro.com`, webhooks per state change, NDJSON decision export, public JWKS for offline verdict verification, private TypeScript SDK. No console is required to operate it. |
| **Identity / delegation** | Credentials are issued per agent, not per installation, so a mandate attaches to an identity rather than to a name in a request body. Agent keys cannot write policy; mandates name the human principal the agent acts for and are revocable, taking effect on the next request. [Security model](https://docs.saifuro.com/reference/security) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Mandate** | Per-agent spending authority: principal, per-transaction and monthly limits, allowed categories, `review_above` threshold, expiry, revocation |
| **Signed verdict** | ES256 JWT bound to amount, recipient, mandate, policy version and nonce; short expiry; verifiable offline against the public JWKS |
| **Eight decision codes** | `allow`, `review`, `deny_limit`, `deny_category`, `deny_velocity`, `deny_expired`, `deny_revoked`, `deny_no_mandate` |
| **Observe mode** | Enforcement switch that evaluates and records every request without blocking any, so a policy can be measured on real traffic before it denies anything; the mode in force is stamped on each decision |
| **Append-only decision log** | Every evaluated request recorded and exported as NDJSON, identity and decision joined per transaction |
| **Escrow** | Conditional deals as contracts on Base and Solana settling in USDC, funds held by the contract and not by Saifuro; simulated in the sandbox |

---

## Autonomy Model

1. The operator creates an agent and a mandate once, with the org key.
2. The agent, holding only its own `ak_` key, calls `POST /v1/authorizations` with amount, currency, recipient and category before paying.
3. The engine evaluates the request against the mandate and returns a verdict with a `verdict_token`, synchronously, in the transaction path.
4. On `allow` the agent proceeds to its payment provider and presents the token; no human is involved at any point.
5. On a `deny_*` code the agent stops and reads the reason, which names the rule that refused it.
6. On `review` the decision names the identity whose approval it waits for; the agent polls or waits for the webhook.
7. The seller's agent verifies the token against the public JWKS, offline, and keeps it as evidence of what was authorized.

---

## Identity and Delegation Model

- Credentials are issued per agent at onboarding, not per installation, so an agent authenticates as itself and a mandate attaches to an identity rather than to a name in a request body.
- Two key classes with different powers: org keys (`sk_`) write policy and resolve reviews; agent keys (`ak_`) may only request authorization. An agent key attempting to write a mandate is refused.
- A mandate names the human principal the agent spends on behalf of, which is what makes the delegation chain readable after the fact.
- Mandates are revocable and expire; revocation takes effect on the next request.
- Every decision is appended to an immutable log with the policy version and the enforcement mode in force; corrections are new records, never edits.
- Verdicts are signed, not booleans: an approval for one purchase cannot be replayed for a second one, reused at a larger amount, or edited in transit.
- Sandbox verdicts are distinguishable by a `kid` beginning with `sandbox-`, so a counterparty delivering real goods can reject them.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `api.saifuro.com`, versioned; `/v1/authorizations`, `/v1/mandates`, `/v1/agents`, `/v1/decisions`, `/v1/escrows`, `/v1/reviews/{id}/approve`, `/v1/enforcement`, `/v1/usage`, `/v1/exports`, `/v1/webhooks` |
| Verdict verification | ES256 JWS verified against https://verdicts.saifuro.com/.well-known/jwks.json — no account required |
| Webhooks | Per state change, including `escrow.funded`, `escrow.released`, `escrow.refunded` and review events |
| Exports | NDJSON decision stream, one record per evaluated request, including the `verdict_token` |
| SDK | Private TypeScript SDK issued at onboarding; the npm package name is a reservation, not a published library |
| MCP | ⚠️ None documented |
| Payment rails | Positioned as one integration across x402, MPP, ACP, AP2 and the card agent programs, with settlement executed by the customer's licensed providers |

---

## Human-in-the-Loop Support

Supported and bounded by policy rather than by a review queue on every payment. A mandate's `review_above` threshold is the only thing that pulls a human in: below it the agent is autonomous, above it the verdict is `review` and the decision names the identity whose approval it waits for — a role, not whoever happens to hold an organization key. Approval and denial are API calls (`POST /v1/reviews/{id}/approve`, `/deny`) and fire webhooks, so an approval queue is built on the customer's own surface.

The vendor documents that reviews can be actioned but not listed: there is no `GET /v1/reviews` collection, so a pending review is discovered through the decision that created it or through the webhook event.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Stripe / card processors with agent toolkits** | Human-facing rails with an agent interface added later — `agent-adapted` by this repository's own classification. They authorize a card, not a delegated mandate, and emit no signed, independently verifiable record of which agent was authorized under whose authority |
| **Spend limits in application code** | A control the agent's own process can route around is a recommendation. The limit lives on the same side of the boundary as the spender, and nothing outside that process can verify a decision was ever made |
| **Approval queues / HITL tools** | They put a human on every action, which defeats autonomy. Saifuro's threshold is the exception path, not the default, and the autonomous case produces an artifact a counterparty can check |
| **Agent wallets** | A wallet answers "can this agent pay"; it does not answer "was this agent permitted to pay this recipient, this much, under whose authority" — and leaves no verdict a seller can verify offline |

---

## Use Cases

- **Procurement agents with real limits** — an agent buys SaaS, compute, data and APIs inside a mandate written once, with the overage path going to a named role rather than to whoever is on call
- **Agent-to-agent settlement between strangers** — the seller's agent verifies the buyer's signed verdict against a public JWKS before delivering, turning a dispute into a signature check
- **Measuring a policy before enforcing it** — observe mode records what a draft policy would have denied on live traffic, so the first enforcing day is not the first day anyone sees the numbers
- **Conditional deals without a custodian** — escrow contracts on Base and Solana hold the funds against a condition, with no party able to release or freeze them early
- **Audit answers per transaction** — the NDJSON export joins identity, decision and settlement, so "who paid whom, under which policy, approved by which rule" is one query
