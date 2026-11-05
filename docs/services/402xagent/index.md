---
title: "402xAgent | Agent-Native Services"
service_name: "402xAgent"
description: "The check an agent calls before paying any x402 endpoint"
permalink: /services/402xagent/
page_kind: service
service_slug: "402xagent"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/402xagent.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/402xagent.md"
tagline: "The check an agent calls before paying any x402 endpoint"
verified_at: "2026-10-13"
website: "https://402xagent.com"
repository: "https://github.com/withgrokbot/x402-spotcheck"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://402xagent.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://402xagent.com/llms.txt and https://api.402xagent.com/openapi.json" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/withgrokbot/x402-spotcheck" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/402xagent.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

402xAgent is the check an agent calls right before paying an x402 endpoint. It probes the endpoint's 402 payment request without paying, compares it to what the listing said, and returns `pay`, `skip`, or `recheck` with a plain reason plus a public receipt URL. The paid tier adds the exact payment terms (network, asset, pay_to, scheme, quoted price) a router may sign. It never pays the target.

Public surfaces for discovery and audit: skips list https://402xagent.com/v1/skips, receipts https://402xagent.com/v1/receipts, Bazaar sample https://402xagent.com/bazaar, OpenAPI https://api.402xagent.com/openapi.json, and `/.well-known/x402`.

---

## Agent-facing interfaces

- **Interaction pattern:** HTTP and MCP
- **Catalog protocols:** MCP, openapi, http, API
- **MCP:** Available
- **Agent Skill:** Not yet published
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** HTTP and MCP

```bash
curl 'https://api.402xagent.com/v1/products/endpoint-spot-check?url=<endpoint>'
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/402xagent.md#how-to-use-agent-onboarding).

## Protocol surface

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

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.402xagent.com/health
- https://api.402xagent.com/v1/products/endpoint-spot-check?url=https://api.402rates.com/v1/ping
- https://402xagent.com/v1/receipts/sc-1373dc485641b938
- https://api.402xagent.com/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
