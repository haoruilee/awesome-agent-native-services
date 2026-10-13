# Agent Substrate

> **"A performant, high density runtime environment for large scale agent deployments."**

| | |
|---|---|
| **Website** | https://github.com/agent-substrate/substrate |
| **Docs** | https://github.com/agent-substrate/substrate#readme |
| **GitHub** | https://github.com/agent-substrate/substrate |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/agent-substrate/substrate?style=social)](https://github.com/agent-substrate/substrate) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-08-25 ([repo metadata](https://api.github.com/repos/agent-substrate/substrate)); early development, APIs expected to change |
| **Verified at** | 2026-10-13 |

---

## Official Website

No separate marketing site is listed on the repository (`homepage` is empty). The canonical entry is the GitHub README:

https://github.com/agent-substrate/substrate

---

## Official Repo

https://github.com/agent-substrate/substrate

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + Kubernetes control plane

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

Then HTTP to the actor via the router `Host` header (see README). GKE bootstrap uses `go run ./tools/setup-gcp bootstrap` and `./hack/install-ate.sh --deploy-ate-system`.

**This is not [Agent Executor (AX)](google-ax.md).** AX (`google/ax`) is a distributed *harness runtime*. Substrate is the Kubernetes *compute control plane* AX documents as a production-oriented deploy path. Do not collapse the two names.

---

## Agent Skills

**Status:** ⚠️ No official Agent Skills package published.

```bash
npx clawhub@latest search agent-substrate
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not a published MCP server.

README compatibility notes say MCP *servers* can run as Substrate Actors (sandboxed durable tools). Substrate itself is `kubectl-ate` + ate-api-server, not an MCP product.

---

## What It Does

Agent Substrate maps a large set of idle-heavy **actors** (agent-like applications) onto a smaller pool of ready **workers**. The control plane handles create/destroy, suspend/resume (official claim: sub-second), assignment of actors to workers, and inbound routing. Sandbox backends include microVMs and gVisor. Kubernetes owns pod provisioning and autoscaling; Substrate adds agent-specific scheduling so many stateful actors share few physical pods.

Official README status (quote): **"NOTE: This is not an officially supported Google product. This project is not eligible for the Google Open Source Software Vulnerability Rewards Program."** Further: **"Agent Substrate is currently in early development. It is not ready for production use, and the APIs are almost guaranteed to change. We are not making any guarantees about backward compatibility at this stage."**

It is framework-agnostic: OCI containers via gVisor, not an agent SDK. AX is listed as an ecosystem harness that can run on Substrate.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: **"Agent Substrate delivers a performant, high density runtime environment for large scale agent deployments"** and **"The workloads it manages don't have to be literal AI agents, but those are the best example of the kind of applications it is designed for. It is not an SDK for building agents, but rather a system for running them at scale."** — [repo](https://github.com/agent-substrate/substrate) |
| **Agent-specific primitive** | Actors, atespaces, ActorTemplates, WorkerPools; suspend/resume with RAM + filesystem snapshots; oversubscription of idle agents onto shared workers |
| **Autonomy-compatible control plane** | After an atespace and template exist, `kubectl ate create actor` and the router send traffic without a human sitting in the pod. Request parking holds requests until a worker frees |
| **M2M integration surface** | `kubectl-ate` CLI, ate-api-server gRPC, Kubernetes CRDs, HTTP via atenet router |
| **Identity / delegation** | Actor DNS/Host routing (`*.actors.resources.substrate.ate.dev` in the demo). Authentication guide documents trusted JWT providers. Early-dev: do not treat this as a supported Google identity product |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Actor** | Stateful application instance that can hibernate and teleport onto a worker |
| **Atespace** | Namespace-like scope; required before creating actors |
| **ActorTemplate** | Image/config used to materialize actors |
| **WorkerPool / Worker** | Physical pod capacity actors multiplex onto |
| **ate-api-server** | gRPC control plane for actor/worker lifecycle |
| **atenet** | DNS + Envoy routing + proxy sidecars |
| **atelet / ateom** | Node supervisor and in-pod checkpoint/restore (gVisor or microVM) |

---

## Autonomy Model

```
Operator provisions a cluster and installs ATE system components
    -> Create an atespace and actor from a template
    -> Router parks or forwards HTTP to the assigned worker
    -> Idle actors suspend; inbound work resumes them onto any free worker
    -> Snapshots keep RAM and filesystem across hibernation
```

The agent workload inside the actor runs its own loop. Substrate's job is density and lifecycle, not prompting.

---

## Identity and Delegation Model

- **Actor identity:** Named actor + atespace, routed by Host/DNS.
- **Human vs workload creds:** Docs include an authentication guide (JWT providers and human credentials). That is cluster/control-plane auth, not a consumer KYA wallet.
- **Support status:** Not an officially supported Google product; not in Google's OSS VRP. Early development; APIs will change.
- **AX relationship:** Substrate ≠ AX. AX is the harness; Substrate is the K8s multiplexed compute plane.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `kubectl ate` (`go install ./cmd/kubectl-ate`) |
| gRPC | `cmd/ateapi` lifecycle API |
| Kubernetes | WorkerPool, ActorTemplate, and related CRs |
| HTTP | atenet router (demo port-forward to `:8000`) |
| Docs | Architecture, API guide, CLI README, threat model in-repo |

---

## Human-in-the-Loop Support

Cluster bootstrap and template install are operator work. Actor traffic after create is machine-routed. Community meeting / Slack are human process, not a runtime approval gate.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **google/ax (Agent Executor)** | Harness runtime: conversations, event log, isolated harnesses. Not the K8s actor/worker multiplex control plane |
| **A plain Kubernetes Deployment** | Replicated stateless pods. No actor teleport, RAM snapshot hibernation, or idle-agent oversubscription API |
| **E2B / hosted sandboxes** | Per-session microVMs as a product API. Substrate is in-cluster density infrastructure for many long-lived actors |

---

## Use Cases

- **High-density coding agents** — multiplex Claude Code / Codex-style environments onto a small worker pool (see repo demos)
- **Stateful HTTP actors** — counter demo: increment state survives suspend/resume
- **Sandboxed shell actors** — Alpine sandbox demo with filesystem persistence
- **AX on Kubernetes** — production-oriented path documented by Agent Executor, implemented here
