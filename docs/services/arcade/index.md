---
title: "Arcade | Agent-Native Services"
service_name: "Arcade"
description: "MCP tools with managed OAuth — credentials stay out of the LLM"
permalink: /services/arcade/
page_kind: service
service_slug: "arcade"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/arcade.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/arcade.md"
tagline: "MCP tools with managed OAuth — credentials stay out of the LLM"
website: "https://www.arcade.dev"
repository: "https://github.com/ArcadeAI/arcade-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.arcade.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.arcade.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/ArcadeAI/arcade-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/arcade.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

[Nango](/services/nango/) hands your code a fresh access token and leaves the API call to you. Arcade takes the call itself. Its tools run with credentials injected on the server side, so the model and the client see the result of a Gmail or Slack action without ever seeing the token that authorized it.

### Authorized tool calls

The dossier describes Arcade as a way to ship production MCP servers whose tools call third-party APIs with OAuth on behalf of end users. Its central idea is authorized tool calling: before a tool executes, Arcade checks the intersection of what the agent is allowed to do and what the user has delegated. If both permit it, Arcade injects the credential and runs the tool; results go back to the agent with secrets stripped out.

That framing is in the tagline, "MCP tools with managed OAuth — credentials stay out of the LLM." The docs also discuss SSO for agents, where enterprise identity providers supply the user side of the delegation. Pre-built integrations, including GitHub, Slack, Google, Gmail, and Salesforce, ship with managed OAuth, and Arcade stores refresh tokens and refreshes them without model visibility.

### Building with the CLI

The documented starting point is the Arcade CLI. The dossier prints `uv tool install arcade-mcp` followed by `arcade new my_server` to scaffold a server, and the CLI also handles local development and deploy. Hosted servers run on Arcade Cloud, reachable through HTTP APIs; transport is stdio or hosted MCP depending on the deployment. Per Arcade's docs, clients include Claude Desktop, Cursor, OpenAI Agents, Google ADK, Vercel AI, Mastra, and CrewAI. The [Arcade docs](https://docs.arcade.dev) have separate guides for building a server and for authorized tool calling.

No official Agent Skill bundle was located. The dossier points to community search.

### Questions for the docs

Within [Tool Access & Integration](/categories/tool-access-and-integration/), Arcade and Nango answer the same question from different heights. [ToolHive](/services/toolhive/) is about running any MCP server securely, which concerns the process more than the credential. [MCP Toolbox for Databases](/services/google-mcp-toolbox/) covers database access configured by an operator rather than OAuth granted by each user. The [MCP servers guide](/guides/getting-started-with-mcp-servers/) explains where an authoring platform like this sits.

A careful adopter should confirm where custom tools execute, on Arcade Cloud or on infrastructure you run, because that decides who holds stored refresh tokens. Find out how authorization policy is expressed and where audit logs can be read. The dossier notes that high-risk actions can still be gated by application policy outside Arcade, which means approval steps are your responsibility, not a built-in feature.

### Editor's take

Arcade is aimed at teams building user-facing copilots that act in mail, calendars, chat, or a CRM, where keeping tokens out of the model is a hard requirement and Python tool code is acceptable. Teams that only want a token store and prefer writing their own HTTP calls should compare Nango. If the main worry is whether a third-party server is safe to install, [Snyk Agent Scan](/services/snyk-agent-scan/) addresses that separate question. This judgement draws on the dossier and Arcade's documentation alone; the project has not deployed an Arcade server.

</section>

## What it does

Arcade helps teams ship **production MCP servers** where tools call third-party APIs with **OAuth on behalf of end users**, while **secrets and tokens never enter the LLM context**. Docs emphasize **user-facing agents**, **authorized tool calling**, and **SSO for AI agents** — bridging agent intent, user consent, and least-privilege API access.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, http
- **MCP:** ✅ Arcade *is* an MCP authoring and hosting platform
- **Agent Skill:** ⚠️ No official npx skills add ArcadeAI/... bundle located.
- **Onboarding type:** `mcp`

## How agents onboard

```bash
uv tool install arcade-mcp
arcade new my_server
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/arcade.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | Primary agent integration |
| Arcade CLI | `arcade new`, deploy, local dev |
| HTTP APIs | Arcade Cloud for hosted servers |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
