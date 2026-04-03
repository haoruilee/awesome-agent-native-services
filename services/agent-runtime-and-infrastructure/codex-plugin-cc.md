# Codex plugin for Claude Code (codex-plugin-cc)

> **"Use Codex from inside Claude Code for code reviews or to delegate tasks to Codex."**

| | |
|---|---|
| **Website** | https://github.com/openai/codex-plugin-cc |
| **Docs** | https://github.com/openai/codex-plugin-cc/blob/main/README.md |
| **GitHub** | https://github.com/openai/codex-plugin-cc |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **Upstream** | [Codex](https://developers.openai.com/codex/) · [Codex app server](https://developers.openai.com/codex/app-server) |

---

## Official Website

https://github.com/openai/codex-plugin-cc

---

## Official Repo

https://github.com/openai/codex-plugin-cc

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Extension / Plugin` (Claude Code marketplace plugin wrapping local Codex CLI + app server)

```bash
# In Claude Code: add marketplace and install plugin (see repo README)
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup

# Optional: ensure Codex CLI is installed and signed in
npm install -g @openai/codex
# then from Claude Code: !codex login

# Typical delegation flow
/codex:review --background
/codex:status
/codex:result

# Delegate a fix or investigation to Codex (subagent)
/codex:rescue investigate why the tests started failing
```

Full command reference: [README](https://github.com/openai/codex-plugin-cc/blob/main/README.md).

---

## Agent Skills

**Status:** ⚠️ Not yet published as a standalone `SKILL.md` install via `npx skills add`

The plugin ships slash commands and a `codex:codex-rescue` subagent inside Claude Code; onboarding is via the marketplace install flow above.

Search community skills: `npx clawhub@latest search codex`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not applicable — this is a Claude Code plugin that drives the local [Codex CLI](https://developers.openai.com/codex/cli/) and [Codex app server](https://developers.openai.com/codex/app-server). It is not itself an MCP server.

---

## What It Does

The **Codex plugin for Claude Code** lets a Claude Code session **invoke OpenAI Codex** for read-only reviews, adversarial design review, and **delegated rescue work** (investigate, patch, resume threads) without leaving the Claude Code workflow. It exposes slash commands (`/codex:review`, `/codex:adversarial-review`, `/codex:rescue`, `/codex:status`, `/codex:result`, `/codex:cancel`, `/codex:setup`) and registers a **Codex subagent** for handoffs.

Background jobs integrate with **status/result/cancel** so an orchestrating agent can run long Codex tasks asynchronously. An optional **review gate** (`/codex:setup --enable-review-gate`) hooks Claude’s stop flow to a targeted Codex review before completion.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | *"Use Codex from inside Claude Code for code reviews or to delegate tasks to Codex"* — README positions the plugin for **Claude Code users** orchestrating **Codex** as a delegated coding agent — [README](https://github.com/openai/codex-plugin-cc/blob/main/README.md) |
| **Agent-specific primitive** | Slash-command **orchestration of another coding agent** (`/codex:rescue`, background jobs, `codex:codex-rescue` subagent, session resume via `/codex:result` + `codex resume`); optional **Stop-hook review gate** that blocks Claude until Codex review passes — not a generic REST CRUD surface |
| **Autonomy-compatible control plane** | `--background` jobs, `--wait`, `--cancel`, `--resume` / `--fresh` for rescue threads; full review/fix loops without manual UI steps inside Claude Code |
| **M2M integration surface** | Claude Code **plugin manifest + slash commands**; wraps **Codex CLI** and **Codex app server** (same machine, same repo checkout) — [Codex integration](https://github.com/openai/codex-plugin-cc/blob/main/README.md#codex-integration) |
| **Identity / delegation** | Uses **local Codex authentication** (ChatGPT or API key per user); **job IDs** and **Codex session IDs** (`/codex:status`, `/codex:result`) separate delegated runs; actions run under the user’s Codex credentials on the workstation with **git-visible** outcomes |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`/codex:review`** | Read-only Codex review of working tree or branch (`--base`); `--background` / `--wait` |
| **`/codex:adversarial-review`** | Steerable challenge review with optional focus text |
| **`/codex:rescue`** | Delegate investigate/fix/continue work via `codex:codex-rescue` subagent; `--model`, `--effort`, `--resume`, `--fresh` |
| **`/codex:status`** | Running and recent Codex jobs for the current repository |
| **`/codex:result`** | Final output for a finished job; includes Codex session ID when available |
| **`/codex:cancel`** | Cancel an active background job |
| **`/codex:setup`** | Codex install/auth check; optional **review gate** enable/disable |
| **Review gate** | Stop hook runs targeted Codex review before Claude can finish (optional; usage-intensive) |

---

## Autonomy Model

```
Claude Code session loads codex-plugin-cc from marketplace
    ↓
/codex:setup verifies Codex CLI + auth (or prompts install/login)
    ↓
Orchestrator invokes /codex:review, /codex:adversarial-review, or /codex:rescue
    ↓
Plugin calls local Codex via app server / CLI on same repo
    ↓
Background: /codex:status → /codex:result (or /codex:cancel)
    ↓
Optional: human or agent continues in native Codex via codex resume <session>
```

---

## Identity and Delegation Model

- **Credentials:** Local **Codex** sign-in (ChatGPT subscription or OpenAI API key) — shared with standalone Codex; not a separate cloud “Claude” identity.
- **Work isolation:** Jobs and sessions are **repository-scoped** in the plugin UX; Codex session IDs tie outputs to a specific delegated run.
- **Attribution:** Changes land in the **local git working tree** under the developer’s environment; Codex session IDs support **audit and resume** in Codex.
- **Orchestration boundary:** **Claude Code** (orchestrator) vs **Codex** (delegated coding agent) is explicit in commands and subagent naming.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Claude Code plugin | Marketplace: `openai/codex-plugin-cc` — package `codex@openai-codex` |
| Slash commands | `/codex:*` as documented in repo README |
| Codex CLI | Global `codex` binary — `config.toml` / `.codex/config.toml` per [Codex config](https://developers.openai.com/codex/config-basic) |
| Codex app server | Used by the plugin for Codex integration — [app server docs](https://developers.openai.com/codex/app-server) |

---

## Human-in-the-Loop Support

Optional **review gate** blocks Claude’s stop until Codex review is clean — explicit human-in-the-loop style **gating** when enabled. Day-to-day use can be fully autonomous inside Claude Code subject to Codex **approval settings** and org policies. Requires **active monitoring** when review gate is on — see README warnings.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Run Codex and Claude Code separately** | No **first-class delegation**, job lifecycle (`status`/`result`/`cancel`), or **subagent** bridge between the two runtimes |
| **Generic shell scripts** | No **Stop-hook review gate**, no **marketplace-distributed** Claude Code integration, no **structured job IDs** tied to Codex sessions |
| **IDE-only Codex** | Human-centric UI; not the same as **agent-orchestrated** slash commands and background job control from Claude Code |

---

## Use Cases

- **Second-opinion code review** — Claude ships a change; Codex reviews the branch or diff read-only before merge
- **Adversarial design review** — Pressure-test caching, auth, concurrency, or rollback assumptions before release
- **Delegate heavy fixes** — Hand off flaky-test or CI investigations to Codex while Claude continues planning
- **Long-running Codex work** — `--background` plus `status`/`result` for async agent workflows
- **Cross-tool continuity** — Resume delegated work in native Codex via `codex resume` using session IDs from `/codex:result`
