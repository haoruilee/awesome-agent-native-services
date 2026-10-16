# Aident Loadout

> **"Give your agents real capabilities"**

| | |
|---|---|
| **Website** | https://aident.ai |
| **Docs** | https://docs.aident.ai/loadout/overview |
| **GitHub** | https://github.com/Aident-AI/aident-skill (MIT skill package; hosted service is closed-source) |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/Aident-AI/aident-skill?style=social)](https://github.com/Aident-AI/aident-skill) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **MCP** | https://loadout.aident.ai/mcp (Streamable HTTP, OAuth) |

---

## Official Website

https://aident.ai

---

## Official Repo

https://github.com/Aident-AI/aident-skill — MIT Agent Skill / setup package. The hosted Loadout service itself is closed-source.

---

## How to Use (Agent Onboarding)

**Quickest verified path (URL onboarding):**

```
Follow https://aident.ai/SETUP.md
```

**MCP (Streamable HTTP + OAuth):**

```bash
claude mcp add --transport http aident https://loadout.aident.ai/mcp
```

**Agent Skill:**

```bash
npx skills add Aident-AI/aident-skill
```

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add Aident-AI/aident-skill
```

| Skill | What It Teaches the Agent |
|---|---|
| `aident-skill` | Connect MCP clients to Aident Loadout, run discover → inspect → preflight → execute, and use 400+ expert-built Skills |

**Compatibility:** Codex, Claude Code, Cursor, ChatGPT, Claude Desktop, and other MCP-compatible clients.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Endpoint** | https://loadout.aident.ai/mcp |
| **Transport** | Streamable HTTP |
| **Auth** | OAuth 2.0 |
| **Official Registry** | `io.github.Aident-AI/loadout` |
| **Compatible Clients** | Claude Code, Codex, Cursor, ChatGPT, Claude Desktop, any MCP HTTP client |

Docs: https://docs.aident.ai/loadout/mcp

---

## What It Does

Aident Loadout is a capability layer for AI agents. After a human connects accounts once in the browser, agents discover and call actions at runtime through one remote MCP endpoint — search by intent, fetch the live input schema, run a side-effect-free preflight that validates input and quotes cost, then execute. Credentials stay in Aident Vault; Audit records what ran, from which client, and at what cost. It also ships 400+ expert-built Skills as task recipes agents can load.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage H1: *"Give your agents real capabilities"*; meta: *"Give any AI agent real capabilities in seconds."* Human surfaces are connection, Vault, and Audit only. Sources: https://aident.ai , https://docs.aident.ai/loadout/overview |
| **Agent-specific primitive** | Runtime discover → inspect → preflight → execute over a capability catalog, plus 400+ Skills. Built so an agent can pick and call a tool it did not know about at planning time. Source: https://docs.aident.ai/loadout/workflows.md |
| **Autonomy-compatible control plane** | After one browser connection, the agent runs actions end to end with no per-action click. Constraints: preflight cost/validation, shared usage balance, per-account connection status. Source: https://docs.aident.ai/loadout/workflows.md |
| **M2M integration surface** | Remote MCP (`https://loadout.aident.ai/mcp`), `aident` CLI (`npm i -g @aident-ai/cli`), installable Agent Skill. Dashboards are secondary. Source: https://docs.aident.ai/loadout/setup-agents.md |
| **Identity / delegation** | Credentials in Aident Vault — *"Your agent should receive connection status, not your provider password or API key."* Audit attributes each action to the agent/client. Agents act on the user's connected accounts (delegated access); Loadout does not mint a separate per-agent KYA wallet. Source: https://docs.aident.ai/loadout/vault-and-audit.md |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Capability search** | Agent searches actions by intent across connected apps |
| **Live schema inspect** | Fetch the exact input schema for an action before calling it |
| **Preflight** | Side-effect-free validation + cost quote before execution |
| **Execute** | Run the action; result returned to the agent |
| **Vault** | Credentials stay server-side; agent never sees raw secrets |
| **Audit** | Log of recent actions with status, source, time, and cost |
| **Skills (400+)** | Expert-built task recipes agents load for research, outreach, content, ops |

---

## Autonomy Model

1. Human connects an account once in the browser (OAuth / API key into Vault).
2. Agent connects via MCP OAuth or CLI / Skill setup.
3. Agent searches for a capability, inspects the schema, runs preflight, then executes.
4. Subsequent calls are fully autonomous within balance and connection constraints — no per-action human click.

---

## Identity and Delegation Model

- Delegation anchor is the user's connected accounts in Vault.
- Agents receive connection status and action results, not provider passwords or API keys.
- Audit attributes each run to the calling client/source.
- Honest boundary: no separate per-agent wallet or Know-Your-Agent identity token.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Remote MCP | `https://loadout.aident.ai/mcp` (Streamable HTTP, OAuth) |
| Agent Skill | `npx skills add Aident-AI/aident-skill` |
| CLI | `npm i -g @aident-ai/cli` |
| Official MCP Registry | `io.github.Aident-AI/loadout` |
| Docs / URL onboarding | https://aident.ai/SETUP.md |

---

## Human-in-the-Loop Support

Initial account connection is a one-time browser step. After that, agents operate without per-action confirmation. Preflight surfaces cost and validation before execution; Audit provides a post-hoc trail.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Zapier / Make** | Human workflow builders; integrations chosen up front in a UI; no agent runtime discover → preflight → execute loop |
| **Direct API calls** | Hardcoded credentials in the agent context; no Vault isolation or unified Audit |
| **Generic iPaaS MCP wrappers** | Often expose human-configured flows rather than agent-driven capability discovery with cost preflight |

Loadout sits next to Composio, Arcade, and Smithery in this category: runtime tool access for agents with managed credentials.

---

## Use Cases

- **Coding agents** — discover and call GitHub, Linear, Notion, Slack from one MCP endpoint with Vault-held credentials
- **Research / ops agents** — load a Skill, then run search/scrape/outreach actions with preflight cost checks
- **Multi-client setups** — same connected accounts reused across Codex, Claude Code, Cursor, and ChatGPT via one Loadout
