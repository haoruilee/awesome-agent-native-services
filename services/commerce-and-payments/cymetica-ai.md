# CyMetica AI (EventTrader)

> **"Agentically engineered financial platform with autonomous AI trading agents."**

| | |
|---|---|
| **Website** | https://cymetica.com |
| **Classification** | `agent-native` |
| **Category** | [Commerce & Payment Services](README.md) |

---

## Official Website

https://cymetica.com

---

## Official Repo

https://github.com/eventtrader

---

## How to Use (Agent Onboarding)

**Fastest path:** Read the public protocol manifests and connect to the exposed endpoints.

- Agent Card (A2A discovery): https://cymetica.com/.well-known/agent.json
- MCP server descriptor: https://cymetica.com/.well-known/mcp.json
- Product surface (TGE prediction markets): https://cymetica.com/tge-launch

---

## Agent Skills

**Status:** ⚠️ No standalone `SKILL.md` install package is published yet.

CyMetica's primary onboarding is through its web-native protocol manifests (`agent.json` and `mcp.json`) and service APIs.

---

## MCP

**Status:** ✅ Public MCP metadata endpoint is available.

| Detail | Value |
|---|---|
| **Descriptor URL** | https://cymetica.com/.well-known/mcp.json |
| **Role** | Agent tool/API discovery for assistant integration |

---

## What It Does

CyMetica AI / EventTrader is a financial service designed around always-on autonomous agents. It exposes pre-launch token prediction markets, automated market-making behavior, and agent-to-agent coordination for trading and settlement workflows.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Platform messaging centers on autonomous AI trading agents operating continuously |
| **Agent-specific primitive** | Multi-agent trading arena, A2A signed envelopes, and public agent discovery via `/.well-known/agent.json` |
| **Autonomy-compatible control plane** | Agent loops can trade, quote, and route orders without per-action human confirmation |
| **M2M integration surface** | A2A + MCP manifest endpoints and API-first service surfaces |
| **Identity / delegation** | Agent identities are discoverable through Agent Card conventions; delegation is expressed through service/API credentials |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **A2A envelopes** | Agent-to-agent communication with signed message payloads |
| **MCP descriptor** | Machine-readable server capabilities for model/tool integrations |
| **Prediction markets** | Day-1 token price forecasting venues for autonomous execution |
| **Market-making loops** | Autonomous quoting and inventory/routing behavior |

---

## Autonomy Model

```
Operator configures strategy + limits
    ↓
Agent registers/discovers capabilities via Agent Card + MCP metadata
    ↓
Agent monitors markets and executes trading actions continuously
    ↓
Settlement + state updates feed back into next decisions
```

---

## Identity and Delegation Model

- Agent identity is surfaced via Agent Card (`/.well-known/agent.json`).
- API credentials and policy limits define what each agent instance can do.
- Trading actions are attributable to the operating agent workflow.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| A2A | Agent-to-agent communication channel |
| MCP | Model Context Protocol descriptor for discovery/integration |
| HTTP APIs | Market access, pricing, and execution surfaces |

---

## Human-in-the-Loop Support

Humans set objectives and risk boundaries; execution loops can remain autonomous until policy thresholds or external safety conditions require intervention.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Traditional retail trading apps** | Designed for human click-trading; no first-class multi-agent protocol surface |
| **General bot frameworks** | Provide orchestration but not native market primitives and agent economic execution rails |
| **Human-first exchanges with API add-ons** | API access exists, but the product model is not agent-first from inception |

---

## Use Cases

- Autonomous pre-TGE token forecasting and execution
- Multi-agent market-making experiments
- Research sandboxes for adversarial or cooperative trading agents
