---
title: "MCP-Cloud (mcp-agent) | Agent-Native Services"
service_name: "MCP-Cloud (mcp-agent)"
description: "Deploy and host your mcp-agents and apps on the cloud"
permalink: /services/mcp-cloud-mcp-agent/
page_kind: service
service_slug: "mcp-cloud-mcp-agent"
category_slug: "durable-execution-and-scheduling"
category_label: "Durable Execution & Scheduling"
hero_image: "/assets/images/editorial-durable.webp"
image: "/assets/images/editorial-durable.webp"
classification: "agent-native"
dossier_path: "services/durable-execution-and-scheduling/mcp-cloud-mcp-agent.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/mcp-cloud-mcp-agent.md"
tagline: "Deploy and host your mcp-agents and apps on the cloud"
website: "https://docs.mcp-agent.com"
repository: "https://github.com/lastmile-ai/mcp-agent"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Durable Execution &amp; Scheduling</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://docs.mcp-agent.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.mcp-agent.com/get-started/cloud" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/lastmile-ai/mcp-agent" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/mcp-cloud-mcp-agent.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

**MCP-Cloud (mcp-c)** is a managed platform for **hosting mcp-agent applications, FastMCP servers, and ChatGPT App backends** as **remote MCP servers**. Long-running tools and workflows run on **Temporal** with **retries**, **pause/resume**, and **human input** support; **secrets** are managed for developers and end users; **observability** includes logs, traces, and workflow history — see [MCP-Cloud overview](https://docs.mcp-agent.com/cloud/mcp-agent-cloud/overview).

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, http
- **MCP:** ✅ Deployed workloads expose a remote MCP server over HTTP/SSE.
- **Agent Skill:** ⚠️ Framework-focused; use repo examples and mcp_agent.config.yaml patterns.
- **Onboarding type:** `mcp`

## How agents onboard

```bash
uvx mcp-agent login
uvx mcp-agent deploy my-agent
# Endpoint: https://<unique_id>.deployments.mcp-agent.com
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/mcp-cloud-mcp-agent.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `uvx mcp-agent` — login, deploy, install, cloud logger |
| MCP over HTTPS | Standard MCP client config with `Authorization: Bearer` |
| Python | `mcp_agent` package patterns in docs |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/durable-execution-and-scheduling/' | relative_url }}"><small>Collection</small><strong>← Durable Execution &amp; Scheduling</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
