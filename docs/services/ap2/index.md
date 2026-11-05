---
title: "Agent Payments Protocol (AP2) | Agent-Native Services"
service_name: "Agent Payments Protocol (AP2)"
description: "An open protocol for the emerging Agent Economy"
permalink: /services/ap2/
page_kind: service
service_slug: "ap2"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/ap2.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/ap2.md"
tagline: "An open protocol for the emerging Agent Economy"
verified_at: "2026-10-13"
website: "https://ap2-protocol.org"
repository: "https://github.com/google-agentic-commerce/AP2"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK · A2A · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://ap2-protocol.org" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://ap2-protocol.org" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/google-agentic-commerce/AP2" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/ap2.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agent Payments Protocol (AP2) is an open protocol for **verifiable agent payments**. Today's rails assume a human clicked Buy. When an agent pays, merchants cannot answer authorization, authenticity, or accountability from that click model. AP2's answer is **verifiable digital credentials (VDCs)** — tamper-evident, cryptographically signed mandates:

- **Checkout Mandate** — open (constraints before a cart exists) or closed (authorization of a finalized checkout), shared with the merchant.
- **Payment Mandate** — open (budget / allowed instruments) or closed (amount bound to a finalized checkout), shared with the credential provider, networks, and merchant processor.

Mandates chain into a non-repudiable audit trail for human-present and human-not-present transactions. Samples include human-not-present cards, human-not-present **x402**, digital payment credentials on Android, and human-present cards.

This is the **mandate layer next to catalog x402**: x402 is HTTP 402 settlement; AP2 is proof of user intent the merchant and networks can verify. UCP documents AP2 as its secure-payment path.

**Freshness:** `pushed_at` on the GitHub repo was 2026-06-17 at verification. Treat the spec and samples as the source of truth; do not infer weekly release cadence.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK + scenario samples
- **Catalog protocols:** SDK, A2A, http
- **MCP:** ⚠️ Extension surface, not a hosted MCP server.
- **Agent Skill:** ⚠️ No official Agent Skills package published.
- **Onboarding type:** `sdk`

## How agents onboard

**Interaction pattern:** SDK + scenario samples

```bash
# Types package (PyPI later; official install is from git): https://github.com/google-agentic-commerce/AP2
uv pip install git+https://github.com/google-agentic-commerce/AP2.git@main
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/ap2.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Spec / docs | https://ap2-protocol.org and repo `docs/` |
| Python types | `uv pip install git+https://github.com/google-agentic-commerce/AP2.git@main` |
| Samples | `code/samples/python`, `go`, `android` + `run.sh` |
| Web demo client | `code/web-client/` (Vite + React) |
| Extensions | A2A, UCP; x402 sample |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/google-agentic-commerce/AP2

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
