# OpenViking

> **"The context database for AI agents."**

| | |
|---|---|
| **Website** | https://openviking.ai |
| **Docs** | https://openviking.ai/docs |
| **GitHub** | https://github.com/volcengine/OpenViking |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Apache 2.0 |
| **GitHub Stars** | 11,800+ |
| **Publisher** | Volcengine (ByteDance) |

---

## Official Website

https://openviking.ai

---

## Official Repo

https://github.com/volcengine/OpenViking — Core platform (Python + Rust + Go)

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / REST` + MCP

```bash
# Install
pip install openviking --upgrade

# Configure (create ~/.openviking/ov.conf with your VLM + embedding keys)
# Then start the server
openviking-server

# Agent connects via MCP (recommended for Claude Code / Cursor)
claude mcp add --transport http openviking http://localhost:8000/mcp

# Or ingest content and query via CLI
ov add ./my-project-docs
ov query "how does the authentication flow work"
```

The agent can then call `query`, `search`, and `add_resource` tools through MCP to manage its full context stack — memories, resources, and skills — without any manual curation.

---

## Agent Skills

**Status:** ✅ Official skills published by the OpenClaw community

```bash
# Install the MCP skill for OpenClaw / Claude Code
npx playbooks add skill openclaw/skills --skill openviking-mcp

# Or the general usage skill
npx playbooks add skill openclaw/skills --skill openviking
```

| Skill | What It Teaches the Agent |
|---|---|
| `openviking-mcp` | Set up and connect to the OpenViking MCP server; use `query`, `search`, `add_resource` tools |
| `openviking` | Filesystem paradigm (`viking://` URIs), tiered context loading (L0/L1/L2), session memory management |
| `adding-resource` | Ingest files, directories, and URLs into the context database |

**Compatibility:** Claude Code, Cursor, OpenCode, and all MCP-compatible clients.

---

## MCP

**Status:** ✅ Available

OpenViking runs an HTTP MCP server that exposes the full context database as three tools.

```bash
# Start OpenViking MCP server
openviking-server  # runs at http://127.0.0.1:8000/mcp by default

# Connect from Claude Code
claude mcp add --transport http openviking http://localhost:8000/mcp

# Or add to claude_desktop_config.json for Claude Desktop
```

| Detail | Value |
|---|---|
| **MCP Transport** | HTTP (StreamableHttp) |
| **Default Endpoint** | `http://127.0.0.1:8000/mcp` |
| **MCP Tools** | `query` (RAG pipeline), `search` (semantic search), `add_resource` (ingest) |
| **Community MCP** | https://playbooks.com/mcp/fencith/openviking-mcp |
| **Compatible Clients** | Claude Code, Cursor, Claude Desktop, any MCP-compatible client |

---

## What It Does

OpenViking is an open-source **context database** — a unified filesystem for everything an AI agent needs to know: its own accumulated experience (`viking://agent/`), user preferences (`viking://user/`), and external resources (`viking://resources/`).

Instead of managing memory in one system, resources in a vector store, and skills in another, OpenViking maps all three to a hierarchical `viking://` virtual filesystem. Agents navigate it with `ls` and `find` — exactly like a developer navigates a project directory. Each node has L0/L1/L2 tiered content: a one-sentence abstract for quick routing, an overview for planning, and full content for deep reasoning — loaded on demand to reduce token cost by up to 91%.

The killer feature: **self-evolution**. At the end of each session, OpenViking asynchronously extracts agent experience from task execution and writes it to `viking://agent/memories/` — the agent accumulates operational knowledge without any human curation.

**Benchmark (LoCoMo10, 1540 long-range dialogue cases):**

| System | Task Completion | Input Tokens |
|---|---|---|
| OpenClaw (baseline) | 35.65% | 24.6M |
| OpenClaw + LanceDB | 44.55% | 51.6M |
| **OpenClaw + OpenViking** | **52.08%** | **4.3M** |

