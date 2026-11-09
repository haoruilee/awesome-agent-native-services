# three.ws

> **"The 3D Agent Layer of the Internet"**

| | |
|---|---|
| **Website** | https://three.ws |
| **Docs** | https://three.ws/grok · https://three.ws/grok-skill.md · https://three.ws/connect · https://three.ws/docs/grok-bot.md |
| **GitHub** | https://github.com/nirholas/three.ws |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/nirholas/three.ws?style=social)](https://github.com/nirholas/three.ws) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | Apache-2.0 (public repository) |
| **Verified at** | 2026-11-07 |
| **Latest-month signal** | Homepage "three.ws: The 3D Agent Layer of the Internet" HTTP 200. `https://three.ws/grok-skill.md` HTTP 200. Grok-dedicated MCP `https://three.ws/api/mcp-grok` answered HTTP 405 on bare GET (expected for Streamable HTTP). Repo Apache-2.0 with description "Give your AI agent a 3D body…" |

---

## Official Website

https://three.ws

three.ws is a 3D layer for AI agents: forge textured models from text or photos, rig avatars, search a CC0 catalog, embed agents, and (when signed in) run agent memory/skills plus read-only Solana market intel. A dedicated free MCP endpoint is documented for Grok Bot.

---

## Official Repo

https://github.com/nirholas/three.ws

Apache-2.0. Repository description: "Give your AI agent a 3D body: text or a photo to a rigged GLB avatar, an LLM brain, a Solana wallet and a one-tag embed. Keyless MCP server for Claude, Cursor and Codex."

---

## How to Use (Agent Onboarding)

**Interaction pattern:** Remote MCP (+ Grok skill URL)

Grok Bot / Grok custom connector (Streamable HTTP; free studio needs no auth):

```
https://three.ws/api/mcp-grok
```

Skill file for Grok / Grok Bot:

```
Read https://three.ws/grok-skill.md and follow the instructions.
```

Setup guide: https://three.ws/grok · Connector reference: https://three.ws/docs/grok-bot.md

Signed-in agent/memory/market tools use the same URL with OAuth or a connector API key (`?auth=oauth` documented on the Grok pages).

---

## Agent Skills

**Status:** ✅ Hosted skill document for Grok / Grok Bot

```
https://three.ws/grok-skill.md
```

| Skill | What It Teaches the Agent |
|---|---|
| `grok-skill.md` | Connector URL, runnable calls, result links, free limits, and the rule that the free Grok connector never spends |

Grok Build plugin path under `integrations/grok/three-ws` is documented on https://three.ws/grok (clone sparse checkout into `~/.grok/plugins/`).

---

## MCP

**Status:** ✅ Available — Grok-dedicated remote endpoint

| Detail | Value |
|---|---|
| **Endpoint** | `https://three.ws/api/mcp-grok` |
| **Transport** | Streamable HTTP |
| **Auth** | None required for free 3D forge / catalog / look-at tools; OAuth or connector key for agent/memory/market tools |
| **Documented free tools** | `forge_free`, `mesh_forge`, `look_at_model`, `refine_model`, `forge_avatar`, `rig_mesh`, `create_agent_persona`, `persona_say`, `search_catalog`, `get_catalog_item`, `get_item_source`, job polling helpers |
| **Signed-in extras** | Agent create/call/memory/skills; read-only Solana market tools (docs state Grok never gets a tool that spends) |
| **Compatible clients** | Explicit Grok Bot + grok.com connector docs; also Claude/Cursor/Codex connect pages |

---

## What It Does

three.ws gives agents a 3D studio and optional body: generate a textured GLB + viewer link from a prompt, rig a humanoid avatar, search ready-made CC0 assets, and create a speaking persona. Long GPU jobs return within a short timeout with a job id for `check_job` polling so agent tasks do not hang. Signed-in surfaces add agent runtime (memory, skills) and read-only market intel; spending tools are excluded from the Grok connector per product docs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: "The 3D Agent Layer of the Internet"; repo: "Give your AI agent a 3D body"; dedicated Grok Bot page — [three.ws](https://three.ws/) · [grok](https://three.ws/grok) · [nirholas/three.ws](https://github.com/nirholas/three.ws) |
| **Agent-specific primitive** | `forge_free` / `forge_avatar` returning viewer+GLB for agents; `create_agent_persona` + `persona_say`; job-id polling contract for cold GPUs; Grok-only MCP that never exposes spend tools |
| **Autonomy-compatible control plane** | Free tools need no account; agent can forge → poll → look_at_model in a loop. Signed-in agent tools similarly tool-driven |
| **M2M integration surface** | Remote MCP, grok-skill.md, xAI Responses API MCP example, Grok Build `.mcp.json` |
| **Identity / delegation** | Free path is keyless per session quotas; signed-in OAuth/connector key scopes agent/memory tools; docs state the Grok connector never receives spending tools |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **forge_free / mesh_forge** | Text/photo → textured 3D model with viewer link and GLB |
| **forge_avatar / rig_mesh** | Humanoid → animation-ready avatar |
| **create_agent_persona / persona_say** | Named body with lip-sync speech |
| **search_catalog** | CC0 props/characters/motions before generating |
| **check_job / look_at_model** | Async job collect + visual QA from the agent |

---

## Autonomy Model

1. Add `https://three.ws/api/mcp-grok` (Grok Bot Plugins / custom connector) or read `https://three.ws/grok-skill.md`.
2. Agent calls `forge_free` or catalog search; on pending, polls job status.
3. Agent returns viewer/GLB/poster links to the user or attaches them to a later step.
4. Optional OAuth unlocks agent runtime and read-only market briefs without spend tools on the Grok connector.

---

## Identity and Delegation Model

- Free forge/catalog tools are keyless with per-session quotas documented for Grok cloud IPs.
- OAuth / connector keys unlock agent and market tools; Grok connector is documented to exclude spending tools.
- Personas are named bodies the agent can reuse across tasks.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP (Grok) | https://three.ws/api/mcp-grok |
| Skill | https://three.ws/grok-skill.md |
| Docs | https://three.ws/grok · https://three.ws/docs/grok-bot.md · https://three.ws/connect |
| Repo | https://github.com/nirholas/three.ws |

---

## Human-in-the-Loop Support

Free 3D tools need no human click after the connector is added. Signed-in agent features need one OAuth/key. Market tools are read-only on the Grok connector (no buy/sell).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A human Blender / Unity workflow** | Desktop DCC for people; no remote MCP forge/persona contract for Grok Bot |
| **A generic image API** | Returns 2D pixels; not textured GLB + viewer + agent persona primitives |
| **A Solana trading bot** | three.ws Grok market tools are explicitly read-only intel, not an execution venue |

---

## Use Cases

- **Asset for a page** — agent forges a model and returns embed/viewer/GLB
- **Avatar from a photo** — rig + persona that lip-syncs a greeting
- **Catalog-first packs** — search CC0 props, generate only gaps
- **Grok Bot routines** — daily 3D brief or hourly read-only market brief via MCP prompts
