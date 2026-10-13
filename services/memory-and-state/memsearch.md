# MemSearch

> **"Cross-platform semantic memory for AI coding agents."**

| | |
|---|---|
| **Website** | https://zilliztech.github.io/memsearch/ |
| **Docs** | https://zilliztech.github.io/memsearch/ |
| **GitHub** | https://github.com/zilliztech/memsearch |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/zilliztech/memsearch?style=social)](https://github.com/zilliztech/memsearch) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push 2026-08-23 ([repo metadata](https://api.github.com/repos/zilliztech/memsearch)); DeepSeek Harness plugin documented |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://zilliztech.github.io/memsearch/

---

## Official Repo

https://github.com/zilliztech/memsearch

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + platform plugins

```bash
# CLI / library (ONNX embeddings, no API key)
uv tool install "memsearch[onnx]"

memsearch index ./memory/
memsearch search "how to configure Redis?" --top-k 5
```

Python API from official docs:

```python
from memsearch import MemSearch

mem = MemSearch(paths=["./memory"])
await mem.index()
results = await mem.search("Redis config", top_k=3)
```

Coding-agent plugins (official docs):

```bash
# Claude Code
# /plugin marketplace add zilliztech/memsearch
# /plugin install memsearch

# DeepSeek Harness
dsh plugin --profile web add @zilliz/memsearch-dsh
```

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ✅ Available as platform skills / `SKILL.md` recall (not `npx skills add`).

| Skill | What It Teaches the Agent |
|---|---|
| Claude Code `memory-recall` | Fork-context subagent recall over indexed sessions (`SKILL.md` with `context: fork`) |
| Codex memory-recall skill | Terminal skill for the same Markdown memory store |
| DSH `memory-recall` | Native DeepSeek Harness skill + pre-step injection |

Claude Code plugin install is the marketplace flow above. Codex uses `plugins/codex/scripts/install.sh`.

---

## MCP

**Status:** ⚠️ Not the primary published interface.

OpenClaw exposes `memory_search`, `memory_get`, and `memory_transcript` as plugin tools. The core product is Markdown files + Milvus hybrid search + per-platform plugins, not a standalone MCP server package.

---

## What It Does

MemSearch is Zilliz's **search-over-memory** layer for coding agents. Official GitHub description: **"A persistent, unified memory layer for all your AI agents (e.g. Claude Code, Codex, DSH), backed by Markdown and Milvus."** Docs: install a plugin and the agent remembers prior work across sessions — conversations are captured, indexed with hybrid search, and recalled when needed.

Markdown under `.memsearch/memory/` is the source of truth. Milvus is a derived, rebuildable index (dense + BM25 + RRF). Recall is progressive: search summaries, expand a section, then drill into the original transcript. The same collection-naming algorithm lets Claude Code, Codex, DeepSeek Harness, OpenClaw, and OpenCode share one project memory.

Official positioning is **retrieval over agent memory**, not a general fact-extraction memory OS. That is the distinction versus Mem0, Zep, and Memoria.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs H1: **"Cross-platform semantic memory for AI coding agents."** — [docs](https://zilliztech.github.io/memsearch/). README: memories flow across Claude Code, Codex, DSH, OpenClaw, and OpenCode |
| **Agent-specific primitive** | Auto-capture of agent turns; hybrid search over session memory; three-layer progressive disclosure (search → expand → transcript); shared project collections across harnesses |
| **Autonomy-compatible control plane** | After plugin install, capture and recall run in hooks / turn events without the user running save commands |
| **M2M integration surface** | CLI, Python API, Claude/Codex/DSH/OpenClaw/OpenCode plugins, optional OpenClaw memory tools |
| **Identity / delegation** | Collection names derive from the project directory. OpenClaw documents per-workspace isolation. This is workspace/project memory, not a hosted per-agent KYA token |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Markdown memory files** | Source of truth under `.memsearch/memory/` |
| **Hybrid search** | Dense vector + BM25 sparse + RRF over Milvus |
| **Progressive disclosure** | `search` → `expand <chunk_hash>` → original transcript |
| **Smart dedup** | SHA-256 hashing skips re-embed of unchanged content |
| **Live sync** | `memsearch watch` indexes on file change |
| **Cross-platform plugins** | Same memory, different harness capture/recall paths |
| **Skills from memory** | Documented distillation of repeated workflows into installable skills |

---

## Autonomy Model

```
Plugin captures a finished turn (hook / DSH event / SQLite daemon)
    -> Writer updates Markdown memory
    -> Indexer embeds into Milvus (local Lite, server, or Zilliz Cloud)
    -> Next session: skill or tool searches; optional pre-step injection (DSH)
    -> Agent expands a hit only when it needs the full section
```

Users do not run a manual save step on the documented plugin path.

---

## Identity and Delegation Model

- **Project-scoped memory:** Collection names come from the project directory so two agents on the same repo share context.
- **Workspace isolation (OpenClaw):** Point an agent's workspace at a project directory; tools stay inside that workspace.
- **No cloud agent account required** for the ONNX + Milvus Lite path.
- **Observation of history, not authorization:** Recall does not grant extra repo or production permissions.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `memsearch index`, `search`, `expand`, `watch` |
| Python API | `MemSearch(paths=...).index()` / `.search()` |
| Claude Code plugin | Marketplace `zilliztech/memsearch` |
| DSH plugin | `dsh plugin --profile web add @zilliz/memsearch-dsh` |
| OpenClaw | `openclaw plugins install --force clawhub:memsearch` |
| Storage | Markdown + Milvus Lite / Server / Zilliz Cloud |

---

## Human-in-the-Loop Support

None required for capture/recall. Markdown files are human-readable and git-friendly. DSH's web profile adds a read-only memory browser. Compaction / "memory compact" is an optional LLM maintenance task.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Mem0** | Extracts and updates *facts* for interactive agents. MemSearch indexes *session transcripts* for coding-agent recall |
| **Zep** | Temporal knowledge graph / business memory. Not a Markdown+Milvus coding-agent memory bus |
| **Memoria** | Git-versioned memory service. Different primitive (snapshots/branches) and not the documented cross-harness plugin matrix |
| **MemPalace** | Verbatim palace (wings/rooms/drawers) plus a local graph. MemSearch is hybrid *search-over-memory* shared across Claude/Codex/DSH/OpenClaw/OpenCode |

---

## Use Cases

- **Resume a debugging thread** — retrieve how a similar Redis/Docker/deploy issue was fixed
- **Recover decision rationale** — why the repo chose a library or API shape
- **Cross-harness continuity** — Claude Code today, DSH tomorrow, same `.memsearch/` store
- **Agent-developer embedding** — call `MemSearch.search` from a custom harness
