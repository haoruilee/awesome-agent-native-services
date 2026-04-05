# Browser Use Cloud

> **"State-of-the-art AI browser automation with stealth browsers, CAPTCHA solving, residential proxies, and managed infrastructure."**

| | |
|---|---|
| **Website** | https://browser-use.com |
| **Docs** | https://docs.cloud.browser-use.com |
| **GitHub** | https://github.com/browser-use/browser-use |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/browser-use/browser-use?style=social)](https://github.com/browser-use/browser-use) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |

---

## Official Website

https://browser-use.com

---

## Official Repo

https://github.com/browser-use/browser-use — Open-source Browser Use framework; **Browser Use Cloud** is the hosted API/SDK layer documented at [docs.cloud.browser-use.com](https://docs.cloud.browser-use.com/introduction)

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK` + **hosted MCP (HTTP)** + **Agent** or **raw CDP browser** modes

1. Create an API key at [cloud.browser-use.com/settings](https://cloud.browser-use.com/settings?tab=api-keys&new=1) (`bu_…` prefix).
2. Install SDK:

```bash
pip install browser-use-sdk
# or: npm install browser-use-sdk
```

3. **Agent task:**

```python
import asyncio
from browser_use_sdk.v3 import AsyncBrowserUse

async def main():
    client = AsyncBrowserUse()
    result = await client.run("List the top 20 posts on Hacker News today with their points")
    print(result.output)

asyncio.run(main())
```

See [Quick start](https://docs.cloud.browser-use.com/introduction).

4. **MCP (cloud):** Configure your MCP client with the hosted endpoint and `x-browser-use-api-key` header — see [Browser Use MCP docs](https://docs.browser-use.com/cloud/guides/mcp-server) (`https://api.browser-use.com/v3/mcp`).

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add browser-use/…` skill pack documented as canonical.

```bash
npx clawhub@latest search browser-use
```

---

## MCP

**Status:** ✅ Hosted MCP server (HTTP)

| Detail | Value |
|---|---|
| **Endpoint** | `https://api.browser-use.com/v3/mcp` (see docs) |
| **Auth** | `x-browser-use-api-key` header |
| **Compatible Clients** | Claude Code, Claude Desktop, Cursor, Windsurf |

---

## What It Does

Browser Use Cloud provides **managed stealth browsers**, **CAPTCHA solving**, **residential proxies**, and two modes: **Agent** (`run()` / `sessions.create()` with NL tasks) and **Browser** (`browsers.create()` with **CDP** control). It targets agents and automation running where local browsers are unavailable (serverless, CI). The **hosted MCP** exposes session/task tools so coding agents drive cloud browsers without custom glue.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Cloud docs headline: *"State-of-the-art AI browser automation"* for managed agent/browser workloads — [introduction](https://docs.cloud.browser-use.com/introduction) |
| **Agent-specific primitive** | **`run()` NL task** vs **`browsers.create()` CDP** split; **sessions** with keep-alive; **browser profiles** for authenticated state — [Agent vs Browser table](https://docs.cloud.browser-use.com/introduction) |
| **Autonomy-compatible control plane** | Tasks and sessions run without per-step human clicks; MCP tools for `run_session`, `send_task`, `stop_session`, etc. |
| **M2M integration surface** | Python/Node `browser-use-sdk`, REST API (`api.browser-use.com`), hosted MCP |
| **Identity / delegation** | API keys; **profile_id** for persisted auth context; workspace-scoped cloud resources |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent run** | Natural-language web task on managed infrastructure |
| **Session** | Durable session with follow-up tasks (`send_task`) |
| **Browser (CDP)** | Raw browser endpoint for non-NL automation |
| **Profile** | Authenticated browser state reuse |
| **MCP tools** | Session lifecycle and task control for MCP hosts |

---

## Autonomy Model

```
Agent sets BROWSER_USE_API_KEY → AsyncBrowserUse().run(prompt) or sessions.create()
    ↓
Cloud provisions stealth browser + proxy/CAPTCHA handling as configured
    ↓
Structured output / CDP control returned to agent
    ↓
Optional MCP: same flows from IDE without custom SDK wiring
```

---

## Identity and Delegation Model

- **API key** authenticates the developer account.
- **Profiles** isolate authenticated site state per automation line.
- **Workspace** metadata (where applicable) scopes team resources.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python | `browser-use-sdk` v3 |
| Node.js | `browser-use-sdk` v3 |
| REST | `https://api.browser-use.com/api/v3` (see API reference in docs) |
| MCP | HTTPS + API key header |

---

## Human-in-the-Loop Support

Live session URLs and message history endpoints support debugging; core runs are API-driven.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Local Playwright only** | No bundled **stealth + CAPTCHA + residential proxy** cloud with **NL agent** and **hosted MCP** |
| **Generic remote browser** | No **first-class `run()` task** + **profile** primitives marketed for **AI agents** |

---

## Use Cases

- **Serverless agents** — Browser automation from Lambda/edge without local Chrome
- **IDE-driven QA** — MCP tools for Cursor/Claude to drive real sessions
- **Authenticated flows** — Profile-backed repeat logins
