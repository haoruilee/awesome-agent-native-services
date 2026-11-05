---
title: "Axern | Agent-Native Services"
service_name: "Axern"
description: "Axern is an open-source sandbox platform for AI agents"
permalink: /services/axern/
page_kind: service
service_slug: "axern"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/axern.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/axern.md"
tagline: "Axern is an open-source sandbox platform for AI agents"
verified_at: "2026-09-26"
website: "https://axern.cofy-x.space"
repository: "https://github.com/cofy-x/axern"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">GRPC · CLI · SDK · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://axern.cofy-x.space" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://axern.cofy-x.space/getting-started/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/cofy-x/axern" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/axern.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Axern is a self-hosted execution control plane built around agent sandboxes. It runs untrusted, agent-generated code behind the `runsc` boundary and trusted long-lived services through `runc`, while exposing the same lifecycle model for environments, processes, files, archives, storage, services, functions, tunnels, terminals, and computer use.

Its durable control plane stores intent, placement, leases, retries, health, cleanup, quota, and storage state in PostgreSQL. Axrun adds reproducible agent tasks: immutable TaskSets and rollout plans, leased workers, resource and budget admission, verifier/oracle phases, trajectories, usage, and content-addressed evidence.

**Production warning:** upstream explicitly says Axern is pre-1.0 and suitable for evaluation/contribution. The bundled PostgreSQL, MinIO, single-node settings, and generated local credentials are development defaults. Before any shared or multi-tenant deployment, operators must harden authentication, TLS, network policy, runtime isolation, image trust, secrets, quotas, and persistent storage. Upstream also does not publish a sub-second cold-start guarantee; benchmark the chosen topology for interactive agent workloads.

---

## Agent-facing interfaces

- **Interaction pattern:** self-hosted control plane + CLI / SDK
- **Catalog protocols:** GRPC, CLI, SDK, http, API
- **MCP:** ⚠️ Not published — the verified agent-facing surfaces are CLI, SDKs, and Axern's gRPC/HTTP data plane.
- **Agent Skill:** ⚠️ Not yet published — Axern documents agent workflows and ships an Axrun harness, but no standalone SKILL.md package is published.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** self-hosted control plane + CLI / SDK

```bash
brew install cofy-x/tap/axern
axern local up
axern run python:3.12-slim -- python -c 'print("hello from axern")'
axern run list
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/axern.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **CLI** | `axern` for local stack, resources, identity, contexts, runs, agents, services, and administration; JSON-capable output |
| **Python SDK** | `axern-sdk`, sync + async sandbox API; agent tooling, browser/computer use, functions, environments, and services |
| **Go SDK** | Versioned Go module for sandbox operations, controllers, rollout control, and task assets |
| **TypeScript SDK** | `@cofy-x/axern-sdk`, Promise-native sandbox/process/file/tunnel API |
| **Wire protocol** | Public gRPC contracts shared by CLI/SDK; gateway also provides HTTP, SSH, terminal, service, and tunnel edges |
| **Axrun CLI** | NDJSON streaming for plan/start/run/watch, stable terminal exit codes, rollout inspection/comparison, and checksum-verified artifact downloads |
| **Deployment** | Docker Compose local stack or cloud-neutral Kubernetes Helm chart |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/cofy-x/axern/releases/tag/v0.11.4
- https://axern.cofy-x.space
- https://api.github.com/repos/cofy-x/axern

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
