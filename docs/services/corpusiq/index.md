---
title: "CorpusIQ | Agent-Native Services"
service_name: "CorpusIQ"
description: "Accelerate your business. All your tools in one place"
permalink: /services/corpusiq/
page_kind: service
service_slug: "corpusiq"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/corpusiq.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/corpusiq.md"
tagline: "Accelerate your business. All your tools in one place"
verified_at: "2026-11-10"
website: "https://www.corpusiq.io"
repository: "https://github.com/CorpusIQ/corpusiq-docs"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Platform API declared proprietary (LicenseRef-CorpusIQ-Proprietary) in openapi.json. MCP server source is private. corpusiq-docs has no license file</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · openapi · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-10</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.corpusiq.io" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.corpusiq.io/developers" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/CorpusIQ/corpusiq-docs" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/corpusiq.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

CorpusIQ is a hosted MCP server that answers questions from business systems the user has connected. The current site says 40+ connectors, including Stripe, Google Analytics 4, and Shopify, and lists others such as QuickBooks, HubSpot, ads platforms, mail, files, and databases. Issue #146's figure of 36 is older than that copy. The connectors page also says "50+ more coming." This entry does not treat any of those phrases as a hand-counted inventory.

The user authorizes each source. External retrieval tools are documented as read-only against those vendor systems: they do not create, update, or delete a vendor record, send a message, or move money. Separate control-plane tools write CorpusIQ's own configuration, such as enabling a connector, resetting a token, or storing a canonical fact. Several of those writes return a `pending_write_id` and ask for `canonical_pending_commit` after the user confirms.

`ask_corpusiq` is the server's route for an executive financial snapshot. It selects a read-only runbook and returns an answer, evidence, warnings, and an execution receipt. Broad questions go through `resolve_connector`. A matching `featured_*` tool returns a `skill_body` runbook for the agent to execute. The site also advertises 150+ pre-built expert workflows. Plans on https://www.corpusiq.io/pricing.md (last updated 2026-11-10) are Solo $29.95, Team $109.95, and Business $189.95 per month, with a 30-day trial and no card required to start.

https://www.corpusiq.io/docs/api/ still documents `POST https://api.corpusiq.io/v1/query` and `POST /v1/deep_search`. An unauthenticated POST to `https://api.corpusiq.io/v1/query` on 2026-11-10 returned HTTP 404 with Vercel's `DEPLOYMENT_NOT_FOUND`. The live machine contract that responded is the MCP host. Its public description is OpenAPI 3.1 at https://www.corpusiq.io/openapi.json, titled "CorpusIQ Platform API", server `https://mcp2.corpusiq.io`, covering OAuth discovery, the device flow, `POST /mcp`, and `GET /api/v1/usage/public-counter`.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP
- **Catalog protocols:** Agent Skill, MCP, openapi, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP

```
claude mcp add --transport http corpusiq https://mcp2.corpusiq.io/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/corpusiq.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | `https://mcp2.corpusiq.io/mcp`, Streamable HTTP. Registry record `io.corpusiq/multi-source-mcp` `1.0.3` |
| OAuth | https://mcp2.corpusiq.io/.well-known/oauth-protected-resource · https://mcp2.corpusiq.io/.well-known/oauth-authorization-server · device authorization `https://mcp2.corpusiq.io/oauth/device/authorize` · registration `https://mcp2.corpusiq.io/oauth/register` |
| OpenAPI | https://www.corpusiq.io/openapi.json — OpenAPI 3.1.0, title "CorpusIQ Platform API", license `LicenseRef-CorpusIQ-Proprietary`, server `https://mcp2.corpusiq.io` |
| Agent documents | https://www.corpusiq.io/llms.txt · https://www.corpusiq.io/llms-full.txt · https://raw.githubusercontent.com/CorpusIQ/corpusiq-docs/main/llms-install.md |
| Docs | https://www.corpusiq.io/developers · https://docs.corpusiq.io · https://www.corpusiq.io/security · https://www.corpusiq.io/connectors |
| Claude skills | https://github.com/CorpusIQ/corpusiq-claude-skills (MIT) |

---

## Verification

Last verified **2026-11-10**.

Sources:
- https://www.corpusiq.io/
- https://corpusiq.io
- https://www.corpusiq.io/llms.txt
- https://www.corpusiq.io/developers
- https://www.corpusiq.io/pricing.md
- https://www.corpusiq.io/openapi.json
- https://mcp2.corpusiq.io/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
