---
title: "GitHub MCP Server | Agent-Native Services"
service_name: "GitHub MCP Server"
description: "The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and chatbots the ability to read repositories and…"
permalink: /services/github-mcp-server/
page_kind: service
service_slug: "github-mcp-server"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/github-mcp-server.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/github-mcp-server.md"
tagline: "The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and chatbots the ability to read repositories and code files, manage issues and PRs, analyze code, and automate workflows"
website: "https://github.com/github/github-mcp-server"
repository: "https://github.com/github/github-mcp-server"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/github/github-mcp-server" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/github/github-mcp-server#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/github/github-mcp-server" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/github-mcp-server.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

GitHub runs the remote version of this server itself, at an HTTP endpoint under api.githubcopilot.com, so an agent host can connect without installing anything. Hosts that cannot speak remote MCP run a local build of the same Go server instead. Either way, every action lands on GitHub under the identity whose OAuth grant or personal access token the host holds, and GitHub's own permissions, branch protections, and audit log apply to it.

### Toolsets over repositories, issues, and Actions

The dossier describes GitHub platform operations exposed as MCP tools. Agents can search and browse code, commits, and repository structure; create, update, and triage issues and pull requests; read workflow runs, failures, and release context from Actions; and surface Dependabot and other security signals. Tools come in selectable toolsets, and an insiders mode, enabled by URL path or header, adds early tools.

The remote endpoint is `https://api.githubcopilot.com/mcp/`, configured as an HTTP server in the host. The dossier lists VS Code, Cursor, Claude Desktop, Windsurf, Copilot CLI, Codex, and JetBrains with Copilot among compatible hosts. A token variant sends an `Authorization: Bearer` header. The local server path is documented in the same repository for hosts without remote MCP support. No dedicated Agent Skill pack exists yet; the dossier points to a community search. The [repository README](https://github.com/github/github-mcp-server#readme) is the documentation.

### A first-party server among MCP connectors

Most of [Tool Access & Integration](/categories/tool-access-and-integration/) is either a single vendor's server or infrastructure for running many. This one is a first-party server, like [Framelink MCP for Figma](/services/framelink-figma-mcp/) for design files or [MCP Toolbox for Databases](/services/google-mcp-toolbox/) for databases, scoped to one platform's objects. [ToolHive](/services/toolhive/) is a different layer, a way to run MCP servers securely wherever you choose, which can apply to the local GitHub server. [Snyk Agent Scan](/services/snyk-agent-scan/) scans MCP servers and skills, useful for any organization standardizing its allowlist. The [MCP getting-started guide](/guides/getting-started-with-mcp-servers/) walks through host configuration for remote and local servers.

### Scope before you connect

Identity is the whole risk model here. OAuth consent or a token's scopes bound what an agent can do, and the agent acts as that user. Use the narrowest token that covers the task, prefer OAuth where the host supports it, and enable only the toolsets the agent needs. The README links a [policies and governance](https://github.com/github/github-mcp-server/blob/main/docs/policies-and-governance.md) document for organizations, and the dossier notes that admins control availability on GitHub Enterprise Cloud and Server.

The dossier does not list which tools write and which only read, or how insiders tools are versioned. Read the toolset reference before turning on write access, and keep insiders mode off in production agents unless someone tracks its changes.

### Editor's take

Any team already on GitHub that wants coding or ops agents to triage CI failures, draft pull requests, or summarize security alerts should start here before writing custom glue. Organizations that need tighter control over where the server runs can host the local build under ToolHive. The project has not connected an agent to this server; the take reflects the dossier and GitHub's README and governance doc.

</section>

## What it does

The GitHub MCP Server exposes **GitHub platform operations as MCP tools**: browsing and querying repositories, working with issues and pull requests, CI/CD and Actions intelligence, security/Dependabot context, and collaboration surfaces. It is explicitly aimed at **AI agents and assistants** automating multi-step development workflows through natural language-driven tool use in MCP hosts.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, http, API
- **MCP:** ✅ Remote HTTP MCP + local server options
- **Agent Skill:** ⚠️ Not yet published as a dedicated npx skills add … pack for the MCP server
- **Onboarding type:** `mcp`

## How agents onboard

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

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/github-mcp-server.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **Remote MCP** | `https://api.githubcopilot.com/mcp/` (insiders: `/mcp/insiders` or header per README) |
| **Local server** | Documented in repo for hosts without remote MCP |
| **Source** | Go — see https://github.com/github/github-mcp-server |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
