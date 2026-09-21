# LoopX

> **"The open, provider-neutral, stateful control plane for long-horizon agents."**

| | |
|---|---|
| **Website** | https://loopx-project.github.io/loopx/ |
| **Docs** | https://loopx-project.github.io/loopx/docs/ |
| **GitHub** | https://github.com/loopx-project/loopx |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/loopx-project/loopx?style=social)](https://github.com/loopx-project/loopx) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-08-19 (verified the same day) |
| **Verified at** | 2026-08-19 |

---

## Official Website

https://loopx-project.github.io/loopx/

---

## Official Repo

https://github.com/loopx-project/loopx

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + **workflow skills**

```bash
python3 -m pip install --upgrade loopx
loopx workflow-skills --install
loopx doctor
cd /path/to/your-project
loopx connect
loopx status
```

If state is missing:

```bash
loopx start-goal --guided --project . --goal-text "Your long-running objective"
```

Official getting-started doc tells an already-running coding agent to connect the project, install from PyPI if needed, run `loopx doctor`, and reuse existing `.loopx/` state. Host-specific drivers (Codex App heartbeat, Claude Code `/loop`, OpenCode facade, and others) are listed in the README.

---

## Agent Skills

**Status:** ✅ Available (installer-registered workflow skills)

```bash
loopx workflow-skills --install
```

The installer registers LoopX command-family skills on host surfaces (for example Codex `~/.codex/skills/loopx*`). Invoke via `$loopx` or `/skills` where the host requires it.

| Skill | What It Teaches the Agent |
|---|---|
| LoopX command facade | Project connect, status, gates, todos, quota |
| LoopX Project workflow | Longer governed-loop protocol for the current goal |

Exact names depend on the host surface; `loopx workflow-skills --install` is the official registration command.

---

## MCP

**Status:** ⚠️ Not the primary surface

LoopX is a local-first CLI/state kernel that sits on top of existing harnesses. No official standalone MCP server is advertised as the default integration in the README.

Search community skills: `npx clawhub@latest search loopx`. See: https://agentskills.io/specification

---

## What It Does

LoopX is a provider-neutral control plane for work that outlives one chat turn. It keeps objectives, gates, todos, evidence, quota, and handoffs while Codex, Claude Code, Cursor, or another harness executes a bounded slice. Registered agents are peers that claim leases; humans keep dangerous permissions and final ownership. Official text: it is not an autonomous production controller.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: **"The open, provider-neutral, stateful control plane for long-horizon agents."** — [loopx-project/loopx](https://github.com/loopx-project/loopx) |
| **Agent-specific primitive** | Durable loop state (objective, gates, todos, evidence, quota) plus claim/lease/handoff operators — an agent-native Kanban, not a chat log |
| **Autonomy-compatible control plane** | Bounded agent slices run without a click; quota decides the next tick. Human gates fire only when the state kernel says judgment is required |
| **M2M integration surface** | `loopx` CLI, workflow skills, host adapters, local `.loopx/` state |
| **Identity / delegation** | Goal/state ids, agent ids, claims and leases. No durable leader identity required. Dangerous writes stay with the human |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Objective / goal state** | Durable goal plus `ACTIVE_GOAL_STATE` |
| **Gates** | Owner, safety, publication, or private-data stops |
| **Todos + evidence** | Continuation the next turn can read |
| **Quota** | Whether another tick should run |
| **Claim / lease / handoff** | Peer agents take and pass work |
| **Doctor / connect** | Machine-checkable project health |

---

## Autonomy Model

```
pip install loopx -> workflow-skills --install -> connect project
    -> harness executes one bounded turn
    -> LoopX writes evidence, handoff, next todo
    -> quota / scheduler_hint decides the next tick
    -> if human judgment is required, ask and wait
    -> else continue or stop
```

---

## Identity and Delegation Model

- **State identity:** `.loopx/registry.json` and goal-state files.
- **Agent identity:** Registered peer agents with claims and leases; no required leader id.
- **Human ownership:** Publishing, production writes, and final authority stay human.
- **Ignore rules:** `.loopx/`, `.codex/goals/`, and `.local/` must not be committed.
- **Not a cloud IAM product:** Local-first control plane.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `loopx connect`, `doctor`, `status`, `start-goal`, `workflow-skills` |
| Skills | Host-registered LoopX command/workflow skills |
| State | `.loopx/`, goal-state markdown |
| Host adapters | Codex App, Claude Code, OpenCode, Pi, KunlunCode, Cursor/shell |

---

## Human-in-the-Loop Support

Explicit. Official line: **"Keep the loop moving. Keep the judgment human."** Gates ask a concrete question and wait. LoopX is not unattended production control; showcased multi-day runs are evidence of governed loops, not a promise of unattended prod autonomy.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Chat memory + cron** | No gates, evidence, or claim/lease semantics |
| **Generic project board** | Human tickets, not agent-claimable loop state |
| **Single-session harness** | Drops objective/evidence across context refreshes |

---

## Use Cases

- **Multi-day engineering or research objectives**
- **Issue/PR loops** that must keep scope and review evidence
- **Peer-agent teams** with leases and handoff
- **Heartbeat / monitor work** gated by quota
