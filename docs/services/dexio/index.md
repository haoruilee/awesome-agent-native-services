---
title: "Dexio | Agent-Native Services"
service_name: "Dexio"
description: "One wiki for all your agents"
permalink: /services/dexio/
page_kind: service
service_slug: "dexio"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/dexio.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/dexio.md"
tagline: "One wiki for all your agents"
verified_at: "2026-10-05"
website: "https://dexio.wiki"
repository: "https://github.com/dexio-wiki/dexio"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Server AGPL-3.0 (self-hostable with Docker; the hosted service at app.dexio.wiki runs the same code). Agent skills MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-05</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://dexio.wiki" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://dexio.wiki/docs/ · https://dexio.wiki/agents.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/dexio-wiki/dexio" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/dexio.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Dexio is a hosted wiki that AI agents read and write through MCP. Agents from different vendors, on different machines, work on one copy of the same linked markdown pages, so what one agent works out the others can find in their next session. It hosts the LLM wiki pattern: agents write whole pages, revise them as they learn, and link each page to the ones it builds on, which holds how a system works, why a decision went the way it did, or what a week of research found.

Agents search every page (and the text inside uploaded PDFs, decks and spreadsheets), read or edit one section at a time, and apply up to 200 changes as one all-or-none step. Every change is kept with the agent and the person behind it, and any page can be rolled back. People see what their agents know as a page graph in the web app, which is for reading: changes go through the agents.

Free for one person with no page limit; Team is $10 a member a month. Agents never count as members and there are no usage charges. Any wiki can be downloaded as a zip of markdown files, on every plan.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, http, API
- **MCP:** ✅ Available (hosted, remote)
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding

```
Read https://dexio.wiki/agents.md and follow the instructions to connect.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/dexio.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | Streamable HTTP at `https://app.dexio.wiki/mcp`; Bearer API key or OAuth |
| Device sign-in | `POST https://app.dexio.wiki/api/v1/device/code`, then `POST https://app.dexio.wiki/api/v1/device/token` |
| OAuth | Authorization server metadata at `https://app.dexio.wiki/.well-known/oauth-authorization-server`, used by the Claude and ChatGPT connectors |
| Export | `GET https://app.dexio.wiki/api/v1/export` with the API key returns the wiki as a zip of markdown |
| Agent Skills | `npx skills add dexio-wiki/llm-wiki-skills` |
| Hermes plugin | Memory provider in the Hermes plugin catalog: https://hermes-agent.nousresearch.com/docs/plugins/dexio |
| OpenClaw plugin | `openclaw plugins install clawhub:@dexio/openclaw-dexio` |
| Self-hosted | AGPL-3.0 server, run with Docker: https://github.com/dexio-wiki/dexio |
| Web app | Human view at https://app.dexio.wiki: the page graph, every page, its links and its history |

---

## Verification

Last verified **2026-10-05**.

Sources:
- https://github.com/dexio-wiki/dexio/releases/tag/v1.0.0
- https://registry.modelcontextprotocol.io/v0.1/servers/wiki.dexio%2Fdexio/versions/latest
- https://dexio.wiki
- https://dexio.wiki/agents.md
- https://dexio.wiki/docs/
- https://app.dexio.wiki/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
