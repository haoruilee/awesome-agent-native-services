---
title: "Kernel | Agent-Native Services"
service_name: "Kernel"
description: "you build agents. we give them the internet"
permalink: /services/kernel/
page_kind: service
service_slug: "kernel"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/kernel.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/kernel.md"
tagline: "you build agents. we give them the internet"
verified_at: "2026-09-30"
website: "https://www.kernel.sh/"
repository: "https://github.com/kernel/kernel-images"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0 (kernel/kernel-images, kernel/cli)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.kernel.sh/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.kernel.sh/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/kernel/kernel-images" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/kernel.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Kernel is cloud browser infrastructure for AI agents. It spins up sandboxed Chromium (hosted unikernel images, advertised cold start under 30ms) that agents drive with Playwright, CDP, WebDriver BiDi, or computer-use actions. The platform adds stealth/CAPTCHA/proxy handling, managed auth, live view, MP4 replay, browser pools, and a serverless app platform that runs agent loops next to the browser.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + published Agent Skill
- **Catalog protocols:** Agent Skill, MCP, CLI, http
- **MCP:** ✅ Available (hosted remote MCP)
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** CLI + published Agent Skill

```bash
brew install kernel/tap/kernel
# or
npm install -g @onkernel/cli

kernel --version
export KERNEL_API_KEY=your_api_key
# fallback: kernel login
kernel browsers create -o json
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/kernel.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `kernel browsers`, `deploy`, `invoke`, `auth`, pools, profiles, proxies |
| Agent Skill | `kernel-cli` in [kernel/skills](https://github.com/kernel/skills) |
| MCP | Hosted Streamable HTTP at `https://mcp.onkernel.com/mcp` (OAuth 2.1); source https://github.com/kernel/kernel-mcp-server |
| CDP / Playwright / BiDi | Connect to hosted or self-hosted Chromium |
| Open-source images | https://github.com/kernel/kernel-images |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://github.com/kernel/cli/releases/tag/v0.41.0
- https://www.kernel.sh/docs/reference/mcp-server

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
