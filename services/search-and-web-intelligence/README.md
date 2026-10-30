# Search & Web Intelligence Services

> Services that give AI agents **optimized, structured access to web information** — returning AI-ready content tuned for LLM context windows, not raw HTML or human-readable SERPs.

## Why This Category Exists

Traditional search APIs (Google Custom Search, Bing Search API) were designed to return results a human would display in a browser. The output format — ranked blue links, snippet strings, raw HTML — was designed for human eyes and requires significant postprocessing before an LLM can use it effectively.

AI agents have fundamentally different search requirements:

1. **Clean text output** — not HTML, not truncated snippets, but full readable content
2. **Pre-ranked relevance** — results already filtered for the agent's query, not a SERP for a human to scan
3. **Configurable depth** — some queries need surface-level summaries; others need deep multi-source synthesis
4. **Domain-specific search** — coding agents need code/documentation; research agents need academic papers
5. **Structured extraction** — not just "here's the page" but "here's the entity data you requested, as JSON"

The services in this category were designed with these requirements as the primary specification.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [contextX](contextx.md) [![⭐](https://img.shields.io/github/stars/KayanoLiam/ContextX?style=social)](https://github.com/KayanoLiam/ContextX) | Remote MCP server for fast and multi-agent deep search | Streamable HTTP MCP, `grok_search`, `grok_deep_search` | ✅ |
| [Jina DeepSearch](jina-deepsearch.md) | Agentic search and deep research API for AI applications | HTTP API, LLM-ready retrieval, research synthesis | ⚠️ |
| [Tavily](tavily.md) | Connect your agent to the web | REST API, Python SDK, LangChain/LlamaIndex/CrewAI integrations | ✅ |
| [Exa](exa.md) | The search engine designed for AI | REST API, Python SDK, LangChain/CrewAI/LlamaIndex/Mastra integrations | ✅ |
| [Parallel](parallel.md) | The highest accuracy web search for your AI | Search/Task/FindAll/Monitor APIs · SDKs · hosted Search MCP & task-mcp | ✅ |
| [Jina Reader](jina-reader.md) [![⭐](https://img.shields.io/github/stars/jina-ai/reader?style=social)](https://github.com/jina-ai/reader) | URL and search results as LLM-friendly text | `r.jina.ai` / `s.jina.ai` · MCP · PDF & image handling | ✅ |
| [Linkup](linkup.md) [![⭐](https://img.shields.io/github/stars/LinkupPlatform/linkup-python-sdk?style=social)](https://github.com/LinkupPlatform/linkup-python-sdk) | Search API for AI agents and LLM apps | LLM-oriented search, structured retrieval, citation-ready outputs | ⚠️ |
| [NotHumanSearch](nothumansearch.md) | Agent-first search — the index of services designed for AI, not humans | REST API · OpenAPI 3.0 · MCP (`ai.nothumansearch/search`) · `llms.txt` onboarding | ✅ |
| [Agent Search MCP](agent-search-mcp.md) [![⭐](https://img.shields.io/github/stars/lennney/agent-search-mcp?style=social)](https://github.com/lennney/agent-search-mcp) | Free-first Chinese and English web search with inspectable evidence | MCP stdio/HTTP, `fasm` CLI, evidence packet, Agent Skill | ✅ |
| [Context7](context7.md) [![⭐](https://img.shields.io/github/stars/upstash/context7?style=social)](https://github.com/upstash/context7) | Up-to-date docs for AI agents | Remote MCP, `@upstash/context7-mcp`, `ctx7` CLI + Skill | ✅ |


---

## Criteria Reminder

To qualify for this category, a service must:

1. Return **LLM-ready content** — not raw HTML or human-formatted SERPs.
2. Use a **ranking model tuned for agent consumption**, not human click-through.
3. Support **structured extraction** or **schema-based output** as a first-class feature.
4. Provide **configurable depth** — surface search, deep extraction, or multi-step research.
5. Have a **machine-to-machine API** as the primary interface.
