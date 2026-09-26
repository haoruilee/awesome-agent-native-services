# Memmy

> **"Memmy is your personal AI agent & local memory hub for all AI agents — it lets every AI connect to the same memory and keep self-evolving."**

| | |
|---|---|
| **Website** | https://memmy.bot/ |
| **Docs** | https://memmy.bot/docs/ |
| **GitHub** | https://github.com/MemTensor/memmy-agent |
| **Latest-month signal** | [v1.1.8](https://github.com/MemTensor/memmy-agent/releases/tag/v1.1.8) released 2026-09-23; 1,982 stars; license MIT; [memmy.bot](https://memmy.bot/) returned HTTP 200 on 2026-09-26 ([repo metadata](https://api.github.com/repos/MemTensor/memmy-agent)) |
| **Verified at** | 2026-09-26 |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MIT |

---

## Official Website

https://memmy.bot/

---

## Official Repo

https://github.com/MemTensor/memmy-agent

---

## How to Use (Agent Onboarding)

**Interaction pattern:** local daemon + JSON CLI / REST + installed Agent Skill

The upstream one-command source path starts the Memory service, Agent API, gateway, frontend, and desktop backend:

```bash
git clone https://github.com/MemTensor/memmy-agent.git && cd memmy-agent
cp .env.example .env
bash scripts/dev-start.sh

memmy-memory init
memmy-memory health
memmy-memory search "memory policies in this project"
```

The local Memory service defaults to `http://127.0.0.1:18960`. An external agent can then run a complete JSON-oriented memory loop:

```bash
memmy-memory session open --source codex --workspace-path "$PWD"
memmy-memory turn start --source codex --session-id "$SESSION_ID" --query "$USER_QUERY"
memmy-memory turn complete "$TURN_ID" --source codex --session-id "$SESSION_ID" \
  --query "$USER_QUERY" --answer "$FINAL_ANSWER" --status succeeded
```

See the official [Quick Start](https://github.com/MemTensor/memmy-agent/blob/main/README.md#quick-start) and [`memmy-memory` CLI guide](https://github.com/MemTensor/memmy-agent/blob/main/docs/en/memory/memory-cli.mdx).

---

## Agent Skills

**Status:** ✅ Available — bundled with the repository and rendered for supported external agents by Memmy; this is not published as an `npx skills add` package.

```bash
memmy-memory init
```

| Skill | What It Teaches the Agent |
|---|---|
| [`memmy-memory`](https://github.com/MemTensor/memmy-agent/blob/main/Memory/src/cli/skills/memmy-memory/SKILL.md) | Open/close memory sessions, retrieve context at turn start, persist completed turns, search, add, read, and delete durable memories with source attribution |
| [`agent-memory-onboarding`](https://github.com/MemTensor/memmy-agent/blob/main/App/memmy-agent/src/skills/agent-memory-onboarding/SKILL.md) | Verify an external agent installation, install a rendered Memmy Skill, import native history, persist an idempotent sync recipe, and validate readiness |

The upstream [Skills guide](https://github.com/MemTensor/memmy-agent/blob/main/docs/en/memory/skills.mdx) explains how Memmy writes the instruction file into an external agent's native rules/Skills directory.

---

## MCP

**Status:** ⚠️ No standalone MCP server is documented for the Memory service.

| Detail | Value |
|---|---|
| **Memmy's MCP role** | The Agent Runtime is an MCP **client** and can connect tools through MCP |
| **Memory integration** | External agents use the `memmy-memory` JSON CLI, installed Skill/hooks, or the local REST API |
| **Important distinction** | MCP tool support in the runtime does not make `http://127.0.0.1:18960` an MCP endpoint |

---

## What It Does

Memmy provides one local-first memory substrate shared by Codex, Claude Code, Cursor, OpenClaw, Hermes Agent, and other agent surfaces. Hooks, plugins, the desktop app, and the `memmy-memory` CLI all read and write the same SQLite-backed service, so context survives both session restarts and switches between agent products.

Its memory pipeline is more than storage. `turn.start` decides whether and what to recall; parallel vector, full-text, pattern, and structural channels retrieve candidates; fusion, thresholding, deduplication, MMR, and an optional LLM filter select context. `turn.complete` captures a raw turn and L1 traces, while background jobs summarize, reflect, score, embed, and evolve higher-level L2 policies, L3 world models, and callable Skills. The full lifecycle is documented in [How Memory Works](https://github.com/MemTensor/memmy-agent/blob/main/docs/en/memory/overview.mdx).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The official README calls Memmy a *"personal AI agent & local memory hub for all AI agents"* and says it lets every AI use the same evolving memory — [source](https://github.com/MemTensor/memmy-agent/blob/main/README.md#memmy-is-your-personal-ai-agent--local-memory-hub--for-all-ai-agents--it-lets-every-ai-connect-to-the-same-memory-and-keep-self-evolving) |
| **Agent-specific primitive** | Agent turns, tool traces, reflections, error signatures, source-agent identity, episode rollups, L2 procedures, L3 world models, and crystallized Skills are first-class memory types—not generic documents or vectors ([memory layers](https://github.com/MemTensor/memmy-agent/blob/main/docs/en/memory/overview.mdx#four-memory-layers)) |
| **Autonomy-compatible control plane** | Hooks/plugins invoke `turn.start` and `turn.complete`; recall and context injection happen automatically; background evolution is non-blocking; reads and writes can be independently enabled or disabled in policy ([request path](https://github.com/MemTensor/memmy-agent/blob/main/docs/en/memory/overview.mdx#the-complete-path-of-one-request)) |
| **M2M integration surface** | JSON CLI, bearer-protected local REST endpoints for sessions/turns/memory, external-agent Skills/hooks, and an OpenAI-compatible Agent API ([Memory Runtime API](https://github.com/MemTensor/memmy-agent/blob/main/docs/en/reference/memory-api.mdx)) |
| **Identity / delegation** | Calls can carry `--source`, `--user-id`, `sessionId`, and `turnId`; bearer/local tokens constrain callers; stored traces retain their source agent and turn status; Memory search/write logs expose attribution ([CLI](https://github.com/MemTensor/memmy-agent/blob/main/docs/en/memory/memory-cli.mdx), [security](https://github.com/MemTensor/memmy-agent/blob/main/docs/en/security/security.mdx)) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Shared Memory service** | Local SQLite-backed service used by every connected agent surface |
| **Session / turn lifecycle** | `sessions/open`, `turns/start`, `turns/:id/complete`, and `sessions/:id/close` bind recall and capture to agent work |
| **L1 Trace** | Requests, responses, tool calls/results, reflections, errors, status, and source attribution |
| **L2 Policy** | Procedures, triggers, boundaries, verification, and failure-avoidance guidance induced from valuable traces |
| **L3 World Model** | Stable knowledge about projects, environments, and constraints |
| **Skill memory** | Verified, callable procedures crystallized from agent experience |
| **Multi-channel recall** | Vector, FTS5, short-pattern, and structural-error retrieval followed by fusion, MMR, and optional LLM filtering |
| **History source onboarding** | Imports existing agent histories and saves validated automatic-sync recipes |
| **Memory audit views** | Search/write logs, candidates, filtered results, source memory IDs, evolution analytics, and memory management |

---

## Autonomy Model

```text
Operator starts the local Memory service and connects an agent once
    ↓
Agent hook/Skill opens or resumes a source-attributed Memmy session
    ↓
turn.start retrieves, filters, and injects relevant cross-agent context
    ↓
Agent performs its task without a per-memory human action
    ↓
turn.complete stores the result and tool trace
    ↓
Background jobs summarize, score, embed, deduplicate, and evolve memory
    ↓
Later sessions and other connected agents recall the evolved context
```

---

## Identity and Delegation Model

- **Calling agent attribution** — External agents pass a stable `source`; installed Skills are rendered for a specific source instead of treating every client as anonymous.
- **User and session namespaces** — `--user-id`, `sessionId`, and `turnId` separate the user scope and bind writes back to an execution episode.
- **Caller authorization** — Memory HTTP endpoints can require a bearer token; local desktop and bridge surfaces use separate local tokens.
- **Auditability** — L1 records retain tool, status, source, and error fields; search and write logs show candidates, selected source memories, and result status.
- **Boundary** — This is a local-first source/user/session credential model, not a hosted enterprise RBAC or approval service; operators must protect the local database and token at the OS boundary.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **Memory REST API** | Local HTTP at `127.0.0.1:18960`; health, sessions, turns, search/add/get/delete, panel, and analytics endpoints |
| **`memmy-memory` CLI** | JSON output; health, session, turn, search, add/get/delete, config reload, and raw calls |
| **Agent Skills / hooks** | Installs active memory instructions into external agent surfaces and mirrors turns automatically |
| **Agent API** | OpenAI-compatible local API on port `18990` when `memmy serve` runs |
| **Desktop / TUI** | Human management and local Agent Runtime entry points; not required for each memory operation after setup |

---

## Human-in-the-Loop Support

Normal recall, turn capture, indexing, and memory evolution run without per-action approval. Humans can inspect exact memory/search logs, give explicit feedback, delete incorrect memories, disable reads or writes independently, tune retrieval/evolution thresholds, and decide which external agent histories may be scanned. Memmy does not ship a mandatory approval gate for every memory write.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Vector database** | Stores and retrieves vectors but does not own agent turn capture, episodic reward, policy/world-model/Skill evolution, source-agent attribution, or context injection |
| **Per-agent transcript files** | Preserve one product's history but do not provide a shared, queryable lifecycle across Codex, Claude Code, Cursor, OpenClaw, and other agents |
| **Human note application** | Requires human curation and lacks autonomous `turn.start` recall, `turn.complete` trace capture, and machine-readable agent Skills/hooks |

---

## Use Cases

- **Cross-agent continuity** — Start research in Claude Code, continue in Codex, and retrieve the same decisions and project history
- **Long-horizon coding agents** — Preserve error signatures, successful procedures, tool outcomes, and unresolved follow-ups across sessions
- **Personal preference memory** — Distill stable user preferences once and reuse them across different agent runtimes
- **Experience-to-Skill evolution** — Turn rewarded traces into policies, world models, and callable procedures
- **Local/private memory infrastructure** — Keep the memory database and ingestion pipeline on the operator's own machine
