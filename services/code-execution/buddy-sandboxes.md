# Buddy Sandboxes

> **"Secure, elastic infrastructure for AI-generated code and the apps it becomes - on a real Linux machine, not a throwaway container."**

| | |
|---|---|
| **Website** | https://buddy.works/sandboxes |
| **Docs** | https://buddy.works/docs/sandboxes |
| **GitHub** | https://github.com/buddy/sandbox-sdk |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |

---

## Official Website

https://buddy.works/sandboxes

---

## Official Repo

The hosted service is closed source. Public repositories: the TypeScript SDK https://github.com/buddy/sandbox-sdk (MIT), the Agent Skill https://github.com/buddy/buddy-plugin and the Claude Managed Agents reference implementation https://github.com/buddy/claude-managed-agents.

---

## How to Use (Agent Onboarding)

**The quickest path for an agent to start using this service.** A person signs in once in the browser (OAuth) or creates a token for the agent. After that the agent runs the whole Sandbox lifecycle on its own.

```
# MCP (remote HTTP, OAuth sign-in in the browser):
claude mcp add --transport http buddy "https://mcp.buddy.works/mcp?tools=sandboxes"

# Coding-time Skill:
npx skills add buddy/buddy-plugin  # drives the bdy CLI: bdy login, bdy sandbox create

# SDK (token with SANDBOX_READ and SANDBOX_WRITE scopes):
npm install @buddy-works/sandbox-sdk  # then: await Sandbox.create({ identifier: "my-sandbox" })

# Inside a running Sandbox (no identifier, no token):
this endpoint add -e 5173
```

**One-URL onboarding:** ⚠️ Not available. MCP needs an OAuth sign-in or a bearer token created by a person first.

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add buddy/buddy-plugin
```

| Skill | What It Teaches the Agent |
|---|---|
| `buddy` | Create a Sandbox in a project, copy code in, run the app bound to `0.0.0.0`, expose it with an endpoint, read logs; also tunnels, artifacts, domains and pipelines through the `bdy` CLI |

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | Hosted server, no public repository. Docs: https://buddy.works/docs/ai-agents/mcp |
| **Endpoint** | `https://mcp.buddy.works/mcp` (EU: `https://mcp.eu.buddy.works/mcp`, Asia: `https://mcp.asia.buddy.works/mcp`); `?tools=sandboxes` limits the tool set to Sandboxes |
| **Transport** | Remote HTTP; stdio through `bdy mcp` |
| **Auth** | Interactive OAuth, a personal access token as `Authorization: Bearer`, or the `bdy login` session through `bdy mcp` |
| **Compatible Clients** | Claude Code, Cursor, Codex, any MCP client |

---

## What It Does

Buddy Sandboxes are persistent Linux VMs for AI-generated code and agents. A Sandbox boots Ubuntu with Node, Docker, Go, Python 3, git, the `bdy` CLI and Claude Code preinstalled, with passwordless `sudo`. The disk survives stops and restarts, so files, packages and build caches are still there in the next session.

An agent creates a Sandbox over MCP, the SDK, the REST API or the CLI, fetches a repository into it, runs commands, starts long-running apps and publishes a port as an HTTPS endpoint. It can save a snapshot and start new Sandboxes from it, so each agent starts from a prepared toolchain instead of running `npm install` again. An optional inactivity timeout stops the machine, and traffic on an endpoint starts it again.

