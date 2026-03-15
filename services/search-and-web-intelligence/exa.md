# Exa

> **"The search engine designed for AI."**

| | |
|---|---|
| **Website** | https://exa.ai |
| **Docs** | https://docs.exa.ai |
| **GitHub** | https://github.com/exa-labs/exa-py |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |

---

## Official Website

https://exa.ai

---

## Official Repo

https://github.com/exa-labs/exa-py — Python SDK

https://github.com/exa-labs/exa-js — JavaScript/TypeScript SDK

https://github.com/exa-labs/exa-mcp-server — Official MCP server

---

## Skills

| Skill | Description |
|---|---|
| **Neural Search** | Embedding-based semantic search that understands conceptual meaning, not just keywords |
| **Content Extraction** | Return full, clean parsed text from search results |
| **Answer Synthesis** | Generate a synthesized answer with cited sources from multiple web pages |
| **Websets** | Build structured datasets of entities (companies, people, papers) from web search |
| **`exa-code` Search** | Specialized corpus search for code examples and documentation (optimized for coding agents) |
| **Similarity Search** | Find documents semantically similar to a given URL or text |
| **Domain-Constrained Search** | Limit semantic search to specific domains or site types |

---

## MCP

**Status:** ✅ Available

Exa provides an official MCP server (`exa-mcp-server`) enabling agents to trigger neural search, content extraction, and Webset operations directly through the Model Context Protocol.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/exa-labs/exa-mcp-server |
| **Transport** | stdio |
| **Compatible Clients** | Claude Desktop, Cursor, Windsurf, Mastra, any MCP-compatible client |

---

## What It Does

Exa is a neural search engine that retrieves semantically relevant web content using embeddings rather than keyword matching. Its output is clean, parsed text ready for LLM consumption — not SERP links. Where keyword search fails on complex entity queries (specific people, companies, research topics), Exa's semantic model returns 20× more accurate results. The `exa-code` product specifically targets coding agents with token-efficient code and documentation retrieval.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | *"The search engine designed for AI"*; output format, ranking model, and content parsing are all optimized for LLM context, not human reading |
| **Agent-specific primitive** | Semantic search (not keyword SERP); `exa-code` corpus for coding agents; Websets for structured dataset creation |
| **Autonomy-compatible control plane** | Agents call the API and receive LLM-ready content with no postprocessing |
| **M2M integration surface** | REST API, Python SDK, native LangChain/CrewAI/LlamaIndex/Mastra integrations |
| **Identity / delegation** | API key per integration |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Neural Search** | Embedding-based semantic search — understands conceptual meaning, not just keywords |
| **Contents** | Full, clean text extraction from search results |
| **Answer** | Synthesized answer from multiple sources (like Perplexity, but API-first) |
| **Websets** | Structured datasets built from web search (entities, companies, research papers) |
| **`exa-code`** | Specialized corpus of code and documentation, optimized for coding agents |

---

## Why Semantic vs. Keyword Matters for Agents

| Query Type | Keyword Search (Google) | Exa Semantic Search |
|---|---|---|
| `"researchers who study transformer attention mechanisms"` | Returns pages *about* the topic, not a list of researchers | Returns actual researchers with their work |
| `"companies building agent-native payments"` | Returns blog posts about payments | Returns actual company pages for relevant companies |
| `"shirts without stripes"` | Misinterprets exclusion — returns striped shirts too | Correctly understands the negative constraint |
| Code: `"how to implement sliding window attention in PyTorch"` | Returns StackOverflow discussions | `exa-code` returns actual code examples and docs |

---

## `exa-code`: Coding Agent Specialization

A specialized search product for coding agents:
- Searches a corpus of code repositories, documentation, and technical resources
- Returns token-efficient, directly usable code examples
- Optimized for coding agent workflows (not general web content)
- Reduces token usage compared to retrieving full documentation pages

---

## Autonomy Model

1. Agent calls `exa.search(query, type="neural", contents={"text": True})`
2. Exa retrieves semantically relevant documents, extracts clean text
3. Returns ranked results with full content — LLM-ready, no HTML parsing
4. Agent injects directly into context window

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Search, contents, answer, websets endpoints |
| Python SDK | `exa-py` package |
| LangChain | Native tool integration |
| CrewAI | Native tool integration |
| LlamaIndex | Native tool integration |
| Mastra | Native integration |
| MCP | Model Context Protocol server |

---

## Human-in-the-Loop Support

None required. Agents use search results directly.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Google Search API** | Keyword-based; returns SERP for human display; snippets require postprocessing |
| **Bing Search API** | Same issues; designed for human-facing applications |
| **Wikipedia API** | Limited to Wikipedia content; no general web search |
| **arXiv API** | Domain-specific academic papers only; no general web or code search |

---

## Use Cases

- **Research agents** — find specific entities (researchers, companies, papers) with semantic precision
- **Coding agents** — retrieve relevant code examples and documentation via `exa-code`
- **Entity research** — build structured datasets of companies, people, or topics via Websets
- **Competitive intelligence** — semantically search for companies with specific characteristics
- **Knowledge synthesis** — retrieve and synthesize information from multiple authoritative sources
