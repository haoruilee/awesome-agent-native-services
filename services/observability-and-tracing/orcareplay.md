# OrcaReplay

> **"Records a coding agent below the harness and replays the run offline, or forks it from a checkpoint onto a different model."**

| | |
|---|---|
| **Website** | https://github.com/Continuum-AI-Corp/OrcaReplay |
| **Docs** | https://github.com/Continuum-AI-Corp/OrcaReplay/tree/main/docs |
| **GitHub** | https://github.com/Continuum-AI-Corp/OrcaReplay |
| **Latest-month signal** | [Created 2026-08-29](https://api.github.com/repos/Continuum-AI-Corp/OrcaReplay); [`orcareplay@0.2.1` published 2026-09-07](https://www.npmjs.com/package/orcareplay); [active on `main` 2026-09-07](https://github.com/Continuum-AI-Corp/OrcaReplay/commits/main); **168 stars** on 2026-09-07 UTC ([GitHub metadata snapshot](https://api.github.com/repos/Continuum-AI-Corp/OrcaReplay)) |
| **Verified at** | 2026-09-07 |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |
| **License** | Apache-2.0 |

---

## Official Website

The GitHub repository is the canonical project and documentation site:

https://github.com/Continuum-AI-Corp/OrcaReplay

---

## Official Repo

https://github.com/Continuum-AI-Corp/OrcaReplay

---

## How to Use (Agent Onboarding)

**Interaction pattern:** local CLI wrapper (process + socket interception) + stdio MCP server

Install and record a session. The agent runs unmodified; two environment variables are set for it.

```bash
npm i -g orcareplay
orca doctor
orca record claude
```

Read, replay, or fork a recorded run:

```bash
orca show <run-id>
orca replay <run-id>
orca fork <run-id> --at 7 --model gpt-5
```

For agents that read no base-URL variable at all, capture a level lower:

```bash
orca record exec --tls-intercept -- <command>
```

---

## Agent Skills

**Status:** ✅ Published — [`skills/orca-replay/SKILL.md`](https://github.com/Continuum-AI-Corp/OrcaReplay/tree/main/skills/orca-replay), also on ClawHub.

```bash
npx clawhub@latest search orca-replay
```

The skill instructs an agent to answer questions about a past run from the recording rather than from memory, and to keep what the trace shows separate from what it is inferring.

---

## MCP

**Status:** ✅ MCP server published (stdio).

| Detail | Value |
|---|---|
| **MCP role** | Exposes recorded runs so another agent can read, replay, or compare them |
| **Tools (6)** | `orca_list_runs`, `orca_show_run`, `orca_checkpoints`, `orca_graph`, `orca_replay`, `orca_compare` |
| **Protocol** | `2025-06-18`, verified against the published `orcareplay@0.2.1` |
| **Transport** | stdio (`npx -y orcareplay mcp`) |
| **Also observes MCP** | A JSON-RPC tee records the MCP calls a recorded agent made, on the same timeline as the model traffic |

---

## What It Does

OrcaReplay captures an agent's trajectory at the process and socket boundary rather than through an SDK, so nothing needs to be added to the agent. Five layers cooperate: a loopback proxy for the model traffic, a PATH shim for shell commands and their exit codes, an MCP JSON-RPC tee, a shadow git index for per-turn file changes, and a `fetch` hook for hardcoded origins. Everything lands on one timeline, which is what lets you ask which tool call sent the run down the wrong branch.

Two capabilities distinguish it from tracing. `orca replay` serves the recorded responses back with the network off, so the harness runs again against a fixed transcript — an intermittent agent failure becomes a fixture. `orca fork` restarts a recorded run from a chosen checkpoint against a different model, with every earlier turn still served from the recording, so two models face byte-identical context and file state.

Bounds, stated rather than implied. The byte-for-byte guarantee is conditional: it holds when the prompt was recorded through argv (`orca record claude -- -p "…"`). A hand-driven terminal session replays the conversation but not the run byte for byte, because the harness makes calls for itself that a replay does not repeat and interactive-only tools such as `AskUserQuestion` are absent without a person. Replay proves the recorded decisions still reproduce; it cannot prove a fresh run would fail the same way, since the model is not asked again. `orca compare` uploads recorded context to third-party providers and spends real money, so it requires explicit approval.

Supported harnesses today: Claude Code, Codex CLI (API key and ChatGPT-subscription login), opencode, Qwen Code, Cursor, grok-cli, MiMo, Kilo.

---
