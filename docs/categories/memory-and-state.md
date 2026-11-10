---
title: "Memory & State | Agent-Native Services"
collection_label: "Memory & State"
description: "Persistent context, structured knowledge, and cross-session state owned by agents."
hero_image: "/assets/images/editorial-memory.webp"
hero_image_alt: "A dark glass disc on a gold rod set against a layered white form with a spherical void."
image: "/assets/images/editorial-memory.webp"
permalink: /categories/memory-and-state/
page_kind: collection
collection_number: "08"
service_count: 33
---

<p class="collection-source"><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/README.md">Collection notes ↗</a></p>

<div class="collection-essay" markdown="1">

A model call does not keep a store. Putting the whole transcript back into the next prompt works until the transcript is the prompt. A vector index still leaves the agent to decide what to write, what to overwrite, and what to drop. This collection is for services that take on that lifecycle: extract or accept a memory, keep it across sessions, and return a slice that fits the next call.

The mechanisms differ enough that the taglines should not be compared as if they were the same feature. Mem0's dossier describes automatic extraction and a reconciliation step that can add, update, delete, or leave a memory. Zep is the managed product built on a temporal knowledge graph. Graphiti is the open-source engine and is listed separately so the two are not treated as one entry. Ensue, mem9, and Dexio lean toward memory more than one agent can read. Dexio is a hosted wiki of linked pages. agentmemory, Claude-Mem, Engram, and Memorix are aimed at coding agents on a machine. Beads is a dependency-aware work graph in Dolt, closer to issues that survive a context reset than to a fact store. Compartment is an encrypted offline vault. Cognee, OpenViking, MemOS, and Supermemory are broader context or memory databases with their own APIs.

Automatic extraction is less work for the agent and can store a fact you did not mean to keep. Explicit writes are easier to audit and easier to forget to call. Hosted memory follows the agent across machines. Local memory stays next to the repo. Shared memory needs a rule for whose fact wins.

The approaches are compared in [Memory layers for agents](/guides/memory-layers-for-agents/).

</div>

