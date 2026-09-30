# TencentDB Agent Memory

> **"Agents remember,Humans innovate."**

| | |
|---|---|
| **Website** | https://github.com/TencentCloud/TencentDB-Agent-Memory |
| **Docs** | https://github.com/TencentCloud/TencentDB-Agent-Memory#readme |
| **GitHub** | https://github.com/TencentCloud/TencentDB-Agent-Memory |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/TencentCloud/TencentDB-Agent-Memory?style=social)](https://github.com/TencentCloud/TencentDB-Agent-Memory) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MIT (LICENSE file; GitHub SPDX shows `NOASSERTION`) |
| **Latest-month signal** | Default branch still `feat/server_team`; [v2.0.1](https://github.com/TencentCloud/TencentDB-Agent-Memory/releases/tag/v2.0.1) released 2026-08-25; last push 2026-09-29; 27,526 stars; LICENSE text still MIT (GitHub SPDX `NOASSERTION`) (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

No separate product homepage was published as of 2026-08-19. The official home is the repository:

https://github.com/TencentCloud/TencentDB-Agent-Memory

---

## Official Repo

https://github.com/TencentCloud/TencentDB-Agent-Memory

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `OpenClaw plugin` or **Hermes gateway plugin**

OpenClaw:

```bash
openclaw plugins install @tencentdb-agent-memory/memory-tencentdb
openclaw gateway restart
```

Enable in `~/.openclaw/openclaw.json`:

```jsonc
{
  "memory-tencentdb": {
    "enabled": true
  }
}
```

Default backend is local `SQLite + sqlite-vec`. Optional short-term offload (plugin ≥ 0.3.4) uses `offload.enabled` plus an OpenClaw `contextEngine` slot and a one-time `after-tool-call` patch script documented in the README.

Hermes: follow README section 2 (Docker one-command or attach `memory_tencentdb` into an existing Hermes plugin directory). The Hermes Gateway default listen port in the README is `:8420`.

---

## Agent Skills

**Status:** ⚠️ Not published as `npx skills add`

Memory is a host plugin (OpenClaw / Hermes), not a portable Agent Skills package. The architecture discusses generating Skills from traces as a layering idea; that is not the same as a published `SKILL.md` installer.

Search community skills: `npx clawhub@latest search tencentdb-agent-memory`. See: https://agentskills.io/specification

---

## MCP

**Status:** ⚠️ Not published as a standalone MCP server

Integration is the OpenClaw plugin and Hermes Gateway HTTP adapters (capture / search / recall). No official stdio MCP package is documented in the README.

---

## What It Does

TencentDB Agent Memory is a layered memory system for long-horizon agents. Short-term memory offloads verbose tool logs and keeps a compact Mermaid symbol graph with `node_id` drill-down to raw `refs/*.md`. Long-term memory builds L0 conversation → L1 atoms → L2 scenarios → L3 persona instead of a flat vector pile. GitHub description also frames a team hub of Chat Memory, Skill, LLM-Wiki, and Code-Graph assets. Official README quotes relative OpenClaw benchmark deltas (WideSearch, SWE-bench, AA-LCR, PersonaMem); treat those as upstream-reported, not independently re-measured here.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: **"Agents remember,Humans innovate."** and **"TencentDB Agent Memory = symbolic short-term memory + layered long-term memory."** GitHub: **"team-level memory hub for AI Agents"** — [repo](https://github.com/TencentCloud/TencentDB-Agent-Memory) |
| **Agent-specific primitive** | Mermaid canvas + `node_id` recovery, and L0–L3 persona layering — not a generic embedding table |
| **Autonomy-compatible control plane** | Once enabled, capture, extract, scene aggregation, persona, and pre-turn recall run automatically |
| **M2M integration surface** | OpenClaw plugin, Hermes Gateway HTTP, npm package `@tencentdb-agent-memory/memory-tencentdb` |
| **Identity / delegation** | Layered assets (persona/scene/atom) with drill-down to raw evidence. Team-hub description implies shared governed assets across agents. Optional Hermes gateway auth is off by default |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Symbolic short-term canvas** | Mermaid task map in context; full logs offloaded |
| **`node_id` trace** | Agent greps an id to recover raw tool output |
| **L0–L3 long-term pyramid** | Conversation → atom → scenario → persona |
| **Heterogeneous storage** | DB/full-text at the bottom; Markdown at the top |
| **OpenClaw / Hermes adapters** | Host-native capture and recall |

---

## Autonomy Model

```
Install OpenClaw or Hermes plugin and enable memory-tencentdb
    -> conversations and tool traces are captured
    -> layers distill atoms/scenes/persona (and optional offload)
    -> next turn receives compact structure, not the full log
    -> agent drills down via node_id when it must verify
```

---

## Identity and Delegation Model

- **Host identity:** Memory is attached to the OpenClaw/Hermes runtime you configure.
- **Traceability:** Official design keeps a path from persona/canvas back to raw L0 / refs.
- **Gateway auth:** Hermes can require tokens; both switches default off.
- **Team hub:** Repository description mentions governed, shared assets across agents/frameworks.
- **No separate KYA token.**

---

## Protocol Surface

| Interface | Detail |
|---|---|
| npm plugin | `@tencentdb-agent-memory/memory-tencentdb` |
| OpenClaw | `openclaw plugins install …` |
| Hermes Gateway | HTTP capture/search/recall (example `:8420`) |
| Local store | SQLite + sqlite-vec by default |

---

## Human-in-the-Loop Support

Positioning is that humans stop repeating SOPs. No approval gate is required for recall. Operators enable the plugin and optional offload/auth.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Flat vector memory** | Official design rejects fragment-only stores without a persona/scene pyramid |
| **Keep full tool logs in context** | Token blow-up; no `node_id` offload |
| **Chat-vendor memory** | Locked to one consumer chat product, not OpenClaw/Hermes agents |

---

## Use Cases

- **Long-horizon coding or search sessions** — keep a symbol map instead of megatokens of logs
- **Persona continuity** — preferences survive across conversations
- **Team memory hub** — shared chat/skill/wiki/code-graph assets (per GitHub description)
- **Hermes or OpenClaw runtimes** — native plugin install paths
