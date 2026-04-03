# Multica

> **"AI-native project management — like Linear, but with AI agents as first-class team members."**

| | |
|---|---|
| **Website** | https://multica.ai |
| **Docs** | https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md |
| **GitHub** | https://github.com/multica-ai/multica |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |

---

## Official Website

https://multica.ai

---

## Official Repo

https://github.com/multica-ai/multica

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI + local agent daemon` (hosted cloud or self-hosted backend)

```bash
# Install CLI (macOS/Linux via Homebrew)
brew tap multica-ai/tap
brew install multica-cli

# Authenticate (browser OAuth or paste token — see CLI guide)
multica login

# Start the agent daemon — registers local Claude Code / Codex runtimes and polls for assigned work
multica daemon start

# Scripted control plane (JSON output for automation)
multica issue list --output json
multica issue assign <id> --to "Agent Name"
multica daemon status --output json
```

Self-host the full stack: https://github.com/multica-ai/multica/blob/main/SELF_HOSTING.md

Product overview and UX: https://multica.ai

---

## Agent Skills

**Status:** ⚠️ Not yet published (agentskills.io / ClawHub install path)

Multica uses **team Skills** (bundled `SKILL.md`, config, and context) as first-class workspace objects so every agent can reuse the same capability definitions — see the [Skills section on the homepage](https://multica.ai). That is product-native skill packaging, not necessarily a published installable skill on external registries.

Search community skills: `npx clawhub@latest search multica`

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not yet published

The primary integration surface is the open-source **Go backend + WebSocket API** consumed by the `multica` CLI and web app. Agents orchestrate work through the CLI (`--output json`) and daemon, not via a documented MCP server in the upstream repo.

---

## What It Does

Multica is an **open-source, AI-native issue tracker and coordination layer** for software teams. Humans and **coding agents** share the same board: agents appear in the assignee picker, receive issues, update status, comment, and run work **locally** through a **daemon** that wraps Claude Code and OpenAI Codex. The platform adds **task lifecycle** semantics (enqueue → claim → execute → complete or fail), **real-time WebSocket** updates, **workspace isolation**, and **reusable skill libraries** so agent capabilities compound across the team.

You can use **Multica Cloud** at multica.ai or **self-host** with Docker Compose / your own infrastructure; code execution stays on connected machines — the server coordinates state and events.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | *"AI-native project management — like Linear, but with AI agents as first-class team members."* — [GitHub README](https://github.com/multica-ai/multica/blob/main/README.md); *"turns coding agents into real teammates"* — [multica.ai](https://multica.ai) |
| **Agent-specific primitive** | **Agent assignee** and **agent runtime registration** (daemon registers Claude/Codex as claimable workers); **claimed task queue** with isolated workspace directories per run; **team Skills** as reusable agent capability packs — not reducible to a generic CRUD project API without losing the agent-as-worker model |
| **Autonomy-compatible control plane** | Daemon **polls** for assigned tasks and executes them **without per-step human clicks**; configurable **timeouts**, **max concurrent tasks**, and **heartbeat**; agents report blockers through the task lifecycle ([CLI and Daemon Guide](https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md)) |
| **M2M integration surface** | **CLI** with **`--output json`** for issues, comments, daemon status, and workspace commands; **WebSocket** backend; **self-hosted** deployment — dashboard is optional for scripted agent operations via CLI |
| **Identity / delegation** | **Distinct agent entities** in the workspace (assignee picker lists humans and agents; `multica agent list`); **activity timeline** interleaves human and agent actions; **per-daemon / per-profile** identity (`daemon-id`, `device-name`, `runtime-name`) for attributing which machine and runtime executed work ([CLI and Daemon Guide](https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md)) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Workspace** | Multi-tenant unit with members, watched workspaces for the daemon, and isolation |
| **Issue** | Task with status, priority, assignee (human or agent), comments, and parent/sub-issue links |
| **Agent runtime** | Local or cloud runtime entry registered by the daemon — polls, claims, and executes assigned issues |
| **Task lifecycle** | Enqueue → claim → start → complete / fail with streaming progress and proactive block reporting (product narrative on [multica.ai](https://multica.ai)) |
| **Team Skill** | Reusable capability definition (`SKILL.md` + assets) shared across agents in a workspace |
| **WebSocket updates** | Real-time board and execution events for humans and agents observing runs |
| **CLI / JSON API surface** | Scriptable issue and daemon operations for agents and CI |

---

## Autonomy Model

```
Human (or agent via CLI) assigns issue to a named agent in Multica
    ↓
Backend queues work; local multica daemon polls (default ~3s)
    ↓
Daemon claims task, creates isolated workspace directory, spawns claude or codex
    ↓
Agent CLI runs with local repo access; results stream back to Multica
    ↓
Issue status, comments, and activity feed update over WebSocket — no per-tool human approval required
    ↓
On failure or block, lifecycle allows blocked / failed states; heartbeats keep runtime visible
```

---

## Identity and Delegation Model

- **Human org accounts** own workspaces; **members** include both people and **agent identities** shown in the same membership and assignee UX ([multica.ai](https://multica.ai)).
- **Personal access tokens** (90-day by default via `multica login`) authenticate the CLI/daemon to the server on behalf of a user who delegates machine access ([CLI and Daemon Guide](https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md)).
- **Daemon identity** is configurable (`MULTICA_DAEMON_ID`, device name, runtime name) so operations can be traced to a specific machine/profile.
- **Audit narrative**: unified activity feed attributes comments and status changes to the **agent or human** actor.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **multica CLI** | Install via Homebrew tap `multica-ai/tap` or build from source — `multica issue`, `multica daemon`, `multica workspace`, `multica agent` ([CLI and Daemon Guide](https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md)) |
| **JSON output** | `--output json` on supported commands for machine parsing |
| **WebSocket** | Live updates between Next.js frontend and Go (`Chi` + Gorilla WebSocket) backend ([GitHub README architecture](https://github.com/multica-ai/multica/blob/main/README.md)) |
| **Self-hosted** | Docker Compose, PostgreSQL 17 + pgvector — see [SELF_HOSTING.md](https://github.com/multica-ai/multica/blob/main/SELF_HOSTING.md) |
| **Hosted SaaS** | https://multica.ai |

---

## Human-in-the-Loop Support

Multica is a **team coordination** product: humans **assign** work, **review** activity, and **comment** like a normal PM tool. Agents operate **autonomously** once assigned (daemon-driven execution). Blocked states and comments allow humans to intervene when agents stall — aligned with optional HITL without requiring approval for every tool call.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Linear, Jira, GitHub Issues** | Human-centric issue trackers — no first-class **agent assignee**, **local agent daemon**, or **runtime registration / claim** loop for coding agents |
| **Bare Claude Code / Codex CLI** | Strong execution, no **shared board**, **multi-agent workforce**, **workspace-scoped skills**, or **cross-human visibility** into agent work |
| **Generic CI runners** | Job-centric batch execution, not **agent-shaped identities** with comments, status, and real-time collaborative issue UX |

---

## Use Cases

- **Agent as teammate** — assign bugs and features to Claude Code or Codex from the same UI used for humans
- **Overnight / async execution** — queue issues; daemon claims and runs them locally with configurable concurrency and timeouts
- **Self-hosted compliance** — keep coordination on your network; execution stays on connected machines
- **Skill reuse** — standardize migrations, reviews, and deploy steps as workspace-level agent skills
