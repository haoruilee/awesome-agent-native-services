# LongHorizon-Harness

> **"Plan → act → verify → checkpoint or recover → repeat — until the work is actually done."**

| | |
|---|---|
| **Website** | https://lh-harness.pages.dev |
| **Docs** | https://github.com/AMAP-ML/LongHorizon-Harness#readme |
| **GitHub** | https://github.com/AMAP-ML/LongHorizon-Harness |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/AMAP-ML/LongHorizon-Harness?style=social)](https://github.com/AMAP-ML/LongHorizon-Harness) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | MIT |
| **Latest-month signal** | [v0.1.7](https://github.com/AMAP-ML/LongHorizon-Harness/releases/tag/v0.1.7) released 2026-08-20; 1,628 stars; license MIT; last push 2026-08-20; [lh-harness.pages.dev](https://lh-harness.pages.dev) returned HTTP 200 on 2026-09-26 ([repo metadata](https://api.github.com/repos/AMAP-ML/LongHorizon-Harness)) |
| **Verified at** | 2026-09-26 |

---

## Official Website

https://lh-harness.pages.dev

---

## Official Repo

https://github.com/AMAP-ML/LongHorizon-Harness

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI + agent adapters + optional computer-use plugin`

```bash
# Python 3.10+; requires Codex or Claude Code on PATH
uv tool install lh-harness

cd /path/to/project
lh-harness init
lh-harness doctor

TASK="Inspect the current directory and summarize its files."
lh-harness run --task "${TASK}" --agent codex
```

GUI tasks additionally require an explicitly installed computer-use plugin and OS permissions. No plugin is enabled by default.

---

## Agent Skills

**Status:** ⚠️ No standalone published Skill required

The harness is driven by its CLI/configuration and preserves native Codex or Claude Code behavior through adapters. Agent-specific MCP configuration can be passed per run without changing the user's global agent configuration.

---

## MCP

**Status:** ✅ Pass-through configuration

LongHorizon-Harness accepts native Claude `.mcp.json` and Codex `[mcp_servers.*]` TOML files per run, plus explicitly allowed MCP file directories. Computer-use plugins are scoped under `~/.lh-harness/` where possible rather than silently changing global registries.

---

## What It Does

LongHorizon-Harness wraps existing coding and computer-use agents in a repeated Manage–Execute–Audit loop. Every round rebuilds the next bounded step from the original goal, last verified checkpoint, failure evidence, and remaining work. The Executor starts fresh, the Auditor independently checks the real files/UI/logs/tests, and only accepted evidence becomes trusted progress. Run state survives context refreshes and failures.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Upstream calls it a **Loop Engineering system for Claude Code and Codex** that turns existing agents into long-running computer-use systems — [README](https://github.com/AMAP-ML/LongHorizon-Harness) |
| **Agent-specific primitive** | Manager/Executor/Auditor role boundaries, fresh-context episodes, verified checkpoints, failure evidence, bounded rounds, recovery, and role trajectories exist specifically for long-horizon agent loops |
| **Autonomy-compatible control plane** | Runs continue across rounds until completion, failure, input, or configured limits; per-role timeouts, max rounds, backend/model selection, and approval gates bound autonomy |
| **M2M integration surface** | `lh-harness` CLI, agent adapter protocol, TOML configuration, native MCP-config pass-through, structured run/event/report artifacts, and local service/dashboard |
| **Identity / delegation** | Each run has an isolated ID/directory; Manager, Executor, and Auditor have separate role trajectories and permission boundaries. Audit decisions bind accepted state to evidence rather than trusting the acting role's claim |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Manager** | Reconstructs verified state and chooses one bounded next step |
| **Executor** | Performs the step with a fresh context in CLI or desktop environment |
| **Auditor** | Independently inspects ground truth and accepts or rejects progress |
| **Verified checkpoint** | Only audited results become durable trusted state |
| **Failure evidence/recovery** | Rejected output informs the next attempt without becoming progress |
| **Run record** | Event stream, audit reports, role trajectories, artifacts, and final report |
| **AgentAdapter/Environment** | Pluggable backend and execution-environment boundaries |

---

## Autonomy Model

```text
Original goal + last verified state
    -> Manager selects one bounded step
    -> Executor acts with a fresh context
    -> Auditor checks actual files, UI, logs, or tests
    -> pass: checkpoint accepted evidence
       fail: record evidence and recover
    -> repeat until verified completion or configured stop condition
```

---

## Identity and Delegation Model

- **Run scope:** Every run lives under its own `runs/<run-id>/` directory with separate task state and logs.
- **Role scope:** Manager, Executor, and Auditor are responsibility boundaries; read-only auditor checks and role-specific models/timeouts reduce self-approval.
- **Workspace boundary:** Agents operate in the selected workspace while harness state remains excluded from the task surface.
- **Permission delegation:** Computer-use access is opt-in and depends on explicit OS grants; MCP files and additional read directories are passed per run.
- **Audit:** Event stream, inputs/outputs per role, audit reports, accepted checkpoints, artifacts, and final report preserve how the verified result was reached.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `lh-harness init|doctor|run|web|dashboard|plugin` |
| Configuration | Project `.lh-harness/config.toml` with per-role backend/model and limits |
| Agent adapters | Codex CLI, Claude Code, and custom `AgentAdapter` implementations |
| MCP | Native per-backend config passed into individual runs |
| Artifacts | Structured run state, event stream, role trajectories, audits, and reports |

---

## Human-in-the-Loop Support

The local workbench lets an operator answer approvals, provide mid-run instructions, stop/restart work, and inspect each plan, execution, audit, and rework decision. The loop can otherwise continue automatically within max-round and timeout limits.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Single long prompt** | Loses state on context refresh and has no independent evidence gate or recovery contract |
| **Basic retry wrapper** | Repeats the same failure without reconstructing verified progress or assigning an auditor |
| **Desktop macro recorder** | Automates actions but does not reason over goals, checkpoint accepted state, or preserve agent role trajectories |

---

## Use Cases

- **Multi-hour coding tasks** — continue through fresh contexts while preserving verified changes
- **Desktop plus CLI workflows** — move between browser, office/design tools, and shell under one goal
- **Evidence-driven operations** — require logs, tests, screenshots, or artifacts before progress is accepted
- **Recoverable research/production** — retain failures and checkpoints across interruption or agent restart
- **Cross-model role allocation** — use different backends/models for planning, execution, and independent audit
