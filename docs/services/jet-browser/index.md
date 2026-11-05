---
title: "Jet Browser | Agent-Native Services"
service_name: "Jet Browser"
description: "Jet Browser — the browser runtime agents can carry"
permalink: /services/jet-browser/
page_kind: service
service_slug: "jet-browser"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/jet-browser.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/jet-browser.md"
tagline: "Jet Browser — the browser runtime agents can carry"
verified_at: "2026-10-11"
website: "https://masaka-ai.vercel.app/jet-browser/"
repository: "https://github.com/masakaai/jet-browser"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · SDK · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-11</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://masaka-ai.vercel.app/jet-browser/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/masakaai/jet-browser#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/masakaai/jet-browser" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/jet-browser.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Jet Browser packages WPE WebKit, a headless Wayland compositor, and a Rust WebDriver bridge as a standalone runtime for agent systems. One container owns one browser session; a harness sends ordered JSONL commands and receives machine-readable results for navigation, native pointer/keyboard/touch input, tabs, JavaScript evaluation, semantic DOM capture, screenshots, downloads, state import/export, and close.

The runtime is intentionally smaller than a complete browser-agent framework. It includes no model, reasoning loop, account, database, proxy network, or hosted control plane. Native input, DOM state, and a fresh screenshot come from the same runtime, while versioned tool declarations let an embedding harness expose only the operations it chooses.

---

## Agent-facing interfaces

- **Interaction pattern:** self-hosted container runtime with an ordered JSONL stdio protocol. Docker and curl are enough for the bounded acceptance proof:
- **Catalog protocols:** Agent Skill, MCP, CLI, SDK, STDIO, http
- **MCP:** ✅ Available — a deliberately bounded runtime verifier, not a general browsing server.
- **Agent Skill:** ✅ Available — the repository publishes one Jet Browser skill through Codex and Claude Code plugin manifests, and keeps the same source at .agents/skills/jet-browser/SKILL.md.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** self-hosted container runtime with an ordered JSONL stdio protocol. Docker and curl are enough for the bounded acceptance proof:

```bash
curl -fsSL https://raw.githubusercontent.com/masakaai/jet-browser/main/scripts/try-jet.sh | sh
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/jet-browser.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **JSONL stdio** | Core create → navigate → native input → inspect → screenshot → close protocol, usable from any subprocess supervisor |
| **Agent tool schemas** | Versioned JSON Schema declarations in [`sdk/tools.mjs`](https://github.com/masakaai/jet-browser/blob/v0.8.0/sdk/tools.mjs) |
| **MCP stdio verifier** | Two bounded tools for capability discovery and immutable network-disabled runtime acceptance |
| **OCI image** | Public `linux/amd64` runtime at `ghcr.io/masakaai/jet-browser:0.8.0`; pin its digest in production |
| **GitHub Action** | [`masakaai/jet-browser@v0.8.0`](https://github.com/marketplace/actions/jet-browser-runtime-smoke-test) runs the acceptance proof in CI |
| **Agent plugins** | Codex, Claude Code, and Hermes integration metadata around the same runtime boundary |

---

## Verification

Last verified **2026-10-11**.

Sources:
- https://github.com/masakaai/jet-browser

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
