# Dasha Compute

> **"OpenAI-compatible inference. A run factory, not a ledger."**

| | |
|---|---|
| **Website** | https://www.getdasha.com/compute |
| **Docs** | https://www.getdasha.com/compute/skill.md |
| **GitHub** | https://github.com/Uuriko/dasha-desk |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |

---

## Official Website

https://www.getdasha.com/compute

---

## Official Repo

Open agent tooling: https://github.com/Uuriko/dasha-desk

---

## ⭐ How to Use (Agent Onboarding)

**URL onboarding — an agent can start from a single document, with no signup and no human in the loop.**

```
# URL Onboarding:
Read https://www.getdasha.com/.well-known/agent.json (or https://www.getdasha.com/llms.txt) and follow the instructions to register and join.

# SDK / REST:
# 1. Mint a 24h guest key with a bare POST (no account, no email):
curl -sS -X POST https://lobby.getdasha.com/compute/api/guest-keys -H 'Content-Type: application/json' -d '{}'
# 2. Use the OpenAI SDK with base_url https://lobby.getdasha.com/compute/api/v1 and the guest key as the Bearer token.
```

---

## Agent Skills

**Status:** ✅ Available — the service publishes its own skill document at `https://www.getdasha.com/compute/skill.md`, plus `llms.txt` and an agent manifest.

| Skill | What It Teaches the Agent |
|---|---|
| `compute/skill.md` | Guest-key minting, model listing, and OpenAI-compatible chat calls against the Dasha Compute API |

---

## MCP

**Status:** ⚠️ Static MCP catalog published at `https://www.getdasha.com/compute/mcp.json` (HTTP tools + base_url); not a streamable MCP session.

---

## What It Does

Dasha Compute is an **OpenAI-compatible inference marketplace** where AI agents are the primary consumer: agents mint their own 24-hour guest API keys with a single unauthenticated POST, list available models, and run chat completions against a standard `base_url`. Inference is routed to idle community hardware, and the DASHA token (Solana SPL) anchors the ecosystem. The service exposes machine-readable agent surfaces throughout: `/.well-known/agent.json`, `llms.txt`, an MCP catalog (`mcp.json`), and a `skill.md`.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The MCP catalog self-describes as machine-consumable (`https://www.getdasha.com/compute/mcp.json`: "Static MCP catalog. Call the existing HTTP tools or the OpenAI-compatible base_url."); `/.well-known/agent.json` and `llms.txt` are published for agent discovery |
| **Agent-specific primitive** | **Guest-key minting by API** — `POST /compute/api/guest-keys` returns a scoped 24h key with no signup, email, or human approval |
| **Autonomy-compatible control plane** | Key minting, model listing, and chat completions are all plain API calls; public reads (`healthz`, `network`, `models`) need no auth at all |
| **M2M integration surface** | OpenAI-compatible REST (`/compute/api/v1`), static MCP catalog, `agent.json`, `llms.txt`, `skill.md` |
| **Identity / delegation** | Guest keys are time-boxed (24h TTL), rate-limited per IP, and scoped (`chat`, `models`); no persistent human identity required |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Guest-key minting** | `POST /compute/api/guest-keys` — 24h key, no signup |
| **OpenAI-compatible chat** | Standard `/chat/completions` at `https://lobby.getdasha.com/compute/api/v1` |
| **Public catalog reads** | `healthz`, `network`, `models` without auth |
| **Agent manifests** | `/.well-known/agent.json`, `llms.txt`, `compute/mcp.json`, `compute/skill.md` |

---

## Autonomy Model

```
Agent fetches /.well-known/agent.json or llms.txt
    ↓
Agent POSTs /compute/api/guest-keys and receives a 24h guest key
    ↓
Agent lists models and calls chat completions with the OpenAI SDK
    ↓
Key expires after 24h; agent mints a fresh one — no human step anywhere
```

---

## Identity and Delegation Model

- **Guest keys** are self-issued, scoped (`chat`, `models`), rate-limited (3/hour/IP), and expire after 24 hours.
- **Bearer keys** gate chat; catalog reads are public.
- No email, OAuth, or human identity is required to start.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | `https://lobby.getdasha.com/compute/api/v1` — OpenAI-compatible (chat, models) |
| Guest keys | `POST https://lobby.getdasha.com/compute/api/guest-keys` |
| Agent discovery | `/.well-known/agent.json`, `/llms.txt`, `/compute/mcp.json`, `/compute/skill.md` |
| MCP | Static catalog only — not a streamable MCP session |

---

## Human-in-the-Loop Support

Not a HITL product; no approval step exists in the agent path. Token governance and ecosystem coordination happen outside the inference loop (X: [@dash_eats](https://x.com/dash_eats)).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Single-vendor LLM API** | Requires human signup, billing, and a credit card before the first call; Dasha Compute guest keys need none |
| **Generic inference marketplace for humans** | Onboarding assumes a person with email/OAuth; Dasha Compute's discovery and key minting are fully machine-readable |
| **Self-hosted inference** | The agent must operate hardware; Dasha Compute is an API surface |

---

## Use Cases

- **Self-provisioning agents** — an agent with no credentials can start making LLM calls in seconds
- **Agent toolchains** — `skill.md` / MCP catalog slot directly into agent skill loaders and service discovery
- **Experimentation without accounts** — throwaway 24h keys for evaluation or CI agents
