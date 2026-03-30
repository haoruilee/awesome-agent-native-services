# Steel

> **"Browser Infrastructure for AI Agents."**

| | |
|---|---|
| **Website** | https://steel.dev |
| **Docs** | https://docs.steel.dev |
| **GitHub** | https://github.com/steel-dev/steel-browser |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/steel-dev/steel-browser?style=social)](https://github.com/steel-dev/steel-browser) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **License** | Apache-2.0 |

---

## Official Website

https://steel.dev

---

## Official Repo

https://github.com/steel-dev/steel-browser — Core browser API and self-hosted Docker image

https://github.com/steel-dev/steel-python — Python SDK

https://github.com/steel-dev/steel-sdk — TypeScript / Node SDK

https://github.com/steel-dev/steel-mcp-server — MCP server for Steel-controlled browsers

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / REST` + `MCP (stdio)` + Puppeteer / Playwright / Selenium `connect`

```bash
pip install steel-sdk   # PyPI package name: steel-sdk
```

```python
from steel import Steel
client = Steel()
session = client.sessions.create()
# Connect Playwright/Puppeteer/Selenium to session.websocket_url (see docs)
```

**MCP:** Add the [steel-mcp-server](https://github.com/steel-dev/steel-mcp-server) to your MCP config — supports Steel Cloud or local/self-hosted sessions.

**TypeScript:** `npm install steel-sdk` — see [docs](https://docs.steel.dev) and [steel-cookbook](https://github.com/steel-dev/steel-cookbook) for agent starters (browser-use, Magnitude, computer-use, etc.).

---

## Agent Skills

**Status:** ⚠️ No single official `npx skills add steel-dev/skills` registry entry yet — use cookbooks and MCP.

```bash
npx clawhub@latest search steel browser
```

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Repo** | https://github.com/steel-dev/steel-mcp-server |
| **Transport** | stdio (typical) |
| **Modes** | Steel Cloud or local / self-hosted Steel |
| **Compatible Clients** | Claude Desktop, Cursor, Codex, Windsurf, any MCP host |

---

## What It Does

Steel provides **cloud (or self-hosted) browser sessions** exposed through a **Sessions API** so AI agents can automate the web without running infrastructure. Agents create isolated sessions (cookies, storage, and fingerprint per session), connect via **Puppeteer, Playwright, or Selenium** with a one-line `connect` change from local `launch`, and tear down when finished. The product emphasizes **sub-second session start**, **long-running sessions** (up to 24h on cloud per marketing), **CAPTCHA handling**, **proxy and fingerprint controls**, **session viewer** for debugging, and **cookie / storage injection** so agents resume authenticated flows.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage headline: *"Browser Infrastructure for AI Agents"*; hero copy: *"open source browser API that lets you control fleets of browsers in the cloud"* — [steel.dev](https://steel.dev) |
| **Agent-specific primitive** | **Session-scoped remote browser** with programmatic lifecycle, CDP-style connect URLs, and **context injection** (cookies/local storage) for autonomous auth continuity — not a human-driven browser farm |
| **Autonomy-compatible control plane** | Agents create/use/destroy sessions via API/SDK; CAPTCHA and anti-bot tooling run without a human in the loop per action |
| **M2M integration surface** | Python SDK, Node SDK, Sessions API, Puppeteer/Playwright/Selenium connect, **steel-mcp-server** |
| **Identity / delegation** | **Per-session isolation**; API keys scope access to the Steel account; session viewer and logs support audit of agent web trajectories |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Session** | Isolated browser instance with its own storage, fingerprint, and connect endpoint |
| **Sessions API** | Create, list, and manage browser sessions programmatically |
| **Automation connect** | `puppeteer.connect` / Playwright CDP / Selenium remote against session endpoint |
| **Context injection** | Save and inject cookies / local storage for authenticated continuation |
| **CAPTCHA & anti-bot** | Built-in solving and fingerprint/proxy controls marketed for agent automation |
| **Session viewer** | Live or recorded session inspection for debugging agent behavior |
| **MCP server** | Tools for LLM clients to drive Steel-backed browsers |

---

## Autonomy Model

```
Agent obtains API key → Steel().sessions.create()
    ↓
Agent connects Playwright/Puppeteer to session WebSocket URL
    ↓
Agent navigates, submits forms, extracts DOM — optional CAPTCHA/proxy handled by platform
    ↓
Agent saves session context or destroys session when task completes
```

---

## Identity and Delegation Model

- **Session boundary** — Each session is a separate browser context; agents should not share sessions across untrusted tenants.
- **API credentials** — Organization/project API keys gate who can spawn sessions; rotate keys for compromised agents.
- **Human sign-in flows** — "Auto sign-in" features delegate authenticated site access to the platform; operators must policy which sites agents may access.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST / Sessions API | https://docs.steel.dev |
| Python | `pip install steel-sdk` |
| Node.js | `npm install steel-sdk` |
| Puppeteer / Playwright / Selenium | Connect to remote session |
| MCP | `steel-dev/steel-mcp-server` |

---

## Human-in-the-Loop Support

Operators use the **session viewer** and logs for debugging; the agent loop itself is API-driven. No built-in human approval gate for each navigation step — enforce policy via keys, allowlists, and downstream agent frameworks.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Self-managed headless Chrome on one VM** | No fleet API, no per-session isolation at scale, no agent-oriented CAPTCHA/session-injection product surface |
| **General remote browser (Browserless generic tier)** | Steel positions explicitly as **browser infrastructure for AI agents** with MCP and agent cookbook integrations as first-class |

---

## Use Cases

- **Web agents** — Shopping, travel, operations bots that need durable sessions and anti-bot resilience
- **Computer-use models** — Pair with computer-use stacks via documented cookbooks
- **Training / scraping at scale** — Fleet of isolated contexts with observability
