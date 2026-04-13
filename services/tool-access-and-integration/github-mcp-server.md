# GitHub MCP Server

> **"The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and chatbots the ability to read repositories and code files, manage issues and PRs, analyze code, and automate workflows."**

| | |
|---|---|
| **Website** | https://github.com/github/github-mcp-server |
| **Docs** | https://github.com/github/github-mcp-server#readme |
| **GitHub** | https://github.com/github/github-mcp-server |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/github/github-mcp-server?style=social)](https://github.com/github/github-mcp-server) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |

---

## Official Website

https://github.com/github/github-mcp-server

---

## Official Repo

https://github.com/github/github-mcp-server

---

## How to Use (Agent Onboarding)

**Remote MCP (hosted by GitHub)** — HTTP MCP endpoint; configure your MCP host (VS Code 1.101+, Cursor, Claude Desktop, Windsurf, Copilot CLI, etc.):

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

**Personal Access Token (PAT)** variant — see [README](https://github.com/github/github-mcp-server#remote-github-mcp-server) for `Authorization: Bearer` header patterns.

**Local MCP server** — if the host does not support remote MCP, use the [local GitHub MCP Server](https://github.com/github/github-mcp-server?tab=readme-ov-file#local-github-mcp-server) install path in the same repository.

**Policies** — enable applicable [policies](https://github.com/github/github-mcp-server/blob/main/docs/policies-and-governance.md) for your org.

Full guides: [Remote Server Documentation](https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md), host-specific pages under `docs/installation-guides/`.

---

## Agent Skills

**Status:** ⚠️ Not yet published as a dedicated `npx skills add …` pack for the MCP server

Search community skills: `npx clawhub@latest search github-mcp`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Remote HTTP MCP + local server options

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/github/github-mcp-server |
| **Transport** | Streamable HTTP (`https://api.githubcopilot.com/mcp/`) · local modes per docs |
| **Compatible Clients** | VS Code, Cursor, Claude Desktop, Windsurf, Copilot CLI, Codex, JetBrains + Copilot, and other hosts listed in the README |

---

## What It Does

The GitHub MCP Server exposes **GitHub platform operations as MCP tools**: browsing and querying repositories, working with issues and pull requests, CI/CD and Actions intelligence, security/Dependabot context, and collaboration surfaces. It is explicitly aimed at **AI agents and assistants** automating multi-step development workflows through natural language-driven tool use in MCP hosts.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"This gives **AI agents**, assistants, and chatbots the ability to…"* and *"Built for developers who want to connect their **AI tools** to GitHub… from simple natural language queries to **complex multi-step agent workflows**"* — [repo README](https://github.com/github/github-mcp-server) |
| **Agent-specific primitive** | **MCP toolsets over GitHub domain objects** (repos, issues, PRs, Actions, security findings) — shaped for LLM tool-calling, not a generic REST tutorial |
| **Autonomy-compatible control plane** | After OAuth or PAT setup, agents invoke tools without per-action UI clicks (subject to org policy and host permissions) |
| **M2M integration surface** | Remote MCP URL, PAT headers, local server modes, Go implementation — see repo docs |
| **Identity / delegation** | **OAuth or PAT** scopes determine what the agent may do; GitHub audit trail attributes actions to the authenticated identity; [policies and governance](https://github.com/github/github-mcp-server/blob/main/docs/policies-and-governance.md) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Repository intelligence** | Search/browse code, commits, structure |
| **Issues & PRs** | Create, update, triage, review-oriented workflows |
| **CI/CD & Actions** | Workflow runs, failures, release-related context |
| **Security context** | Dependabot and security signal surfacing (per toolsets) |
| **Toolset configuration** | Selectable tool groups — see remote server docs |
| **Insiders mode** | Early tools via URL path or header — [README](https://github.com/github/github-mcp-server) |

---

## Autonomy Model

```
Human or admin configures MCP host with GitHub OAuth or PAT + policies
  ↓
Agent plans a task (e.g. fix CI, update PR, summarize security alerts)
  ↓
Agent calls GitHub MCP tools (issues, PRs, Actions, code search, …)
  ↓
GitHub enforces permissions; results stream back into the agent loop
```

---

## Identity and Delegation Model

- **OAuth** — user or org consent establishes delegated access for the MCP client; token scopes bound what automated tool calls may do.
- **PAT** — static bearer with explicit scopes; same GitHub audit semantics.
- **Enterprise** — README documents GitHub Enterprise Cloud / Server paths; admins control availability.
- **Policy layer** — `policies-and-governance.md` describes governance expectations for enterprise use.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **Remote MCP** | `https://api.githubcopilot.com/mcp/` (insiders: `/mcp/insiders` or header per README) |
| **Local server** | Documented in repo for hosts without remote MCP |
| **Source** | Go — see https://github.com/github/github-mcp-server |

---

## Human-in-the-Loop Support

Org admins configure **policies** and OAuth apps; users complete OAuth consent or PAT setup. High-risk merges or branch protections still follow GitHub's native rules independent of MCP.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw GitHub REST without MCP** | No standard **tool schema + discovery** for diverse MCP hosts; higher bespoke glue per agent runtime |
| **Human-only GitHub UI** | Not M2M; blocks autonomous agent loops |
| **Generic iPaaS** | Not centered on **GitHub developer objects** and copilot-remote MCP distribution |

---

## Use Cases

- **Agent-driven PR workflows** — draft descriptions, request reviews, iterate on CI failures
- **Repo onboarding** — agent maps structure, dependencies, and hot files for a task
- **Security triage** — correlate alerts with code context via tool calls
- **Ops agents** — monitor Actions and releases with structured GitHub data
