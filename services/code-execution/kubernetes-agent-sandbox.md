# Agent Sandbox (Kubernetes SIG)

> **"Agent Sandbox provides a secure and isolated execution layer to safely deploy autonomous AI agents on Kubernetes that generate and run untrusted code at scale."**

| | |
|---|---|
| **Website** | https://agent-sandbox.sigs.k8s.io |
| **Docs** | https://agent-sandbox.sigs.k8s.io/docs/ |
| **GitHub** | https://github.com/kubernetes-sigs/agent-sandbox |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/kubernetes-sigs/agent-sandbox?style=social)](https://github.com/kubernetes-sigs/agent-sandbox) |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-08-25 ([repo metadata](https://api.github.com/repos/kubernetes-sigs/agent-sandbox)); Python package `k8s-agent-sandbox`; SIG Apps CRD |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://agent-sandbox.sigs.k8s.io

---

## Official Repo

https://github.com/kubernetes-sigs/agent-sandbox

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK` + Kubernetes CRDs

This is **not** the hosted [Agent Sandbox](agent-sandbox.md) product at agentsandbox.co. It is also not [OpenSandbox](opensandbox.md), which can integrate this CRD as a backend.

```bash
pip install k8s-agent-sandbox
```

Official Python SDK ([client README](https://github.com/kubernetes-sigs/agent-sandbox/blob/main/clients/python/agentic-sandbox-client/README.md)):

```python
from k8s_agent_sandbox import SandboxClient

client = SandboxClient()
sandbox = client.create_sandbox(
    warmpool="example-sandbox-pool",
    namespace="default",
)
try:
    result = sandbox.commands.run("echo 'Hello from Agent Sandbox!'")
    print(result.stdout)
finally:
    sandbox.terminate()
```

Install the controller first (version tag from [releases](https://github.com/kubernetes-sigs/agent-sandbox/releases)):

```bash
export VERSION="vX.Y.Z"
kubectl apply -f https://github.com/kubernetes-sigs/agent-sandbox/releases/download/${VERSION}/sandbox-with-extensions.yaml
```

The official quickstart lists **kubectl 1.28+** as a prerequisite ([quickstart](https://agent-sandbox.sigs.k8s.io/docs/use-cases/examples/quickstart/)). Strong isolation is optional and uses a Kubernetes `RuntimeClass` such as gVisor or Kata Containers; the project is a *sandbox orchestrator* and delegates isolation to those runtimes.

---

## Agent Skills

**Status:** ⚠️ No official Agent Skills package published.

```bash
npx clawhub@latest search kubernetes-agent-sandbox
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not published as a dedicated official MCP server.

| Detail | Value |
|---|---|
| **Primary interface** | Kubernetes CRDs (`Sandbox`, `SandboxClaim`, `SandboxWarmPool`, `SandboxTemplate`) + Python/Go SDKs |
| **Compatible clients** | Any agent that can call `k8s-agent-sandbox` or the Go client against a configured cluster |

---

## What It Does

Kubernetes SIG Agent Sandbox (SIG Apps) is a declarative API for isolated, stateful, singleton workloads — the kind of long-running, identity-stable container AI agent runtimes and RL evaluators need. The core `Sandbox` CRD gives a stable hostname, persistent storage, and lifecycle (create, scheduled delete, pause, resume). Extensions add reusable templates, warm pools, and claim-based allocation.

Official scope: it orchestrates sandboxes; it does **not** implement gVisor or Kata itself. Pods select those isolation backends through `RuntimeClass`. Homepage use cases include short-lived code execution, coding agents, computer-use desktops, CI, and always-on OpenClaw environments.

