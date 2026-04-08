# Apify

> **"Get real-time web data for your AI."**

| | |
|---|---|
| **Website** | https://apify.com |
| **Docs** | https://docs.apify.com |
| **GitHub** | https://github.com/apify |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/apify/crawlee?style=social)](https://github.com/apify/crawlee) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |

---

## Official Website

https://apify.com

---

## Official Repo

https://github.com/apify/crawlee — open-source web crawling library (powers many Actors)

https://github.com/apify/apify-sdk-js — JavaScript SDK

Actor and platform code spread across https://github.com/apify

---

## How to Use (Agent Onboarding)

**REST API / SDK — run Actors (scrapers, crawlers, automations) and retrieve structured datasets.**

```bash
npm install apify-client
# or
pip install apify-client
```

Create API token at https://console.apify.com — run Actors via `POST` run endpoints per [API docs](https://docs.apify.com/api/v2).

**MCP** — Apify lists **MCP client** integrations on https://apify.com/integrations .

---

## Agent Skills

**Status:** ⚠️ Search community skills for Apify patterns.

```bash
npx clawhub@latest search apify
```

---

## MCP

**Status:** ⚠️ Apify integrates with MCP **clients** (per integrations page); the primary surface remains **REST + SDK**.

---

## What It Does

Apify is a **web data platform** for running **Actors** — serverless scrapers, crawlers, and browser automations that return **structured datasets** (JSON, CSV) through an **API**. The homepage explicitly targets **AI apps and agents** that need **fresh web data** (social, maps, e-commerce, generic site content) without operating their own proxy and browser farms.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Hero copy: *"Get real-time web data for your AI"*; Actors marketed for **AI apps and agents** |
| **Agent-specific primitive** | **Actor run lifecycle** (start, wait, fetch dataset) as a **machine-consumable** web extraction primitive; **thousands of pre-built Actors** address agent-sized tasks (single URL → structured record) |
| **Autonomy-compatible control plane** | Agents trigger runs via **API**; polling/webhooks deliver results without a human operating a browser |
| **M2M integration surface** | **REST API v2**, **JavaScript/Python clients**, webhooks, schedules |
| **Identity / delegation** | **Per-account API tokens**; Actor runs attributed to token owner; dataset ACLs via Apify account |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Actor** | Packaged scraper/automation with inputs and outputs |
| **Run** | Execution instance with status, logs, and compute metering |
| **Dataset** | Structured output storage (items, export) |
| **Proxy & anti-blocking** | Platform-managed IP rotation and unblocking options |
| **Schedules & webhooks** | Automate recurring agent data pulls |

---

## Autonomy Model

```
Agent selects Actor + input JSON via API
    ↓
Apify schedules run on platform infrastructure
    ↓
Actor completes → dataset keys returned
    ↓
Agent fetches items through API — ready for RAG or tool context
```

---

## Identity and Delegation Model

- **API tokens** scope access to account resources.
- **Per-run attribution** for billing and audit.
- **OAuth integrations** (where Actors connect to SaaS) follow Apify connector model.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | https://docs.apify.com/api/v2 |
| JavaScript | `apify-client` npm package |
| Python | `apify-client` PyPI |
| Console | https://console.apify.com |

---

## Human-in-the-Loop Support

Actors may encode approval steps in target sites; platform itself is API-first.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **curl + raw HTML** | No extraction schema, anti-bot, or dataset lifecycle |
| **Self-hosted browser only** | You operate scaling, proxies, and maintenance |
| **Firecrawl / other catalog entries** | Different extraction models; Apify emphasizes **marketplace Actors** and **programmatic run API** at scale |

---

## Use Cases

- **Research agents** — scheduled news, maps, or social data pulls
- **Lead-gen agents** — structured company/person lists into CRM tools
- **RAG ingestion** — Website Content Crawler Actor for LLM-ready markdown
