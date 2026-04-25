# LLM Wiki

> **"LLM-compiled knowledge bases for any AI agent."**

| | |
|---|---|
| **Website** | https://llm-wiki.net |
| **Docs** | https://llm-wiki.net/ |
| **GitHub** | https://github.com/nvk/llm-wiki |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/nvk/llm-wiki?style=social)](https://github.com/nvk/llm-wiki) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MIT |

---

## Official Website

https://llm-wiki.net

---

## Official Repo

https://github.com/nvk/llm-wiki

---

## How to Use (Agent Onboarding)

**Claude Code (native plugin):**

```bash
claude plugin install wiki@llm-wiki
```

**OpenAI Codex (repo-local plugin):**

```bash
git clone https://github.com/nvk/llm-wiki.git
# In Codex: /plugins → add marketplace
# → .agents/plugins/marketplace.json
# → install "LLM Wiki"
```

**Any agent (portable protocol file):**

```bash
curl -sL https://raw.githubusercontent.com/nvk/llm-wiki/master/AGENTS.md > ~/your-project/AGENTS.md
```

---

## Agent Skills

**Status:** ✅ The repository ships agent-native instruction surfaces (Claude plugin skill tree + portable `AGENTS.md`).

| Skill Surface | Path |
|---|---|
| Claude plugin skill | `claude-plugin/skills/wiki-manager/` |
| OpenCode instruction skill | `plugins/llm-wiki-opencode/skills/wiki-manager/SKILL.md` |
| Universal portable protocol | `AGENTS.md` |

---

## MCP

**Status:** ⚠️ No standalone first-party MCP server as the primary interface.

Notes:
- LLM Wiki's core interface is plugin commands + `AGENTS.md` protocol.
- The official install docs emphasize Claude/Codex/OpenCode/portable AGENTS.md flows rather than a standalone MCP server endpoint.

---

## What It Does

LLM Wiki builds a compounding, cross-session knowledge base for agents: parallel research, source ingestion, synthesis into wiki articles, deep query over accumulated content, and output generation (reports/slides/plans). The knowledge base is durable and grows with each run.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Official tagline: "LLM-compiled knowledge bases for any AI agent." |
| **Agent-specific primitive** | Agent-run wiki compilation pipeline: `research` → `ingest` → `compile` → `query` → `output`, plus session lesson extraction (`/wiki:ll`). |
| **Autonomy-compatible control plane** | Commands are designed for autonomous execution loops, including multi-agent parallel research and long-running rounds. |
| **M2M integration surface** | CLI/plugin command surfaces for Claude/Codex/OpenCode + portable `AGENTS.md` protocol for any compatible agent host. |
| **Identity / delegation** | Topic-isolated wiki workspaces with command-level audit trails (`log.md`) and explicit per-project wiki scoping. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Research orchestration** | Parallel agents explore multiple angles and continuously deepen findings |
| **Source ingestion** | URL/file/text ingestion into immutable raw source store |
| **Wiki compilation** | Synthesizes source material into cross-linked markdown knowledge articles |
| **Query depths** | Quick/standard/deep retrieval modes over indexes/articles/raw corpus |
| **Artifact generation** | Produce report/slides/study-guide/timeline outputs from compiled knowledge |
| **Lessons learned extraction** | Writes error→fix patterns from sessions back into the wiki (`/wiki:ll`) |

---

## Autonomy Model

```
Agent runs /wiki:research on a topic
    ↓
Parallel agents ingest + score sources
    ↓
/wiki:compile synthesizes wiki articles
    ↓
Agent runs /wiki:query and /wiki:output
    ↓
/wiki:ll writes lessons learned back into memory
```

---

## Identity and Delegation Model

- Topic-scoped wiki directories isolate contexts (`~/wiki/topics/<name>/`).
- Global and topic logs provide attributable action history.
- Portable `AGENTS.md` lets operators delegate wiki-memory operations to different agent hosts consistently.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Claude plugin | `claude plugin install wiki@llm-wiki` |
| Codex plugin | Clone repo, then install from `.agents/plugins/marketplace.json` in Codex `/plugins` |
| OpenCode instruction file | `plugins/llm-wiki-opencode/skills/wiki-manager/SKILL.md` |
| Portable protocol | `AGENTS.md` copied into agent context |

---

## Human-in-the-Loop Support

Optional. Humans may review generated wiki pages and outputs, but the research/compile/query pipeline is designed to run autonomously by agents.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw vector DB/RAG only** | Retrieval alone does not provide end-to-end wiki compilation, curation, and artifact generation workflow. |
| **Manual markdown wiki** | Human-authored by default; lacks agent-oriented automated ingest/compile/query loops. |
| **Single-session chat memory** | Does not provide durable, structured, cross-session knowledge accumulation in a wiki substrate. |

---

## Use Cases

- Build a long-lived domain research wiki for coding/product agents.
- Maintain institutional memory from agent sessions and retrospectives.
- Generate recurring deliverables (reports/slides/plans) grounded in an ever-growing knowledge base.
- Run thesis-style multi-angle investigations and preserve evidence-backed conclusions.
