### Two credentials, one store

Access is handed out two different ways, and the dossier documents only one of them in detail. The hosted MCP endpoint at `https://mcp.supermemory.ai/mcp` uses OAuth: the client opens a consent page once, and the owner picks which spaces that client may read or write. No API key sits in the client config. The Memory API and SDKs take an API key instead, and the dossier does not say whether such a key can be limited to particular spaces the way an OAuth grant is. Self-hosting gets one line, an MIT monorepo that can run fully locally, with no word on whether the OAuth flow and console come along. The [Supermemory docs](https://supermemory.ai/docs) are where both answers should be.

The repository ships a `skills/` directory, but no install command is documented, so the catalog leaves the Agent Skill status as unknown.

### Spaces and profiles

What the dossier does document is a memory engine with a clear tool contract. An agent saves facts and documents with `add_memory`, and the engine extracts versioned memories. A later session, in the same or a different MCP client, recalls them with `search_memory`, which returns memories with their source document IDs. `get_profile` returns stable and recent facts for the active space, and a `context` prompt primes a new session with them. `forget_memory` removes a memory by ID or by exact content.

Spaces are the isolation boundary. Reads and writes go to the active space unless a `namespace` targets another permitted one, so several assistants can share a project's memory without mixing in unrelated work. `who_am_i` reports the client's identity, role, and scope, and each connected app can be revoked from the console's Agents page.

A person can stay out of the loop entirely, or use the `guided-save` widget to edit a memory before it is stored.

### Shared memory elsewhere in the category

[Memory & State](/categories/memory-and-state/) holds several stores with different shapes, compared in [Memory layers for agents](/guides/memory-layers-for-agents/). [Mem0](/services/mem0/) calls itself the memory layer for your agents, the closest pitch. [Zep](/services/zep/) and [Graphiti](/services/graphiti/) attach time to facts through a knowledge graph. [Memoria](/services/memoria/) offers Git-level version control over memory. The tagline, "The Memory API for the AI era.", undersells the part the dossier spends most time on: per-client grants and spaces, which turn it into memory shared across assistants.

### Editor's take

Supermemory fits someone who works across several AI clients and wants one project memory they all read, with consent granted per client rather than a shared key copied between configs. Teams that need reasoning about when facts changed should compare Zep, and teams that want history on every edit should look at Memoria. This is our reading of the dossier and the vendor's MCP documentation; we have not connected a client to it.
