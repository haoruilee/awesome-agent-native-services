# Firecrawl

> **"Turn any website into LLM-ready data."**

| | |
|---|---|
| **Website** | https://firecrawl.dev |
| **Docs** | https://docs.firecrawl.dev |
| **GitHub** | https://github.com/mendableai/firecrawl |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |

---

## Official Website

https://firecrawl.dev

---

## Official Repo

https://github.com/mendableai/firecrawl

---

## Skills

| Skill | Description |
|---|---|
| **Intent-Driven Extraction (`/agent`)** | Describe what data you need in natural language — no URLs required |
| **Scrape** | Extract clean markdown or structured JSON from a single URL |
| **Crawl** | Recursively crawl an entire site with configurable depth and rules |
| **Extract (Schema)** | Pull structured data from one or many URLs using Pydantic/Zod schemas |
| **Map** | Enumerate all URLs on a website as a structured graph |
| **LLM-Ready Output** | All endpoints return markdown or typed JSON, never raw HTML |

---

## MCP

**Status:** ✅ Available

Firecrawl provides an official MCP server enabling agents to trigger scraping, extraction, and crawling operations directly through the Model Context Protocol.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/mendableai/firecrawl/tree/main/apps/mcp-server |
| **Transport** | stdio |
| **Compatible Clients** | Claude Desktop, Cursor, any MCP-compatible client |

---

## What It Does

Firecrawl is a web extraction API that converts websites into clean, LLM-ready markdown or structured JSON. Its `/agent` endpoint goes further: agents describe *what data they need* in natural language — no URLs required. Firecrawl autonomously searches, navigates, and extracts across multiple sources in parallel, returning structured output directly consumable by an LLM.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The `/agent` endpoint requires no human URL input — agents express intent, not URLs; output format is tuned for LLM context windows, not human reading |
| **Agent-specific primitive** | Intent-driven extraction (agent describes what it wants, not where it is); LLM-ready markdown/JSON output; schema-driven structured extraction |
| **Autonomy-compatible control plane** | Agent describes intent; Firecrawl plans and executes web navigation autonomously; no human is in the loop during extraction |
| **M2M integration surface** | REST API, Python SDK, Node.js SDK, MCP server |
| **Identity / delegation** | API key authentication per integration; dynamic pricing per query complexity |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`/agent` Endpoint** | Intent-driven extraction — agent provides a natural-language prompt, no URLs needed |
| **`/scrape` Endpoint** | Single-URL extraction returning clean markdown or structured JSON |
| **`/crawl` Endpoint** | Recursive site-wide crawl with configurable depth |
| **`/extract` Endpoint** | Schema-driven structured data extraction from one or many URLs |
| **`/map` Endpoint** | Enumerate all URLs on a site as a structured graph |
| **LLM-Ready Output** | All endpoints return markdown or Pydantic/Zod-typed JSON, not raw HTML |

---

## Autonomy Model

**Standard mode (`/scrape`, `/crawl`):** Agent provides URL(s) + optional schema → Firecrawl handles crawling, parsing, and formatting.

**Agent mode (`/agent`):**
1. Agent sends a natural-language prompt: `"Find the pricing tiers and feature lists for Acme SaaS"`
2. Firecrawl autonomously determines which sites to visit, how deep to crawl, and how to extract the information
3. Returns structured, LLM-ready result

No human determines URLs. The agent describes intent; Firecrawl executes the web navigation plan.

---

## Identity and Delegation Model

- API key scoped per integration
- Dynamic credit-based pricing during research preview (query complexity determines cost)
- Model selection (Spark 1 Mini vs Spark 1 Pro) allows cost/accuracy tradeoff per agent use case

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | All endpoints (agent, scrape, crawl, extract, map) |
| Python SDK | `pip install firecrawl-py`; Pydantic schema support |
| Node.js SDK | `npm install @mendable/firecrawl-js`; Zod schema support |
| MCP Server | Model Context Protocol for direct LLM tool use |

---

## Human-in-the-Loop Support

None required. Agents drive all extraction autonomously. Humans can review output post-hoc; no human is in the extraction loop.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **BeautifulSoup** | A Python parsing library; humans write the crawl logic, select URLs, and handle JavaScript rendering separately |
| **Scrapy** | Developer-operated web scraping framework; agents cannot express intent — they must write crawl code |
| **Puppeteer (raw)** | Headless browser library; no LLM-ready output, no intent-driven navigation, no schema extraction |
| **Common Crawl** | A static dataset; not a live, agent-queryable extraction service |

---

## Use Cases

- **Market intelligence** — agent extracts competitor pricing, feature lists, or job postings on demand
- **Research synthesis** — agent describes a research question; Firecrawl retrieves and structures relevant web content
- **Product catalog ingestion** — agent extracts structured product data from retailer pages using a Pydantic schema
- **News monitoring** — agent continuously extracts and structures articles matching a topic description
- **Documentation indexing** — agent crawls and extracts API docs into structured knowledge for RAG pipelines
