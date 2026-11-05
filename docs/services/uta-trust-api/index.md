---
title: "UTA Trust API | Agent-Native Services"
service_name: "UTA Trust API"
description: "The USB-C of agent trust"
permalink: /services/uta-trust-api/
page_kind: service
service_slug: "uta-trust-api"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/uta-trust-api.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/uta-trust-api.md"
tagline: "The USB-C of agent trust"
website: "https://uta-trust-api.eddyflores100.workers.dev"
repository: "https://github.com/alicelabs-llc/universal-trust-adapter"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Open-core — SDK MIT OR Apache-2.0; engine AL-1.0; spec CC-BY-NC-ND 4.0; license matrix</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · REST · SDK · openapi · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://uta-trust-api.eddyflores100.workers.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/alicelabs-llc/universal-trust-adapter" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/uta-trust-api.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

UTA Trust API answers one question an agent consumer asks over HTTP: **is this automated requester trustworthy?** The caller presents an Agent Trust Card (ATC) — a self-contained, CA-signed JSON credential binding an agent's identity and capabilities to an Ed25519 public key — and the verifier returns a machine-readable verdict.

Verification is fail-closed and offline-oriented: the Ed25519 signature (RFC 8032) is checked over the JCS-canonicalized (RFC 8785) subtree (ATC-006), the CA public key is resolved from the card's own `attestation.ca_url` so no network call to the CA is required, and revocation is checked against `revocation_check_url` when `revocation_check_required: true` — an unreachable check denies rather than degrades. Verdicts are anchored as public evidence (Sigstore Rekor) so an operator can later bind "verified agent X, verdict Y at time Z" into grant records and audit trails.

The service is x402-native: settlement is $0.01 USDC per single verification (or $0.08 for a 1–10 card batch) on Base (Mainnet `eip155:8453` and Sepolia testnet `eip155:84532`), with no signup, no API key, and no human consent step — an agent that has never heard of the service can pay and call it in one round trip.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, REST, SDK, openapi, http, API
- **MCP:** ⚠️ Not yet published
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `url`

## How agents onboard

```
# URL Onboarding:
Read https://uta-trust-api.eddyflores100.workers.dev/openapi.json and follow the instructions to settle and call.

# SDK / REST:
npm install agent-trust-card        # issue / verify / inspect Agent Trust Cards
# or call the verifier directly — an agent with no pre-paid access receives
# HTTP 402 + payment metadata, settles $0.01 USDC via x402, and retries:
POST https://uta-trust-api.eddyflores100.workers.dev/v1/trust/verify

# Conformance (self-test a credential before submitting it):
npx @marketnow/uta-conformance      # signed vectors + card generator
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/uta-trust-api.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `POST /v1/trust/verify` (single), `POST /v1/trust/batch` (1–10 cards) — [OpenAPI](https://uta-trust-api.eddyflores100.workers.dev/openapi.json) |
| Payments | x402 (v2) over USDC on Base mainnet (`eip155:8453`) and Base Sepolia testnet; discovery document at the root URL |
| SDK | npm [`agent-trust-card`](https://www.npmjs.com/package/agent-trust-card) — `issue` / `verify` / `inspect` |
| Conformance | `npx @marketnow/uta-conformance` — signed vectors + card generator |
| Evidence ledger | Sigstore Rekor anchors — https://www.marketnow.site/uta/conformance/anchors/ |
| CA public keys | [JWK](https://marketnow.site/api/atc) (pinned trust anchors) · CRL: `/api/atc?action=revocation-list` · OCSP-style: `/api/ocsp?card_id=` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
