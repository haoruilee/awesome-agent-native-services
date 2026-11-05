---
title: "ContextStream | Agent-Native Services"
service_name: "ContextStream"
description: "Persistent memory. Millisecond code search"
permalink: /services/contextstream/
page_kind: service
service_slug: "contextstream"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/contextstream.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/contextstream.md"
tagline: "Persistent memory. Millisecond code search"
verified_at: "2026-10-27"
website: "https://contextstream.io"
repository: "https://github.com/contextstream/mcp-server"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-27</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://contextstream.io" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://contextstream.io/docs · https://contextstream.io/docs/editors/setup · https://contextstream.io/llms.txt" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/contextstream/mcp-server" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/contextstream.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

ContextStream gives coding agents **shared project context**: hybrid code search over indexed project files plus saved decisions, lessons, plans, and related memory that travel across sessions and tools. Indexing supplies code context; agents are expected to save decisions explicitly so later sessions can retrieve them.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP install script / hosted MCP
- **Catalog protocols:** MCP, http
- **MCP:** ✅ Official MCP server (local + hosted)
- **Agent Skill:** ⚠️ No official AgentSkills bundle located in verified materials; primary path is the MCP install scripts / hosted MCP.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP install script / hosted MCP

```bash
curl -fsSL https://contextstream.io/scripts/mcp.sh | bash
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/contextstream.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP (local) | `curl …/scripts/mcp.sh \| bash` or PowerShell `mcp.ps1` |
| MCP (hosted) | `https://mcp.contextstream.io/mcp` |
| Docs / llms.txt | https://contextstream.io/docs · https://contextstream.io/llms.txt |
| Benchmarks | https://contextstream.io/benchmarks |

---

## Verification

Last verified **2026-10-27**.

Sources:
- https://github.com/contextstream/mcp-server

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
