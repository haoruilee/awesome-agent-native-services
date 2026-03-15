# Composio

> **"The tool platform built for agents."**

| | |
|---|---|
| **Website** | https://composio.dev |
| **Docs** | https://docs.composio.dev |
| **GitHub** | https://github.com/ComposioHQ/composio |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **Integrations** | 250+ external APIs |

---

## What It Does

Composio gives AI agents the ability to **discover, authenticate, and call external tools at runtime**. Rather than a developer pre-configuring a fixed set of integrations at build time, agents receive meta-tools at runtime that let them find the right integration, authenticate on behalf of the user, and execute the call — all within the agent loop, without any human clicking an OAuth button.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs: *"Agent gets meta tools that discover, authenticate, and execute the right tools at runtime"* |
| **Agent-specific primitive** | Runtime tool discovery; in-loop OAuth (agent prompts user with Connect Link during conversation); per-`user_id` credential scoping |
| **Autonomy-compatible control plane** | Token refresh, credential storage, and tool selection are handled by Composio; agent code stays clean |
| **M2M integration surface** | Python SDK (`composio_openai`, `composio_anthropic`), TypeScript SDK, MCP-compatible, 10+ framework integrations |
| **Identity / delegation** | Each tool call is scoped to a `user_id`; Composio manages OAuth tokens per user, per agent |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Meta-Tools** | Tools that let agents discover, authenticate, and call other tools at runtime |
| **Connect Link** | Hosted OAuth page agents present to users inline during conversation |
| **Runtime Tool Discovery** | Agent queries a tool registry to find relevant integrations dynamically |
| **Credential Lifecycle** | Composio handles OAuth token creation, refresh, and revocation |
| **Tool Execution** | Managed execution layer with context injection and result formatting |
| **Per-User Scoping** | Each `user_id` gets isolated credentials; tool calls cannot leak between users |

---

## Autonomy Model

**Without Composio:** Agent needs hardcoded tool list, static OAuth tokens, manual credential rotation. Fails when a token expires mid-loop.

**With Composio:**
1. Agent receives meta-tools: `discover_tools(query)`, `authenticate_app(app, user_id)`, `execute_tool(tool, params, user_id)`
2. At runtime, agent discovers which tool fits the task
3. If the user hasn't connected the app yet, agent serves a Connect Link inline (user clicks once, Composio handles OAuth)
4. Subsequent calls are fully autonomous — tokens refresh automatically

---

## Identity and Delegation Model

- `user_id` is the delegation anchor — every tool call is scoped to a specific user's credentials
- Composio stores OAuth tokens; they never appear in agent code
- Custom OAuth configs support white-labeling and custom scopes
- Multi-tenant: one agent can serve thousands of users with isolated credential sets

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `composio_openai`, `composio_anthropic`, `composio_langchain`, etc. |
| TypeScript SDK | `@composio/core`, framework-specific packages |
| MCP Compatible | Works with Claude Desktop, Cursor, OpenAI Agents without framework packages |
| Framework Integrations | LangChain, CrewAI, LangGraph, LlamaIndex, Vercel AI SDK, AutoGen, and more |

---

## Human-in-the-Loop Support

Initial OAuth consent is triggered inline by the agent (agent serves Connect Link to user). After consent, all subsequent tool calls are fully autonomous — no human interaction needed unless credentials are revoked.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Zapier** | Human-facing workflow builder; integrations are configured by humans clicking through a UI; no runtime discovery, no agent-initiated OAuth |
| **Make (Integromat)** | Visual automation for human operators; no per-agent credential isolation, no runtime tool discovery |
| **Direct API calls** | Requires hardcoded credentials, manual token rotation; no runtime discovery |
| **LangChain Tools** | Framework-level tool definition; developers write tool code; Composio provides the managed execution and auth layer on top |

---

## Use Cases

- **Personal assistant agents** — agent discovers and calls Calendar, Gmail, Slack, Notion on behalf of the user with isolated per-user credentials
- **Sales agents** — agent searches for the right CRM integration at runtime, authenticates with Salesforce/HubSpot, and logs calls
- **Coding agents** — agent discovers and calls GitHub, Jira, Linear at runtime to create issues, PRs, and comments
- **Research agents** — agent dynamically selects from hundreds of data integrations based on task requirements
