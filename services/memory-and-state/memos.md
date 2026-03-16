# MemOS

> **"A memory OS for LLM and AI agent systems."**

| | |
|---|---|
| **Website** | https://openmem.net |
| **Docs** | https://memos-docs.openmem.net |
| **GitHub** | https://github.com/MemTensor/MemOS |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/MemTensor/MemOS?style=social)](https://github.com/MemTensor/MemOS) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Apache 2.0 |
| **Publisher** | MemTensor / OpenMem |

---

## Official Website

https://openmem.net

---

## Official Repo

https://github.com/MemTensor/MemOS

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / REST`

```bash
pip install memos-core

# Configure and start MemOS
from memos import MemOS
memory = MemOS(config="~/.memos/config.yaml")

# Add a memory from agent session
memory.add("User prefers Python over TypeScript for new projects")

# Retrieve relevant memories before agent responds
results = memory.get("user coding preferences")
```

---

## Agent Skills

**Status:** ✅ Official OpenClaw plugin available

```bash
# Install via OpenClaw plugin
npx playbooks add skill openclaw/skills --skill memos
```

| Skill | What It Teaches the Agent |
|---|---|
| `memos` | Add, retrieve, update memories using the MemCube model; use parametric/activation/plaintext memory types; integrate with OpenClaw sessions |

---

## MCP

**Status:** ✅ Available

MemOS exposes its memory operations through an MCP server.

| Detail | Value |
|---|---|
| **MCP Docs** | https://memos-docs.openmem.net/open_source/home/architecture |
| **Transport** | stdio / HTTP |
| **Compatible Clients** | Claude Code, Cursor, OpenClaw, any MCP-compatible client |

---

## What It Does

MemOS is a **memory operating system** — it manages memory as a system resource for AI agents the way an OS manages memory for processes. Rather than treating agent memory as a simple key-value store or vector database, MemOS unifies three fundamentally different types of memory under one API:

- **Parametric memory** — knowledge embedded in model weights
- **Activation memory** — precomputed KV-caches and hidden states for fast context retrieval
- **Plaintext memory** — searchable, editable text, documents, and graph nodes

The basic unit is the **MemCube**: a composable memory object with content, provenance, versioning, and lifecycle metadata. MemCubes can be composed, migrated, and fused as the agent accumulates knowledge.

**MemOS v2.0 benchmark (March 2026):** +43.70% accuracy vs. OpenAI Memory, 35.24% token savings.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | *"Memory OS for LLM and Agent systems"* — memory management for agents is the entire product, not a feature |
| **Agent-specific primitive** | **MemCube** — composable memory objects with provenance, versioning, and lifecycle; three distinct memory types (parametric/activation/plaintext) that reflect how agents actually reason |
| **Autonomy-compatible control plane** | **MemScheduler** runs memory operations asynchronously with millisecond-level latency; agents query without human curation |
| **M2M integration surface** | Python SDK (`pip install memos-core`), REST API, MCP server, OpenClaw plugin |
| **Identity / delegation** | Per-agent memory namespacing; memory provenance tracks which agent created which MemCube |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **MemCube** | Composable memory unit with content, provenance, version history, and lifecycle metadata |
| **Parametric Memory** | Knowledge embedded in model weights for stable domain expertise |
| **Activation Memory** | Precomputed KV-cache and hidden states for sub-millisecond context retrieval |
| **Plaintext Memory** | Searchable, editable text and graph nodes — the most common type |
| **MemScheduler** | Async memory operation scheduler with millisecond-level latency |
| **Memory Feedback** | Refine stored memories through natural-language correction |
| **Multi-modal Support** | Natively handles text, images, tool traces, and agent personas |
| **Unified Memory API** | Single interface: add, retrieve, edit, delete across all memory types |

---

## Autonomy Model

```
Agent receives task
    ↓
memory.get("relevant context query") → MemOS retrieves across all 3 memory types
    ↓
Agent reasons with retrieved MemCubes
    ↓
Agent completes task
    ↓
memory.add(new_learning) → MemScheduler processes asynchronously
    ↓
MemCube composed, provenance recorded, versioning updated
    ↓
Next session: agent starts with accumulated structured memory, not empty context
```

---

## Identity and Delegation Model

- Memory is namespaced per agent instance
- Every MemCube carries provenance: which agent created it, when, from what source
- Memory feedback allows the agent to self-correct stored knowledge
- MemCubes can be migrated between agents (knowledge transfer)

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install memos-core` |
| REST API | Full memory CRUD and retrieval |
| MCP Server | stdio / HTTP |
| OpenClaw Plugin | `MemOS-Cloud-OpenClaw-Plugin` at github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin |

---

## Human-in-the-Loop Support

None required. Memory operations run asynchronously. Memory feedback API lets agents self-correct without human intervention.

---

## How MemOS Differs from Mem0, Zep, and OpenViking

| Dimension | Mem0 | Zep | OpenViking | MemOS |
|---|---|---|---|---|
| Memory model | Extraction (text) | Temporal graph (text) | Filesystem (text+resources+skills) | **OS model (parametric+activation+plaintext)** |
| Activation memory | No | No | No | **Yes — KV-cache and hidden states** |
| Unit of memory | Fact/memory item | Knowledge graph node | File node (L0/L1/L2) | **MemCube (composable, versioned)** |
| Memory composition | No | No | No | **Yes — MemCubes can be fused and migrated** |

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Redis** | Key-value store; no memory type model, no provenance, no async scheduler |
| **Vector database** | Handles plaintext only; no parametric or activation memory |
| **OpenAI Memory** | Black box; +43.7% accuracy gap vs. MemOS; no MemCube model |
| **Mem0** | Extraction-based text memory only; no activation memory, no MemCube composability |

---

## Use Cases

- **Long-running coding agents** — parametric memory stores domain expertise; activation memory provides sub-ms context retrieval; plaintext stores project-specific notes
- **Personal assistants** — MemCubes accumulate user preferences with provenance and versioning across months
- **Research agents** — multi-modal MemCubes capture text findings, image analysis, and tool call traces from experiments
- **Multi-agent systems** — MemCubes migrated between specialist agents for knowledge transfer
