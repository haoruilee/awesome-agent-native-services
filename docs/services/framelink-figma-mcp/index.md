---
title: "Framelink MCP for Figma | Agent-Native Services"
service_name: "Framelink MCP for Figma"
description: "Give your coding agent access to your Figma data. Implement designs in any framework in one-shot"
permalink: /services/framelink-figma-mcp/
page_kind: service
service_slug: "framelink-figma-mcp"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/framelink-figma-mcp.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/framelink-figma-mcp.md"
tagline: "Give your coding agent access to your Figma data. Implement designs in any framework in one-shot"
website: "https://www.framelink.ai/"
repository: "https://github.com/GLips/Figma-Context-MCP"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.framelink.ai/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.framelink.ai/docs/quickstart" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/GLips/Figma-Context-MCP" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/framelink-figma-mcp.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

Turning a design into working UI code is a job coding agents are often handed with a screenshot and a hope. The screenshot loses spacing values, component structure, and type styles, so the agent guesses. The raw Figma file has all of that and far too much else. Framelink sits between the two. Its tagline is "Give your coding agent access to your Figma data. Implement designs in any framework in one-shot."

### From a pasted link to layout context

The dossier describes the workflow plainly. A developer adds the server to an MCP client. In agent chat, someone pastes a link to a Figma file, frame, or group. The agent calls the server's MCP tools, and the server fetches metadata through the Figma API, strips it down to layout and styling information, and returns that to the model. The dossier's word for the second step is pruning. The point is to send the agent design structure without the noise of the full JSON payload.

Setup is an `npx` entry in the client's MCP configuration that runs `figma-developer-mcp` with a Figma API key and the `--stdio` flag. Transport is stdio. Cursor is named as the primary client, with other MCP-enabled coding tools also listed. Windows needs a `cmd` wrapper, per the README. The [quickstart](https://www.framelink.ai/docs/quickstart) has the current configuration. No dedicated Agent Skill is published; the dossier points to community search instead.

### Token scope is the permission model

Access is a Figma personal access token. Whatever files the token's owner can read, the agent can read, and nothing more. The dossier notes there is no write path to Figma by default. The agent consumes design data, and code changes go into the repository under normal git permissions. Designers keep control through Figma sharing and through who issues tokens.

That is simple and also coarse. A personal token is tied to one person, so check in Figma's own docs how tokens are scoped and revoked, and decide whose account an agent on a shared machine should use. The dossier also cites a lower hallucination rate than screenshots as a project claim. Treat it as the vendor's claim.

### Editor's take

Among the [tool access and integration services](/categories/tool-access-and-integration/), Framelink is a single-purpose MCP server, closer in kind to [MCP Toolbox for Databases](/services/google-mcp-toolbox/), which connects agents to one class of system, than to [Arcade](/services/arcade/) or [Nango](/services/nango/), which manage OAuth and credentials across many tools. [ToolHive](/services/toolhive/) is a way to run servers like this one in a contained environment, and pairs with it rather than replacing it. The [getting started with MCP servers guide](/guides/getting-started-with-mcp-servers/) covers the client configuration pattern Framelink uses.

Front-end developers who work from Figma and use an MCP-capable editor are the natural audience. Teams that need per-user OAuth instead of a pasted personal token should look at how Arcade or Nango handle credentials and whether they fit around it. This page is an editorial reading of the dossier, the README, and the quickstart. The server has not been configured against a Figma file by anyone here.

</section>

## What it does

Framelink MCP fetches **Figma file metadata via the Figma API** and **simplifies/translates** the payload so coding agents receive **layout- and styling-focused context** instead of noisy raw JSON. README positions it for **one-shot UI implementation** in agent mode when the user pastes a Figma link.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, STDIO, http, API
- **MCP:** ✅ MCP server (figma-developer-mcp)
- **Agent Skill:** ⚠️ Not yet published as a dedicated npx skills add … pack
- **Onboarding type:** `mcp`

## How agents onboard

```json
{
  "mcpServers": {
    "Framelink MCP for Figma": {
      "command": "npx",
      "args": ["-y", "figma-developer-mcp", "--figma-api-key=YOUR-KEY", "--stdio"]
    }
  }
}
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/framelink-figma-mcp.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **MCP** | stdio via `npx -y figma-developer-mcp …` |
| **Figma API** | https://www.figma.com/developers/api |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
