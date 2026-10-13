# DeepSeek Harness (dsh)

> **"Everything is a Plugin."**

| | |
|---|---|
| **Website** | https://deepseek.com/harness |
| **Docs** | https://deepseek.com/harness |
| **GitHub** | https://github.com/deepseek-ai/deepseek-harness |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/deepseek-ai/deepseek-harness?style=social)](https://github.com/deepseek-ai/deepseek-harness) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push 2026-08-21 ([repo metadata](https://api.github.com/repos/deepseek-ai/deepseek-harness)); developer-preview release with public Web UI entry (`npx @deepseek-ai/dsh web`) |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://deepseek.com/harness

---

## Official Repo

https://github.com/deepseek-ai/deepseek-harness

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + Web UI (developer preview)

```bash
npx @deepseek-ai/dsh web
```

The official homepage and README both give that command as the fastest start. After Node.js is installed, it starts the Web UI at `http://127.0.0.1:3080` by default and opens a browser on a local launch. Pass `--no-open` to keep the server headless. From a checkout:

```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```

The repository also documents an ACP automation server and a headless profile (`pnpm dsh --profile headless "task"`). There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

The harness treats Skills as a first-class plugin (`packages/skill/` — skill provider registry, local impl, catalog/loader tool). Community plugins use the [`dsh-plugin`](https://github.com/topics/dsh-plugin) GitHub topic.

```bash
npx clawhub@latest search deepseek-harness dsh
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not published as a standalone MCP server.

The primary machine surfaces are the `dsh` CLI, Web UI, JSON-RPC SDK, and an automation-only Agent Client Protocol (ACP) server. MCP clients can still sit beside dsh as ordinary tools; dsh itself is the harness, not an MCP product.

| Detail | Value |
|---|---|
| **Primary interface** | `npx @deepseek-ai/dsh web` / `pnpm dsh` |
| **Other machine surfaces** | ACP server, JSON-RPC SDK, session event log |
| **Compatible clients** | Local Web UI, ACP hosts, any agent that can run the CLI |

---

## What It Does

DeepSeek Harness (`dsh`) is DeepSeek AI's open-source agent harness. Official positioning is that a model is the agent's soul and the harness is what lets the agent understand its environment, use tools, and keep working in real scenes. Every agent capability — model, tools, skills, session, sandbox, storage, loop, scheduling, UI — is a Cordis plugin. Developers compose or replace those plugins in configuration without forking the harness.

The product is a **developer preview**. The README warns there will be compatibility-breaking changes. The homepage lists four run modes: Standard (full coding agent), PTC (standard tools plus a Code Mode TypeScript program that batches tool calls), Minimal (persistent bash + `str_replace_editor` for model benchmarks), and Create (inspect the runtime, experiment with plugins, author new presets).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | GitHub description: **"DeepSeek Harness: Everything is a Plugin."** — [repo](https://github.com/deepseek-ai/deepseek-harness). Homepage: **"Harness 让 Agent 在真实场景中持续工作"** / **"Agent = Model + Harness"** — [deepseek.com/harness](https://deepseek.com/harness) |
| **Agent-specific primitive** | Cordis plugin seams for model, tools, skills, session, sandbox, storage, loop, scheduling, and UI; append-only session logs that record system prompts, chain-of-thought, tool calls, sub-agent dispatch, and context injection; Trajectory view for resume, fork, retrieve, and replay |
| **Autonomy-compatible control plane** | Once a profile starts, the agent loop runs tools, skills, plans, goals, sub-agents, and workflows without per-action human confirmation. PTC mode lets the model compose multi-step tool work in one generated program |
| **M2M integration surface** | `npx @deepseek-ai/dsh web`, source CLI, ACP server, JSON-RPC SDK, Python SDK, session event stream |
| **Identity / delegation** | Sessions are the attributable unit. Official copy: everything the model sees is written to an append-only session log, and resume/fork/retrieve/replay share that event stream. The repo also has identity, credentials, and permission/ask-user plugins. dsh does not mint a separate payment or KYA identity |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Cordis plugin** | Every agent capability is a loadable plugin; the kernel only loads, unloads, and resolves dependencies |
| **Preset / profile** | Configuration-layer composition of plugins (Standard, PTC, Minimal, Create, or a custom preset) |
| **Session event log** | Append-only record of model-visible inputs, tool results, sub-agent dispatch, and context injection |
| **Trajectory view** | Operator/agent surface for inspecting, resuming, forking, and replaying the same event stream |
| **PTC / Code Mode** | Model writes a TypeScript program that batches multiple tool calls |
| **Skill / sub-agent / workflow plugins** | First-class plugin packages for skills, delegated sub-agents, and worker-thread workflows |
| **ACP server** | Automation-only Agent Client Protocol surface for hosts that speak ACP |

---

## Autonomy Model

```
Operator or coding agent starts dsh (npx @deepseek-ai/dsh web or a headless profile)
    -> Cordis loads the selected preset's plugins (model, tools, skills, sandbox, loop, UI)
    -> Agent loop plans and calls tools / skills / sub-agents without per-step human clicks
    -> Every model-visible event is appended to the session log
    -> Trajectory view can resume, fork, retrieve, or replay from that log
    -> Optional ask-user / approval plugins pause only when the preset enables them
```

Human setup is install + profile selection. The loop itself is autonomous inside a started session.

---

## Identity and Delegation Model

- **Session identity:** Each run writes an append-only session log. Official docs treat that log as the shared source for resume, fork, retrieve, and replay.
- **Plugin-scoped credentials:** Credential and authorization plugins sit beside env/`.env` providers. Secrets stay in operator-controlled config, not a minted per-agent wallet.
- **Delegation:** Sub-agent plugins dispatch child agents; the parent session remains the audit root.
- **No product-wide approval gate:** Interaction/approval plugins exist, but they are optional composition, not a required HITL product.
- **Preview boundary:** Developer preview. Compatibility-breaking changes are expected; backends reject old on-disk formats.

---

## Protocol Surface

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

## Human-in-the-Loop Support

The Web UI and Trajectory view are operator surfaces: watch a run, inspect what the model saw, resume or fork a session. Optional interaction plugins can ask the user or require permission. After a profile starts, the agent does not wait for per-action confirmation unless those plugins are composed in.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A raw model API** | Supplies tokens only. It has no plugin harness, session log, or trajectory replay |
| **A generic chatbot UI** | Humans chat; it does not treat tools, skills, sandbox, loop, and scheduling as replaceable agent plugins |
| **Agent Executor (AX)** | AX is a distributed harness *runtime* (isolated environments + event log). dsh is DeepSeek's plugin-composed coding harness and local control plane, not a K8s compute control plane |

---

## Use Cases

- **Plugin-composed coding agents** — run Standard or PTC mode against a repo with file, shell, search, skills, and sub-agents
- **Model benchmarking** — Minimal mode keeps only bash + `str_replace_editor`
- **Custom harness research** — Create mode inspects the runtime and authors new presets without forking core
- **Session replay** — recover, fork, or audit a run from the append-only event stream
