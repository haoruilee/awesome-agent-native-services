---
title: "Sallyport | Agent-Native Services"
service_name: "Sallyport"
description: "Let your agent touch prod. Keep the keys"
permalink: /services/sallyport/
page_kind: service
service_slug: "sallyport"
category_slug: "oversight-and-approval"
category_label: "Oversight & Approval"
hero_image: "/assets/images/editorial-oversight.webp"
image: "/assets/images/editorial-oversight.webp"
classification: "agent-native"
dossier_path: "services/oversight-and-approval/sallyport.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/sallyport.md"
tagline: "Let your agent touch prod. Keep the keys"
verified_at: "2026-09-26"
website: "https://sallyport.dev"
repository: "https://github.com/OlegSotnikov/sallyport"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Oversight &amp; Approval</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Free Apache-2.0 Mac app; Apple Silicon and macOS 14+ only</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://sallyport.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/OlegSotnikov/sallyport/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/OlegSotnikov/sallyport" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/sallyport.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Sallyport is a local Mac credential vault and execution gate for AI agents. An agent asks for a structured HTTP request, SSH command, credential-provisioning request, or upstream MCP tool call; Sallyport resolves the bound credential, applies its fixed authorization ladder, writes a durable audit intent, executes the operation, and returns a bounded result without providing a credential-reveal command.

The boundary is intentionally precise. Stored keys remain in the app for HTTP and SSH operations, but configured local stdio MCP servers necessarily receive credentials in their child environments. Target/upstream responses are returned without content inspection and may echo sensitive values. Sallyport protects its own execution path; it cannot govern traffic the agent sends elsewhere.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, STDIO, http, API
- **MCP:** ✅ Available — MCP is the primary agent-facing gate.
- **Agent Skill:** ⚠️ Not yet published by the project.
- **Onboarding type:** `cli`

## How agents onboard

```bash
brew install --cask olegsotnikov/tap/sallyport
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/sallyport.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **MCP stdio** | `sp mcp` exposes Sallyport tools to a local MCP client |
| **Private Unix socket** | Connects the minimal shim to `Sallyport.app` with kernel peer identity |
| **HTTP executor** | Structured GET/POST/PUT/PATCH/DELETE/HEAD with bearer, basic, custom-header, AWS SigV4, or OAuth2 client-credentials adapters |
| **SSH executor** | Configured-host command execution with challenge signing and encrypted asciicast recording |
| **Upstream MCP** | Local stdio or remote Streamable HTTP with API key or OAuth 2.1 support |
| **Audit JSONL** | ECIES-sealed rows, hash chain, ECDSA signatures, and an integrity anchor under `~/.sallyport/audit` |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/OlegSotnikov/sallyport/releases/tag/v0.8.16
- https://sallyport.dev
- https://api.github.com/repos/OlegSotnikov/sallyport

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/oversight-and-approval/' | relative_url }}"><small>Collection</small><strong>← Oversight &amp; Approval</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
