# ToolHive

> **"Run any MCP server securely, instantly, anywhere."**

| | |
|---|---|
| **Website** | https://toolhive.dev |
| **Docs** | https://docs.toolhive.dev |
| **GitHub** | https://github.com/stacklok/toolhive-studio |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |

---

## Official Website

https://toolhive.dev

---

## Official Repo

https://github.com/stacklok/toolhive-studio

---

## ⭐ How to Use (Agent Onboarding)

```bash
brew tap stacklok/tap
brew install thv
thv --help
```

Then discover and run MCP servers via `thv` runtime commands per docs.

Docs: https://docs.toolhive.dev

---

## Agent Skills

**Status:** ⚠️ No official AgentSkills package yet.

---

## MCP

**Status:** ✅ Core product.

ToolHive is specifically built to discover, run, and manage MCP servers with secure isolation for agent clients.

---

## What It Does

ToolHive provides a control plane for MCP servers: discovery, deployment, sandboxed execution, and secure connection for agent runtimes and coding assistants.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Product is centered on connecting MCP servers to AI agents |
| **Agent-specific primitive** | MCP server lifecycle + agent-facing server catalog |
| **Autonomy-compatible control plane** | Non-interactive server management + policy/security controls |
| **M2M integration surface** | API/CLI/app interfaces focused on MCP runtime operations |
| **Identity / delegation** | Per-environment credentials and controlled server exposure |

---

## Primary Primitives

- MCP server install/discovery
- Server runtime lifecycle management
- Isolation/security policy for MCP execution
- Agent-client connection management

---


## Autonomy Model

Agents can bootstrap and operate ToolHive non-interactively through CLI/API workflows:

1. Install `thv`
2. Discover/select MCP servers
3. Run servers in isolated runtime contexts
4. Connect agent clients to approved server endpoints

No per-action human confirmation is required for normal tool execution loops.

---

## Identity and Delegation Model

- Tool access is controlled by runtime/environment credentials.
- MCP servers are exposed intentionally via ToolHive-managed endpoints/sessions.
- Teams can constrain which servers are available to which agent environments.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `thv` install/run/manage lifecycle |
| MCP | Runs MCP servers for stdio/socket/HTTP-compatible clients |
| Docs/API | Operational configuration and server management workflows |

---

## Human-in-the-Loop Support

Optional. Human operators can approve which MCP servers are allowed in an environment, while agents invoke approved tools autonomously at runtime.

---

## Why Generic Alternatives Do Not Qualify

- Generic container managers orchestrate processes but are not MCP-native control planes for agent tool connectivity.

---

## Use Cases

- Standardizing MCP operations across teams
- Securely exposing approved tool servers to agents
- Reducing manual MCP setup in IDE agent environments
