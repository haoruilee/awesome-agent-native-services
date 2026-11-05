---
title: "Agent Sandbox (Kubernetes SIG) | Agent-Native Services"
service_name: "Agent Sandbox (Kubernetes SIG)"
description: "Agent Sandbox provides a secure and isolated execution layer to safely deploy autonomous AI agents on Kubernetes that generate and run untrusted code at scale"
permalink: /services/kubernetes-agent-sandbox/
page_kind: service
service_slug: "kubernetes-agent-sandbox"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/kubernetes-agent-sandbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/kubernetes-agent-sandbox.md"
tagline: "Agent Sandbox provides a secure and isolated execution layer to safely deploy autonomous AI agents on Kubernetes that generate and run untrusted code at scale"
verified_at: "2026-10-13"
website: "https://agent-sandbox.sigs.k8s.io"
repository: "https://github.com/kubernetes-sigs/agent-sandbox"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agent-sandbox.sigs.k8s.io" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://agent-sandbox.sigs.k8s.io/docs/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/kubernetes-sigs/agent-sandbox" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/kubernetes-agent-sandbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Kubernetes SIG Agent Sandbox (SIG Apps) is a declarative API for isolated, stateful, singleton workloads — the kind of long-running, identity-stable container AI agent runtimes and RL evaluators need. The core `Sandbox` CRD gives a stable hostname, persistent storage, and lifecycle (create, scheduled delete, pause, resume). Extensions add reusable templates, warm pools, and claim-based allocation.

Official scope: it orchestrates sandboxes; it does **not** implement gVisor or Kata itself. Pods select those isolation backends through `RuntimeClass`. Homepage use cases include short-lived code execution, coding agents, computer-use desktops, CI, and always-on OpenClaw environments.

**Distinctness:** this entry is the in-cluster CRD/controller. The catalog already lists hosted [Agent Sandbox](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-sandbox.md) (`agentsandbox.co`) — a different product with URL onboarding. [OpenSandbox](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/opensandbox.md) is a separate sandbox runtime that can sit on Kubernetes and may consume this CRD; it is not this SIG project.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK + Kubernetes CRDs
- **Catalog protocols:** SDK, http, API
- **MCP:** ⚠️ Not published as a dedicated official MCP server.
- **Agent Skill:** ⚠️ No official Agent Skills package published.
- **Onboarding type:** `sdk`

## How agents onboard

**Interaction pattern:** SDK + Kubernetes CRDs

```bash
pip install k8s-agent-sandbox
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/kubernetes-agent-sandbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Kubernetes API | `Sandbox`, `SandboxTemplate`, `SandboxClaim`, `SandboxWarmPool` |
| Python SDK | `pip install k8s-agent-sandbox` — [PyPI](https://pypi.org/project/k8s-agent-sandbox/) |
| Go SDK | `go get sigs.k8s.io/agent-sandbox/clients/go/sandbox@latest` |
| Docs | https://agent-sandbox.sigs.k8s.io/docs/ |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/kubernetes-sigs/agent-sandbox

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
