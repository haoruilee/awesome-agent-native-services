---
title: "AffixIO | Agent-Native Services"
service_name: "AffixIO"
description: "Know which agent acted. Prove it stayed inside the lines"
permalink: /services/affixio/
page_kind: service
service_slug: "affixio"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/affixio.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/affixio.md"
tagline: "Know which agent acted. Prove it stayed inside the lines"
website: "https://www.affix-io.com/"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.affix-io.com/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.affix-io.com/agent-trust/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/affixio.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AffixIO ships an Agentic Pay Kit (npm `affixio`) so a **host application** can get a signed yes/no before an agent pays, runs a privileged tool, or is granted access. The core idea is host-side **action attestation**: Know Your Agent (KYA) enrolment and capability grants for a named agent id, then runtime checks such as `x402BeforePay` and `mcpToolGate` that return an attestible allow/deny with a proof id.

This path is **not person KYC**. It decides whether *this agent* may act under a host-written policy, not whether a human passed identity verification at checkout.

---

## Agent-facing interfaces

- **Catalog protocols:** SDK, http, API
- **MCP:** ⚠️ Not yet published
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `sdk`

## How agents onboard

```bash
npm install affixio
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/affixio.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| npm SDK | `affixio` - https://www.npmjs.com/package/affixio |
| TypeScript SDK | npm `affixio` (proprietary; no public GitHub source) |
| HTTP API | `api.affix-io.com` (see agent-trust docs) |
| Local dashboard | `npx affixio dashboard` |
| Docs | https://www.affix-io.com/agent-trust/ |
| MCP | Not an MCP server product; `mcpToolGate` + Streamable HTTP proof/tool endpoints as documented publicly |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
