---
title: "Holm | Agent-Native Services"
service_name: "Holm"
description: "Isolated desktops for AI agents"
permalink: /services/holm/
page_kind: service
service_slug: "holm"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/holm.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/holm.md"
tagline: "Isolated desktops for AI agents"
verified_at: "2026-11-25"
website: "https://holm.computer"
repository: "https://github.com/holm-inc/holm"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT (Copyright 2026 Oyetoke Toby)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-25</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://holm.computer" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/holm-inc/holm" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/holm-inc/holm" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/holm.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Holm runs an isolated Linux desktop box for an agent: browser, native apps, shell, files, and screens. The agent drives it from the CLI, a Rust crate, REST, or MCP. The operator can watch in a browser and take the pointer when the agent asks. `hand_over` is optional and is how a person clears a CAPTCHA or a login. Traces and forks are part of the box, so a run can be inspected or branched.

Runtimes named for this project are Docker, Podman, smolvm, microsandbox, and E2B. The last push on the public repo was 2026-10-05. The website still answered HTTP 200 on 2026-11-25. Treat the repo date as the code's last published change, not as a hosted status page.

---

## Agent-facing interfaces

- **Interaction pattern:** local CLI and self-hosted MCP. Not a one-URL join.
- **Catalog protocols:** MCP, REST, CLI, STDIO, http
- **MCP:** ✅ Available — local stdio, or Streamable HTTP on a server you run
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** local CLI and self-hosted MCP. Not a one-URL join.

```bash
# Install holm and holmd, then a runtime (Docker, Podman, smolvm, microsandbox, or E2B).
holm mcp --stdio
# or Streamable HTTP on your own holmd: /mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/holm.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `holm`, `holmd` |
| Rust | Crate in https://github.com/holm-inc/holm |
| REST | Served by the self-hosted daemon |
| MCP | `holm mcp --stdio`, or Streamable HTTP `/mcp` on `holmd` |
| Docs | https://github.com/holm-inc/holm and https://holm.computer |

---

## Verification

Last verified **2026-11-25**.

Sources:
- https://holm.computer
- https://github.com/holm-inc/holm

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
