---
title: "Smithery | Agent-Native Services"
service_name: "Smithery"
description: "Connect your agent to thousands of MCP tools and Agent Skills"
permalink: /services/smithery/
page_kind: service
service_slug: "smithery"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/smithery.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/smithery.md"
tagline: "Connect your agent to thousands of MCP tools and Agent Skills"
website: "https://smithery.ai"
repository: "https://github.com/arcadeai-labs/smithery-cli"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://smithery.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://smithery.ai/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/arcadeai-labs/smithery-cli" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/smithery.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

Most tools an agent reaches through this registry have two operators. The MCP server belongs to whoever published it. The connection, the OAuth grant, and the session are held by Smithery. The agent's own machine runs only the CLI and the host configuration it writes. The dossier also records that Arcade.dev has acquired Smithery ([announcement](https://arcade.dev/blog/smithery-joins-arcade)), so the broker in the middle now sits inside a larger company, and that is worth weighing before you route credentials through it.

### Registry, gateway, and CLI

The dossier calls Smithery a registry and gateway for Model Context Protocol servers and Agent Skills. An operator, or an agent with shell access, searches the catalog, adds a server to a host, and calls its tools. The command sequence it prints is `npx @smithery/cli@latest setup` or a global install, then `smithery auth login`, `smithery mcp add <server>`, `smithery tool list`, and `smithery tool call <server> <tool> '<json-args>'`. The same CLI configures hosts such as Cursor, Claude Desktop, VS Code, and ChatGPT Apps, bridging remote servers to local stdio clients where needed.

The managed OAuth is the part that changes an agent's day. Hosted servers use Smithery-run auth URLs and sessions, so the agent does not hold a long-lived secret for each third-party API. A skills registry sits alongside the server catalog, browsable on the site and installed through the same CLI. Publishers get usage observability. The dossier notes that the former TypeScript SDK repository no longer resolves, and points to the [Smithery docs](https://smithery.ai/docs) for programmatic access instead.

### One broker versus single-purpose servers

Most of [Tool Access & Integration](/categories/tool-access-and-integration/) is individual servers. [Apify MCP Server](/services/apify-mcp-server/) and [MCP Toolbox for Databases](/services/google-mcp-toolbox/) each expose one product's tools; Smithery is a directory and router across many of them. [ToolHive](/services/toolhive/) answers a nearby question differently: it helps you run MCP servers yourself, wherever you choose, rather than reaching servers someone else hosts. [Nango](/services/nango/) overlaps on credentials, as an OAuth and API credential layer without the public server catalog. The [MCP getting-started guide](/guides/getting-started-with-mcp-servers/) explains how a host connects to any of these.

### Due diligence on a broker

Start with consent. The first OAuth grant for each tool may need a human in a browser; after that, calls run under the stored grant. Ask how grants are scoped, where they are stored, and how a user revokes one without breaking the rest.

Then look at what the dossier leaves out. It does not say how servers are vetted before listing, what Smithery logs when a call passes through, or how the acquisition changes terms, hosting, or support. A registry makes it easy to add a server nobody on the team has read, so pair it with a review step; [Snyk Agent Scan](/services/snyk-agent-scan/) is one listing built for scanning MCP servers and skills.

### Editor's take

Smithery makes most sense during exploration, when an agent or a pilot team needs to try many tools quickly without wiring OAuth for each one. Once a short list is settled, running those servers directly, or under ToolHive, removes a party from the credential path. This assessment is assembled from the dossier and Smithery's public docs; the project has not brokered a tool call through it.

</section>

## What it does

Smithery is a **registry and gateway** for **Model Context Protocol** servers and **Agent Skills**. An agent (or its human operator once) uses the CLI to **search**, **install**, and **invoke** tools across thousands of published MCP servers — with **managed authentication** and **usage observability** for publishers. It solves the integration explosion problem for tool-using agents: one discovery and OAuth flow instead of bespoke config per SaaS.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, CLI, SDK, http, API
- **MCP:** ✅ Smithery is an MCP-native distribution layer: the registry exposes remote MCP servers; the CLI configures clients (Cursor, Claude Desktop, VS Code, ChatGPT Apps, etc.). Hosted servers use Smithery-managed OAuth and sessions so agents do not embed long-lived third-party secrets for every integration.
- **Agent Skill:** ✅ Smithery hosts a large Skills registry (machine-readable workflows) browsable at https://smithery.ai/skills — install flows use the Smithery CLI; see docs for publishing and discovery.
- **Onboarding type:** `mcp`

## How agents onboard

```bash
npx @smithery/cli@latest setup
# or
npm install -g @smithery/cli
smithery auth login
smithery mcp add <server>
smithery tool list
smithery tool call <server> <tool> '<json-args>'
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/smithery.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Smithery CLI | `npx @smithery/cli@latest`, global `smithery` |
| TypeScript SDK | Former `smithery-ai/sdk` repo is 404; use current [Smithery docs](https://smithery.ai/docs) for programmatic access |
| MCP | Remote servers in the registry; CLI configures host clients |
| Docs API | https://smithery.ai/docs |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
