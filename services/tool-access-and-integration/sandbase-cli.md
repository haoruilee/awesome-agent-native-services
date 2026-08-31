# SandBase CLI

> **"Give your AI agent superpowers. One command. 2,000+ AI models."**

| | |
|---|---|
| **Website** | https://www.sandbase.ai |
| **Docs** | https://github.com/sandbaseai/cli#readme |
| **GitHub** | https://github.com/sandbaseai/cli |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/sandbaseai/cli?style=social)](https://github.com/sandbaseai/cli) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Last GitHub push 2026-08-23; immutable [`v0.1.17`](https://github.com/sandbaseai/cli/releases/tag/v0.1.17) published 2026-08-19 |
| **Verified at** | 2026-08-25 |

This entry catalogs **SandBase CLI** — the local MCP bridge and published Agent Skill — not the broader SandBase store, harness, or skills org. Issue [#103](https://github.com/haoruilee/awesome-agent-native-services/issues/103) was submitted by an authorized promoter.

---

## Official Website

https://www.sandbase.ai

The homepage is a broader builder/FDE platform ("Agent-native delivery platform for builders and FDEs") with a Store, Setup, API, and Build Agent product. This catalog lists only the CLI.

---

## Official Repo

https://github.com/sandbaseai/cli

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `local MCP bridge` (stdio) after one browser approval

The official repo's current canonical install is the immutable GitHub Release tarball, not npm `latest`:

```sh
npx -y https://github.com/sandbaseai/cli/releases/download/v0.1.17/sandbaseai-cli-0.1.17.tgz connect
```

Approve the SandBase browser authorization once. The CLI stores a restricted local credential, installs the on-demand stdio MCP bridge for detected clients, and the agent then uses `discover → inspect → run`.

**Release split (verified 2026-08-25):** the GitHub Release tarball is built from the immutable `v0.1.17` tag (SHA-256 `1ad535b2899ca460b57b3c268aef278fee28fd28e649a89b92951514fd71fffa`). The npm `latest` tag currently serves **v0.1.14** while tokenless trusted publishing is being enabled. Do not treat `npx @sandbaseai/cli` as the current CLI.

Read-only compatibility catalog (no sign-in, no config writes):

```sh
npx -y https://github.com/sandbaseai/cli/releases/download/v0.1.17/sandbaseai-cli-0.1.17.tgz catalog --json
```

Optional published skill (install after connect; this is still a one-time browser-approval flow, not a one-URL join):

```sh
npx skills add sandbaseai/cli --skill sandbase
```

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add sandbaseai/cli --skill sandbase
```

| Skill | What It Teaches the Agent |
|---|---|
| [`sandbase`](https://github.com/sandbaseai/cli/blob/main/skills/sandbase/SKILL.md) | When to use the six MCP tools, the `discover → inspect → run` loop, async polling, pricing/balance checks, and the one-time browser connect step |

Also listed at [skills.sh/sandbaseai/cli/sandbase](https://www.skills.sh/sandbaseai/cli/sandbase). This is the CLI-packaged Skill, not the separate [sandbaseai/sandbase-skills](https://github.com/sandbaseai/sandbase-skills) org catalog.

---

## MCP

**Status:** ✅ Available (local on-demand bridge)

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/sandbaseai/cli |
| **Transport** | stdio local bridge launched by the client; no daemon or background process |
| **Authentication** | One browser OAuth device-flow + PKCE approval; credential stored locally with `0600` |
| **Compatible Clients** | Official README lists 25 targets, including Cursor, Cursor CLI, Claude Code, Codex, Kiro IDE/CLI, Windsurf, Gemini CLI, Amp, Warp, OpenCode, Qwen Code, Kimi CLI, Hermes, OpenClaw, plus manual setup for ChatGPT and Claude Desktop |

After connecting, the agent sees six tools: `sandbase_discover`, `sandbase_inspect`, `sandbase_run`, `sandbase_run_get`, `sandbase_runs`, `sandbase_account`.

---

## What It Does

SandBase CLI is an Apache-2.0 TypeScript CLI that connects a coding agent to a catalog of 2,000+ models and APIs through a compact local MCP surface. The operator (or an installer) runs `connect` once; the CLI detects supported clients, opens a browser authorization, writes a client-scoped credential, and adds only SandBase-owned MCP configuration.

After that, the agent searches the catalog (`sandbase_discover`), reads the current schema and price (`sandbase_inspect`), and executes (`sandbase_run`), polling async jobs with `sandbase_run_get`. `sandbase_runs` and `sandbase_account` expose recent cost and balance without starting a paid run.

This is a **tool-access bridge**, not an LLM gateway and not the SandBase Store. The homepage and [Getting Started](https://www.sandbase.ai/docs/getting-started/) docs describe a builder/FDE platform (Store, Setup, Build Agent). Those products are out of scope here. The sibling [SandBase Harness](../agent-runtime-and-infrastructure/sandbase-harness.md) is cataloged separately. [sandbase-skills](https://github.com/sandbaseai/sandbase-skills) is not cataloged.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Official README leads with **"Give your AI agent superpowers. One command. 2,000+ AI models."** and **"One command connects your agent to 2,000+ AI models through the [Model Context Protocol](https://modelcontextprotocol.io)."** — [sandbaseai/cli](https://github.com/sandbaseai/cli) |
| **Agent-specific primitive** | Six MCP tools for a planning loop (`discover → inspect → run`) plus async poll, recent-cost, and balance tools. A human model dashboard or per-provider REST API does not expose this compact runtime selection surface — [MCP tools](https://github.com/sandbaseai/cli#mcp-tools-available-to-your-agent-after-connecting), [SKILL.md](https://github.com/sandbaseai/cli/blob/main/skills/sandbase/SKILL.md) |
| **Autonomy-compatible control plane** | After one browser approval, the agent invokes the six tools without a human confirming each call. `sandbase_inspect` exposes schema and current price first; `unregister` removes only SandBase-owned state — [How it works](https://github.com/sandbaseai/cli#how-it-works), [Security](https://github.com/sandbaseai/cli#security). Initial authorization is not autonomous and is not URL Onboarding |
| **M2M integration surface** | On-demand stdio MCP bridge; `connect` / `doctor` / `unregister` / `catalog --json`; published Agent Skill; `llms-install.md` for automated installers — [CLI commands](https://github.com/sandbaseai/cli#cli-commands), [llms-install.md](https://github.com/sandbaseai/cli/blob/main/llms-install.md) |
| **Identity / delegation** | Each connected client gets a `CredentialRecord` (`credentialId`, `client`, `scope`, `mcpUrl`, `createdAt`) stored in a client-keyed local file. Ownership checks require `scope` to include `mcp:invoke` — [types.ts](https://github.com/sandbaseai/cli/blob/main/src/types.ts), [store.ts](https://github.com/sandbaseai/cli/blob/main/src/credentials/store.ts), [commands.ts](https://github.com/sandbaseai/cli/blob/main/src/commands.ts). This is **client-scoped delegated credentials under a user SandBase account**, not independent KYA or agent legal identity |

Tool Access is the correct category: the primitive is runtime discovery and delegated execution of models **and** APIs (search, scrape, social, media). It is not a per-agent LLM router.

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`sandbase_discover`** | Search the live catalog of 2,000+ models and APIs |
| **`sandbase_inspect`** | Return current input schema, price, and execution template before a call |
| **`sandbase_run`** | Execute the selected model or API |
| **`sandbase_run_get`** | Poll an asynchronous job (video generation, large scrapes) by run ID |
| **`sandbase_runs`** | List recent calls with status and cost |
| **`sandbase_account`** | Read account balance without starting a paid run |
| **Client-scoped credential** | Per-client local record with `mcp:invoke` scope, `0600` file mode, ownership-aware rollback |
| **25-client catalog** | Machine-readable `catalog --json` describing auto, guided, and manual client targets |

---

## Autonomy Model

```
Operator runs the v0.1.17 GitHub Release `connect` command
    -> CLI opens OAuth device-flow + PKCE browser approval (one human click)
    -> credential stored locally (0600), MCP bridge added for the target client
    -> agent calls sandbase_discover, then sandbase_inspect, then sandbase_run
    -> async jobs are polled with sandbase_run_get
    -> sandbase_runs / sandbase_account report cost and balance
    -> unregister / dashboard revoke removes only SandBase-owned state
```

No daemon. The client launches the stdio bridge on demand. The CLI is not a general policy or approval engine.

---

## Identity and Delegation Model

- **User account:** Browser approval binds a SandBase user account. The CLI does not mint an independent agent passport or KYA token.
- **Client-scoped credential:** `CredentialRecord` is keyed by client and includes `credentialId`, `client`, `scope`, `mcpUrl`, and `createdAt` ([types.ts](https://github.com/sandbaseai/cli/blob/main/src/types.ts)).
- **Delegation scope:** Ownership validation requires `scope` to include `mcp:invoke` ([commands.ts](https://github.com/sandbaseai/cli/blob/main/src/commands.ts)).
- **Isolation:** The local store writes one record per client; shared configuration slots refuse silent takeover by another client.
- **Secrets:** Device-flow + PKCE; no secrets in URLs or CLI args; files written with `0600` ([fs-safe.ts](https://github.com/sandbaseai/cli/blob/main/src/fs-safe.ts), [Security](https://github.com/sandbaseai/cli#security)).
- **Audit / cost:** `sandbase_runs` returns recent model/API calls with status and cost. That is run/cost history, not a full replay or approval artifact.
- **Revocation:** `unregister` removes only SandBase-owned MCP/Skill state; keys can also be revoked in the [SandBase Dashboard](https://sandbase.ai/console/keys).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Local MCP | On-demand stdio bridge exposing six `sandbase_*` tools |
| CLI | `connect`, `doctor`, `unregister`, `catalog --json` |
| Agent Skill | `npx skills add sandbaseai/cli --skill sandbase` |
| Installer notes | [llms-install.md](https://github.com/sandbaseai/cli/blob/main/llms-install.md) |
| Parent platform API | Separate HTTP API on sandbase.ai — not this catalog entry |
| npm package | `@sandbaseai/cli` exists; `latest` is v0.1.14 as of 2026-08-25 |

---

## Human-in-the-Loop Support

One browser approval is required to create the local credential. After that, ordinary discover/inspect/run calls do not prompt the operator. The CLI is not a per-action approval gate. Balance top-up and key revocation happen in the human dashboard. `llms-install.md` states the user must complete authorization personally and must not paste a credential into chat.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **SandBase Store / Build Agent homepage** | Human-facing capability marketplace and FDE workflow builder. It is the parent platform, not an agent MCP control plane. Not cataloged here |
| **Per-provider REST keys** | Each vendor has its own schema, auth, pricing, and async lifecycle. No single `discover → inspect → run` loop or client-scoped local delegation |
| **Generic LLM gateway** | Routes chat completions. SandBase CLI also searches, scrapes, and calls social/media APIs through the same six tools |
| **Manual per-client MCP config** | Repeats auth and dumps provider-specific tools into every host. No ownership-aware rollback or 25-client catalog |

---

## Use Cases

- **Coding agents that need live data** — web search, scrape, social, or image/video generation without wiring each provider key
- **Schema-before-spend** — inspect current price and input schema, then run
- **Async media jobs** — start a video generation run and poll by `run_id`
- **Shared laptop, scoped clients** — connect Cursor and Codex separately; each keeps its own credential record
- **Support / CI inspection** — `catalog --json` and `doctor` without signing in or rewriting config
