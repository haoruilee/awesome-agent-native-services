# AgentQL

> **"Make the web AI‑ready."**

| | |
|---|---|
| **Website** | https://agentql.com |
| **Docs** | https://docs.agentql.com |
| **GitHub** | https://github.com/tinyfish-io/agentql |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/tinyfish-io/agentql?style=social)](https://github.com/tinyfish-io/agentql) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |

---

## Official Website

https://agentql.com

---

## Official Repo

https://github.com/tinyfish-io/agentql — Examples and query patterns; **REST API** and **SDKs** are primary integration surfaces

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `REST` + **Python/JS SDK** + **Playwright** + optional **remote browser (CDP)**

1. Sign up at [agentql.com/dev](https://agentql.com/dev) for an API key.
2. **Browserless REST** — query public URLs for structured data without running a local browser ([REST API](https://docs.agentql.com/rest-api/api-reference)).
3. **SDK + Playwright** — install [Python](https://docs.agentql.com/python-sdk/installation) or [JavaScript](https://docs.agentql.com/javascript-sdk/installation) SDK and drive pages with **AgentQL queries** (structured syntax or natural language) instead of brittle XPath/CSS.
4. **Remote browser** — managed sessions with **CDP**, streaming viewer, stealth profiles, proxies — [remote browser docs](https://docs.agentql.com/browser/remote-browser).

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills registry entry documented as canonical.

```bash
npx clawhub@latest search agentql
```

---

## MCP

**Status:** ⚠️ Not documented as a first-party MCP server in this entry — integrate via REST/SDK from your MCP host or community servers if published.

---

## What It Does

AgentQL connects **LLMs and AI agents to the web** through an **AI-assisted query language**: you describe the data shape (or use NL), and AgentQL resolves elements and extracts **JSON** robust to DOM changes (**self-healing**). It supports **authenticated pages**, **PDFs/images**, a **browserless API** for public pages, and **remote Chromium** with CDP for full agent control.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Hero: *"AgentQL connects LLMs and AI agents to the entire web"*; H1: *"Make the web AI‑ready"* — [agentql.com](https://agentql.com) |
| **Agent-specific primitive** | **AgentQL query → JSON** abstraction designed for **LLM grounding** (avoids context-blob HTML); **NL or schema** queries; **self-healing** extraction |
| **Autonomy-compatible control plane** | API/SDK execute without a human in the loop per query |
| **M2M integration surface** | REST API, Python SDK, JavaScript SDK, Playwright integration, remote browser CDP |
| **Identity / delegation** | API keys; remote browser + profiles for authenticated agent sessions |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **AgentQL query** | Declarative or NL extraction spec |
| **Structured JSON result** | Typed output for agent tool returns |
| **Browserless API** | No local browser for public URLs |
| **Remote browser session** | CDP + stealth + proxy |
| **PDF / image extraction** | Non-HTML documents in the same model |

---

## Autonomy Model

```
Agent forms AgentQL query (+ optional URL)
    ↓
REST (browserless) or SDK+Playwright / remote browser
    ↓
AgentQL resolves page structure with AI assistance
    ↓
JSON returned to agent tool pipeline
```

---

## Identity and Delegation Model

- **API key** scopes usage and rate limits.
- **Remote browser profiles** carry auth state for delegated site access.
- Operators should rotate keys if an agent is compromised.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | https://docs.agentql.com/rest-api/api-reference |
| Python | https://docs.agentql.com/python-sdk/installation |
| JavaScript | https://docs.agentql.com/javascript-sdk/installation |
| Browser / CDP | https://docs.agentql.com/browser |

---

## Human-in-the-Loop Support

**Browser extension IDE** and **playground** for humans to refine queries; runtime API is autonomous.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw HTML → LLM** | No **query language** primitive; causes **context bloat** and **hallucination** (AgentQL’s stated problem) |
| **Fixed XPath scrapers** | Break on UI changes; not **self-healing** for agent loops |

---

## Use Cases

- **Structured grounding** — Replace huge HTML dumps with small JSON facts
- **Authenticated portals** — Remote browser + queries behind login
- **Price monitoring / catalogs** — Reusable queries across similar pages
