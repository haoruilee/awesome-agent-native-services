# Memorix

> **"Local-first shared memory layer for AI coding agents."**

| | |
|---|---|
| **Website** | https://github.com/AVIDS2/memorix |
| **Docs** | https://github.com/AVIDS2/memorix#readme |
| **GitHub** | https://github.com/AVIDS2/memorix |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/AVIDS2/memorix?style=social)](https://github.com/AVIDS2/memorix) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-09-02 ([repo metadata](https://api.github.com/repos/AVIDS2/memorix)); npm `memorix`; listed in the official MCP Registry |
| **Verified at** | 2026-09-03 |

---

## Official Website

https://github.com/AVIDS2/memorix

No separate marketing domain is published (`homepage` is empty on the GitHub repo). The README is the canonical surface.

README H1 quote (live 2026-09-03): **"Local-first shared memory layer for AI coding agents."**

---

## Official Repo

https://github.com/AVIDS2/memorix

GitHub description: open-source **cross-agent** memory layer via MCP for Claude Code, Codex, Cursor, Windsurf, Gemini CLI, Antigravity, OpenClaw, Hermes, and other MCP-capable agents.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + MCP / `memorix setup`

```bash
npm install -g memorix
memorix setup --agent claude --global
# also: codex, copilot, cursor, pi, gemini-cli, opencode, windsurf,
# kiro, antigravity, trae, openclaw, hermes, omp, dsh, workbuddy, …
```

Manual MCP (stdio; default tool profile `micro`):

```json
{
  "mcpServers": {
    "memorix": {
      "command": "memorix",
      "args": ["serve"]
    }
  }
}
```

Requires Node.js `>=22.18.0` and a real Git root — **project identity is the git project**, not a chat window. `memorix background start` / `memorix serve-http` expose a shared HTTP endpoint and dashboard when several clients need one daemon.

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ✅ Generated / bundled by `memorix setup` and `memorix skills` (not `npx skills add`)

| Skill | What It Teaches the Agent |
|---|---|
| Official per-agent skills | When to search, store, promote, and resume a Workset |
| `memorix_promote` | Turn durable knowledge into a reusable project skill |

```bash
npx clawhub@latest search memorix
```

---

## MCP

**Status:** ✅ Available — stdio is the default; HTTP optional

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/AVIDS2/memorix |
| **Transport** | stdio (`memorix serve`); HTTP via `memorix serve-http` / `background start` |
| **Compatible Clients** | Claude Code, Codex, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, OpenClaw, Hermes, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy, any MCP client |
| **Default profile** | `micro` — compact core tools (`memorix_project_context`, search, store, resolve) |

---

## What It Does

Memorix is a **local-first shared memory daemon anchored to the Git project**. Official README: the agent can change (Claude Code today, Codex tomorrow, Cursor in the afternoon); the project memory stays. SQLite is canonical; Orama searches; LLM formation/embedding is optional — without keys it still does local full-text retrieval.

It is more than a note store: **Git Memory** turns commits into engineering facts; **Reasoning Memory** keeps alternatives and trade-offs; **Memory Autopilot** builds a bounded Workset (`memorix context` / `memorix resume`); **orchestration** (`memorix orchestrate`) coordinates locks, handoffs, and review loops. Long-term curated items cross projects only when explicitly marked portable.

Distinct from [agentmemory](agentmemory.md) (one memory server, chat/wiki style) and [Claude-Mem](claude-mem.md) (per-user observation firehose): Memorix’s identity key is the **git root**, and the surface is a cross-agent local daemon plus setup matrix.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: **"Local-first shared memory layer for AI coding agents."** / “One project memory system for Claude Code, Codex, … and any MCP-capable agent.” — [AVIDS2/memorix](https://github.com/AVIDS2/memorix) |
| **Agent-specific primitive** | Git-anchored shared pool; Workset autopilot; Git Memory; Reasoning Memory; `memorix orchestrate` locks/handoffs |
| **Autonomy-compatible control plane** | After `memorix setup`, hooks and MCP run without a curator. Orchestration review loops are optional gates, not a required GUI |
| **M2M integration surface** | `memorix` CLI, stdio/HTTP MCP, SDK `createMemoryClient()`, per-agent plugins/hooks/skills |
| **Identity / delegation** | **C5-local:** “project identity is derived from the real Git root.” Teams/locks/messages attribute work to the calling agent process. No hosted KYA token. Only an explicitly portable user item may leave the project |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Git-project memory pool** | SQLite + Orama under the repo, shared across agents |
| **Workset / Autopilot** | `memorix context` / `resume` — start files, cautions, verification |
| **Git Memory** | Commit-derived facts (`memorix ingest commit`) |
| **Reasoning Memory** | Design rationale, alternatives, trade-offs |
| **Orchestration** | Task context, handoffs, file locks, review loops |
| **`memorix serve`** | stdio MCP bridge (`micro` tool profile) |
| **Background daemon** | HTTP MCP + dashboard for multi-client use |

---

## Autonomy Model

```
npm i -g memorix → memorix setup --agent <host> --global
    -> Agent opens the git project; MCP resolves the repo root
    -> context/resume injects a Workset; agent searches/stores via MCP
    -> Optional hooks capture prompts and session lifecycle
    -> Next agent on the same repo sees the same pool
```

---

## Identity and Delegation Model

- **Project key:** Git root. No git → no project identity (by design).
- **Caller:** the wired agent/MCP client; orchestration locks name workers.
- **Portability:** long-term items stay local unless marked portable.
- **Honest C5:** filesystem + git scoping, not a delegated cloud credential.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `memorix setup`, `serve`, `memory`, `orchestrate`, `doctor` |
| MCP stdio | `memorix serve` |
| MCP HTTP | `memorix serve-http` / `background start` |
| SDK | `createMemoryClient()` |
| Dashboard | local web UI (operator, not required) |

---

## Human-in-the-Loop Support

Dashboard preview-first cleanup/dedup/retention. Knowledge workspace is review-gated (proposals do not silently overwrite reviewed pages). Orchestration review loops are optional HITL. Day-to-day recall/store does not need the GUI.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **agentmemory** | Shared server across hosts; not a git-root daemon with Git Memory + orchestration |
| **Claude-Mem** | Per-user firehose compression, not a cross-agent project pool |
| **Notes file / CLAUDE.md** | No Workset, Git Memory, or multi-agent locks |
| **Raw SQLite** | No MCP setup matrix or reasoning/git ingest |

---

## Use Cases

- **Handoff across IDEs** — same repo memory in Claude Code, Codex, and Cursor
- **Commit-aware recall** — “what changed and why” from Git Memory
- **Parallel agents** — `memorix orchestrate` locks and handoffs
- **Keyless local search** — FTS without an embedding vendor
