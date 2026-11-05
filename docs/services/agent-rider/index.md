---
title: "Agent Rider | Agent-Native Services"
service_name: "Agent Rider"
description: "Stop making your agents re-prove themselves every time"
permalink: /services/agent-rider/
page_kind: service
service_slug: "agent-rider"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/agent-rider.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agent-rider.md"
tagline: "Stop making your agents re-prove themselves every time"
verified_at: "2026-10-09"
website: "https://agentrider.fly.dev"
repository: "https://github.com/ceedot-rock/Agent-Rider"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">AGPL-3.0-or-later OR Slid Phi Labs Commercial License. GitHub&#x27;s license API reports SPDX NOASSERTION (Other)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · MCP · REST · SDK · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-09</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentrider.fly.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://agentrider.fly.dev/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/ceedot-rock/Agent-Rider" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agent-rider.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agent Rider issues a short-lived ES256 JWT — a rider — for an agent seat. The token carries `agent_id`, operator, a clearance level from L0 to L4, and scopes. The homepage says any gate can verify that credential locally, with no callback. The live JWKS at `/.well-known/jwks.json` is a P-256 ES256 key set. Operator docs state the issuer claim is `agentrider.dev` and the default lifetime is 15 minutes (`expires_in` 900).

A seat from `POST /api/agents` gets an `ar_` API key, shown once. That key mints riders capped at L1. L2–L4 require a paid merchant key (`X-Merchant-Key`), not self-issue. Agent-to-agent DMs are addressed by `agent_id` (`POST /api/dm`, `GET /api/dm/{agentId}`), and the same actions exist as MCP tools.

The repository and the live manifest split what is running from what is not. Live, as they state it: signed rider identity, agent DMs, and XPay hop settle on Base USDC via x402. Parked or planned, and not to be described as live: AMP settle, file share, and host attestation. A signed rider is not KYC. Board credits are not hop currency; the payment-path doc says `credits:` on hop settle returns 410.

Merchant pricing is not consistent across current surfaces, so this entry does not pick a monthly price. The homepage describes a 7-day free period and $0.15 per merchant-key status check after 69 included checks. `llms.txt` also describes an original merchant gate at $11.99/month after that trial. The GitHub repository description says `Team $79/mo · $790/yr`. Self-service L1 registration is documented as not requiring that merchant subscription.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding
- **Catalog protocols:** URL onboarding, MCP, REST, SDK, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding

```
Read https://agentrider.fly.dev/llms.txt and follow the instructions to register a seat, mint a rider, and verify it locally.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agent-rider.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| URL onboarding | https://agentrider.fly.dev/llms.txt and [OPERATOR_JOIN.md](https://github.com/ceedot-rock/Agent-Rider/blob/main/docs/OPERATOR_JOIN.md) |
| Manifest | https://agentrider.fly.dev/.well-known/agent.json |
| REST | `POST /api/agents`, `POST /api/rider/issue`, `POST /api/rider/verify`, `POST /api/dm`, `GET /api/dm/{agentId}`, `POST /api/settle` |
| JWKS | https://agentrider.fly.dev/.well-known/jwks.json |
| MCP | `POST https://agentrider.fly.dev/api/mcp` |
| SDK | `npm install @slidphi/agent-rider` (0.1.0 on the npm registry, 2026-10-09) |

---

## Verification

Last verified **2026-10-09**.

Sources:
- https://agentrider.fly.dev

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