+49% task completion, -83% token cost versus baseline.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | GitHub: *"open-source context database designed specifically for AI Agents"*; `viking://agent/` namespace is a first-class entity distinct from `viking://user/` |
| **Agent-specific primitive** | `viking://agent/skills/`, `viking://agent/memories/`, `viking://agent/instructions/` — the agent has its own context namespace; self-evolution loop extracts agent experience autonomously; L0/L1/L2 tiered loading designed for agent reasoning cost |
| **Autonomy-compatible control plane** | Session memory extraction runs asynchronously at session end — agent accumulates knowledge without human curation; `query` / `search` called autonomously during reasoning |
| **M2M integration surface** | MCP server (HTTP StreamableHttp), Python SDK (`pip install openviking`), Rust CLI (`ov`), HTTP server, OpenClaw/OpenCode memory plugin |
| **Identity / delegation** | Separate namespaces: `viking://agent/` (agent's own experience), `viking://user/` (user preferences), `viking://resources/` (shared knowledge) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`viking://` Virtual Filesystem** | Hierarchical URI namespace unifying agent memories, user preferences, and resources |
| **`viking://agent/` Namespace** | The agent's own context space: skills, task memories, instructions — separate from the user's namespace |
| **L0/L1/L2 Tiered Context** | Abstract (L0, ~100 tokens) → Overview (L1, ~2k tokens) → Full content (L2) — loaded on demand |
| **Directory Recursive Retrieval** | Intent analysis → vector positioning → directory-level refinement → recursive drill-down |
| **Self-Evolution Loop** | Automatic async extraction of agent experience from task sessions into `viking://agent/memories/` |
| **Visualized Retrieval Trajectory** | Every retrieval's directory browsing path is preserved for debugging and optimization |
| **`query` Tool** | Full RAG pipeline: intent → retrieval → LLM answer generation |
| **`search` Tool** | Semantic search returning docs with relevance scores |
| **`add_resource` Tool** | Ingest files, directories, or URLs into the context database |

---

## Autonomy Model

```
Agent receives a task
    ↓
Agent calls MCP tool: query("how does authentication work")
    ↓
OpenViking: intent analysis → vector positioning in viking://resources/
    ↓
L0 abstract scan → L1 overview if promising → L2 full content if needed
    ↓
Returns structured answer with retrieval trajectory
    ↓
Agent completes task
    ↓
Session ends → OpenViking async extraction:
  - User preferences → viking://user/memories/preferences/
  - Agent operational tips → viking://agent/memories/
  - New skills discovered → viking://agent/skills/
    ↓
Next session: agent starts with accumulated experience, not from zero
```

---

## Identity and Delegation Model

- `viking://agent/` — the agent's own namespace; experience, skills, and instructions are owned by the agent instance
- `viking://user/` — user preferences and memories, separate from agent state
- `viking://resources/` — shared external knowledge (project docs, web pages, repos)
- Each node has a unique URI enabling deterministic access and audit
- Retrieval trajectories are preserved — every context decision is observable and reproducible

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP Server | HTTP StreamableHttp at `localhost:8000/mcp`; tools: `query`, `search`, `add_resource` |
| Python SDK | `pip install openviking` |
| Rust CLI | `curl ... | bash` (ov_cli); commands: `ov add`, `ov query`, `ov find`, `ov grep`, `ov ls` |
| HTTP REST | Direct API at `localhost:8000` |
| OpenClaw Plugin | Memory plugin for OpenClaw agents |
| OpenCode Plugin | Memory plugin for OpenCode agents |

---

## Human-in-the-Loop Support

None required. The self-evolution loop runs asynchronously. The visualized retrieval trajectory enables human review of what context was used and why — but the agent operates fully autonomously.

---

## How OpenViking Differs from Mem0, Zep, and Ensue

| Dimension | Mem0 | Zep | Ensue | OpenViking |
|---|---|---|---|---|
| Core model | Extraction-based memory | Temporal knowledge graph | Multi-agent shared workspace | **Context filesystem (agent OS)** |
| Scope | User ↔ agent (single pair) | User ↔ agent (temporal) | Many agents (shared) | **Agent + user + resources (unified)** |
| Agent namespace | No | No | Per-agent key prefix | **Dedicated `viking://agent/` namespace** |
| Resources / skills | No | No | No | **Yes — `viking://resources/`, `viking://agent/skills/`** |
| Self-evolution | Managed (ADD/UPDATE) | Temporal invalidation | Claim/publish | **Async extraction per session** |
| Retrieval | Semantic | Temporal graph | Semantic + hypothesis | **Directory recursive + L0/L1/L2 tiered** |

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Traditional RAG (LangChain, LlamaIndex)** | Flat vector storage; no agent-specific namespace; no tiered loading; no self-evolution; no visualized trajectory |
| **LanceDB / Chroma** | Vector databases; agents must build all extraction, routing, and lifecycle logic themselves |
| **Mem0** | Per-agent conversational memory only; no resource management, no skill namespace, no tiered loading |
| **Local file system + grep** | No semantic retrieval; no L0/L1/L2 tiering; no automatic session extraction; no `viking://` URI unification |

---

## Use Cases

- **Coding agents** — index a codebase into `viking://resources/my_project/`; agent queries it with directory-aware RAG; operational tips accumulated in `viking://agent/memories/` across sessions
- **Research agents** — ingest papers and web pages; agent traverses the knowledge hierarchy using L0 abstracts for routing before loading full content
- **Personal assistants** — user preferences stored in `viking://user/memories/preferences/`; agent skills and learned workflows in `viking://agent/skills/`
- **Long-running task agents** — task execution results and lessons extracted to agent memory automatically at session end
- **Multi-tool agents** — unified context layer beneath any agent framework (OpenClaw, OpenCode, LangChain, CrewAI) via MCP or Python SDK
