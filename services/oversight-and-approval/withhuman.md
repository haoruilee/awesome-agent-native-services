# withHuman

> **"The approval layer for AI agents."**

| | |
|---|---|
| **Website** | https://withhuman.ai |
| **Docs** | https://withhuman.ai/blog/introducing-withhuman |
| **GitHub** | https://github.com/withHumanAI/withHuman |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/withHumanAI/withHuman?style=social)](https://github.com/withHumanAI/withHuman) |
| **Classification** | `agent-native` |
| **Category** | [Oversight & Approval Services](README.md) |
| **License** | Elastic-2.0 (core); Apache-2.0 (Agent Approval Protocol spec and libraries) |

---

## Official Website

https://withhuman.ai

---

## Official Repo

https://github.com/withHumanAI/withHuman — self-hostable core: queue, audit trail, web UI (single binary)

https://github.com/agentapprovalprotocol/agentapprovalprotocol — Agent Approval Protocol (AAP): spec, OpenAPI contract, Go adapters and CLI

---

## How to Use (Agent Onboarding)

**Interaction pattern:** **Hooks** (Claude Code, Codex) + **SDKs** (Python/TypeScript) + **AAP** HTTP protocol

1. Run withHuman yourself (Docker or from source; one binary with built-in database and workflow engine) or use the hosted version.
2. Connect a coding agent with the prebuilt hooks, or wrap tools in your own agent with the AAP SDKs (LangGraph, Pydantic AI, OpenAI Agents SDK, CrewAI, Mastra, …).
3. Write approval pipelines (e.g. "approve refunds up to $20, ask payments above that") and escalation paths.

See the repository README for the quickstart.

---

## Agent Skills

**Status:** ❌ No Agent Skill; integration is through hooks and SDKs.

---

## MCP

**Status:** ⚠️ Gates MCP tool calls (starting point per the launch post) rather than exposing its own MCP server.

---

## What It Does

withHuman sits **between agents and their tools** and intercepts every tool call before it runs. **Approval pipelines** approve, deny, ask a model or service, or decide the call needs a person, based on the tool and its arguments. **Escalation paths** route the rest to the right team or person by team, level and working hours, notifying via email, Slack or Discord. Reviewers see the exact arguments and the agent's explanation in a shared review queue and approve or deny with a note the agent reads. Agents speak the open **Agent Approval Protocol (AAP)**, so integrations are portable between providers.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"The approval layer for AI agents."* |
| **Agent-specific primitive** | Tool-call interception with per-call approval request carrying the exact tool and arguments; denial reason returned to the agent |
| **Autonomy-compatible control plane** | Policies auto-approve or auto-deny routine calls so agents run unattended; only escalated calls wait for a human |
| **M2M integration surface** | AAP OpenAPI contract, Python/TypeScript SDKs, coding-agent hooks |
| **Identity / delegation** | Every decision recorded in an audit trail tied to the agent's request and the reviewer |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **AAP approval request** | Adapter holds a tool call and requests a decision |
| **Approval pipeline** | Rules on tool + arguments → approve / deny / escalate |
| **Escalation path** | Picks reviewers by team, level and hours |
| **Review queue + audit trail** | Shared human decisions with notes fed back to the agent |

---

## Autonomy Model

```
Agent calls a tool as usual
    ↓
AAP hook/SDK holds the call → withHuman
    ↓
Pipeline: approve / deny automatically, or escalate to a human
    ↓
Approved call runs; denied call fails with the reason visible to the agent
```

---

## Identity and Delegation Model

- **Request attribution:** each AAP request carries the agent's tool call, exact arguments and the agent's explanation.
- **Reviewer routing:** escalation paths pick reviewers by team, level and working hours.
- **Audit:** decisions and reviewer notes are kept in the withHuman audit trail.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **AAP** | Open spec + OpenAPI contract (Apache-2.0) |
| **Hooks** | Claude Code, Codex and other coding agents |
| **SDKs** | Python and TypeScript; framework integrations (LangGraph, Pydantic AI, OpenAI Agents SDK, CrewAI, Mastra) |
| **Notifications** | Email, Slack, Discord |

---

## Human-in-the-Loop Support

Core purpose. Reviewers are notified by email, Slack or Discord and decide in the review queue.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Per-agent built-in permission prompts** | Different per tool, no shared rules, routing or audit across agents |
| **Generic ticketing / workflow tools** | Not wired into the tool call, so agents can skip them |

---

## Use Cases

- **Gating production changes** (SQL, deploys) proposed by coding agents.
- **Spending limits** on refunds or payments with escalation above a threshold.

---

## License Note

The core is source-available under the Elastic License 2.0 (self-hosting allowed; offering it as a managed service is not). The AAP spec and libraries are Apache-2.0.
