### Everything is yours to hold

No service stands behind Graphiti. It is an Apache-2.0 Python framework, and the dossier is explicit that the credentials are the operator's: LLM API keys for extraction and the graph database login, both of which the MCP server inherits from its environment. There are no hosted users, threads, or API keys; those belong to the managed [Zep](/services/zep/) product. What the dossier does not settle is the MCP server's maturity. Graphiti's own docs call it experimental, and it starts from a cloned repository rather than an installed package. Read the [Graphiti docs](https://help.getzep.com/graphiti) on its current state before wiring an assistant to it.

No official Agent Skill has been published either.

### Episodes in, facts out

The documented model starts with an episode: a piece of text, a message, or JSON that the agent adds. Graphiti extracts entities and facts from it, and every fact carries a validity window and a pointer back to the episode that produced it. New episodes update the graph incrementally, and older facts that no longer hold are invalidated rather than recomputed in a batch. Retrieval mixes semantic search, BM25 keyword search, and graph traversal.

After `pip install graphiti-core`, the dossier shows `from graphiti_core import Graphiti`, a Neo4j driver passed in as `graph_driver`, then `add_episode(...)` and `search(...)`. Neo4j, FalkorDB, Kuzu, and Neptune are the supported backends. Custom entity and edge types are Pydantic models, and a `group_id` separates graphs per user or project.

The MCP server runs with `uv run graphiti_mcp_server.py`, over stdio for Claude Desktop or SSE for Cursor, and a Docker Compose file starts it together with a database. Its tools include `add_episode`, `search_facts`, `search_nodes`, and `clear_graph`.

### Not the same entry as Zep

[Memory & State](/categories/memory-and-state/) keeps Graphiti and Zep apart deliberately. Zep is the managed service with its own engine and dashboard; Graphiti is the open framework you run. [Cognee](/services/cognee/) also builds graphs, but from warehouses, documents, and APIs rather than episodes. [Recall](/services/recall/) is open-source, MCP-native, and self-hosted as well, so it is the other entry to read if running your own memory is the requirement. [Mem0](/services/mem0/) calls itself the memory layer for your agents. The tagline here is "Build Real-Time Knowledge Graphs for AI Agents". The [Memory layers for agents](/guides/memory-layers-for-agents/) guide sets the approaches next to each other.

### Editor's take

Graphiti is for teams that want temporal memory, already run or are willing to run a graph database, and want to read every line of the engine. If you would rather not operate Neo4j and an extraction pipeline, Zep packages the same lineage as a service. Our account reflects the dossier and Graphiti's public docs; we have not built a graph with it.
