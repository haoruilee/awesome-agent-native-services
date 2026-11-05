---
title: "ToolHive | Agent-Native Services"
service_name: "ToolHive"
description: "Run any MCP server securely, instantly, anywhere"
permalink: /services/toolhive/
page_kind: service
service_slug: "toolhive"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/toolhive.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhive.md"
tagline: "Run any MCP server securely, instantly, anywhere"
website: "https://stacklok.com/download/"
repository: "https://github.com/stacklok/toolhive-studio"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://stacklok.com/download/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.stacklok.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/stacklok/toolhive-studio" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhive.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

ToolHive provides a control plane for MCP servers: discovery, deployment, sandboxed execution, and secure connection for agent runtimes and coding assistants.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, STDIO, http, API
- **MCP:** ✅ Core product.
- **Agent Skill:** ⚠️ No official AgentSkills package yet.
- **Onboarding type:** `cli`

## How agents onboard

```bash
brew tap stacklok/tap
brew install thv
thv --help
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhive.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `thv` install/run/manage lifecycle |
| MCP | Runs MCP servers for stdio/socket/HTTP-compatible clients |
| Docs/API | Operational configuration and server management workflows |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
