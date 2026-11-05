---
title: "ProofFetch | Agent-Native Services"
service_name: "ProofFetch"
description: "Web pages your agent can quote"
permalink: /services/prooffetch/
page_kind: service
service_slug: "prooffetch"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/prooffetch.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/prooffetch.md"
tagline: "Web pages your agent can quote"
website: "https://prooffetch.steellantern.com"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · MCP · REST · A2A · openapi · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://prooffetch.steellantern.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://prooffetch.steellantern.com/llms.txt (agent guide) · https://prooffetch.steellantern.com/connect · https://prooffetch.steellantern.com/openapi.json" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/prooffetch.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

ProofFetch fetches one public web page or text-layer PDF and returns it as **numbered, citable paragraphs** (`p1`, `p2`, …) so an agent can quote a specific paragraph by ID. Each response keeps the fetch time and two SHA-256 fingerprints: `rawSha256` over the exact bytes the server sent and `contentSha256` over the cleaned text.

Every fetch also runs a deterministic **hidden-instruction (prompt-injection) scan** and returns each match with its excerpt. A flag is a warning to review, not a safety guarantee; the text stays as the page had it.

Anyone can check a response with the open-source verifier, which recomputes both fingerprints from the page bytes and confirms every paragraph comes from that text in order. The service reads public resources only: no cookies, credentials, browser actions, JavaScript rendering, or private networks.

---

## Agent-facing interfaces

- **Interaction pattern:** remote MCP + REST, with an llms.txt agent guide.
- **Catalog protocols:** URL onboarding, MCP, REST, A2A, openapi, http, API
- **MCP:** ✅ Available (hosted remote server)
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** remote MCP + REST, with an llms.txt agent guide.

```
# Agent guide:
Read https://prooffetch.steellantern.com/llms.txt and follow the instructions.

# MCP (Claude Code):
claude mcp add --transport http proof-fetch https://prooffetch.steellantern.com/mcp

# REST: get a free key (1,000 extractions, shown once), then fetch a page
POST https://prooffetch.steellantern.com/v1/keys/free
POST https://prooffetch.steellantern.com/v1/evidence   (Authorization: Bearer <key>; body: url, idempotencyKey)
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/prooffetch.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `/v1/preflight`, `/v1/evidence`, `/v1/evidence/batch`, `/v1/credits`, `/v1/keys/free` — OpenAPI at `/openapi.json` |
| MCP | Remote HTTP at `/mcp`; 3 tools |
| Payments | Stripe MPP pay-per-request ($0.50 for 50 pages); card packs (500 / 5,000 / 25,000 / 100,000 extractions) |
| Agent discovery | `llms.txt`, `/offer` JSON, A2A-style agent card at `/.well-known/agent-card.json` |
| Verifier | Open-source Node.js CLI and library (MIT), no dependencies |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
