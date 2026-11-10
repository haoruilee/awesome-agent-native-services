### Open repository, managed product

Two catalog records disagree on how open Zep is. The Zep dossier lists `getzep/zep` as the open-source core platform. The Graphiti dossier, citing the official README, describes Zep as managed infrastructure on a proprietary Context Graph Engine, with Graphiti as the open framework you host yourself. Neither record describes a self-hosted Zep deployment. Plan on Zep being a service someone else runs unless the [Zep docs](https://help.getzep.com) say otherwise for your case, and read the data handling terms on that basis.

The dossier lists no official Agent Skill. The MCP server is documented with a stdio transport, so it runs beside the client and calls Zep with your key.

### Facts with dates

The documented idea is a temporal knowledge graph. After each turn the agent adds the message. Graphiti, the engine underneath, extracts entities, facts, and relationships and compares them against what the graph already holds. When a fact changes, the old one is marked invalid with a date range instead of being deleted. Before the next response, the agent searches and gets back an assembled context object of current facts, entities, and changed preferences, ready to drop into a prompt.

The calls shown are `zep.add_session_message(...)` and `zep.search(...)`, after `pip install zep-python`. TypeScript and Go SDKs and a REST API are listed as well. A `session_id` scopes a conversation and a `user_id` scopes long-term memory across sessions. Custom entity and relationship types can be defined with Pydantic or Zod, and structured business data such as CRM records can be loaded into the same graph as conversation.

No person curates the graph. A dashboard exists for inspection and debugging.

### Among memory services

The [Memory & State](/categories/memory-and-state/) category keeps Zep and [Graphiti](/services/graphiti/) apart on purpose: same lineage, different operator. [Mem0](/services/mem0/) is the comparison the Zep dossier draws itself, describing it as add, update, and delete extraction without temporal reasoning. [Cognee](/services/cognee/) builds a graph from warehouses and documents rather than conversation. [Supermemory](/services/supermemory/) separates memories into spaces. The tagline, "The memory layer for production AI agents — powered by a temporal knowledge graph.", is the vendor's framing. The [Memory layers for agents](/guides/memory-layers-for-agents/) guide walks through the alternatives.

### Editor's take

Zep is the choice for assistants whose users change their minds over months, where knowing when something stopped being true matters as much as the fact itself, and where a managed service is acceptable. Teams that need the same model on their own database should go to Graphiti directly and accept running it. Everything here is drawn from two catalog files and Zep's help center; no session was written to Zep while preparing it.
