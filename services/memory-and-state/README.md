# Memory & State Services

> Services that give AI agents **persistent, queryable memory across sessions** — treating memory as infrastructure rather than application logic, and managing the full lifecycle of what agents remember, forget, and retrieve.

## Why This Category Exists

LLMs are stateless by design. Every new conversation starts from zero. This is acceptable for a one-shot Q&A, but fundamentally broken for an autonomous agent that must:

- Remember a user's preferences from a previous session
- Build on findings from prior research runs
- Maintain continuity in long-running tasks spanning days or weeks
- Accumulate skills and avoid repeating past mistakes

Naive approaches — stuffing the entire conversation history into the context window — are expensive, hit token limits, and inject irrelevant noise. A vector database helps with retrieval but puts the agent in charge of deciding what to store, what to update, and what to discard.

Agent-native memory services solve this by providing:

1. **Automatic extraction** — the service decides what facts are worth retaining from each conversation
2. **Conflict resolution** — new facts are reconciled against existing memories (UPDATE, not just INSERT)
3. **Efficient retrieval** — only the relevant memories are fetched, not the entire history
4. **Cross-session persistence** — memories survive agent restarts and model redeployments

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Memmy](memmy-agent.md) [![⭐](https://img.shields.io/github/stars/MemTensor/memmy-agent?style=social)](https://github.com/MemTensor/memmy-agent) | Personal AI agent and local memory hub shared across AI agents | JSON CLI, REST, Agent Skills/hooks, OpenAI-compatible Agent API | ⚠️ client only |
| [Memoria](memoria.md) [![⭐](https://img.shields.io/github/stars/matrixorigin/Memoria?style=social)](https://github.com/matrixorigin/Memoria) | Persistent memory layer for AI agents with Git-level version control | REST API, MCP server, semantic search, snapshots/branches | ✅ |
| [Recall](recall.md) [![⭐](https://img.shields.io/github/stars/RecallWorks/Recall?style=social)](https://github.com/RecallWorks/Recall) | Open-source memory for AI agents. MCP-native. Self-hosted. | MCP stdio, Docker, searchable persistent memory | ✅ |
| [Mem0](mem0.md) | The memory layer for your AI agents | Python SDK, REST API | ✅ |
| [Zep](zep.md) | Agent memory powered by a temporal knowledge graph | Python SDK, TypeScript SDK, Go SDK, REST API | ✅ |
| [Ensue](ensue.md) | The shared memory network for AI agents | REST API, MCP stdio, Python Coordinator SDK, Agent Skill | ✅ |
| [OpenViking](openviking.md) | The context database for AI agents | Python SDK, Rust CLI, HTTP MCP server, Agent Plugins | ✅ |
| [MemOS](memos.md) | A memory OS for LLM and AI agent systems | Python SDK, REST API, MCP server, OpenClaw Plugin | ✅ |
| [memU](memu.md) | Memory for 24/7 proactive AI agents | Python SDK, REST API | ⚠️ |
| [mem9](mem9.md) | Persistent memory for AI agents | REST API, OpenClaw/Claude Code/OpenCode plugins | ⚠️ |
| [LLM Wiki](llm-wiki.md) [![⭐](https://img.shields.io/github/stars/nvk/llm-wiki?style=social)](https://github.com/nvk/llm-wiki) | LLM-compiled knowledge bases for any AI agent | Claude plugin, Codex plugin, AGENTS.md protocol | ⚠️ |
| [LycheeMem](lycheemem.md) | Compact memory framework for LLM agents | REST API, HTTP MCP, OpenClaw plugin | ✅ |
| [MemMachine](memmachine.md) [![⭐](https://img.shields.io/github/stars/MemMachine/MemMachine?style=social)](https://github.com/MemMachine/MemMachine) | Universal memory layer — episodic graph + profile SQL + working memory | Python SDK, LangChain/CrewAI adapters, REST API | ⚠️ |
| [Cognee](cognee.md) [![⭐](https://img.shields.io/github/stars/topoteretes/cognee?style=social)](https://github.com/topoteretes/cognee) | Memory control plane for AI agents — managed world model with auto ontology | Python SDK, 28+ connectors, MCP server, framework adapters | ✅ |
| [Hindsight](hindsight.md) [![⭐](https://img.shields.io/github/stars/vectorize-io/hindsight?style=social)](https://github.com/vectorize-io/hindsight) | Agent Memory That Learns | Python SDK, open-source memory service, cookbook examples | ⚠️ |
| [agentmemory](agentmemory.md) [![⭐](https://img.shields.io/github/stars/rohitg00/agentmemory?style=social)](https://github.com/rohitg00/agentmemory) | Your coding agent remembers everything. No more re-explaining. | Local memory server, MCP, Skills, INSTALL_FOR_AGENTS.md | ✅ |
| [TencentDB Agent Memory](tencentdb-agent-memory.md) [![⭐](https://img.shields.io/github/stars/TencentCloud/TencentDB-Agent-Memory?style=social)](https://github.com/TencentCloud/TencentDB-Agent-Memory) | Agents remember,Humans innovate. | OpenClaw plugin, Hermes Gateway, layered + symbolic memory | ⚠️ |
| [MemPalace](mempalace.md) [![⭐](https://img.shields.io/github/stars/MemPalace/mempalace?style=social)](https://github.com/MemPalace/mempalace) | The best-benchmarked open-source AI memory system. And it's free. | CLI, stdio MCP, Python API, verbatim palace + graph | ✅ |
| [MemSearch](memsearch.md) [![⭐](https://img.shields.io/github/stars/zilliztech/memsearch?style=social)](https://github.com/zilliztech/memsearch) | Cross-platform semantic memory for AI coding agents | CLI, Python API, Claude/Codex/DSH/OpenClaw/OpenCode plugins | ⚠️ |
| [Claude-Mem](claude-mem.md) [![⭐](https://img.shields.io/github/stars/thedotmack/claude-mem?style=social)](https://github.com/thedotmack/claude-mem) | Persistent memory compression system for Claude Code | Installer, lifecycle hooks, local worker, MCP search | ✅ |
| [Engram](engram.md) [![⭐](https://img.shields.io/github/stars/Gentleman-Programming/engram?style=social)](https://github.com/Gentleman-Programming/engram) | Persistent memory for AI coding agents | CLI, stdio MCP, HTTP API, TUI, `engram setup` | ✅ |
| [Beads](beads.md) [![⭐](https://img.shields.io/github/stars/gastownhall/beads?style=social)](https://github.com/gastownhall/beads) | Dependency-aware, Dolt-backed issue tracker built for AI coding agents that survive context loss | `bd` CLI, `beads-mcp`, `bd setup` recipes, Dolt sync | ✅ |
| [projectmem](projectmem.md) [![⭐](https://img.shields.io/github/stars/riponcm/projectmem?style=social)](https://github.com/riponcm/projectmem) | We don't make AI smarter. We make it experienced. | Typed event log, `pjm` CLI, stdio MCP, precheck gate | ✅ |
| [Memoir](memoir.md) [![⭐](https://img.shields.io/github/stars/zhangfengcdt/memoir?style=social)](https://github.com/zhangfengcdt/memoir) | Git for AI Memory | CLI, `memoir-mcp`, Claude Code/Codex plugins (Alpha) | ✅ |
| [Memorix](memorix.md) [![⭐](https://img.shields.io/github/stars/AVIDS2/memorix?style=social)](https://github.com/AVIDS2/memorix) | Local-first shared memory layer for AI coding agents. | Git-root daemon, `memorix serve`, orchestration, skills | ✅ |
| [Compartment](compartment.md) [![⭐](https://img.shields.io/github/stars/MaxFreedomPollard/Compartment?style=social)](https://github.com/MaxFreedomPollard/Compartment) | Encrypted, fully offline memory for AI agents. | Encrypted vault, `compartment serve` MCP, integrate CLI | ✅ |



---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide **automatic memory extraction** — not just storage (agent does not need to decide what to save).
2. Handle **memory lifecycle** — deduplication, conflict resolution, and eviction.
3. Support **cross-session persistence** — memories survive across agent restarts.
4. Provide **semantic retrieval** — not just key-value lookup.
5. Be designed as **external infrastructure** — not embedded in a specific agent framework.
