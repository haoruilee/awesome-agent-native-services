# Sandboxer

> **"The agent swarm platform."**

| | |
|---|---|
| **Website** | https://sandboxer.com |
| **Docs** | https://sandboxer.com/docs/mcp |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |

---

## Official Website

https://sandboxer.com

---

## Official Repo

The hosted service is closed source and has no public repository. The public packages are the TypeScript SDK [`sandboxer-sdk` on npm](https://www.npmjs.com/package/sandboxer-sdk), the Python SDK [`sandboxer-sdk` on PyPI](https://pypi.org/project/sandboxer-sdk/) (imported as `sandboxer`) and the MCP stdio adapter [`sandboxer-mcp` on npm](https://www.npmjs.com/package/sandboxer-mcp).

---

## How to Use (Agent Onboarding)

> **URL Onboarding with human steps: the agent reads one document and connects itself, but a person signs in with OAuth or creates an API key for it once.**

**One-sentence instruction:**

```
Read https://sandboxer.com/docs/mcp.md and follow the "If you are an agent setting this up" steps to connect the Sandboxer MCP server.
```

**Interaction pattern:** `URL Onboarding` ⚠️ — partial.

People still have to do one thing:
- In a client that can open a browser (Claude, ChatGPT, Claude Code, Codex, Cursor), sign in to Sandboxer and click **Allow** when the client connects (OAuth 2.1).
- In a headless run, create an API key at https://sandboxer.com/app/api-keys (a scoped key such as the `ci` preset is enough) and put it in the agent's `SANDBOXER_API_KEY` environment variable. The docs say an agent can't create this key itself.

Remote MCP (Streamable HTTP):

```
claude mcp add --transport http --scope user sandboxer https://sandboxer.com/mcp
```

Local stdio adapter (reads `SANDBOXER_API_KEY`):

```
claude mcp add sandboxer -- npx -y sandboxer-mcp
```

SDK / REST:

```
npm install sandboxer-sdk   # or: pip install sandboxer-sdk
curl -sS https://sandboxer.com/api/v1/sandboxes -H "Authorization: Bearer $SANDBOXER_API_KEY"
```

---

## Agent Skills

**Status:** ⚠️ Not yet published

Search community skills: `npx clawhub@latest search sandboxer`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | Hosted endpoint `https://sandboxer.com/mcp`; stdio adapter [`sandboxer-mcp`](https://www.npmjs.com/package/sandboxer-mcp) (MIT) |
| **Registry** | Official MCP Registry: `com.sandboxer/mcp` |
| **Transport** | Streamable HTTP; stdio through `npx -y sandboxer-mcp` or `sbx mcp` |
| **Auth** | OAuth 2.1 (PKCE, dynamic client registration or a Client ID Metadata Document), or an API key as `Authorization: Bearer <key>` |
| **Compatible Clients** | Claude (claude.ai, Claude Desktop), ChatGPT, Claude Code, Codex, Cursor, any MCP client |

The hosted server has 20 tools (create, exec, files, ports, snapshots, stop, resume, delete and coding-agent tasks); the local `sbx mcp` server adds `handoff_session`. Docs: https://sandboxer.com/docs/mcp

---

## What It Does

Sandboxer runs cloud sandboxes for AI agents. Each sandbox is a persistent Ubuntu 24.04 virtual machine (a Cloud Hypervisor microVM with its own kernel), not a container: root, systemd, Docker, nested KVM, SSH and an HTTPS URL for any port. An agent creates sandboxes, runs commands, reads and writes files, publishes ports, saves named snapshots and forks sandboxes through the REST API, the `sbx` CLI, the TypeScript and Python SDKs or the MCP server.

Coding agents are installed in every sandbox: Claude Code, Codex, OpenCode, Pi, Kimi Code and Mistral Vibe. A caller prompts them over the API (`POST /api/v1/sandboxes/{id}/prompt`), streams their work as structured events, keeps several conversations running side by side, and steers or interrupts a running turn. The provider keys are the account's own.

Stopping a sandbox saves its memory as well as its disk, so processes are still running after resume, and a stopped sandbox bills no running time. An idle sandbox pauses itself and wakes on the next API call or request to its URL. Forks are copy-on-write copies of a sandbox's disk, and named snapshots act as templates, so many agents can start from one prepared state. Billing is per second while a sandbox runs; there are no GPUs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "The agent swarm platform. Throw compute at the problem. Sandboxer runs your agent swarm: thousands of isolated agents in parallel, coordinated toward one goal, priced per second." — https://sandboxer.com ; "Sandboxer runs cloud sandboxes for AI agents and people" — https://sandboxer.com/llms.txt. People can also use sandboxes by hand over SSH; agents are the primary consumer. |
| **Agent-specific primitive** | Integrated agents: `POST /sandboxes/{id}/prompt` starts a harness in the sandbox, streams structured events, keeps the session so the next prompt continues it, runs several conversations at once, and `/steer` and `/interrupt` change a running turn — https://sandboxer.com/docs/agents. Memory-preserving stop and resume, idle auto-pause with wake on request, copy-on-write forks. |
| **Autonomy-compatible control plane** | An agent creates, runs commands in, prompts, forks, snapshots, stops, resumes and deletes sandboxes with no per-action confirmation. Limits: scoped API keys restrict a key to chosen actions, sandboxes and environments with an expiry; `sandbox.delete-own` deletes only sandboxes the key created; plan and rate limits apply; sandboxes created through MCP stop after an hour unless `ttlSeconds` says otherwise — https://sandboxer.com/docs/api-keys , https://sandboxer.com/docs/mcp |
| **M2M integration surface** | REST API (`/api/v1`, OpenAPI at https://sandboxer.com/openapi.yaml), `sbx` CLI, TypeScript and Python SDKs, hosted MCP over Streamable HTTP and a stdio adapter; the dashboard is a secondary surface |
| **Identity / delegation** | Every sandbox gets its own `SANDBOXER_TOKEN`, limited to that sandbox (it can't create, fork or delete sandboxes or read the account); separate scoped keys per agent or pipeline with expiry, rotation and revocation; `GET /api-keys/{id}/usage` lists the sandboxes a key created; each MCP client is listed as its own connection that can be disconnected — https://sandboxer.com/docs/api-keys , https://sandboxer.com/docs/mcp |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Sandbox** (`create_sandbox`, `POST /sandboxes`) | A persistent Ubuntu 24.04 microVM with root, systemd, Docker and nested KVM, created from a base image or a named snapshot |
| **Command** (`exec`, `command_status`, `kill_command`) | Runs a shell command in the foreground (stdout, stderr, exit code) or detached, with incremental output |
| **Files** (`read_file`, `write_file`) | Reads and writes files in the sandbox; `sbx scp` for larger transfers |
| **Hosted port** (`host_port`) | Serves a port on an HTTPS URL, private with a token or public |
| **Integrated agent prompt** (`/prompt`, `/steer`, `/interrupt`, `/events`) | Runs Claude Code, Codex, OpenCode, Pi, Kimi Code or Mistral Vibe in the sandbox as structured, resumable conversations |
| **Agent task** (`create_task`, `task_status`) | Runs a coding agent on a connected GitHub repo in its own sandbox and ends with a pull request |
| **Stop / resume** (`stop_sandbox`, `resume_sandbox`) | Saves memory and disk and stops billing; resume restores running processes |
| **Idle auto-pause** (`idleStopMinutes`) | Pauses an unused sandbox with its memory; it wakes on the next API call or URL request |
| **Fork and named snapshot** (`sbx fork`, `save_snapshot`) | Copy-on-write disk copies and versioned templates for starting many sandboxes from one state |
| **Scoped key / in-sandbox token** | Per-agent API keys limited by action, sandbox, environment and expiry; `SANDBOXER_TOKEN` per sandbox |

---

## Autonomy Model

1. A person connects the agent once: OAuth sign-in in an MCP client, or a scoped API key in `SANDBOXER_API_KEY`.
2. The agent calls `create_sandbox` (or `POST /api/v1/sandboxes`), optionally from a named snapshot.
3. The agent runs commands, writes files, installs packages and starts services with `exec`, or prompts an integrated coding agent inside the sandbox and follows its events.
4. The agent publishes a port with `host_port` to check what it built, and forks or snapshots a prepared sandbox to run more agents from the same state.
5. When the work pauses, the agent calls `stop_sandbox` (memory kept, no running time billed) or lets idle auto-pause do it; `resume_sandbox` continues where it left off.
6. When the work is done, the agent calls `delete_sandbox` with an explicit id.

---

## Identity and Delegation Model

- API keys authenticate machines; each key is scoped by action (`sandbox.create`, `exec`, `file.write`, `agent.prompt`, `sandbox.delete-own` and others), by sandbox or environment, and by expiry. Presets include `read-only`, `full-sandbox`, `ci` and `admin`.
- Every sandbox gets `SANDBOXER_TOKEN` for calls it makes about itself. It can run commands, read and write files and prompt its own sandbox, but can't create, resume, fork or delete sandboxes, and account endpoints such as `/me`, `/billing/overview` and `/api-keys` answer `403 api_key_action_forbidden`.
- Keys are rotated and revoked on their own; a revoked key's sandboxes keep running, and `GET /api-keys/{id}/usage` lists the sandboxes each key created, readable after revocation.
- MCP clients that sign in get their own connection, listed under API keys as "Claude (MCP)", "ChatGPT (MCP)" and so on, which can be disconnected at once; a connector token only works on `/mcp`.
- A key's scopes apply tool by tool on MCP, and creating keys needs a browser session or an `admin` key.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `https://sandboxer.com/api/v1`, OpenAPI at https://sandboxer.com/openapi.yaml |
| MCP | `https://sandboxer.com/mcp`, Streamable HTTP, OAuth 2.1 or API key; registry name `com.sandboxer/mcp` |
| MCP stdio adapter | `npx -y sandboxer-mcp` or `sbx mcp` |
| CLI | `sbx` for macOS, Linux and Windows (`curl -fsSL https://sandboxer.com/install \| sh`) |
| TypeScript SDK | `sandboxer-sdk` on npm |
| Python SDK | `sandboxer-sdk` on PyPI, imported as `sandboxer` |
| Events | Integrated-agent events by polling or server-sent events (`/sandboxes/{id}/events`) |
| Docs for agents | https://sandboxer.com/llms.txt, https://sandboxer.com/docs/mcp.md |

---

## Human-in-the-Loop Support

No human step is needed in the agent's own loop after the one-time sign-in or key. A person can watch a sandbox's desktop stream while an integrated agent does GUI work, steer or interrupt a running conversation, SSH into the sandbox, and disconnect an MCP client or revoke a key at any time. MCP tools are marked read-only or destructive, so a client can ask for confirmation before destructive calls.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A cloud VM (EC2, a dedicated server)** | Provisioned and managed for people; no per-sandbox agent credential, no API to prompt and steer a coding agent inside the machine, no memory-preserving pause with wake on request, no MCP server for the agent to create and fork its own machines |
| **A Docker container** | Shares the host kernel and has no agent-facing lifecycle, identity or MCP surface; Sandboxer gives each sandbox its own microVM kernel with Docker inside |

---

## Use Cases

- **Many coding agents in parallel** — each agent gets its own VM, started from one named snapshot or forked from a prepared sandbox
- **Long-running agent work that pauses** — stop a sandbox with its agent and dev server in memory, pay no running time while it waits, and resume where it left off
- **Prompting coding agents over an API** — run Claude Code or Codex inside a sandbox, stream their events and steer them from your own orchestrator
- **Preview URLs for what an agent built** — publish any port as an HTTPS URL, private with a token or public
- **Docker and nested virtualization** — run Docker, kind or k3s, or `/dev/kvm` workloads such as the Android emulator, inside the sandbox
