# Engram

> **"Persistent memory for AI coding agents"**

| | |
|---|---|
| **Website** | https://gentleman-programming-engram.mintlify.app/introduction |
| **Docs** | https://gentleman-programming-engram.mintlify.app/introduction |
| **GitHub** | https://github.com/Gentleman-Programming/engram |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/Gentleman-Programming/engram?style=social)](https://github.com/Gentleman-Programming/engram) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push 2026-08-27 ([repo metadata](https://api.github.com/repos/Gentleman-Programming/engram)); Homebrew tap + `engram setup <agent>` matrix |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://gentleman-programming-engram.mintlify.app/introduction

Mintlify docs H1: **"Persistent memory system for AI coding agents."** The GitHub README tagline is **"Persistent memory for AI coding agents"** with the supporting line **"One brain. Local or cloud. Agent-agnostic, single binary, zero dependencies."**

---

## Official Repo

https://github.com/Gentleman-Programming/engram

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + MCP / plugin

```bash
brew install gentleman-programming/tap/engram
```

Wire an agent (official README table):

```bash
# Claude Code
claude plugin marketplace add Gentleman-Programming/engram && claude plugin install engram

# Codex, OpenCode, Cursor, and others
engram setup codex
engram setup opencode
engram setup cursor
```

`engram setup <agent>` writes MCP config and plugin files. Most agents launch `engram mcp` as a short-lived stdio subprocess — no manual `engram serve` except OpenCode / Pi HTTP session tracking (default port 7437). Other install methods: [docs/INSTALLATION.md](https://github.com/Gentleman-Programming/engram/blob/main/docs/INSTALLATION.md).

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ✅ Published as a Claude Code marketplace plugin with a Memory Protocol skill (not `npx skills add`).

| Skill | What It Teaches the Agent |
|---|---|
| Memory Protocol (Claude Code plugin) | When to `mem_save` / `mem_search` and the session-close summary ([docs](https://gentleman-programming-engram.mintlify.app/agents/claude-code)) |
| Pi package `gentle-engram` | Persistent project memory + compaction recovery via `engram setup pi` |

```bash
npx clawhub@latest search engram
```

---

## MCP

**Status:** ✅ Available — stdio MCP is the primary agent surface.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/Gentleman-Programming/engram |
| **Transport** | stdio (`engram mcp`). Official README: **no HTTP/network MCP endpoint** |
| **Compatible Clients** | Claude Code, OpenCode, Gemini CLI, Codex, VS Code (Copilot), Antigravity, Cursor, Windsurf, Pi, and any other MCP client |
| **Tool count (upstream)** | README lists **20** MCP tools (`mem_save`, `mem_search`, session lifecycle, conflict surfacing, …). Mintlify intro still says "14 MCP Tools" on an older page |

---

## What It Does

Engram is a **single Go binary** that gives coding agents a persistent SQLite + FTS5 memory. Official positioning: the **agent** decides what is worth remembering via `mem_save`; Engram stores and searches it. Docs: "Engram trusts the agent to decide what's worth remembering — not a firehose of raw tool calls."

Next session, the agent calls `mem_search` / `mem_context` (and plugins can inject prior session context). Progressive disclosure is `mem_search` → `mem_timeline` → `mem_get_observation`. Optional git-chunk sync and opt-in cloud replication leave local SQLite authoritative.

**Distinct from [Claude-Mem](claude-mem.md):** Claude-Mem auto-captures a tool-call firehose and compresses it in a worker. Engram is agent-curated FTS5 — one binary, zero Node/Bun/Python/Chroma. Their [COMPARISON.md](https://github.com/Gentleman-Programming/engram/blob/main/docs/COMPARISON.md) is the official contrast (note: that file's Claude-Mem **AGPL-3.0** license row is stale; Claude-Mem relicensed to Apache-2.0 in v13.0.0).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: **"Persistent memory for AI coding agents"** / **"One brain. Local or cloud. Agent-agnostic, single binary, zero dependencies."** — [repo](https://github.com/Gentleman-Programming/engram). Docs: **"Your AI coding agent forgets everything when the session ends. Engram gives it a brain."** — [introduction](https://gentleman-programming-engram.mintlify.app/introduction) |
| **Agent-specific primitive** | `mem_save` / `mem_search` / `mem_session_summary`; 3-layer disclosure; session start/end tools; conflict surfacing (`mem_judge`, `mem_compare`) |
| **Autonomy-compatible control plane** | After `engram setup`, the agent launches `engram mcp` and saves/searches without a dashboard. Session context can be injected automatically (docs session lifecycle) |
| **M2M integration surface** | `engram` CLI, stdio MCP, HTTP REST on 7437, TUI, `engram setup <agent>` |
| **Identity / delegation** | Project-scoped local DB (`~/.engram/engram.db` or `ENGRAM_DATA_DIR`). Cloud mode is project-scoped and opt-in. `<private>` tags stripped at plugin and store layers. No hosted KYA token |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`mem_save`** | Agent-curated observation (title, type, What/Why/Where/Learned) |
| **`mem_search`** | SQLite FTS5; default `match_mode: "all"`, optional `"any"` |
| **`mem_timeline` / `mem_get_observation`** | Chronological context, then full record |
| **Session lifecycle** | `mem_session_start` / `mem_session_end` / `mem_session_summary` |
| **Single Go binary** | MCP stdio + CLI + optional HTTP; `modernc.org/sqlite`, no CGO |
| **Git sync** | Compressed chunks; local SQLite remains source of truth |
| **Opt-in cloud** | Project-scoped replication; local DB stays authoritative |
| **Privacy tags** | `<private>…</private>` stripped before disk write |

---

## Autonomy Model

```
Operator installs the binary and runs `engram setup <agent>`
    -> Agent (or plugin) starts `engram mcp` over stdio
    -> Agent calls mem_save after significant work
    -> Session end writes a structured summary
    -> Next session: context inject and/or mem_search — no human save click
```

Cloud enroll/sync is operator opt-in, not required for the local loop.

---

## Identity and Delegation Model

- **Project / data-dir isolation:** Default `~/.engram/engram.db`; override with `ENGRAM_DATA_DIR`.
- **Agent-curated writes:** The calling agent is the author of each `mem_save`; Engram does not impersonate another agent.
- **Privacy:** Two-layer `<private>` strip (plugin + store) so tagged secrets never hit disk.
- **Cloud tokens:** Optional `ENGRAM_HTTP_TOKEN` / managed cloud tokens; HTTP defaults to loopback. This is filesystem + MCP access, not a hosted agent passport.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Homebrew | `brew install gentleman-programming/tap/engram` |
| Agent setup | `engram setup <codex\|opencode\|cursor\|…>` or Claude Code marketplace plugin |
| MCP stdio | `engram mcp` |
| HTTP API | `engram serve` (default 7437) — not an MCP transport |
| CLI | `engram save`, `search`, `timeline`, `context`, `sync`, `doctor`, … |
| TUI | `engram tui` |
| Docs | https://gentleman-programming-engram.mintlify.app/introduction |

---

## Human-in-the-Loop Support

None required for save/search after setup. Humans can browse `engram tui`, review git-synced chunks, and run `engram doctor`. Manual Memory Protocol snippets in `CLAUDE.md` / `GEMINI.md` are documented as a "nuclear option" for compaction survival, not the required first step.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Claude-Mem** | Firehose capture + separate compression worker (Node/Bun/uv/Chroma). Engram is agent-curated FTS5 in one Go binary ([COMPARISON.md](https://github.com/Gentleman-Programming/engram/blob/main/docs/COMPARISON.md)) |
| **MemPalace** | Verbatim palace + semantic backends. Not `mem_save` / FTS5 agent-curated summaries |
| **MemSearch** | Markdown + Milvus hybrid index of session transcripts. Different storage and recall contract |
| **A raw SQLite file** | No MCP tool protocol, session lifecycle, or agent setup matrix |

---

## Use Cases

- **Agent-curated project memory** — save architecture decisions and bugfixes without indexing every tool call
- **Cross-harness one brain** — Claude Code today, Codex or Cursor tomorrow, same `~/.engram/`
- **Air-gapped / zero-dep install** — one static Go binary, no Node or vector DB
- **Optional team replication** — git chunks or project-scoped cloud sync
