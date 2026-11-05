---
title: "Moli | Agent-Native Services"
service_name: "Moli"
description: "Moli is a production-ready, structured-first browser engine for AI agents"
permalink: /services/moli/
page_kind: service
service_slug: "moli"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/moli.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/moli.md"
tagline: "Moli is a production-ready, structured-first browser engine for AI agents"
verified_at: "2026-09-26"
website: "https://browser.lexmount.com"
repository: "https://github.com/lexmount/moli"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Open-source engine; Apache-2.0 or MIT at the user&#x27;s option; managed Lexmount Browser control plane is separate</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://browser.lexmount.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/lexmount/moli#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/lexmount/moli" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/moli.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Moli is a Rust browser kernel built for agent workloads that usually need page structure rather than a continuously rendered visual world. It runs JavaScript, DOM, CSS, networking, browser storage, workers, and browser APIs by default, then computes real layout or software-rendered pixels only when an operation requests them.

Agents can extract HTML, Markdown, JSON, or compact semantic trees from the CLI, drive the same runtime through CDP and both WebDriver protocols, or launch the first-party stdio MCP server. Profiles, cookies, cache directories, proxies, network policies, timeouts, resource families, structured logging, and tracing are explicit operational controls rather than hidden browser defaults.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, STDIO
- **MCP:** ✅ Available — the first-party stdio server and moli mcp command ship in the v0.1.1 source/release. The command is not yet advertised in the top-level README, so treat this as an early, under-documented interface.
- **Agent Skill:** ⚠️ Not yet published by the project.
- **Onboarding type:** `mcp`

## How agents onboard

```bash
cargo build --release -p moli

./target/release/moli fetch \
  --dump semantic_tree_text \
  --wait-selector body \
  https://example.com

./target/release/moli serve

# Or expose Moli's first-party MCP server over stdio:
./target/release/moli mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/moli.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **CLI fetch** | HTML, Markdown, JSON, semantic-tree, selector/script/response waits, profile and network controls |
| **CDP** | Browser automation and Playwright `connectOverCDP()` on the default server endpoint |
| **WebDriver Classic** | Standard WebDriver commands served by the same kernel and scheduler |
| **WebDriver BiDi** | Bidirectional browser automation on the same endpoint |
| **MCP stdio** | `moli mcp`; browser navigation, extraction, script evaluation, semantic-tree, wait, and element-action tools plus HTML/Markdown resources |
| **Screenshots / PDF / screencast** | Software-rendered visual surfaces under `--layout`, within the documented scope |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/lexmount/moli/releases/tag/v1.1.10
- https://browser.lexmount.com
- https://api.github.com/repos/lexmount/moli

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
