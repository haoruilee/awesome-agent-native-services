# Skyvern

> **"AI agents to automate workflows on any website."**

| | |
|---|---|
| **Website** | https://www.skyvern.com |
| **Docs** | https://www.skyvern.com/docs |
| **GitHub** | https://github.com/Skyvern-AI/skyvern |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/Skyvern-AI/skyvern?style=social)](https://github.com/Skyvern-AI/skyvern) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |

---

## Official Website

https://www.skyvern.com

---

## Official Repo

https://github.com/Skyvern-AI/skyvern — Open-source agent + self-host path; **Skyvern Cloud** adds managed API at `https://api.skyvern.com`

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / REST` + optional **MCP**

1. Get an API key from [app.skyvern.com/settings](https://app.skyvern.com/settings) (cloud) or self-host per [self-hosted docs](https://www.skyvern.com/docs/self-hosted/overview).
2. **REST:** `POST https://api.skyvern.com/v1/run/tasks` with `x-api-key` — body includes `prompt` (required), optional `url`, `engine` (`skyvern-2.0`, `openai-cua`, `anthropic-cua`, …), `data_extraction_schema`, `browser_session_id`, webhooks, proxy/geo, TOTP hooks — see [Run a task](https://www.skyvern.com/docs/api-reference/api-reference/agent/run-task).
3. **SDKs:** [Python](https://www.skyvern.com/docs/sdk-reference/overview) and [TypeScript](https://www.skyvern.com/docs/ts-sdk-reference/overview) quickstarts from docs home.
4. **MCP:** Docs advertise MCP-ready integration for coding agents — configure per your MCP host against Skyvern’s documented MCP surface.

Example (conceptual):

```bash
curl -X POST https://api.skyvern.com/v1/run/tasks \
  -H "x-api-key: $SKYVERN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Find the top 3 posts on Hacker News", "url": "https://news.ycombinator.com"}'
```

---

## Agent Skills

**Status:** ⚠️ No single official `npx skills add …` registry entry documented as primary path.

```bash
npx clawhub@latest search skyvern
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Documented as MCP-ready — see [Skyvern docs](https://www.skyvern.com/docs) integrations section.

| Detail | Value |
|---|---|
| **Transport** | Per MCP host configuration |
| **Compatible Clients** | Claude Desktop, Cursor, Windsurf, and other MCP hosts |

---

## What It Does

Skyvern runs **vision-driven browser automation**: an agent describes a goal in natural language; Skyvern drives a real browser, plans actions, and completes multi-step workflows (forms, logins, downloads, structured extraction) without brittle XPath-only scripts. It supports **CAPTCHA handling**, **2FA/TOTP** flows, **geo-targeted proxies**, **persistent browser sessions**, **JSON-schema extraction**, **webhooks**, and **recordings** for audit. **Skyvern Cloud** offers a production API; the core stack is **open source** for self-hosting.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"AI agents to automate workflows on any website"*; docs: *"Automate any browser workflow with AI"* — [skyvern.com](https://www.skyvern.com), [docs](https://www.skyvern.com/docs) |
| **Agent-specific primitive** | **Task run** with `prompt` + optional `engine` (Skyvern agent vs CUA backends), **browser_session_id** for stateful runs, **data_extraction_schema** for agent-consumable structured output — [API reference](https://www.skyvern.com/docs/api-reference/api-reference/agent/run-task) |
| **Autonomy-compatible control plane** | Async task execution with webhooks and dashboards; no per-click human in the core API loop |
| **M2M integration surface** | REST (`api.skyvern.com`), Python SDK, TypeScript SDK, MCP integration |
| **Identity / delegation** | API keys (`x-api-key`); **credential / TOTP** integration for delegated login; **browser_session_id** / **browser_profile_id** for scoped browser identity |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Task run** | NL goal + optional start URL + engine + extraction schema |
| **Browser session** | Persist state across runs (`browser_session_id`) |
| **Workflow** | Multi-step automations (dashboard + API) |
| **Structured extraction** | JSON Schema-shaped outputs from agent runs |
| **Proxy / geo** | Residential and granular geo targeting for agent traffic |
| **2FA / TOTP** | Push or URL-based code delivery for auth flows |

---

## Autonomy Model

```
Agent obtains API key → POST /v1/run/tasks with prompt (+ optional url, schema, session)
    ↓
Skyvern queues/runs browser agent (vision + planning)
    ↓
Optional webhook on completion; poll or SDK for status
    ↓
Structured output + artifacts (screenshots, recordings, downloads)
```

---

## Identity and Delegation Model

- **API key** scopes access to the Skyvern account/project.
- **Credentials vault / TOTP** patterns delegate human-style login without sharing secrets in prompts (see Skyvern credentials docs).
- **Sessions and profiles** bind automation state to a stable browser context for repeat runs.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | `https://api.skyvern.com` — OpenAPI-linked from docs |
| Python SDK | https://www.skyvern.com/docs/sdk-reference/overview |
| TypeScript SDK | https://www.skyvern.com/docs/ts-sdk-reference/overview |
| Self-hosted | Docker / K8s — own LLM keys |

---

## Human-in-the-Loop Support

Dashboard and **explainable run summaries** support human review; **workflows** and **Zapier/Make** integrations fit human-triggered automation. Core task API is autonomous once started.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Playwright scripts only** | No first-class **NL task** + **multi-engine** agent loop + managed **2FA/CAPTCHA** product surface |
| **RPA recorders** | Not built for **LLM agents** consuming an API with **schema-first extraction** and **session IDs** |

---

## Use Cases

- **AP / invoicing** — Log into vendor portals, download PDFs
- **Government and insurance** — Multi-page forms with vision resilience
- **Lead gen and testing** — Adaptive UI navigation without selector maintenance
