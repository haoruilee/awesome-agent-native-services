---
title: "INAM Protocol | Agent-Native Services"
service_name: "INAM Protocol"
description: "Check an AI agent or x402 seller before you pay it"
permalink: /services/inam-protocol/
page_kind: service
service_slug: "inam-protocol"
category_slug: "commerce-and-payments"
category_label: "Commerce & Payments"
hero_image: "/assets/images/editorial-commerce.webp"
image: "/assets/images/editorial-commerce.webp"
classification: "agent-native"
dossier_path: "services/commerce-and-payments/inam-protocol.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/inam-protocol.md"
tagline: "Check an AI agent or x402 seller before you pay it"
verified_at: "2026-10-13"
website: "https://inamprotocol.org"
repository: "https://github.com/inamprotocol/inam-protocol"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Commerce &amp; Payments</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Early-stage. Launched August 2026, spec is a draft (v0.42), little outside usage so far (12 finalized receipts in the public log on 2026-10-13). Stake is in the data model but cannot be posted yet.</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · CLI · SDK · A2A · openapi · json rpc · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://inamprotocol.org" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.inamprotocol.org (spec + API reference from openapi.yaml) and https://inamprotocol.org/llms.txt" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/inamprotocol/inam-protocol" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/inam-protocol.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

INAM Protocol is an open reputation layer for AI agents. After a job, both agents sign an Execution Receipt with their `did:key` (Ed25519) keys; finalized receipts are appended to an RFC 6962-style Merkle transparency log, and an agent's reputation is computed only from those receipts. Every reputation reports an `evidenceLevel` (`none`, `countersigned`, or `independently_verified`).

On the payment side, an agent can check an x402 seller, a `0x` wallet or a `did:key` before paying, either through the free hosted check or by wrapping its x402 fetch so a payment only goes out if the payee's INAM ID proved control of the `payTo` wallet and has countersigned work.

INAM is not an identity or authorization system (it links to AgentPass, AITP, ERC-8004 and similar) and not a messaging protocol. The project is early: the spec is a draft, there is one live independent verifier (an integrity check, not a correctness check), and stake cannot yet be posted.

---

## Agent-facing interfaces

- **Interaction pattern:** HTTP, CLI and MCP
- **Catalog protocols:** MCP, REST, CLI, SDK, A2A, openapi, json rpc, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published as an npx skills package
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** HTTP, CLI and MCP

```bash
curl 'https://api.inamprotocol.org/v1/check?target=<x402 endpoint URL | 0x wallet | did:key>'
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/commerce-and-payments/inam-protocol.md#how-to-use-agent-onboarding).

## Protocol surface

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

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.inamprotocol.org/v1/health
- https://api.inamprotocol.org/v1/transparency/sth
- https://api.inamprotocol.org/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/commerce-and-payments/' | relative_url }}"><small>Collection</small><strong>← Commerce &amp; Payments</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
