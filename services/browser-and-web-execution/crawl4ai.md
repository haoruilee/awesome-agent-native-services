# Crawl4AI

> **"🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper."**

| | |
|---|---|
| **Website** | https://crawl4ai.com |
| **Docs** | https://docs.crawl4ai.com |
| **GitHub** | https://github.com/unclecode/crawl4ai |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social)](https://github.com/unclecode/crawl4ai) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |

---

## Official Website

https://crawl4ai.com

---

## Official Repo

https://github.com/unclecode/crawl4ai — Library, Docker, and **MCP server** for LLM-native crawling

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Python library` + **Docker** + **MCP**

1. Install per [docs](https://docs.crawl4ai.com/) (`pip`, Docker, or cloud deploy).
2. Use the crawler to produce **clean markdown**, **fit markdown**, **JSON extraction**, and **LLM-ready** chunks — designed for RAG and agents.
3. **MCP:** Run the Crawl4AI MCP server (see project README and community guides) so Claude/Cursor can call crawl/scrape tools against your deployment.

---

## Agent Skills

**Status:** ⚠️ No single official `npx skills add unclecode/…` skill pack required by upstream.

```bash
npx clawhub@latest search crawl4ai
```

---

## MCP

**Status:** ✅ MCP server shipped in ecosystem (see repo and *"Crawl4AI MCP Server"* documentation in community/dev posts linked from project).

| Detail | Value |
|---|---|
| **Repo** | https://github.com/unclecode/crawl4ai |
| **Notes** | Often run via Docker; configure transport per MCP host |

---

## What It Does

Crawl4AI is an **open-source web crawler and scraper** built for **LLMs and AI agents**: JavaScript rendering, **LLM-friendly markdown** output, extraction strategies, **anti-bot** hooks, **shadow DOM** handling, and **crash recovery**. Agents use it to turn arbitrary URLs into **context-window-sized**, structured text instead of raw HTML soup.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | GitHub tagline: *"LLM Friendly Web Crawler & Scraper"*; homepage positions **LLM-ready** output — [crawl4ai.com](https://crawl4ai.com), [repo](https://github.com/unclecode/crawl4ai) |
| **Agent-specific primitive** | **Fit markdown** / chunking for LLM context; **schema-guided extraction**; crawler configs tuned for **agent RAG** pipelines |
| **Autonomy-compatible control plane** | Batch/async crawling without human browsing |
| **M2M integration surface** | Python library, CLI, Docker, HTTP service patterns, MCP |
| **Identity / delegation** | Self-hosted: you control keys, proxies, and cookies; no third-party human inbox |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Crawl job** | URL discovery + fetch + render |
| **LLM-ready markdown** | Noise-stripped text for context injection |
| **Extraction strategy** | CSS, LLM, JSON schema, etc. |
| **MCP tools** | Expose crawl/scrape to IDE agents |
| **Anti-bot / stealth hooks** | Configurable for protected sites (policy-dependent) |

---

## Autonomy Model

```
Agent or pipeline enqueues URLs → Crawl4AI fetches/renders
    ↓
Markdown or structured extract returned
    ↓
Downstream LLM/agent consumes compact text
```

---

## Identity and Delegation Model

- **Self-hosted**: OS/network identity is yours; use **proxy** and **cookie** config for delegated site access.
- **API keys** only where you front Crawl4AI with your own gateway.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python | Primary library |
| Docker | Recommended for MCP / full browser stack |
| MCP | Model Context Protocol integration |
| HTTP | When deployed as a service |

---

## Human-in-the-Loop Support

Humans tune configs and review crawl results; unattended runs are supported.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **wget/curl** | No **JS rendering**, **LLM chunking**, or **agent-oriented extraction** |
| **Generic headless scrape** | Not **LLM-native** output and ecosystem (**MCP**, fit markdown) as first-class |

---

## Use Cases

- **RAG ingestion** — Clean markdown from dynamic sites
- **Agent research** — MCP tool for coding agents
- **High-volume crawl** — OSS deploy on your infra
