# Ruflo

> **"An agent meta-harness for Claude Code and Codex."**

| | |
|---|---|
| **Website** | https://github.com/ruvnet/ruflo |
| **Docs** | https://github.com/ruvnet/ruflo/tree/main/docs |
| **GitHub** | https://github.com/ruvnet/ruflo |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/ruvnet/ruflo?style=social)](https://github.com/ruvnet/ruflo) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push 2026-10-19 ([repo metadata](https://api.github.com/repos/ruvnet/ruflo)); README tagline still “An agent meta-harness for Claude Code and Codex.” |
| **Verified at** | 2026-10-19 |

---

## Official Website

https://github.com/ruvnet/ruflo

The former marketing domain `https://ruflo.ai` is a Spaceship for-sale listing (title “ruflo.ai for sale | Spaceship.com”, re-checked 2026-08-29) and is **not** the official site. The GitHub repo homepage field is [Cognitum.One](https://Cognitum.One). Optional UI beta, still live and titled RuFlo: https://flo.ruv.io/

---

## Official Repo

https://github.com/ruvnet/ruflo

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI initialization + MCP + plugins/Skills`

For Codex:

```bash
# Run in the target project
npx ruflo@latest init --codex

# Optional full skill surface
npx ruflo@latest init --codex --full
```

The Codex adapter says initialization generates `AGENTS.md`, installs the selected skills, and auto-registers the MCP server. For a guided general setup use `npx ruflo@latest init wizard`.

---

## Agent Skills

**Status:** ✅ Bundled

Ruflo ships project skills, agent definitions, commands, and optional plugin packs. The full Codex setup advertises 137+ skills; install only the subset justified by the repository to avoid unnecessary prompt and tool surface.

---

## MCP

**Status:** ✅ Primary control surface

The CLI installation registers Ruflo's MCP server. Its tool families cover swarm initialization and agent spawning, memory storage/search, workflow operations, development tools, security, and federation. Plugin-only installation has a smaller surface; `ruflo-core` registers namespaced MCP tools, while the CLI path supplies the full loop.

---

## What It Does

Ruflo is an execution layer around Claude Code and Codex. It adds specialized agents, swarm topologies, background workers, persistent vector memory, self-learning trajectories, model routing, budgets, local/cloud execution, plugins, and a zero-trust federation layer for collaboration across machines or organizations. Codex remains the executor; Ruflo coordinates roles and stores reusable state around it.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Upstream explicitly calls Ruflo an **agent meta-harness** and defines an agent as model plus harness — [README](https://github.com/ruvnet/ruflo) |
| **Agent-specific primitive** | Swarm topology, agent spawn, consensus, shared vector memory, background agent workers, learned trajectories, trust-scored federation, and agent budgets have no equivalent in a normal human app |
| **Autonomy-compatible control plane** | Hooks route work automatically; swarms coordinate, background workers run, budgets/circuit breakers bound execution, and trust can downgrade peers without per-message human action |
| **M2M integration surface** | Ruflo CLI, MCP server and tools, Codex adapter, plugin manifests, Agent Skills, daemon, and structured memory/runtime APIs |
| **Identity / delegation** | Federation uses mTLS plus Ed25519 challenge-response, explicit trust levels, PII egress policy, and structured audit records. Local swarms retain agent IDs, roles, memory namespaces, budgets, and trajectories |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Swarm orchestration** | Hierarchical, mesh, and adaptive agent teams with coordination/consensus |
| **Agent registry/spawn** | Specialized role definitions and bounded worker creation |
| **AgentDB memory** | HNSW-backed persistent vector memory for plans, outcomes, and patterns |
| **Background workers** | Automatically triggered audit, optimization, test-gap, and related jobs |
| **Federation** | Cross-machine agent discovery, authenticated task exchange, and trust policy |
| **Security controls** | Sandboxes, budgets, PII policies, circuit breakers, verification, and audit tooling |
| **MetaHarness** | Grades and snapshots an agent setup, scans tool configuration, and detects drift |

---

## Autonomy Model

```text
Project is initialized for Codex or Claude Code
    -> hooks/router classify incoming work
    -> relevant memories and successful trajectories are retrieved
    -> a swarm topology and specialized workers are selected
    -> agents execute through native runtime and MCP tools
    -> results, costs, and trajectories are stored
    -> policy, trust, budget, and circuit breakers constrain the next action
```

---

## Identity and Delegation Model

- **Local agents:** Spawned workers have explicit roles, IDs, statuses, budgets, and memory namespaces.
- **Federated agents:** Peers prove identity with mTLS and Ed25519 instead of shared API keys.
- **Delegation:** Trust level gates what a remote peer can discover, receive, or access; outbound messages pass through configurable PII controls.
- **Attribution:** Federation events and local trajectories create searchable audit records. Operators can inspect or terminate workers from agent/status surfaces.
- **Scope caution:** Ruflo has a very large optional tool/skill surface. Production deployments should start with the smallest profile and review plugins before enabling them.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `npx ruflo@latest` initialization, orchestration, memory, federation, and operations |
| MCP | Full CLI-track server plus namespaced plugin MCP tools |
| Codex adapter | `@claude-flow/codex`; generates guidance and registers MCP |
| Plugins/Skills | Marketplace plugins, agent definitions, commands, and skills |
| Federation | Authenticated cross-node agent messaging and trust lifecycle |

---

## Human-in-the-Loop Support

Operators can inspect agents, budgets, trajectories, and status; kill or reassign workers; and choose narrower install profiles. Cross-agent work can run automatically after trust and policy are configured. Human review is an orchestration policy rather than a mandatory step for every tool call.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Plain model/agent CLI** | Executes one session but lacks swarm coordination, shared learned memory, federation identity, and budgeted background workers |
| **Generic task queue** | Has jobs and retries but no agent roles, trajectories, semantic memory, consensus, or MCP orchestration |
| **Shared chat channel** | Does not cryptographically identify agent peers or apply trust-level data and delegation policy |

---

## Use Cases

- **Large-repository swarms** — coordinate specialist agents around one coding objective
- **Cross-session learning** — retrieve successful patterns and store new trajectories
- **Federated delivery** — delegate tasks to authenticated agents across machines or organizations
- **Budgeted autonomous maintenance** — run audit/test/optimization workers with cost and circuit-breaker controls
- **Harness readiness audits** — snapshot and grade tools, memory, security, and workflow configuration before release
