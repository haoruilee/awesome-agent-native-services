# Tavily

> **"Connect your agent to the web."**

| | |
|---|---|
| **Website** | https://tavily.com |
| **Docs** | https://docs.tavily.com |
| **GitHub** | https://github.com/tavily-ai/tavily-python |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |
| **Funding** | $25M |

---

## What It Does

Tavily is a web intelligence API built specifically for AI agents and RAG pipelines. Unlike general search APIs that return links for a human to click, Tavily returns **ranked, pre-processed content** ready for direct injection into an LLM's context window. It provides multiple specialized endpoints covering search, extraction, crawling, site mapping, and multi-step research.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Connect your agent to the web"*; explicitly built for AI agents and RAG, not for human search interfaces |
| **Agent-specific primitive** | AI-optimized ranked sources with content snippets (not SERP links); configurable search depth; multi-step research with source synthesis |
| **Autonomy-compatible control plane** | Agents call the API and receive structured, LLM-ready data; no postprocessing required |
| **M2M integration surface** | REST API, Python SDK, LangChain/LlamaIndex/CrewAI native integrations, MCP |
| **Identity / delegation** | API key authentication; per-tier rate limits |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Search** | Agent-friendly web search returning ranked snippets + optional answers and raw content |
| **Extract** | Clean content extraction from specified URLs in markdown or text |
| **Crawl** | Combined map + extract for site-scale operations |
| **Map** | Structured URL graph of a website with configurable depth |
| **Research** | Multi-step research with automatic synthesis and source attribution |

---

## Search Depth Options

| Depth | Speed | Use Case |
|---|---|---|
| `ultra-fast` | Fastest | Quick fact-checking |
| `fast` | Fast | Simple queries |
| `basic` | Standard | General research |
| `advanced` | Slower | Deep research; returns up to 3 chunks per source |

---

## Output Format

Every endpoint returns data tuned for LLM consumption:

```json
{
  "results": [
    {
      "title": "...",
      "url": "...",
      "content": "...",   // Clean text, not HTML
      "score": 0.92,      // Relevance score for agent ranking
      "raw_content": "..."  // Optional full content
    }
  ],
  "answer": "...",        // Optional synthesized answer
  "follow_up_questions": [...]  // Optional for multi-step research
}
```

---

## Autonomy Model

1. Agent calls `tavily.search(query, search_depth="advanced")`
2. Tavily retrieves, ranks, and extracts content from relevant web pages
3. Returns structured, LLM-ready data
4. Agent injects results directly into context window or uses them as tool call results

No human selects which sources to read. No HTML parsing required. Content is ready for LLM consumption.

---

## Identity and Delegation Model

- API key authentication per integration
- Rate limits: 100 RPM (development) / 1,000 RPM (production)
- Credit-based pricing: basic/fast = 1 credit; advanced = 2 credits

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Base URL: `https://api.tavily.com` |
| Python SDK | `tavily-python` package |
| LangChain | `TavilySearchResults` tool |
| LlamaIndex | Native tool integration |
| CrewAI | Native tool integration |
| MCP | Model Context Protocol server |

---

## Human-in-the-Loop Support

None required. Agents call the search API and use results directly. Humans can review agent research output post-hoc.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Google Custom Search API** | Returns SERP-formatted results for human display; snippets are truncated and require postprocessing; no content extraction |
| **Bing Search API** | Same as Google — designed for human SERP rendering |
| **SerpAPI** | Scrapes SERP data for human-style display; output is not LLM-optimized |
| **Direct web scraping** | Agent must handle JavaScript rendering, encoding, pagination, rate limiting — all solved by Tavily |

---

## Use Cases

- **Research agents** — multi-step web research with automatic source synthesis
- **RAG pipeline augmentation** — real-time web content to supplement vector database retrieval
- **Competitive intelligence** — agent monitors competitor pricing, product updates, job postings
- **News monitoring** — agent tracks developments on specific topics with recency filtering
- **Fact verification** — agent checks claims against current web sources with domain filtering
