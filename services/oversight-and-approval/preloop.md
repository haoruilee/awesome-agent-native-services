# Preloop

> **"The Open Source Control Plane for AI Agents"**

| | |
|---|---|
| **Website** | https://preloop.ai |
| **Docs** | https://docs.preloop.ai |
| **GitHub** | https://github.com/preloop/preloop |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/preloop/preloop?style=social)](https://github.com/preloop/preloop) |
| **Classification** | `agent-native` |
| **Category** | [Oversight & Approval Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | [v0.16.0](https://github.com/preloop/preloop/releases/tag/v0.16.0) released 2026-09-21; last GitHub push 2026-09-29; Apache-2.0; [preloop.ai](https://preloop.ai), [docs](https://docs.preloop.ai), and the CLI installer HTTP 200 (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

https://preloop.ai

---

## Official Repo

https://github.com/preloop/preloop

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` that rewrites local agents onto the control plane

```bash
curl -fsSL https://preloop.ai/install/cli | sh
preloop signup
# or: preloop login --url http://localhost:3000
preloop agents discover
```

`preloop agents discover` finds local Claude Code, Codex CLI, Cursor, Gemini CLI, Hermes, OpenClaw, OpenCode, and other MCP-compatible configs, mints a managed credential, and rewrites supported agents to route tools through the Preloop MCP Firewall and models through the Preloop Gateway.

For live Agent Control on OpenClaw or Hermes, the CLI still needs the runtime plugin:

```bash
preloop agents onboard openclaw
preloop agents install-plugin openclaw
preloop agents validate openclaw
```

Native coding-agent tools (for example Claude Code `Bash`/`Edit`) can be routed with `preloop agents onboard --approvals`.

---

## Agent Skills

**Status:** ⚠️ Not published as a standard `SKILL.md` package

Onboarding is the CLI plus optional runtime plugins, not `npx skills add`.

Search community skills: `npx clawhub@latest search preloop`. See: https://agentskills.io/specification

---

## MCP

**Status:** ✅ Available (firewall / managed MCP)

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/preloop/preloop |
| **Transport** | Preloop-managed MCP URLs after discover/onboard; agents keep speaking MCP |
| **Compatible Clients** | OpenClaw, Claude Code, Codex CLI, Cursor, Gemini CLI, Hermes, OpenCode, Windsurf, and other MCP-compatible agents |

Preloop is the policy plane in front of existing MCP servers, not a single-tool server. It also exposes built-in tools such as `ask_user` and an opt-in Claude Code `permission_prompt` tool.

---

## What It Does

Preloop is a self-hostable (or Preloop Cloud) control plane for agents that already exist on a machine. It unifies an MCP firewall (allow / deny / require approval / require justification with YAML + CEL), an OpenAI- and Anthropic-compatible model gateway with budgets and attribution, human approvals (mobile, watch, Slack, Mattermost, email, webhook), runtime session timelines, and audit evidence.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: **"The Open Source Control Plane for AI Agents"** / **"Preloop is the open-source AI agent control plane."** — [preloop.ai](https://preloop.ai), [README](https://github.com/preloop/preloop) |
| **Agent-specific primitive** | Policy-gated tool calls with denial or approval injected back to the agent, plus `ask_user` and session-attributed audit — not a generic ticket queue |
| **Autonomy-compatible control plane** | Allowed tools run without a click. Only policy-selected actions pause. Async approval lets the agent poll instead of blocking the transport |
| **M2M integration surface** | CLI, MCP firewall URLs, OpenAI/Anthropic-compatible gateway, REST (`GET /api/v1/flows/executions/{id}/result`, control WebSocket) |
| **Identity / delegation** | Discover/onboard mints a durable runtime credential. Every tool/model/policy/approval event is attributed to the managed agent/session |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **MCP firewall** | CEL/YAML allow, deny, approve, justify on MCP and selected native tools |
| **Human approval** | Mobile/watch/Slack/Mattermost/email/webhook with full call context |
| **`ask_user`** | Agent-initiated multiple-choice or free-text question to the operator |
| **Model gateway** | Budgeted OpenAI/Anthropic-compatible proxy; provider keys stay in Preloop |
| **Runtime session** | Timeline of tools, models, policy, spend, and outcome |
| **Audit / AI Act evidence** | Durable logs with matched policy, approver, inputs, timestamps |

---

## Autonomy Model

```
Operator installs CLI and connects Cloud or self-host
    -> preloop agents discover / onboard
    -> agent continues its normal loop
    -> tool and model traffic hit Preloop
    -> policy: allow | deny (message back to agent) | require approval
    -> agent may ask_user or poll async approval
    -> session timeline and audit store the decision
```

---

## Identity and Delegation Model

- **Runtime credential:** Onboarding mints a durable token and can write `preloop.control`.
- **Secret custody:** Provider API keys stay in Preloop; agents receive short-lived gateway tokens.
- **Attribution:** Usage ledger ties tokens and cost to the runtime principal.
- **Approver identity:** Audit records who approved or denied.
- **Plugin boundary:** Live Talk/Agent Control needs the OpenClaw/Hermes plugin WebSocket; the CLI alone does not keep an unmodified agent online.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `preloop signup`, `login`, `agents discover`, `onboard`, `install-plugin`, `validate` |
| MCP firewall | Managed MCP endpoints after rewrite |
| Model gateway | `/openai/v1/…`, `/anthropic/v1/messages` |
| Control WS | `WS /api/v1/agents/control/ws` |
| REST | Flow execution results, security-screen score, session APIs |

---

## Human-in-the-Loop Support

This is the product. Policy can require approval or justification; `ask_user` is a first-class tool. Async mode avoids breaking transport hooks during long reviews. Allowed actions stay non-blocking.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Jira / email approval** | Human-initiated tickets; no agent-context denial or MCP intercept |
| **Model-only gateway** | Tracks spend but does not pause a tool call for a human and return the decision |
| **Log-only MCP proxy** | Observes calls; does not enforce CEL approve/deny with an audit trail |

---

## Use Cases

- **Govern existing coding agents** — discover local Claude Code / Codex / Cursor and wrap their tools
- **Production-dangerous commands** — require approval for deploy or `Bash` that touches prod
- **Budgeted model access** — keep provider keys off the agent host
- **EU AI Act evidence** — retain policy, approver, and outcome (not a legal compliance guarantee)
