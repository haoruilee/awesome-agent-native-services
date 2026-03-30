# AgentAnycast

> **"Connect AI agents across any network. No public IP required."**

| | |
|---|---|
| **Website** | https://github.com/AgentAnycast/agentanycast |
| **Docs** | https://github.com/AgentAnycast/agentanycast/blob/main/README.md |
| **MCP setup** | https://github.com/AgentAnycast/agentanycast/blob/main/docs/integrations/mcp-setup.md |
| **GitHub** | https://github.com/AgentAnycast/agentanycast |
| **MCP package repo** | https://github.com/AgentAnycast/agentanycast-mcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/AgentAnycast/agentanycast?style=social)](https://github.com/AgentAnycast/agentanycast) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | SDKs and protocol: [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0); daemon and relay: [FSL-1.1-Apache-2.0](https://fsl.software/) (per [repo README license section](https://github.com/AgentAnycast/agentanycast/blob/main/README.md)) |

---

## Official Website

https://github.com/AgentAnycast/agentanycast

---

## Official Repo

https://github.com/AgentAnycast/agentanycast — Python SDK, protocol (`proto/`), docs, examples

https://github.com/AgentAnycast/agentanycast-ts — TypeScript SDK (`npm install agentanycast`)

https://github.com/AgentAnycast/agentanycast-node — Go **daemon** (`agentanycastd`) releases

https://github.com/AgentAnycast/agentanycast-mcp — PyPI **`agentanycast-mcp`** wrapper for IDE MCP configs

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK` + `MCP` (stdio via **`agentanycastd`** or **`uvx agentanycast-mcp`**) + auto-managed daemon

```bash
pip install agentanycast && agentanycast demo
# Second terminal — use the peer id printed by the demo:
agentanycast send <PEER_ID> "Hello!"
```

**MCP — Option A (daemon on PATH after `pip install agentanycast`):** from [mcp-setup.md](https://github.com/AgentAnycast/agentanycast/blob/main/docs/integrations/mcp-setup.md):

```bash
agentanycastd --mcp-listen stdio
```

**MCP — Option B (no global daemon config):** [README](https://github.com/AgentAnycast/agentanycast/blob/main/README.md) documents:

```bash
uvx agentanycast-mcp
```

See [agentanycast-mcp](https://github.com/AgentAnycast/agentanycast-mcp) for Cursor, VS Code, Windsurf, JetBrains, Gemini CLI, and other host snippets.

**Streamable HTTP MCP (optional):** `agentanycastd --mcp-listen :8080` — remote clients connect to `http://localhost:8080` (see mcp-setup.md).

