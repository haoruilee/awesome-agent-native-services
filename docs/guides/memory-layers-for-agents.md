---
layout: default
title: "Memory layers for agents: approaches and trade-offs"
description: "Fact extractors, temporal graphs, shared wikis, and local memory for coding agents, and why a vector index is not the whole problem."
permalink: /guides/memory-layers-for-agents/
page_kind: document
ads: false
guide_order: 4
---

A model does not remember the last session. The next call sees what you put in the prompt and nothing else. Stuffing the transcript back in works until the transcript is most of the window, and then it works badly, because the old lines crowd out the question. A vector database is the usual next step, and it solves retrieval of chunks. It does not decide which sentence was a fact, whether the new sentence contradicts the old one, or which agent is allowed to read it. That lifecycle is what the [memory collection](/categories/memory-and-state/) is selecting for. The category notes say so directly: extraction or an equivalent write path, a way to update and drop, persistence across restarts, retrieval by meaning, and a store that is infrastructure rather than a helper buried in one framework.

This guide sorts the listings by the mechanism, not by which tagline says "memory." The mechanisms imply different bugs.

## Automatic facts

[Mem0](https://mem0.ai) is the clearest statement of automatic memory in the catalog. The [docs](https://docs.mem0.ai) and the dossier describe a layer that extracts what is worth keeping, reconciles it with what is already stored, and returns a slice for the next prompt. The reconciliation actions the dossier names are add, update, delete, and no-op. Namespaces separate users, agents, or sessions. An MCP server is recorded. The agent is not supposed to manage the table.

The appeal is that the agent cannot forget to write. The failure is that it also cannot fully refuse a write it did not intend. A stray preference in a test conversation becomes a fact. If you need an audit of who asserted something, look for whether the product stores a source. Mem0's positioning is a memory layer for agents, not a system of record you edit by hand. The dossier also mentions a graph form of the same product. Treat "graph" as their feature name until you have read the docs. It is not the same object as the next section.

Vendor pages sometimes attach accuracy or token figures to this design. The Mem0 dossier repeats some of those figures. This guide does not. They are the vendor's benchmark story. If you care about them, read the current write-up on their site and decide whether the setup matches yours. This catalog has not rerun it.

## Facts that expire

[Zep](https://www.getzep.com) is a managed memory service whose dossier says it is built on a temporal knowledge graph. Facts have a validity window. A newer fact can invalidate an older one instead of leaving both chunks nearby for the model to reconcile in prose. The [Zep docs](https://help.getzep.com) describe context assembled for a prompt in one call. Custom entity types are part of the product, via schemas, so the graph is not only whatever the extractor felt like naming.

[Graphiti](https://help.getzep.com/graphiti) is the open-source engine behind that idea, and it is a separate catalog entry so nobody files one issue against the wrong project. The dossier describes episodes in, entities and facts out, validity windows, and hybrid retrieval. There is a paper linked from the dossier for the design. Use Graphiti when you will run the engine. Use Zep when you want the hosted product. Using either and calling it "just a vector store" throws away the reason they are in the catalog. The point of a validity window is that "the user lives in Paris" and "the user moved to Lyon" should not both come back as current.

Temporal structure does not free you from a bad extractor. It gives the contradiction a place to sit. Someone still has to notice if the extractor marked the wrong fact as current. That is an evaluation problem, which belongs with the [observability collection](/categories/observability-and-tracing/), not inside the graph by magic.

## A world model, not a note

[Cognee](https://www.cognee.ai) describes itself as a memory control plane: connectors into data the organization already has, an ontology, a graph plus vectors, recall back to the agent. [OpenViking](https://openviking.ai) is positioned as a context database. [MemOS](https://openmem.net) calls itself a memory operating system and ships an API and an MCP server. [Supermemory](https://supermemory.ai) is a memory API with a remote MCP server, spaces, and a self-host option in the dossier.

These are closer to "what the agent is allowed to know about a domain" than to "what the user said yesterday." The trade-off is setup. A fact extractor can be pointed at a transcript and left. A control plane wants sources, and it will be wrong in ways that reflect the sources. If your agent only chats, this is more system than you need. If your agent answers from a changing body of internal data, a chat-memory tool will not grow that body for you.

## Memory more than one agent can read

[Ensue](https://ensue-network.ai) is a shared memory network. The dossier's problem statement is agents that restart from zero and repeat each other's work. The join path is a skill file, which is why it appears on the catalog's URL-onboarding list. [mem9](https://mem9.ai) is cloud memory aimed at agents on different coding tools sharing a pool, also with a skill document. [Dexio](https://dexio.wiki) is a hosted wiki: agents read and write linked markdown pages over MCP, including a documented agent entrance at `https://dexio.wiki/agents.md`. The dossier's model is the LLM wiki pattern. Pages are revised as the agents learn, and they link to each other. That is a different artifact from a bag of extracted triples. A person can read a wiki. A person cannot read a vector index without a tool.

Shared memory needs an owner for conflicts. Two agents can write two pages, or two facts, about the same outage. Dexio's model pushes that into the page history of a wiki. Ensue's model is a network agents subscribe to. Neither is "the company wiki" unless you decide it is and you govern it. Do not point a shared store at customer conversations and a coding-agent store at the same time without a namespace. The category criteria mention cross-session persistence. They do not require that every session in the building share one brain.

## On the machine, next to the code

A large part of the collection is memory for coding agents, local or close to it.

[agentmemory](https://agent-memory.dev) is a local server with MCP and skills, aimed at a coding agent that otherwise asks the same question every session. [Claude-Mem](https://cmem.ai/) compresses what a coding session did. The dossier describes hooks that record prompts and tool use, a local worker that summarizes, and MCP search later. [Engram](https://engram.gentlemanprogramming.com/) is persistent memory with a CLI and MCP. [Memorix](https://github.com/AVIDS2/memorix) is local-first and shared among coding agents on a machine. [MemSearch](https://zilliztech.github.io/memsearch/) is semantic memory aimed at coding agents across several clients.

[Beads](https://beads.gascity.com) is the outlier that earns its place by not pretending to be a fact store. It is a dependency-aware issue graph in Dolt, with hash ids so concurrent agents do not collide and a ready query so an agent picks up unblocked work. The memory is the work graph, which survives a context reset because it is a database you can push, not because an extractor summarized the chat. Use it when the thing being forgotten is a task. Use a fact store when the thing being forgotten is a preference or a decision.

[Compartment](https://maxfreedompollard.github.io/Compartment/) is the privacy extreme: encrypted, offline, one claim per memory, a source and a date required, no model inside the vault. The dossier describes a hash-chained log. Choose it when the memory cannot leave the machine and you want the write path to be strict. Do not choose it when several hosted agents must read the same store. Offline is the feature.

Local memory fails in a hosted deployment unless you sync it. People discover this when the laptop agent is wise and the CI agent is not. The sync mechanism, if any, is part of the product. Beads has Dolt. A folder of markdown has git, if you commit it. A process listening on localhost has neither until you add them.

## What a vector database still is

A vector index is a reasonable component inside several of these systems. Graphiti's dossier says retrieval is hybrid: semantic, keyword, and graph. Compartment's dossier says the same about its local index. The reason a plain vector service does not qualify on its own is the category rule. If the agent decides every write and every delete, the lifecycle is application code, and the index is a library. That can be the right architecture when you want the control. It is not the thing this collection is pointing at.

If you build the lifecycle yourself, be explicit about four operations the hosted products are packaging: what is allowed to be written, how a contradiction is represented, how something is forgotten, and which identity the row belongs to. Skipping "forgotten" is how memory products fill up with test data and then inject it into production prompts.

## Choosing without a leaderboard

If the agent is a coding assistant on one repo, start local: agentmemory, Claude-Mem, Engram, or Beads if the forgotten object is work rather than chat. You avoid sending the repository's conversations to a vendor, and you accept that the memory does not follow a teammate until you sync it.

If many agents, or many sessions of one product, must share user-specific facts, look at Mem0, Zep, mem9, or Supermemory, and read how a namespace is named. "User" and "agent" are different keys. Mixing them is a data leak between tenants.

If the fact changes and the old fact must remain as history, prefer a temporal graph, Zep or Graphiti, over a store that only upserts a chunk.

If the artifact should be readable as pages, Dexio or an LLM wiki is closer than a triple store. [LLM Wiki](https://llm-wiki.net) is the pattern as a project in the same collection.

If nothing may leave the machine and the claims must be short and sourced, Compartment is the listing that says that in its own docs.

Then decide who writes. Automatic extraction, explicit tool calls, and hooks on a coding session are three write paths. Hooks see tool use the model will not remember to summarize. Explicit calls see only what the prompt remembered to store. Extraction sees the transcript and applies someone else's judgment. None of the three is free of error. The [editorial policy](/editorial-policy/) forbids this page from pretending a benchmark settled it.
