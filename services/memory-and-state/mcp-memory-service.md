# mcp-memory-service

> **"Memory for AI Agents — REST, MCP, OAuth, CLI"**

| | |
|---|---|
| **Website** | https://mcpmemory.services |
| **Docs** | https://mcpmemory.services |
| **GitHub** | https://github.com/doobidoo/mcp-memory-service |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/doobidoo/mcp-memory-service?style=social)](https://github.com/doobidoo/mcp-memory-service) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-09-02 ([repo metadata](https://api.github.com/repos/doobidoo/mcp-memory-service)); PyPI `mcp-memory-service`; homepage showed v11.10.0 on 2026-09-04 |
| **Verified at** | 2026-09-04 |

---

## Official Website

https://mcpmemory.services

Homepage title lead (live 2026-09-04): **“Memory for AI Agents — REST, MCP, OAuth, CLI”** · `mcp-memory-service v11.10.0`. Supporting line: “Interactive 3D knowledge graph — every memory a glowing node, every relationship a curved edge.”

---

## Official Repo

https://github.com/doobidoo/mcp-memory-service

README H1: **“Persistent Shared Memory for AI Agent Pipelines”**

README lead: “Open-source memory backend for AI agents — **REST API, MCP, OAuth, CLI, dashboard**. One self-hosted service, every transport.”

GitHub description: **“Open-source persistent memory for AI agent pipelines (LangGraph, CrewAI, AutoGen) and Claude. REST API + knowledge graph + autonomous consolidation.”**

Mirror: https://codeberg.org/doobidoo/mcp-memory-service

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + MCP / REST

```bash
pip install mcp-memory-service
```

stdio MCP (Claude Desktop / Claude Code):

```bash
claude mcp add memory -- memory server
```

Agent pipelines (REST — LangGraph, CrewAI, AutoGen, any HTTP client):

```bash
MCP_ALLOW_ANONYMOUS_ACCESS=true memory server --http
# REST API at http://localhost:8000
```

```python
import httpx
httpx.post(
    "http://localhost:8000/api/memories",
    json={"content": "..."},
    headers={"X-Agent-ID": "researcher"},
)
```

Remote MCP + OAuth (claude.ai browser):

```bash
MCP_STREAMABLE_HTTP_MODE=1 MCP_SSE_HOST=0.0.0.0 MCP_OAUTH_ENABLED=true \
  python -m mcp_memory_service.server
```

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

OpenCode ships a repo-local plugin (`opencode/memory-plugin.js`). Community search:

```bash
npx clawhub@latest search mcp-memory-service
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — the service **is** an MCP memory server (stdio + Streamable HTTP + SSE)

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/doobidoo/mcp-memory-service |
| **Transport** | stdio (`memory server`); Streamable HTTP / SSE for remote MCP |
| **Auth** | OAuth 2.0 + DCR (remote); optional anonymous local HTTP |
| **Compatible Clients** | Claude Desktop, Claude Code, Cursor, OpenCode, claude.ai (Remote MCP), ChatGPT Developer Mode, any HTTP agent |
| **Header** | `X-Agent-ID` auto-tags memories per agent |

---

## What It Does

mcp-memory-service is a **self-hosted memory backend** for AI agent pipelines: one process exposes REST, MCP, OAuth, CLI, and a dashboard. Agents store decisions, share a causal knowledge graph (typed edges: causes, fixes, contradicts), retrieve in ~5 ms, and run autonomous consolidation — embeddings stay local (ONNX) unless the operator chooses a cloud backend.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [Zep](zep.md) / [Graphiti](graphiti.md) | Temporal context-graph product vs OSS Graphiti framework. This entry is a multi-transport memory *service* (REST+MCP+OAuth) with `X-Agent-ID` |
| [Mem0](mem0.md) | Extraction SDK/SaaS. mcp-memory-service is self-host MCP+REST with OAuth DCR |
| [Recall](recall.md) | MCP-native self-host memory — narrower transport set, no OAuth/DCR story |
| [MemPalace](mempalace.md) | Palace/drawer metaphor + 44 MCP tools. Different architecture (README compares LongMemEval claims) |

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: **“Memory for AI Agents — REST, MCP, OAuth, CLI”** — [mcpmemory.services](https://mcpmemory.services). README: “Open-source memory backend for AI agents.” |
| **Agent-specific primitive** | Shared causal knowledge graph; `X-Agent-ID` scoped retrieval; `conversation_id`; SSE on store/delete; autonomous consolidation horizons |
| **Autonomy-compatible control plane** | After `memory server`, agents store/search over REST or MCP with no dashboard click |
| **M2M integration surface** | 76 REST endpoints, stdio MCP, Streamable HTTP, CLI, SSE |
| **Identity / delegation** | `X-Agent-ID` per caller; OAuth 2.0 + PKCE + DCR for remote MCP; optional anonymous local mode (C5-weak, documented) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Multi-transport memory** | REST + MCP + OAuth + CLI + dashboard, one backend |
| **`X-Agent-ID`** | Auto-tag and scope memories per agent |
| **Causal knowledge graph** | Typed edges (causes, fixes, contradicts) |
| **Autonomous consolidation** | Time-horizon compression of old memories |
| **Local ONNX embeddings** | Memory can stay on-box |
| **Remote MCP + OAuth DCR** | Browser/claude.ai connectors without a desktop host |

---

## Autonomy Model

```
Operator pip-installs and starts `memory server` (stdio or --http)
    -> Agent stores via MCP tool or REST + X-Agent-ID
    -> Graph + vector index update; SSE notifies peers
    -> Agent retrieves in ~5 ms on the next turn
    -> Consolidation job compresses old horizons without a human curator
```

---

## Identity and Delegation Model

- **Agent identity:** `X-Agent-ID` header (REST) and MCP session identity.
- **Remote callers:** OAuth 2.0 + DCR; refresh via `offline_access`.
- **Local default:** bind `127.0.0.1`; `MCP_ALLOW_ANONYMOUS_ACCESS` is an explicit trust-the-host switch.
- **Multi-user:** backends include SQLite, hybrid sync, Cloudflare, Milvus; AuthMCP-style proxies documented for team ACLs.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| PyPI | `pip install mcp-memory-service` |
| CLI | `memory server` / `memory server --http` |
| REST | `:8000` — 76 endpoints |
| MCP | stdio + Streamable HTTP + SSE |
| OAuth | 2.0 + DCR for remote MCP |
| License | Apache-2.0 |

---

## Human-in-the-Loop Support

Optional dashboard and 3D graph visualization. Store/search/consolidate do not require a click. First-time OAuth to a public remote MCP URL needs a human browser once.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **[Zep](zep.md) / [Graphiti](graphiti.md)** | Managed temporal graph vs OSS Graphiti. This is a multi-transport self-host memory service with OAuth DCR |
| **Mem0 / Redis / Pinecone** | SDK or raw store — no MCP+OAuth+`X-Agent-ID` control plane |
| **Recall / MemPalace** | Different MCP memory shapes (stdio-only or palace drawers) |
| **Chat-product memory** | Human workspace feature, not an agent-callable service |

---

## Use Cases

- **Multi-agent pipelines** — LangGraph/CrewAI/AutoGen share one REST memory
- **Claude/Cursor MCP** — stdio or remote HTTP with OAuth
- **claude.ai in the browser** — Remote MCP + DCR
- **On-prem memory** — ONNX embeddings, no cloud lock-in
