# MCP-Cloud (mcp-agent)

> **"Deploy and host your mcp-agents and apps on the cloud."**

| | |
|---|---|
| **Website** | https://docs.mcp-agent.com |
| **Docs** | https://docs.mcp-agent.com/get-started/cloud |
| **GitHub** | https://github.com/lastmile-ai/mcp-agent |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/lastmile-ai/mcp-agent?style=social)](https://github.com/lastmile-ai/mcp-agent) |
| **Classification** | `agent-native` |
| **Category** | [Durable Execution & Scheduling Services](README.md) |

---

## Official Website

https://docs.mcp-agent.com (documentation hub; marketing site may vary)

---

## Official Repo

https://github.com/lastmile-ai/mcp-agent — `mcp-agent` framework and CLI

---

## How to Use (Agent Onboarding)

**CLI — deploy durable MCP servers and agents to managed cloud (open beta).**

```bash
uvx mcp-agent login
uvx mcp-agent deploy my-agent
# Endpoint: https://<unique_id>.deployments.mcp-agent.com
```

Wire into Claude Desktop, Cursor, VS Code, or ChatGPT Apps:

```bash
uvx mcp-agent install https://<unique_id>.deployments.mcp-agent.com \
  --client cursor \
  --name my-agent
```

See [MCP-Cloud](https://docs.mcp-agent.com/get-started/cloud).

---

## Agent Skills

**Status:** ⚠️ Framework-focused; use repo examples and `mcp_agent.config.yaml` patterns.

---

## MCP

**Status:** ✅ Deployed workloads expose a **remote MCP server** over HTTP/SSE.

| Detail | Value |
|---|---|
| **Transport** | SSE / Streamable HTTP (per client config examples) |
| **Endpoint** | `https://<id>.deployments.mcp-agent.com` |

---

## What It Does

**MCP-Cloud (mcp-c)** is a managed platform for **hosting mcp-agent applications, FastMCP servers, and ChatGPT App backends** as **remote MCP servers**. Long-running tools and workflows run on **Temporal** with **retries**, **pause/resume**, and **human input** support; **secrets** are managed for developers and end users; **observability** includes logs, traces, and workflow history — see [MCP-Cloud overview](https://docs.mcp-agent.com/cloud/mcp-agent-cloud/overview).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Product is **MCP-agent** hosting — agents and tools are the unit of deploy |
| **Agent-specific primitive** | **Durable MCP tool workflows** on Temporal; **deployment-scoped secrets**; **one URL per deployed agent server** |
| **Autonomy-compatible control plane** | Workflows survive failures via Temporal; human input is modeled as **workflow steps**, not ad-hoc SSH |
| **M2M integration surface** | `uvx mcp-agent` CLI, Python SDK patterns, YAML config |
| **Identity / delegation** | **Bearer auth** to deployments; **user vs deployment secrets** |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Cloud deploy** | Push agent → receive `*.deployments.mcp-agent.com` MCP endpoint |
| **Temporal workflows** | Durable execution for long tools |
| **Secrets** | Deployment vs user-provided secrets |
| **Client install** | One command to register remote MCP in Cursor / Claude / VS Code |
| **Observability** | `mcp-agent cloud logger tail`, workflow describe commands |

---

## Autonomy Model

```
Developer defines MCPApp + tools in Python
    ↓
uvx mcp-agent deploy packages app → cloud assigns HTTPS MCP URL
    ↓
MCP clients call tools — long steps run as Temporal workflows
    ↓
Failures retry; optional human-in-the-loop waits inside workflow
    ↓
Operator tails logs and traces from CLI
```

---

## Identity and Delegation Model

- **API tokens** from `mcp-agent login` gate deploy and management APIs.
- **Deployment auth** via bearer tokens on MCP HTTP endpoints.
- **User secrets** supplied by end users through `mcp-agent cloud configure` flows.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `uvx mcp-agent` — login, deploy, install, cloud logger |
| MCP over HTTPS | Standard MCP client config with `Authorization: Bearer` |
| Python | `mcp_agent` package patterns in docs |

---

## Human-in-the-Loop Support

Temporal workflows support **pause/resume** and **human input** steps — see [Long-running tools](https://docs.mcp-agent.com/cloud/mcp-agent-cloud/long-running-tools).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw Temporal Cloud** | You build MCP framing, auth, and client install UX yourself |
| **Serverless functions** | Short timeouts; poor fit for hour-long agent sessions |
| **Self-hosted MCP only** | No managed secret split for end-user keys |

---

## Use Cases

- **Hosted research agents** — expose durable MCP tools to Cursor teams
- **ChatGPT Apps** — ship backends that speak MCP without operating Temporal
- **Enterprise pilots** — one deploy command per agent experiment
