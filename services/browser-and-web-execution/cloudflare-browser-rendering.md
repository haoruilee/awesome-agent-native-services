# Cloudflare Browser Rendering

> **Headless browsers for AI agents (Cloudflare Workers).**

| | |
|---|---|
| **Website** | https://workers.cloudflare.com/product/browser-rendering/ |
| **Docs** | https://developers.cloudflare.com/browser-rendering/ |
| **AI guide** | https://developers.cloudflare.com/browser-rendering/how-to/ai/ |
| **GitHub** | https://github.com/cloudflare/workers-sdk |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/cloudflare/workers-sdk?style=social)](https://github.com/cloudflare/workers-sdk) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |

---

## Official Website

https://workers.cloudflare.com/product/browser-rendering/

---

## Official Repo

https://github.com/cloudflare/workers-sdk — Cloudflare Workers platform SDKs (Browser Rendering is used via Workers bindings and APIs)

---

## How to Use (Agent Onboarding)

**Workers Bindings or REST — run headless Chrome on Cloudflare's network.**

1. Enable Browser Rendering on a Cloudflare account and create a Worker with a **browser binding** per [docs](https://developers.cloudflare.com/browser-rendering/).
2. Control the browser with **Puppeteer** or **Playwright** compatible APIs from the Worker.
3. For LLM control, add the **Playwright MCP** path documented under [Use browser rendering with AI](https://developers.cloudflare.com/browser-rendering/how-to/ai/).

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official `npx skills add cloudflare/...` bundle located for Browser Rendering.

```bash
npx clawhub@latest search cloudflare browser
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Playwright MCP integration documented for AI-driven browser control

| Detail | Value |
|---|---|
| **Docs** | https://developers.cloudflare.com/browser-rendering/how-to/ai/ |
| **Pattern** | Playwright MCP + Browser Rendering (managed headless Chrome) |
| **Compatible Clients** | MCP-capable agents and IDEs |

---

## What It Does

Cloudflare **Browser Rendering** provides **pooled headless Chrome** on Cloudflare's edge. Developers and **AI agents** automate navigation, screenshots, PDFs, markdown extraction, and structured extraction (including AI-assisted JSON from pages). It scales to many concurrent isolated browser instances without agents running local Chrome.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Product page and docs frame **AI agents** as a primary use case; dedicated guide *"Use browser rendering with AI"* ([how-to/ai](https://developers.cloudflare.com/browser-rendering/how-to/ai/)) |
| **Agent-specific primitive** | **Remote headless browser fleet** with **Playwright MCP** path — agents drive real browser sessions without a human-operated desktop |
| **Autonomy-compatible control plane** | API/Worker-driven sessions; policies enforced via Cloudflare account and Worker code |
| **M2M integration surface** | Workers bindings (Puppeteer/Playwright), REST API for common operations, MCP per AI guide |
| **Identity / delegation** | Cloudflare account API tokens / OIDC; audit via Cloudflare logging; per-deployment isolation |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Browser session** | Headless Chrome instance on Cloudflare infrastructure |
| **Puppeteer / Playwright APIs** | Programmatic navigation, clicks, screenshots |
| **Screenshot / PDF / content** | Common automation outputs |
| **AI extraction** | Natural-language or schema-guided structured data from rendered pages (per docs) |
| **Playwright MCP** | LLM tool surface for browser actions |

---

## Autonomy Model

1. Operator deploys a Worker (or REST client) with Browser Rendering enabled.
2. Agent receives MCP tools or calls APIs to open URLs and perform actions.
3. Results (DOM, screenshots, structured JSON) return to the agent loop.
4. Sessions tear down without local browser installs.

---

## Identity and Delegation Model

- Authentication via Cloudflare API tokens or Workers OIDC (on Vercel etc.).
- Isolation per Worker deployment and browser instance.
- Human Cloudflare account owns billing and global policy; agents operate within configured bounds.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Workers + bindings | Puppeteer/Playwright from Worker code |
| REST API | [Browser Rendering API](https://developers.cloudflare.com/api/resources/browser_rendering/) |
| MCP | Playwright MCP per [AI guide](https://developers.cloudflare.com/browser-rendering/how-to/ai/) |

---

## Human-in-the-Loop Support

- Cloudflare account setup and Worker deployment typically involve a human operator once.
- Runtime browsing is automated; sensitive flows can add application-level approval.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Local headless Chrome** | No pooled edge fleet, no Cloudflare scale/isolation — agents must self-host infra |
| **Static HTTP fetch** | Cannot execute JS-heavy sites or drive true browser UX flows |

---

## Use Cases

- **Web agents** — sites without stable APIs; form flows and dynamic content.
- **Structured extraction** — render then parse with LLM-assisted schemas.
- **High concurrency** — many parallel agent sessions without local RAM limits.