<div class="service-grid">
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--01">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://agent-memory.dev" rel="noopener noreferrer">agentmemory</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/agentmemory/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Your coding agent remembers everything. No more re-explaining.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/agentmemory/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/agentmemory.md">Dossier ↗</a>
      <a href="https://github.com/rohitg00/agentmemory">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--02">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://beads.gascity.com" rel="noopener noreferrer">Beads</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/beads/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Dependency-aware, Dolt-backed issue tracker built for AI coding agents that survive context loss</p>
    <div class="service-card__actions">
      <a href="{{ '/services/beads/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/beads.md">Dossier ↗</a>
      <a href="https://github.com/gastownhall/beads">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--03">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://cmem.ai/" rel="noopener noreferrer">Claude-Mem</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/claude-mem/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Persistent memory compression system for Claude Code</p>
    <div class="service-card__actions">
      <a href="{{ '/services/claude-mem/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/claude-mem.md">Dossier ↗</a>
      <a href="https://github.com/thedotmack/claude-mem">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--arrival atlas-visual--04">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://www.cognee.ai" rel="noopener noreferrer">Cognee</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/cognee/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Memory control plane for AI Agents in 6 lines of code.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/cognee/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/cognee.md">Dossier ↗</a>
      <a href="https://github.com/topoteretes/cognee">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--05">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://maxfreedompollard.github.io/Compartment/" rel="noopener noreferrer">Compartment</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/compartment/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Encrypted, fully offline memory for AI agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/compartment/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/compartment.md">Dossier ↗</a>
      <a href="https://github.com/MaxFreedomPollard/Compartment">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--06">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://contextstream.io" rel="noopener noreferrer">ContextStream</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/contextstream/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Persistent memory. Millisecond code search.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/contextstream/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/contextstream.md">Dossier ↗</a>
      <a href="https://github.com/contextstream/mcp-server">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--07">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://dexio.wiki" rel="noopener noreferrer">Dexio</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/dexio/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">One wiki for all your agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/dexio/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/dexio.md">Dossier ↗</a>
      <a href="https://github.com/dexio-wiki/dexio">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--08">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://engram.gentlemanprogramming.com/" rel="noopener noreferrer">Engram</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/engram/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Persistent memory for AI coding agents</p>
    <div class="service-card__actions">
      <a href="{{ '/services/engram/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/engram.md">Dossier ↗</a>
      <a href="https://github.com/Gentleman-Programming/engram">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--arrival atlas-visual--09">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://ensue-network.ai" rel="noopener noreferrer">Ensue</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/ensue/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The shared memory network for AI agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/ensue/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/ensue.md">Dossier ↗</a>
      <a href="https://github.com/mutable-state-inc">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--arrival atlas-visual--10">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://goodmem.ai/" rel="noopener noreferrer">GoodMem</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/goodmem/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Memory that survives context windows.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/goodmem/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/goodmem.md">Dossier ↗</a>
      <a href="https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--11">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://help.getzep.com/graphiti" rel="noopener noreferrer">Graphiti</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/graphiti/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Build Real-Time Knowledge Graphs for AI Agents</p>
    <div class="service-card__actions">
      <a href="{{ '/services/graphiti/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/graphiti.md">Dossier ↗</a>
      <a href="https://github.com/getzep/graphiti">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--arrival atlas-visual--12">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://hindsight.vectorize.io" rel="noopener noreferrer">Hindsight</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/hindsight/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Agent Memory That Learns.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/hindsight/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/hindsight.md">Dossier ↗</a>
      <a href="https://github.com/vectorize-io/hindsight">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--arrival atlas-visual--13">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://llm-wiki.net" rel="noopener noreferrer">LLM Wiki</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/llm-wiki/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">LLM-compiled knowledge bases for any AI agent.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/llm-wiki/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/llm-wiki.md">Dossier ↗</a>
      <a href="https://github.com/nvk/llm-wiki">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--arrival atlas-visual--14">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://mcpmemory.services" rel="noopener noreferrer">mcp-memory-service</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/mcp-memory-service/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Memory for AI Agents — REST, MCP, OAuth, CLI</p>
    <div class="service-card__actions">
      <a href="{{ '/services/mcp-memory-service/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mcp-memory-service.md">Dossier ↗</a>
      <a href="https://github.com/doobidoo/mcp-memory-service">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--arrival atlas-visual--15">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://mem0.ai" rel="noopener noreferrer">Mem0</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/mem0/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The memory layer for your AI agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/mem0/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mem0.md">Dossier ↗</a>
      <a href="https://github.com/mem0ai/mem0">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--arrival atlas-visual--16">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://mem9.ai" rel="noopener noreferrer">mem9</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/mem9/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Persistent memory for AI agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/mem9/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mem9.md">Dossier ↗</a>
      <a href="https://github.com/mem9-ai/mem9">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--01">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://memmachine.ai" rel="noopener noreferrer">MemMachine</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/memmachine/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Universal memory layer for AI Agents. Scalable, extensible, and interoperable memory storage and retrieval for next-generation autonomous systems.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/memmachine/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memmachine.md">Dossier ↗</a>
      <a href="https://github.com/MemMachine/MemMachine">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--02">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://memmy.bot/" rel="noopener noreferrer">Memmy</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/memmy-agent/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Memmy is your personal AI agent &amp; local memory hub for all AI agents — it lets every AI connect to the same memory and keep self-evolving.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/memmy-agent/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memmy-agent.md">Dossier ↗</a>
      <a href="https://github.com/MemTensor/memmy-agent">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--03">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://www.memoir-ai.dev" rel="noopener noreferrer">Memoir</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/memoir/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Git for AI Memory</p>
    <div class="service-card__actions">
      <a href="{{ '/services/memoir/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memoir.md">Dossier ↗</a>
      <a href="https://github.com/zhangfengcdt/memoir">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--04">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://github.com/matrixorigin/Memoria" rel="noopener noreferrer">Memoria</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/memoria/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Persistent memory layer for AI agents with Git-level version control.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/memoria/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memoria.md">Dossier ↗</a>
      <a href="https://github.com/matrixorigin/Memoria">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--05">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://github.com/AVIDS2/memorix" rel="noopener noreferrer">Memorix</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/memorix/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Local-first shared memory layer for AI coding agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/memorix/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memorix.md">Dossier ↗</a>
      <a href="https://github.com/AVIDS2/memorix">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--06">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://openmem.net" rel="noopener noreferrer">MemOS</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/memos/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">A memory OS for LLM and AI agent systems.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/memos/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memos.md">Dossier ↗</a>
      <a href="https://github.com/MemTensor/MemOS">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--07">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://mempalaceofficial.com" rel="noopener noreferrer">MemPalace</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/mempalace/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The best-benchmarked open-source AI memory system. And it&#39;s free.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/mempalace/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mempalace.md">Dossier ↗</a>
      <a href="https://github.com/MemPalace/mempalace">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--08">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://zilliztech.github.io/memsearch/" rel="noopener noreferrer">MemSearch</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/memsearch/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Cross-platform semantic memory for AI coding agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/memsearch/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memsearch.md">Dossier ↗</a>
      <a href="https://github.com/zilliztech/memsearch">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--09">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://memu.pro" rel="noopener noreferrer">memU</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/memu/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Memory for 24/7 proactive AI agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/memu/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/memu.md">Dossier ↗</a>
      <a href="https://github.com/NevaMind-AI/memU">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--10">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://mnemoverse.com/" rel="noopener noreferrer">Mnemoverse</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/mnemoverse/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Persistent memory for AI agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/mnemoverse/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/mnemoverse.md">Dossier ↗</a>
      <a href="https://github.com/mnemoverse/mcp-memory-server">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--11">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://openviking.ai" rel="noopener noreferrer">OpenViking</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/openviking/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The context database for AI agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/openviking/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/openviking.md">Dossier ↗</a>
      <a href="https://github.com/volcengine/OpenViking">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--12">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://www.projectmem.dev" rel="noopener noreferrer">projectmem</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/projectmem/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">We don&#39;t make AI smarter. We make it experienced.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/projectmem/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/projectmem.md">Dossier ↗</a>
      <a href="https://github.com/riponcm/projectmem">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--13">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://www.recall.works" rel="noopener noreferrer">Recall</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/recall/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Open-source memory for AI agents. MCP-native. Self-hosted.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/recall/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/recall.md">Dossier ↗</a>
      <a href="https://github.com/RecallWorks/Recall">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--14">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://supermemory.ai" rel="noopener noreferrer">Supermemory</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/supermemory/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The Memory API for the AI era.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/supermemory/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/supermemory.md">Dossier ↗</a>
      <a href="https://github.com/supermemoryai/supermemory">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--15">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://github.com/TencentCloud/TencentDB-Agent-Memory" rel="noopener noreferrer">TencentDB Agent Memory</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/tencentdb-agent-memory/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Agents remember,Humans innovate.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/tencentdb-agent-memory/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/tencentdb-agent-memory.md">Dossier ↗</a>
      <a href="https://github.com/TencentCloud/TencentDB-Agent-Memory">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--16">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://zambo.dev" rel="noopener noreferrer">Zambo</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/zambo/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Give your AI hands, memory, and proof.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/zambo/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/zambo.md">Dossier ↗</a>
      <a href="https://github.com/zambodotdev/zambo-mcp">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--arrival atlas-visual--01">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://www.getzep.com" rel="noopener noreferrer">Zep</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/zep/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The memory layer for production AI agents — powered by a temporal knowledge graph.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/zep/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/zep.md">Dossier ↗</a>
      <a href="https://github.com/getzep/zep">Official repo ↗</a>
    </div>
    </div>
  </article>
</div>
<nav class="collection-pagination" aria-label="Adjacent collections">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Previous collection</small><strong>← Agent Harnesses & Operator Surfaces</strong></a>
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Next collection</small><strong>Search & Web Intelligence →</strong></a>
</nav>
