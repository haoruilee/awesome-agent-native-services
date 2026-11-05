---
title: "SandBase Harness | Agent-Native Services"
service_name: "SandBase Harness"
description: "A local-first runtime for AI agents"
permalink: /services/sandbase-harness/
page_kind: service
service_slug: "sandbase-harness"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/sandbase-harness.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/sandbase-harness.md"
tagline: "A local-first runtime for AI agents"
website: "https://github.com/sandbaseai/sandbase-harness"
repository: "https://github.com/sandbaseai/sandbase-harness"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Open source · Apache-2.0 · self-hosted/local-first</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/sandbaseai/sandbase-harness" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/sandbaseai/sandbase-harness/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/sandbaseai/sandbase-harness" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/sandbase-harness.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Official README: **"A local-first runtime for AI agents. Sessions, sandboxed tools, memory, credentials, audit trails, and a built-in Console — all running on your machine or in your own infrastructure."** — [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness)

SandBase Harness is a local-first runtime for operating multi-step AI-agent sessions. It combines persistent sessions and resumable event streams with sandboxed turns, MCP toolsets, credential scopes, permission policies, approvals, artifacts, memory, audit records, and replay. It can run on an operator's machine or in self-hosted infrastructure; the exact isolation boundary depends on the selected and configured execution backend.

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, STDIO, http, API
- **MCP:** ✅ A native stdio MCP bridge is published.
- **Agent Skill:** ⚠️ No first-party Agent Skill package is published.
- **Onboarding type:** `mcp`

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP/API | Local runtime and Console surface |
| MCP | Native stdio bridge; metadata in `server.json` |
| TypeScript | Runtime and CLI packages |
| Deployment | Local process, Docker, Kubernetes, and self-hosted worker paths |

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
