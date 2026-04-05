# Scrapybara

> **"A COMPUTER FOR YOUR AI."**

| | |
|---|---|
| **Website** | https://scrapybara.com |
| **Docs** | https://docs.scrapybara.com |
| **GitHub** | https://github.com/Scrapybara/scrapybara-python · https://github.com/Scrapybara/scrapybara-ts |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/Scrapybara/scrapybara-python?style=social)](https://github.com/Scrapybara/scrapybara-python) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |

---

## Official Website

https://scrapybara.com

---

## Official Repo

https://github.com/Scrapybara/scrapybara-python

https://github.com/Scrapybara/scrapybara-ts

https://github.com/Scrapybara/scrapybara-mcp — MCP integration

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Python/TypeScript SDK` + **Act SDK** + **MCP**

1. Sign up and install:

```bash
pip install scrapybara
# or: npm install scrapybara
```

2. **Act SDK** — unified tools for computer-use models:

```python
from scrapybara import Scrapybara
from scrapybara.openai import OpenAI
from scrapybara.tools import ComputerTool, BashTool, EditTool

client = Scrapybara()
instance = client.start_ubuntu()
response = client.act(
    tools=[ComputerTool(instance), BashTool(instance), EditTool(instance)],
    model=OpenAI(),
    system="You are a webscraping agent",
    prompt="Scrape all YC W25 companies",
)
```

See [Act SDK](https://docs.scrapybara.com/act-sdk) and [quickstart](https://docs.scrapybara.com/quickstart).

3. **Instance types:** **Ubuntu**, **Browser** (Chromium), **Windows** — [instances](https://docs.scrapybara.com/ubuntu).
4. **MCP:** [scrapybara-mcp](https://github.com/Scrapybara/scrapybara-mcp) for IDE agents.

---

## Agent Skills

**Status:** ⚠️ No official ClawHub skill pack documented as canonical.

```bash
npx clawhub@latest search scrapybara
```

---

## MCP

**Status:** ✅ Community/org MCP repo

| Detail | Value |
|---|---|
| **Repo** | https://github.com/Scrapybara/scrapybara-mcp |
| **Compatible Clients** | Claude, Cursor, other MCP hosts |

---

## What It Does

Scrapybara hosts **remote desktops for computer-use agents** (OpenAI CUA and similar): spin up **Ubuntu**, **browser-only**, or **Windows** VMs in milliseconds, stream the desktop, run **bash**, **file edits**, and **browser automation** via Playwright. It supports **authenticated browser state** (save/load), **pause/resume**, and **hundreds of concurrent instances** for parallel agent workloads.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Hero: *"Scrapybara hosts remote desktop instances for computer use agents like CUA"* — [scrapybara.com](https://scrapybara.com) |
| **Agent-specific primitive** | **Act SDK** with **ComputerTool / BashTool / EditTool** bound to a **remote instance** — not generic VMs marketed to humans |
| **Autonomy-compatible control plane** | Agents drive instances via API without a human at the keyboard |
| **M2M integration surface** | Python/TS SDKs, REST, MCP |
| **Identity / delegation** | API keys; **session persistence** and **auth profiles** for delegated web access |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Instance** | Ubuntu / Browser / Windows desktop |
| **Act** | Multi-tool loop with computer-use models |
| **ComputerTool** | Screen/action bridge for CUA-style models |
| **BashTool / EditTool** | Shell and filesystem on the instance |
| **Stream** | Interactive monitoring / handoff |
| **MCP** | IDE-facing tool surface |

---

## Autonomy Model

```
Agent obtains API key → Scrapybara().start_ubuntu() or start_browser()
    ↓
client.act(...) runs tool loop on remote desktop
    ↓
Structured messages / artifacts returned; instance pause or teardown
```

---

## Identity and Delegation Model

- **API key** controls org quota and concurrency.
- **Authenticated profiles** isolate site login state per automation.
- **Credits** meter agent steps (see pricing on site).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python | `scrapybara` on PyPI |
| TypeScript | `scrapybara` on npm |
| REST | Per docs |
| MCP | `scrapybara-mcp` repo |

---

## Human-in-the-Loop Support

**Interactive stream** allows human monitoring or takeover during a run.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw EC2** | No **Act SDK**, **computer tool** bindings, or **CUA**-oriented product surface |
| **Browser-only SaaS** | No full **Ubuntu/Windows** desktop for non-web computer use |

---

## Use Cases

- **CUA evals** — Parallel desktops for benchmarking
- **E2E testing bots** — Real UI in cloud desktops
- **Research agents** — Browser + bash in one instance
