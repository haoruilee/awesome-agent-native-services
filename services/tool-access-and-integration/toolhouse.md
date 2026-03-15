# Toolhouse

> **"BaaS for AI agents — tools, memory, and execution in one."**

| | |
|---|---|
| **Website** | https://toolhouse.ai |
| **Docs** | https://docs.toolhouse.ai |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |

---

## Official Website

https://toolhouse.ai

---

## Official Repo

https://github.com/toolhouseai/toolhouse-sdk-python — Python SDK

https://github.com/toolhouseai/toolhouse-sdk-typescript — TypeScript SDK

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official skill published by Toolhouse yet.

Toolhouse's MCP server is itself the primary extension mechanism — agents connect to it at runtime to discover tools. No `SKILL.md`-based skill has been published to the AgentSkills ecosystem as of Q1 2026.

```bash
# No official install command yet — watch the repo:
# https://github.com/toolhouseai
```

> If you want to contribute a skill, see the [AgentSkills specification](https://agentskills.io/specification) and reference the [Toolhouse docs](https://docs.toolhouse.ai).

---

## MCP

**Status:** ✅ Built-in

MCP is the core tool access mechanism in Toolhouse. Every deployed agent automatically connects to Toolhouse's MCP server, gaining access to all registered tools (RAG, memory, code execution, browser) without additional configuration.

| Detail | Value |
|---|---|
| **MCP Docs** | https://docs.toolhouse.ai/toolhouse |
| **Transport** | Streaming HTTP (built into agent endpoint) |
| **Compatible Clients** | Any Toolhouse-deployed agent; Claude Desktop; Cursor |

---

## What It Does

Toolhouse is a Backend-as-a-Service platform where agents are the deployment unit. Developers define agents as code, publish them with `th deploy`, and Toolhouse exposes each agent as a streaming API endpoint. Each deployed agent automatically connects to Toolhouse's MCP server, gaining access to RAG, memory, code execution, browser use, and custom tools — without managing any infrastructure.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The CLI command `th deploy` publishes an *agent* (not a function or service) as an API endpoint |
| **Agent-specific primitive** | Agent endpoint, MCP-connected tool registry, built-in RAG, scheduled agent execution via cron |
| **Autonomy-compatible control plane** | Globally distributed runtime; agents run headlessly with built-in observability and retries |
| **M2M integration surface** | CLI (`th deploy`, `th run`), MCP server, streaming REST API at `https://agents.toolhouse.ai/{id}` |
| **Identity / delegation** | Public/private agent endpoints with optional authentication tokens |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent Endpoint** | Each deployed agent becomes a streaming REST API endpoint |
| **MCP Tool Registry** | Automatic connection to Toolhouse MCP server for tool discovery and execution |
| **Built-in RAG** | Retrieval-augmented generation without managing a vector database |
| **Agent Memory** | Persistent memory across agent sessions |
| **Scheduled Execution** | Cron-based agent invocation for autonomous background tasks |
| **Observability** | Execution logs, MCP call traces, full agent lifecycle visibility |

---

## Autonomy Model

1. Developer defines agent logic in TypeScript/Python
2. `th deploy` publishes the agent to Toolhouse's globally distributed runtime
3. Agent is available at `https://agents.toolhouse.ai/{agent_id}` as a streaming endpoint
4. Agent automatically connects to the Toolhouse MCP server and discovers available tools
5. Cron schedules allow agents to run autonomously without any trigger

---

## Identity and Delegation Model

- Agents can be deployed as public (no auth) or private (token-authenticated) endpoints
- Toolhouse handles runtime identity and secret management for the agent
- Each agent has a unique ID used for routing, logging, and billing

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `th deploy` (publish), `th run` (test locally) |
| MCP Server | Automatic connection to Toolhouse tool registry |
| Streaming REST API | `POST https://agents.toolhouse.ai/{agent_id}` with streaming response |
| Cron Expressions | `@hourly`, `0 9 * * MON`, etc. for scheduled execution |

---

## Human-in-the-Loop Support

Optional. Agents support asynchronous, event-driven execution patterns. Human approval can be composed on top via HumanLayer or webhook callbacks.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **AWS Lambda** | General compute; no agent identity, no MCP tool registry, no built-in RAG or memory |
| **Vercel Functions** | Serverless for human-facing web apps; no agent-specific primitives |
| **Heroku** | General PaaS; agents are not a deployment primitive |
| **Railway** | General deployment platform; no concept of agent endpoint, tool registry, or agent memory |

---

## Use Cases

- **Autonomous research agents** — deployed agents that periodically search, synthesize, and report
- **API-served agents** — organizations expose agents as internal APIs consumed by other systems
- **Scheduled monitoring** — agents that run on cron to check conditions and trigger actions
- **Tool-heavy agents** — agents that need access to many tools (web, code execution, memory, RAG) without building the integration layer
