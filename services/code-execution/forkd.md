# forkd

> **"A microVM sandbox runtime for AI agent fan-out."**

| | |
|---|---|
| **Website** | https://github.com/deeplethe/forkd |
| **Docs** | https://github.com/deeplethe/forkd/blob/dev/README.md |
| **GitHub** | https://github.com/deeplethe/forkd |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/deeplethe/forkd?style=social)](https://github.com/deeplethe/forkd) |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-09-02 ([repo metadata](https://api.github.com/repos/deeplethe/forkd)); default branch `dev`; release tarball `forkd-v0.5.3` |
| **Verified at** | 2026-09-04 |

---

## Official Website

https://github.com/deeplethe/forkd

GitHub-only. Repo `homepage` is empty in GitHub metadata.

---

## Official Repo

https://github.com/deeplethe/forkd

README H1 (live 2026-09-04): **“Fork 100 microVMs in 101 ms. BRANCH a live VM in 56 ms (v0.4 live mode).”**

README lead (catalog tagline): **“A microVM sandbox runtime for AI agent fan-out.”**

GitHub description: **“Fork() for AI agent microVMs. Spawn 100 children in ~100ms from a warm parent; BRANCH a live VM in ~150ms. KVM-isolated, snapshot CoW.”**

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + REST / SDK / MCP

x86_64 Linux with KVM (official README quick start):

```bash
curl -sSL https://github.com/deeplethe/forkd/releases/download/v0.5.3/forkd-v0.5.3-x86_64-linux.tar.gz \
  | sudo tar -xz -C /usr/local/bin/
sudo -E forkd quickstart
```

Language clients:

```bash
pip install forkd
npm install @deeplethe/forkd
pip install forkd-mcp
```

```python
from forkd import Controller
c = Controller()
parent = c.spawn_sandboxes("pyagent", n=1, live_fork=True)[0]
branch = c.branch_sandbox(parent["id"], mode="live", wait=False)
```

`forkd doctor` probes KVM, Firecracker, guest kernel, and the live-BRANCH (`uffd_wp`) path. There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

```bash
npx clawhub@latest search forkd
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — `forkd-mcp`

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/deeplethe/forkd/tree/dev/sdk/mcp |
| **Package** | `pip install forkd-mcp` |
| **Transport** | stdio (Claude Desktop / Claude Code / Cursor / Cline) |
| **Compatible Clients** | Claude Desktop, Claude Code, Cursor, Cline, any MCP client |
| **Recipe** | [`recipes/mcp-agent/`](https://github.com/deeplethe/forkd/tree/dev/recipes/mcp-agent) |

---

## What It Does

forkd is a **Firecracker copy-on-write sandbox runtime** for AI-agent fan-out. A parent microVM boots once, warms the runtime (imports, JIT, model weights), and is paused to disk. Each child is a separate Firecracker process that `mmap`s the parent with `MAP_PRIVATE`, so spawn cost is closer to `fork(2)` than to a cold-boot VM.

**BRANCH** pauses a *live* sandbox, snapshots in-flight state, and resumes so an agent can fork mid-thought — not only at warm-up. v0.4 live BRANCH advertises a 56 ms p50 pause window; v0.5 adds stacked diff-snapshot chains.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [E2B](e2b.md) | Hosted cold-start cloud VMs. forkd is self-host Firecracker **fork-from-warm** |
| [CubeSandbox](cubesandbox.md) | E2B-compatible self-host microVMs (pool / cold-start). forkd’s primitive is CoW fork + live BRANCH |
| [OpenSandbox](opensandbox.md) | Runtime abstraction over Docker/K8s/etc. |
| [SmolVM](smolvm.md) | Disposable agent computers (Firecracker/QEMU/libkrun). No fork/BRANCH fan-out primitive |
| [Dormice](dormice.md) | Cheap-idle E2B-compat daemon, not Firecracker CoW fork |

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README lead: **“A microVM sandbox runtime for AI agent fan-out.”** — [repo](https://github.com/deeplethe/forkd). Properties section: “Built for agent fan-out.” GitHub description: **“Fork() for AI agent microVMs…”** |
| **Agent-specific primitive** | `fork` N children from a warmed parent; **BRANCH** a live VM mid-thought; stacked snapshot chains; per-child KVM + netns |
| **Autonomy-compatible control plane** | After `quickstart` / daemon up, agents call REST, Python/TS SDK, or MCP with no UI |
| **M2M integration surface** | REST `POST /v1/sandboxes`, `forkd` CLI, `pip install forkd`, `@deeplethe/forkd`, `forkd-mcp` |
| **Identity / delegation** | Per-child Firecracker process, netns, cgroup v2 limit; REST bearer token; append-only JSON audit log; Prometheus `/metrics` |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **fork-from-warm** | Spawn N KVM-isolated children from a paused parent snapshot |
| **BRANCH** | Snapshot a *running* agent VM and resume (~56 ms live pause in v0.4) |
| **Diff-snapshot chains** | Stack `pip install` layers; spawn walks `parent_tag` edges |
| **Per-child isolation** | Own Firecracker + netns + cgroup + re-seeded `/dev/urandom` |
| **E2B-shaped Python client** | `from forkd import Sandbox` as a drop-in style vs `from e2b import Sandbox` |

---

## Autonomy Model

```
Operator runs forkd quickstart (KVM host) and bakes a warmed parent snapshot
    -> Agent POST /v1/sandboxes n=N (or SDK spawn / MCP)
    -> Children inherit CoW memory; each runs isolated
    -> Agent BRANCH mid-thought to fan out hypotheses
    -> Results return over REST; audit log records the cohort
```

---

## Identity and Delegation Model

- **Child identity:** one Firecracker process + netns + cgroup per sandbox ID.
- **Caller auth:** REST bearer token on the daemon (Unix or TCP).
- **Audit:** append-only JSON log and Prometheus metrics attributable to sandbox IDs.
- **No hosted KYA token** — C5 is local daemon credentials + KVM isolation.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `forkd quickstart`, `fork`, `snapshot`, `doctor` |
| REST | `/v1/sandboxes`, live BRANCH `mode: "live"` |
| Python SDK | `pip install forkd` |
| TypeScript SDK | `npm install @deeplethe/forkd` |
| MCP | `pip install forkd-mcp` |
| License | Apache-2.0 |

---

## Human-in-the-Loop Support

None on the data path. `quickstart` asks consent before host setup unless `--yes`. Humans inspect benches and the audit log after the fact.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **E2B / CubeSandbox** | Cold-start or pooled microVMs. forkd’s design point is CoW fork + live BRANCH |
| **SmolVM / OpenSandbox** | Disposable VM SDK or runtime abstraction — no fork(2)-shaped fan-out |
| **Docker / gVisor** | Shared-kernel or userspace isolation; README benches them as slower fan-out |
| **`os.fork()` in-process** | No KVM boundary; unsafe for untrusted agent code |

---

## Use Cases

- **Code-interpreter fan-out** — one warmed SciPy/torch parent, fork-per-turn
- **Mid-thought BRANCH** — LangGraph ReAct demo forks grandchildren with different hints
- **Parallel evals** — N isolated `pytest` children from one checkout snapshot
- **Untrusted CI** — `git clone + pip install + pytest` inside a real Linux microVM
