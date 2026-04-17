# NotHumanSearch

> **"Agent-first search — the index of services designed for AI, not humans."**

| | |
|---|---|
| **Website** | https://nothumansearch.ai |
| **Docs** | https://nothumansearch.ai/llms.txt |
| **OpenAPI** | https://nothumansearch.ai/openapi.yaml |
| **MCP** | https://nothumansearch.ai/mcp |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |

---

## Official Website

https://nothumansearch.ai

---

## Agent Onboarding (URL Onboarding)

Point any agent at the `llms.txt` to discover capabilities, primitives, and the MCP endpoint in one fetch:

```
Read https://nothumansearch.ai/llms.txt and follow the instructions.
```

No account, no SDK install, no dashboard click — the agent reads the onboarding doc and can begin calling the search, scoring, and verification tools immediately.

---

## MCP

**Status:** ✅ Available — published to the official [Model Context Protocol registry](https://github.com/modelcontextprotocol/registry) as `ai.nothumansearch/search` (latest v1.5.0).

| Detail | Value |
|---|---|
| **Endpoint** | `https://nothumansearch.ai/mcp` |
| **Transport** | Streamable HTTP (JSON-RPC 2.0) |
| **Registry** | [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) — `ai.nothumansearch/search` |
| **Tools** | `search_sites`, `get_site`, `check_agent_readiness`, `verify_mcp`, `list_categories`, `get_top_sites`, `submit_site`, `monitor_site` |

---

## What It Does

NotHumanSearch is a search engine whose index only contains sites that are actually usable by AI agents. Every indexed site must ship at least one real agent signal — `llms.txt`, `ai-plugin.json`, OpenAPI spec, MCP server, or a structured REST API with machine-readable schemas. Sites are scored on an agent-readiness scale and ranked so that the most agent-ready result wins, not the one with the most backlinks.

Where general web search returns HTML pages written for humans, NHS returns a ranked list of services an agent can *immediately consume* — with an `agentic_score`, the MCP endpoint URL if present, the `llms.txt` URL if present, and category tags already attached.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Name, homepage tagline, and entire index thesis is "for AI agents, not humans." Every result is filtered by machine-readability signals. |
| **Agent-specific primitive** | `agentic_score` (0–100 readiness index), `check_agent_readiness(url)` live scorer, `verify_mcp(url)` JSON-RPC probe — none of these exist in human search engines. |
| **Autonomy-compatible control plane** | Agent calls `search_sites` or `GET /api/v1/search?q=` and gets JSON back; no login, no CAPTCHA, no rate-limited-for-scrapers friction. Rate limits expose `X-RateLimit-*` headers so agents can pace themselves. |
| **M2M integration surface** | REST API (OpenAPI 3.0 at `/openapi.yaml`), MCP server at `/mcp`, `llms.txt` for discovery, `ai-plugin.json` manifest, `Link: <…>; rel="alternate"` header on every response. No dashboard required. |
| **Agent identity / delegation** | API-key-per-agent (optional); all search and scoring calls are read-only and attributed to the calling key. No user impersonation surface. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`search_sites(query, category?, min_score?, per_page?)`** | Full-text + semantic rank across the agent-native index, sorted by `agentic_score` with text-match tiebreaker |
| **`check_agent_readiness(url)`** | Live probe: fetches `llms.txt`, `ai-plugin.json`, `/openapi.yaml`, robots.txt, structured data — returns a score and the exact signals found/missing |
| **`verify_mcp(url)`** | Real JSON-RPC probe of the candidate MCP endpoint — distinguishes actual MCP servers from sites that merely mention MCP |
| **`get_site(slug)`** | Full metadata for an indexed site including category, tags, score history, agent-signal inventory |
| **`list_categories` / `get_top_sites`** | Category discovery and top-by-score browsing for agents building directories |
| **`submit_site(url)`** | Agent-submittable inclusion endpoint — no human gatekeeper |
| **`monitor_site(url)`** | Weekly recrawl alerts when an indexed site loses an agent signal (e.g., `llms.txt` returns 404) |

---

## Why This Is Different from Generic Web Search

| Alternative | Why It Is Not Sufficient for Agents |
|---|---|
| **Google / Bing Search API** | Indexes HTML for human readers; no filter for agent-readiness; `agentic_score` concept does not exist; results require HTML parsing before LLM use |
| **Exa / Tavily / Jina Reader** | Return LLM-ready *web content*, but the corpus is the whole human web — not curated to sites that expose `llms.txt`, MCP, or structured APIs |
| **Awesome-lists of MCP servers** | Static, human-maintained, not searchable over HTTP, no scoring, no live verification |

NHS is to the agent web what DNS is to the human web — a discovery layer whose sole job is returning *working, agent-usable endpoints*.

---

## Autonomy Model

1. Agent reads `https://nothumansearch.ai/llms.txt` to discover endpoints
2. Agent calls `search_sites(query="vector database")` via MCP or REST
3. NHS returns top N sites with `agentic_score`, `mcp_url`, `llms_url`, `openapi_url`, `tags` already attached
4. Agent picks the highest-scoring result and calls its MCP/API directly — no HTML scrape, no human step

---

## Identity and Delegation Model

- Anonymous access for all search/read tools (rate-limited per-IP)
- Optional API key per agent for higher limits; keys are attributable in logs
- No user-impersonation surface — NHS is a read-only discovery layer

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `GET /api/v1/search`, `/api/v1/check`, `/api/v1/submit`, `/api/v1/monitor/register` — OpenAPI 3.0 |
| MCP | Streamable HTTP transport at `/mcp`; 8 tools; published to MCP registry |
| `llms.txt` | Machine-readable onboarding at `/llms.txt` |
| `ai-plugin.json` | ChatGPT-style plugin manifest |
| Webhook | Per-site change alerts via `/api/v1/monitor/register` |

---

## Human-in-the-Loop Support

None required for search, check, or verify. Site submission is automated; curation rejections (sites without real agent signals) are also automated.

---

## Use Cases

- **Agent discovery** — an agent needs "a service that does X" and finds one with `llms.txt` already published
- **Tool-selection agents** — build dynamic tool catalogs filtered by `agentic_score ≥ 75`
- **MCP-aware routers** — `verify_mcp` before wiring a new MCP server into the agent runtime
- **Agent-readiness audits** — score your own service with `check_agent_readiness(url)` and get a list of missing signals
- **Monitoring** — get alerted when a dependency's agent surface regresses
