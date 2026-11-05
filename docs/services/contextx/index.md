---
title: "contextX | Agent-Native Services"
service_name: "contextX"
description: "contextX is a remote MCP server that provides normal search powered by Grok 4.3 and deep search powered by Grok 4.20 Multi-Agent 0309"
permalink: /services/contextx/
page_kind: service
service_slug: "contextx"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/contextx.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/contextx.md"
tagline: "contextX is a remote MCP server that provides normal search powered by Grok 4.3 and deep search powered by Grok 4.20 Multi-Agent 0309"
verified_at: "2026-09-26"
website: "https://github.com/akasakariko/ContextX"
repository: "https://github.com/akasakariko/ContextX"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">⚠️ No repository license detected as of 2026-09-26 (GitHub metadata)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/akasakariko/ContextX" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/akasakariko/ContextX/blob/main/README.en.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/akasakariko/ContextX" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/contextx.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

contextX turns two hosted search modes into MCP tools. `grok_search` handles fast everyday retrieval, while `grok_deep_search` uses a multi-agent deep-search model for slower, broader investigation and cross-referencing. The server forwards MCP queries to OpenAI-compatible Responses API upstreams and continuously consumes their stream before returning the generated content as the MCP tool result, reducing long-search gateway timeout risk.

The public endpoint fixes the upstream models and requires no caller credential. Operators who need their own keys or endpoint policy can self-host the Rust server by supplying normal- and deep-search Responses API URLs and bearer tokens through environment variables.

---

## Agent-facing interfaces

- **Interaction pattern:** remote MCP over Streamable HTTP
- **Catalog protocols:** MCP, http, API
- **MCP:** ✅ Available — public remote server
- **Agent Skill:** ⚠️ Not yet published — the repository provides MCP instructions, but no SKILL.md package.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** remote MCP over Streamable HTTP

```bash
claude mcp add --transport http contextX https://mcp.twitter.monster/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/contextx.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **Remote MCP** | Streamable HTTP at `https://mcp.twitter.monster/mcp` |
| **MCP tools** | `grok_search({query})`, `grok_deep_search({query})` |
| **Health endpoint** | `/health` on a self-hosted instance |
| **Upstream protocol** | OpenAI-compatible Responses API with streaming, configured independently for normal and deep search |
| **Self-hosted runtime** | Rust server started with `cargo run`; default MCP listener `127.0.0.1:3000/mcp` |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://mcp.twitter.monster/mcp
- https://api.github.com/repos/akasakariko/ContextX

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
