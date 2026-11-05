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
