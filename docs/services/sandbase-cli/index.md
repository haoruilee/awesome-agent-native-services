---
title: "SandBase CLI | Agent-Native Services"
service_name: "SandBase CLI"
description: "Give your AI agent superpowers. One command. 2,000+ AI models"
permalink: /services/sandbase-cli/
page_kind: service
service_slug: "sandbase-cli"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/sandbase-cli.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/sandbase-cli.md"
tagline: "Give your AI agent superpowers. One command. 2,000+ AI models"
verified_at: "2026-10-13"
website: "https://www.sandbase.ai"
repository: "https://github.com/sandbaseai/cli"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · STDIO · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.sandbase.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/sandbaseai/cli#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/sandbaseai/cli" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/sandbase-cli.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

SandBase CLI is an Apache-2.0 TypeScript CLI that connects a coding agent to a catalog of 2,000+ models and APIs through a compact local MCP surface. The operator (or an installer) runs `connect` once; the CLI detects supported clients, opens a browser authorization, writes a client-scoped credential, and adds only SandBase-owned MCP configuration.

After that, the agent searches the catalog (`sandbase_discover`), reads the current schema and price (`sandbase_inspect`), and executes (`sandbase_run`), polling async jobs with `sandbase_run_get`. `sandbase_runs` and `sandbase_account` expose recent cost and balance without starting a paid run.

This is a **tool-access bridge**, not an LLM gateway and not the SandBase Store. The homepage and [Getting Started](https://www.sandbase.ai/docs/getting-started/) docs describe a builder/FDE platform (Store, Setup, Build Agent). Those products are out of scope here. The sibling [SandBase Harness](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/../agent-runtime-and-infrastructure/sandbase-harness.md) is cataloged separately. [sandbase-skills](https://github.com/sandbaseai/sandbase-skills) is not cataloged.

---

## Agent-facing interfaces

- **Interaction pattern:** local MCP bridge (stdio) after one browser approval
- **Catalog protocols:** Agent Skill, MCP, CLI, STDIO, http
- **MCP:** ✅ Available (local on-demand bridge)
- **Agent Skill:** ✅ Available
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** local MCP bridge (stdio) after one browser approval

```sh
npx -y https://github.com/sandbaseai/cli/releases/download/v0.1.17/sandbaseai-cli-0.1.17.tgz connect
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/sandbase-cli.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Local MCP | On-demand stdio bridge exposing six `sandbase_*` tools |
| CLI | `connect`, `doctor`, `unregister`, `catalog --json` |
| Agent Skill | `npx skills add sandbaseai/cli --skill sandbase` |
| Installer notes | [llms-install.md](https://github.com/sandbaseai/cli/blob/main/llms-install.md) |
| Parent platform API | Separate HTTP API on sandbase.ai — not this catalog entry |
| npm package | `@sandbaseai/cli` exists; `latest` is v0.1.14 as of 2026-08-25 |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://github.com/sandbaseai/cli/releases/tag/v0.1.17

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