Inside the Sandbox, the `this` command changes the machine the agent is on: endpoints, apps, snapshots, resources, stop and destroy. It needs no Sandbox name and no access token.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Buddy Sandboxes are persistent Linux VMs for AI-generated code and agents." — https://buddy.works/sandboxes |
| **Agent-specific primitive** | The `this` command: "An agent dropped into a Sandbox does not know the machine's name and has no access token - and still needs to expose the dev server it just started." — https://buddy.works/docs/sandboxes/self-management ; agents are a separate section in Sandbox permissions, assigned apart from members and groups — https://buddy.works/docs/sandboxes/permissions-and-security |
| **Autonomy-compatible control plane** | The agent creates, runs, exposes, snapshots and deletes a Sandbox with no clicks. Limits: per-Sandbox access level for each agent, tokens scoped to Sandbox operations, allowed pipelines, an inactivity timeout, a workspace IP whitelist for the API and CLI |
| **M2M integration surface** | Remote MCP server, TypeScript SDK (`@buddy-works/sandbox-sdk`), REST API (https://buddy.works/docs/api/sandboxes), `bdy sandbox` CLI, `this` inside the Sandbox |
| **Identity / delegation** | Agents get their own rows in Sandbox permissions (Manage, View-only, Project role, None); repository and artifact access is granted to the Sandbox, not to a person; the Activity tab records lifecycle operations and executed commands — https://buddy.works/docs/sandboxes/logs |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Sandbox** | Persistent Ubuntu VM with root access, Docker inside and a disk that survives restarts |
| **`this` command** | Changes the current Sandbox from inside, with no identifier and no token |
| **Command** (`execute-sandbox-command`, `runCommand`) | Runs a command and returns status, exit code and output; detached commands keep logs to read later |
| **App** | A supervised long-running process that starts again on every boot |
| **Endpoint** | HTTPS URL for a port, optionally behind Buddy sign-in, with request logging |
| **Snapshot** | Saved machine state; new Sandboxes start from it |
| **Fetch** | A repository or artifact version pulled into a directory, with no credentials inside the Sandbox |
| **Timeout / wake-up** | Stops after a set time without activity and starts again on endpoint traffic |

---

## Autonomy Model

1. A person connects the MCP server once (OAuth) or gives the agent a token scoped to Sandboxes.
2. The agent creates a Sandbox, from a snapshot when one exists, with the repository fetched in.
3. The agent runs commands and reads exit codes and output; long commands run detached and the agent reads their logs.
4. The agent starts the app and publishes its port as an endpoint, from outside or with `this endpoint add` from inside.
5. Before a risky change the agent takes a snapshot.
6. When the task is done the agent deletes the Sandbox, or the timeout stops it. Cleanup can also run as a pipeline on the Sandbox time-out event.

---

## Identity and Delegation Model

- Sandbox permissions have three sections: Member, Agent and Group. An agent's row decides its access to that Sandbox: Manage, View-only, Project role or None.
- Automation uses a token limited to Sandbox scopes (`SANDBOX_READ`, `SANDBOX_WRITE`, `SANDBOX_MANAGE`) instead of a full personal token.
- Repository and artifact access is granted on the resource to a single Sandbox, to all Sandboxes or to an environment, as read-only, read-write or none. Fetching and pushing need no credentials inside the machine.
- The `this` command acts only on the Sandbox it runs in.
- A workspace IP whitelist limits who can reach the REST API and the CLI.
- The Activity tab records who started, stopped or deleted a Sandbox and what was executed in it. Command, app, setup and HTTP request logs are readable over the API, the SDK and MCP.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | `https://mcp.buddy.works/mcp`, remote HTTP, OAuth or bearer token; `bdy mcp` as a stdio proxy |
| REST API | https://buddy.works/docs/api/sandboxes |
| SDK | `@buddy-works/sandbox-sdk` (TypeScript, MIT) |
| CLI | `bdy sandbox` (`bdy sb`); `this` inside a Sandbox |
| YAML | Sandbox definition with resources, apps, endpoints and permissions |
| Agent Skill | `npx skills add buddy/buddy-plugin` |

---

## Human-in-the-Loop Support

A person approves the OAuth connection or creates the token, and sets the agent's access level per Sandbox. Workspace owners and administrators always keep Manage on every Sandbox. Endpoints can require Buddy sign-in, so only workspace members see what the agent published. Deleting a Sandbox is irreversible; the docs recommend starting agents on read-only access and a narrow tool set.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A plain cloud VM** | Gives the agent a shell, but changing the machine from inside needs its ID and a credential; no agent principal in permissions, no MCP tools for the lifecycle |
| **A container service with an API** | Throwaway filesystem by default; volumes, images and registry pushes are set up by a person |
| **A local dev container** | Runs on the user's machine and shares its resources and credentials |

---

## Use Cases

- **Coding agent off the laptop** — Claude Code or another agent works in a Sandbox with the repository fetched in and pushes its work back
- **Preview URLs** — the agent starts the app and shares an HTTPS endpoint, optionally behind Buddy sign-in
- **One machine per session** — Claude Managed Agents run each session in its own worker Sandbox created from a snapshot
- **Checkpoint before risk** — snapshot before a migration or dependency upgrade, start a new Sandbox from it if it breaks
- **Code execution backend** — a product creates Sandboxes per user or per task through the SDK
