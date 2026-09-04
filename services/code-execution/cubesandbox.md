# CubeSandbox

> **"Instant, Concurrent, Secure & Lightweight Sandbox Service for AI Agents"**

| | |
|---|---|
| **Website** | https://cubesandbox.com |
| **Docs** | https://cubesandbox.com |
| **GitHub** | https://github.com/TencentCloud/CubeSandbox |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/TencentCloud/CubeSandbox?style=social)](https://github.com/TencentCloud/CubeSandbox) |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **License** | Apache-2.0 (GitHub SPDX shows `NOASSERTION` because `LICENSE` wraps Apache-2.0 plus third-party component exceptions — official file: “Cube Sandbox is licensed under the Apache-2.0 except for the third-party components listed below.”) |
| **Latest-month signal** | Last GitHub push 2026-09-03 ([repo metadata](https://api.github.com/repos/TencentCloud/CubeSandbox)); one-click installer + E2B-compatible API on `:3000` |
| **Verified at** | 2026-09-04 |

---

## Official Website

https://cubesandbox.com

Docs home hero (live 2026-09-04, [docs/index.md](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/index.md)): name **Cube Sandbox**, text **“Empowering your AI Agents.”**, tagline **“Instant, Concurrent, Secure & Lightweight Sandbox Service for AI Agents”**. Quick Start is at [cubesandbox.com/guide/quickstart](https://cubesandbox.com/guide/quickstart).

---

## Official Repo

https://github.com/TencentCloud/CubeSandbox

GitHub description (live 2026-09-04): **“Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.”** — same lead as the docs/README hero, minus the word “Service.” README repeats the hero tagline with “Service.”

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + E2B-compatible SDK

One-click install on an x86_64 Linux host (root; official [Quick Start](https://cubesandbox.com/guide/quickstart)):

```bash
curl -sL https://github.com/tencentcloud/CubeSandbox/raw/master/deploy/one-click/online-install.sh | CUBE_PVM_ENABLE=1 bash
```

Create a code-interpreter template, then point the official E2B SDK at the local CubeAPI:

```bash
pip install e2b-code-interpreter
export E2B_API_URL="http://127.0.0.1:3000"
export E2B_API_KEY="e2b_000000"
export CUBE_TEMPLATE_ID="<your-template-id>"
```

```python
import os
from e2b_code_interpreter import Sandbox

with Sandbox.create(template=os.environ["CUBE_TEMPLATE_ID"]) as sandbox:
    result = sandbox.run_code("print('Hello from Cube Sandbox, safely isolated!')")
    print(result)
```

Native Python SDK (`pip install cubesandbox`) uses `CUBE_API_URL` / `CUBE_TEMPLATE_ID` and `from cubesandbox import Sandbox`. There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

```bash
npx clawhub@latest search cubesandbox
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not yet published as a first-party MCP server.

The agent surface is the E2B-compatible REST API (port `3000`) plus the official `e2b-code-interpreter` SDK or native `cubesandbox` SDK. Cube can run agent workloads (OpenClaw examples ship in the repo); it does not expose an official MCP endpoint as of 2026-09-04.

| Detail | Value |
|---|---|
| **MCP Repo** | — |
| **Transport** | — |
| **Compatible Clients** | Any E2B SDK client; `e2b-code-interpreter`; `cubesandbox` SDK |

---

## What It Does

CubeSandbox is a **self-hosted microVM sandbox service** built on RustVMM and KVM. It boots a hardware-isolated, fully serviceable sandbox in under 60 ms with less than 5 MB of memory overhead, and is **compatible with the E2B SDK** — switch from E2B Cloud by changing `E2B_API_URL`.

The control plane (CubeAPI / CubeMaster / Cubelet / CubeProxy) plus CubeCoW snapshots, AutoPause, an eBPF virtual switch (CubeVS), and an L7 egress proxy (CubeEgress) are designed for high-concurrency AI-agent code execution, not a human IDE.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [E2B](e2b.md) | Hosted cloud sandboxes + E2B’s own control plane. CubeSandbox is the **self-host E2B-compatible** microVM service |
| [OpenSandbox](opensandbox.md) | Sandbox runtime / K8s / MCP. Cube is RustVMM+KVM with an E2B wire-compatible API |
| [Dormice](dormice.md) | Early-dev E2B-compat daemon; Cube is a production-oriented Tencent Cloud OSS cluster |
| [forkd](forkd.md) | Firecracker CoW **fork/BRANCH** from a warmed parent. Cube cold-starts / pools microVMs; it is not fork-from-warm |
| [SmolVM](smolvm.md) | Local Firecracker/QEMU/libkrun SDK for disposable agent computers. Cube is a multi-node E2B-compatible service |

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs/README hero tagline: **“Instant, Concurrent, Secure & Lightweight Sandbox Service for AI Agents”** — [cubesandbox.com](https://cubesandbox.com), [docs/index.md](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/index.md). GitHub description: **“Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.”** Hero text: **“Empowering your AI Agents.”** |
| **Agent-specific primitive** | Per-agent KVM microVM; E2B-compatible sandbox lifecycle; CubeCoW snapshot/clone/rollback; AutoPause/AutoResume; credential vault so API keys never enter the sandbox |
| **Autonomy-compatible control plane** | After install + template, agents create/run/destroy sandboxes via SDK/API with no dashboard click. WebUI on `:12088` is optional ops |
| **M2M integration surface** | E2B-compatible REST (`:3000`), `e2b-code-interpreter`, native `cubesandbox` SDK, `cubemastercli` / `cubeopscli` |
| **Identity / delegation** | Per-sandbox dedicated kernel + eBPF isolation; optional API key (`CUBE_API_KEY` / `X-API-Key`); CubeEgress injects credentials so secrets never appear in sandbox code; sandbox IDs attribute exec |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **E2B-compatible sandbox** | Drop-in `Sandbox.create()` against self-hosted CubeAPI |
| **Sub-60 ms microVM** | RustVMM + KVM; pooled / snapshot-cloned cold start |
| **CubeCoW** | Hundred-millisecond snapshot, clone, rollback |
| **AutoPause / AutoResume** | Idle sandboxes suspend; next request wakes them |
| **Credential vault + CubeEgress** | L7 domain/path/method policy; keys injected, never visible in-guest |
| **Volume framework** | E2B-compatible volumes with independent lifecycle |

---

## Autonomy Model

```
Operator installs Cube (one-click or Terraform/K8s) and builds a READY template
    -> Agent sets E2B_API_URL to the CubeAPI and calls Sandbox.create(...)
    -> CubeMaster schedules a Cubelet microVM; code runs isolated
    -> stdout/stderr/files stream back; agent iterates or destroys
    -> Optional AutoPause parks idle VMs; WebUI is not on the data path
```

---

## Identity and Delegation Model

- **Sandbox identity:** each instance is a dedicated-kernel microVM with its own network token and policy-routed egress.
- **Caller credentials:** optional API key on CubeAPI (`CUBE_API_KEY`); local quickstart uses a placeholder `E2B_API_KEY` when auth is off.
- **Secret delegation:** CubeEgress / credential vault injects upstream keys so agent code never sees them.
- **Audit:** sandbox IDs, egress logs, and WebUI/ops surfaces attribute work to a concrete instance.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| E2B-compatible REST | CubeAPI on `:3000` |
| E2B Python SDK | `pip install e2b-code-interpreter` + `E2B_API_URL` |
| Native Python SDK | `pip install cubesandbox` + `CUBE_API_URL` |
| CLI | `cubemastercli`, `cubeopscli` |
| WebUI | `:12088` — optional operator console |
| License | Apache-2.0 + third-party exceptions in `LICENSE` (GitHub `NOASSERTION`) |

---

## Human-in-the-Loop Support

Optional WebUI for templates, capacity, and live logs. Agent code execution does not require a click. First-time cluster install and template build are operator steps.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **E2B Cloud** | Hosted product. CubeSandbox is the self-host, E2B-compatible microVM service — listed separately |
| **OpenSandbox / Dormice** | Different runtime (K8s/Docker abstraction or early-dev daemon), not this RustVMM+KVM cluster |
| **forkd / SmolVM** | Fork-from-warm Firecracker fan-out, or local multi-VMM SDK — not an E2B-wire self-host service |
| **Raw Docker / KVM** | No E2B sandbox lifecycle, CubeCoW, or credential-vault egress |

---

## Use Cases

- **Self-host E2B workloads** — keep the E2B SDK, change one URL
- **High-density agent code exec** — thousands of microVMs per node via CoW
- **Secret-safe tool calls** — egress proxy injects API keys
- **Snapshot / clone / rollback** — explore branches of agent state without a full cold boot
