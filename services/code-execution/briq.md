# briq

> **"Cloud sandboxes for your agents."**

| | |
|---|---|
| **Website** | https://briq.cloud |
| **Docs** | https://briq.cloud/docs |
| **GitHub** | https://github.com/briq-cloud |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |

---

## Official Website

https://briq.cloud

---

## Official Repo

The hosted service is closed source. Public repositories: the MCP server listing https://github.com/briq-cloud/briq-mcp, the TypeScript SDK https://github.com/briq-cloud/briq-sdk, the Python client https://github.com/briq-cloud/briq-python, the CLI https://github.com/briq-cloud/briq-cli and the sandbox image https://github.com/briq-cloud/sandbox.

---

## How to Use (Agent Onboarding)

**The quickest path for an agent to start using this service.** A person signs in once in the browser and approves the agent for a team with a budget. For CI and scripts, an API key from the dashboard replaces the sign-in.

```
# MCP (Streamable HTTP, OAuth sign-in in the browser):
claude mcp add --transport http briq https://api.briq.cloud/mcp

# Agent instructions:
Read https://briq.cloud/llms.txt and follow the instructions.

# CLI:
npm install -g @briq-cloud/cli  # then: briq login, briq run sandbox

# SDK / REST (API key):
npm install @briq-cloud/sdk  # or: pip install briq-cloud
```

---

## Agent Skills

**Status:** ✅ Available

The skill is served at https://briq.cloud/.well-known/skills/briq/SKILL.md (MIT). It teaches an agent when to reach for a sandbox or a service, and how to connect briq.

