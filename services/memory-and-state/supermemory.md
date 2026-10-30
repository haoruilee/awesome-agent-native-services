# Supermemory

> **"The Memory API for the AI era."**

| | |
|---|---|
| **Website** | https://supermemory.ai |
| **Docs** | https://supermemory.ai/docs |
| **GitHub** | https://github.com/supermemoryai/supermemory |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/supermemoryai/supermemory?style=social)](https://github.com/supermemoryai/supermemory) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push 2026-10-29 ([repo metadata](https://api.github.com/repos/supermemoryai/supermemory)); ~31k stars |
| **Verified at** | 2026-10-30 |

---

## Official Website

https://supermemory.ai

GitHub description: **"Memory and context engine + app that is extremely fast, scalable, and can be run fully locally. The Memory API for the AI era."** MCP docs: **"Give every MCP-compatible assistant shared memory, team spaces, and interactive workflows."**

---

## Official Repo

https://github.com/supermemoryai/supermemory (MIT; monorepo with the engine, MCP server, apps, and `skills/`)

---

## How to Use (Agent Onboarding)

**Interaction pattern:** Remote MCP + REST API / SDK

```json
{ "mcpServers": { "supermemory": { "url": "https://mcp.supermemory.ai/mcp" } } }
```

The client opens an OAuth page once; the owner picks which spaces the client may read or write. No API key is required for MCP. For programmatic use, the Memory API and SDKs take an API key.

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ The repository ships a `skills/` directory; no single published `npx skills add` command is documented on the MCP page.

---

## MCP

**Status:** ✅ Available — hosted remote MCP (Streamable HTTP) with OAuth.

| Detail | Value |
|---|---|
| **Endpoint** | `https://mcp.supermemory.ai/mcp` |
| **Auth** | OAuth with per-client space scoping |
| **Tools** | `search_memory`, `get_profile`, `add_memory`, `forget_memory`, `list_documents`, `get_document`, `list_memories`, `list_spaces`, `who_am_i` |
| **MCP Apps widgets** | `select-space`, `guided-save`, `upload-file`, `memory-graph` |
| **Resources / prompts** | `supermemory://profile`, `supermemory://spaces`, `context` prompt |

---

## What It Does

Supermemory is a memory and context engine for AI assistants and agents. Agents save facts and documents, the engine extracts versioned memories, and later sessions (in any MCP client) recall them by semantic search or a stable profile. Spaces keep each project's memories separate, so a single agent or a team of assistants can share context without mixing unrelated work.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Give every MCP-compatible assistant shared memory…" — [MCP docs](https://supermemory.ai/docs/supermemory-mcp/introduction) |
| **Agent-specific primitive** | `add_memory` / `search_memory` / `forget_memory` with extracted, versioned memories; `get_profile` context for the active space; `context` prompt to prime a new session |
| **Autonomy-compatible control plane** | After the one-time OAuth grant the assistant picks tools itself; writes are scoped to granted spaces; `guided-save` is an optional review step |
| **M2M integration surface** | Remote MCP, Memory REST API, SDKs |
| **Identity / delegation** | Each connected app gets its own grant (scope + spaces); `who_am_i` reports identity, role and scope; access is edited or revoked per app on the console Agents page |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Memory write / forget** | `add_memory`, `forget_memory` (by id or exact content) |
| **Semantic recall** | `search_memory` returns memories with source document ids |
| **Profile** | `get_profile` — stable + recent facts for a space |
| **Spaces** | Namespaced memory per project/team, active-space switching |
| **Documents** | Upload and read source material behind memories |

---

## Autonomy Model

```
Owner connects MCP once (OAuth, picks spaces)
    -> Agent calls get_profile / search_memory at session start
    -> Agent calls add_memory after useful work
    -> Next session or a different AI client recalls the same space
```

---

## Identity and Delegation Model

- **Per-client grant:** each MCP client is an app with its own scope and space list.
- **Space isolation:** reads and writes default to the active space; `namespace` targets another permitted space.
- **Revocation:** "Disconnect memory" on the console Agents page revokes a client.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Remote MCP | `https://mcp.supermemory.ai/mcp` |
| REST API / SDKs | https://supermemory.ai/docs |
| Self-host | MIT monorepo, can run fully locally |

---

## Human-in-the-Loop Support

Optional: the `guided-save` widget lets a person edit a memory before it is stored, and the console shows and revokes app access. Not required for the agent loop.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A vector database** | Stores embeddings; no memory extraction, profile, forgetting, or MCP tool contract |
| **Notes apps** | Built for people; no per-agent grant or recall tools |

---

## Use Cases

- **Cross-assistant memory** — same project context in Claude, ChatGPT, Cursor
- **Team spaces** — shared, permissioned knowledge for several agents
- **Long-running agents** — profile + recall instead of re-sending history
