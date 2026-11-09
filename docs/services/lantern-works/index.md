---
title: "Lantern Works | Agent-Native Services"
service_name: "Lantern Works"
description: "GPU price comparison for agents, checked daily"
permalink: /services/lantern-works/
page_kind: service
service_slug: "lantern-works"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/lantern-works.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/lantern-works.md"
tagline: "GPU price comparison for agents, checked daily"
website: "https://thelanternworks.com"
repository: "https://github.com/connormatthewdouglas/agent-work-stack-deals"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · STDIO · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://thelanternworks.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://thelanternworks.com/for-agents/ · https://thelanternworks.com/install/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/connormatthewdouglas/agent-work-stack-deals" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/lantern-works.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Lantern Works tracks GPU rental prices across cloud GPU vendors and checks them daily. Agents call MCP tools to compare current rates for a GPU, estimate what a job will cost before it runs, and see which prices changed recently.

Every rate comes with the vendor's `source_url`, an evidence snippet, and a `checked_at` time, so an agent can cite where a price came from and how fresh it is. Job estimates come back as itemized receipts. Lantern Works does not rent GPUs or spend money on the agent's behalf; it only compares and estimates.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP (local stdio package or hosted Streamable HTTP). No API key for the core tools.
- **Catalog protocols:** MCP, STDIO, http
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP (local stdio package or hosted Streamable HTTP). No API key for the core tools.

```
# MCP (stdio, PyPI package lantern-works-deals-mcp):
Add to mcp_servers: "command": "uvx", "args": ["lantern-works-deals-mcp"]

# MCP (hosted Streamable HTTP):
claude mcp add --transport http lantern-works https://lantern-works-mcp.lantern-works.workers.dev/mcp

# Agent guide:
Read https://thelanternworks.com/for-agents/ and follow the install steps.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/lantern-works.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP (stdio) | `uvx lantern-works-deals-mcp` (PyPI `lantern-works-deals-mcp`) |
| MCP (Streamable HTTP) | `https://lantern-works-mcp.lantern-works.workers.dev/mcp` |
| JSON feeds + docs | https://thelanternworks.com/install/ · https://thelanternworks.com/for-agents/ |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
