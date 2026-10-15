# Latchkey

> **"CI your coding agents can run, read and fix."**

| | |
|---|---|
| **Website** | https://latchkey.dev |
| **Docs** | https://latchkey.dev/documentation/connect-your-ai-agent |
| **GitHub** | https://github.com/latchkey-dev |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |

---

## Official Website

https://latchkey.dev

---

## Official Repo

The platform and the hosted MCP server are closed source. Public repositories: https://github.com/latchkey-dev/cache-action and https://github.com/latchkey-dev/docker-cache-action (GitHub Actions used on the runners).

---

## How to Use (Agent Onboarding)

**The quickest path for an agent to start using this service.** The account owner creates an API key once in the Latchkey dashboard (agents are told never to create accounts or keys themselves); everything after that is machine-driven.

```
# Agent instructions (when to use it, how to call it, MCP / REST / CLI):
Read https://latchkey.dev/agent.txt and follow the instructions.

# MCP (Streamable HTTP):
claude mcp add --transport http latchkey https://latchkey.dev/mcp --header "Authorization: Bearer $LATCHKEY_TOKEN"

# CLI:
npm install -g @latchkeydev/cli  # then: latchkey run 'npm test'
```

---

## Agent Skills

**Status:** ⚠️ Not yet published

Search community skills: `npx clawhub@latest search latchkey`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | Hosted, closed source. Descriptor: https://latchkey.dev/.well-known/mcp/manifest.json |
| **Endpoint** | `https://latchkey.dev/mcp` |
| **Transport** | Streamable HTTP |
| **Auth** | Latchkey API key as `Authorization: Bearer` |
| **Tools / prompts** | 8 tools (`list_failed_runs`, `get_failure_bundle`, `get_run_status`, `tail_run_logs`, `dispatch_workflow`, `run_job`, `get_job_status`, `get_job_logs`), 2 prompts (`fix`, `triage_failures`) |
| **Compatible Clients** | Claude Code, Cursor, any MCP client |

---

## What It Does

Latchkey gives coding agents a place to actually execute and verify work. `run_job` (or `latchkey run` from the CLI) runs one command on a fresh ephemeral Ubuntu 24.04 x86_64 runner with no workspace and no GitHub in the path, then returns the command's own exit code and logs, so an agent can run a test suite on a clean machine before it opens a pull request.

