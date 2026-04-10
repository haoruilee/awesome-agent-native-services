# Arcade

> **MCP tools with managed OAuth — credentials stay out of the LLM.**

| | |
|---|---|
| **Website** | https://www.arcade.dev |
| **Docs** | https://docs.arcade.dev |
| **GitHub** | https://github.com/ArcadeAI/arcade-mcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/ArcadeAI/arcade-mcp?style=social)](https://github.com/ArcadeAI/arcade-mcp) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |

---

## Official Website

https://www.arcade.dev

---

## Official Repo

https://github.com/ArcadeAI/arcade-mcp — framework to build, deploy, and share MCP servers with OAuth and secret isolation

---

## How to Use (Agent Onboarding)

**Arcade CLI — scaffold an MCP server with authorized tool calling.**

```bash
uv tool install arcade-mcp
arcade new my_server
```

Follow [build MCP server](https://docs.arcade.dev/en/guides/create-tools/tool-basics/build-mcp-server) and [authorized tool calling](https://docs.arcade.dev/en/guides/tool-calling/custom-apps/auth-tool-calling) guides. Pre-built integrations (GitHub, Slack, Gmail, etc.) ship with **managed OAuth**.

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official `npx skills add ArcadeAI/...` bundle located.

```bash
npx clawhub@latest search arcade mcp
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Arcade *is* an MCP authoring and hosting platform

| Detail | Value |
|---|---|
| **Framework repo** | https://github.com/ArcadeAI/arcade-mcp |
| **Docs** | https://docs.arcade.dev/en/mcp-servers |
| **Transport** | stdio / hosted MCP per deployment |
| **Compatible Clients** | Claude Desktop, Cursor, OpenAI Agents, Google ADK, Vercel AI, Mastra, CrewAI (per Arcade docs) |

---

## What It Does

Arcade helps teams ship **production MCP servers** where tools call third-party APIs with **OAuth on behalf of end users**, while **secrets and tokens never enter the LLM context**. Docs emphasize **user-facing agents**, **authorized tool calling**, and **SSO for AI agents** — bridging agent intent, user consent, and least-privilege API access.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Blog and guides center **AI agents**, **MCP tools**, and **agent authentication** ([Arcade docs](https://docs.arcade.dev), [SSO for AI Agents](https://arcade.dev/blog/sso-for-ai-agents-authentication-and-authorization-guide)) |
| **Agent-specific primitive** | **Authorized tool calling** — runtime intersection of *what the agent may do* and *what the user delegated*; **credential isolation from the model** |
| **Autonomy-compatible control plane** | After OAuth consent, agents invoke tools without repeated human clicks; tokens refresh server-side |
| **M2M integration surface** | MCP protocol, Arcade Cloud APIs, CLI |
| **Identity / delegation** | Per-user OAuth connections; audit via Arcade/tool logs; secrets kept server-side |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **MCP tool with OAuth** | Tool definition + managed auth flow |
| **Authorized tool call** | Policy checks before execution |
| **Secret storage** | API keys and tokens hidden from LLM and client |
| **Pre-built integrations** | GitHub, Slack, Google, Salesforce, etc. |

---

## Autonomy Model

1. Human completes OAuth once per user/tool (or via enterprise SSO).
2. Agent plans a task and selects MCP tools.
3. Arcade evaluates authorization and injects credentials server-side.
4. Tool executes; results return to the agent without exposing secrets.

---

## Identity and Delegation Model

- **User identity** from IdP / OAuth.
- **Agent** acts through MCP with bounded tool allowlists.
- **Arcade** stores refresh tokens and performs refresh without model visibility.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | Primary agent integration |
| Arcade CLI | `arcade new`, deploy, local dev |
| HTTP APIs | Arcade Cloud for hosted servers |

---

## Human-in-the-Loop Support

- Initial OAuth / SSO consent is user-driven (appropriate for user-delegated tools).
- High-risk actions can still be gated by application policy outside Arcade.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw API keys in prompts** | Violates secret isolation; not safe for user-facing agents |
| **Generic iPaaS** | Not MCP-native; not built around LLM tool calls and token isolation |

---

## Use Cases

- **User-facing copilots** — Gmail, Calendar, CRM tools via MCP with OAuth.
- **Enterprise agents** — SSO-backed tool access with audit trails.
- **Custom MCP** — fastest path from Python tool code to deployed MCP with auth.
