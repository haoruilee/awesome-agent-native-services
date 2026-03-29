# AgentAnycast

> **"Connect AI agents across any network. No public IP required."**

| | |
|---|---|
| **Website** | https://github.com/AgentAnycast/agentanycast |
| **Docs** | https://github.com/AgentAnycast/agentanycast/blob/main/README.md |
| **GitHub** | https://github.com/AgentAnycast/agentanycast |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/AgentAnycast/agentanycast?style=social)](https://github.com/AgentAnycast/agentanycast) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | Apache-2.0 / FSL (per repo badge) |

---

## Official Website

https://github.com/AgentAnycast/agentanycast

---

## Official Repo

https://github.com/AgentAnycast/agentanycast — Python + TypeScript SDKs, MCP server, Go sidecar daemon ([agentanycast-node](https://github.com/AgentAnycast/agentanycast-node) releases)

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK` + `MCP (stdio via uvx)` + auto-managed daemon

```bash
pip install agentanycast && agentanycast demo
# Second terminal — use the peer id printed by the demo:
agentanycast send <PEER_ID> "Hello!"
```

**MCP for Claude, Cursor, VS Code, etc.:**
```bash
uvx agentanycast-mcp
```

**TypeScript agents:** `npm install agentanycast`

---

## Agent Skills

**Status:** ⚠️ Not published as a standalone `npx skills add` repo — onboarding is README + PyPI/npm + `uvx agentanycast-mcp`.

```bash
npx clawhub@latest search agentanycast
```

---

## MCP

**Status:** ✅ Available ([agentanycast-mcp on PyPI](https://pypi.org/project/agentanycast-mcp/))

| Detail | Value |
|---|---|
| **Install** | `uvx agentanycast-mcp` |
| **Transport** | stdio (typical for `uvx` MCP servers) |
| **Compatible Clients** | Claude Desktop, Cursor, VS Code MCP, Codex, other MCP hosts |

---

## What It Does

AgentAnycast is a **peer-to-peer runtime** for AI agents that need to be reachable without a public URL. The project positions itself as fixing a gap in agent-to-agent protocols that assume every agent exposes a public endpoint: real agents often run on laptops, behind NAT, or inside corporate networks. It provides **NAT traversal** (hole punching + relay fallback), **Noise_XX end-to-end encryption**, and **skill-based anycast routing** so peers discover each other by advertised capabilities (`AgentCard` + `Skill` metadata) rather than by DNS or static URLs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"Connect AI agents across any network"*; *"AgentAnycast is a **P2P runtime** that gives any agent a reachable identity"*; contrasts with A2A assuming a public URL — [source](https://github.com/AgentAnycast/agentanycast/blob/main/README.md) |
| **Agent-specific primitive** | **NAT-traversing agent reachability** + **skill-based anycast discovery** (find by capability, not address) — not a generic VPN or static API gateway |
| **Autonomy-compatible control plane** | Agents run `Node(card=...).serve_forever()` and handle tasks asynchronously; messaging does not require a human per packet |
| **M2M integration surface** | Python SDK, TypeScript SDK, MCP server (`uvx agentanycast-mcp`), auto-downloaded Go daemon |
| **Identity / delegation** | Each node has a **`peer_id`**; agents publish an **`AgentCard`** with **`Skill`** entries for discovery; E2E encryption defines the trust boundary; task results return structured **artifacts** |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Node** | Long-running agent runtime wrapping `AgentCard` and task handlers |
| **Peer ID** | Stable identifier for addressing after NAT traversal |
| **AgentCard** | Agent metadata + skill list for discovery |
| **Skill** | Declared capability used in anycast-style routing |
| **Encrypted mesh** | Noise_XX; relay sees ciphertext |
| **NAT traversal** | DCUtR hole punching with relay fallback |
| **MCP server** | `agentanycast-mcp` exposes tools to MCP hosts |

---

## Autonomy Model

```
pip install agentanycast  →  daemon/bootstrap resolves connectivity
    ↓
Agent instantiates Node(AgentCard(skills=[...]))
    ↓
Peer A discovers Peer B by skill / peer id (no public IP on either laptop)
    ↓
Tasks and messages flow E2E encrypted; handlers return artifacts
```

---

## Identity and Delegation Model

- **Peer identity** — `peer_id` is the routable identity on the mesh.
- **Capability advertisement** — `AgentCard` + `Skill` list lets other agents route work without hard-coded URLs.
- **Trust** — Noise_XX key agreement; operators should still validate `AgentCard` provenance in multi-tenant settings.
- **Audit** — Task completion carries structured artifacts suitable for logging by the host agent.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install agentanycast` — `Node`, `AgentCard`, `Skill`, `@node.on_task` |
| TypeScript SDK | `npm install agentanycast` |
| MCP | `uvx agentanycast-mcp` |
| Daemon | Go sidecar from [agentanycast-node releases](https://github.com/AgentAnycast/agentanycast-node/releases) (auto-managed by Python installer) |

---

## Human-in-the-Loop Support

No first-class human approval channel in the mesh protocol — agents exchange tasks directly. Organizations add policy at the agent layer (what skills to expose, what remote cards to trust).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Tailscale / VPN** | Network tunnel only; no **`AgentCard` skill routing**, no A2A-oriented task/artifact model, no MCP entry point for agent hosts |
| **Public reverse proxy + fixed URL** | Violates the *no public IP* laptop/NAT use case AgentAnycast targets |
| **Generic WebRTC demo** | Lacks agent semantic discovery, multi-language SDK parity, and documented MCP integration for coding agents |

---

## Use Cases

- **Claude Code ↔ Codex ↔ local tools** — MCP-connected agents that must message each other without cloud-hosted endpoints
- **Cross-machine agent swarms** — Skill-based routing when agents move between dev laptop, CI runner, and office network
- **Firewall-constrained enterprises** — Encrypted relay path when UDP hole punching is blocked
