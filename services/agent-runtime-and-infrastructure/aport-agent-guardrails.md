# APort Agent Guardrails

> **"Deterministic pre-action authorization for AI agents."**

| | |
|---|---|
| **Website** | https://aport.io |
| **Docs** | https://aport.io/docs |
| **GitHub** | https://github.com/aporthq/aport-agent-guardrails |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/aporthq/aport-agent-guardrails?style=social)](https://github.com/aporthq/aport-agent-guardrails) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |

---

## Official Website

https://aport.io

---

## Official Repo

https://github.com/aporthq/aport-agent-guardrails

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No standalone Agent Skill listed in this catalog yet.

APort currently ships framework-specific setup paths for OpenClaw, Cursor, Claude Code, LangChain, CrewAI, DeerFlow, and n8n through its CLI and packages.

```bash
npx @aporthq/aport-agent-guardrails
```

---

## MCP

**Status:** ❌ Not a standalone MCP server

APort is a runtime guardrail layer rather than an MCP server. It integrates through CLI setup, framework hooks, callbacks, and provider adapters that run before tool execution.

| Detail | Value |
|---|---|
| **Node package** | `@aporthq/aport-agent-guardrails` |
| **Python package** | `aport-agent-guardrails` |
| **Policy artifact** | Open Agent Passport (OAP) |
| **Supported frameworks** | OpenClaw, Cursor, Claude Code, LangChain, CrewAI, DeerFlow, n8n |

---

## What It Does

APort Agent Guardrails verifies AI agent actions before tool execution. It checks each proposed tool call or sensitive action against an Open Agent Passport policy and records allow/deny decisions, reducing reliance on prompt-only safety instructions.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Product tagline and docs focus on AI agent pre-action authorization, not human workflow automation |
| **Agent-specific primitive** | OAP passport, policy verification, fail-closed guardrail, and per-tool-call audit records |
| **Autonomy-compatible control plane** | Agents can continue autonomously while risky actions are deterministically allowed or denied by policy |
| **M2M integration surface** | CLI, npm package, PyPI package, framework hooks, callbacks, and provider adapters |
| **Identity / delegation** | Passport and decision artifacts make agent action constraints explicit and auditable |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Open Agent Passport (OAP)** | Policy artifact describing allowed actions, limits, assurance, and verification rules |
| **Pre-action authorization** | Guardrail runs before tool execution, not after the agent has acted |
| **Fail-closed evaluation** | Missing or invalid guardrail configuration blocks risky actions by default |
| **Audit log** | Decision records capture timestamp, tool, allow/deny outcome, policy, and context |
| **Framework adapters** | Setup paths for OpenClaw, Cursor, Claude Code, LangChain, CrewAI, DeerFlow, and n8n |

---

## Autonomy Model

```text
Agent proposes a tool call
    ↓
APort hook/callback/provider receives the action
    ↓
OAP policy is evaluated locally or through the APort API
    ↓
Decision is logged as allow or deny
    ↓
Allowed action executes; denied action is blocked before side effects
```

---

## Identity and Delegation Model

- **Passport file** defines the agent's permitted actions and policy boundaries.
- **Hosted agent ID** can reference a passport managed by APort.
- **Decision artifact** records the evaluated action and outcome.
- **Audit log** gives operators a trail of what the agent attempted and what policy allowed.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `npx @aporthq/aport-agent-guardrails` |
| Node runtime | npm package and framework-specific setup |
| Python runtime | PyPI package and framework-specific callbacks/providers |
| API mode | Optional hosted policy evaluation through APort API |
| Local mode | Offline policy subset for local/bash guardrail paths |

---

## Human-in-the-Loop Support

APort is primarily deterministic policy enforcement, not a human approval queue. Humans define or review the passport policy; runtime decisions are machine-evaluated before the agent acts.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Prompt-only rules** | The model can ignore or be induced to bypass instructions embedded in prompts |
| **Manual approval in chat** | Does not provide deterministic enforcement or structured per-action audit records |
| **Generic API gateway** | Controls network requests, but not agent-specific tool semantics or OAP policy decisions |
| **Post-action logging** | Records incidents after side effects; APort blocks before execution |

---

## Use Cases

- Blocking destructive shell commands in coding agents.
- Enforcing policy limits for OpenClaw, Cursor, Claude Code, LangChain, and CrewAI agents.
- Auditing allow/deny decisions for high-risk tool calls.
- Running agent workflows with explicit, reviewable action boundaries.

---

## Links

- [Docs](https://aport.io/docs)
- [GitHub repository](https://github.com/aporthq/aport-agent-guardrails)
- [Open Agent Passport spec](https://github.com/aporthq/aport-spec)
- [npm package](https://www.npmjs.com/package/@aporthq/aport-agent-guardrails)
- [PyPI package](https://pypi.org/project/aport-agent-guardrails/)
