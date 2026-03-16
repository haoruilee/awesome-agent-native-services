# Mem0

> **"The memory layer for your AI agents."**

| | |
|---|---|
| **Website** | https://mem0.ai |
| **Docs** | https://docs.mem0.ai |
| **GitHub** | https://github.com/mem0ai/mem0 |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social)](https://github.com/mem0ai/mem0) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **Funding** | $24M Series A |
| **Adoption** | 100,000+ developers |

---

## Official Website

https://mem0.ai

---

## Official Repo

https://github.com/mem0ai/mem0

https://github.com/mem0ai/mem0-mcp — Official MCP server

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ✅ Official skill available via the AgentSkills ecosystem

Community skill published on skills.sh:

```bash
npx skills add yonatangross/orchestkit --skill mem0-memory
```

| Skill | What It Teaches the Agent |
|---|---|
| `mem0-memory` | Persist and retrieve semantic memories across Claude sessions; organize by scope (project-decisions, project-patterns, project-continuity); auto-categorize across auth, testing, deployment, and database domains |

**Compatibility:** Claude Code, Cursor, and all [AgentSkills](https://agentskills.io/)-compatible tools.

> Set `MEM0_API_KEY` and `MEM0_USER_ID` in your agent's environment settings after installation. See [skills.sh/yonatangross/orchestkit/mem0-memory](https://skills.sh/yonatangross/orchestkit/mem0-memory).

---

## MCP

**Status:** ✅ Available

Mem0 provides an official MCP server (`mem0-mcp`) that exposes all nine memory management operations as MCP tools, enabling any MCP-compatible client to read and write agent memory.

| Detail | Value |
|---|---|
| **MCP Docs** | https://docs.mem0.ai/integrations/mcp-server |
| **MCP Repo** | https://github.com/mem0ai/mem0-mcp |
| **PyPI Package** | `mem0-mcp-server` (install via `uvx` or `pip`) |
| **Transport** | stdio / Docker / Smithery (hosted) |
| **Compatible Clients** | Claude Desktop, Cursor, Windsurf, any MCP-compatible client |

---

## What It Does

Mem0 is a self-improving, adaptive memory layer for AI agents. It automatically extracts salient facts from conversations, reconciles new information with existing memories, and returns only the relevant context at query time — reducing token costs by 90% versus full context injection, while improving answer accuracy by 26% on memory benchmarks.

The agent calls the Mem0 API; Mem0 handles all decisions about what to store, what to update, and what to retrieve. The agent does not manage its own memory.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Positioned as agent infrastructure: *"the memory layer for your AI agents"*; not a chat history feature |
| **Agent-specific primitive** | Automatic memory extraction; conflict resolution (ADD/UPDATE/DELETE/NOOP); episodic, semantic, and procedural memory types |
| **Autonomy-compatible control plane** | Memory is updated and retrieved autonomously during agent execution; no human curates memories |
| **M2M integration surface** | Python SDK, REST API, MCP server |
| **Identity / delegation** | Per-user and per-agent memory namespacing; graph-based relational memory (Mem0ᵍ) available |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Memory Extraction** | Automatically identifies which facts from a conversation are worth storing |
| **Memory Update** | Reconciles new facts against existing memories: ADD, UPDATE, DELETE, or NOOP |
| **Semantic Retrieval** | Fetches only the memories relevant to the current query |
| **Memory Types** | Episodic (events), semantic (facts), procedural (how-to knowledge) |
| **Graph Memory (Mem0ᵍ)** | Relational graph representation for complex multi-entity memory |
| **Namespacing** | Separate memory spaces per user, per agent, or per session |

---

## Two-Phase Memory Pipeline

```
Phase 1 — Extraction:
  Recent conversation + rolling summary
      ↓
  Extract candidate memories (facts, preferences, events)

Phase 2 — Update:
  Compare new memories against stored entries
      ↓
  ADD: new fact not previously known
  UPDATE: existing fact has changed
  DELETE: fact is no longer valid
  NOOP: fact already stored, no change needed
```

---

## Performance Benchmarks (LOCOMO Dataset)

| Metric | Mem0 vs. Comparison |
|---|---|
| Accuracy | +26% vs. OpenAI's memory approach |
| P95 Latency | 91% lower vs. full-context methods |
| Token Usage | 90% fewer tokens vs. full conversation history |

Real-world deployments show:
- 40% reduction in token costs
- Personalization scaled to tens of thousands of users

---

## Autonomy Model

1. Agent calls `mem0.add(messages, user_id=...)` after each conversation turn
2. Mem0 extracts relevant memories automatically
3. Before the next turn, agent calls `mem0.search(query, user_id=...)`
4. Mem0 returns the most relevant memories as context
5. Agent injects memories into system prompt or context window

The agent never reads or writes raw memory records — it interacts with the memory API and receives structured, relevant context.

---

## Identity and Delegation Model

- `user_id` namespaces memories per user
- `agent_id` namespaces memories per agent type
- `run_id` namespaces memories per session
- Multiple namespace dimensions can be combined: user × agent × session
- Graph memory supports relational queries across entities

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `mem0.add()`, `mem0.search()`, `mem0.update()`, `mem0.delete()` |
| REST API | Full memory CRUD and search |
| MCP Server | Model Context Protocol for direct LLM memory access |

---

## Human-in-the-Loop Support

None required. Mem0 manages all memory lifecycle decisions autonomously. Humans can inspect memory state via dashboard for debugging, but no human curation is needed for normal operation.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Pinecone / Weaviate (raw)** | Vector databases for storage; agents must write all extraction, deduplication, and lifecycle logic themselves |
| **Redis** | Key-value store; no semantic search, no memory extraction, no conflict resolution |
| **LangChain ConversationBufferMemory** | In-process memory that grows unboundedly; no cross-session persistence, no automatic extraction |
| **Full context injection** | Expensive, hits token limits, injects irrelevant noise from old conversations |

---

## Use Cases

- **Personal assistants** — remember user preferences, past decisions, and ongoing projects across sessions
- **Customer service agents** — remember customer history, past issues, and preferences across interactions
- **Research agents** — accumulate findings from previous research runs to build on over time
- **Coding agents** — remember project conventions, past mistakes, and user preferences across coding sessions
- **Healthcare agents** — maintain longitudinal patient context across appointments (with appropriate privacy controls)
