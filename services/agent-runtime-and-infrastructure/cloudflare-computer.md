# Cloudflare Computer

> **"Give your agent a computer 👾"**

| | |
|---|---|
| **Website** | https://github.com/cloudflare/computer |
| **Docs** | https://github.com/cloudflare/computer/tree/main/docs |
| **GitHub** | https://github.com/cloudflare/computer |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/cloudflare/computer?style=social)](https://github.com/cloudflare/computer) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | npm `@cloudflare/computer` 0.3.1 released 2026-09-18; README still marks the package **PREVIEW ONLY**; last GitHub push 2026-09-29; 9,325 stars; MIT; [`examples/mcp`](https://github.com/cloudflare/computer/tree/main/examples/mcp) still present (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

No separate marketing site. The official home is the repository:

https://github.com/cloudflare/computer

---

## Official Repo

https://github.com/cloudflare/computer

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK` (Durable Object workspace)

```bash
npm install @cloudflare/computer
```

Then attach `withWorkspace` to a Durable Object and call `workspace.fs` / `workspace.runtime.exec()`. The package README is the install and API map. Workers need `nodejs_compat`; isolate backends also need the `experimental` flag and a Worker Loader binding.

An MCP example lives at `examples/mcp` in the repo (Code Mode `code` tool on a durable workspace). Repo `AGENTS.md` and `.agents/skills/` are for contributors working in this repository, not a published product Skill.

**Honesty:** Official README marks the package **PREVIEW ONLY** — unstable APIs, not suitable for production.

---

## Agent Skills

**Status:** ⚠️ Not published for product consumers

In-repo `.agents/skills/` and `AGENTS.md` target collaborators on `cloudflare/computer`, not `npx skills add` for an external agent.

Search community skills: `npx clawhub@latest search cloudflare-computer`. See: https://agentskills.io/specification

---

## MCP

**Status:** ⚠️ Example only

| Detail | Value |
|---|---|
| **MCP Repo** | Example at https://github.com/cloudflare/computer/tree/main/examples/mcp |
| **Transport** | Example wiring (Code Mode `code` tool + workspace); not a published npm MCP package |
| **Compatible Clients** | Whatever host you wire to the example |

---

## What It Does

Cloudflare Computer is a Durable Object virtual filesystem (SQLite-backed) with one execution entry point, `workspace.runtime.exec`. Backends today are a full Linux container (FUSE + `computerd`), an isolate shell ([just-bash](https://github.com/vercel-labs/just-bash)), and isolate JavaScript. Agents get a small durable working directory plus optional AI SDK tools (`read`, `ls`, `grep`, `write`, `edit`, `exec`).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | GitHub description: **"Give your agent a computer 👾"**. Package README: **"Built for agents that need a small, portable working directory"** — [repo](https://github.com/cloudflare/computer), [package](https://github.com/cloudflare/computer/blob/main/packages/computer/README.md) |
| **Agent-specific primitive** | Durable workspace FS + pluggable `runtime.exec` (container / isolate shell / isolate JS) aimed at agent-scale workspaces, not a general PaaS disk |
| **Autonomy-compatible control plane** | Once the Worker is deployed, the agent/runtime can read, write, and exec without a human desktop |
| **M2M integration surface** | `@cloudflare/computer` API, capnweb RPC to `computerd`, example MCP, example HTTP `write`/`read`/`exec` |
| **Identity / delegation** | Workspace state is the Durable Object's SQLite. Callers address a DO id (example uses `idFromName`). Egress policies can be none/all/custom. No separate KYA token |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Workspace filesystem** | `node:fs/promises`-like API durable across DO restarts |
| **`runtime.exec`** | One entry point; backend chooses shell vs JS module |
| **Container backend** | Full Linux userland via FUSE + `computerd` |
| **Isolate backends** | In-Worker just-bash or fresh Dynamic Worker JS |
| **Agent tool helpers** | Optional AI SDK tools over the same workspace |

---

## Autonomy Model

```
Developer installs @cloudflare/computer on a Worker
    -> Durable Object constructed with withWorkspace
    -> agent or Worker code writes files and calls runtime.exec
    -> selected backend runs against the same SQLite-backed FS
    -> optional example MCP exposes a code tool on that workspace
```

Preview APIs may change; do not treat this as a production SLA.

---

## Identity and Delegation Model

- **Workspace identity:** The Durable Object instance is the store.
- **Backend IDs:** Multiple runtimes can register under stable IDs.
- **Egress:** Examples show `none`, `all`, or custom URL policy.
- **No delegated user OAuth:** This is compute/filesystem, not a user-token broker.
- **Preview boundary:** Official text says not for production.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| npm | `@cloudflare/computer` |
| FS / runtime API | `workspace.fs`, `workspace.runtime.exec` |
| RPC | capnweb between DO and `computerd` |
| Examples | container, worker-shell, worker-javascript, egress, mcp, think |

---

## Human-in-the-Loop Support

None as a product gate. Humans deploy the Worker. Example UIs (`think-compare-runtimes`) are optional operator views.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Ordinary Worker KV / R2 only** | Object storage without an agent workspace exec surface |
| **Generic Docker host** | Not a Durable Object-authoritative FS with isolate/container backends on one API |
| **Cloudflare Agents SDK alone** | Related runtime; Computer is the filesystem-plus-exec package (see also [Cloudflare Agents SDK](cloudflare-agents-sdk.md)) |

---

## Use Cases

- **Agent working directory** — durable notes, artifacts, and commands on a DO
- **Compare runtimes** — same task on container vs Worker shell
- **Code Mode** — one `code` tool backed by the workspace (example)
- **Prototypes only** — official preview warning still applies
