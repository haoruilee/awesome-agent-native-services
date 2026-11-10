---
title: "MCP Toolbox for Databases | Agent-Native Services"
service_name: "MCP Toolbox for Databases"
description: "MCP Toolbox for Databases is an open source Model Context Protocol (MCP) server that connects your AI agents, IDEs, and applications directly to your…"
permalink: /services/google-mcp-toolbox/
page_kind: service
service_slug: "google-mcp-toolbox"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/google-mcp-toolbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/google-mcp-toolbox.md"
tagline: "MCP Toolbox for Databases is an open source Model Context Protocol (MCP) server that connects your AI agents, IDEs, and applications directly to your enterprise databases"
website: "https://mcp-toolbox.dev/"
repository: "https://github.com/googleapis/mcp-toolbox"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · SDK · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://mcp-toolbox.dev/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://mcp-toolbox.dev/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/googleapis/mcp-toolbox" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/google-mcp-toolbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

[Apify MCP Server](/services/apify-mcp-server/) points an agent outward, at web data someone else hosts. MCP Toolbox for Databases points it inward, at the databases an organization already runs, and exposes their operations as MCP tools.

### Prebuilt packs and custom tools

The dossier describes two modes. Prebuilt generic tools, such as `list_tables` and `execute_sql`, give an IDE or coding agent fast schema discovery and query access; the exact set depends on the database pack. Packs listed in the README include AlloyDB, BigQuery, Cloud SQL for Postgres, MySQL, and SQL Server, Spanner, Firestore, and Knowledge Catalog, along with plain Postgres in the quick-start example.

The second mode is a custom tools framework aimed at production agents. Here the operator defines restricted, structured queries, semantic search, or NL2SQL-style tools with safety controls, and the server adds integrated auth including IAM, connection pooling, and OpenTelemetry metrics and tracing. The distinction matters. A prebuilt `execute_sql` hands the agent whatever the database credential allows. A custom tool hands it only the query shape the operator wrote.

### Starting the server

The documented MCP path is the `@toolbox-sdk/server` package run through `npx`, with a flag such as `--prebuilt=postgres` selecting the pack. Connection details come from environment variables described in the prebuilt configuration reference at [mcp-toolbox.dev](https://mcp-toolbox.dev/). Transport is typically stdio. The README names Gemini CLI, Google Antigravity, Claude Code, and Codex as clients.

For application code there are SDKs: Python as `toolbox-core`, JavaScript as `@toolbox-sdk/core`, plus Go and Java. No dedicated Agent Skill package is published; the dossier points to community search instead.

### Credentials and blast radius

Most neighbors in [Tool Access & Integration](/categories/tool-access-and-integration/) deal with SaaS APIs. [Nango](/services/nango/) and [Arcade](/services/arcade/) manage per-user OAuth to third-party services. Toolbox deals with database credentials supplied through environment variables or cloud IAM bindings, and the operator, not the end user, designs that access. The [MCP servers guide](/guides/getting-started-with-mcp-servers/) explains how a server like this gets registered in a client config.

Before relying on it, decide which mode you are in. A prebuilt pack on a laptop, pointed at a development database, is a different risk from the same pack pointed at production. Check which database role the server connects as, because that role is the real permission boundary for prebuilt tools. With stdio transport, the server process and its credentials sit on whatever host launches the agent. Confirm how IAM-based auth is configured for your database type, and where the OpenTelemetry output will land. The dossier mentions service or user delegation but does not explain how per-user delegation is set up.

### Editor's take

Toolbox makes sense for teams on Google Cloud data stores or Postgres who want coding agents to see live schema, and for production agents where an operator is willing to write narrow custom tools instead of exposing raw SQL. If the agent's real job is acting in Gmail, Slack, or a CRM on a user's behalf, Nango or Arcade is the better starting point. These conclusions come from reading the dossier, the README, and the project site; the server has not been connected to a database for this review.

</section>

## What it does

MCP Toolbox exposes **database operations as MCP tools** in two modes: **prebuilt generic tools** (schema discovery, SQL execution, etc.) for fast IDE/agent connectivity, and a **custom tools framework** for production agents with **auth (including IAM)**, **restricted access**, **structured queries**, **semantic search**, **connection pooling**, and **OpenTelemetry** observability.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, SDK, http
- **MCP:** ✅ MCP server (@toolbox-sdk/server) + prebuilt database packs
- **Agent Skill:** ⚠️ Not yet published as a dedicated npx skills add … pack
- **Onboarding type:** `mcp`

## How agents onboard

```json
{
  "mcpServers": {
    "toolbox-postgres": {
      "command": "npx",
      "args": ["-y", "@toolbox-sdk/server", "--prebuilt=postgres"]
    }
  }
}
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/google-mcp-toolbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **MCP** | `@toolbox-sdk/server` via npx |
| **SDKs** | Python, JS/TS, Go, Java |
| **Docs** | https://mcp-toolbox.dev/ |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
