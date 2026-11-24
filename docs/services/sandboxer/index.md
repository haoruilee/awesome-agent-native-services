---
title: "Sandboxer | Agent-Native Services"
service_name: "Sandboxer"
description: "The agent swarm platform"
permalink: /services/sandboxer/
page_kind: service
service_slug: "sandboxer"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/sandboxer.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/sandboxer.md"
tagline: "The agent swarm platform"
website: "https://sandboxer.com"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · MCP · REST · CLI · SDK · openapi · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://sandboxer.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://sandboxer.com/docs/mcp" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/sandboxer.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Sandboxer runs cloud sandboxes for AI agents. Each sandbox is a persistent Ubuntu 24.04 virtual machine (a Cloud Hypervisor microVM with its own kernel), not a container: root, systemd, Docker, nested KVM, SSH and an HTTPS URL for any port. An agent creates sandboxes, runs commands, reads and writes files, publishes ports, saves named snapshots and forks sandboxes through the REST API, the `sbx` CLI, the TypeScript and Python SDKs or the MCP server.

Coding agents are installed in every sandbox: Claude Code, Codex, OpenCode, Pi, Kimi Code and Mistral Vibe. A caller prompts them over the API (`POST /api/v1/sandboxes/{id}/prompt`), streams their work as structured events, keeps several conversations running side by side, and steers or interrupts a running turn. The provider keys are the account's own.

Stopping a sandbox saves its memory as well as its disk, so processes are still running after resume, and a stopped sandbox bills no running time. An idle sandbox pauses itself and wakes on the next API call or request to its URL. Forks are copy-on-write copies of a sandbox's disk, and named snapshots act as templates, so many agents can start from one prepared state. Billing is per second while a sandbox runs; there are no GPUs.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⚠️ — partial.
- **Catalog protocols:** URL onboarding, MCP, REST, CLI, SDK, openapi, STDIO, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⚠️ — partial.

```
Read https://sandboxer.com/docs/mcp.md and follow the "If you are an agent setting this up" steps to connect the Sandboxer MCP server.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/sandboxer.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | `https://sandboxer.com/api/v1`, OpenAPI at https://sandboxer.com/openapi.yaml |
| MCP | `https://sandboxer.com/mcp`, Streamable HTTP, OAuth 2.1 or API key; registry name `com.sandboxer/mcp` |
| MCP stdio adapter | `npx -y sandboxer-mcp` or `sbx mcp` |
| CLI | `sbx` for macOS, Linux and Windows (`curl -fsSL https://sandboxer.com/install \| sh`) |
| TypeScript SDK | `sandboxer-sdk` on npm |
| Python SDK | `sandboxer-sdk` on PyPI, imported as `sandboxer` |
| Events | Integrated-agent events by polling or server-sent events (`/sandboxes/{id}/events`) |
| Docs for agents | https://sandboxer.com/llms.txt, https://sandboxer.com/docs/mcp.md |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
