---
title: "SendRaven | Agent-Native Services"
service_name: "SendRaven"
description: "Email infrastructure for AI agents"
permalink: /services/sendraven/
page_kind: service
service_slug: "sendraven"
category_slug: "communication"
category_label: "Communication"
hero_image: "/assets/images/editorial-communication.webp"
image: "/assets/images/editorial-communication.webp"
classification: "agent-native"
dossier_path: "services/communication/sendraven.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/sendraven.md"
tagline: "Email infrastructure for AI agents"
website: "https://sendraven.ai"
repository: "https://github.com/CommonNinja/sendraven-mcp-server"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Communication</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · webhook · openapi · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://sendraven.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://sendraven.ai/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/CommonNinja/sendraven-mcp-server" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/sendraven.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

SendRaven is an email platform whose stated primary caller is an AI agent. An agent sends transactional email from the customer's own verified domain, receives the replies, and reads them as thread state: each reply is joined to its conversation on `Message-ID` (never on subject), quoted history is stripped, and a thread carries an `awaiting_reply` flag, so the agent can ask "what needs an answer?" and reply in the same thread.

The second half is the constraint model. Limits live on the credential the agent holds, not on the workspace: a per-key daily send cap, a recipient allowlist, and an approval hold that turns every send from that key into a draft a person releases. A key cannot edit its own limits, mint a looser key, or approve its own drafts.

The same platform also runs campaigns, automations and ordinary transactional mail (it replaced the email providers of its builders' own products), so it is not agent-only; agents are the primary consumer on the homepage, the docs and the MCP page.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP server (remote Streamable HTTP with OAuth, or stdio with an API key); REST for everything else
- **Catalog protocols:** MCP, REST, webhook, openapi, STDIO, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP server (remote Streamable HTTP with OAuth, or stdio with an API key); REST for everything else

```bash
npx -y @sendraven/mcp   # with SENDRAVEN_API_KEY=sk_live_... in the environment
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/communication/sendraven.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `https://api.sendraven.ai/v1`, Bearer `sk_live_…` keys, snake_case JSON, one error vocabulary |
| OpenAPI | https://sendraven.ai/openapi.json |
| MCP Server | Remote Streamable HTTP with OAuth, or `npx -y @sendraven/mcp` over stdio |
| Webhooks | Signed deliveries for `inbound`, `delivery`, `bounce`, `complaint`, `open`, `click` and more |
| llms.txt | https://sendraven.ai/llms.txt |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/communication/' | relative_url }}"><small>Collection</small><strong>← Communication</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
