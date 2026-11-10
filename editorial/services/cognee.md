### What runs where

Open-source library first, managed tier second: that is the shape the dossier gives Cognee, with an on-prem enterprise option beside both. It does not say which graph and vector stores the local library uses by default, which model does the extraction, or what moves to the vendor's servers when you switch to Cognee Cloud. It promises per-agent and per-tenant permissions on memory without describing how an agent identity is defined or checked. Those are the questions to answer in the [Cognee docs](https://docs.cognee.ai) before pointing it at a warehouse full of customer data.

The catalog also has no confirmed Agent Skill. Cognee does not publish a `SKILL.md` of its own, though the dossier notes that skills from other catalog entries name it as a runtime target.

### Three verbs

The documented API is small. After `pip install cognee`, an agent calls `cognee.add(...)` to ingest content, `cognee.cognify()` to build or refresh what the dossier calls a world model, and `cognee.search(...)` to retrieve from it. Cognify is where the work happens: Cognee extracts an ontology, builds a graph alongside embeddings, and tunes recall as use accumulates. You can override the extracted schema with a custom ontology. Search results carry source attribution, so an agent can cite the PDF page, table row, or Slack message a fact came from.

The sources are broader than chat history. Connectors cover warehouses such as Snowflake and Postgres, files, Slack, and REST APIs. Cognify runs manually or on a schedule, which means the graph lags new data by however often you run it.

The first-party MCP server lives in a sibling `cognee-mcp` repository and runs over stdio or Streamable HTTP. Framework adapters are listed for Claude Code, Codex, Cursor, LangGraph, CrewAI, Continue, and others.

### Against other memory layers

In [Memory & State](/categories/memory-and-state/), the dossier draws its own line: [Mem0](/services/mem0/) and [Zep](/services/zep/) are shaped around conversation memory, while Cognee is shaped around an agent's world of documents, databases, and APIs. [Graphiti](/services/graphiti/) also builds a graph, but its emphasis is facts with validity windows that change over time. [Supermemory](/services/supermemory/) calls itself the memory API for the AI era and keeps memories in per-project spaces. The [Memory layers for agents](/guides/memory-layers-for-agents/) guide compares the approaches side by side.

### Editor's take

Cognee fits an agent whose knowledge lives in a warehouse, a document store, and a handful of APIs, and which needs cited answers drawn from all of them at once. An assistant that mostly needs to remember what a user said last week is better served by Mem0 or Zep. Our judgment comes from the dossier and Cognee's published docs; we have not run cognify on any data.
