---
title: "Hronaut | Agent-Native Services"
service_name: "Hronaut"
description: "A browser your AI agent can come back to"
permalink: /services/hronaut/
page_kind: service
service_slug: "hronaut"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/hronaut.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/hronaut.md"
tagline: "A browser your AI agent can come back to"
verified_at: "2026-09-30"
website: "https://hronaut.dev/"
repository: "https://github.com/hronaut/hronaut"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://hronaut.dev/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://hronaut.dev/setup" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/hronaut/hronaut" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/hronaut.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Hronaut is a visible desktop Chromium browser for coding agents. Named workspaces retain tabs, cookies and local storage across agent disconnects. The person can watch the browser, pause agent access and take over for manual steps.

It runs on Windows, macOS and Linux and automates pages inside Hronaut. It does not supply the coding agent or model, control native apps, or automatically attach an arbitrary existing Chrome profile. The public latest release observed September 30, 2026 was [v2.8.6](https://github.com/hronaut/hronaut/releases/tag/v2.8.6). Windows packages remain unsigned and macOS packages are not Apple-notarized; hashes and build attestations have a separate provenance scope.

The trial starts with the first agent tool call and lasts 10 consecutive days, with no card or automatic billing during trial. Ongoing use requires $4/month or $24/year per named user, up to three active devices. [Released terms](https://github.com/hronaut/hronaut/blob/v2.8.6/LICENSE).

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, http
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `mcp`

## Protocol surface

| Interface | Detail |
|---|---|
| Native MCP | Local Streamable HTTP browser navigation, observations, actions and diagnostics |
| Optional agent skill | Workflow instructions; separate from the runtime and connection |
| Optional MCPB adapter | Requires the separate running desktop application and reachable endpoint |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://github.com/hronaut/hronaut/releases/tag/v2.8.6
- https://hronaut.dev/
- https://hronaut.dev/setup
- https://hronaut.dev/client-topology

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
