---
title: "DeepSeek Harness (dsh) | Agent-Native Services"
service_name: "DeepSeek Harness (dsh)"
description: "Everything is a Plugin"
permalink: /services/deepseek-harness/
page_kind: service
service_slug: "deepseek-harness"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/deepseek-harness.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/deepseek-harness.md"
tagline: "Everything is a Plugin"
verified_at: "2026-10-13"
website: "https://deepseek.com/harness"
repository: "https://github.com/deepseek-ai/deepseek-harness"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · SDK · ACP · json rpc · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://deepseek.com/harness" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://deepseek.com/harness" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/deepseek-harness.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

DeepSeek Harness (`dsh`) is DeepSeek AI's open-source agent harness. Official positioning is that a model is the agent's soul and the harness is what lets the agent understand its environment, use tools, and keep working in real scenes. Every agent capability — model, tools, skills, session, sandbox, storage, loop, scheduling, UI — is a Cordis plugin. Developers compose or replace those plugins in configuration without forking the harness.

The product is a **developer preview**. The README warns there will be compatibility-breaking changes. The homepage lists four run modes: Standard (full coding agent), PTC (standard tools plus a Code Mode TypeScript program that batches tool calls), Minimal (persistent bash + `str_replace_editor` for model benchmarks), and Create (inspect the runtime, experiment with plugins, author new presets).

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + Web UI (developer preview)
- **Catalog protocols:** CLI, SDK, ACP, json rpc, http
- **MCP:** ⚠️ Not published as a standalone MCP server.
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + Web UI (developer preview)

```bash
npx @deepseek-ai/dsh web
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/deepseek-harness.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI / npm | `npx @deepseek-ai/dsh web`; source `pnpm dsh` |
| Web UI | Local operator UI, default `http://127.0.0.1:3080` |
| ACP | Automation-only Agent Client Protocol server |
| JSON-RPC SDK | TypeScript client in `packages/sdk/` |
| Python SDK | Bundled runtime under `python/` |
| Session log | Append-only events; Trajectory resume/fork/replay |
| Plugin topic | [`dsh-plugin`](https://github.com/topics/dsh-plugin) for community plugins |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/deepseek-ai/deepseek-harness

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