The same runners execute GitHub Actions jobs and diagnose failing steps while the job is still running: exit codes, then a pattern library, then a time-boxed sandboxed AI stage. Transient failures (registry timeouts, OOM kills, full disks, missing tools) are fixed on the ephemeral runner and retried; real defects are never retried or masked. What the runner cannot fix reaches the agent as a failure bundle: root cause, exact failing file and secret-scrubbed logs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "CI your coding agents can run, read and fix. Self-healing GitHub Actions runners, plus a CLI and MCP server your coding agents can drive." — https://latchkey.dev/ ; agent instructions at https://latchkey.dev/agent.txt |
| **Agent-specific primitive** | `run_job`: one command on a fresh runner with no workspace and no GitHub in the path, returning the real exit code; `get_failure_bundle`: root cause, failing file and scrubbed logs shaped for an agent to act on — https://latchkey.dev/.well-known/mcp/manifest.json |
| **Autonomy-compatible control plane** | Agents run jobs, read bundles and (when the key allows it) dispatch workflows with no human step; keys are read-only by default and each write is a separate opt-in at key creation — https://latchkey.dev/documentation/connect-your-ai-agent |
| **M2M integration surface** | MCP (Streamable HTTP), REST Jobs API with OpenAPI 3.1 (https://latchkey.dev/openapi.json), CLI, agent.txt and llms.txt |
| **Identity / delegation** | Workspace-scoped bearer keys with explicit scopes (`jobs:read`, `jobs:run`, `mcp:dispatch`), named per tool or machine, optional expiry, revocable — https://latchkey.dev/documentation/connect-your-ai-agent |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Fresh-runner job** (`run_job`, `latchkey run`) | One command on a new ephemeral Linux runner; working tree packed with `.gitignore` applied and credential-shaped files held back; command's own exit code returned |
| **Failure bundle** (`get_failure_bundle`) | Root cause, exact failing file and secret-scrubbed logs for a CI failure the runner could not repair |
| **Failure feed** (`list_failed_runs`) | Recent failures self-heal could not turn green on its own |
| **Run and job state** (`get_run_status`, `tail_run_logs`, `get_job_status`, `get_job_logs`) | Status, per-job timing and cursor-walked logs |
| **Workflow dispatch** (`dispatch_workflow`) | Trigger a `workflow_dispatch` run; requires a key created with dispatch allowed |
| **Self-healing runner** | Transient step failures diagnosed and fixed in-run on the ephemeral machine, then retried |

---

## Autonomy Model

1. The account owner creates a workspace API key once and chooses its scopes (read-only by default; dispatch and running jobs are opt-in).
2. The agent connects to `https://latchkey.dev/mcp` (or uses the REST API or CLI) with that key.
3. Before opening a pull request, the agent calls `run_job` with its test command and reads the exit code and logs from a clean machine.
4. When a GitHub Actions run fails, the runner first tries to repair transient failures in place; real failures stay red.
5. The agent calls `list_failed_runs` and `get_failure_bundle`, fixes the cause, pushes, and (if allowed) calls `dispatch_workflow`, then watches `get_run_status` until the run is green.

---

## Identity and Delegation Model

- Keys are workspace-scoped: the workspace is derived from the key, so a key can only see its own workspace's data.
- Read-only by default; `mcp:dispatch` (workflow dispatch) and `jobs:run` (one-off jobs, includes `jobs:read`) are explicit opt-ins chosen when the key is created.
- Keys are named per tool or machine (for example "Cursor on my laptop"), can expire, and can be revoked at any time; write-capable keys lose access immediately on revocation.
- Logs returned to the agent are secret-scrubbed. Jobs started through MCP or the CLI are recorded and billed as their own line.
- Limit, stated plainly: there is no per-agent identity beyond the key; one key is shared by whatever agent holds it.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | `https://latchkey.dev/mcp`, Streamable HTTP, 8 tools, 2 prompts |
| REST Jobs API | `https://api.latchkey.dev`, OpenAPI 3.1 at https://latchkey.dev/openapi.json |
| CLI | `@latchkeydev/cli` — https://latchkey.dev/documentation/latchkey-cli |
| Agent instructions | https://latchkey.dev/agent.txt, https://latchkey.dev/llms.txt, markdown twin of every docs page at URL + `.md` |
| GitHub Actions | `runs-on: latchkey-small` (and larger sizes) for existing workflows |

---

## Human-in-the-Loop Support

Humans set the boundary once: the account owner creates keys and decides whether an agent may dispatch workflows or run jobs. Self-heal never edits repository code; fixes only touch the ephemeral runner, and durable fixes arrive as pull requests for human review. Real code failures are never retried or hidden, so a human (or the agent) always sees them. A human dashboard exists for cost and reliability analytics but is not needed for any of the agent flows above.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **GitHub-hosted runners + Actions REST API** | Built around human-triggered workflows and the GitHub UI: a failed run is a red check and a raw log with no root-cause bundle, and there is no way to run one command on a clean machine without committing and pushing a workflow |
| **Faster managed runners** | Speed up the same human workflow; they do not repair failures in-run or expose an agent-facing failure and job surface |
| **General-purpose code sandboxes** | Execute arbitrary code but carry no CI context: no workflow runs, failure history or dispatch |

---

## Use Cases

- **Pre-push verification** — the agent runs the full test suite on a fresh Linux runner and only opens a PR when the real exit code is 0
- **Fixing red CI** — the agent pulls the failure bundle for a failed run, fixes the root cause and re-runs the workflow
- **Failure triage** — `triage_failures` groups recent failures so the agent can prioritise and route them
- **Isolated command execution** — run a build or test command without touching the developer's machine or queueing on GitHub Actions
