# Zambo

> **"Give your AI hands, memory, and proof."**

| | |
|---|---|
| **Website** | https://zambo.dev |
| **Docs** | https://zambo.dev/add/ |
| **GitHub** | https://github.com/zambodotdev/zambo-mcp |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |

---

## Official Website

https://zambo.dev

---

## Official Repo

https://github.com/zambodotdev/zambo-mcp

---

## How to Use (Agent Onboarding)

**Pattern: MCP.** Add Zambo as a remote MCP server; no API key, no signup, no account to start.

```json
{
  "mcpServers": {
    "zambo": { "url": "https://zambo.dev/mcp" }
  }
}
```

Or, in Claude Code:

```bash
claude mcp add --transport http zambo https://zambo.dev/mcp
```

Free tier: 20 calls + 1 wrap-up free every day; picking up in another AI is always free. Paid use is machine-settled (Day Pass via x402, USDC on Base). Setup for more clients: https://zambo.dev/add/

---

## Agent Skills

**Status:** ✅ Available, the `zambo` skill on ClawHub (https://clawhub.ai/skills/zambo).

```bash
npx clawhub@latest install zambo
```

| Skill | What It Teaches the Agent |
|---|---|
| `zambo` | How to connect to the Zambo MCP endpoint and use its tools, memory, handover, and per-call receipts |

---

## MCP

**Status:** ✅ Available, native remote MCP server, the primary interface.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/zambodotdev/zambo-mcp |
| **Server** | https://zambo.dev/mcp |
| **Transport** | Streamable HTTP |
| **Tools** | 153 total, 36 on the default surface |
| **Compatible Clients** | Claude Code, Claude Desktop, Cursor, Codex, any MCP-compatible runtime |

---

## What It Does

Zambo is the verifiable work layer for AI: 153 tools behind one remote MCP endpoint (live data, research, site and code audits, payments with spend limits, input screening), built around three agent-only primitives. HANDOVER is the flagship: an agent wraps up a session in one AI (goal, notes, files, links, next step) and any other AI picks it up and continues, with pickup always free. Memory persists across AIs, so what one agent saves, another recalls. And every tool call returns a verifiable AER-1 receipt (IETF Internet-Draft draft-zambo-aer1-26): a saved record of the job and its result that anyone can check later, without an account, at https://zambo.dev/verify/.

The point of the receipt is narrow and provable: it proves the saved result was not changed since it was saved. Receipts are issued for every call, including calls that are rejected.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage addresses AI agents as the primary consumer: "Give your AI hands, memory, and proof." (https://zambo.dev). The product is one MCP endpoint an AI connects to, not a human app with an agent add-on. |
| **Agent-specific primitive** | Handover (wrap up a session in one AI, continue it in any other; pickup is free), persistent memory shared across AIs, and a verifiable AER-1 receipt minted for every tool call. None of these has a human-facing equivalent. |
| **Autonomy-compatible control plane** | An agent connects and works with no per-action human confirmation and no signup. Paid use is machine-settled (Day Pass via x402, USDC on Base); the daily free tier (20 calls + 1 wrap-up) and owner-set spend limits are the constraint mechanisms. |
| **M2M integration surface** | Remote MCP server (Streamable HTTP) is the primary interface: https://zambo.dev/mcp. Human pages are secondary. |
| **Identity / delegation** | Every call is attributable to a specific caller identity, and the per-call receipt is the audit trail for what that agent did, checkable by anyone at https://zambo.dev/verify/. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Handover** | Wrap up a session in one AI with a code; any other AI picks it up and continues. Pickup is always free. |
| **Cross-AI memory** | Persistent memory shared across AIs and sessions; save in one, recall in another. |
| **Verifiable receipt** | An AER-1 receipt for every tool call, proving the saved result was not changed since it was saved. |

---

## Autonomy Model

1. Agent adds `https://zambo.dev/mcp` as a remote MCP server (no key, no signup).
2. Agent lists tools at runtime and calls them inside the daily free tier.
3. Every call returns its result plus an AER-1 receipt.
4. When the session needs to move, the agent wraps up with handover; a different AI picks up for free and continues with full context.
5. If the agent needs more than the free tier, it settles a Day Pass itself via x402 (USDC on Base), within spend limits its owner set.

---

## Identity and Delegation Model

- Each call carries a caller identity; usage, quota, and receipts are attributed to that identity, not to a human dashboard session.
- Delegated authority is bounded by owner-set spend limits on payment tools; the agent cannot exceed them.
- The per-call receipt is the audit trail: it names the tool, the caller, and the saved result, and anyone can verify it at https://zambo.dev/verify/ without an account.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP server | Streamable HTTP, https://zambo.dev/mcp |
| Receipt verification | https://zambo.dev/verify/ (no account needed) |
| Agent Skill | ClawHub `zambo`, install: `npx clawhub@latest install zambo` |
| Setup guides | https://zambo.dev/add/ |

---

## Human-in-the-Loop Support

Out of scope by design: Zambo's control plane is autonomy-compatible, so there is no per-action approval step. Human control sits at the boundaries an owner sets once: spend limits for payments, and the handover code, which only the agent that wrapped up (or someone it gives the code to) can pick up.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Generic tool gateways** | They expose human-built APIs to agents; they have no cross-AI session handover, no shared agent memory, and no per-call verifiable receipt. |
| **Plain memory stores** | Storage and retrieval only; no work tools, no continuity handover between AIs, and no audit trail proving what the agent did. |

---

## Use Cases

- **Switching AIs mid-task**: wrap up in one AI, pick up in another, lose nothing
- **Long-running agent work**: memory and receipts survive across sessions and runtimes
- **Client work with proof**: hand the client a receipt they can verify themselves
