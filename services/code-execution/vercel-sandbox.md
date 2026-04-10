# Vercel Sandbox

> **Secure, isolated microVMs for AI-generated code.**

| | |
|---|---|
| **Website** | https://vercel.com/docs/vercel-sandbox |
| **Docs** | https://vercel.com/docs/vercel-sandbox |
| **GitHub** | https://github.com/vercel/sandbox |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/vercel/sandbox?style=social)](https://github.com/vercel/sandbox) |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |

---

## Official Website

https://vercel.com/docs/vercel-sandbox

---

## Official Repo

https://github.com/vercel/sandbox — TypeScript SDK (`@vercel/sandbox`) and tooling for Vercel Sandbox

---

## How to Use (Agent Onboarding)

**TypeScript SDK or REST — create a Firecracker microVM, run commands, snapshot state.**

```bash
npm install @vercel/sandbox
```

```typescript
// See https://vercel.com/docs/vercel-sandbox/sdk-reference
// import { Sandbox } from '@vercel/sandbox'
```

REST: `POST /v1/sandboxes` per [Create a sandbox](https://vercel.com/docs/rest-api/sandboxes/create-a-sandbox). On Vercel deployments, OIDC-based auth is available.

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official `npx skills add vercel/...` bundle located.

```bash
npx clawhub@latest search vercel sandbox
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not yet published as a dedicated first-party MCP server

Agents integrate via SDK/REST from their runtime.

---

## What It Does

Vercel Sandbox provides **Firecracker microVMs** with fast cold start, full **Node.js and Python** runtimes, optional **snapshots** for save/resume, and **persistent sandboxes** (beta). Documentation positions it for **AI agents**, **AI-generated code**, and **untrusted code** execution at scale.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Vercel Sandbox docs describe workloads for **AI agents** and **AI-generated / untrusted code** ([Vercel Sandbox](https://vercel.com/docs/vercel-sandbox)) |
| **Agent-specific primitive** | **Ephemeral secure VMs** spawned programmatically per agent turn with **snapshot/resume** — a lifecycle model for autonomous code execution, not a human SSH box |
| **Autonomy-compatible control plane** | API/SDK create/destroy/run without per-command human approval |
| **M2M integration surface** | `@vercel/sandbox` SDK, REST API, CLI for debugging |
| **Identity / delegation** | Vercel access tokens / OIDC; per-team scoping; auditable via Vercel platform logs |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Sandbox** | Isolated microVM with its own filesystem and network policy |
| **Command** | Run shell / process with streamed stdout/stderr |
| **Snapshot** | Save and restore VM state for long-horizon agent tasks |
| **Persistent sandbox (beta)** | Auto-save state across stops |

---

## Autonomy Model

1. Agent (or host app) creates sandbox via SDK or REST.
2. Agent streams generated code or commands into the VM.
3. Agent reads stdout, files, and HTTP preview URLs if enabled.
4. Agent snapshots or destroys the VM when done.

---

## Identity and Delegation Model

- Credentials: Vercel personal/team tokens or OIDC from Vercel-hosted workloads.
- Sandboxes are isolated per invocation; host application enforces which agents may create VMs.
- Billing and quotas attach to the Vercel team.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| TypeScript | `@vercel/sandbox` — [SDK reference](https://vercel.com/docs/vercel-sandbox/sdk-reference) |
| REST API | [Sandboxes REST](https://vercel.com/docs/rest-api/sandboxes/create-a-sandbox) |
| CLI | `sandbox` CLI for manual and agentic debugging workflows |

---

## Human-in-the-Loop Support

- Vercel account and token issuance require human setup.
- Optional human review of agent outputs can be implemented in the host app.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Local `docker run`** | Agent host must manage images, security, and scale — not a managed per-agent VM API |
| **Shared dev container** | No isolation guarantees between untrusted agent-generated runs |

---

## Use Cases

- **Code-interpreter agents** — run untrusted Python/JS with streaming output.
- **CI-like agent tasks** — clone repo, run tests, report results inside an isolated VM.
- **Long tasks** — snapshot/resume across durable workflows.
