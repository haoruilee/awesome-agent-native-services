---
title: "Obot | Agent-Native Services"
service_name: "Obot"
description: "Complete MCP Platform — Hosting, Registry, Gateway, and Chat Client"
permalink: /services/obot/
page_kind: service
service_slug: "obot"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/obot.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/obot.md"
tagline: "Complete MCP Platform — Hosting, Registry, Gateway, and Chat Client"
website: "https://obot.ai"
repository: "https://github.com/obot-platform/obot"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://obot.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.obot.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/obot-platform/obot" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/obot.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Obot is a single deployable that bundles four MCP-related concerns into one stack: **hosting** (run MCP servers in a managed sandbox — Node.js, Python, or container-based), **registry** (catalog and discover MCP servers and their tools), **gateway** (front everything with a unified URL with OAuth, RBAC, and usage policies), and an optional **chat client** (a generic agent UI that consumes the gateway).

For teams that want a private, in-cluster MCP plane — instead of stitching together Smithery for the registry, ToolHive for the runtime, and a hand-rolled gateway — Obot gives them all four in one repo with Kubernetes-ready Helm charts and OAuth 2.1 baked in.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, http, API
- **MCP:** ✅ Available — Obot is an MCP platform; everything it does is exposed over MCP.
- **Agent Skill:** ⚠️ Not yet published.
- **Onboarding type:** `mcp`

## How agents onboard

```
# Self-hosted (Kubernetes / Docker):
helm install obot obot/obot
# or:
docker run -p 8080:8080 ghcr.io/obot-platform/obot:latest

# Then point any MCP-compatible agent at the gateway URL:
https://<obot-host>/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/obot.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP (Streamable HTTP) | Unified gateway URL for tool discovery + invocation |
| REST admin API | Server registration, token issuance, policy management |
| OAuth 2.1 | Auth code + client credentials flows |
| Helm chart / Docker image | Kubernetes-native deploy |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
