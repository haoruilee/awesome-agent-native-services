# oh-my-codex (OMX)

> **"Start Codex stronger, then let OMX add better prompts, workflows, and runtime help when the work grows."**

| | |
|---|---|
| **Website** | https://oh-my-codex.dev |
| **Docs** | https://github.com/Yeachan-Heo/oh-my-codex/tree/main/docs |
| **GitHub** | https://github.com/Yeachan-Heo/oh-my-codex |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/Yeachan-Heo/oh-my-codex?style=social)](https://github.com/Yeachan-Heo/oh-my-codex) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | MIT (root `LICENSE` file, confirmed 2026-09-26) |
| **Latest-month signal** | [v0.21.6](https://github.com/Yeachan-Heo/oh-my-codex/releases/tag/v0.21.6) released 2026-09-21; 33,371 stars; root `LICENSE` is MIT; [oh-my-codex.dev](https://oh-my-codex.dev) returned HTTP 200 on 2026-09-26 ([repo metadata](https://api.github.com/repos/Yeachan-Heo/oh-my-codex)) |
| **Verified at** | 2026-09-26 |

---

## Official Website

https://oh-my-codex.dev

---

## Official Repo

https://github.com/Yeachan-Heo/oh-my-codex

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Codex wrapper CLI + project setup + Agent Skills`

```bash
# Requires an already-working, authenticated Codex CLI and Node.js 20+
codex --version
npm install -g oh-my-codex

# Run from the actual project root
omx setup --scope project --merge-agents
omx doctor
omx exec --skip-git-repo-check -C . "Reply with exactly OMX-EXEC-OK"

# Safer isolation for an autonomous session
omx --worktree=feat/task --xhigh
```

`--madmax` disables Codex approvals and sandboxing; it is not a safe default. Use it only in a trusted repository and preferably inside a dedicated worktree.

---

## Agent Skills

**Status:** ✅ Bundled

OMX ships workflow skills such as `$deep-interview`, `$ralplan`, `$prometheus-strict`, `$ultragoal`, `$ultrawork`, `$team`, `$ralph`, and research/review helpers. Project setup writes durable guidance to scoped `AGENTS.md`; its Codex plugin layout also mirrors supported skills.

---

## MCP

**Status:** ⚠️ Optional compatibility surface

OMX is primarily a CLI/hook harness. The official plugin layout includes optional MCP compatibility servers and app metadata, while lifecycle control remains in `omx`, Codex hooks, tmux/worktrees, and `.omx/` state.

---

## What It Does

OMX keeps Codex as the execution engine and adds a repeatable control layer for planning, durable goals, specialist roles, multi-agent teams, worktree isolation, lifecycle hooks, runtime state, replay, and operator visibility. Its canonical flow moves from clarification and plan review into checkpointed execution, with `.omx/` preserving plans, logs, memory, mission state, worker assignments, and recovery data across turns.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The official project calls itself a workflow layer for Codex and says it adds prompts, workflows, and runtime help as agent work grows — [README](https://github.com/Yeachan-Heo/oh-my-codex) |
| **Agent-specific primitive** | Durable goals, role routing, team worker assignments, mailboxes, authority leases, lifecycle continuation, dispatch/replay events, and session-scoped state exist only to operate agent loops |
| **Autonomy-compatible control plane** | Ultragoal/Ultrawork/Ralph continuation, bounded team execution, worktree isolation, cancellation, doctor checks, and fail-closed authority gates support unattended progress within explicit modes |
| **M2M integration surface** | `omx` CLI, JSON commands/events/snapshots, Codex lifecycle hooks, Agent Skills, plugin metadata, and optional MCP compatibility |
| **Identity / delegation** | Leader/worker IDs, task assignments, lease IDs, session-owner sidecars, dispatch delivery events, replay cursors, and audited state mutations separate authority and attribute work. Where Codex lacks host-verifiable leader or consensus proof, security-sensitive adapted flows fail closed rather than minting local trust |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Workflow spine** | Clarify, review a plan, then execute through durable goal/worker loops |
| **Durable `.omx/` state** | Plans, logs, memory, goals, missions, events, and checkpoints |
| **Team runtime** | Leader/worker assignments, mailboxes, tmux panes, and isolated worktrees |
| **Authority and replay** | Lease acquisition/renewal, dispatch events, snapshots, replay cursors, deduplication |
| **Native hooks** | Session, tool, compaction, prompt, stop, and continuation lifecycle adapters |
| **Diagnostics** | `omx doctor`, runtime smoke checks, state/status surfaces, and HUD support |

---

## Autonomy Model

```text
Scoped project setup establishes durable AGENTS.md guidance
    -> Codex session starts through OMX
    -> clarification and plan roles produce approved state
    -> durable goal loop assigns bounded work, optionally to team workers
    -> hooks record progress and continue non-terminal workflows
    -> independent review/checkpoints accept, retry, recover, or block
    -> final state and evidence remain under .omx/ and git
```

---

## Identity and Delegation Model

- **Session scope:** Project/user setup and per-session runtime homes prevent accidental cross-project state sharing.
- **Team identity:** Workers carry durable IDs and explicit task assignments; leader authority uses time-bounded leases.
- **Attribution:** JSONL events record authority, dispatch, delivery, worker assignment, stalls, recovery, and run state.
- **Fail-closed boundary:** Current Codex native hooks do not always provide non-user-mintable proof of the root leader or a host-issued consensus receipt. OMX documents this and denies affected authority transitions.
- **License:** Root `LICENSE` is MIT as of 2026-09-26. GitHub identifies that file as MIT. The earlier "no root license file" caveat no longer applies.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `omx` setup, launch, exec, doctor, state, team, session, and workflow commands |
| Hooks | Official Codex plugin-scoped hooks plus documented runtime fallbacks |
| Skills | Bundled Codex skills and specialist workflows |
| State/events | Structured JSON/JSONL command, event, snapshot, mission, and checkpoint artifacts |
| Runtime | Codex CLI, tmux/psmux where supported, and Git worktrees |

---

## Human-in-the-Loop Support

Planning/review workflows can require human approval before durable execution. Codex approval and sandbox policy remain configurable, Stop hooks can block premature completion, and the operator can steer/cancel a run. Autonomous modes are opt-in and their risk depends on the underlying Codex permissions.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Plain Codex CLI** | No OMX workflow catalog, durable goal ledger, team mailbox/lease model, or cross-turn recovery state |
| **Prompt collection** | Cannot own sessions, worktrees, hooks, assignments, replay, or completion gates |
| **Human-only HUD** | Displays activity but does not provide the machine control plane that assigns, continues, or authorizes agent work |

---

## Use Cases

- **Long Codex projects** — preserve objectives, plans, checkpoints, and recovery state across turns
- **Parallel implementation** — assign isolated stories to team workers in separate worktrees
- **Adversarial planning** — clarify, critique, and approve architecture before mutations begin
- **Autonomous completion loops** — keep a bounded owner working until verified exit criteria pass
- **Auditable harness operations** — inspect structured lifecycle, authority, dispatch, and replay events
