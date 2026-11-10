Tomorrow's session of an agent should know what today's session learned: the user's preferred test runner, the API that kept timing out, the decision made three tasks ago. That needs a store outside the context window and a way for the agent to search it. Recall offers that store as something you run yourself. Its tagline is "Open-source memory for AI agents. MCP-native. Self-hosted."

### Memory as a local process

The dossier lists three surfaces: MCP over stdio, Docker, and searchable persistent memory. The onboarding command it prints is `uvx ai-recallworks stdio`, which starts the server as a stdio MCP process that a client such as a coding assistant can register. Docker is the other documented path. The record does not describe how the container is configured or what it persists.

MCP is marked as verified, and it is the main way an agent talks to Recall. No Agent Skill is listed. The catalog cites a [website](https://www.recall.works) and a GitHub repository, with no separate docs URL, so the site and the README are where the tool names and storage details live.

### Questions for the README

The record's generic sections say isolation may be by run, process, or memory namespace depending on deployment. For memory, that choice is the whole design. Before relying on Recall, find out whether separate agents or users get separate namespaces, where the data is persisted when running over stdio versus Docker, how search works, and whether memories can be listed, edited, or deleted by a person. Self-hosting means you hold the data, and also that backup and retention are yours to arrange.

### Beside other memory layers

The [memory and state collection](/categories/memory-and-state/) and the [memory layers guide](/guides/memory-layers-for-agents/) cover a wide spread. [Mem0](/services/mem0/) and [Supermemory](/services/supermemory/) present memory as an API you call. [Zep](/services/zep/) builds a temporal knowledge graph, and [Graphiti](/services/graphiti/) is the graph-building approach on its own. [Memoria](/services/memoria/) is the closest in deployment style, also with an MCP server you run, but it adds snapshots and branches over memory. Recall's record claims less than any of these: MCP first, self-hosted, searchable. That is either a virtue or a gap depending on what you need. If all you want is a place an agent can write facts and find them later, without a graph or a version history, smaller can be easier to reason about.

### Editor's take

Recall fits a developer who wants persistent memory for an MCP client on hardware they control and does not want an account with a hosted memory vendor. If the agent needs relationships between facts or a view of how they changed over time, Zep or Graphiti are built for that. If you want to roll memory back, Memoria is the one to compare. This page reflects the dossier, the project site, and the repository README; the server has not been started or queried for this review.
