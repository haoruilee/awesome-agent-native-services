# Hindsight

> **"Agent Memory That Learns."**

| | |
|---|---|
| **Website** | https://hindsight.vectorize.io |
| **Docs** | https://hindsight.vectorize.io |
| **GitHub** | https://github.com/vectorize-io/hindsight |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/vectorize-io/hindsight?style=social)](https://github.com/vectorize-io/hindsight) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MIT |

---

## Official Website

https://hindsight.vectorize.io

---

## Official Repo

https://github.com/vectorize-io/hindsight

---

## How to Use (Agent Onboarding)

```bash
pip install hindsight-ai
```

Then wire the memory client into an agent loop so the agent can `retain()`, `recall()`, and `reflect()` against its dedicated memory bank.

Docs: https://hindsight.vectorize.io

---

## Agent Skills

**Status:** ⚠️ No official portable Agent Skill package found.

---

## MCP

**Status:** ⚠️ No official MCP server found in the main repository at time of listing.

---

## What It Does

Hindsight is an open-source memory system for AI agents that focuses on learning from experience rather than only replaying conversation history. Agents store observations and experiences, retrieve relevant memories, and run reflection to produce higher-level lessons that can change future behavior.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The official docs describe Hindsight as a memory system designed specifically for AI agents, and the repo tagline is "Agent Memory That Learns." |
| **Agent-specific primitive** | `retain()`, `recall()`, and `reflect()` are agent-memory lifecycle operations rather than generic vector CRUD. |
| **Autonomy-compatible control plane** | Agents can write, search, and consolidate memories during execution without a human curating each record. |
| **M2M integration surface** | Python package and open-source service components for direct programmatic integration. |
| **Identity / delegation** | Agents operate against dedicated memory banks; applications can isolate memory by agent, user, or deployment context. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Retain** | Store facts, observations, and experiences from an agent run. |
| **Recall** | Retrieve relevant prior memories for the current task or context. |
| **Reflect** | Consolidate lower-level memories into lessons, preferences, or strategies. |
| **Dedicated memory bank** | Keep an agent's long-term learning state separate from transient context windows. |

---

## Autonomy Model

1. Agent records useful run outcomes with `retain()`.
2. Before or during future tasks, the agent calls `recall()` for relevant context.
3. Periodically, the agent calls `reflect()` to distill durable lessons.
4. The agent injects the recalled or reflected memory into planning and execution.

No per-memory human confirmation is required for normal operation.

---

## Identity and Delegation Model

- Memory can be scoped to an agent or application-defined actor.
- Dedicated memory banks separate one agent's learned behavior from another's.
- Host applications remain responsible for mapping users, agents, and tenants to memory namespaces.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | Agent memory operations such as retain, recall, and reflect |
| Open-source server/library | Self-hostable components from the official repository |
| Cookbook examples | Framework integration examples in the Hindsight ecosystem |

---

## Human-in-the-Loop Support

Optional. Humans can inspect or reset memory as an operational control, but ordinary retention, recall, and reflection are agent-driven.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Vector database** | Stores embeddings but does not decide what an agent should learn or reflect on. |
| **Conversation buffer** | Replays raw history instead of producing durable behavioral learning. |
| **RAG pipeline** | Retrieves documents, but does not provide agent experience retention and reflection primitives. |

---

## Use Cases

- Long-running personal assistants that improve from prior interactions
- Coding agents that remember project-specific lessons and recurring failure modes
- Research agents that retain observations across experiments
- Support agents that learn account-specific preferences and resolutions
