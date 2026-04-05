# Parallel

> **"The highest accuracy web search for your AI."**

| | |
|---|---|
| **Website** | https://www.parallel.ai |
| **Docs** | https://docs.parallel.ai |
| **GitHub** | https://github.com/parallel-web/search-mcp · https://github.com/parallel-web/task-mcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/parallel-web/search-mcp?style=social)](https://github.com/parallel-web/search-mcp) |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |

---

## Official Website

https://www.parallel.ai

---

## Official Repo

https://github.com/parallel-web/search-mcp — **Search MCP**

https://github.com/parallel-web/task-mcp — **Task MCP**

Additional OSS: [parallel-sdk-python](https://github.com/parallel-web/parallel-sdk-python), [parallel-sdk-typescript](https://github.com/parallel-web/parallel-sdk-typescript), [parallel-web-tools](https://github.com/parallel-web/parallel-web-tools)

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `REST` + **Python/TypeScript SDK** + **MCP**

1. Create an API key at [platform.parallel.ai](https://platform.parallel.ai).
2. **SDK:** `pip install parallel-web` or `npm install parallel-web` — see [Getting started](https://docs.parallel.ai/getting-started/overview).
3. **Products** (from docs/marketing): **Search API** (fast NL web search with excerpts), **Extract** (URL → clean content), **Task API** (deep research with citations and confidence), **FindAll** (entity discovery), **Monitor** (scheduled web change tracking with webhooks), **Chat API** (OpenAI-compatible research chat).
4. **MCP:** Install/configure [search-mcp](https://github.com/parallel-web/search-mcp) and [task-mcp](https://github.com/parallel-web/task-mcp) for IDE agents.

---

## Agent Skills

**Status:** ⚠️ See GitHub [parallel-agent-skills](https://github.com/parallel-web/parallel-agent-skills) for curated agent skill assets.

```bash
npx clawhub@latest search parallel web
```

---

## MCP

**Status:** ✅ Available (official org repos)

| Detail | Value |
|---|---|
| **Search MCP** | https://github.com/parallel-web/search-mcp |
| **Task MCP** | https://github.com/parallel-web/task-mcp |
| **Compatible Clients** | Claude, Cursor, Codex, other MCP hosts |

---

## What It Does

Parallel provides **web intelligence APIs purpose-built for AIs**: high-accuracy **search** with verifiable excerpts, **structured deep research** tasks, **monitoring** with webhooks, and **OpenAI-compatible** chat for research apps. It targets **agent workflows** that need grounded facts, citations, and predictable per-query pricing rather than raw SERP HTML.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"A web API purpose-built for AIs"*; *"Give AIs Search"*; deep research framed for **ChatGPT / agent** workloads — [parallel.ai](https://www.parallel.ai) |
| **Agent-specific primitive** | **Task API** with **citations + calibrated confidence**; **Monitor API** for agent-friendly change feeds; **FindAll** for structured entity tables from NL |
| **Autonomy-compatible control plane** | APIs and MCP run without a human clicking SERPs |
| **M2M integration surface** | REST, official SDKs, MCP servers, n8n/LangChain helpers in org |
| **Identity / delegation** | API keys; org billing; audit-friendly cited outputs |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Search** | NL query → ranked excerpts + URLs |
| **Task** | Multi-hop research → structured answer + basis |
| **Extract** | Single URL → LLM-ready text |
| **FindAll** | NL criteria → tabular entity results |
| **Monitor** | Scheduled query + webhook on change |
| **MCP** | Drop-in tools for coding agents |

---

## Autonomy Model

```
Agent sets PARALLEL_API_KEY → calls Search / Task / Monitor SDK or MCP tool
    ↓
Parallel fetches and cross-checks web evidence
    ↓
Structured JSON + citations returned to agent context
```

---

## Identity and Delegation Model

- **API key** scopes usage per workspace.
- **Webhooks** receive only what you configure for downstream agents.
- **SOC 2** posture referenced on marketing site for enterprise delegation.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | https://docs.parallel.ai |
| Python | `parallel-web` on PyPI |
| TypeScript | `parallel-web` on npm |
| MCP | `parallel-web/search-mcp`, `parallel-web/task-mcp` |

---

## Human-in-the-Loop Support

Playground UIs for humans; production path is API/MCP for agents.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Classic Bing/Google JSON API** | Human SERP snippets, not **citation-first task** primitives |
| **Raw fetch + LLM** | No **managed cross-checking**, **monitor webhooks**, or **FindAll** entity fabric |

---

## Use Cases

- **Sales / recruiting agents** — FindAll + enrichment pipelines
- **Compliance research** — Task API with explicit basis fields
- **Always-fresh agents** — Monitor API feeding tool results
