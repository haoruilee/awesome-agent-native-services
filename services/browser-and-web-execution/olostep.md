# Olostep

> **"Transform websites into clean, LLM-ready data."**

| | |
|---|---|
| **Website** | https://www.olostep.com |
| **Docs** | https://docs.olostep.com |
| **llms.txt** | https://www.olostep.com/llms.txt |
| **GitHub** | https://github.com/olostep/olostep-mcp-server |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/olostep/olostep-mcp-server?style=social)](https://github.com/olostep/olostep-mcp-server) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |

---

## Official Website

https://www.olostep.com

---

## Official Repo

https://github.com/olostep/olostep-mcp-server — official MCP server wrapping Olostep web data APIs

---

## How to Use (Agent Onboarding)

**REST API — get an API key from the dashboard, then call scrape / search / crawl / batch endpoints.**

```bash
# See https://docs.olostep.com/get-started/welcome
# Set OLOSTEP_API_KEY and call HTTPS endpoints (scrapes, searches, maps, crawls, batches)
```

**MCP (recommended for MCP clients):**

```bash
npx -y olostep-mcp
```

Remote endpoint (per docs): `https://mcp.olostep.com/mcp` with API key.

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official `npx skills add org/repo` bundle located; use [llms.txt](https://www.olostep.com/llms.txt) and docs for machine-readable discovery.

```bash
npx clawhub@latest search olostep
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/olostep/olostep-mcp-server |
| **Docs** | https://docs.olostep.com/integrations/mcp-server |
| **Remote MCP** | `https://mcp.olostep.com/mcp` (per Olostep docs) |
| **Transport** | stdio (`npx olostep-mcp`) / remote HTTP |
| **Compatible Clients** | Claude Desktop, Cursor, Windsurf, Claude Code |

---

## What It Does

Olostep is a **web data API** that turns URLs into **Markdown, HTML, JSON, or plain text** with high reliability, handling proxies, bot mitigation, and JavaScript rendering. It provides **search** (e.g. structured SERP-style results), **crawl**, **map** (URL discovery), **batch** scraping at scale, and an **Agents** API for autonomous research workflows. It is explicitly positioned as infrastructure for **AI and research agents** (see [llms.txt](https://www.olostep.com/llms.txt)).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | [llms.txt](https://www.olostep.com/llms.txt): *"developers and AI agents can focus on building"*; dedicated *"Deep Research & AI Agents"* section; blog *"Olostep Web Data API for AI Agents"* |
| **Agent-specific primitive** | **LLM-ready markdown/JSON** as default contract; **batch** and **crawl** primitives for agent-scale web ingestion; optional **Agents API** for scheduled autonomous research pipelines |
| **Autonomy-compatible control plane** | API-driven; no human browser session per request |
| **M2M integration surface** | HTTPS REST API, official MCP server, Docker image |
| **Identity / delegation** | API key per account; usage and quotas attributable per key |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Scrape** | Single URL → clean Markdown / HTML / JSON / text |
| **Search** | Query → structured links and snippets (Google/Bing/Brave per docs) |
| **Map** | Discover URLs on a site (sitemap + crawl) |
| **Crawl** | Recursive crawl from a seed URL |
| **Batch** | High-throughput parallel URL processing |
| **Agents API** | Managed multi-step research agents (availability per Olostep product tier) |

---

## Autonomy Model

1. Agent obtains API key.
2. Agent issues scrape/search/crawl/batch calls (or invokes MCP tools).
3. Olostep returns structured, context-window-friendly content.
4. Agent continues reasoning loop without operating a local browser.

---

## Identity and Delegation Model

- API key authentication.
- Rate limits and billing tied to key / workspace.
- No end-user OAuth in the core scrape API (contrast with user-delegated SaaS APIs).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | https://docs.olostep.com |
| MCP | `npx -y olostep-mcp`, remote `https://mcp.olostep.com/mcp` |
| Docker | `olostep/mcp-server` image (per docs) |

---

## Human-in-the-Loop Support

- Optional human approval for enterprise or gated features (e.g. Agents API) per Olostep sales/policy.
- Standard API usage is fully automated.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw curl + HTML** | Agents must handle anti-bot, JS rendering, and cleanup — Olostep centralizes that |
| **Human-oriented SERP UIs** | Not machine contracts; Olostep returns API-first structured results |

---

## Use Cases

- **Research agents** — search → follow URLs → extract markdown for synthesis.
- **Price / catalog monitoring** — batch and map endpoints for large URL sets.
- **Vertical search products** — continuous refresh of structured web data.
