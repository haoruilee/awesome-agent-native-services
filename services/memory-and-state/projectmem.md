# projectmem

> **"We don't make AI smarter. We make it experienced."**

| | |
|---|---|
| **Website** | https://www.projectmem.dev |
| **Docs** | https://www.projectmem.dev |
| **GitHub** | https://github.com/riponcm/projectmem |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/riponcm/projectmem?style=social)](https://github.com/riponcm/projectmem) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push 2026-09-01 ([repo metadata](https://api.github.com/repos/riponcm/projectmem)); PyPI `projectmem` v0.3.1 — one MCP server for every project |
| **Verified at** | 2026-09-03 |

---

## Official Website

https://www.projectmem.dev

Homepage H1 (live 2026-09-03): **"We don't make AI smarter. We make it experienced."** Supporting line: **"Local-first, open-source coding agent memory for Claude Code, Cursor, Codex, Antigravity and every MCP agent"**

---

## Official Repo

https://github.com/riponcm/projectmem

README repeats the same H1. GitHub description: open-source coding-agent memory that records issues, attempts, fixes, and decisions, then warns before the agent repeats a failed approach.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / CLI` + MCP

```bash
pip install -U projectmem
pjm doctor
pjm doctor --fix
pjm init    # per repo — writes .projectmem/ and git hooks
```

One MCP server serves every registered project (no `--root`):

```json
{
  "mcpServers": {
    "projectmem": {
      "command": "/absolute/path/to/python",
      "args": ["-m", "projectmem.mcp_server"]
    }
  }
}
```

`pjm init` prints this block with the local Python path. Fast-restart the client after editing MCP config. Optional: `pjm wrap claude` injects a token-budgeted memory block before the session.

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

```bash
npx clawhub@latest search projectmem
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — native stdio server, 17 tools (homepage); README comparison table also says “15 focused tools”

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/riponcm/projectmem |
| **Transport** | stdio (`python -m projectmem.mcp_server`) — no persistent server |
| **Compatible Clients** | Claude Desktop, Claude Code, Cursor, Antigravity, Codex, and any MCP client |
| **Tools (upstream)** | Distilled summary + per-issue fetch; agent reads memory and logs work on its own |

---

## What It Does

projectmem is a **local-first typed event log** plus a **pre-action judgment gate** for coding agents. Memory lives in `.projectmem/` (append-only `events.jsonl`: issues, attempts, fixes, decisions, notes). Git hooks classify commits (`revert` → failed attempt, `fix:` → fix). `pjm precheck` warns *before* a commit if the staged files match a failed approach.

**Judgment, not just recall:** official positioning is “memory + judgment” — stale memories are flagged, never silently deleted; `pjm score` reports a Prevention Score (hours/tokens/dollars). Cross-project gotchas live in `~/.projectmem/global/`. No cloud, no account, no telemetry (optional `--online` update check only).

Distinct from [Claude-Mem](claude-mem.md) (session firehose) and [agentmemory](agentmemory.md) (shared memory server): projectmem’s contract is a **typed development log** and a **pre-commit / pre-action warning**, not chat-memory extraction.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage/README H1: **"We don't make AI smarter. We make it experienced."** — [projectmem.dev](https://www.projectmem.dev), [repo](https://github.com/riponcm/projectmem) |
| **Agent-specific primitive** | Typed events (issue/attempt/fix/decision) + `pjm precheck` failure warnings + MCP tools that log and recall without a human curator |
| **Autonomy-compatible control plane** | After MCP wiring, the agent reads `get_summary` / writes events; git hooks capture commits. No per-turn dashboard |
| **M2M integration surface** | `pjm` CLI (25 commands), stdio MCP, `pjm wrap`, optional local dashboard |
| **Identity / delegation** | **C5-weak / local:** memory is scoped to the git repo (`.projectmem/`) plus optional `~/.projectmem/global/`. No minted KYA token, no multi-tenant agent passport — filesystem + MCP process identity only |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Typed event log** | `events.jsonl` — issues, attempts, fixes, decisions, notes |
| **`pjm precheck`** | Pre-commit / pre-action warning against failed approaches |
| **MCP server** | One stdio process for every registered project |
| **`pjm wrap`** | Token-budgeted context injection into CLAUDE.md / session |
| **Global memory** | `~/.projectmem/global/` library-scoped gotchas |
| **Prevention Score** | `pjm score` — A+–F plus hours/tokens/USD |
| **Stale-flag, never delete** | Git-verified staleness; history is superseded, not erased |

---

## Autonomy Model

```
pip install projectmem → pjm doctor --fix → wire MCP → pjm init per repo
    -> Agent calls get_summary / get_issue at session start
    -> Agent logs issues, attempts, fixes, decisions via MCP
    -> Git hooks classify commits; pjm precheck warns before repeat failures
    -> Next session reads distilled memory (~800–1,500 tokens in MCP mode)
```

---

## Identity and Delegation Model

- **Project scope:** `.projectmem/` inside the repository; global gotchas under `~/.projectmem/global/`.
- **No cloud identity:** no account, no API key, no telemetry by default.
- **Author of an event** is the agent (or git hook) that wrote it — not a hosted agent ID.
- **Honest C5:** this is local filesystem isolation, not delegated OAuth or a KYA token.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `pjm init`, `doctor`, `precheck`, `wrap`, `score`, `dashboard` |
| MCP | `python -m projectmem.mcp_server` (stdio) |
| Store | `.projectmem/events.jsonl` + distilled markdown |
| Wrap | `pjm wrap claude` / Cursor rules / clipboard |

---

## Human-in-the-Loop Support

Optional `pjm dashboard` (ephemeral local viewer) and `pjm score` for operators. The agent loop does not require the GUI. Pre-commit warnings surface to whoever runs `git commit` — often the agent.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Claude-Mem** | Auto-firehose + compression of tool calls. projectmem is a typed event log + judgment gate |
| **agentmemory** | Shared memory server across hosts. No pre-commit failure warning or `events.jsonl` vocabulary |
| **mem0 / chat memory** | Chat-level facts, not development-history events |
| **CLAUDE.md alone** | Static rules. projectmem is dynamic history of what failed |

---

## Use Cases

- **Stop repeating a failed approach** — `pjm precheck` names the dead end before the commit
- **Cheaper session start** — distilled MCP summary instead of re-reading the tree
- **Cross-project gotchas** — Pydantic/SQLAlchemy lessons follow the next repo
- **Air-gapped memory** — 100% local, MIT, no telemetry
