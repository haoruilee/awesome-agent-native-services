---
title: "Memoria | Agent-Native Services"
service_name: "Memoria"
description: "Persistent memory layer for AI agents with Git-level version control"
permalink: /services/memoria/
page_kind: service
service_slug: "memoria"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/memoria.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memoria.md"
tagline: "Persistent memory layer for AI agents with Git-level version control"
website: "https://github.com/matrixorigin/Memoria"
repository: "https://github.com/matrixorigin/Memoria"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/matrixorigin/Memoria" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/matrixorigin/Memoria" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memoria.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

Memory that only grows has a failure mode. An agent writes a wrong fact, later sessions retrieve it, and the mistake compounds with no clean way back to the state before it went in. Undoing that is a version-control problem as much as a storage problem. Memoria takes the version-control framing literally. The repository describes it as "Persistent memory layer for AI agents with Git-level version control."

### Branches for what an agent believes

The dossier lists four parts: a REST API, an MCP server, semantic search, and snapshots and branches. Search is the retrieval side. Snapshots and branches are the unusual part. An agent, or the person supervising it, could capture memory at a known-good point, try something on a branch, and discard the branch if it went badly. The dossier uses the Git comparison but does not explain merge behavior, how conflicts are handled, or whether branches are per agent or shared. Those details decide whether the feature is a safety net or a curiosity, so read the [GitHub repository](https://github.com/matrixorigin/Memoria) before planning around it.

### Two servers from one install

Onboarding is to install `memoria`, then run either `memoria serve` or `memoria mcp`. The first exposes the REST API, the second the MCP server. That split is practical. A coding assistant registers the MCP server and calls memory as tools. A backend service, or an agent framework without MCP support, talks to the REST API instead. MCP is marked as verified. No Agent Skill is listed.

What the record does not cover is operational. It does not say where data is stored, how a deployment authenticates callers, or how one agent's memory is kept apart from another's beyond a generic mention of namespaces. A self-run service also means you own backups and upgrades. Check those in the README before giving it production memory.

The [memory and state collection](/categories/memory-and-state/) puts Memoria next to services that model memory in other ways. [Recall](/services/recall/) is the nearest in deployment style, self-hosted and MCP-first, without version control in its record. [Zep](/services/zep/) tracks change over time with a temporal knowledge graph, which answers a related question: what was true when. [Mem0](/services/mem0/) and [Cognee](/services/cognee/) present memory as a layer or control plane you call into. The [memory layers guide](/guides/memory-layers-for-agents/) helps separate these by what the agent needs to ask of its memory.

### Editor's take

Memoria is the one to evaluate if your agents write to memory often and you want to roll back a bad write as you would revert a commit. If history matters more as a timeline than as branches, Zep's temporal graph is the closer model. If you only need a place to store and search facts, Recall or Mem0 carry less conceptual weight. Everything above draws on the dossier and the public repository; this project has not run either server or created a branch.

</section>

## What it does

Memoria provides persistent memory layer for AI agents with Git-level version control. Its agent-facing value is to give autonomous systems a programmatic primitive that can be invoked during a task loop without requiring a human to operate a dashboard for each action.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, http, API
- **MCP:** ✅ Verified/documented by upstream or MCP server listings.
- **Agent Skill:** ⚠️ No dedicated catalog skill verified in this entry. Search ClawHub or the upstream README for the latest installable skills.
- **Onboarding type:** `mcp`

## Protocol surface

| Interface | Detail |
|---|---|
| **Primary surface** | REST API, MCP server, semantic search, snapshots/branches |
| **Repository** | https://github.com/matrixorigin/Memoria |
| **MCP** | ✅ |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
