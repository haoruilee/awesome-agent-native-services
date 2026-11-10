[Zep](/services/zep/) builds agent memory around a temporal knowledge graph. Mem0 puts its emphasis on the write path: deciding what in a conversation is worth keeping, reconciling it with what is already stored, and returning only the relevant pieces later.

### Deciding what to keep

The dossier describes a self-improving memory layer. After a conversation turn, the agent hands messages to Mem0. Mem0 extracts salient facts, compares each against existing memories, and chooses one of four outcomes: ADD, UPDATE, DELETE, or NOOP. Before the next turn, the agent searches with the current query and gets back the memories that matter, which it places in its prompt. The dossier is clear that the agent never reads or writes raw memory records.

Memories are typed as episodic for events, semantic for facts, and procedural for how-to knowledge. A graph variant, written Mem0ᵍ in the dossier, adds a relational representation for multi-entity queries. The dossier cites benchmark and token-saving percentages; current figures and their methodology belong in the vendor docs.

### Namespaces and interfaces

Scoping uses three identifiers: `user_id`, `agent_id`, and `run_id`. They combine, so a memory can belong to one user, one agent type, and one session at once.

The quickest documented path is `pip install mem0ai` followed by `m.add(messages, user_id=...)`. The Python SDK exposes add, search, update, and delete. A REST API offers full CRUD and search, documented at [docs.mem0.ai](https://docs.mem0.ai).

An official MCP server, `mem0-mcp`, published on PyPI as `mem0-mcp-server`, exposes the memory operations as MCP tools over stdio, Docker, or a hosted Smithery deployment. The dossier marks Agent Skills as official, but the command it gives, `npx skills add yonatangross/orchestkit --skill mem0-memory`, installs from a third-party repository, so treat it as community work.

### Automatic edits need review

The [Memory & State](/categories/memory-and-state/) category splits on who decides what gets stored. Mem0 decides for you. [Memoria](/services/memoria/) offers Git-level version control over memory, which matters when you need to see and revert each change. [Recall](/services/recall/) is open-source, MCP-native, and self-hosted. [Graphiti](/services/graphiti/) builds real-time knowledge graphs. The [memory layers guide](/guides/memory-layers-for-agents/) compares these designs.

Automatic DELETE and UPDATE are convenient and also a source of silent loss. Before relying on Mem0, find out whether past versions of a memory are retained and how to audit a deletion. Extraction is model-driven, so check which model runs it and who pays for those calls. The dossier lists a dashboard for inspection and an open-source repository, but does not compare hosted and self-hosted features. The healthcare use case it lists raises data-residency questions that belong in the vendor's terms, not in this catalog.

### Editor's take

Mem0 works best for assistants and support agents that accumulate per-user facts over many sessions, built by teams content to delegate the keep-or-discard decision. When every memory change must be traceable, Memoria's versioning is the safer starting point; for time-aware relationships between entities, Zep. This review comes from the dossier and Mem0's public docs, and none of its accuracy claims were checked by this project.
