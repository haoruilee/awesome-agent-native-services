# Beads

> **"Dependency-aware, Dolt-backed issue tracker built for AI coding agents that survive context loss"**

| | |
|---|---|
| **Website** | https://beads.gascity.com |
| **Docs** | https://beads.gascity.com |
| **GitHub** | https://github.com/gastownhall/beads |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/gastownhall/beads?style=social)](https://github.com/gastownhall/beads) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push 2026-09-03 ([repo metadata](https://api.github.com/repos/gastownhall/beads)); Homebrew `beads`, npm `@beads/bd`, PyPI `beads-mcp` |
| **Verified at** | 2026-09-03 |

---

## Official Website

https://beads.gascity.com

Docs H1 quote (live 2026-09-03): **"Dependency-aware, Dolt-backed issue tracker built for AI coding agents that survive context loss"**

---

## Official Repo

https://github.com/gastownhall/beads

README H1 is `bd - Beads`. Supporting line: **"Distributed graph issue tracker for AI agents, powered by Dolt."** GitHub description: **"Beads - A memory upgrade for your coding agent"**

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + optional MCP / agent setup recipes

```bash
brew install beads
# or: curl -fsSL https://raw.githubusercontent.com/gastownhall/beads/main/scripts/install.sh | bash
# or: npm install -g @beads/bd

cd your-project
bd init --quiet
bd setup claude    # also: codex, cursor, factory, mux, gemini, copilot, …
bd ready --json
```

`bd init` writes `AGENTS.md` and project Claude/Codex integrations unless `--skip-agents` or `--stealth`. `bd prime` injects workflow context and `bd remember` memories. JSON is the agent path: `bd list --json`, `bd show <id> --json`.

MCP-only hosts (Claude Desktop, no shell):

```bash
pip install beads-mcp
# or: uv tool install beads-mcp
```

Then point the host at `"command": "beads-mcp"`.

There is no URL-onboarding document. Docs expose `https://beads.gascity.com/llms.txt` as a documentation index, not a join protocol.

---

## Agent Skills

**Status:** ✅ Bundled with `bd setup` (not `npx skills add`)

| Skill | What It Teaches the Agent |
|---|---|
| Codex beads skill | `.agents/skills/beads/SKILL.md` installed by `bd setup codex` — when to `bd ready` / `bd claim` / `bd close` |
| `bd prime` workflow | SessionStart hook injects commands, ready work, and `bd remember` memories |
| `bd onboard` snippet | Printed AGENTS.md block for unsupported hosts |

```bash
npx clawhub@latest search beads
```

---

## MCP

**Status:** ✅ Available — optional; the primary surface is the `bd` CLI

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/gastownhall/beads (`beads-mcp` on PyPI) |
| **Transport** | stdio (`beads-mcp`) |
| **Compatible Clients** | VS Code Copilot, Claude Desktop, and any MCP host |
| **Official note** | Docs: MCP is for hosts without a shell; CLI + `bd prime` is preferred (tool schemas cost 10–50k tokens) |

---

## What It Does

