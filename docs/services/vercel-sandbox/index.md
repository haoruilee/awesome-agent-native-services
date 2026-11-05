---
title: "Vercel Sandbox | Agent-Native Services"
service_name: "Vercel Sandbox"
description: "Secure, isolated microVMs for AI-generated code"
permalink: /services/vercel-sandbox/
page_kind: service
service_slug: "vercel-sandbox"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/vercel-sandbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/vercel-sandbox.md"
tagline: "Secure, isolated microVMs for AI-generated code"
website: "https://vercel.com/docs/sandbox"
repository: "https://github.com/vercel/sandbox"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · CLI · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://vercel.com/docs/sandbox" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://vercel.com/docs/sandbox" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/vercel/sandbox" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/vercel-sandbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Vercel Sandbox provides **Firecracker microVMs** with fast cold start, full **Node.js and Python** runtimes, optional **snapshots** for save/resume, and **persistent sandboxes** (beta). Documentation positions it for **AI agents**, **AI-generated code**, and **untrusted code** execution at scale.

---

## Agent-facing interfaces

- **Catalog protocols:** REST, CLI, SDK, http, API
- **MCP:** ⚠️ Not yet published as a dedicated first-party MCP server
- **Agent Skill:** ⚠️ No official npx skills add vercel/... bundle located.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
npm install @vercel/sandbox
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/vercel-sandbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| TypeScript | `@vercel/sandbox` — [SDK reference](https://vercel.com/docs/sandbox/sdk-reference) |
| REST API | [Sandboxes REST](https://vercel.com/docs/rest-api/sandboxes/create-a-sandbox) |
| CLI | `sandbox` CLI for manual and agentic debugging workflows |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
