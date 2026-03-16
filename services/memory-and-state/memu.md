# memU

> **"Memory for 24/7 proactive AI agents."**

| | |
|---|---|
| **Website** | https://memu.pro |
| **Docs** | https://memu.pro/docs |
| **GitHub** | https://github.com/NevaMind-AI/memU |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | Open-source |
| **GitHub Stars** | 12,948+ |
| **Publisher** | NevaMind AI |

---

## Official Website

https://memu.pro

---

## Official Repo

https://github.com/NevaMind-AI/memU

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / REST`

```bash
pip install memu

# Initialize memory layer
from memu import MemU
memory = MemU(agent_id="my-agent")

# Continuous monitoring mode — for proactive 24/7 agents
memory.monitor(data_stream=my_stream, callback=on_relevant_event)

# Or: standard add/retrieve
memory.add(content="User has deadline on Friday")
context = memory.retrieve("user schedule and priorities")
```

---

## Agent Skills

**Status:** ⚠️ No official skill published yet.

```bash
npx clawhub@latest search memu memory
```

---

## MCP

**Status:** ⚠️ Not yet published as standalone MCP server.

Integration is via Python SDK and REST API. Community MCP wrappers may exist on ClawHub.

---

## What It Does

memU is a **persistent memory framework specifically built for 24/7 proactive AI agents** — agents that run continuously, monitor data streams, and act without explicit user commands. The critical insight: most agent memory systems are optimized for interactive sessions, but proactive agents need memory that works at *millisecond* latency while the agent is idle, only invoking expensive LLM reasoning when something truly relevant is detected.

memU solves this with **dual-mode retrieval**:
- **Fast Context (RAG mode)** — embedding-based monitoring running continuously, sub-millisecond latency, near-zero cost
- **Deep Reasoning (LLM mode)** — full LLM capabilities activated only when Fast Context detects a relevant pattern

The agent saves ~90% of token costs because expensive LLM reasoning only fires when the lightweight monitor says "this matters."

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | *"Memory for 24/7 proactive agents like openclaw"* — the 24/7 proactive agent use case is the entire design brief |
| **Agent-specific primitive** | **Dual-mode retrieval** (Fast Context + Deep Reasoning) — only meaningful for agents that run continuously; heartbeat monitoring; proactive intent capture without explicit commands |
| **Autonomy-compatible control plane** | Agents monitor streams and act without user prompts; Fast Context runs continuously at near-zero cost |
| **M2M integration surface** | Python SDK, REST API, OpenClaw integration; `v1.4.0` with 22 releases |
| **Identity / delegation** | Per-agent memory with bidirectional traceability — every knowledge item traces to its source |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Fast Context (RAG mode)** | Continuous embedding-based monitoring at millisecond latency — always-on, near-zero cost |
| **Deep Reasoning (LLM mode)** | Full LLM activation triggered only when Fast Context detects relevance |
| **Dual-mode Switch** | Automatic gate between fast and deep modes based on pattern detection |
| **Proactive Intent Capture** | Understands and stores user intent; agent can act without explicit commands |
| **Continuous Stream Monitoring** | Agent watches data streams (messages, events, feeds) and reacts when relevant patterns emerge |
| **Hierarchical Memory Structure** | Mount Points (raw data) → Files (facts/preferences/skills) → Folders (auto-organized topics) |
| **Bidirectional Traceability** | Every stored fact traces back to its source document and session |
| **Multimodal Support** | Handles text, images, audio, and video |

---

## Autonomy Model

```
memU Fast Context runs continuously in background (near-zero cost)
    ↓
Data stream arrives (message, email, calendar event, news feed…)
    ↓
Fast Context evaluates: is this relevant to the agent's goals/context?
    ├── NO → discard, continue monitoring
    └── YES → trigger Deep Reasoning (LLM mode)
              ↓
              LLM extracts meaning, updates memory hierarchy
              ↓
              Agent proactively acts (schedules, notifies, executes)
```

No human triggers the agent. The 24/7 monitoring loop runs autonomously.

---

## Identity and Delegation Model

- Per-agent memory with `agent_id` isolation
- Bidirectional traceability: every piece of knowledge links back to its source
- Memory items carry metadata: source, timestamp, confidence, relevance score
- Proactive intent model: agent builds a model of user goals that persists across sessions

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install memu` |
| REST API | Memory CRUD, stream monitoring, context retrieval |
| OpenClaw Integration | Native plugin for OpenClaw memory sessions |

---

## Human-in-the-Loop Support

None required for the core monitoring loop. The agent operates 24/7 autonomously. Humans can review stored memory items via the memU dashboard.

---

## How memU Differs from Mem0, Zep, and OpenViking

| Dimension | Mem0 | Zep | OpenViking | memU |
|---|---|---|---|---|
| Optimized for | Interactive sessions | Interactive sessions | Coding agent sessions | **24/7 proactive agents** |
| Always-on monitoring | No | No | No | **Yes — Fast Context runs continuously** |
| Dual-mode retrieval | No | No | No | **Yes — RAG gate to LLM** |
| Token cost model | Per-operation | Per-operation | Per-query | **Near-zero idle cost; LLM only on trigger** |
| Proactive intent | No | No | No | **Yes — acts without explicit commands** |

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Mem0** | Designed for interactive sessions; no continuous monitoring; no dual-mode gate; no proactive intent capture |
| **Full context injection** | Extremely expensive at 24/7 operation; memU's Fast Context reduces cost 90% |
| **Cron + LLM polling** | High cost per cycle; no semantic relevance gate; not agent-specific |

---

## Use Cases

- **Personal assistant agents** — agent monitors the user's email, calendar, and messages 24/7; proactively surfaces relevant items before the user asks
- **Market monitoring agents** — agent watches price feeds and news streams; activates Deep Reasoning only when a relevant pattern triggers
- **Health agents** — continuous monitoring of wearable data streams; agent acts proactively when anomalies detected
- **Research agents** — agent monitors academic feeds, flags new papers matching stored research interests, and drafts summaries without human prompting
