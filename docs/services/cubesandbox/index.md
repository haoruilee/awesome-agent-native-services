---
title: "CubeSandbox | Agent-Native Services"
service_name: "CubeSandbox"
description: "Instant, Concurrent, Secure & Lightweight Sandbox Service for AI Agents"
permalink: /services/cubesandbox/
page_kind: service
service_slug: "cubesandbox"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/cubesandbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/cubesandbox.md"
tagline: "Instant, Concurrent, Secure & Lightweight Sandbox Service for AI Agents"
verified_at: "2026-10-20"
website: "https://cubesandbox.com"
repository: "https://github.com/TencentCloud/CubeSandbox"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0 (GitHub SPDX shows NOASSERTION because LICENSE wraps Apache-2.0 plus third-party component exceptions — official file: “Cube Sandbox is licensed under the Apache-2.0 except for the third-party components listed below.”)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · CLI · SDK</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://cubesandbox.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://cubesandbox.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/TencentCloud/CubeSandbox" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/cubesandbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

CubeSandbox is a **self-hosted microVM sandbox service** built on RustVMM and KVM. It boots a hardware-isolated, fully serviceable sandbox in under 60 ms with less than 5 MB of memory overhead, and is **compatible with the E2B SDK** — switch from E2B Cloud by changing `E2B_API_URL`.

The control plane (CubeAPI / CubeMaster / Cubelet / CubeProxy) plus CubeCoW snapshots, AutoPause, an eBPF virtual switch (CubeVS), and an L7 egress proxy (CubeEgress) are designed for high-concurrency AI-agent code execution, not a human IDE.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [E2B](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/e2b.md) | Hosted cloud sandboxes + E2B’s own control plane. CubeSandbox is the **self-host E2B-compatible** microVM service |
| [OpenSandbox](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/opensandbox.md) | Sandbox runtime / K8s / MCP. Cube is RustVMM+KVM with an E2B wire-compatible API |
| [Dormice](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/dormice.md) | Early-dev E2B-compat daemon; Cube is a production-oriented Tencent Cloud OSS cluster |
| [forkd](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/forkd.md) | Firecracker CoW **fork/BRANCH** from a warmed parent. Cube cold-starts / pools microVMs; it is not fork-from-warm |
| [SmolVM](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/smolvm.md) | Local Firecracker/QEMU/libkrun SDK for disposable agent computers. Cube is a multi-node E2B-compatible service |

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + E2B-compatible SDK
- **Catalog protocols:** REST, CLI, SDK
- **MCP:** ⚠️ Not yet published as a first-party MCP server.
- **Agent Skill:** ⚠️ No official npx skills add package published yet.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + E2B-compatible SDK

```bash
curl -sL https://github.com/tencentcloud/CubeSandbox/raw/master/deploy/one-click/online-install.sh | CUBE_PVM_ENABLE=1 bash
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/cubesandbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| E2B-compatible REST | CubeAPI on `:3000` |
| E2B Python SDK | `pip install e2b-code-interpreter` + `E2B_API_URL` |
| Native Python SDK | `pip install cubesandbox` + `CUBE_API_URL` |
| CLI | `cubemastercli`, `cubeopscli` |
| WebUI | `:12088` — optional operator console |
| License | Apache-2.0 + third-party exceptions in `LICENSE` (GitHub `NOASSERTION`) |

---

## Verification

Last verified **2026-10-20**.

Sources:
- https://api.github.com/repos/TencentCloud/CubeSandbox

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
