# Axern

> **"Axern is an open-source sandbox platform for AI agents."**

| | |
|---|---|
| **Website** | https://axern.cofy-x.space |
| **Docs** | https://axern.cofy-x.space/getting-started/ |
| **GitHub** | https://github.com/cofy-x/axern |
| **Latest-month signal** | [v0.11.4](https://github.com/cofy-x/axern/releases/tag/v0.11.4) released 2026-09-24; 66 stars on 2026-09-26 (the 2026-08-13 snapshot recorded 232); license Apache-2.0; [axern.cofy-x.space](https://axern.cofy-x.space) returned HTTP 200 ([repo metadata](https://api.github.com/repos/cofy-x/axern)) |
| **Verified at** | 2026-09-26 |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **License** | Apache-2.0 |
| **Maturity** | ⚠️ Pre-1.0, active development, and explicitly recommended upstream for evaluation/contribution—not unreviewed multi-tenant production ([status](https://github.com/cofy-x/axern/blob/main/README.md#axern)) |

---

## Official Website

https://axern.cofy-x.space

---

## Official Repo

https://github.com/cofy-x/axern

---

## How to Use (Agent Onboarding)

**Interaction pattern:** self-hosted control plane + CLI / SDK

The quickest supported local path installs the CLI, starts the complete Docker Compose stack, and executes an isolated workload:

```bash
brew install cofy-x/tap/axern
axern local up
axern run python:3.12-slim -- python -c 'print("hello from axern")'
axern run list
```

Without Homebrew, use the upstream checksummed installer:

```bash
curl -fsSL https://raw.githubusercontent.com/cofy-x/axern/main/install.sh | sh
```

Agents and orchestration code can then pin the release-matched [Python, Go, or TypeScript SDK](https://axern.cofy-x.space/sdk/). See the official [Local Quickstart](https://github.com/cofy-x/axern/blob/main/README.md#local-quickstart).

---

## Agent Skills

**Status:** ⚠️ Not yet published — Axern documents agent workflows and ships an Axrun harness, but no standalone `SKILL.md` package is published.

```bash
npx clawhub@latest search axern sandbox
```

For faster access in China, use `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or pass `--registry https://cn.clawhub-mirror.com`.

See https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not published — the verified agent-facing surfaces are CLI, SDKs, and Axern's gRPC/HTTP data plane.

| Detail | Value |
|---|---|
| **MCP server** | No official MCP endpoint or package documented in the README as of 2026-09-26 |
| **Primary integration** | `axern` CLI; Go, Python, and TypeScript SDKs |
| **Agent harness** | `axrun` for immutable tasks, rollouts, verification, trajectories, usage, and typed artifacts |

---

## What It Does

Axern is a self-hosted execution control plane built around agent sandboxes. It runs untrusted, agent-generated code behind the `runsc` boundary and trusted long-lived services through `runc`, while exposing the same lifecycle model for environments, processes, files, archives, storage, services, functions, tunnels, terminals, and computer use.

Its durable control plane stores intent, placement, leases, retries, health, cleanup, quota, and storage state in PostgreSQL. Axrun adds reproducible agent tasks: immutable TaskSets and rollout plans, leased workers, resource and budget admission, verifier/oracle phases, trajectories, usage, and content-addressed evidence.

**Production warning:** upstream explicitly says Axern is pre-1.0 and suitable for evaluation/contribution. The bundled PostgreSQL, MinIO, single-node settings, and generated local credentials are development defaults. Before any shared or multi-tenant deployment, operators must harden authentication, TLS, network policy, runtime isolation, image trust, secrets, quotas, and persistent storage. Upstream also does not publish a sub-second cold-start guarantee; benchmark the chosen topology for interactive agent workloads.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The README opens: *"Axern is an open-source sandbox platform for AI agents"* and says it isolates untrusted agent-generated code — [source](https://github.com/cofy-x/axern/blob/main/README.md#axern) |
| **Agent-specific primitive** | Axrun owns immutable agent TaskSets, rollout plans, verifier/oracle materialization, trajectories, usage, and typed evidence on top of per-agent sandbox/workspace lifecycle ([Axrun architecture](https://github.com/cofy-x/axern/blob/main/apps/axrun/docs/architecture.md)) |
| **Autonomy-compatible control plane** | Agents can create and execute workloads through CLI/SDK; durable intent, placement, leases, retries, health, cleanup, quotas, and storage reconciliation survive client/node restarts; `rollout run --detach` supports accepted unattended execution ([README](https://github.com/cofy-x/axern/blob/main/README.md#why-axern), [Axrun usage](https://github.com/cofy-x/axern/blob/main/apps/axrun/docs/usage.md#managed-rollouts)) |
| **M2M integration surface** | Release-matched Python, Go, and TypeScript SDKs expose sandbox lifecycle, execution, processes, files, archives, tunnels, metadata, and typed errors; CLI and public gRPC/HTTP/SSH-compatible data-plane surfaces expose the same model ([SDKs](https://github.com/cofy-x/axern/blob/main/apps/docs/src/content/docs/sdk/index.md)) |
| **Identity / delegation** | Every verified client certificate maps to a durable Principal; namespace-scoped viewer/editor/admin roles authorize calls; managed Axrun workers have dedicated service identities further restricted by short-lived work leases; control-plane audit/evidence records retain attribution ([authorization](https://github.com/cofy-x/axern/blob/main/apps/docs/src/content/docs/guides/authorization.md)) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Sandbox / Run** | Create an isolated execution environment from an OCI image, execute commands, stream output, and tear it down |
| **Process and terminal** | Attached process streams and SSH-compatible interactive access |
| **Files and archives** | Read/write files and transfer bounded workspace archives through the public data plane |
| **Environment** | Reusable source/config boundary that a sandbox can select or continue |
| **Service / Function** | Long-lived trusted workloads and packaged invocations under the same lifecycle model |
| **Volume / Storage claim** | Persistent project data and topology-aware storage lifecycle |
| **Tunnel** | Explicit reverse TCP tunnel into a sandbox-local service |
| **Agent workspace** | Persistent Service + Volume + per-connection Tunnel for Codex or Claude Code; provider token remains local |
| **Axrun TaskSet / Rollout** | Immutable tasks, frozen agent/model plan, selection, attempts, concurrency, resource limits, timeouts, and capabilities |
| **Evidence artifact** | Verified trajectories, execution facts, usage, results, and content-addressed artifacts tied to a rollout generation |

---

## Autonomy Model

```text
Operator deploys Axern and grants an agent Principal a namespace role
    ↓
Agent/worker creates a sandbox, workspace, or immutable Axrun rollout
    ↓
Control plane validates source, quota, budget, identity, and resource intent
    ↓
Leased node/worker starts runsc or runc workload and streams machine-readable state
    ↓
Agent executes processes, exchanges files, and observes lifecycle without per-step clicks
    ↓
Verifier captures terminal facts, trajectories, usage, and typed artifacts
    ↓
Control plane reconciles completion, cleanup, storage, and retry eligibility
```

---

## Identity and Delegation Model

- **Durable Principals** — A verified mTLS client certificate maps to a control-plane Principal; the client private key is never uploaded.
- **Scoped delegation** — `namespace_viewer`, `namespace_editor`, and `namespace_admin` apply to exactly one namespace; `platform_admin` is reserved for platform operations.
- **Agent service identity** — Managed Axrun workers use a dedicated identity that cannot edit user namespaces merely by holding its certificate.
- **Lease fencing** — Short-lived renewable work leases and execution generations constrain each worker mutation to the assigned rollout work.
- **Credential separation** — Interactive Codex/Claude workspaces keep the provider credential on the local machine and send only a session-scoped adapter token to the remote runtime.
- **Audit/evidence** — PostgreSQL keeps rollout lifecycle/events and usage reservations; terminal episode facts, trajectories, and content-addressed artifacts bind evidence to allocation and generation identities.

---

## Protocol Surface

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

## Human-in-the-Loop Support

Normal sandbox lifecycle and an accepted Axrun rollout execute unattended. Operators can separate `rollout plan` from `rollout start` for an explicit review point, inspect frozen plans and immutable task digests, cancel or retry eligible runs, and compare evidence. Platform and namespace administrators grant identities, roles, quotas, and policy boundaries. Axern does not require a human click for each command inside a sandbox.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw Docker socket** | Gives an agent a dangerous host-level control surface without per-agent Principals, namespace roles, durable leases, evidence, or managed cleanup |
| **Generic Kubernetes Job** | Requires the agent application to build process/file streaming, workspace lifecycle, tunnel access, retries, task verification, and artifact contracts itself |
| **Remote SSH host** | Provides a human shell, not an isolated per-run lifecycle with typed state, resource admission, immutable task inputs, and machine-readable evidence |

---

## Use Cases

- **Untrusted code execution** — Run LLM-generated Python, shell, or build commands behind a `runsc` isolation boundary
- **Persistent coding agents** — Give Codex or Claude Code a resumable workspace while keeping provider credentials on the client machine
- **Agent evaluation rollouts** — Execute immutable TaskSets across models/agents and compare verifier, reward, cost, and trajectory evidence
- **Durable agent-created services** — Promote trusted workloads to long-running `runc` services with health, replicas, storage, and rollout state
- **Self-hosted sandbox infrastructure** — Keep execution, storage, identity, and audit planes inside an operator-controlled cluster
