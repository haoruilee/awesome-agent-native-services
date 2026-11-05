---
title: "YYLO | Agent-Native Services"
service_name: "YYLO"
description: "Run the work. Keep the memory"
permalink: /services/yylo/
page_kind: service
service_slug: "yylo"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/yylo.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/yylo.md"
tagline: "Run the work. Keep the memory"
website: "https://yylo.dev"
repository: "https://github.com/yylo-dev/yylo"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://yylo.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/yylo-dev/yylo#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/yylo-dev/yylo" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/yylo.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

YYLO is a command-line orchestrator for coding agents. It coordinates a typed task loop — intent, isolated worktree, validation, review, merge, and release-readiness — and keeps the receipts that explain what happened. It does not replace Git. It routes bounded work to coding subagents, freezes a protected target SHA, and records task, session, review, and evaluation evidence.

The control plane (`yy` / `yylo`) coordinates action; [YYLO Ledger](https://github.com/yylo-dev/yylo-ledger) preserves task truth in Git; [YYLO Benchmark](https://github.com/yylo-dev/yylo-benchmark) turns attempts into evaluation evidence.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI
- **Catalog protocols:** Agent Skill, CLI, http
- **MCP:** ⚠️ Not yet published
- **Agent Skill:** ✅ Available (independently versioned; not bundled in @yylo/cli)
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI

```bash
npm install --global '@yylo/cli@latest'
yy --version
yy init --task "Ship one verified change" --subagent pi
yy info --json
yy doctor workspace
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/yylo.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `yylo` and `yy` (equivalent); `ypl` is `yy pi --live` — [@yylo/cli](https://www.npmjs.com/package/@yylo/cli) |
| Machine output | `--format json\|ndjson --raw`; `yy info --json`; `yy capabilities` |
| Receipts | Watch receipts, terminal manifests, content-addressed evidence |
| Agent Skills | [yylo-dev/yylo-skills](https://github.com/yylo-dev/yylo-skills) |
| Ledger / Benchmark | Separate CLIs via `yy ledger` / `yy benchmark` |
| MCP | Not published |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
