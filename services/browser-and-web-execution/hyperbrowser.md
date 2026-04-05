# Hyperbrowser

> **"Hyperbrowser - Web Infra for AI Agents."**

| | |
|---|---|
| **Website** | https://www.hyperbrowser.ai |
| **Docs** | https://docs.hyperbrowser.ai |
| **GitHub** | https://github.com/hyperbrowserai/mcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/hyperbrowserai/mcp?style=social)](https://github.com/hyperbrowserai/mcp) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |

---

## Official Website

https://www.hyperbrowser.ai

---

## Official Repo

https://github.com/hyperbrowserai/mcp — Official **MCP server** for Hyperbrowser

Additional OSS: [HyperAgent](https://github.com/hyperbrowserai/HyperAgent), [python-sdk](https://github.com/hyperbrowserai/python-sdk), [node-sdk](https://github.com/hyperbrowserai/node-sdk)

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `REST API` + **SDKs** + **MCP**

1. Sign up at Hyperbrowser and create an API key.
2. **MCP (quick path for coding agents):**

```bash
npx hyperbrowser-mcp <YOUR-HYPERBROWSER-API-KEY>
```

See [hyperbrowserai/mcp](https://github.com/hyperbrowserai/mcp) and [MCP integration docs](https://docs.hyperbrowser.ai/guides/model-context-protocol).

3. **API:** Browser automation endpoints (e.g. browser-use style tasks), **scrape**, **crawl**, **extract structured data**, **search**, **profiles** — see [API reference](https://www.hyperbrowser.ai/docs/api-reference/start-a-browser-use-task) and docs index.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add hyperbrowser/…` skill registry entry documented here.

```bash
npx clawhub@latest search hyperbrowser
```

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Repo** | https://github.com/hyperbrowserai/mcp |
| **Install** | `npx hyperbrowser-mcp <API_KEY>` |
| **Tools (examples)** | `scrape_webpage`, `crawl_webpages`, `extract_structured_data`, `browser_use_agent`, `openai_computer_use_agent`, `claude_computer_use_agent`, profile management |
| **Compatible Clients** | Claude Desktop, Cursor, Windsurf |

---

## What It Does

Hyperbrowser is **web infrastructure for AI agents**: managed browsers, **scraping/crawling**, **structured extraction**, and **multi-agent backends** (browser-use, OpenAI CUA, Claude computer-use) behind one API. **HyperAgent** is the platform’s agent SDK. The **MCP server** exposes these capabilities directly to LLM clients so agents can research, extract, and automate the web without custom middleware.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Site title and brand: *"Web Infra for AI Agents"* — [hyperbrowser.ai](https://www.hyperbrowser.ai) |
| **Agent-specific primitive** | **MCP tools** that wrap **browser_use_agent** / **computer use** runs; **managed profiles** for persistent agent browser state; **HyperAgent** as first-class SDK |
| **Autonomy-compatible control plane** | API/MCP-driven tasks without per-click human operation |
| **M2M integration surface** | REST API, Python/Node SDKs, MCP, LangChain/LlamaIndex examples in org repos |
| **Identity / delegation** | API keys; **create_profile** / **list_profiles** tools for session/auth scoping |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Browser-use task** | NL or configured task on managed browser |
| **Scrape / crawl / extract** | LLM-oriented web data pipelines |
| **Computer-use backends** | OpenAI / Anthropic CUA integration |
| **Profile** | Persistent browser identity/state |
| **MCP toolpack** | Direct agent access from IDEs |

---

## Autonomy Model

```
Agent configures MCP or SDK with API key
    ↓
Invoke scrape, crawl, browser agent, or CUA tool
    ↓
Hyperbrowser runs managed browser + proxies/infra as documented
    ↓
Structured or narrative result returned to agent
```

---

## Identity and Delegation Model

- **API key** gates all cloud resources.
- **Profiles** isolate cookies/storage per automation line.
- **Org/team** billing and keys (per product console).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | `https://api.hyperbrowser.ai` (see docs) |
| MCP | `hyperbrowserai/mcp` |
| Python | https://github.com/hyperbrowserai/python-sdk |
| Node.js | https://github.com/hyperbrowserai/node-sdk |

---

## Human-in-the-Loop Support

Dashboard/debug flows for operators; MCP/API paths are autonomous.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Self-hosted Playwright only** | No single **MCP-first** tool surface bundling **CUA + browser-use + profiles** |
| **Generic scraping API** | Not positioned as **infrastructure for AI agents** with **computer-use** engines |

---

## Use Cases

- **Research agents** — Crawl + extract with citations-friendly text
- **Coding agents (MCP)** — One config line to add web automation tools
- **E-commerce / ops** — Profile-backed authenticated scraping
