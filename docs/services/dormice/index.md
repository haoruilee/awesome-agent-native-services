---
title: "Dormice | Agent-Native Services"
service_name: "Dormice"
description: "The SQLite of agent sandboxes — a self-hosted sandbox platform for AI agents. One machine, sandboxes that live forever, idle costs nothing"
permalink: /services/dormice/
page_kind: service
service_slug: "dormice"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/dormice.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/dormice.md"
tagline: "The SQLite of agent sandboxes — a self-hosted sandbox platform for AI agents. One machine, sandboxes that live forever, idle costs nothing"
verified_at: "2026-10-13"
website: "https://github.com/BitMiracle-AI/Dormice"
repository: "https://github.com/BitMiracle-AI/Dormice"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · CLI · SDK · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/BitMiracle-AI/Dormice" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/BitMiracle-AI/Dormice/blob/main/README.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/BitMiracle-AI/Dormice" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/dormice.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Dormice is a **self-hosted sandbox platform** that inverts billed-ephemeral cloud sandboxes. Official idea: you run one daemon on a machine you already pay for; sandboxes are **permanent** and get cheaper the longer they sit idle (`active → frozen → stopped → archived`). `acquireSandbox(userKey)` is idempotent — same key always returns the same sandbox.

Idle freeze is the headline: README claims freezing an idle 1 GiB sandbox down to ~5 MiB RSS and ~50 ms wake (measured on their hardware). Deploy shape: one daemon, one SQLite ledger, one port. Isolation is Docker + gVisor, not Firecracker.

**Early-dev warning (do not skip):** README status block: the daemon, lifecycle engine, SDK, CLI, console, Docker+gVisor executor, S3 archiver, and E2B-compatible API work end to end — **"Nothing here is ready for production yet."** Treat it as evaluation software, same honesty bar as [Axern](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/axern.md).

**Distinct from [E2B](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/e2b.md)** (billed ephemeral cloud): self-hosted, single-binary-shaped, permanent cheap-idle sandboxes, E2B SDK by changing two URLs. **Not** [Kubernetes SIG Agent Sandbox](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/kubernetes-agent-sandbox.md) and **not** hosted [Agent Sandbox](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-sandbox.md) (`agentsandbox.co`).

---

## Agent-facing interfaces

- **Interaction pattern:** self-hosted daemon + SDK / CLI / Agent Skill
- **Catalog protocols:** Agent Skill, CLI, SDK, http, API
- **MCP:** ⚠️ Not published as a dedicated MCP server.
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** self-hosted daemon + SDK / CLI / Agent Skill

```bash
curl -fsSL https://raw.githubusercontent.com/BitMiracle-AI/Dormice/main/deploy/install.sh | bash
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/dormice.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Installer | `curl -fsSL https://raw.githubusercontent.com/BitMiracle-AI/Dormice/main/deploy/install.sh \| bash` |
| HTTP RPC | `http://127.0.0.1:3676/<verb>` + `Authorization: Bearer` |
| Native SDK | `@dormice/sdk` (build from repo until npm publish) |
| E2B SDK | Official `e2b` package against `/e2b/api` and `/e2b/envd` |
| CLI | `dor` |
| Agent Skill | `npx skills add BitMiracle-AI/Dormice` |
| Console | `http://127.0.0.1:3676/console` |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/BitMiracle-AI/Dormice

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
