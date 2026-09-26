# Clawk

> **"Give a coding agent its own disposable Linux machine, not yours."**

| | |
|---|---|
| **Website** | https://github.com/clawkwork/clawk |
| **Docs** | https://github.com/clawkwork/clawk/tree/main/docs |
| **GitHub** | https://github.com/clawkwork/clawk |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/clawkwork/clawk?style=social)](https://github.com/clawkwork/clawk) |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **License** | Apache-2.0 |
| **Maturity** | ⚠️ Pre-1.0 — official README: expect breaking changes ([Status](https://github.com/clawkwork/clawk/blob/main/README.md#status)) |
| **Latest-month signal** | Last GitHub push 2026-08-13 ([repo metadata](https://api.github.com/repos/clawkwork/clawk)); Homebrew tap `clawkwork/tap/clawk` |
| **Verified at** | 2026-08-27 |

---

## Official Website

https://github.com/clawkwork/clawk

GitHub-only. The repository does not publish a separate product homepage (`homepage` is empty in GitHub repo metadata).

---

## Official Repo

https://github.com/clawkwork/clawk

GitHub description: **"Give coding agents a disposable Linux VM, not your laptop."** README lead: *Give a coding agent its own disposable Linux machine, not yours.*

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` (local hypervisor VM)

Requires **macOS 14+ on Apple silicon** ([README](https://github.com/clawkwork/clawk#install)). No Windows.

```bash
brew install clawkwork/tap/clawk
cd <repo>
clawk                      # boot a sandbox for this dir + attach Claude Code
```

From-source alternative: `git clone https://github.com/clawkwork/clawk && make install` (Go 1.26+). No Docker daemon, qemu, or sudo — the hypervisor is Virtualization.framework (macOS) or Firecracker (Linux). Linux via Firecracker is official but **experimental** ([linux-quickstart](https://github.com/clawkwork/clawk/blob/main/docs/linux-quickstart.md)).

Structured control plane after first boot:

```bash
clawk run shell
clawk run codex
clawk status --json
clawk up / down
clawk snapshot
clawk destroy
```

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` / `SKILL.md` package published.

`clawk.mod` can seed skills and MCP servers **inside** the guest. That is guest configuration, not a published Agent Skills package.

```bash
npx clawhub@latest search clawk
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not a hosted MCP server. Clawk can *provision* MCP servers in the guest via `clawk.mod`.

| Detail | Value |
|---|---|
| **Primary interface** | `clawk` CLI (`status --json`, up/down/snapshot/destroy, `run <agent>`) |
| **Guest MCP** | Documented in [docs/mcp.md](https://github.com/clawkwork/clawk/blob/main/docs/mcp.md) — credentials stay off the guest disk |
| **Compatible clients** | Claude Code, Codex, pi, OpenCode, or a shell attached inside the VM |

---

## What It Does

Clawk gives a coding agent a **disposable Linux VM** on the operator's desk instead of the host laptop. `cd` into a repo and run `clawk`: the project is live-mounted, the agent runs as root in the guest with permission-bypass flags, and host files, keychain, and unlisted network destinations stay out of reach.

Isolation is a **hypervisor** (Apple Virtualization.framework / Firecracker), not a process sandbox. Egress is deny-by-default and **DNS-aware** — the userspace stack in the per-sandbox daemon filters TCP/UDP/ICMP; the guest cannot reconfigure it. Idle VMs balloon memory and can suspend; `clawk destroy` drops the VM disk while repo and agent conversation state stay on the host.

**Pre-1.0:** README IMPORTANT callout and Status section both say the project is pre-1.0, moving fast, and will break between releases.

**Distinct from** hosted [Agent Sandbox](agent-sandbox.md) (`agentsandbox.co`), [Kubernetes SIG Agent Sandbox](kubernetes-agent-sandbox.md), E2B / Runloop / Vercel Sandbox (cloud microVMs), and [CodeRunner](coderunner.md) (Apple Containers). Clawk is local-first hypervisor VMs with a DNS-aware egress allow-list.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: **"Give a coding agent its own disposable Linux machine, not yours."** and **"The agent gets its own machine instead of yours."** — [repo](https://github.com/clawkwork/clawk) |
| **Agent-specific primitive** | Per-project disposable Linux VM; runners start in externally-sandboxed modes (`--dangerously-skip-permissions` / Codex bypass / OpenCode `--auto`); DNS-aware egress allow-list; ticket worktrees |
| **Autonomy-compatible control plane** | After `clawk`, the agent works without per-command host approvals. `--safe` is the opt-out that restores prompts. Honest C4: the **daily path is a human launching `clawk`** — same pattern as catalog [CodeRunner](coderunner.md). The structured CLI (`status --json`, `up`/`down`/`snapshot`/`destroy`) is the machine control plane |
| **M2M integration surface** | `clawk` CLI with JSON status; `clawk.mod` templates; no hosted REST API |
| **Identity / delegation** | Each sandbox is a separate VM + allow-list. Host ssh-agent is forwarded (signing stays on the host). Claude token via `clawk auth set-token`. Audit of blocked destinations: `clawk network denials` |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Disposable Linux VM** | Virtualization.framework (macOS) or Firecracker (Linux, experimental) |
| **`clawk` / `clawk run`** | Attach Claude, Codex, pi, OpenCode, or a shell |
| **DNS-aware egress allow-list** | Default deny; hostname-based; denials logged |
| **`clawk status --json`** | Scriptable state, forwards, blocked hosts |
| **Snapshot / pause / destroy** | Hibernate RAM to disk, or drop the VM; host-side agent state persists |
| **`clawk.mod`** | Optional go.mod-style template: image, network, forwards, env, MCP, hooks |
| **Ticket mode** | `clawk work TICKET` — worktree per repo; `clawk pr` opens linked PRs |
| **Port forwards** | Guest → localhost and reverse host → guest |

---

## Autonomy Model

```
Operator installs Clawk and runs `clawk` in a repo (human daily path)
    -> Per-sandbox daemon boots the VM and attaches the agent
    -> Agent runs with host permission prompts bypassed; VM + allow-list contain it
    -> CLI (`status --json`, up/down/snapshot/destroy) manages lifecycle without a dashboard
    -> `clawk destroy && clawk` recreates a wrecked VM; conversations stay on the host
```

`--safe` restores the agent's own confirmation prompts for that attach.

---

## Identity and Delegation Model

- **Sandbox identity:** One VM per project or ticket name; agent home dirs are host-mounted under `~/.clawk/namespaces/…/state/`.
- **Credentials:** ssh-agent proxy keeps private keys off the guest; `clawk auth set-token` injects a Claude token so sandboxes do not share `/login`.
- **Network policy:** Allow-list is the delegation of which hosts the agent may reach. `clawk network denials` is the audit log of blocked destinations.
- **Limits (official):** Whatever you mount or allow is exposed; forwarded secrets are readable; hypervisor escapes are out of scope ([SECURITY.md](https://github.com/clawkwork/clawk/blob/main/SECURITY.md)).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `brew install clawkwork/tap/clawk` then `clawk`, `run`, `status --json`, `up`/`down`/`snapshot`/`destroy` |
| Config | Optional `clawk.mod` |
| Docs | https://github.com/clawkwork/clawk/tree/main/docs |
| MCP | Guest-side servers via `clawk.mod`; not a Clawk-hosted MCP package |

---

## Human-in-the-Loop Support

The everyday entry is a human typing `clawk`. After attach, the default is full autonomy inside the VM. `--safe` brings back runner confirmation prompts. Operators review egress denials, add allow-list entries, and treat sandbox output like an untrusted PR (official security model).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Hosted Agent Sandbox (agentsandbox.co)** | Different product: hosted sessions + `skill.md`. Not a local hypervisor |
| **Kubernetes SIG Agent Sandbox** | In-cluster CRDs. Not a laptop VM workflow |
| **E2B / Runloop / Vercel Sandbox** | Billed cloud microVMs. Clawk is local-first; code stays on the desk |
| **CodeRunner** | Apple Containers on the host kernel. Clawk is a separate Linux VM + DNS-aware egress filter |
| **Lima / generic VMs** | A Linux VM without per-project agent attach, default-deny egress, or ticket worktrees |
| **OS-level agent sandboxes** | Process policy on the real machine. One mistake exposes the keychain |

---

## Use Cases

- **Local autonomous coding** — let Claude/Codex install packages and run servers without `--dangerously-skip-permissions` on the host
- **Untrusted builds** — break the VM, `clawk destroy && clawk`, keep the repo
- **Multi-repo tickets** — `clawk work INFRA-123` then `clawk pr`
- **Egress-constrained agents** — default-deny network with a denial log
