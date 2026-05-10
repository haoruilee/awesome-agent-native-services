# Polos

> **"The open-source runtime for AI agents. Sandboxed execution with built-in tools, human-in-the-loop approvals, Slack integration, and durable workflows with automatic retries and prompt caching. You write the agent. Polos handles the infrastructure."**

| | |
|---|---|
| **Website** | https://github.com/polos-dev/polos |
| **Docs** | https://github.com/polos-dev/polos#readme |
| **GitHub** | https://github.com/polos-dev/polos |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure](README.md) |
| **Status** | Open source · early-stage · Jan 2026 launch |

---

## Official Website

https://github.com/polos-dev/polos

---

## Official Repo

https://github.com/polos-dev/polos

---

## How to Use (Agent Onboarding)

```
# Install:
pip install polos
# or
npm install polos

# Run an agent inside the runtime:
import polos

@polos.agent(triggers=["http", "cron", "webhook"])
def my_agent(ctx): ...
```

The runtime gives the agent: a Docker / E2B sandbox, a built-in tool surface (exec, files, search), durable workflow with automatic retries, prompt caching, and Slack-based HITL approvals.

---

## Agent Skills

**Status:** ⚠️ Not yet published.

```bash
npx clawhub@latest search polos
```

---

## MCP

**Status:** ⚠️ Not yet published as a first-party MCP server. Polos consumes MCP tools (it can call any MCP server from inside the sandbox); a server-side MCP surface is on the roadmap.

| Detail | Value |
|---|---|
| **MCP Role** | Client (consumes external MCP tools) |
| **Transport** | n/a |

---

## What It Does

Polos is an **opinionated runtime for AI agents** that bundles four concerns into one stack:

1. **Sandboxed execution** — agent code runs in a Docker or E2B container with a clean, throw-away filesystem and a built-in tool kit (exec, files, search).
2. **Durable workflow** — each step is checkpointed; on failure, the runtime retries with prompt cache hits to avoid re-paying LLM costs.
3. **Multiple triggers** — HTTP, webhook, cron, and event triggers are first-class; agents are deployed once and react to many sources.
4. **HITL via Slack / UI** — pause-and-approve gates without ad-hoc plumbing.

The pitch is that it sits in the gap between code-execution sandboxes (E2B, Daytona) and durable workflow engines (Trigger.dev, Inngest): you get both, agent-shaped, in one runtime — at small-team operational cost.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repo tagline: *"The open-source runtime for AI agents."* |
| **Agent-specific primitive** | Sandboxed step execution + durable workflow + prompt cache as a single primitive; HITL gate that suspends durably |
| **Autonomy-compatible control plane** | Agent runs end-to-end without per-action human input; HITL is opt-in per step |
| **M2M integration surface** | Python + TS SDK; HTTP / webhook / cron / event triggers |
| **Identity / delegation** | Per-run sandbox identity; secrets injected at runtime, not stored in code |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Sandboxed Run** | Docker or E2B container per run; clean filesystem; built-in tools |
| **Durable Step** | Checkpointed; auto-retries with prompt-cache reuse |
| **Multi-Trigger Deploy** | HTTP / webhook / cron / event from one agent definition |
| **HITL Gate** | Slack or web UI approval; durably suspends the run |
| **Prompt Cache** | Step retries hit cache instead of re-paying full LLM cost |

---

## Autonomy Model

1. Developer writes an agent function and decorates it with `@polos.agent(...)`.
2. Polos deploys it; subscribers (HTTP / cron / webhook / event) trigger runs.
3. Each step runs inside a sandbox; output is checkpointed.
4. On crash or transient error, the runtime auto-retries from the last checkpoint, leveraging prompt cache to avoid LLM token cost.
5. HITL gates suspend the run until a human approves in Slack or the web UI.

---

## Identity and Delegation Model

- Each run is a discrete sandbox identity.
- Secrets are injected at runtime via the runtime's secret store; agent code does not see raw values at rest.
- Audit trail per run: trigger, steps, retries, HITL approvals.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install polos` |
| TypeScript SDK | `npm install polos` |
| HTTP / webhook / cron / event triggers | All first-class |
| Slack integration | HITL approval channel |

---

## Human-in-the-Loop Support

Slack-based approval gates with optional web-UI fallback. Suspended runs are durable — they survive process restarts.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **E2B / Daytona alone** | Sandbox only; no durable workflow, no HITL gate, no triggers |
| **Trigger.dev / Inngest alone** | Durable workflow only; no built-in sandbox + tool surface |
| **DIY: Lambda + Step Functions + Slack bot** | High operational overhead; no prompt cache integration; agent-specific primitives are bolted on rather than first-class |

---

## Use Cases

- **Scheduled research agent** — cron-triggered run that crawls, summarizes, posts a digest; survives crashes
- **Webhook-driven triage** — incoming webhooks fan out to sandboxed agents; HITL approval before any external mutation
- **Cost-bounded long agent loops** — durable retries with prompt cache keep the LLM bill flat after transient failures
