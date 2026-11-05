---
title: "Cloudflare Computer | Agent-Native Services"
service_name: "Cloudflare Computer"
description: "Give your agent a computer 👾"
permalink: /services/cloudflare-computer/
page_kind: service
service_slug: "cloudflare-computer"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/cloudflare-computer.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cloudflare-computer.md"
tagline: "Give your agent a computer 👾"
verified_at: "2026-09-30"
website: "https://github.com/cloudflare/computer"
repository: "https://github.com/cloudflare/computer"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/cloudflare/computer" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/cloudflare/computer/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/cloudflare/computer" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cloudflare-computer.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Cloudflare Computer is a Durable Object virtual filesystem (SQLite-backed) with one execution entry point, `workspace.runtime.exec`. Backends today are a full Linux container (FUSE + `computerd`), an isolate shell ([just-bash](https://github.com/vercel-labs/just-bash)), and isolate JavaScript. Agents get a small durable working directory plus optional AI SDK tools (`read`, `ls`, `grep`, `write`, `edit`, `exec`).

---

## Agent-facing interfaces

- **Interaction pattern:** SDK (Durable Object workspace)
- **Catalog protocols:** SDK, API
- **MCP:** ⚠️ Example only
- **Agent Skill:** ⚠️ Not published for product consumers
- **Onboarding type:** `sdk`

## How agents onboard

**Interaction pattern:** SDK (Durable Object workspace)

```bash
npm install @cloudflare/computer
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cloudflare-computer.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| npm | `@cloudflare/computer` |
| FS / runtime API | `workspace.fs`, `workspace.runtime.exec` |
| RPC | capnweb between DO and `computerd` |
| Examples | container, worker-shell, worker-javascript, egress, mcp, think |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://github.com/cloudflare/computer/tree/main/examples/mcp

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
