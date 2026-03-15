# Letta

> **"The fastest way to bring stateful agents to production."**

| | |
|---|---|
| **Website** | https://letta.com |
| **Docs** | https://docs.letta.com |
| **GitHub** | https://github.com/letta-ai/letta |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **Origin** | Evolved from MemGPT (UC Berkeley) |

---

## Official Website

https://letta.com

---

## Official Repo

https://github.com/letta-ai/letta — Core platform (open-source)

https://github.com/letta-ai/letta-python — Python SDK (`letta-client`)

https://github.com/letta-ai/letta-node — TypeScript SDK (`@letta-ai/letta-client`)

---

## Agent Skills

**Status:** ⚠️ No official skill published by Letta yet.

```bash
npx clawhub@latest search letta
```

---

## MCP

**Status:** ✅ Available

Letta provides MCP server support, allowing agents to access Letta-managed stateful agents as tools through the Model Context Protocol.

| Detail | Value |
|---|---|
| **MCP Docs** | https://docs.letta.com/mcp |
| **Transport** | stdio / HTTP |
| **Compatible Clients** | Claude Desktop, Cursor, any MCP-compatible client |

---

## What It Does

Letta (evolved from the MemGPT research project at UC Berkeley) is a cloud platform for deploying and managing stateful agents at scale. Each agent deployed on Letta has persistent state, memory, conversation history, and reasoning traces stored in a model-agnostic format in the cloud — surviving restarts, model migrations, and provider changes.

The core abstraction: **the agent is the deployment unit**. Letta Cloud manages 24/7 uptime, auto-scaling, agent templates with versioning, and a visual debugging environment (Agent Development Environment, ADE).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"The fastest way to bring stateful agents to production"*; agents are the deployment primitive, not functions or services |
| **Agent-specific primitive** | Stateful agent deployment with model-agnostic persistent state; agent templates with versioning; memory variables injected at agent creation; self-editing memory (MemGPT pattern) |
| **Autonomy-compatible control plane** | 24/7 uptime with auto-scaling; agents maintain state autonomously without human intervention between sessions |
| **M2M integration surface** | REST API, Python SDK (`letta-client`), TypeScript SDK (`@letta-ai/letta-client`), MCP server |
| **Identity / delegation** | Per-agent IDs; agent state is scoped and isolated; model-agnostic state format prevents vendor lock-in |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Stateful Agent** | An agent with persistent state, memory, and conversation history that survives restarts |
| **Agent Template** | Versioned agent blueprint for deploying many agents with consistent initial configuration |
| **Memory Variable** | Custom fields injected into agent memory at creation time (per-user context, initial knowledge) |
| **Self-Editing Memory** | Agents can modify their own memory blocks during execution (MemGPT pattern) |
| **Model-Agnostic State** | Agent state stored in a format that survives LLM provider migration |
| **Agent Development Environment (ADE)** | Visual debugger for inspecting agent memory, reasoning traces, and conversation history |
| **Multi-Agent Orchestration** | Deploy and coordinate large numbers of agents with isolated state per agent |

---

## Autonomy Model

```
Developer defines agent via template (tools, memory schema, model config)
    ↓
Letta deploys agent with injected memory variables and initial state
    ↓
Agent runs 24/7, maintaining persistent state across sessions
    ↓
User interacts with agent — state updated after each turn
    ↓
Agent modifies own memory blocks when relevant facts change
    ↓
Developer can inspect / replay state via ADE or API at any time
    ↓
To migrate to a new LLM: Letta re-serializes model-agnostic state, no data loss
```

---

## Identity and Delegation Model

- Each agent has a unique ID; state is fully isolated between agents
- Agent templates enable deploying identical agents for different users with isolated state
- Memory variables allow operator-injected context (e.g., user's name, account tier) at creation
- Model-agnostic state format: no lock-in to OpenAI, Anthropic, or Google models

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Full agent lifecycle: create, query, update, delete |
| Python SDK | `pip install letta-client` |
| TypeScript SDK | `npm install @letta-ai/letta-client` |
| MCP Server | Expose Letta agents as tools for other agents |
| ADE | Visual Agent Development Environment for debugging |
| Letta Cloud | Fully managed hosted deployment |
| Self-hosted | Open-source Docker deployment |

---

## Human-in-the-Loop Support

Optional. Agents run fully autonomously. The ADE enables human inspection and debugging. Human approval for agent actions can be composed on top via HumanLayer.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **AWS Lambda** | Stateless compute; no agent state persistence, no memory, no agent templates |
| **Vercel / Railway** | General application deployment; agents are not the deployment unit |
| **OpenAI Assistants API** | Vendor-locked; state stored in OpenAI format; no custom memory architecture, no model migration |
| **Mem0** | Memory extraction layer; Letta is a full stateful agent runtime with self-editing memory, templates, and deployment infrastructure |

---

## Use Cases

- **Personal assistant agents** — agent remembers each user's preferences and history persistently across unlimited sessions
- **Enterprise knowledge agents** — deploy isolated agents per employee with company-specific memory variables
- **Long-running research agents** — agents accumulate knowledge over days or weeks without losing context
- **Multi-user SaaS agents** — manage thousands of isolated agent instances (one per user) from a single template
- **Model migration** — switch agents from GPT-4o to Claude Sonnet without losing any stored state
