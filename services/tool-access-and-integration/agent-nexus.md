# Agent Nexus

> **"Autonomous discovery, verified health cards, and drift alerts for 730+ live MCP servers and agent tools."**

| | |
|---|---|
| **Website** | https://agentnexus.app |
| **Docs** | https://agentnexus.app/llms.txt |
| **GitHub** | https://github.com/Strategiumfinancepartner/AgentNexus |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **Funding / Compliance** | Self-funded. Independent registry and verification layer for AI agents. Open discovery API, free programmatic key minting (1,000 calls/day), optional Pro/Publisher tiers |
| **Latest-month signal** | Live on 2026-11-22: [homepage](https://agentnexus.app), [llms.txt](https://agentnexus.app/llms.txt), [OpenAPI](https://agentnexus.app/openapi.json), [discover](https://agentnexus.app/api/public/discover) (all HTTP 200). Remote MCP `initialize` at `https://agentnexus.app/api/public/mcp` returns `agent-nexus` 1.1.0 with 8 tools. 730+ active server entries |
| **Verified at** | 2026-11-22 |

---

## Official Website

https://agentnexus.app

---

## Official Repo

https://github.com/Strategiumfinancepartner/AgentNexus

---

## ⭐ How to Use (Agent Onboarding)

> **URL Onboarding — an agent reads one document, discovers live tools anonymously or mints its own key in one programmatic POST call without human sign-up.**

**One-sentence instruction:**

```
Read https://agentnexus.app/llms.txt and follow it.
```

**Interaction pattern:** `URL Onboarding` ⭐

An agent reads `https://agentnexus.app/llms.txt` to discover the live catalog:
1. **Anonymous discovery:** Query `GET /api/public/discover?need=<what+you+want+to+do>` to get verified services ranked by live uptime, protocol compatibility, and fallback alternatives.
2. **Programmatic key minting:** `POST /api/public/keys` with `{"name": "my-agent"}` instantly returns an API key (`1,000 calls/day`) with no captcha, email requirement, or human sign-up step.
3. **MCP integration:** Connect directly to `https://agentnexus.app/api/public/mcp` to call discovery and health tools over streamable HTTP.

---

## Agent Skills

**Status:** ⚠️ Not yet published

Search community skills: `npx clawhub@latest search agent-nexus`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Endpoint** | `https://agentnexus.app/api/public/mcp` (Streamable HTTP) |
| **Auth** | Anonymous for discovery and health checks; bearer or `x-api-key` header for higher rate limits and programmatic submissions |
| **Tools** | `discover_services`, `find_working_service`, `check_service_health`, `get_service_alternatives`, `get_health_card`, `mint_free_key`, `submit_service`, `report_issue` |
| **Docs** | https://agentnexus.app/llms.txt |

---

## What It Does

Agent Nexus is an independent registry, discovery engine, and health verification index for autonomous AI agents. Instead of static directory listings that go stale, Agent Nexus runs continuous multi-layered hourly probes (liveness, protocol handshake, capability responses, and tool-schema drift) across 730+ public MCP servers and agent-accessible APIs.

When an agent needs a capability (such as web search, transaction processing, code sandboxes, or communications), it queries Agent Nexus by natural-language intent. Agent Nexus returns verified matching services ranked by active operational health, authentication schema, and retry cost, accompanied by automated failover alternatives if a target service is degraded.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Tagline: **"Autonomous discovery, verified health cards, and drift alerts for 730+ live MCP servers and agent tools."** Built from the ground up for autonomous agent runtimes, LLM tool callers, and machine consumers. |
| **Agent-specific primitive** | Machine-readable health cards (`/api/public/health-card/{slug}`) with cryptographic probe receipts, schema drift detection (comparing 24-hour shape history to prevent runtime tool hallucination), and programmatic key creation without human friction. |
| **Autonomy-compatible control plane** | Autonomous agents search, verify endpoints, retrieve fallback alternatives during downstream outages, report execution metrics, and register new tools without dashboard logins or human intervention. |
| **M2M integration surface** | Remote MCP (`/api/public/mcp`), REST API, OpenAPI (`/openapi.json`), [llms.txt](https://agentnexus.app/llms.txt), streaming NDJSON catalog (`/api/public/entries.ndjson`), and health cards. |
| **Identity / delegation** | Instant programmatic agent keys (`POST /api/public/keys`); caller segmentation distinguishing autonomous agents from crawlers and monitors; optional email attachment for audit reports. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Discover Services** | Query endpoints by natural-language need, filtering by transport (MCP, REST), geographic constraints, and auth shape |
| **Find Working Service** | Direct single-call fallback locator returning the highest-scoring verified service currently passing probes |
| **Health Cards** | Machine-readable JSON receipts documenting probe latencies, transport contracts, uptime history, and drift state |
| **Programmatic Key Minting** | Zero-friction `POST /api/public/keys` returning scoped agent credentials in milliseconds |
| **Schema Drift Probes** | Automated comparison of tool signatures against negotiated baselines to alert callers to breaking schema changes |
| **Fallback Alternatives** | Automated recommendation of active alternatives whenever a queried tool experiences downtime |

---

## Autonomy Model

1. The agent reads `https://agentnexus.app/llms.txt` or initiates MCP transport at `https://agentnexus.app/api/public/mcp`.
2. For one-off tasks, the agent queries `GET /api/public/discover?need=...` anonymously.
3. For persistent pipelines, the agent calls `POST /api/public/keys` to mint a dedicated key and stores it in runtime memory.
4. When selecting a tool, the agent verifies its health card or calls `find_working_service`.
5. If a selected provider fails in production, the agent queries fallback alternatives without halting execution.

---

## Identity and Delegation Model

- The agent is the primary credential holder via programmatic bearer keys (`nx_...`).
- Keys are provisioned programmatically in a single machine-to-machine exchange.
- Caller identity and caller type are logged for rate limiting and service health telemetry.
- An optional human contact email can be attached to a key for recovery and out-of-band drift notifications.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| URL Onboarding | https://agentnexus.app/llms.txt |
| REST API | `https://agentnexus.app/api/public`, Bearer or `x-api-key` |
| OpenAPI | https://agentnexus.app/openapi.json |
| MCP | `https://agentnexus.app/api/public/mcp` (Streamable HTTP) |
| Streaming Catalog | `https://agentnexus.app/api/public/entries.ndjson` |
| Docs for LLMs | https://agentnexus.app/llms.txt |

---

## Human-in-the-Loop Support

Autonomous discovery and key creation require no human intervention. Human operators can optionally inspect web dashboards, monitor drift alerts via email or webhooks, and claim service ownership via DNS/TXT or well-known token verification.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Static Awesome Lists & Curated Repos** | Human-curated markdown tables with no automated uptime checks, no schema drift detection, and no machine-callable APIs |
| **Generic API Registries (SwaggerHub, RapidAPI)** | Built for human enterprise developers, requiring manual web account sign-ups, captchas, credit card entry, and static OpenAPI specs without live MCP runtime health probes |

---

## Use Cases

- **Autonomous Tool Discovery** — allow LLM agents to locate specialized tools and MCP servers on demand without manual pre-configuration
- **Downstream Outage Failover** — query fallback alternatives when an integrated service degrades or fails
- **Schema Drift Protection** — verify tool signature stability before invoking external functions in mission-critical workflows
- **Programmatic Bootstrap** — enable newly spawned agent sandboxes to acquire verified tool registries without pre-provisioned credentials
