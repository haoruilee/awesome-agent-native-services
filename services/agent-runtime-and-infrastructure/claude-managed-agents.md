# Claude Managed Agents

> **"The Claude API is a RESTful API at `https://api.anthropic.com` that provides programmatic access to Claude models and Claude Managed Agents."**

| | |
|---|---|
| **Website** | https://docs.anthropic.com/en/api/overview |
| **Docs** | https://platform.claude.com/docs/en/managed-agents/quickstart |
| **GitHub** | https://github.com/anthropics/anthropic-sdk-python |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **Provider** | Anthropic |

---

## Official Website

https://docs.anthropic.com/en/api/overview

---

## Official Repo

Anthropic publishes official client SDKs (Python, TypeScript, and others) that call the Claude API, including beta endpoints for Managed Agents:

https://github.com/anthropics/anthropic-sdk-python

https://github.com/anthropics/anthropic-sdk-typescript

---

## How to Use (Agent Onboarding)

**SDK / REST:**

1. Create a [Claude Console](https://platform.claude.com/) account and [API key](https://docs.anthropic.com/settings/keys).
2. Follow [Claude Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart) (`Create your first autonomous agent`).
3. Use beta APIs per [API overview](https://docs.anthropic.com/en/api/overview): **Agents** (`POST /v1/agents`), **Sessions** (`POST /v1/sessions`), **Environments** (`POST /v1/environments`), **Skills** (`POST /v1/skills`), **Files** (`POST /v1/files`) — include required [beta headers](https://platform.claude.com/docs/en/api/beta-headers).

```bash
pip install anthropic
```

> **Availability:** Anthropic states that *"Claude Managed Agents is available only through the direct Claude API"* (not Bedrock / Vertex / Azure parity) — [API overview](https://docs.anthropic.com/en/api/overview).

---

## Agent Skills

**Status:** ⚠️ Not yet published

The Claude API includes a beta **Skills API** for creating and managing custom agent skills (`POST /v1/skills`) — [API overview](https://docs.anthropic.com/en/api/overview). That is an API primitive, not an [AgentSkills.io](https://agentskills.io/) marketplace install.

Search community skills: `npx clawhub@latest search claude managed agents`.

---

## MCP

**Status:** ⚠️ No standalone MCP server

Managed Agents run in Anthropic-managed containers; MCP can be composed at the application layer (agent code calling MCP servers), not as a built-in Anthropic MCP daemon.

| Detail | Value |
|---|---|
| **Integration pattern** | REST via Claude API beta endpoints |
| **Compatible Clients** | Any HTTP client; official SDKs recommended |

---

## What It Does

**Claude Managed Agents** is Anthropic’s hosted infrastructure for **versioned agent definitions**, **stateful sessions in managed cloud containers**, and **environment templates** that define how those sessions run. It sits alongside the Messages API: you define an agent configuration, create a session, and stream or poll execution — without operating the container fleet yourself. Related beta APIs cover **file uploads** for multi-step workflows and **custom skills** registration.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Anthropic documents *"programmatic access to Claude models and Claude Managed Agents"* and links managed infrastructure to a dedicated [Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart) — [API overview](https://docs.anthropic.com/en/api/overview) |
| **Agent-specific primitive** | First-class **Agents** (reusable versioned configs), **Sessions** (stateful runs in managed containers), **Environments** (container templates) — not generic chat completions alone |
| **Autonomy-compatible control plane** | Sessions run to completion in managed containers; orgs use API spend and rate limits for control — [rate limits](https://docs.anthropic.com/docs/en/api/rate-limits) |
| **M2M integration surface** | REST (`api.anthropic.com`) plus official SDKs; beta features require beta headers — [API overview](https://docs.anthropic.com/en/api/overview) |
| **Identity / delegation** | API keys are org-scoped; responses include `request-id` and `anthropic-organization-id` for attribution — [API overview](https://docs.anthropic.com/en/api/overview). Fine-grained **workspaces** segment keys and spend — [workspaces](https://platform.claude.com/settings/workspaces) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agents API** | Define reusable, versioned agent configurations for Managed Agents |
| **Sessions API** | Create and run stateful agent sessions; streaming supported (`GET /v1/sessions/{id}/stream`) |
| **Environments API** | Configure container templates for agent sessions |
| **Skills API (beta)** | Create and manage custom skills attached to agent workflows |
| **Files API (beta)** | Upload and reference files across multi-call agent runs |

---

## Autonomy Model

1. `POST /v1/agents` defines a versioned agent configuration (instructions, tools, policy).
2. `POST /v1/sessions` starts a managed session bound to an agent and optional environment.
3. The agent executes inside Anthropic-managed infrastructure; the client consumes streamed or polled output.
4. Files and skills are attached via their respective beta APIs as the task requires.

---

## Identity and Delegation Model

- **API key** authenticates the calling integration; **workspaces** segment usage and spend per team or use case.
- **Response headers** (`request-id`, `anthropic-organization-id`) tie traffic to org-level audit and support.
- **Delegation** to third-party tools (OAuth, enterprise SaaS) is composed in agent/tool configuration; Anthropic’s API is the control plane for session lifecycle, not end-user IAM for every external system.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | `https://api.anthropic.com` — Messages + beta Managed Agents endpoints |
| Python SDK | `anthropic` package |
| TypeScript SDK | `@anthropic-ai/sdk` |
| Beta access | [Beta headers](https://platform.claude.com/docs/en/api/beta-headers) required for Agents, Sessions, Environments, Skills, Files |

---

## Human-in-the-Loop Support

Application-defined (tool design, approval steps in your orchestration). The Managed Agents APIs focus on session lifecycle and execution, not a built-in human approval product.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Messages API only** | Stateless turn-by-turn chat; no managed session containers or environment templates |
| **Self-hosted Docker** | You operate images, scaling, and isolation; Managed Agents provides Anthropic-operated session infrastructure |
| **Claude via Bedrock / Vertex** | Anthropic states Managed Agents is **direct API only** — [API overview](https://docs.anthropic.com/en/api/overview) |

---

## Use Cases

- **Hosted coding or research agents** — long sessions with files without running your own sandbox fleet
- **Versioned agent rollouts** — promote agent configurations like software versions
- **Multi-step workflows** — Files + Sessions for tasks that exceed a single Messages round-trip
