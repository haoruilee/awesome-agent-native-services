---
title: "datawebot | Agent-Native Services"
service_name: "datawebot"
description: "The world's ecommerce. One MCP"
permalink: /services/datawebot/
page_kind: service
service_slug: "datawebot"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/datawebot.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/datawebot.md"
tagline: "The world's ecommerce. One MCP"
verified_at: "2026-11-09"
website: "https://www.datawebot.com"
repository: "https://github.com/datawebot/datawebot-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Hosted service closed source. Connection kit MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · CLI · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-09</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.datawebot.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.datawebot.com/docs/agents" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/datawebot/datawebot-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/datawebot.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

datawebot gives an agent ecommerce product data: what is for sale, at what price, from which shop, with a link to the product page. `search_products` searches one shop or across shops in a chosen country. `get_product` reads one product by URL or by the `product_id` from a search. When several shops sell it, the answer lists each seller's price, shipping total, delivery note and direct link. Ads are returned separately from organic results. Every answer is a best-effort snapshot labelled with when it was retrieved. It is not a verified or guaranteed-current price, and datawebot does not store a price history.

Extraction Jobs read one exact store endpoint: a search page, a catalogue or category page, or a product page. `find_endpoints` lists a shop's endpoint ids, prices and page limits. `submit_job` runs one id on one URL. The same operations are on the REST API and on the `dtwb` CLI. The site index, checked against the catalogue when the site is built (the copy fetched on 2026-11-09 says checked 2026-11-03), states that Jobs cover 36,413 stores in 126 countries through 109,094 endpoints, including Amazon in 20 countries, Mercado Libre in 18, eBay in 17, Zalando in 17 and Walmart US. Product search is not limited to that store list.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, CLI, openapi, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding

```
Read https://mcp.datawebot.com/setup.md and follow the instructions.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/datawebot.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | `https://mcp.datawebot.com/mcp`, Streamable HTTP, OAuth 2.1 or bearer key. Discovery document: https://www.datawebot.com/.well-known/mcp.json |
| REST | `https://api.datawebot.com`. OpenAPI 3.1, title "datawebot. Jobs API", at https://www.datawebot.com/openapi.json. Intent calls use `POST /v1/requests`. Jobs use `GET /v1/job-blueprints`, `POST /v1/jobs`, `GET /v1/jobs/{id}`, `GET /v1/jobs/{id}/results` |
| CLI | `npm install --global @datawebot/cli`, then `dtwb login`, `dtwb search`, `dtwb product`, `dtwb extract`. stdout is one JSON document. Guide: https://www.datawebot.com/cli.md |
| Agent documents | https://mcp.datawebot.com/setup.md · https://www.datawebot.com/SKILL.md · https://www.datawebot.com/llms.txt |
| Reference | https://www.datawebot.com/docs/agents · https://www.datawebot.com/docs/api/reference · store directory https://www.datawebot.com/scraper |

---

## Verification

Last verified **2026-11-09**.

Sources:
- https://mcp.datawebot.com/setup.md
- https://www.datawebot.com/llms.txt
- https://www.datawebot.com/SKILL.md
- https://www.datawebot.com/openapi.json
- https://mcp.datawebot.com/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
