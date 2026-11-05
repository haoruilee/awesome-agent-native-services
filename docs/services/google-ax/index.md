---
title: "Agent Executor (AX) | Agent-Native Services"
service_name: "Agent Executor (AX)"
description: "An open source distributed agent runtime"
permalink: /services/google-ax/
page_kind: service
service_slug: "google-ax"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/google-ax.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/google-ax.md"
tagline: "An open source distributed agent runtime"
verified_at: "2026-09-30"
website: "https://agentexecutor.io"
repository: "https://github.com/google/ax"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">GRPC · CLI</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-30</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentexecutor.io" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/google/ax#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/google/ax" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/google-ax.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AX (Agent Executor) is a self-hosted distributed harness runtime from Google. It provisions isolated environments from suspendable/resumable images, runs harnesses and agents, and keeps durable execution state in an event log so work can resume after failure. It is compute-agnostic, with the best-documented path on Kubernetes via Agent Substrate. Official text says AX is **not** a managed service and **not** an agentic framework.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + optional gRPC server
- **Catalog protocols:** GRPC, CLI
- **MCP:** ⚠️ Consumer, not a published MCP server
- **Agent Skill:** ⚠️ Hosted by the harness, not a published npx skills add package
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + optional gRPC server

```bash
go install github.com/google/ax/cmd/ax@latest
ax --help

# Local built-in Antigravity harness (needs GEMINI_API_KEY or Vertex ADC)
ax --input "Can you list this directory?"

# Resume
ax --conversation <id> --input "Show me the contents of README.md"
ax --conversation <id> --resume
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/google-ax.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `ax`, `ax serve`, `--conversation`, `--resume`, `--server` |
| gRPC | Controller when `--server` is set (default example `:8494`) |
| Config | `ax.yaml` (`version: v1alpha`) |
| K8s | `manifests/` + Agent Substrate |

---

## Verification

Last verified **2026-09-30**.

Sources:
- https://github.com/google/ax/releases/tag/v0.3.1
- https://agentexecutor.io

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
