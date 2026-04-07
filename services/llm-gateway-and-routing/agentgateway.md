# Agentgateway

> **"Connect Secure Observe Connect Agentic Workflows."**

| | |
|---|---|
| **Website** | https://agentgateway.dev |
| **Docs** | https://agentgateway.dev/docs/ |
| **GitHub** | https://github.com/agentgateway/agentgateway |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/agentgateway/agentgateway?style=social)](https://github.com/agentgateway/agentgateway) |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |

---

## Official Website

https://agentgateway.dev

---

## Official Repo

https://github.com/agentgateway/agentgateway

---

## How to Use (Agent Onboarding)

**Interaction pattern:** **self-hosted proxy** (binary, Docker, or Kubernetes) — OpenAI-compatible LLM front door plus **MCP** and **A2A** routing

Quick start from the project site:

```bash
curl https://raw.githubusercontent.com/agentgateway/agentgateway/refs/heads/main/common/scripts/get-agentgateway | bash
curl -sL https://raw.githubusercontent.com/agentgateway/agentgateway/main/examples/basic/config.yaml -o config.yaml
agentgateway -f config.yaml
# Open UI at localhost:15000
```

Full paths: [Quickstart](https://agentgateway.dev/docs/quickstart/) · [LLM gateway tutorial](https://agentgateway.dev/docs/standalone/latest/tutorials/llm-gateway/) · [MCP connectivity](https://agentgateway.dev/docs/mcp/).

---

## Agent Skills

**Status:** ⚠️ No official `SKILL.md` / `npx skills add …` pack for Agentgateway yet.

```bash
npx clawhub@latest search agentgateway
```

---

## MCP

**Status:** ✅ Core protocol (MCP gateway is a primary feature)

Agentgateway **terminates and federates MCP**: multiple MCP servers behind one endpoint, stdio / HTTP/SSE / Streamable HTTP transports, OpenAPI-to-MCP exposure, and MCP auth spec alignment — see [MCP Gateway](https://agentgateway.dev/) and [docs](https://agentgateway.dev/docs/mcp/).

| Detail | Value |
|---|---|
| **Docs** | https://agentgateway.dev/docs/mcp/ |
| **Federation** | Single MCP endpoint aggregating many tool servers |
| **Deployment** | Standalone binary/Docker or Kubernetes Gateway API |

---

## What It Does

Agentgateway is an **open-source proxy** for agentic traffic: it routes **agent-to-LLM** requests through an OpenAI-compatible surface (multi-provider), connects **agent-to-tool** via MCP (including federation and auth), and **agent-to-agent** via the A2A protocol. It adds **JWT/API key auth**, CEL-based **RBAC**, rate limits, prompt guards, and **OpenTelemetry** visibility — positioned as infrastructure for agent workloads rather than a generic HTTP reverse proxy.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Site copy: *"open source proxy built on AI-native protocols (A2A & MCP) to connect, secure, and observe agent-to-LLM, agent-to-tool, and agent-to-agent communication"* — [agentgateway.dev](https://agentgateway.dev) |
| **Agent-specific primitive** | **MCP gateway / federation**; **A2A gateway**; **LLM routing** with inference-style prioritization; **OpenAPI → MCP tools** — primitives aimed at agent+tool meshes, not human CRUD apps |
| **Autonomy-compatible control plane** | Policy engine and routing operate per request; agents do not need human clicks per call |
| **M2M integration surface** | Config file / K8s CRDs, OpenAI-compatible LLM path, MCP and A2A protocol fronts, OTEL |
| **Identity / delegation** | JWT, API keys, RBAC, CEL policies, audit via telemetry — requests attributable through gateway observability |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **LLM gateway** | OpenAI-compatible routing to major providers; budget/spend controls (per docs) |
| **MCP gateway** | Federate MCP servers; enforce auth and tool access |
| **A2A gateway** | Agent-to-agent protocol routing and capability discovery |
| **Traffic policies** | Rate limit, CORS, TLS, external authz |
| **Prompt guard / enrichment** | Gate or augment prompts at the proxy (Kubernetes docs) |
| **Observability** | OpenTelemetry metrics, logs, traces |

---

## Autonomy Model

```
Agent (or agent runtime) sends LLM request to Agentgateway OpenAI-compatible endpoint
    ↓
Gateway applies auth, policy, routing → upstream LLM provider
    ↓
For tools: agent uses MCP through gateway — federation + auth to backends
    ↓
Optional A2A path for multi-agent delegation
    ↓
OTEL exports traces/metrics for operations and security review
```

---

## Identity and Delegation Model

- **JWT / API keys** — caller authentication at the edge
- **RBAC + CEL** — fine-grained authorization on routes and tools
- **MCP OAuth alignment** — integrate with IdPs per MCP auth spec (docs)
- **Distributed traces** — correlate agent, tool, and LLM hops

---

## Protocol Surface

| Interface | Detail |
|---|---|
| OpenAI-compatible HTTP | Chat completions proxy to many providers |
| MCP | stdio, SSE, Streamable HTTP — client and server federation |
| A2A | Agent-to-agent protocol routing |
| Kubernetes | Gateway API / control-plane deployment options |
| Configuration | YAML locally; CRDs on Kubernetes |

---

## Human-in-the-Loop Support

Humans deploy and define **policies** (auth, rate limits, prompt guards). Individual LLM/MCP calls do not require a human in the loop unless the application adds one above the gateway.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **NGINX / Envoy** | Generic L7 proxy; no MCP/A2A semantics, no OpenAPI→MCP, no agentic policy tutorials as first-class |
| **Managed LLM API** | Single vendor; no cross-protocol agent mesh (MCP + A2A + multi-LLM) in one open control plane |
| **Portkey / Keywords AI** | Managed SaaS LLM gateways — complementary; Agentgateway is self-hosted protocol infrastructure for MCP/A2A |

---

## Use Cases

- **Enterprise agent mesh** — one audited egress for LLM, MCP tools, and peer agents
- **MCP sprawl control** — federate dozens of MCP servers with unified auth and observability
- **Multi-provider LLM routing** — OpenAI-compatible clients without hard-coding vendor endpoints
- **Air-gapped / VPC** — run the same proxy on-prem or in Kubernetes
