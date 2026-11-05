---
title: "Agent Substrate | Agent-Native Services"
service_name: "Agent Substrate"
description: "A performant, high density runtime environment for large scale agent deployments"
permalink: /services/agent-substrate/
page_kind: service
service_slug: "agent-substrate"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/agent-substrate.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agent-substrate.md"
tagline: "A performant, high density runtime environment for large scale agent deployments"
verified_at: "2026-10-13"
website: "https://github.com/agent-substrate/substrate"
repository: "https://github.com/agent-substrate/substrate"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">GRPC · CLI · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/agent-substrate/substrate" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/agent-substrate/substrate#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/agent-substrate/substrate" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agent-substrate.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agent Substrate maps a large set of idle-heavy **actors** (agent-like applications) onto a smaller pool of ready **workers**. The control plane handles create/destroy, suspend/resume (official claim: sub-second), assignment of actors to workers, and inbound routing. Sandbox backends include microVMs and gVisor. Kubernetes owns pod provisioning and autoscaling; Substrate adds agent-specific scheduling so many stateful actors share few physical pods.

Official README status (quote): **"NOTE: This is not an officially supported Google product. This project is not eligible for the Google Open Source Software Vulnerability Rewards Program."** Further: **"Agent Substrate is currently in early development. It is not ready for production use, and the APIs are almost guaranteed to change. We are not making any guarantees about backward compatibility at this stage."**

It is framework-agnostic: OCI containers via gVisor, not an agent SDK. AX is listed as an ecosystem harness that can run on Substrate.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + Kubernetes control plane
- **Catalog protocols:** GRPC, CLI, http, API
- **MCP:** ⚠️ Not a published MCP server.
- **Agent Skill:** ⚠️ No official Agent Skills package published.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + Kubernetes control plane

```bash
# Local kind path from the official README (development only)
hack/create-kind-cluster.sh
hack/install-ate-kind.sh --deploy-ate-system
hack/install-ate-kind.sh --deploy-demo-counter
go install ./cmd/kubectl-ate

kubectl ate create atespace demo
kubectl ate create actor my-counter-1 -a demo --template=ate-demo-counter/counter
kubectl port-forward -n ate-system svc/atenet-router 8000:80
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/agent-substrate.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `kubectl ate` (`go install ./cmd/kubectl-ate`) |
| gRPC | `cmd/ateapi` lifecycle API |
| Kubernetes | WorkerPool, ActorTemplate, and related CRs |
| HTTP | atenet router (demo port-forward to `:8000`) |
| Docs | Architecture, API guide, CLI README, threat model in-repo |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://api.github.com/repos/agent-substrate/substrate

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
