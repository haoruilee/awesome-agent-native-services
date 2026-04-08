# Smithery

> **"Connect your agent to thousands of MCP tools and Agent Skills."**

| | |
|---|---|
| **Website** | https://smithery.ai |
| **Docs** | https://smithery.ai/docs |
| **GitHub** | https://github.com/smithery-ai/cli |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/smithery-ai/cli?style=social)](https://github.com/smithery-ai/cli) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |

---

## Official Website

https://smithery.ai

---

## Official Repo

https://github.com/smithery-ai/cli — CLI for installing and managing MCP servers and skills

https://github.com/smithery-ai/sdk — TypeScript SDK for programmatic access

https://github.com/smithery-ai/smithery-cli-mcp — MCP server wrapping Smithery CLI operations

---

## How to Use (Agent Onboarding)

**CLI — wire thousands of hosted MCP servers into an agent host with managed OAuth.**

```bash
npx @smithery/cli@latest setup
# or
npm install -g @smithery/cli
smithery auth login
smithery mcp add <server>
smithery tool list
smithery tool call <server> <tool> '<json-args>'
```

See [Introduction](https://docs.smithery.ai/) and [Registry: Search Servers](https://smithery.ai/docs/concepts/registry_search_servers).

---

## Agent Skills

**Status:** ✅ Smithery hosts a large **Skills** registry (machine-readable workflows) browsable at https://smithery.ai/skills — install flows use the Smithery CLI; see docs for publishing and discovery.

---

## MCP

**Status:** ✅ Smithery is an **MCP-native** distribution layer: the registry exposes **remote MCP servers**; the CLI configures clients (Cursor, Claude Desktop, VS Code, ChatGPT Apps, etc.). Hosted servers use Smithery-managed **OAuth and sessions** so agents do not embed long-lived third-party secrets for every integration.

| Detail | Value |
|---|---|
| **MCP Docs** | https://docs.smithery.ai/ |
| **Transport** | Remote MCP (HTTP/SSE per server) + CLI stdio bridging for local clients |
| **Compatible Clients** | Cursor, Claude Desktop, VS Code MCP hosts, ChatGPT Apps, other MCP-compatible hosts |

---

## What It Does

Smithery is a **registry and gateway** for **Model Context Protocol** servers and **Agent Skills**. An agent (or its human operator once) uses the CLI to **search**, **install**, and **invoke** tools across thousands of published MCP servers — with **managed authentication** and **usage observability** for publishers. It solves the integration explosion problem for tool-using agents: one discovery and OAuth flow instead of bespoke config per SaaS.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Connect your agent to thousands of MCP tools and Agent Skills"*; CLI examples are agent-client oriented |
| **Agent-specific primitive** | **MCP server discovery + hosted remote MCP** with **OAuth handoff URLs** designed for LLM clients — not a human-only integration catalog |
| **Autonomy-compatible control plane** | After auth, tool calls are **programmatic** (`smithery tool call`, SDK, or MCP client) without per-tool dashboard clicks |
| **M2M integration surface** | CLI, TypeScript SDK, MCP protocol, REST/registry APIs per docs |
| **Identity / delegation** | **Per-connection OAuth** and session management; tool calls attributable via Smithery/account scoping |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **MCP registry** | Searchable catalog of remote MCP servers (tools, metadata, install counts) |
| **CLI install** | `smithery mcp add` wires a server into a host config |
| **Managed OAuth** | Hosted auth URLs for third-party APIs without static secrets in agent prompts |
| **Skills registry** | Published Agent Skills for reusable agent workflows |
| **Publisher observability** | Usage metrics for MCP authors (per marketing site) |

---

## Autonomy Model

```
Agent host (or operator) runs Smithery CLI / SDK
    ↓
Search registry → select MCP server
    ↓
OAuth or API flow completes → session stored by Smithery
    ↓
Agent issues tool calls through MCP — Smithery routes to remote server
    ↓
Results return as MCP tool outputs; no per-call human UI
```

---

## Identity and Delegation Model

- **User / workspace accounts** own OAuth grants for third-party tools.
- **Tool calls** run under those grants — agents act within delegated scopes, not with raw provider passwords in context.
- **Audit** via publisher dashboards and standard MCP host logging.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Smithery CLI | `npx @smithery/cli@latest`, global `smithery` |
| TypeScript SDK | https://github.com/smithery-ai/sdk |
| MCP | Remote servers in registry; `smithery-cli-mcp` for meta-operations |
| Docs API | https://smithery.ai/docs |

---

## Human-in-the-Loop Support

Initial **OAuth consent** may require a human browser step; after that, tool execution is automated. Skills may encode HITL workflows.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Manual MCP config per server** | No centralized discovery, OAuth brokerage, or publisher analytics |
| **Zapier / Make** | Human-centric automation; not MCP-first or LLM client-native |
| **Single-vendor MCP** | One integration surface; Smithery aggregates many independent MCP publishers |

---

## Use Cases

- **Coding agents** — add Notion, Slack, GitHub, Drive, etc. via one registry
- **Research agents** — discover search and doc MCPs without custom Docker per tool
- **Enterprise pilots** — evaluate many MCP servers before standardizing allowlists