Beads (`bd`) is a **dependency-aware work graph** for coding agents, stored in a [Dolt](https://github.com/dolthub/dolt) version-controlled SQL database. Official docs: traditional trackers were not designed for agents; Beads uses hash IDs (`bd-a1b2`) so concurrent agents do not collide, `bd ready` so an agent only claims unblocked work, and Dolt push/pull so the graph survives context loss across machines.

This is **not fact memory**. Distinct from [LycheeMem](lycheemem.md) (working/semantic/procedural stores), [agentmemory](agentmemory.md) (shared memory server), and [Claude-Mem](claude-mem.md) (tool-call firehose + compression): Beads tracks issues, blockers, formulas/molecules, and `bd remember` project insights as a **work graph**, not a fact/RAG store.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs: **"Dependency-aware, Dolt-backed issue tracker built for AI coding agents that survive context loss"** — [beads.gascity.com](https://beads.gascity.com). README: **"Distributed graph issue tracker for AI agents, powered by Dolt."** |
| **Agent-specific primitive** | Hash-based IDs; `bd ready` unblocked-work queue; `bd update --claim`; formulas/molecules/gates; `bd remember` + `bd prime` session injection |
| **Autonomy-compatible control plane** | After `bd init` / `bd setup`, SessionStart hooks run `bd prime`; agents create, claim, and close beads with `--json` and no dashboard click. Git authority is gated by `agent.profile` (`conservative` default) |
| **M2M integration surface** | `bd` CLI (JSON), `beads-mcp`, `bd setup <agent>` recipes, Homebrew/npm/install.sh |
| **Identity / delegation** | Hash IDs + `--claim` assignee; `prepare-commit-msg` **agent identity trailers**; Dolt audit history. **C5 note:** no hosted KYA token — identity is the local/Dolt actor plus optional `BD_AGENT_PROFILE`. `team-maintainer` must be set explicitly; Beads does not infer commit/push authority from a remote |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Bead** | Work item with priority, type, labels, dependencies |
| **`bd ready`** | Only unblocked, claimable work |
| **`bd update --claim`** | Atomic assignee + `in_progress` |
| **Dependencies** | `blocks`, `parent-child`, `discovered-from`, `related` |
| **Formulas / molecules / gates** | Declarative workflow templates, instantiated graphs, async human/timer/GitHub gates |
| **`bd remember` / `bd prime`** | Persistent project insights injected at session start |
| **Dolt sync** | `bd dolt push` / `bd dolt pull` — the DB is the source of truth |
| **Hash IDs** | `bd-a1b2` (hierarchical `bd-a3f8.1.1`) — collision-safe multi-agent IDs |

---

## Autonomy Model

```
Operator installs bd and runs `bd init` (+ optional `bd setup <agent>`)
    -> SessionStart / AGENTS.md tells the agent to run `bd prime`
    -> Agent lists `bd ready --json`, claims a bead, implements, closes
    -> Discovered work is `bd create … --deps discovered-from:<id>`
    -> `bd dolt push` shares the graph (when the profile allows)
```

No per-action human confirmation on the issue graph. Commit/push stays conservative unless `agent.profile=team-maintainer`.

---

## Identity and Delegation Model

- **Issue identity:** Hash IDs prevent two agents from minting the same key.
- **Claim:** `--claim` records the acting agent as assignee.
- **Audit:** Dolt history plus `bd show` trail; git hooks add agent identity trailers.
- **Authority knob:** `conservative` (default) vs `team-maintainer` for commit/`bd dolt push`.
- **No hosted agent passport.** Stealth / `--contributor` modes keep planning beads out of shared PRs.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `bd` — `--json` on list/show/create |
| MCP | `beads-mcp` stdio |
| Agent setup | `bd setup claude\|codex\|cursor\|…` |
| Sync | `bd dolt push` / `bd dolt pull` |
| Docs | https://beads.gascity.com — also `/llms.txt` index |

---

## Human-in-the-Loop Support

Gates can wait on a human, a timer, or GitHub. `conservative` profile tells the agent to report diffs and not commit. Aider integration is explicitly human-run (`/run`). The operational loop for claim/close does not require a tracker UI.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **GitHub Issues / Jira** | Human dashboards; no `bd ready` graph, hash IDs, or `bd prime` injection |
| **LycheeMem / agentmemory / Claude-Mem** | Fact or session memory. Beads is a **work graph** (issues, blockers, formulas), not a recall store |
| **Markdown TODO in the repo** | No dependency-aware ready queue, no collision-safe IDs, no Dolt sync |

---

## Use Cases

- **Long-horizon coding agents** that lose the chat but must resume the next unblocked bead
- **Multi-agent / multi-clone work** — hash IDs + Dolt remotes
- **Discovered-from bugs** — create a child bead mid-implementation without a human filing it
- **Session priming** — `bd prime` + `bd remember` instead of rewriting MEMORY.md
