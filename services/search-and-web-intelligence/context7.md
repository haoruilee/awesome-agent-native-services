# Context7

> **"Up-to-date Docs for AI Agents"**

| | |
|---|---|
| **Website** | https://context7.com |
| **Docs** | https://context7.com/docs |
| **GitHub** | https://github.com/upstash/context7 |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/upstash/context7?style=social)](https://github.com/upstash/context7) |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence](README.md) |
| **License** | MIT (MCP server + `ctx7` CLI); hosted index is operated by Upstash |
| **Latest-month signal** | Last GitHub push 2026-10-29 ([repo metadata](https://api.github.com/repos/upstash/context7)); ~64k stars |
| **Verified at** | 2026-10-30 |

---

## Official Website

https://context7.com

README H1: **"Context7 - Up-to-date Docs for AI Agents"** — "Context7 pulls up-to-date, version-specific documentation and code examples straight from the source — and gives them to your coding agent."

---

## Official Repo

https://github.com/upstash/context7

---

## How to Use (Agent Onboarding)

**Interaction pattern:** Remote MCP or CLI + Skill

```bash
npx ctx7 setup            # OAuth, mints an API key, installs a skill or MCP config
# targets: --cursor, --claude, --opencode
```

Manual MCP: `https://mcp.context7.com/mcp` with `Authorization: Bearer <API_KEY>` (a free key raises rate limits).

---

## Agent Skills

**Status:** ✅ `ctx7 setup` installs a skill that tells the agent when and how to fetch docs with `ctx7` CLI commands (no MCP needed).

---

## MCP

**Status:** ✅ Available — hosted remote MCP and the MIT `@upstash/context7-mcp` package.

| Detail | Value |
|---|---|
| **Endpoint** | `https://mcp.context7.com/mcp` |
| **Package** | `@upstash/context7-mcp` (npm) |
| **Tools** | `resolve-library-id` (name → Context7 id), `query-docs` (version-aware docs + code snippets) |
| **Clients** | Claude, ChatGPT, Cursor, VS Code, OpenCode and other MCP clients |

---

## What It Does

Context7 indexes library and framework documentation and serves version-specific snippets to coding agents at the moment they write code, so the agent stops relying on stale training data or hallucinated APIs. Prompts can name a library id (`/supabase/supabase`) or a version and Context7 matches it.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Up-to-date Docs for AI Agents" — [README](https://github.com/upstash/context7) |
| **Agent-specific primitive** | Library-id resolution + token-budgeted, version-matched doc retrieval meant to be injected into an LLM context window |
| **Autonomy-compatible control plane** | After setup the agent calls the tools (or the skill triggers `ctx7`) on its own; API key gives rate limits, no per-call approval |
| **M2M integration surface** | Remote MCP, npm MCP server, `ctx7` CLI, Skill |
| **Identity / delegation** | Per-user API key minted by `ctx7 setup` (OAuth), sent as Bearer header |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`resolve-library-id`** | Maps a package name to a Context7 library id |
| **`query-docs`** | Returns current docs and code examples for that id/version |
| **Skill mode** | CLI + skill path for agents without MCP |

---

## Autonomy Model

```
Developer runs `npx ctx7 setup` once
    -> Agent hits a library question while coding
    -> Agent calls resolve-library-id, then query-docs
    -> Fresh snippets land in context; agent writes code
```

---

## Identity and Delegation Model

- **API key:** created through OAuth in `ctx7 setup`; scoped to the user's Context7 account and rate limits.
- **Read-only:** tools only read the public doc index; no write access to user systems.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Remote MCP | `https://mcp.context7.com/mcp` |
| npm | `@upstash/context7-mcp` |
| CLI | `ctx7` (`setup`, `remove`, doc queries) |
| Docs | https://context7.com/docs/resources/all-clients |

---

## Human-in-the-Loop Support

Not required. Library owners can add or claim docs on context7.com.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Web search** | Returns pages for people, not version-matched snippets sized for a context window |
| **Docs sites** | Built for human reading; no resolve/query tool contract |

---

## Use Cases

- **Coding agents on fast-moving frameworks** — Next.js, Supabase, Cloudflare Workers
- **Version pinning** — "Next.js 16 proxy" gets 16-era APIs
- **Agents without MCP** — skill + CLI path
