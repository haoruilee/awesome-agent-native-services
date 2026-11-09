# Mobbin

> **"The Design MCP Server for AI Agents"**

| | |
|---|---|
| **Website** | https://mobbin.com/mcp · https://mobbin.com |
| **Docs** | https://docs.mobbin.com/mcp/introduction |
| **GitHub** | https://github.com/mobbin/skills (official Agent Skills + client plugins; MCP is hosted) · [![GitHub Stars](https://img.shields.io/github/stars/mobbin/skills?style=social)](https://github.com/mobbin/skills) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | Hosted commercial product (Pro / Team / Enterprise); skills repo is public |
| **Verified at** | 2026-11-08 |
| **Latest-month signal** | `https://mobbin.com/mcp` og:title "Mobbin MCP: The Design MCP Server for AI Agents" HTTP 200. `https://docs.mobbin.com/llms.txt` HTTP 200. Remote MCP `https://api.mobbin.com/mcp` answered HTTP 401 without auth (OAuth-protected Streamable HTTP, expected). Official skills at `npx skills add mobbin/skills`. Dedicated Grok Bot / Cursor Marketplace plugin docs live |

---

## Official Website

https://mobbin.com/mcp

Mobbin MCP is Mobbin's hosted design MCP server: AI assistants and coding agents search **600,000+ shipped product screens**, multi-step flows, and website sections with natural language, then save references into collections. The human Mobbin library remains at https://mobbin.com; the agent-native surface catalogued here is MCP + skills + the documented search API.

---

## Official Repo

https://github.com/mobbin/skills

Official Agent Skills pack and per-client plugins (Cursor, Claude, Codex, Grok, Gemini, Antigravity, Kimi, …). The MCP server itself is hosted at `https://api.mobbin.com/mcp` (nothing to clone for the server). GitHub MCP Registry entry: https://github.com/mcp/com.mobbin/mobbin

---

## How to Use (Agent Onboarding)

**Interaction pattern:** Remote MCP (OAuth) + Agent Skills / marketplace plugins

