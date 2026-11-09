---
title: "briq | Agent-Native Services"
service_name: "briq"
description: "Cloud sandboxes for your agents"
permalink: /services/briq/
page_kind: service
service_slug: "briq"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/briq.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/briq.md"
tagline: "Cloud sandboxes for your agents"
website: "https://briq.cloud"
repository: "https://github.com/briq-cloud/briq-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · CLI · SDK · openapi · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://briq.cloud" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://briq.cloud/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/briq-cloud/briq-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/briq.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

briq gives an agent a machine of its own, and the services that machine needs next to it. `briq_run({ recipe: "sandbox" })` starts a Linux microVM with Python, Node, git and a shell. The agent writes files, runs commands (long ones asynchronously, with a result to poll), reads the output and destroys the machine when it is done. Nothing runs on the person's computer.

The same call starts a service: Postgres, MySQL, Redis, MongoDB, Qdrant, a headless Chrome, an app from a GitHub repository or any OCI image. Services in one stack reach each other by name, and each returns connection strings. A briq goes to sleep after a window without use (default one hour), keeps its disk while it sleeps, is not billed for compute, and wakes on the next call or visit. `briq_fork` copies a briq, for example a database before a risky migration.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, CLI, SDK, openapi, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

```
# MCP (Streamable HTTP, OAuth sign-in in the browser):
claude mcp add --transport http briq https://api.briq.cloud/mcp

# Agent instructions:
Read https://briq.cloud/llms.txt and follow the instructions.

# CLI:
npm install -g @briq-cloud/cli  # then: briq login, briq run sandbox

# SDK / REST (API key):
npm install @briq-cloud/sdk  # or: pip install briq-cloud
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/briq.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | `https://api.briq.cloud/mcp`, Streamable HTTP, OAuth or API key |
| REST API | `https://api.briq.cloud/v1`, OpenAPI 3.1 at `/v1/openapi.json` |
| SDK | `@briq-cloud/sdk` (TypeScript), `briq-cloud` (Python) |
| CLI | `@briq-cloud/cli` |
| Agent instructions | https://briq.cloud/llms.txt, https://briq.cloud/.well-known/skills/briq/SKILL.md, a Markdown copy of every docs page |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
