# Notte

> **"Browser infrastructure that lets AI run on the internet at speed."**

| | |
|---|---|
| **Website** | https://www.notte.cc |
| **Docs** | https://docs.notte.cc |
| **GitHub** | https://github.com/nottelabs/notte |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/nottelabs/notte?style=social)](https://github.com/nottelabs/notte) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |

---

## Official Website

https://www.notte.cc

---

## Official Repo

https://github.com/nottelabs/notte — Open-source SDK, framework, and **notte-mcp** package (`packages/notte-mcp`)

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / REST` + remote browser via **CDP** + optional **MCP (SSE)**

1. Create an API key in the [Console](https://console.notte.cc/).
2. Install the SDK:

```bash
pip install notte-sdk
```

3. **Browser session (Playwright over CDP):**

```python
from playwright.sync_api import sync_playwright
from notte_sdk import NotteClient

client = NotteClient()
with client.Session(open_viewer=True) as session:
    cdp_url = session.cdp_url()
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(cdp_url)
        page = browser.contexts[0].pages[0]
        page.goto("https://www.google.com")
```

4. **Web agent (natural-language task on a session):**

```python
from notte_sdk import NotteClient

client = NotteClient()
with client.Session(open_viewer=True) as session:
    agent = client.Agent(session=session, max_steps=5)
    response = agent.run(
        task="Browse on Notte docs and book a demo for me",
        url="https://docs.notte.cc",
    )
    print(response)
```

See [Quickstart](https://docs.notte.cc/quickstart) for scraping with Pydantic-typed extraction.

**MCP:** `pip install notte-mcp` → `export NOTTE_API_KEY=...` → `python -m notte_mcp.server` — then point your MCP client at the server URL (see [Notte MCP blog post](https://www.notte.cc/blog/mcp-server) and [packages/notte-mcp](https://github.com/nottelabs/notte/tree/main/packages/notte-mcp)).

---

## Agent Skills

**Status:** ⚠️ No single official `npx skills add …` registry entry yet — use SDK, Studio, and MCP.

```bash
npx clawhub@latest search notte browser
```

For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Package / path** | PyPI `notte-mcp` · [packages/notte-mcp](https://github.com/nottelabs/notte/tree/main/packages/notte-mcp) |
| **Transport** | SSE (typical local server; see blog for `config.json` example) |
| **Compatible Clients** | Claude Desktop, Cursor, other MCP hosts |

---

## What It Does

Notte is a **unified browser platform for AI**: remote **browser sessions** (CDP for Playwright, Puppeteer, Selenium, browser-use, Stagehand), **web agents** that complete natural-language tasks in those sessions, **serverless browser functions** (deploy automations next to the browser), AI-assisted **scraping** with structured outputs, and **agent-facing auth** — **vaults** (encrypted credentials the LLM never sees), **agent identities** (email/phone for OTP and 2FA), and **session profiles** that persist browser state. The product also offers **Studio** for building and debugging automations and an **Anything API** for custom engineered endpoints from natural-language task descriptions.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage title: *"Notte - Browser Platform for AI"*; hero: *"Browser infrastructure that lets AI run on the internet at speed."*; mission copy: *"sole mission is to be the infrastructure for the agentic internet"* — [notte.cc](https://www.notte.cc) |
| **Agent-specific primitive** | **Vault-mediated credential fill** — the vault intercepts sensitive actions and injects real secrets so the **LLM never sees actual passwords** ([docs](https://docs.notte.cc/concepts/vaults)); **agent identities** (dedicated inbox/SMS for OTP); **browser agents** as first-class task runners on cloud sessions |
| **Autonomy-compatible control plane** | Agents run sessions, agents, scrapes, and functions via API/SDK without per-click human confirmation; optional live viewer/replay for operators |
| **M2M integration surface** | Python/Node `notte-sdk`, Platform API, CDP sessions, **notte-mcp**, integrations with Playwright/Puppeteer/Selenium and agent frameworks |
| **Identity / delegation** | API keys scope the account; **vaults** with scoped access and audit; **agent personas** and **session profiles** model delegated web identity separate from the developer |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Session** | Cloud browser with CDP URL, proxies, anti-detection, captcha solving, optional live view/replay |
| **Agent** | Natural-language web agent bound to a session (`client.Agent`, `run(task=..., url=...)`) |
| **Scrape** | Structured extraction with Pydantic (or similar) response shapes |
| **Function** | Serverless automation colocated with browser infra; schedulable |
| **Vault** | Encrypted credentials; execution path keeps secrets out of LLM context |
| **Identity / profile** | Agent email/phone for verification; persisted browser profiles for auth continuity |
| **MCP** | `notte-mcp` exposes browser control to MCP clients |

---

## Autonomy Model

```
Agent obtains NOTTE_API_KEY → NotteClient()
    ↓
Open Session → receive cdp_url (or attach vault / profile)
    ↓
Either: connect Playwright/Puppeteer over CDP and drive DOM
    Or: client.Agent(...).run(task, url) for NL web task
    Or: client.scrape(...) / invoke deployed function for structured data
    ↓
Session teardown; optional replay for audit
```

---

## Identity and Delegation Model

- **API key** — Authenticates the developer account; rotate if an agent or integration is compromised.
- **Vault** — Delegates site login to the platform; credentials are vault-resolved at execution time, not in the model context ([Vault docs](https://docs.notte.cc/concepts/vaults)).
- **Agent identities & profiles** — Delegate human-style verification (OTP, 2FA) and session state to Notte-managed channels.
- **Audit** — Vault and access patterns are designed for logging and enterprise review (e.g. SOC 2 posture referenced on marketing site).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **Python SDK** | `pip install notte-sdk` — [Quickstart](https://docs.notte.cc/quickstart) |
| **Node SDK** | `npm install notte-sdk` (see docs for current coverage) |
| **CDP** | `session.cdp_url()` for Playwright `connect_over_cdp` |
| **REST / Platform API** | https://docs.notte.cc |
| **MCP** | `notte-mcp` — [blog](https://www.notte.cc/blog/mcp-server) |

---

## Human-in-the-Loop Support

**Live View & Replays** help humans debug agent sessions without driving each action. **Vault** design keeps humans out of the per-field approval loop while protecting secrets. High-stakes policy is enforced via account limits, vault scoping, and operator governance rather than mandatory human clicks per navigation.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw cloud browser (Browserless-style) only** | No first-class **agent vault** that prevents LLM exposure of secrets, no bundled **NL web agents** + **serverless functions** as one agent-oriented product surface |
| **Local Playwright only** | No global edge sessions, anti-bot/proxy product layer, or managed agent identities at scale |
| **Generic secrets manager** | Not bound to browser **FillActions** with automatic vault takeover so credentials never enter the model ([Vault docs](https://docs.notte.cc/concepts/vaults)) |

---

## Use Cases

- **E-commerce / SaaS agents** — Checkout, invoice download, subscription changes with vault-backed auth
- **Research agents** — NL browsing plus structured scrape endpoints
- **MCP coding assistants** — Drive real browsers from Cursor/Claude via `notte-mcp`
- **Anything API** — Production JSON endpoints for repeatable web workflows agents call without one-off prompting
