---
title: "Agent Search MCP | Agent-Native Services"
service_name: "Agent Search MCP"
description: "A Node.js MCP server and CLI for English and Chinese web search"
permalink: /services/agent-search-mcp/
page_kind: service
service_slug: "agent-search-mcp"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/agent-search-mcp.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/agent-search-mcp.md"
tagline: "A Node.js MCP server and CLI for English and Chinese web search"
verified_at: "2026-09-26"
website: "https://lennney.com/en/agent-search-mcp"
repository: "https://github.com/lennney/agent-search-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://lennney.com/en/agent-search-mcp" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/lennney/agent-search-mcp#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/lennney/agent-search-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/agent-search-mcp.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agent Search MCP is a Node.js search runtime that starts without an API key. It fans out to zero-key engines (and optional paid providers only when policy and credentials allow), then returns a Search Evidence Packet: results plus `meta.execution`, quality-gate `stop_reason`, budgets, and `partialFailures`. Compact mode bounds tokens while keeping provenance. Chinese queries can use Sogou/Baidu without a translation layer.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP (stdio) + optional Agent Skill + fasm CLI
- **Catalog protocols:** Agent Skill, MCP, CLI, STDIO, http
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** MCP (stdio) + optional Agent Skill + fasm CLI

```json
{
  "mcpServers": {
    "agent-search": {
      "command": "npx",
      "args": ["-y", "agent-search-mcp"]
    }
  }
}
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/agent-search-mcp.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP stdio | `npx -y agent-search-mcp` |
| MCP HTTP | `MODE=http` + `HTTP_AUTH_TOKEN` |
| CLI | `fasm search`, `extract`, `doctor` |
| Skill | `npx skills add lennney/agent-search-mcp --skill agent-search` |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://lennney.com/en/agent-search-mcp
- https://github.com/lennney/agent-search-mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