| Skill | What It Teaches the Agent |
|---|---|
| `briq` | Run code in a sandbox instead of the user's machine, start a real database or service for a project, share a preview link, fork a database before a risky change, connect briq from a laptop, a server or a chat app |

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/briq-cloud/briq-mcp (listing; the server is hosted). Registry name `cloud.briq/briq` |
| **Endpoint** | `https://api.briq.cloud/mcp` |
| **Transport** | Streamable HTTP |
| **Auth** | OAuth per the MCP authorization spec (PKCE, dynamic client registration, device code for agents without a browser), or an API key as `Authorization: Bearer` |
| **Tools / prompts** | `briq_run`, `briq_exec`, `briq_files_put`, `briq_files_get`, `briq_expose`, `briq_fork`, `briq_stop`, `briq_start`, `briq_destroy`, `briq_quota` and others ([list](https://briq.cloud/docs/mcp/tools)); prompt `briq_getting_started` |
| **Compatible Clients** | Claude, Claude Code, Cursor, VS Code, Codex, any MCP client |

---

## What It Does

briq gives an agent a machine of its own, and the services that machine needs next to it. `briq_run({ recipe: "sandbox" })` starts a Linux microVM with Python, Node, git and a shell. The agent writes files, runs commands (long ones asynchronously, with a result to poll), reads the output and destroys the machine when it is done. Nothing runs on the person's computer.

The same call starts a service: Postgres, MySQL, Redis, MongoDB, Qdrant, a headless Chrome, an app from a GitHub repository or any OCI image. Services in one stack reach each other by name, and each returns connection strings. A briq goes to sleep after a window without use (default one hour), keeps its disk while it sleeps, is not billed for compute, and wakes on the next call or visit. `briq_fork` copies a briq, for example a database before a risky migration.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Cloud sandboxes for your agents. A sandbox, a database, a desktop or a whole app in one command or MCP call." — https://briq.cloud ; MCP registry description: "Give your agent its own cloud" — https://github.com/briq-cloud/briq-mcp |
| **Agent-specific primitive** | Per-agent policy checked before any machine is created (concurrent briqs, daily spend cap, allowed sizes and registries, longest sleep, expiry); `quota_exceeded` and `payment_required` errors that tell the model to adapt or stop; `briq_quota` so a model plans instead of retrying — https://briq.cloud/docs/concepts/keys-and-policy |
| **Autonomy-compatible control plane** | The agent creates, runs, exposes, forks and destroys without a human step after the one-time approval; spend is bounded by the policy, not by confirmations — https://briq.cloud/docs/guides/budgets |
| **M2M integration surface** | MCP, REST API with OpenAPI 3.1 (https://api.briq.cloud/v1/openapi.json), TypeScript SDK, Python client, CLI, `llms.txt` |
| **Identity / delegation** | Each connected client and each API key is its own agent with its own policy; the audit log records the client on every row; only a signed-in person can create, edit or revoke agents, so an agent cannot raise its own budget — https://briq.cloud/docs/concepts/keys-and-policy |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Sandbox** (`briq_run` with `recipe: "sandbox"`) | A microVM with Python, Node, git, a shell and database clients, on a persistent volume |
| **Service recipe** (`briq_catalog`, `briq_run`) | Postgres, Redis, a headless browser, an app from a repository or any OCI image, with ready connection strings in `outputs` |
| **Stack** (`briq_up`) | Several briqs that reach each other by internal name, from one stack file |
| **Async exec** (`briq_exec` with `async: true`, `briq_exec_result`) | A long command with a result to poll; counts as use while it runs |
| **Fork** (`briq_fork`) | A copy of a briq, for a database before a risky change or one environment per task |
| **Sleep** (`briq_set_sleep`) | One setting for when an idle briq stops; it wakes on the next call |
| **Preview URL** (`briq_expose`) | `private` (the link is the secret) or `public` HTTPS URL for a running service |
| **Quota** (`briq_quota`) | What the agent's policy and plan still allow |

---

## Autonomy Model

1. A person adds `https://api.briq.cloud/mcp` to the client and signs in once. The approval page sets the agent's team and budget.
2. The agent calls `briq_catalog`, then `briq_run` for a sandbox or a service.
3. The agent writes files with `briq_files_put` and runs commands with `briq_exec`, reading output and exit codes.
4. If a call fails with `quota_exceeded` or `policy_violation`, the agent calls `briq_quota` and picks a smaller size or a shorter sleep.
5. The agent shares a preview URL with `briq_expose` when something outside needs to reach the service.
6. When done, the agent calls `briq_destroy`. If it forgets, the briq goes to sleep and stops costing compute.

---

## Identity and Delegation Model

- Each connected client or API key is one agent of a team, with its own policy: concurrent briqs, daily spend cap, allowed sizes, allowed image registries, longest sleep, expiry.
- Tokens stay with the client; the model never sees them. Revoking an agent takes effect immediately.
- An API key acts for the whole team, under the budget of its policy. The policy bounds what the key spends, not what it reaches; a narrower reach needs a separate team.
- Credentials are not managed by agents: an API key calling the credential routes gets `403 forbidden`.
- Secrets go in as named values, boot-only or team-scoped, and are not returned by status. A team secret reaches the code as a placeholder that a credential gateway replaces in requests to allowed hosts.
- The audit log records the client of every action.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | `https://api.briq.cloud/mcp`, Streamable HTTP, OAuth or API key |
| REST API | `https://api.briq.cloud/v1`, OpenAPI 3.1 at `/v1/openapi.json` |
| SDK | `@briq-cloud/sdk` (TypeScript), `briq-cloud` (Python) |
| CLI | `@briq-cloud/cli` |
| Agent instructions | https://briq.cloud/llms.txt, https://briq.cloud/.well-known/skills/briq/SKILL.md, a Markdown copy of every docs page |

---

## Human-in-the-Loop Support

A person approves each client once, for a team and a budget, and can change or revoke it on the dashboard at any time. Plan limits and the policy hold even if the agent asks for more. A person creates and revokes keys; an agent cannot. Teams top up credits on the dashboard; an agent that hits `payment_required` is told to report it and stop.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A cloud VM or container service with an API** | Built for a person who writes the provisioning code and holds one account credential; no per-agent policy, no approval flow, no quota errors written for a model |
| **A hosted database with a REST API** | One service, no machine to run code on, no stack, no fork-and-destroy lifecycle driven by the agent |
| **A general-purpose sandbox SDK** | Runs the code, but the databases and apps the code needs live somewhere else and are set up by hand |

---

## Use Cases

- **Running generated code** — the agent runs a script, test suite or build in a sandbox instead of the user's machine
- **Tests against real services** — a real Postgres or Redis next to the code, not a mock
- **Safe migrations** — fork a database, try the change, destroy the copy
- **Preview links** — start an app from a GitHub repository and share a URL
- **Parallel agents** — one forked stack per task or worktree
