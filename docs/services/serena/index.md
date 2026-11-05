---
title: "Serena | Agent-Native Services"
service_name: "Serena"
description: "Serena is the IDE for your coding agent"
permalink: /services/serena/
page_kind: service
service_slug: "serena"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/serena.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/serena.md"
tagline: "Serena is the IDE for your coding agent"
website: "https://oraios.github.io/serena/"
repository: "https://github.com/oraios/serena"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">GPL-3.0-or-later for the Serena application; SolidLSP is MIT. Combined distributions such as serena-agent are GPL-3.0-or-later</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://oraios.github.io/serena/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://oraios.github.io/serena/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/oraios/serena" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/serena.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Serena gives coding agents **semantic code intelligence**: symbol-level retrieval, editing, and refactoring tools backed by **language servers (LSP)** or an optional **JetBrains plugin**, all exposed through **MCP**. README positions **agent-first tool design** with high-level abstractions instead of brittle line-number grep/replace, plus an optional **memory system** for long-lived agent workflows across large codebases.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, http
- **MCP:** ✅ Serena is an MCP server (stdio by default; HTTP mode documented)
- **Agent Skill:** ⚠️ Not yet published as a standalone npx skills add … pack
- **Onboarding type:** `other`

## How agents onboard

```bash
uv tool install -p 3.13 serena-agent@latest --prerelease=allow
serena init
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/serena.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **MCP** | Primary integration for coding agents |
| **CLI** | `serena` via `uv tool install … serena-agent` |
| **Docs** | https://oraios.github.io/serena/ |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
