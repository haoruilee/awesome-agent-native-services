---
title: "Mnemoverse | Agent-Native Services"
service_name: "Mnemoverse"
description: "Persistent memory for AI agents"
permalink: /services/mnemoverse/
page_kind: service
service_slug: "mnemoverse"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/mnemoverse.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mnemoverse.md"
tagline: "Persistent memory for AI agents"
verified_at: "2026-09-20"
website: "https://mnemoverse.com/"
repository: "https://github.com/mnemoverse/mcp-memory-server"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MCP server MIT, Python SDK MIT; the memory engine they call is a proprietary hosted service with a free tier. No self-hostable build of the engine is published; Enterprise customers can self-host it by agreement</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · SDK · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mnemoverse.com/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://mnemoverse.com/docs/api/reference" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/mnemoverse/mcp-memory-server" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mnemoverse.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Mnemoverse keeps what an agent learns outside its context window and returns it in whatever tool the agent is running in next. A decision made while pairing in Claude Code is available in Cursor an hour later under the same account, and in a ChatGPT connector the same evening, because all of them talk to one hosted store rather than to per-tool instruction files.

The primitive that separates it from a vector index is outcome feedback: after a recall the agent calls `memory_feedback` with the identifiers it used, and rating a recalled memory as helpful or misleading re-ranks what comes back next. Similarity alone never changes because advice turned out to be wrong; a reported outcome does.

**Boundary, stated rather than implied.** The agent decides what to offer for storage; `memory_write` is an explicit call, not a transcript miner. What the service does on its own at write time is decide whether to keep the candidate: an importance gate may filter low-value writes, and the result says for each atom whether it was stored or filtered, with a `reason`. A read returns provenance with each hit, including the author principal, and a read can exclude one author. Several other entries in this category are explicit-write services on the same terms.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP (Streamable HTTP)
- **Catalog protocols:** Agent Skill, MCP, REST, CLI, SDK, STDIO, http, API
- **MCP:** ✅ Available on two transports, with the same ten tools on each.
- **Agent Skill:** ✅ Available, published separately from the server.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP (Streamable HTTP)

```json
{
  "mcpServers": {
    "mnemoverse": {
      "url": "https://mcp.mnemoverse.com/mcp"
    }
  }
}
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mnemoverse.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP over Streamable HTTP | Hosted at `https://mcp.mnemoverse.com/mcp`, OAuth 2.1 + PKCE, POST only |
| MCP over stdio | `npx -y @mnemoverse/mcp-memory-server@latest`, authenticated with `MNEMOVERSE_API_KEY` |
| REST API | `https://core.mnemoverse.com/api/v1`, the full surface, including the administrative operations that sit outside the MCP tool set |
| Python SDK | `pip install mnemoverse` |
| Editor and CLI packages | Claude Code plugin, Cursor plugin, Gemini CLI extension, VS Code extension, and an MCPB desktop-extension manifest that runs the server as a local process |
| Agent Skill | `agent-memory-discipline`, CC0, distributed through the plugin marketplace and bundled in the Claude Code plugin |

---

## Verification

Last verified **2026-09-20**.

Sources:
- https://www.npmjs.com/package/@mnemoverse/mcp-memory-server
- https://pypi.org/project/mnemoverse/
- https://mcp.mnemoverse.com/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
