---
title: "REA (Reverse Engineer Anything) | Agent-Native Services"
service_name: "REA (Reverse Engineer Anything)"
description: "One MCP for reverse engineering across binaries, applications, and runtime behavior"
permalink: /services/rea/
page_kind: service
service_slug: "rea"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/rea.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/rea.md"
tagline: "One MCP for reverse engineering across binaries, applications, and runtime behavior"
website: "https://rea.tools"
repository: "https://github.com/morluto/rea"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · STDIO</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://rea.tools" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/morluto/rea/blob/main/docs/getting-started/installation.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/morluto/rea" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/rea.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

REA connects a coding agent to local reverse-engineering tools for **native binaries** (pseudocode, assembly, strings, symbols via Hopper, Ghidra or IDA), **JavaScript and Electron apps** (modules, source maps, IPC channels, native add-ons), **.NET assemblies** (metadata and CIL), **Android APKs** (via JADX) and **websites** (structure, scripts, observed traffic via a Chrome-family browser). It can also capture runtime process behavior. Analysis runs locally, and results include the evidence and limitations behind each conclusion, so the agent can ask follow-up questions or write and test an implementation.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP (stdio) + CLI + agent workflow instructions
- **Catalog protocols:** Agent Skill, MCP, CLI, STDIO
- **MCP:** ✅ Available
- **Agent Skill:** ✅ setup installs matching workflow instructions for each selected agent alongside the MCP server.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP (stdio) + CLI + agent workflow instructions

```bash
# Preview the config changes first, then apply
npx -y rea-agents setup --dry-run
npx rea-agents setup        # choose agents, review, approve (backs up existing config)
# restart the agent, then verify
rea doctor --json
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/rea.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **MCP** | stdio server registered by `rea-agents setup` |
| **CLI** | `rea …` commands sharing the MCP workflows; `rea doctor --json` |
| **npm** | `rea-agents` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
