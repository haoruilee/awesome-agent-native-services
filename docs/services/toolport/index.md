---
title: "Toolport | Agent-Native Services"
service_name: "Toolport"
description: "Every tool. One port"
permalink: /services/toolport/
page_kind: service
service_slug: "toolport"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/toolport.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolport.md"
tagline: "Every tool. One port"
verified_at: "2026-09-26"
website: "https://toolport.app"
repository: "https://github.com/btsouth/toolport"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://toolport.app" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/btsouth/toolport#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/btsouth/toolport" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolport.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Toolport is a local-first MCP gateway. A human (or installer) authenticates each server once. Every AI client then points at one gateway and shares that catalog. Lazy discovery replaces thousands of tool-definition tokens with a handful of meta-tools the agent searches on demand. The same path fingerprints tool schemas (rug-pull / poisoning), marks untrusted returned content, and can pause destructive calls for human approval.

---

## Agent-facing interfaces

- **Interaction pattern:** local MCP gateway (stdio) after a one-time desktop install
- **Catalog protocols:** MCP, STDIO, http
- **MCP:** ✅ Available (gateway)
- **Agent Skill:** ⚠️ Not published as a SKILL.md package
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** local MCP gateway (stdio) after a one-time desktop install

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolport.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Desktop app | Tauri app for servers, profiles, credentials, clients |
| Gateway | `toolport-gateway` stdio MCP |
| Downstream | stdio or remote HTTP/SSE MCP servers |
| Agent rules sync | Marked blocks in `AGENTS.md` and similar |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://api.github.com/repos/btsouth/toolport

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