**TypeScript agents:** `npm install agentanycast` ([agentanycast-ts](https://github.com/AgentAnycast/agentanycast-ts))

---

## Agent Skills

**Status:** ⚠️ No standalone `npx skills add` registry entry — onboarding is README + PyPI/npm + MCP docs above.

```bash
npx clawhub@latest search agentanycast
```

---

## MCP

**Status:** ✅ Available — MCP is implemented in the **Go daemon** (`agentanycastd`); PyPI package **`agentanycast-mcp`** wraps it for `uvx` workflows.

| Detail | Value |
|---|---|
| **Implementation** | Go daemon — [mcp-setup.md](https://github.com/AgentAnycast/agentanycast/blob/main/docs/integrations/mcp-setup.md) |
| **PyPI wrapper** | [agentanycast-mcp](https://pypi.org/project/agentanycast-mcp/) — `uvx agentanycast-mcp` |
| **Transport** | stdio (`agentanycastd --mcp-listen stdio`) or Streamable HTTP (`agentanycastd --mcp-listen :PORT`) |
| **Tools (7)** | `discover_agents`, `send_task`, `send_task_by_skill`, `get_task_status`, `get_agent_card`, `list_connected_peers`, `get_node_info` |
| **Compatible Clients** | Claude Desktop, Cursor, VS Code Copilot, Gemini CLI, Codex, JetBrains, Windsurf — config examples in mcp-setup.md |

**Cursor** (from upstream docs):

```json
{
  "mcpServers": {
    "agentanycast": {
      "command": "agentanycastd",
      "args": ["--mcp-listen", "stdio"]
    }
  }
}
```

Equivalent using `uvx`:

```json
{
  "mcpServers": {
    "agentanycast": {
      "command": "uvx",
      "args": ["agentanycast-mcp"]
    }
  }
}
```

---

## What It Does

AgentAnycast is a **peer-to-peer runtime** for AI agents that need to be reachable without a public URL. The project positions itself as fixing a gap in agent-to-agent protocols that assume every agent exposes a public endpoint: real agents often run on laptops, behind NAT, or inside corporate networks. It provides **NAT traversal** (DCUtR hole punching + relay fallback), **Noise_XX end-to-end encryption**, and **skill-based anycast routing** so peers discover each other by advertised capabilities (`AgentCard` + `Skill` metadata) rather than by DNS or static URLs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"Connect AI agents across any network"*; *"AgentAnycast is a **P2P runtime** that gives any agent a reachable identity"*; contrasts with A2A assuming a public URL — [source](https://github.com/AgentAnycast/agentanycast/blob/main/README.md) |
| **Agent-specific primitive** | **NAT-traversing agent reachability** + **skill-based anycast discovery** (`send_task_by_skill` in MCP) — not a generic VPN or static API gateway |
| **Autonomy-compatible control plane** | Agents run `Node(card=...).serve_forever()` and handle tasks asynchronously; MCP `send_task` / `send_task_by_skill` do not require a human per message |
| **M2M integration surface** | Python SDK, TypeScript SDK, **`agentanycastd`** MCP (stdio + HTTP), **`uvx agentanycast-mcp`**, auto-downloaded Go daemon |
| **Identity / delegation** | **`peer_id`** for routing; **`AgentCard`** + **`Skill`** for capability advertisement; MCP **`get_agent_card`** returns skills and **DID**; **`get_node_info`** exposes PeerID and **`did:key`**; E2E Noise_XX; task results as structured **artifacts** |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Node** | Long-running agent runtime wrapping `AgentCard` and `@node.on_task` handlers |
| **Peer ID** | Stable routable identity after NAT traversal |
| **AgentCard** | Published capability metadata (skills, DID, endpoints) |
| **Skill** | Declared capability used in anycast-style routing |
| **Encrypted mesh** | Noise_XX; relay sees ciphertext |
| **NAT traversal** | DCUtR hole punching with relay fallback |
| **MCP: `discover_agents`** | Find agents by skill via DHT + relay registry |
| **MCP: `send_task` / `send_task_by_skill`** | Encrypted task delivery by PeerID or skill |
| **MCP: `get_task_status`** | Poll remote task state |
| **MCP: `get_agent_card`** | Fetch remote **AgentCard** (skills, DID) |
| **MCP: `list_connected_peers` / `get_node_info`** | Local mesh introspection (PeerID, `did:key`, listen addrs) |

---

## Autonomy Model

```
pip install agentanycast  →  daemon/bootstrap resolves connectivity
    ↓
Agent instantiates Node(AgentCard(skills=[...]))
    ↓
Peer A reaches Peer B by peer_id or by skill (no public IP on either host)
    ↓
Tasks and messages flow E2E encrypted; handlers return artifacts
    ↓
MCP client can discover_agents / send_task_by_skill without a human in the loop
```

---

## Identity and Delegation Model

- **Peer identity** — `peer_id` is the routable handle on the mesh.
- **Decentralized identifier** — MCP exposes **`did:key`** via `get_node_info` / agent cards for cryptographic identity semantics.
- **Capability advertisement** — `AgentCard` + `Skill` list lets other agents route work without hard-coded URLs.
- **Trust** — Noise_XX key agreement; operators should validate remote `AgentCard` provenance in multi-tenant deployments.
- **Audit** — Task completion returns structured **artifacts** suitable for logging by the host agent.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install agentanycast` — `Node`, `AgentCard`, `Skill`, `@node.on_task` |
| TypeScript SDK | `npm install agentanycast` |
| MCP | `agentanycastd --mcp-listen stdio` or `uvx agentanycast-mcp` |
| Daemon | `~/.agentanycast/bin/agentanycastd` (auto-installed with Python SDK) |

---

## Human-in-the-Loop Support

No first-class human approval channel in the mesh protocol — agents exchange tasks directly. Organizations add policy at the agent layer (which skills to expose, which remote cards to trust).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Tailscale / VPN** | Network tunnel only; no **`AgentCard` skill routing**, no MCP **`send_task_by_skill`**, no DHT-style **discover_agents** |
| **Public reverse proxy + fixed URL** | Violates the *no public IP* laptop/NAT use case AgentAnycast targets |
| **Generic WebRTC demo** | Lacks agent semantic discovery, multi-language SDK parity, and documented MCP tool surface for coding agents |

---

## Use Cases

- **Claude Code ↔ Codex ↔ local tools** — MCP-connected agents that must message each other without cloud-hosted endpoints
- **Cross-machine agent swarms** — Skill-based routing when agents move between dev laptop, CI runner, and office network
- **Firewall-constrained enterprises** — Encrypted relay path when UDP hole punching is blocked
