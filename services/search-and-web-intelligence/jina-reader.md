# Jina Reader

> **"Convert a URL to LLM-friendly input, by simply adding `r.jina.ai` in front."**

| | |
|---|---|
| **Website** | https://jina.ai/reader |
| **Docs** | https://jina.ai/reader (API parameters and examples) |
| **GitHub** | https://github.com/jina-ai/reader |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/jina-ai/reader?style=social)](https://github.com/jina-ai/reader) |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |

---

## Official Website

https://jina.ai/reader

---

## Official Repo

https://github.com/jina-ai/reader — Open-source Reader; **hosted API** at `https://r.jina.ai` and `https://s.jina.ai`

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `HTTP GET/POST` + **MCP** (`mcp.jina.ai`)

1. **Reader (URL → markdown/text):**

```bash
curl "https://r.jina.ai/https://www.example.com"
```

2. **Search (query → top results as LLM-friendly text):**

```bash
curl "https://s.jina.ai/?q=your+encoded+query"
```

3. Add API key headers for higher rate limits (see pricing table on [reader page](https://jina.ai/reader)).
4. **MCP:** Add `mcp.jina.ai` as an MCP server in Claude/Cursor per on-page instructions.

Advanced: **JSON response**, **token budget**, **ReaderLM-v2**, **image captions**, **PDF** URLs, **proxy** headers — all documented on the Reader page.

---

## Agent Skills

**Status:** ⚠️ No official ClawHub skill pack required; integration is URL + MCP.

```bash
npx clawhub@latest search jina reader
```

---

## MCP

**Status:** ✅ Documented on Reader page — `mcp.jina.ai`

| Detail | Value |
|---|---|
| **Compatible Clients** | Claude, Cursor, other MCP hosts |

---

## What It Does

Reader turns **URLs and search queries** into **clean, LLM-friendly text**: it renders pages (including dynamic content), strips boilerplate, optionally **captions images** for VLMs, reads **PDFs**, and returns **JSON** shapes agents can parse. **Search mode** returns multiple results with page bodies, not just blue links — optimized for **grounding** and **RAG**.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Reader page: *"ensuring high-quality input for your agent and RAG systems"*; *"Feeding web information into LLMs"* — [jina.ai/reader](https://jina.ai/reader) |
| **Agent-specific primitive** | **URL-prefix Reader** (`r.jina.ai/…`) and **search-prefix** (`s.jina.ai`) as machine-oriented affordances; **token budget** and **LLM-oriented** markdown |
| **Autonomy-compatible control plane** | Agents call HTTP/MCP without a human opening a browser |
| **M2M integration surface** | HTTPS API, MCP, open-source self-host option |
| **Identity / delegation** | API keys; optional **forward cookie** / **proxy** headers for delegated access (see docs; caching rules apply) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Read URL** | Single-page extraction to markdown/JSON |
| **Search** | SERP → multi-document LLM-ready bundle |
| **ReaderLM-v2** | SLM-powered HTML→markdown/JSON |
| **Image captions** | Alt text for downstream VLMs |
| **PDF input** | Direct document ingestion |

---

## Autonomy Model

```
Agent forms r.jina.ai/{url} or s.jina.ai?q=… (+ optional headers)
    ↓
Jina renders and normalizes content
    ↓
Markdown/JSON returned into agent context or tool output
```

---

## Identity and Delegation Model

- **API key** controls rate limits and billing.
- **Per-key** usage dashboards on Jina.
- **Do not cache** / **do not track** headers for sensitive fetches (see FAQ).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTPS | `https://r.jina.ai`, `https://s.jina.ai` |
| MCP | `mcp.jina.ai` |
| Open source | Self-host from GitHub |

---

## Human-in-the-Loop Support

Interactive demo on site; production use is API-only.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw fetch** | Returns cluttered HTML; poor for **token budgets** |
| **Traditional SERP API** | Snippets only — not full **LLM-readable** documents |

---

## Use Cases

- **Tool-calling web browse** — Cheap read tool for agents
- **RAG ingestion** — Normalize arbitrary URLs
- **Search grounding** — `s.jina.ai` multi-hop pipelines
