# Memoir

> **"Git for AI Memory"**

| | |
|---|---|
| **Website** | https://www.memoir-ai.dev |
| **Docs** | https://zhangfengcdt.github.io/memoir/ |
| **GitHub** | https://github.com/zhangfengcdt/memoir |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/zhangfengcdt/memoir?style=social)](https://github.com/zhangfengcdt/memoir) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Apache-2.0 |
| **Status** | **Alpha** — official README badge `Status-Alpha`; contributing section: “Memoir is alpha” |
| **Latest-month signal** | Last GitHub push 2026-09-03 ([repo metadata](https://api.github.com/repos/zhangfengcdt/memoir)); PyPI `memoir-ai`; Claude Code / Codex plugins |
| **Verified at** | 2026-09-03 |

---

## Official Website

https://www.memoir-ai.dev

Homepage H1 (live 2026-09-03): **"Git for AI Memory"** — “Local-first memory your agents can explain, rewind, and branch.”

GitHub Pages docs (`https://zhangfengcdt.github.io/memoir/`) use a different intro: “Welcome to Memoir's Documentation” / “semantic memory system for AI agents… Git-like version control.” The catalog tagline is the **homepage/README H1**, not the docs welcome heading.

---

## Official Repo

https://github.com/zhangfengcdt/memoir

README H1 quote: **Git for AI Memory** / *Hierarchical Memory with Git-Like Version Control*. GitHub description: **"Hierarchical Agent Memory with Git-Like Version Control"**

**Alpha caveat (keep):** README ships `[Status-Alpha]` and says contributions are welcome because the project is alpha and optimized for coding agents.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / CLI` + plugins / MCP

```bash
pip install memoir-ai
# Claude Code:
#   /plugin marketplace add zhangfengcdt/memoir
#   /plugin install memoir@memoir
```

Any MCP host (no extra install if `uv` is on PATH):

```json
{
  "mcpServers": {
    "memoir": {
      "command": "uvx",
      "args": ["--from", "memoir-ai[mcp]", "memoir-mcp"],
      "env": { "MEMOIR_STORE": "~/.memoir/mcp" }
    }
  }
}
```

CLI loop: `memoir new ./store` → `memoir remember "…" -p path` → `memoir recall "…" --json`. Codex: `codex plugin marketplace add zhangfengcdt/memoir` and enable hooks. Hermes / OpenClaw / OpenCode plugins are documented on the homepage.

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ✅ Bundled with Claude Code / Codex plugins (not `npx skills add`)

| Skill | What It Teaches the Agent |
|---|---|
| `memory-recall` / `memoir-remember` | When to recall vs write a path |
| `memoir-onboard` | Project snapshot / taxonomy onboarding |
| `memoir-status` / `memoir-ui` | Store health and visual explorer |

```bash
npx clawhub@latest search memoir
```

---

## MCP

**Status:** ✅ Available — `memoir-mcp`

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/zhangfengcdt/memoir |
| **Transport** | stdio (`uvx --from memoir-ai[mcp] memoir-mcp`); remote HTTP documented for ChatGPT / Claude.ai connectors |
| **Compatible Clients** | Claude Desktop, Cursor, Cline, Windsurf, VS Code, Zed, Continue, LibreChat, and any MCP host |
| **Tools (upstream)** | `memoir_recall`, `memoir_remember`, `memoir_forget`, `memoir_status`, `memoir_branches`, `memoir_checkout`, `memoir_commits` |

---

## What It Does

Memoir replaces opaque vector memory with a **local-first, taxonomy-structured, Git-versioned store**. Official homepage: recall by path (`memoir get api.v2.auth`), time-travel to reproduce bugs, branch to test risky strategies. Claude Code hooks shadow git branches so a `git checkout` does not contaminate `main` memory. Merges review feature-branch lessons into the main knowledge base.

**Alpha:** APIs, plugins, and taxonomy may change. Treat as an early coding-agent memory VCS, not a frozen production SLA.

Distinct from [Memoria](memoria.md) (also git-like, different product) and from [Claude-Mem](claude-mem.md) (compressed observation firehose): Memoir’s claim is **hierarchical semantic paths + cryptographic git operations** (`blame` / `checkout` / `merge`), not session-log compression.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage/README H1: **"Git for AI Memory"** — [memoir-ai.dev](https://www.memoir-ai.dev), [README](https://github.com/zhangfengcdt/memoir). Copy: built for coding agents and custom runtimes |
| **Agent-specific primitive** | Path-addressed memory (`profile.professional.skills.python`); branch-shadowing hooks; `memoir_branches` / `memoir_checkout` / `memoir_commits` MCP tools |
| **Autonomy-compatible control plane** | After plugin/MCP install, session-start injection and stop-hook capture run without a save click. CLI `--json` + stable exit codes |
| **M2M integration surface** | `memoir` CLI, Python SDK, `memoir-mcp`, Claude Code / Codex / Hermes / OpenClaw plugins, LangGraph `BaseStore` |
| **Identity / delegation** | Namespaces + git-like blame (“who taught this rule”). **C5-weak / local:** store path (`MEMOIR_STORE`) and namespace isolate data; no hosted KYA token. Alpha — do not treat blame as a production audit product yet |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Semantic path** | Hierarchical key (`api.v2.auth`) instead of a vector UUID |
| **Branch / merge / checkout** | Git operations on the memory store; hooks follow `git checkout` |
| **`memoir remember` / `recall`** | Write (explicit path or LLM classify) and search |
| **Time-travel** | `memoir time-travel HEAD~5` to reproduce a poisoned state |
| **`memoir blame`** | Audit which session taught a rule |
| **MCP versioning tools** | `memoir_branches`, `memoir_checkout`, `memoir_commits` |

---

## Autonomy Model

```
Install plugin or memoir-mcp
    -> Session start injects relevant paths
    -> Agent remembers/recalls via MCP or slash commands
    -> git checkout switches the memory branch (hooks)
    -> Session stop auto-captures durable facts
    -> Optional memoir merge to promote a feature-branch lesson
```

---

## Identity and Delegation Model

- **Namespace / store path:** `MEMOIR_STORE` or `./my_store`; MCP default `~/.memoir/mcp`.
- **Blame:** cryptographic history of who wrote a path — still **Alpha**.
- **Branch isolation:** feature-branch memories do not leak onto `main` until merge.
- **No hosted agent passport.** LLM keys (optional) are for classification/recall modes, not identity.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| PyPI | `pip install memoir-ai` (import `memoir`, CLI `memoir`) |
| MCP | `memoir-mcp` via `uvx --from memoir-ai[mcp]` |
| Plugins | Claude Code, Codex, Hermes, OpenClaw, community OpenCode |
| SDK | Async `MemoryClient`; LangGraph `LangGraphMemoryStore` |
| UI | `memoir ui` — local explorer (secondary) |

---

## Human-in-the-Loop Support

`memoir ui` and `memoir merge` are operator/review surfaces. Auto-capture and recall do not require the UI. Merge conflicts on memory paths are the HITL analog of a git merge.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Vector DB / “vibe search”** | No path addressing, branch shadowing, or `blame`/`checkout` |
| **CLAUDE.md as a global store** | Official anti-pattern: token rent + cache invalidation |
| **Claude-Mem** | Firehose compression, not a git-versioned taxonomy |
| **Memoria** | Separate git-like memory product; different store and plugin matrix |

---

## Use Cases

- **Branch-aware coding agents** — experimental refactor memory stays off `main`
- **Reproducible memory bugs** — time-travel to the commit that poisoned recall
- **Prefix-cache-friendly prompts** — fetch ten tokens at `api.v2.auth` instead of a blob
- **Alpha evaluation** — try the VCS model; expect breaking changes
