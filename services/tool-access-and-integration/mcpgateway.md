# MCP Gateway

> **"The platform for production AI agents."**

| | |
|---|---|
| **Website** | https://mcpgateway.com |
| **Docs** | https://mcpgateway.com (product + blog) |
| **GitHub** | N/A (platform SDK on PyPI) |
| **PyPI** | https://pypi.org/project/mcpgateway-sdk/ |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |

---

## Official Website

https://mcpgateway.com

---

## Official Repo

Primary integration surface is the **`mcpgateway-sdk`** Python package — https://pypi.org/project/mcpgateway-sdk/

---

## How to Use (Agent Onboarding)

**SDK / REST — one gateway URL and API key for tools, skills, and sandboxes.**

```bash
pip install mcpgateway-sdk
```

```python
from mcpgateway_sdk import MCPGateway

async with MCPGateway() as gw:
    results = await gw.tools.search("create a pull request")
    # execute discovered tools with server scoping — see PyPI readme
```

Configure `MCPGATEWAY_URL` and `MCPGATEWAY_TOKEN` (or pass `api_key` / `url` explicitly). See product page for deployment options (self-hosted Kubernetes / cloud marketplaces — some listed as coming soon).

---

## Agent Skills

**Status:** ⚠️ Platform supports **Agent Skills** as portable instruction packages (create/manage via SDK per marketing examples); no single public `npx skills add` repo verified here — see vendor docs.

---

## MCP

**Status:** ✅ Core product is an **MCP aggregation gateway** — multiple MCP servers behind **one URL** with OAuth token lifecycle, RBAC, audit, and telemetry (per homepage).

| Detail | Value |
|---|---|
| **Product surface** | Federated MCP servers + skills + sandboxes |
| **SDK** | Python `mcpgateway-sdk` |

---

## What It Does

MCP Gateway is an **enterprise control plane** for production agents: it unifies **MCP servers** (tools), **Agent Skills** (how to use tools), and **sandboxes** (where code runs) behind **one API key and URL**. Marketing emphasizes governance — semantic **tool search** across many servers, **automatic OAuth refresh**, **RBAC**, **audit trails**, and **telemetry** — to reduce "shadow AI" from unmanaged MCP sprawl.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"The platform for production AI agents"*; explicitly lists LangChain, CrewAI, Claude, Cursor, Copilot Studio as clients |
| **Agent-specific primitive** | **Semantic tool search across federated MCP servers**; **skills** as agent instruction packages tied to tool graphs; **warm sandboxes** for agent code execution |
| **Autonomy-compatible control plane** | OAuth tokens **stay alive without human re-auth** per marketing copy; agents call tools through the gateway API |
| **M2M integration surface** | Python SDK (`mcpgateway-sdk`); API-first gateway |
| **Identity / delegation** | **RBAC**, **audit**, **token management** — delegated third-party access attributed through gateway policies |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Federated MCP** | Many MCP servers behind one endpoint |
| **Tool search** | Natural-language discovery over registered tools |
| **Skill packages** | Versioned `skill.md`-style workflow definitions |
| **Sandboxes** | Isolated execution environments with exec API |
| **Governance** | Auth, RBAC, audit, telemetry |

---

## Autonomy Model

```
Agent (or orchestrator) holds MCP Gateway API key
    ↓
gw.tools.search(intent) → ranked tools across servers
    ↓
gw.tools.execute(...) with server scope — OAuth handled by gateway
    ↓
Optional: gw.sandboxes.exec(...) for code/actions in isolation
    ↓
Audit + telemetry record tool and sandbox events
```

---

## Identity and Delegation Model

- **API keys** gate gateway access; **RBAC** maps principals to allowed servers/tools.
- **OAuth tokens** for SaaS integrations stored and refreshed by the platform.
- **Audit trail** ties actions to gateway identity and policy context.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install mcpgateway-sdk` |
| HTTP API | Gateway URL from deployment |
| MCP | Aggregated MCP backend servers |

---

## Human-in-the-Loop Support

Enterprise workflows may require approval policies; core design targets unattended agent tool use under governance.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Open-source MCP proxy only** | May lack bundled skills registry, warm sandboxes, and enterprise RBAC as one product |
| **iPaaS** | Not MCP-native; human workflow builders predominate |
| **Per-server MCP config** | No unified search, OAuth brokerage, or cross-server audit |

---

## Use Cases

- **Regulated enterprises** — single governed MCP front door for many teams
- **Multi-tenant SaaS** — ship agent features without exposing raw provider OAuth to each tenant
- **Tool sprawl** — semantic discovery over dozens of internal and external MCP servers