Remote MCP (Streamable HTTP; OAuth through the user's Mobbin account — no manual API key for MCP):

```
https://api.mobbin.com/mcp
```

Cursor / generic MCP config:

```json
{
  "mcpServers": {
    "mobbin": {
      "url": "https://api.mobbin.com/mcp"
    }
  }
}
```

Claude Code:

```bash
claude mcp add --transport http mobbin https://api.mobbin.com/mcp
```

Skills (skills-only; still add MCP URL for tools):

```bash
npx skills add mobbin/skills
```

Preferred where available: install the official plugin (bundles skills + MCP) — Codex / Claude Code / Antigravity / Gemini / Grok Bot Marketplace. Grok Bot: Plugins → Mobbin → Authenticate — [docs](https://docs.mobbin.com/mcp/clients/grok-bot).

Requires a **Pro, Team, or Enterprise** Mobbin plan. Rate limit: 60 requests / 60 seconds / user. Docs index: https://docs.mobbin.com/llms.txt

---

## Agent Skills

**Status:** ✅ Published

```bash
npx skills add mobbin/skills
```

| Skill | Useful for |
|---|---|
| `best-practices` | What Mobbin / MCP can and cannot do; how skills compose |
| `search` | Choosing screens vs flows vs sections, query writing, recovery |
| `redesign-screen` | Redesign / rebuild grounded in shipped Mobbin references |
| `plain-writing` | Writing rules for text Mobbin skills hand to a person |

Plugin marketplaces (Claude, Codex, Antigravity, Gemini, Cursor/Grok, …) install skills together with the MCP server — [mobbin/skills README](https://github.com/mobbin/skills).

---

## MCP

**Status:** ✅ Available — remote Streamable HTTP, OAuth

| Detail | Value |
|---|---|
| **Endpoint** | `https://api.mobbin.com/mcp` |
| **Transport** | Streamable HTTP |
| **Auth** | OAuth via the user's Mobbin account (browser consent on first connect); no manually copied API key for MCP |
| **Plans** | Pro, Team, Enterprise |
| **Rate limit** | 60 requests per 60 seconds per user |
| **Search tools** | `search_screens`, `search_flows`, `search_sections` |
| **Saved tools** | `list_collections`, `get_collection_contents`, `create_collection`, `save_content`, `add_comment` |
| **Results** | Low-res inline previews for the model + high-res `image_url` (expire after 30 days) + `mobbin_url` citations; MCP Apps interactive gallery in supported clients |
| **Compatible clients** | Documented for Claude, ChatGPT, Codex, Cursor, Grok Bot, Figma agent, v0, Lovable, VS Code, Gemini CLI, and others — [clients overview](https://docs.mobbin.com/mcp/clients/overview) |

---

## What It Does

Mobbin MCP turns Mobbin's catalog of real iOS/web UI screens, multi-step flows, and website sections into tools an agent can call mid-build. Agents search in natural language, inspect inline preview images, cite `mobbin_url` links, export crisp assets from `image_url`, and manage private collections with comments. Official skills teach search hygiene and redesign workflows so coding/design agents ground UI in shipped product patterns instead of inventing placeholder layouts.

Honesty: the classic Mobbin website is still a human design library. What qualifies here is the **first-party agent surface** (remote MCP, OAuth, agent-oriented tool schemas, skills, docs `llms.txt`, and search API) — not a claim that every Mobbin web feature was rebuilt for agents.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | MCP product page og:title / positioning: **"Mobbin MCP: The Design MCP Server for AI Agents"**; H1 frames connecting **AI agents** to 600k+ screens — [mobbin.com/mcp](https://mobbin.com/mcp) |
| **Agent-specific primitive** | NL search tools that return **inline images sized for model consumption**, `task_intent` / `output_destination` parameters, MCP Apps gallery, and skills that load redesign/search playbooks — not a human SERP dump |
| **Autonomy-compatible control plane** | After one OAuth approval, agents search, page, save, and comment without per-action human clicks; rate limits and plan gates bound runaway loops |
| **M2M integration surface** | Hosted remote MCP, REST search API + OpenAPI, `docs.mobbin.com/llms.txt`, installable skills/plugins |
| **Identity / delegation** | OAuth ties the MCP session to the signed-in Mobbin user; saves/comments run under that account's permissions; comments record which client app posted. Not a separate KYA agent wallet — delegated user OAuth (same class as other catalogued remote MCPs) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **search_screens** | Natural-language search over individual mobile/web UI screens |
| **search_flows** | Ordered multi-step journeys (onboarding, checkout, KYC, …) |
| **search_sections** | Website composition blocks (hero, pricing, footer, …) |
| **collections + save_content** | Private/team collections agents create and fill |
| **add_comment** | Notes on screens/flows/sections visible to the team |
| **Agent Skills pack** | `best-practices`, `search`, `redesign-screen`, `plain-writing` |

---

## Autonomy Model

1. Human connects Mobbin MCP once (plugin or MCP URL) and completes OAuth on a paid plan.
2. Agent chooses `search_screens` / `search_flows` / `search_sections` from the task.
3. Agent reads inline previews, cites `mobbin_url`, optionally downloads `image_url` for code/Figma/docs.
4. Agent may `create_collection` / `save_content` / `add_comment` without further UI clicks.
5. Rate limit (60/60s) and plan entitlement stop unbounded loops.

---

## Identity and Delegation Model

- **OAuth to Mobbin user account** — agent acts with the signed-in member's library and collection permissions.
- **No separate agent KYA credential** documented; attribution is via the OAuth connection and client app noted on comments.
- **Revoke** documented at https://docs.mobbin.com/mcp/disconnect — human can cut delegated access.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | `https://api.mobbin.com/mcp` (Streamable HTTP + OAuth) |
| Docs / llms.txt | https://docs.mobbin.com/llms.txt |
| REST search | Documented under https://docs.mobbin.com/api/quickstart · OpenAPI https://docs.mobbin.com/openapi.json |
| Skills / plugins | `npx skills add mobbin/skills` · https://github.com/mobbin/skills |
| Product page | https://mobbin.com/mcp |

---

## Human-in-the-Loop Support

Plan purchase, first OAuth consent, and access revoke are human. Ongoing search/save/comment loops run autonomously inside plan and rate limits. Teams can review saved collections and comments on the Mobbin website.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Manual screenshot paste into chat** | Breaks autonomy; no structured ids, collections, or high-res export contract |
| **Generic image search / web scrape** | Not shipped-product UI flows with Mobbin metadata, patterns, or OAuth-scoped saves |
| **Human-only Mobbin web UI** | Requires clicking the library; no MCP tool loop for coding agents |
| **Raw Figma file alone** | One product's draft; Mobbin MCP supplies **cross-product shipped** references agents can search |

---

## Use Cases

- **Ground UI generation** — pull real paywalls/onboarding before an agent writes React/Swift/HTML
- **Pattern research** — compare how fintech/social apps handle empty states, permissions, KYC
- **Ticket-linked references** — agents attach Mobbin screens to design/engineering tasks
- **Collection curation** — build private reference sets and comment rationale for teammates
