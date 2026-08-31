# SandBase Harness

> **"A local-first runtime for AI agents."**

| | |
|---|---|
| **Website** | https://github.com/sandbaseai/sandbase-harness |
| **Docs** | https://github.com/sandbaseai/sandbase-harness/tree/main/docs |
| **GitHub** | https://github.com/sandbaseai/sandbase-harness |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/sandbaseai/sandbase-harness?style=social)](https://github.com/sandbaseai/sandbase-harness) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure](README.md) |
| **Status** | Open source · Apache-2.0 · self-hosted/local-first |

## Official Website

https://github.com/sandbaseai/sandbase-harness

## Official Repo

https://github.com/sandbaseai/sandbase-harness

## How to Use (Agent Onboarding)

Follow the [installation guide](https://github.com/sandbaseai/sandbase-harness/blob/main/docs/installation.md). Supported entry points include the local TypeScript runtime/CLI, Docker, Kubernetes, and self-hosted workers. For the MCP bridge, use the metadata in [`server.json`](https://github.com/sandbaseai/sandbase-harness/blob/main/server.json) and the official [MCP Registry entry](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.sandbaseai%2Fsandbase-harness).

## Agent Skills

**Status:** ⚠️ No first-party Agent Skill package is published.

## MCP

**Status:** ✅ A native stdio MCP bridge is published.

| Detail | Value |
|---|---|
| **Server metadata** | [`server.json`](https://github.com/sandbaseai/sandbase-harness/blob/main/server.json) |
| **Registry identity** | `io.github.sandbaseai/sandbase-harness` |
| **Transport** | stdio |
| **Auth** | Configured managed-agent endpoint/API key; see installation guide |
| **Compatible clients** | MCP clients that support stdio servers |

## What It Does

Official README: **"A local-first runtime for AI agents. Sessions, sandboxed tools, memory, credentials, audit trails, and a built-in Console — all running on your machine or in your own infrastructure."** — [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness)

SandBase Harness is a local-first runtime for operating multi-step AI-agent sessions. It combines persistent sessions and resumable event streams with sandboxed turns, MCP toolsets, credential scopes, permission policies, approvals, artifacts, memory, audit records, and replay. It can run on an operator's machine or in self-hosted infrastructure; the exact isolation boundary depends on the selected and configured execution backend.

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Official README: **"A local-first runtime for AI agents. Sessions, sandboxed tools, memory, credentials, audit trails, and a built-in Console — all running on your machine or in your own infrastructure."** — [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) |
| **Agent-specific primitive** | Persistent sessions, resumable streams, sandboxed turns, tool trajectories, artifacts, audit records, and replay model agent execution directly. |
| **Autonomy-compatible control plane** | Agents can operate through the HTTP/API and MCP surfaces after configuration; permissions, credentials, approvals, audit, and replay constrain or review execution. |
| **Machine-to-machine integration** | Local HTTP API, native stdio MCP bridge, TypeScript runtime/CLI, Docker, Kubernetes, and worker deployment paths. |
| **Identity / delegation** | Session, event, audit, and replay records attribute execution; credential and permission configuration defines the delegation boundary. |

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent session** | Persistent, resumable session and event-stream lifecycle. |
| **Sandboxed turn** | Tool execution isolated according to the configured backend. |
| **MCP toolset** | Native stdio bridge for exposing managed-agent tools to MCP clients. |
| **Credential scope** | Runtime-managed credentials and permission policies for tool access. |
| **Audit and replay** | Records, artifacts, and replay support for inspecting execution trajectories. |
| **Memory** | Agent/session memory exposed as a first-class runtime concern. |

## Autonomy Model

1. Configure the runtime and any managed-agent endpoint/API key described by the installation guide.
2. Start a local, Docker, Kubernetes, or self-hosted worker deployment.
3. Create or resume an agent session through the API, runtime/CLI, or MCP bridge.
4. Execute multi-step turns using configured toolsets, credentials, policies, and optional approvals.
5. Inspect artifacts and audit records, then resume or replay the session as needed.

## Identity and Delegation Model

- Sessions and runs are represented by runtime records that can be inspected and resumed.
- Credential scopes and permission policies define which tools an agent may use.
- Approval gates can add human review to write-capable or sensitive operations.
- Local-first storage keeps the default runtime under the operator's infrastructure.
- Isolation is backend/deployment dependent; this entry does not claim identical guarantees for every configuration.

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP/API | Local runtime and Console surface |
| MCP | Native stdio bridge; metadata in `server.json` |
| TypeScript | Runtime and CLI packages |
| Deployment | Local process, Docker, Kubernetes, and self-hosted worker paths |

## Human-in-the-Loop Support

Permission policies and approval controls can require review before configured actions proceed. Audit records and replay provide post-action inspection; whether an approval is required is a deployment and policy choice.

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Is Different |
|---|---|
| **Generic model loop** | Does not provide the combined session, sandbox, credential, artifact, audit, and replay lifecycle. |
| **Generic MCP directory** | Catalogs servers but does not execute or govern agent sessions. |
| **Standalone container runner** | Provides execution isolation only, without the runtime's session and tool-trajectory model. |

## Use Cases

- Self-hosted coding and research agents with resumable sessions.
- MCP-connected workflows requiring credential and permission boundaries.
- Long-running tool loops where artifacts, audit records, and replay matter.
- Local development that later moves to Docker, Kubernetes, or worker deployment.
