---
title: "OrcaReplay | Agent-Native Services"
service_name: "OrcaReplay"
description: "Your agent broke something at 2am. Replay it at 9am — exactly, offline, as many times as you like"
permalink: /services/orcareplay/
page_kind: service
service_slug: "orcareplay"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/orcareplay.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/orcareplay.md"
tagline: "Your agent broke something at 2am. Replay it at 9am — exactly, offline, as many times as you like"
verified_at: "2026-10-20"
website: "https://github.com/Continuum-AI-Corp/OrcaReplay"
repository: "https://github.com/Continuum-AI-Corp/OrcaReplay"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0 (code); trace spec CC BY 4.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/Continuum-AI-Corp/OrcaReplay" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/Continuum-AI-Corp/OrcaReplay/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Continuum-AI-Corp/OrcaReplay" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/orcareplay.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

OrcaReplay records a coding agent **below the harness** and gives the run back. Capture happens at the process and socket boundary rather than through an SDK, so the agent binary stays unmodified. Five layers cooperate on one timeline: a loopback proxy for model traffic, a PATH shim for shell commands and exit codes, an MCP JSON-RPC tee, a shadow git index for per-turn file state, and a `fetch` hook (or opt-in `--tls-intercept`) for hardcoded origins. That shared timeline is what lets you ask which tool call sent the run down the wrong branch.

`orca replay` serves recorded HTTP bodies back with the network off (`egress=blocked`), so the harness runs again against a fixed transcript. `orca fork` / `orca replay --from N --model <other>` sits a cursor on a derived checkpoint: earlier turns stay on disk, later turns go live on a different model against the same conversation prefix and restored git tree. `orca compare` repeats that fork across named models and grades each with a `--verify` command.

Bounds, stated rather than implied. The byte-for-byte guarantee holds when the prompt was recorded through argv (`orca record claude -- -p "…"`). A hand-driven terminal session replays the conversation but not the run byte for byte — the harness makes calls for itself, and interactive-only tools such as `AskUserQuestion` are absent without a person. Replay proves the recorded decisions still reproduce; it cannot prove a fresh run would fail the same way, because the model is not asked again. Replay re-executes recorded tool calls for real and is not a sandbox. `orca compare` uploads recorded context to third-party providers and spends real money.

Supported capture paths include Claude Code, Codex CLI (API key or ChatGPT-subscription login via `--tls-intercept`), opencode, goose, OpenClaw, grok-cli, Cursor-in-the-IDE, plus framework traffic that reads a base-URL variable (OpenAI Agents SDK, Vercel AI SDK, LangGraph, CrewAI, Aider, and others listed in the README).

**Maturity, stated plainly.** The repository was created on **2026-08-29**. As of 2026-09-12 it is on npm as `orcareplay@0.2.4`, listed in the official MCP registry, and ships a published Agent Skill — and it is still early. There is no tagged 1.0, no stability guarantee on the v0 trace schema, and no adoption figure worth claiming. The catalog lists it because the operator-surface is real and documented, not because it is mature.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI wrapper (process + socket interception; operator-surface track)
- **Catalog protocols:** Agent Skill, MCP, CLI, STDIO, http, API
- **MCP:** ✅ Available (orca mcp, protocol 2025-06-18)
- **Agent Skill:** ✅ Published — skills/orca-replay/SKILL.md, also discoverable on ClawHub.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI wrapper (process + socket interception; operator-surface track)

```bash
npm i -g orcareplay
orca doctor
orca record claude
orca replay last
orca fork last
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/orcareplay.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `orca doctor`, `record`, `replay`, `fork`, `compare`, `show`, `checkpoints`, `graph`, `export`, `scrub`, `gc`, `attach`, `setup`, `models`, `quickstart`; `--json` on the read/replay commands |
| MCP | stdio `orca mcp` / `npx -y orcareplay mcp`; six tools; official registry `io.github.Continuum-AI-Corp/orcareplay` |
| Agent Skill | [`skills/orca-replay/SKILL.md`](https://github.com/Continuum-AI-Corp/OrcaReplay/tree/main/skills/orca-replay); ClawHub search `orca-replay` |
| TypeScript API | `import { Orca } from 'orcareplay'` — same source of truth the CLI renders |
| On-disk format | v0 trace + JSON Schema; spec at [`spec/orca-trace-v0.md`](https://github.com/Continuum-AI-Corp/OrcaReplay/blob/main/spec/orca-trace-v0.md) (CC BY 4.0) |
| Viewer | Optional single-file HTML (`orca replay --ui` / `orca export -o run.html`); not required for the operational loop |

---

## Verification

Last verified **2026-10-20**.

Sources:
- https://api.github.com/repos/Continuum-AI-Corp/OrcaReplay
- https://registry.npmjs.org/orcareplay
- https://registry.modelcontextprotocol.io/v0.1/servers/io.github.Continuum-AI-Corp%2Forcareplay/versions/latest

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
