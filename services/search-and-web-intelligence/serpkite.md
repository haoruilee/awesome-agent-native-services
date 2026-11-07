# SerpKite

> **"The Google SERP API built for AI agents"**

| | |
|---|---|
| **Website** | https://serpkite.com |
| **Docs** | https://serpkite.com/docs/mcp · https://serpkite.com/llms.txt · https://serpkite.com/openapi/serp-api.yaml |
| **GitHub** | https://github.com/serpkite/serpkite-js (TypeScript SDK, MIT; also Python/Go SDK repos) |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/serpkite/serpkite-js?style=social)](https://github.com/serpkite/serpkite-js) |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |
| **License** | MIT (official SDKs); hosted API is a commercial service |
| **Verified at** | 2026-11-07 |
| **Latest-month signal** | Homepage tagline "The Google SERP API built for AI agents" HTTP 200. `https://serpkite.com/llms.txt` HTTP 200. Remote MCP `https://api.serpkite.com/v1/mcp` answered HTTP 405 on bare GET (expected for Streamable HTTP POST). Docs list 23 MCP tools with OAuth or Bearer auth |

---

## Official Website

https://serpkite.com

SerpKite is a search and web-content API aimed at AI agents: Google verticals (search, news, maps, shopping, scholar, patents, …), multi-engine fallback, webpage-to-Markdown, cited answers, crawl/research jobs, and a remote MCP server — with Markdown/compact JSON sized for context windows.

---

## Official Repo

https://github.com/serpkite/serpkite-js

Official TypeScript SDK (`npm install serpkite`, MIT). Companion SDKs: https://github.com/serpkite/serpkite-python · https://github.com/serpkite/serpkite-go · LangChain / Vercel AI SDK packages linked from `llms.txt`.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** Remote MCP + REST/SDKs

Remote MCP (Streamable HTTP; OAuth 2.1 or `Authorization: Bearer skt_live_…`):

```
https://api.serpkite.com/v1/mcp
```

Claude Code:

```bash
claude mcp add --transport http serpkite https://api.serpkite.com/v1/mcp
```

Cursor `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "serpkite": {
      "url": "https://api.serpkite.com/v1/mcp",
      "headers": { "Authorization": "Bearer ${env:SERPKITE_API_KEY}" }
    }
  }
}
```

REST quickstart uses `SERPKITE_API_KEY` against `https://api.serpkite.com/v1/search`. Full agent map: https://serpkite.com/llms.txt · MCP guide: https://serpkite.com/docs/mcp

---

## Agent Skills

**Status:** ⚠️ Not published as an `npx skills add` package

Machine-readable docs are via `llms.txt` / `llms-full.txt` and OpenAPI. Framework packages (LangChain, CrewAI, Vercel AI SDK) expose tools to agents without a separate SKILL.md package as of 2026-11-07.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Endpoint** | `https://api.serpkite.com/v1/mcp` |
| **Transport** | Streamable HTTP (stateless) |
| **Auth** | OAuth 2.1 sign-in, or Bearer API key (`skt_live_…` / OAuth access tokens) |
| **Tools** | 23 tools documented (search, news, maps, place, scholar, patents, shopping, images, videos, autocomplete, chatgpt/gemini/copilot/ai_mode/brave_ai, webpage, answer, extract, crawl(+result), map, research(+result)) |
| **Billing** | Same credit model as REST; failed/empty calls not billed; per-key monthly credit limits recommended for agents |
| **Compatible clients** | Claude connectors, Claude Code, Cursor, VS Code, ChatGPT, generic streamable-HTTP MCP clients |

---

## What It Does

SerpKite turns live search and page content into LLM-ready Markdown or structured JSON. Agents can search Google (and fall back across engines), fetch pages as Markdown, get cited answers, extract schema-shaped JSON, and run async crawl/research jobs. Spend is prepaid credits with per-key caps so a runaway loop stops at a known cost.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: "The Google SERP API built for AI agents"; `llms.txt`: "search and web content APIs for AI agents" — [serpkite.com](https://serpkite.com/) · [llms.txt](https://serpkite.com/llms.txt) |
| **Agent-specific primitive** | Markdown/`format=markdown` and field projection for context windows; MCP tool set returning model-formatted text; cited `answer` / research reports with `[n]` citations |
| **Autonomy-compatible control plane** | After one OAuth/key, agents call tools in a loop; monthly `credit_limit` on keys caps spend without human clicks per search |
| **M2M integration surface** | Remote MCP, REST OpenAPI, official SDKs, LangChain/CrewAI/AI SDK tools |
| **Identity / delegation** | API keys and OAuth connections named per client; per-key credit limits and revoke; usage metadata without logging query text (per privacy docs) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **search / verticals** | Google (and multi-engine) results as JSON or Markdown |
| **webpage / extract / crawl** | Page Markdown, schema extract, async site crawl |
| **answer / research** | Cited short answers and deep research reports |
| **AI assistant probes** | Logged-out ChatGPT/Gemini/Copilot/AI Mode/Brave answers for visibility tracking |
| **MCP tool surface** | Same capabilities as tools for Claude/Cursor/ChatGPT |

---

## Autonomy Model

1. Person connects MCP via OAuth or sets `SERPKITE_API_KEY` (ideally with a monthly credit limit).
2. Agent calls `search` / `webpage` / `answer` / etc. as tools or REST.
3. Agent branches on structured results; polls `crawl_result` / `research_result` for async jobs.
4. When the key hits its limit, calls fail with `key_limit_reached` and stop spending.

---

## Identity and Delegation Model

- Bearer API keys and OAuth app connections are the credentials; OAuth creates a named key for that client.
- Per-key monthly credit limits bound delegated spend.
- No separate KYA wallet; attribution is per account/key in the request log.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | https://api.serpkite.com/v1/mcp |
| REST | https://api.serpkite.com/v1/* |
| OpenAPI | https://serpkite.com/openapi/serp-api.yaml |
| SDKs | `serpkite` (TS/Python/Go), langchain-serpkite, `@serpkite/ai-sdk` |
| llms.txt | https://serpkite.com/llms.txt |

---

## Human-in-the-Loop Support

Account/key creation and OAuth approval are human once. Ongoing search/extract/research calls are autonomous within credit limits. Spend-control emails and checkout links can be handed to the human when balance is low.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Google Custom Search JSON API** | Human SERP JSON for apps; shut-down path; not Markdown-first or MCP-native for agents |
| **A generic scraper** | Returns HTML; no agent credit caps, cited-answer tools, or MCP tool contract |
| **Browser automation alone** | Session/UI oriented; SerpKite is a search/content API an agent calls as tools |

---

## Use Cases

- **Agent web lookup** — live Google results as Markdown in one tool call
- **Cited answers** — short answers with `[n]` sources for user-facing replies
- **Site ingest** — map + crawl + extract into a knowledge base
- **AI visibility** — probe ChatGPT/Gemini/AI Mode mentions of a brand
