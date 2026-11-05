---
title: "Zambo | Agent-Native Services"
service_name: "Zambo"
description: "Give your AI hands, memory, and proof"
permalink: /services/zambo/
page_kind: service
service_slug: "zambo"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/zambo.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/zambo.md"
tagline: "Give your AI hands, memory, and proof"
website: "https://zambo.dev"
repository: "https://github.com/zambodotdev/zambo-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://zambo.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://zambo.dev/add/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/zambodotdev/zambo-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/zambo.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Zambo is the verifiable work layer for AI: 153 tools behind one remote MCP endpoint (live data, research, site and code audits, payments with spend limits, input screening), built around three agent-only primitives. HANDOVER is the flagship: an agent wraps up a session in one AI (goal, notes, files, links, next step) and any other AI picks it up and continues, with pickup always free. Memory persists across AIs, so what one agent saves, another recalls. And every tool call returns a verifiable AER-1 receipt (IETF Internet-Draft draft-zambo-aer1-26): a saved record of the job and its result that anyone can check later, without an account, at https://zambo.dev/verify/.

The point of the receipt is narrow and provable: it proves the saved result was not changed since it was saved. Receipts are issued for every call, including calls that are rejected.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, http
- **MCP:** ✅ Available, native remote MCP server, the primary interface.
- **Agent Skill:** ✅ Available, the zambo skill on ClawHub (https://clawhub.ai/skills/zambo).
- **Onboarding type:** `mcp`

## How agents onboard

```json
{
  "mcpServers": {
    "zambo": { "url": "https://zambo.dev/mcp" }
  }
}
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/zambo.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP server | Streamable HTTP, https://zambo.dev/mcp |
| Receipt verification | https://zambo.dev/verify/ (no account needed) |
| Agent Skill | ClawHub `zambo`, install: `npx clawhub@latest install zambo` |
| Setup guides | https://zambo.dev/add/ |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
