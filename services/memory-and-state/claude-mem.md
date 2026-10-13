# Claude-Mem

> **"Persistent memory compression system for Claude Code"**

| | |
|---|---|
| **Website** | https://cmem.ai/ |
| **Docs** | https://docs.claude-mem.ai/introduction |
| **GitHub** | https://github.com/thedotmack/claude-mem |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/thedotmack/claude-mem?style=social)](https://github.com/thedotmack/claude-mem) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Apache-2.0 (relicensed from AGPL-3.0 in [v13.0.0, 2026-05-08](https://github.com/thedotmack/claude-mem/blob/main/CHANGELOG.md)) |
| **Latest-month signal** | Last GitHub push 2026-08-26 ([repo metadata](https://api.github.com/repos/thedotmack/claude-mem)); npm/plugin installers for Claude Code, Cursor, Windsurf, OpenCode, Codex CLI, Antigravity CLI, OpenClaw |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://cmem.ai/

`https://claude-mem.ai` redirects here. Homepage positions **claude-mem** as the open-source engine and **CMEM Cloud** as the optional hosted mirror / private MCP link. Official install copy on the homepage: `$ npx claude-mem install`. Docs remain at https://docs.claude-mem.ai/introduction.

---

## Official Repo

https://github.com/thedotmack/claude-mem

GitHub description: **"Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions."**

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + coding-agent plugin

Recommended installer ([docs](https://docs.claude-mem.ai/installation)):

```bash
npx claude-mem install
```

The installer detects installed IDEs (Claude Code, Cursor, Windsurf, OpenCode, Codex CLI, Antigravity CLI) and wires hooks plus the local worker. Official note: `npm install -g claude-mem` installs the **SDK/library only** and does **not** register hooks or start the worker.

Claude Code marketplace:

```text
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

Other official installers from the [README](https://github.com/thedotmack/claude-mem/blob/main/README.md):

```bash
npx claude-mem install --ide opencode
npx claude-mem install --ide antigravity
curl -fsSL https://install.cmem.ai/openclaw.sh | bash
```

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ✅ Bundled with the plugin (not `npx skills add`).

| Skill | What It Teaches the Agent |
|---|---|
| `mem-search` | Natural-language query over compressed observations with progressive disclosure ([README](https://github.com/thedotmack/claude-mem/blob/main/README.md)) |
| Claude Desktop skill | Search memory from Claude Desktop conversations |
| Troubleshoot skill | Diagnose worker / install issues from a problem description |

Docs also list **Knowledge Agents** ("queryable brains" from observation history). [docs/license.md](https://github.com/thedotmack/claude-mem/blob/main/docs/license.md) reserves hosted cloud, team sync, enterprise features, and **premium knowledge agents** outside the Apache-2.0 public core.

---

## MCP

**Status:** ✅ Available — four search tools on the local worker.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/thedotmack/claude-mem |
| **Transport** | Local worker HTTP API + MCP tools (stdio/plugin wiring via installer) |
| **Compatible Clients** | Claude Code, Cursor, Windsurf, OpenCode, Codex CLI, Antigravity CLI, OpenClaw, other MCP clients |
| **Tools (upstream)** | `search`, `timeline`, `get_observations` (3-layer workflow); README also lists a fourth MCP search surface |

---

## What It Does

Claude-Mem is a **persistent memory compression system** for coding agents. Official docs: it automatically captures tool-usage observations, generates semantic summaries, and injects relevant context into later sessions so the agent keeps project continuity after a session ends.

The capture path is a **firehose**: lifecycle hooks record prompts and tool executions (Read, Write, and the rest), a local Bun worker compresses them via the Claude Agent SDK, and the next SessionStart primes context from recent sessions. Storage is SQLite + FTS5 with an optional Chroma vector index.

**Distinct from [MemPalace](mempalace.md)** (verbatim palace rooms/drawers, no official paraphrase) and **[MemSearch](memsearch.md)** (Markdown + Milvus hybrid search plugins): Claude-Mem auto-captures a tool-call firehose, compresses it, and primes the next session.

**OSS vs hosted:** Apache-2.0 covers the local engine, CLI, MCP tools, and docs. [docs/license.md](https://github.com/thedotmack/claude-mem/blob/main/docs/license.md) states Claude-Mem Server v0.1 does **not** ship hosted cloud, team sync, enterprise features, premium knowledge agents, private evals, or customer deployment tooling — those sit outside the public implementation. CMEM Cloud (homepage: paid cloud mirror + private MCP link) is that hosted layer.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs H1: **"Persistent memory compression system for Claude Code"** — [docs](https://docs.claude-mem.ai/introduction). Repo: **"Persistent Context Across Sessions for Every Agent"** — [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) |
| **Agent-specific primitive** | Auto-firehose of tool observations + AI compression + SessionStart priming; 3-layer MCP search (`search` → `timeline` → `get_observations`) |
| **Autonomy-compatible control plane** | Official: **"Automatic Operation — No manual intervention required."** After install, hooks capture and the worker compresses without a save click ([introduction](https://docs.claude-mem.ai/introduction)) |
| **M2M integration surface** | `npx claude-mem install`, Claude Code / OpenCode / Codex / Antigravity / OpenClaw installers, local worker HTTP API, MCP search tools |
| **Identity / delegation** | Memory is scoped to the local user data dir (`~/.claude-mem/`) and the wired agent/IDE. `<private>` tags exclude content from storage. Hosted team scopes and premium knowledge-agent corpora are reserved commercial surfaces, not the OSS core |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Lifecycle hooks** | SessionStart, UserPromptSubmit, PostToolUse, Stop/Summary, SessionEnd capture the firehose |
| **Observation** | Structured record of a tool use / learning, cited by ID |
| **Compression worker** | Local Bun/Express service (default port `37700 + (uid % 100)`) that extracts summaries via the Claude Agent SDK |
| **Session priming** | Inject context from recent sessions at SessionStart |
| **FTS5 + optional Chroma** | Keyword and hybrid semantic search over observations |
| **3-layer recall** | Compact `search` index → `timeline` → full `get_observations` |
| **Folder `CLAUDE.md`** | Auto-generated folder context files with activity timelines (docs) |
| **`<private>` tags** | Exclude sensitive spans from storage |

---

## Autonomy Model

```
Operator runs `npx claude-mem install` (or the marketplace / OpenClaw installer)
    -> Worker starts; hooks register on the chosen agent/IDE
    -> SessionStart injects compressed context from prior sessions
    -> Tool executions are captured automatically
    -> Worker compresses observations without a human save step
    -> Later sessions search or receive primed context
```

No per-turn confirmation for capture or recall.

---

## Identity and Delegation Model

- **Local-first engine:** Observations live under `~/.claude-mem/` (override with `CLAUDE_MEM_DATA_DIR`). The agent's session is the capture subject.
- **Privacy tags:** `<private>` content is excluded from storage.
- **No minted KYA token** in the OSS path. Delegation is "this machine's worker + this agent's hooks."
- **Hosted boundary:** CMEM Cloud / team sync / premium knowledge agents are reserved outside Apache-2.0 ([license.md](https://github.com/thedotmack/claude-mem/blob/main/docs/license.md)). Do not treat the cloud MCP link as part of the open core.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Installer | `npx claude-mem install` (multi-IDE) |
| Claude Code plugin | `/plugin marketplace add thedotmack/claude-mem` then `/plugin install claude-mem` |
| OpenCode / Antigravity | `npx claude-mem install --ide opencode` / `--ide antigravity` |
| OpenClaw | `curl -fsSL https://install.cmem.ai/openclaw.sh \| bash` |
| MCP search | `search`, `timeline`, `get_observations` |
| Worker HTTP | Local API + web viewer (port printed on startup) |
| Docs | https://docs.claude-mem.ai/introduction |

---

## Human-in-the-Loop Support

None required for capture, compression, or session priming. Humans can browse the local web viewer, tune `~/.claude-mem/settings.json`, and wrap secrets in `<private>` tags. Cloud sync and team governance are optional paid surfaces.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **MemPalace** | Verbatim palace (wings/rooms/drawers) that officially does **not** summarize. Claude-Mem's contract is firehose capture + compression |
| **MemSearch** | Markdown + Milvus hybrid *search-over-memory* with harness plugins. Not an auto-compressing observation worker |
| **Engram** | Agent-curated `mem_save` / FTS5. Engram's own [COMPARISON.md](https://github.com/Gentleman-Programming/engram/blob/main/docs/COMPARISON.md) contrasts that with Claude-Mem's raw-tool-call firehose (COMPARISON.md's AGPL row is stale — Claude-Mem is Apache-2.0 as of v13.0.0) |
| **A raw SQLite file** | No hook firehose, no compression worker, no SessionStart priming |

---

## Use Cases

- **Resume a Claude Code / Codex / OpenCode project** — next session starts with compressed history instead of a blank context
- **Search past bugfixes by citation ID** — `search` then `get_observations`
- **OpenClaw gateway memory** — official `install.cmem.ai/openclaw.sh` plugin path
- **Local-only memory** — keep the Apache-2.0 engine on disk; skip CMEM Cloud
