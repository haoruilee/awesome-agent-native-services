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
