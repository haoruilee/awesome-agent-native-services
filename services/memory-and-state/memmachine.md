# MemMachine

> **"Universal memory layer for AI Agents. Scalable, extensible, and interoperable memory storage and retrieval for next-generation autonomous systems."**

| | |
|---|---|
| **Website** | https://memmachine.ai |
| **Docs** | https://docs.memmachine.ai |
| **GitHub** | https://github.com/MemMachine/MemMachine |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **Stars** | 3,000+ (rapid growth through 2026) |

---

## Official Website

https://memmachine.ai

---

## Official Repo

https://github.com/MemMachine/MemMachine

---

## How to Use (Agent Onboarding)

```
pip install memmachine
# then:
from memmachine import Memory
m = Memory()
m.add(messages, agent_id=...)
context = m.recall(query, agent_id=...)
```

Native LangChain and CrewAI integrations ship in-tree.

---

## Agent Skills

**Status:** ⚠️ Not yet published as an official skill.

```bash
npx clawhub@latest search memmachine
```

---

## MCP

**Status:** ⚠️ MCP server is on the roadmap; community wrappers exist. Primary surface is SDK + REST.

| Detail | Value |
|---|---|
| **MCP Repo** | (community wrappers; not first-party as of writing) |
| **Transport** | n/a |
| **Compatible Clients** | any agent runtime via SDK |

---

## What It Does

MemMachine is a long-term memory layer for AI agents that explicitly composes **three memory types** as separate, interoperable subsystems:

1. **Episodic memory** — graph-backed conversational context (who said what, in what order, with what relationships).
2. **Profile memory** — SQL-backed user / agent facts (durable, queryable, deduplicated).
3. **Working memory** — short-term scratchpad scoped to the current run.

This three-layer model is the differentiator from one-bucket memory layers: episodic graph traversal answers "what happened in the conversation?", profile SQL answers "what do we know about this user?", and working memory is the running scratchpad that flushes to the other two on a schedule. The library is framework-agnostic but ships first-class adapters for LangChain and CrewAI.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repo description: *"Universal memory layer for AI Agents"* |
| **Agent-specific primitive** | Three-layer memory composition (episodic graph + profile SQL + working memory) — no human-facing equivalent |
| **Autonomy-compatible control plane** | Memory lifecycle (extract / update / consolidate) is automatic; the agent does not decide what to save |
| **M2M integration surface** | Python SDK; LangChain / CrewAI adapters; REST |
| **Identity / delegation** | Memory namespaced per `agent_id` (and per `user_id`); cross-agent sharing is opt-in |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Episodic Memory** | Graph of conversational events with temporal edges |
| **Profile Memory** | SQL store of agent / user facts with conflict resolution |
| **Working Memory** | Short-term scratchpad; flushes to episodic + profile on a schedule |
| **Hybrid Recall** | One query hits all three layers and ranks together |
| **Framework Adapters** | LangChain, CrewAI in-tree |

---

## Autonomy Model

1. Agent calls `m.add(messages, agent_id=...)` after each turn.
2. The library extracts facts, updates the profile store, appends to the episodic graph, and updates working memory.
3. Conflicts are resolved automatically (UPDATE / DELETE / NOOP).
4. On retrieval, `m.recall(query)` does hybrid retrieval across all three layers.

The agent never needs to decide which store to write to or how to invalidate a stale fact.

---

## Identity and Delegation Model

- Memories are namespaced per `agent_id` and `user_id`.
- Cross-agent sharing is opt-in (a memory can be tagged for shared access).
- Audit log of writes per namespace.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install memmachine` |
| LangChain adapter | In-tree |
| CrewAI adapter | In-tree |
| REST API | For non-Python agents |

---

## Human-in-the-Loop Support

Out of scope for MemMachine itself; compose with HumanLayer or Inferable if specific memory writes need approval.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Plain vector DB** | One bucket — no separate episodic / profile / working layers; no conflict resolution |
| **Mem0** | Excellent extraction-based memory but uses a single layer; MemMachine differs by composing graph + SQL + working memory |
| **Zep** | Temporal graph focus; MemMachine adds explicit profile (SQL) and working memory layers as peers |

---

## Use Cases

- **Long-running personal agents** — agent remembers user preferences over months (profile), recalls last week's chats (episodic), and operates on today's scratchpad (working)
- **Multi-agent collaborations** — each agent has its own memory namespace; shared facts are tagged for cross-agent access
- **Replacing ad-hoc RAG** — drop in MemMachine where a team had built their own vector + SQL stack
