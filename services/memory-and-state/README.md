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
| [Mem0](mem0.md) | The memory layer for your AI agents | Python SDK, REST API | ✅ |
| [Zep](zep.md) | Agent memory powered by a temporal knowledge graph | Python SDK, TypeScript SDK, Go SDK, REST API | ✅ |

---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide **automatic memory extraction** — not just storage (agent does not need to decide what to save).
2. Handle **memory lifecycle** — deduplication, conflict resolution, and eviction.
3. Support **cross-session persistence** — memories survive across agent restarts.
4. Provide **semantic retrieval** — not just key-value lookup.
5. Be designed as **external infrastructure** — not embedded in a specific agent framework.
