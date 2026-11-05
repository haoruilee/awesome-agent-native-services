---
title: "txcript | Agent-Native Services"
service_name: "txcript"
description: "Continue your conversation in another coding agent"
permalink: /services/txcript/
page_kind: service
service_slug: "txcript"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/txcript.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/txcript.md"
tagline: "Continue your conversation in another coding agent"
verified_at: "2026-09-20"
website: "https://github.com/skillsynchq/txcript"
repository: "https://github.com/skillsynchq/txcript"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/skillsynchq/txcript" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/skillsynchq/txcript/blob/main/docs/usage.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/skillsynchq/txcript" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/txcript.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

txcript is a library for converting agent sessions — "Pandoc for AI chats" in the repository description. Start a conversation in Claude Code and continue it in Codex, Cursor, OpenCode, or another supported harness, carrying over messages, reasoning, and tool history where the target can represent them.

The CLI discovers local sessions, searches them, views or crops them, exports a harness-neutral **Simple** JSON document, and writes a native session the destination agent can resume. The Rust crate and npm WASM package expose the same canonical `Transcript` model so other tools can search, edit, or convert without re-implementing each on-disk format.

**Related product honesty:** Skillsync desktop (`https://skillsync.com`) markets portable, searchable context and a multiplayer UI. That app is not this listing. txcript is the OSS converter, CLI, and MCP session tools.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + stdio MCP (read-only session tools)
- **Catalog protocols:** MCP, CLI, STDIO, http
- **MCP:** ✅ Available (stdio, read-only)
- **Agent Skill:** ⚠️ Not yet published as an official npx skills add pack.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + stdio MCP (read-only session tools)

```bash
cargo install --git https://github.com/skillsynchq/txcript txcript-cli --locked
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/txcript.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `txcript list`, `continue` / `resume`, `query`, `view`, `crop`, `export`, `mcp` |
| stdio MCP | Read-only session tools |
| Rust crate | `txcript` — codecs, stores, search — https://docs.rs/txcript |
| npm / WASM | `npm install txcript` — in-memory convert / search |
| Simple JSON | Interchange document for agents without a native adapter |
| Skillsync desktop | Related commercial product at https://skillsync.com — not the listed interface |

---

## Verification

Last verified **2026-09-20**.

Sources:
- https://news.ycombinator.com/item?id=49743049

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
