# SpecStream

> **"The live web data engine for AI agents."**

| | |
|---|---|
| **Website** | https://specstream.ai |
| **Docs** | https://specstream.ai/agents.md |
| **GitHub** | https://github.com/specstreamai |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |

---

## Official Website

https://specstream.ai

---

## Official Docs

https://specstream.ai/agents.md

---

## How to Use (Agent Onboarding)

**Quickest verified path:**

Follow the [SpecStream agent reference](https://specstream.ai/agents.md) to use the Search API or the Extract API.

---

## Agent Skills

**Status:** ⚠️ Not yet published

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://api.specstream.ai/mcp |
| **Transport** | Streamable HTTP |
| **Compatible Clients** | Any MCP-compliant client |

---

## What It Does

SpecStream is the live web data engine for AI agents. It provides high-performance search and extraction APIs designed for agentic workflows, including drop-in support for existing search protocols.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Documentation specifically defines the engine for AI agents and agent-native protocols. |
| **Agent-specific primitive** | Protocol-compatible endpoints for agent tools (Tavily/Exa/Brave/Serper/SearXNG). |
| **Autonomy-compatible control plane** | API key based operation, configurable for automated reasoning loops. |
| **M2M integration surface** | REST API, MCP. |
| **Identity / delegation** | API key scoped to project/agent execution. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Search API** | `GET /v1/web-search` — high-performance search for agents. |
| **Extract API** | `POST /v1/extract` — LLM-ready content extraction. |
| **Protocol Endpoints** | Drop-in support for existing search tool interfaces. |

---

## Autonomy Model

An agent performs reasoning, identifies the need for information, calls the SpecStream Search or Extract API directly, and processes the LLM-ready result in its next reasoning step.

---

## Identity and Delegation Model

API key authentication, scoped per project or agent to manage resource usage and audit API calls.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP API | Full REST interface |
| MCP | `https://api.specstream.ai/mcp` |

---

## Human-in-the-Loop Support

Optional, configurable on the agent side if needed.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Google Search** | Designed for human-readable SERP UX, not LLM-ready data streams. |

---

## Use Cases

- **Autonomous Research** — Deep-research retrieval via Search API.
- **Data Extraction** — Automated content extraction for agent pipelines.
- **Protocol Integration** — Drop-in replacement for existing agent tools.
