---
title: "Composio | Agent-Native Services"
service_name: "Composio"
description: "The tool platform built for agents"
permalink: /services/composio/
page_kind: service
service_slug: "composio"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/composio.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/composio.md"
tagline: "The tool platform built for agents"
website: "https://composio.dev"
repository: "https://github.com/ComposioHQ/composio"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · SDK</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://composio.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.composio.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/ComposioHQ/composio" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/composio.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

### Whose tokens, held where

Holding other people's OAuth tokens is the whole arrangement here. The dossier says so directly: the platform creates, stores, refreshes, and revokes tokens, and agent code never sees them. What it does not say is where that storage lives, whether an operator can run it inside their own network, or how a user disconnects an app without going through the agent. For anything that touches a customer's email or CRM, those answers belong in the review before the first Connect Link goes out, and the place to find them is the [Composio docs](https://docs.composio.dev).

The MCP record is thin in a similar way. It lists stdio and SSE transports and links an authentication concepts page rather than an MCP setup page, so whether you run a local server or connect to a hosted one is left to the docs.

### Discovery inside the loop

The documented model is runtime tool selection. Instead of a developer wiring a fixed list of integrations at build time, the agent gets meta-tools: one to search for a tool that fits the task, one to authenticate an app for a given `user_id`, and one to execute. If the user has not connected that app yet, the agent shows a Connect Link in the conversation, the user clicks once, and later calls go through without asking again. Every call is scoped to a `user_id`, which is how one agent serves many users without their credentials crossing.

Integration paths are broad. The quickest is `npx skills add composiohq/skills`, which installs official skills including `composio-tool-router` for isolated per-user tool sessions. Python packages such as `composio_openai` and `composio_anthropic`, the TypeScript `@composio/core`, and adapters for LangChain, CrewAI, LlamaIndex, and the Vercel AI SDK are also listed. Custom OAuth configs allow white-labeled consent screens and custom scopes.

### Neighbors in tool access

In [Tool Access & Integration](/categories/tool-access-and-integration/), the closest comparison is [Nango](/services/nango/), which calls itself the OAuth and API credential layer for agents. Both hold credentials; Composio also ships the tool catalog and the execution layer, so more of the stack is theirs. [ToolHive](/services/toolhive/) is about running any MCP server securely rather than brokering SaaS logins. [Snyk Agent Scan](/services/snyk-agent-scan/) scans agents, MCP servers, and skills, which pairs sensibly with any tool platform. Composio's tagline is "The tool platform built for agents." The MCP side of all this is covered in [Getting started with MCP servers](/guides/getting-started-with-mcp-servers/).

### Editor's take

Multi-user agents that need to act in many SaaS accounts, with consent collected mid-conversation, are the case Composio was shaped for. If you would rather keep tokens in a system you operate and write your own tool definitions, Nango is the smaller dependency. Our view is assembled from the dossier and the vendor's published material, and no connection was authorized through Composio while writing it.

</section>

## What it does

Composio gives AI agents the ability to **discover, authenticate, and call external tools at runtime**. Rather than a developer pre-configuring a fixed set of integrations at build time, agents receive meta-tools at runtime that let them find the right integration, authenticate on behalf of the user, and execute the call — all within the agent loop, without any human clicking an OAuth button.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, SDK
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skills published at composiohq/skills
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `composio_openai`, `composio_anthropic`, `composio_langchain`, etc. |
| TypeScript SDK | `@composio/core`, framework-specific packages |
| MCP Compatible | Works with Claude Desktop, Cursor, OpenAI Agents without framework packages |
| Framework Integrations | LangChain, CrewAI, LangGraph, LlamaIndex, Vercel AI SDK, AutoGen, and more |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