**Distinctness:** this entry is the in-cluster CRD/controller. The catalog already lists hosted [Agent Sandbox](agent-sandbox.md) (`agentsandbox.co`) — a different product with URL onboarding. [OpenSandbox](opensandbox.md) is a separate sandbox runtime that can sit on Kubernetes and may consume this CRD; it is not this SIG project.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: **"Agent Sandbox provides a secure and isolated execution layer to safely deploy autonomous AI agents on Kubernetes that generate and run untrusted code at scale."** — [agent-sandbox.sigs.k8s.io](https://agent-sandbox.sigs.k8s.io). README: ideal for **"AI agent runtimes and reinforcement learning"** |
| **Agent-specific primitive** | `Sandbox` / `SandboxClaim` / `SandboxWarmPool` CRDs; SDK `create_sandbox` + `commands.run`; warm-pool claims for low-latency agent start |
| **Autonomy-compatible control plane** | After the controller and a warm pool exist, an agent creates a sandbox, runs commands, and terminates without a human `kubectl` per action |
| **M2M integration surface** | Python `k8s-agent-sandbox`, Go `sigs.k8s.io/agent-sandbox/clients/go/sandbox`, Kubernetes API |
| **Identity / delegation** | Each Sandbox has a stable hostname and network identity. `create_sandbox` can stamp claim labels and pod labels/annotations (for example a tenant `client-id` via the Downward API). RBAC on the cluster is the authorization plane |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Sandbox CRD** | Single stateful pod with stable identity, storage, pause/resume, scheduled deletion |
| **SandboxTemplate** | Reusable sandbox spec |
| **SandboxWarmPool** | Pre-warmed sandboxes for fast claims |
| **SandboxClaim** | Allocates a sandbox from a warm pool and hides template detail |
| **RuntimeClass isolation** | Optional gVisor or Kata (or other) backend selected on the Pod spec |
| **SandboxClient** | Python/Go clients: `create_sandbox`, `commands.run`, `terminate` |
| **Sandbox router** | Reverse proxy / gateway path so clients do not port-forward each pod (required with some isolated runtimes) |

---

## Autonomy Model

```
Operator installs the controller and (optionally) a RuntimeClass + SandboxWarmPool
    -> Agent authenticates to the cluster and constructs SandboxClient
    -> client.create_sandbox(...) watches the claim until Ready
    -> Agent runs commands inside the isolated pod
    -> Agent terminates the sandbox (or the controller enforces scheduled deletion)
```

Warm pools make the claim path fast; custom env or volume templates force a cold start per official SDK notes.

---

## Identity and Delegation Model

- **Sandbox identity:** Stable hostname and network identity per Sandbox object (`agents.x-k8s.io`).
- **Claim vs pod metadata:** Labels on the `SandboxClaim`; optional `pod_labels` / `pod_annotations` on the running pod for in-sandbox tenant checks.
- **Cluster RBAC:** The agent's kubeconfig or in-cluster service account is the delegated credential. This project does not mint a hosted API key.
- **Isolation ≠ this controller:** Strong isolation is the RuntimeClass (gVisor/Kata). The SIG project orchestrates Pods that use those classes.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Kubernetes API | `Sandbox`, `SandboxTemplate`, `SandboxClaim`, `SandboxWarmPool` |
| Python SDK | `pip install k8s-agent-sandbox` — [PyPI](https://pypi.org/project/k8s-agent-sandbox/) |
| Go SDK | `go get sigs.k8s.io/agent-sandbox/clients/go/sandbox@latest` |
| Docs | https://agent-sandbox.sigs.k8s.io/docs/ |

---

## Human-in-the-Loop Support

Cluster install, RuntimeClass, and warm-pool templates are operator work. Runtime command execution is SDK/API-driven. `kubectl` remains available for debug; it is not required per agent command.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Hosted Agent Sandbox (agentsandbox.co)** | Different product: hosted sessions + `skill.md` URL onboarding. Not the Kubernetes SIG CRD |
| **OpenSandbox** | Separate sandbox runtime. It may *integrate* this CRD; it is not the SIG controller |
| **A Deployment or StatefulSet** | Generic workload APIs. They lack Sandbox claims, warm pools, and agent-oriented pause/resume |
| **Local Docker only** | No cluster-wide Sandbox identity, warm-pool claims, or RuntimeClass orchestration API |

---

## Use Cases

- **Untrusted code interpreters** — run generated code in isolated Kubernetes sandboxes
- **Coding agents** — medium-lived sandboxes with persistent storage and a stable hostname
- **RL / eval harnesses** — high-throughput warm-pool claims for isolated scoring environments
- **Computer-use / OpenClaw** — GUI or always-on agent environments behind a Sandbox + RuntimeClass
