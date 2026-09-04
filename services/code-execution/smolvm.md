# SmolVM

> **"SmolVM: secure microVM sandboxes for AI agents"**

| | |
|---|---|
| **Website** | https://docs.celesto.ai/smolvm |
| **Docs** | https://docs.celesto.ai/smolvm |
| **GitHub** | https://github.com/CelestoAI/SmolVM |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/CelestoAI/SmolVM?style=social)](https://github.com/CelestoAI/SmolVM) |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-09-03 ([repo metadata](https://api.github.com/repos/CelestoAI/SmolVM)); PyPI `smolvm`; docs index at [docs.celesto.ai/llms.txt](https://docs.celesto.ai/llms.txt) |
| **Verified at** | 2026-09-04 |

---

## Official Website

https://docs.celesto.ai/smolvm

Docs H1 (live 2026-09-04): **“SmolVM: secure microVM sandboxes for AI agents”**. Supporting line: “Introduction to SmolVM — an open-source microVM sandbox with sub-second boot, hardware isolation, and persistent state for running AI agents safely.”

---

## Official Repo

https://github.com/CelestoAI/SmolVM

README subtitle (live 2026-09-04): **“Secure, isolated computers that AI agents can use to browse, run code, and get real work done.”**

GitHub description: **“Open-source AI sandbox infrastructure with unified API for VMMs -- Firecracker, QEMU and libkrun.”**

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + Python SDK

```bash
curl -sSL https://celesto.ai/install.sh | bash
```

```python
from smolvm import SmolVM

with SmolVM() as vm:
    result = vm.run("echo 'Hello from the sandbox!'")
    print(result.stdout.strip())
```

CLI:

```bash
smolvm sandbox create --name my-sandbox
smolvm sandbox exec my-sandbox -- python --version
smolvm claude start    # coding-agent sandbox
smolvm browser start --live
```

Manual path: `pip install smolvm && smolvm setup && smolvm doctor`. There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

```bash
npx clawhub@latest search smolvm
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not yet published as a first-party MCP server.

The agent surface is the Python SDK (`smolvm`) and CLI (`smolvm sandbox`, `smolvm claude|codex|pi start`, `smolvm browser`). Framework examples wrap SmolVM as a tool for OpenAI Agents, LangChain, and PydanticAI.

| Detail | Value |
|---|---|
| **MCP Repo** | — |
| **Transport** | — |
| **Compatible Clients** | Any Python agent; CLI-driven coding agents (Claude Code, Codex, Pi, OpenCode) |

---

## What It Does

SmolVM gives AI agents a **disposable computer**: a hardware-isolated microVM that boots in hundreds of milliseconds, runs arbitrary code or a full browser, can mount host directories, snapshot/restore, and disappear when the task ends. One API covers Firecracker (Linux), QEMU (macOS), and libkrun.

Docs body (live): “SmolVM gives AI agents their own disposable computer. Each microVM boots in milliseconds, runs any code or software you throw at it, persists files and state across sessions, and disappears when you're done — built for scale in production.”

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [E2B](e2b.md) | Hosted cloud sandboxes. SmolVM is local/self-host multi-VMM |
| [CubeSandbox](cubesandbox.md) | E2B-compatible self-host *service* (cluster API). SmolVM is an SDK/CLI on the machine |
| [forkd](forkd.md) | Firecracker CoW fork/BRANCH fan-out. SmolVM is create/run/snapshot of a single disposable VM |
| [OpenSandbox](opensandbox.md) | K8s/runtime abstraction + MCP |
| [Clawk](clawk.md) | Local hypervisor VM for one coding agent on a desk (macOS). SmolVM is Linux+macOS+Windows guests with a unified SDK |

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs H1: **“SmolVM: secure microVM sandboxes for AI agents”** — [docs.celesto.ai/smolvm](https://docs.celesto.ai/smolvm). README: **“Secure, isolated computers that AI agents can use to browse, run code, and get real work done.”** |
| **Agent-specific primitive** | Disposable microVM; domain-allowlisted egress; in-sandbox browser (`cdp_url` / VNC); coding-agent launchers (`smolvm claude start`); snapshots |
| **Autonomy-compatible control plane** | After `smolvm setup`, agents create/run/stop VMs via SDK/CLI with no dashboard |
| **M2M integration surface** | `pip install smolvm`, `smolvm` CLI, framework tool wrappers (OpenAI Agents, LangChain, PydanticAI) |
| **Identity / delegation** | Per-VM isolation; optional `allowed_domains`; host mounts default read-only; no hosted KYA — C5 is local VM boundary + network policy |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Disposable microVM** | Firecracker / QEMU / libkrun behind one SDK |
| **Sub-second boot** | Docs: VMs ready in ~413 ms |
| **Browser sandbox** | CDP + live viewer + VNC for computer-use agents |
| **Network allowlist** | `internet_settings.allowed_domains` |
| **Host mounts** | Read-only by default; `--writable-mounts` opt-in |
| **Snapshots** | Save/restore memory, disk, and processes |
| **Coding-agent launchers** | `smolvm claude\|codex\|opencode\|pi start` |

---

## Autonomy Model

```
Operator runs install.sh / smolvm setup once
    -> Agent SmolVM() or smolvm sandbox create
    -> Agent vm.run(...) / browser / coding-agent CLI
    -> Output returns to the loop; snapshot optional
    -> vm.stop() or context-manager teardown
```

---

## Identity and Delegation Model

- **Sandbox identity:** one microVM per `SmolVM()` / named sandbox.
- **Network delegation:** domain allowlists constrain egress.
- **Filesystem delegation:** mounts are read-only unless the operator opts into writable mounts.
- **No multi-tenant SaaS identity** — local/self-host trust plus VM isolation.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Installer | `curl -sSL https://celesto.ai/install.sh \| bash` |
| Python SDK | `from smolvm import SmolVM` |
| CLI | `smolvm sandbox`, `smolvm browser`, `smolvm claude start` |
| Docs | https://docs.celesto.ai/smolvm · llms.txt index |
| License | Apache-2.0 |

---

## Human-in-the-Loop Support

Optional live browser viewer (`--live` / `viewer_url`) and macOS Screen Sharing desktop. Normal `vm.run()` and headless browser automation do not require a click.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **E2B / CubeSandbox** | Hosted or E2B-wire cluster services. SmolVM is a local multi-VMM SDK |
| **forkd** | Fan-out fork/BRANCH, not a general disposable-computer SDK with browser/coding-agent launchers |
| **Docker** | Shared kernel; no hardware-isolated guest + snapshot/browser primitives |
| **Generic QEMU/Firecracker** | No agent-oriented SDK, allowlists, or `smolvm claude start` |

---

## Use Cases

- **Untrusted generated code** — run it in a microVM, not on the host
- **Browser / computer-use agents** — CDP + VNC inside the sandbox
- **Coding agents off the laptop** — one command isolates Claude Code / Codex / Pi
- **Stateful multi-turn work** — reuse the same VM; snapshot and restore
