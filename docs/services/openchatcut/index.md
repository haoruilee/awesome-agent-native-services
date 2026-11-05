---
title: "OpenChatCut | Agent-Native Services"
service_name: "OpenChatCut"
description: "Open-source, local-first conversational AI video editor with a professional multi-track timeline, Agent Skills, MCP integration, and Remotion rendering"
permalink: /services/openchatcut/
page_kind: service
service_slug: "openchatcut"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/openchatcut.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/openchatcut.md"
tagline: "Open-source, local-first conversational AI video editor with a professional multi-track timeline, Agent Skills, MCP integration, and Remotion rendering"
verified_at: "2026-09-26"
website: "https://openchatcut.com"
repository: "https://github.com/0xsline/OpenChatCut"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Early, actively evolving local-first project; AGPL-3.0-or-later</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://openchatcut.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/0xsline/OpenChatCut#using-openchatcut-with-codex--claude-code" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/0xsline/OpenChatCut" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/openchatcut.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

OpenChatCut turns a real, editable video project into an agent tool surface. Its built-in agent and external MCP clients operate the same `EditorCore` commands over multitrack timelines, media, transcripts, captions, audio, transitions, effects, motion graphics, and color rather than generating a one-off flattened result.

External agents work inside isolated draft edit sessions. They can inspect a project, propose precise operations, and submit an atomic set of changes that is either manually reviewed or applied in explicit `auto` mode as one undo step. Immediate, non-reversible side effects such as generation, export, and project deletion are intentionally unavailable through these draft sessions.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, http
- **MCP:** ✅ Available — first-party Streamable HTTP MCP.
- **Agent Skill:** ✅ Available.
- **Onboarding type:** `agent-skill`

## How agents onboard

```bash
npx skills add 0xsline/OpenChatCut
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/openchatcut.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **Agent Skill** | Installable router with MCP setup and safe editing workflow |
| **MCP** | Streamable HTTP endpoint for project discovery, skill loading, draft reads/edits, review, and status |
| **EditorCore commands** | Validated immutable timeline operations shared by UI and agents |
| **Local application** | Electron desktop builds and local web development server |
| **Project artifacts** | Editable project state, local media, version history, MP4/audio/captions/FCPXML export through the application |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/0xsline/OpenChatCut/releases/tag/v0.2.14
- https://openchatcut.com
- https://api.github.com/repos/0xsline/OpenChatCut

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
