# Dormice

> **"The SQLite of agent sandboxes — a self-hosted sandbox platform for AI agents. One machine, sandboxes that live forever, idle costs nothing."**

| | |
|---|---|
| **Website** | https://github.com/BitMiracle-AI/Dormice |
| **Docs** | https://github.com/BitMiracle-AI/Dormice/blob/main/README.md |
| **GitHub** | https://github.com/BitMiracle-AI/Dormice |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/BitMiracle-AI/Dormice?style=social)](https://github.com/BitMiracle-AI/Dormice) |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **License** | Apache-2.0 |
| **Maturity** | ⚠️ Early development — official README: **"Nothing here is ready for production yet."** Same honesty bar as [Axern](axern.md) |
| **Latest-month signal** | Last GitHub push 2026-08-14 ([repo metadata](https://api.github.com/repos/BitMiracle-AI/Dormice)); `npx skills add BitMiracle-AI/Dormice` |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://github.com/BitMiracle-AI/Dormice

GitHub-only. Repo `homepage` is empty. After install the daemon serves a small web console on loopback port 3676 at `/console` (token → httpOnly session cookie).

---

## Official Repo

https://github.com/BitMiracle-AI/Dormice

---

## How to Use (Agent Onboarding)

**Interaction pattern:** self-hosted daemon + SDK / CLI / Agent Skill

One command on a bare Ubuntu/Debian x86_64 host (as root), from the [README](https://github.com/BitMiracle-AI/Dormice/blob/main/README.md):

```bash
curl -fsSL https://raw.githubusercontent.com/BitMiracle-AI/Dormice/main/deploy/install.sh | bash
```

Then install the official skill:

```bash
npx skills add BitMiracle-AI/Dormice
```

Native TypeScript client (`@dormice/sdk` — README: **not on npm yet**; `pnpm build` inside the repo produces it):

```ts
import { Dormice } from '@dormice/sdk';

const client = new Dormice({
  endpoint: 'http://127.0.0.1:3676',
  token: process.env.DORMICE_API_TOKEN!,
});

await client.acquireSandbox('my-agent', { policy: { stopAfterSeconds: null } });
const result = await client.execCommand('my-agent', 'python3 -c "print(6 * 7)"');
```

E2B SDK compatibility — official `e2b` package, two URL changes:

```ts
import { Sandbox } from 'e2b';

const sbx = await Sandbox.create({
  apiKey: `e2b_${process.env.DORMICE_API_TOKEN}`,
  apiUrl: 'http://127.0.0.1:3676/e2b/api',
  sandboxUrl: 'http://127.0.0.1:3676/e2b/envd',
});
```

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add BitMiracle-AI/Dormice
```

| Skill | What It Teaches the Agent |
|---|---|
| `dormice` | Connect, pick E2B SDK / native HTTP / `dor` CLI, run commands, move files, set lifecycle policy — [skills/dormice/SKILL.md](https://github.com/BitMiracle-AI/Dormice/blob/main/skills/dormice/SKILL.md) |

---

## MCP

**Status:** ⚠️ Not published as a dedicated MCP server.

| Detail | Value |
|---|---|
| **Primary interface** | HTTP RPC (`POST /acquireSandbox`, `POST /execCommand`, …), `@dormice/sdk`, `dor` CLI, official `e2b` SDK |
| **Compatible clients** | Any agent that can call HTTP RPC or the E2B SDK against the daemon |
| **Docs for agents** | Skill above; README says the docs build emits `/llms.txt` twins |

---

## What It Does

Dormice is a **self-hosted sandbox platform** that inverts billed-ephemeral cloud sandboxes. Official idea: you run one daemon on a machine you already pay for; sandboxes are **permanent** and get cheaper the longer they sit idle (`active → frozen → stopped → archived`). `acquireSandbox(userKey)` is idempotent — same key always returns the same sandbox.

Idle freeze is the headline: README claims freezing an idle 1 GiB sandbox down to ~5 MiB RSS and ~50 ms wake (measured on their hardware). Deploy shape: one daemon, one SQLite ledger, one port. Isolation is Docker + gVisor, not Firecracker.

**Early-dev warning (do not skip):** README status block: the daemon, lifecycle engine, SDK, CLI, console, Docker+gVisor executor, S3 archiver, and E2B-compatible API work end to end — **"Nothing here is ready for production yet."** Treat it as evaluation software, same honesty bar as [Axern](axern.md).

**Distinct from [E2B](e2b.md)** (billed ephemeral cloud): self-hosted, single-binary-shaped, permanent cheap-idle sandboxes, E2B SDK by changing two URLs. **Not** [Kubernetes SIG Agent Sandbox](kubernetes-agent-sandbox.md) and **not** hosted [Agent Sandbox](agent-sandbox.md) (`agentsandbox.co`).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: **"The SQLite of agent sandboxes — a self-hosted sandbox platform for AI agents."** Skill frontmatter: **"Dormice's users are agents"** — [repo](https://github.com/BitMiracle-AI/Dormice) |
| **Agent-specific primitive** | Idempotent `acquireSandbox(userKey)`; idle freeze/stop/archive; HTTP RPC verbs; resident-agent policy (`stopAfterSeconds: null`) |
| **Autonomy-compatible control plane** | After the daemon and token exist, an agent acquires, execs, and writes files without a console click. Console is secondary |
| **M2M integration surface** | HTTP RPC, `@dormice/sdk`, `dor` CLI, unmodified `e2b` SDK, Agent Skill |
| **Identity / delegation** | One API token (installer) plus revocable `dor apikey` keys. Sandbox **name** is the stable address. Console uses an httpOnly session cookie so the page never stores the token |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`acquireSandbox(userKey)`** | Idempotent: create / wake / start / restore the same sandbox |
| **Idle cooldown** | `active → frozen → stopped → archived`; acquire reverses it |
| **HTTP RPC** | `POST /acquireSandbox`, `/execCommand`, `/writeFiles`, … |
| **`@dormice/sdk`** | Native TypeScript client (first npm release queued per README) |
| **`dor` CLI** | `dor sandbox ls / exec / push / pull / rebuild / destroy`, `dor doctor` |
| **E2B compat** | `/e2b/api` + `/e2b/envd`; `metadata.name` maps to idempotent acquire |
| **S3 cold archive** | Optional last idle step; next acquire reports `{ status: 'restoring', progress }` |
| **`/console`** | Operator UI on `:3676/console` |

---

## Autonomy Model

```
Operator runs install.sh; dor doctor verifies Docker + gVisor
    -> Agent receives endpoint + DORMICE_API_TOKEN (or a minted API key)
    -> acquireSandbox('my-agent') creates or wakes the named sandbox
    -> execCommand / writeFiles without per-step human approval
    -> Idle policy freezes/stops/archives; next acquire restores
    -> destroySandbox is the only verb that loses disk data
```

---

## Identity and Delegation Model

- **Sandbox name = address:** Same key, same disk, whatever lifecycle state.
- **Token vs API keys:** Installer token can mint/revoke keys; keys cannot manage keys.
- **Loopback bind:** Daemon listens on `127.0.0.1` only. Exposure is an explicit SSH tunnel or reverse proxy.
- **No hosted tenant account:** Delegation is "this token on this machine," not a cloud KYA passport.
- **Threat-model honesty (upstream):** gVisor, not hardware virtualization; block cloud metadata; `"icc": false`. Wrong tool if you need Firecracker-class isolation or a multi-machine fleet.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Installer | `curl -fsSL https://raw.githubusercontent.com/BitMiracle-AI/Dormice/main/deploy/install.sh \| bash` |
| HTTP RPC | `http://127.0.0.1:3676/<verb>` + `Authorization: Bearer` |
| Native SDK | `@dormice/sdk` (build from repo until npm publish) |
| E2B SDK | Official `e2b` package against `/e2b/api` and `/e2b/envd` |
| CLI | `dor` |
| Agent Skill | `npx skills add BitMiracle-AI/Dormice` |
| Console | `http://127.0.0.1:3676/console` |

---

## Human-in-the-Loop Support

Install, `dor doctor`, network hardening, and optional reverse proxy are operator work. Runtime acquire/exec is API-driven. The console is a convenience UI, not required per command. Production use is **not** recommended by upstream yet.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **E2B (hosted)** | Billed-ephemeral cloud sandboxes. Dormice is self-hosted permanence + cheap idle |
| **Hosted Agent Sandbox (agentsandbox.co)** | Different hosted product + URL onboarding. Not this daemon |
| **Kubernetes SIG Agent Sandbox** | Cluster CRDs / warm pools. Dormice is one machine, one SQLite ledger |
| **Axern** | Different control plane (Principals, Axrun, gRPC). Not E2B-protocol compatible by two URLs |
| **Raw Docker socket** | No idempotent acquire, idle freeze ladder, or E2B wire compat |

---

## Use Cases

- **Resident coding agents** — one named sandbox that freezes instead of dying
- **E2B app migration** — point the official SDK at two local URLs
- **Cheap-idle eval harnesses** — keep many stopped sandboxes on one host
- **Self-hosted only** — no hosted SLA; that is E2B's product (official "wrong tool" list)
