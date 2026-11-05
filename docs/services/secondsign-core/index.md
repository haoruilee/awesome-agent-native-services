---
title: "SecondSign Core | Agent-Native Services"
service_name: "SecondSign Core"
description: "An independent transaction co-signer for AI agents that manage other people's money"
permalink: /services/secondsign-core/
page_kind: service
service_slug: "secondsign-core"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/secondsign-core.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/secondsign-core.md"
tagline: "An independent transaction co-signer for AI agents that manage other people's money"
verified_at: "2026-09-26"
website: "https://secondsignruntime.com"
repository: "https://github.com/Bestpart-Irene/secondsign-core"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Pre-1.0 preview. Interfaces may change; no independent security audit; some gateway control-plane state is not restart-durable. Apache-2.0.</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://secondsignruntime.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/Bestpart-Irene/secondsign-core#documentation" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Bestpart-Irene/secondsign-core" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/secondsign-core.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

SecondSign Core is a deterministic transaction authorization boundary for financial agents. The agent proposes a structured, immutable intent without raw account or customer data. Policies can only tighten the result to `ALLOW`, `REVIEW`, or `DENY`; reviewed actions receive a one-shot, expiring, proposal-bound human decision; and the execution gateway rechecks the exact intent before dispatching it once with a gateway-derived idempotency key.

The reference deployment separates three trust domains: a credential-free agent client, a gateway that alone holds the rail credential, and an approver on a second mTLS network the agent cannot reach. Redacted receipts form a hash chain. A separate on-chain path can act as one key in a 2-of-2 Safe, but that path is younger, unaudited, and has only run against a local chain.

This is pre-1.0 software, not a production-security endorsement. The official status notes that principal fingerprint data, spend-window state, and pending reviews currently live in process and are forgotten on gateway restart; spending limits are configured as gateway constants rather than state held by an auditable authority.

---

## Agent-facing interfaces

- **Catalog protocols:** SDK, http, API
- **MCP:** ⚠️ No first-party MCP server is documented. The verified agent surfaces are the Python public API and the standalone gateway's versioned HTTPS authorization protocol.
- **Agent Skill:** ⚠️ Not yet published by the project.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
pip install secondsign-core
python examples/quickstart.py
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/secondsign-core.md#how-to-use-agent-onboarding).

## Protocol surface

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

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/Bestpart-Irene/secondsign-core/releases/tag/v0.2.0
- https://secondsignruntime.com
- https://api.github.com/repos/Bestpart-Irene/secondsign-core

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
