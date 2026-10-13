# MemPalace

> **"The best-benchmarked open-source AI memory system. And it's free."**

| | |
|---|---|
| **Website** | https://mempalaceofficial.com |
| **Docs** | https://mempalaceofficial.com/guide/getting-started.html |
| **GitHub** | https://github.com/MemPalace/mempalace |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/MemPalace/mempalace?style=social)](https://github.com/MemPalace/mempalace) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push 2026-08-25 ([repo metadata](https://api.github.com/repos/MemPalace/mempalace)); default branch `develop`; PyPI package `mempalace` |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://mempalaceofficial.com

The repository README is explicit: the only official sources are this [GitHub repository](https://github.com/MemPalace/mempalace), the [PyPI package](https://pypi.org/project/mempalace/), and docs at [mempalaceofficial.com](https://mempalaceofficial.com). Other domains are called impostors. A live fetch of the homepage can sit behind Cloudflare bot-check; use the GitHub README and the docs URLs the README publishes.

---

## Official Repo

https://github.com/MemPalace/mempalace

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + MCP

```bash
uv tool install mempalace
mempalace init ~/projects/myapp
mempalace mine ~/projects/myapp
mempalace search "why did we switch to GraphQL"
mempalace wake-up
```

`pipx install mempalace` is the documented alternative. Plain `pip install mempalace` is only for an activated virtualenv where you want `import mempalace`. Docker:

```bash
docker pull ghcr.io/mempalace/mempalace:latest
```

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

MemPalace ships auto-save hooks for Claude Code, Codex CLI, and Cursor, plus an MCP tool surface agents call directly. That is hook/MCP integration, not a published Agent Skills package.

```bash
npx clawhub@latest search mempalace
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/MemPalace/mempalace |
| **Transport** | stdio (CLI or `docker run -i … ghcr.io/mempalace/mempalace`) |
| **Compatible Clients** | Claude Code, Codex, Cursor, and other stdio MCP clients |
| **Tool count (upstream)** | README: 44 MCP tools covering palace reads/writes, knowledge-graph ops, cross-wing navigation, drawers, agent diaries, and coordination |

Example Claude Code stdio config from the official README:

```json
{
  "mcpServers": {
    "mempalace": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-v", "mempalace-data:/data",
        "-v", "/absolute/path/to/.claude/projects:/transcripts:ro",
        "ghcr.io/mempalace/mempalace"
      ]
    }
  }
}
```

---

## What It Does

MemPalace is a local-first memory system for AI agents. It stores conversation history as **verbatim text** and retrieves it with semantic search. Official copy: it does not summarize, extract, or paraphrase. The index is a palace metaphor — people and projects are *wings*, topics are *rooms*, original content lives in *drawers* — so searches can be scoped instead of run against a flat corpus.

The retrieval backend is pluggable (ChromaDB default; SQLite exact, Milvus, Qdrant, and pgvector are documented). Nothing leaves the machine unless the operator opts in. A temporal entity-relationship graph with validity windows sits on local SQLite. Each specialist agent can get its own wing and diary, discoverable at runtime via `mempalace_list_agents`.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | GitHub description: **"The best-benchmarked open-source AI memory system. And it's free."** — [repo](https://github.com/MemPalace/mempalace). README: **"Local-first AI memory. Verbatim storage, pluggable backend"** and first-class Claude Code / Gemini CLI / MCP / local-model guides |
| **Agent-specific primitive** | Verbatim drawers + wing/room scoping; `mine` / `search` / `wake-up`; per-agent wings and diaries; 44 MCP tools including agent coordination (logstream events + artifact handoffs) |
| **Autonomy-compatible control plane** | After `mempalace init`, agents mine, search, and wake context without a human clicking through a dashboard. Auto-save hooks persist sessions before compaction |
| **M2M integration surface** | `mempalace` CLI, Python API, stdio MCP, Docker image |
| **Identity / delegation** | Specialist agents get their own wing and diary; `mempalace_list_agents` discovers them at runtime. Memory stays local unless the operator opts into a remote embedder |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Wing / room / drawer** | Scoped palace layout: projects/people, topics, and verbatim source content |
| **`mine`** | Ingest project files or conversation transcripts into the palace |
| **`search` / `wake-up`** | Semantic retrieval and session-start context load |
| **Pluggable backend** | Chroma default; SQLite exact, Milvus, Qdrant, pgvector via `--backend` / env / `config.json` |
| **Knowledge graph** | Temporal entity-relationship graph with validity windows on local SQLite |
| **Agent wing + diary** | Per-specialist-agent memory, listed at runtime |
| **Auto-save hooks** | Claude Code, Codex, and Cursor hooks that persist before context compression |

---

## Autonomy Model

```
Operator installs CLI (`uv tool install mempalace`) and inits a palace
    -> Agent or hook mines transcripts / project files into wings and drawers
    -> Later sessions call search or wake-up (or MCP tools) without re-explaining history
    -> Optional sweep stores one verbatim drawer per user/assistant message
    -> Knowledge-graph add/query/invalidate stays in the same local control plane
```

No per-query human confirmation. The operator chooses the machine, backend, and whether embeddings stay local.

---

## Identity and Delegation Model

- **Per-agent wings:** Each specialist agent gets its own wing and diary; `mempalace_list_agents` lists them without stuffing every agent into the system prompt.
- **Local default:** Core path needs no API key. Remote OpenAI-compatible embedders are opt-in and require `mempalace repair rebuild-index`.
- **Attribution:** Drawers are verbatim source text, not paraphrases, so retrieved memory points back at original content.
- **No minted cloud identity:** Delegation is filesystem + MCP client access to the palace, not a hosted agent credential.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `uv tool install mempalace` then `init`, `mine`, `search`, `wake-up` |
| Python API | `pip install mempalace` inside a venv |
| MCP stdio | Local CLI or `docker run -i ghcr.io/mempalace/mempalace` |
| Docker | `ghcr.io/mempalace/mempalace:latest`; data under `/data` |
| Docs | [Getting started](https://mempalaceofficial.com/guide/getting-started.html), [MCP tools](https://mempalaceofficial.com/reference/mcp-tools.html) |

---

## Human-in-the-Loop Support

None required for mine/search/wake-up. Humans can read the markdown-adjacent palace on disk and review docs. Hooks exist so coding agents persist memory before compaction without asking the user each turn.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Mem0 / Zep** | Those layers extract or graph *facts*. MemPalace's official contract is verbatim storage — it does not summarize, extract, or paraphrase |
| **MemSearch** | MemSearch is a cross-platform *search-over-memory* index (Markdown + Milvus hybrid recall) for coding-agent sessions. MemPalace is a local palace (wings/rooms/drawers) with pluggable backends and a temporal graph |
| **A raw vector database** | Stores embeddings only. It has no palace scoping, agent diaries, wake-up, or MCP coordination tools |

---

## Use Cases

- **Claude Code / Codex retention** — mine JSONL transcripts and hook auto-save before compaction
- **Project archaeology** — search why a stack decision was made without stuffing the whole repo into context
- **Multi-agent coordination** — give each specialist its own wing and hand off artifacts through MCP tools
- **Air-gapped memory** — keep verbatim history and embeddings on one machine
