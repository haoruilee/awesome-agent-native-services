---
title: "Scalekit | Agent-Native Services"
service_name: "Scalekit"
description: "Connect your agents to any tool. Authenticated, scoped, and logged"
permalink: /services/scalekit/
page_kind: service
service_slug: "scalekit"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/scalekit.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/scalekit.md"
tagline: "Connect your agents to any tool. Authenticated, scoped, and logged"
website: "https://www.scalekit.com"
repository: "https://github.com/scalekit-inc/scalekit-sdk-python"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · webhook · SDK · openapi · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.scalekit.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.scalekit.com/agentkit/overview/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/scalekit-inc/scalekit-sdk-python" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/scalekit.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AgentKit, Scalekit's agent integration product, lets an AI agent act in third-party apps on behalf of each user. A user connects Gmail, Slack, Salesforce, GitHub or any of 500+ connectors once through an authorization link; Scalekit stores and refreshes their tokens (OAuth 2.0, API keys, RSA key pairs, Basic and bearer credentials) in an encrypted, per-tenant token vault that can use the customer's own KMS key, and the agent calls 20,000+ prebuilt tools as that user through the SDKs, the REST API, or a Virtual MCP server. Admins decide which tools each agent role sees, and every tool call is logged for audit and can be streamed to a SIEM.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, webhook, SDK, openapi, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official AgentKit skills published at scalekit-inc/authstack
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `scalekit-sdk-python` — tools, connected accounts, authorization links, MCP session tokens; LangChain and Google ADK adapters |
| Node.js SDK | `@scalekit-sdk/node` |
| REST API | OAuth 2.0 client credentials; [OpenAPI spec](https://docs.scalekit.com/api/agentkit.scalar.json) |
| MCP | Virtual MCP servers and per-connection MCP servers over Streamable HTTP |
| Webhooks | Connected-account events; triggers (beta) |
| Agent Skills | `npx skills add scalekit-inc/authstack --skill setup-agentkit integrate-agentkit discover-connectors expose-agentkit-mcp integrate-agentkit-host check-agentkit-prod` |
| Framework guides | LangChain, LangGraph, Google ADK, OpenAI Agents SDK, Anthropic, Vercel AI SDK, Mastra, CrewAI |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
