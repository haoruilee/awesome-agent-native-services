# Tracekit

> **"Let your agents act. Prove every action."**

| | |
|---|---|
| **Website** | https://tracekit.tech |
| **Docs** | https://github.com/Cygnux-Labs/Tracekit/wiki |
| **GitHub** | https://github.com/Cygnux-Labs/Tracekit |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/Cygnux-Labs/Tracekit?style=social)](https://github.com/Cygnux-Labs/Tracekit) |
| **Classification** | `agent-native` |
| **Category** | [Oversight & Approval Services](README.md) |
| **License** | MIT |
| **Status** | Self-hosted software: a stable core, with the other surfaces marked experimental ([what's stable](https://github.com/Cygnux-Labs/Tracekit/wiki/Support)) |

---

## Official Website

https://tracekit.tech

---

## Official Repo

https://github.com/Cygnux-Labs/Tracekit

The Python package is `tracekit-ai` on PyPI (`tracekit` on PyPI is an unrelated project); the TypeScript SDK is `@cygnuxlabs/tracekit` on npm.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** SDK (Python or TypeScript) that asks a signer you run before each tool call

**Quickest verified path:**

```bash
pip install tracekit-ai   # then make "import tracekit; tracekit.instrument()" the agent's first line and run it
tracekit last             # export the latest run and verify it offline
tracekit approvals list   # calls held for a person; answer with: tracekit approvals approve ID
```

`tracekit.instrument()` starts a dev signer (or reuses the running one) and gates and records every tool and model call of the frameworks it finds ([quickstart](https://github.com/Cygnux-Labs/Tracekit/wiki/Quickstart)).

Other entry points:

- Coding agents: `tracekit init --dev --v2` wires Claude Code's hooks to a dev signer; add `--agent codex`, `cursor`, `gemini` or `opencode` for the others (experimental). See [coding agents](https://github.com/Cygnux-Labs/Tracekit/wiki/Coding-Agents).
- TypeScript (Node 18 or newer): `npm install @cygnuxlabs/tracekit` (experimental).
- Agents that reach their tools over MCP: put the MCP gateway in front of the MCP servers (experimental, see [MCP](#mcp) below).

Dev mode is for trying Tracekit: the signer runs as your user, the same user as the agent, so it protects nothing against that agent. For a record the agent can't rewrite, run the signer as another OS user (Linux system mode, `tracekit init --v2 --user AGENT` as root), in a container or on another host, and point the agent at it with `TRACEKIT_SIGNER` ([deployment](https://github.com/Cygnux-Labs/Tracekit/wiki/Deploy)). The agent's code is the same in every mode.

---

## Agent Skills

**Status:** ⚠️ Not yet published as a standalone `SKILL.md` package

The experimental Claude Code plugin (`/plugin marketplace add Cygnux-Labs/Tracekit`) carries the Claude Code hooks, three slash commands and one skill, `tracekit-graph`, which answers questions about past runs from `tracekit graph` output. There is no skill that sets Tracekit up.

Search community skills: `npx clawhub@latest search tracekit`. See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available: an MCP gateway in front of your MCP servers (experimental)

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/Cygnux-Labs/Tracekit |
| **Server** | `tracekit mcp-gateway serve`, listed in the MCP Registry as `io.github.Cygnux-Labs/tracekit-mcp-gateway`: a remote server at `https://{tracekit_gateway}/mcp`, the host you run it on |
| **Transport** | Streamable HTTP to agents; stdio or Streamable HTTP to the upstream MCP servers it proxies |
| **Auth** | The gateway's HTTPS listener uses the signer's identity plugins (mTLS, Kubernetes service-account tokens, tokens); each request carries the agent's run in `X-Tracekit-Run` |
| **Compatible Clients** | MCP clients whose agent framework sets `X-Tracekit-Run` for each run. It changes every run, so a client that takes headers once, at install, works for one run only |
| **Docs** | https://github.com/Cygnux-Labs/Tracekit/wiki/MCP-Gateway |

The gateway decides, runs and completes every tool call in the signer, and keeps the upstream servers' credentials, so the agent can only ask for a call. The stable MCP client integration instead wraps the agent's own MCP client session and records the calls it makes ([MCP integration](https://github.com/Cygnux-Labs/Tracekit/wiki/Integrations-MCP)).

---

## What It Does

Tracekit checks every tool call an agent makes before it runs, signs each call and decision into a hash chain, and exports one `.tkb` file per run that anyone can verify offline. The policy answers allow, deny or ask. A denied call goes back to the model as a refusal and the agent carries on; an asked call waits until a person approves it, and the approval covers those exact arguments and works once.

The signer is a separate process the agent reaches over a Unix socket, loopback TCP or HTTPS. The agent holds a run token, never a signing key, and never assigns sequence numbers. The record is tamper-evident: an edited, deleted, swapped or inserted record fails verification at that record. Cutting off the end of the log, or re-signing it with a stolen key, takes an independent witness (experimental) to catch.

Limits, from the project's own docs: in dev mode the signer runs as the agent's own user, so the agent could read the key and rewrite the store; the guarantee needs the signer under another user, in a container or on another host. A verified run proves the record is intact, not intent, not that a reported tool result is true, and not that every action was captured. Calls that skip the SDK, hook or gateway aren't decided or recorded, and policy rules match text and tool names, so a determined agent can reword a command ([limits](https://github.com/Cygnux-Labs/Tracekit/wiki/Limits)).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | **"Tracekit checks each tool call your agent makes before it runs. Risky calls wait for a person to approve them."** — [tracekit.tech](https://tracekit.tech); **"Tracekit checks every tool call your agent makes before it runs, signs each call and decision into a hash chain, and gives you one `.tkb` file per run that anyone can verify offline."** — [README](https://github.com/Cygnux-Labs/Tracekit#readme) |
| **Agent-specific primitive** | A per-call `decide` (allow, deny or ask) the agent's adapter calls before each tool call, and an approval bound to that call's exact arguments, run, tool call id and attempt that `approval_consume` uses once. Edited arguments, a replayed approval or another run's approval are refused, and each refusal is signed ([approvals](https://github.com/Cygnux-Labs/Tracekit/wiki/Approvals)) |
| **Autonomy-compatible control plane** | Allowed calls run with no click; the signer round trip added 0.91 ms per call at p99 in the project's E9 benchmark. Only calls that match an `ask` rule wait for a person. A denied call returns the rule and reason to the agent instead of running |
| **M2M integration surface** | Python SDK (`tracekit.instrument()`, `RunHandle`), TypeScript SDK, framework integrations, coding-agent hooks, MCP gateway, signer RPC over a Unix socket or HTTPS, CLI |
| **Identity / delegation** | The signer takes each caller's identity from its transport and records it in the run's `run.registered`; `signer.yaml` grants each identity the RPCs it may make and names who may approve; each signed `approval` record carries the approver's identity ([identity](https://github.com/Cygnux-Labs/Tracekit/wiki/Identity)) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Policy decision** | `decide` before each tool call: allow, deny or ask, from YAML policy packs for shell, files, SQL, HTTP, cloud CLIs, browsers, email, messaging, payments, secrets and MCP; signed as `policy.decision` |
| **Argument-bound approval** | `approval_request` binds one call's tool and exact arguments (a commitment), run, tool call id, attempt, policy hash and expiry. States: `requested → approved, rejected or expired`; `approved → consumed or expired` |
| **Consume once** | `approval_consume` lets the call run only if its arguments match the approved ones and the approval is unexpired and unused; it signs `approval.consumed`, or `approval.binding_mismatch` / `approval.refused` |
| **T2 execution** | An `ask` rule marked `approval: {executor: t2}` makes the signer hand its own copy of the approved arguments to a gateway or executor outside the agent (experimental), which runs exactly those |
| **Signed run record** | Every call, decision, approval and result in one Ed25519-signed hash chain per run; a lost event becomes a signed gap |
| **Offline bundle** | `tracekit export --v2` writes one `.tkb` file per run; `tracekit verify` (Python) or the TypeScript verifier checks it offline against keys you pinned |
| **Holds and quarantine** | Detection sequences and limits that hold or quarantine a run as signed incidents (experimental) |

---

## Autonomy Model

1. The agent's adapter (a framework integration, a coding-agent hook or the MCP gateway) registers a run with the signer and gets a run token. It never holds a signing key.
2. Before each tool call, the adapter calls `decide`. The signer signs the decision; an allowed call runs at once.
3. A denied call doesn't run. The rule and reason go back to the agent as a refusal, and the agent goes on with its task.
4. An asked call: the adapter calls `approval_request`, and the signer signs an `approval.request` bound to that call. Depending on the adapter, the run waits up to a deadline, or pauses and resumes after the answer (LangGraph `interrupt()`, OpenAI Agents `RunState`). The coding-agent hooks block the call at once, and the agent's retry of the same call runs once a person has approved it.
5. `approval_consume` checks the call's arguments against the approved ones; the call runs once, and its result is signed.
6. When the run ends, `tracekit export --v2` writes it as a `.tkb` bundle, and `tracekit verify` checks it offline.

---

## Identity and Delegation Model

- **Agent vs. signer:** the agent never holds a signing key and never assigns sequence numbers. Nothing the agent reports about itself is trusted: not its isolation, its fail mode, gaps, or who approved a call.
- **Caller identity:** the signer takes it from the transport: the Unix socket's peer uid or a token (stable); over HTTPS, mTLS (SPIFFE), Kubernetes service-account tokens or OIDC (experimental). It is recorded in the run's `run.registered`.
- **Delegation:** `signer.yaml` `authorize` grants each identity the RPCs it may make; `approvals` lists who may answer approvals and who may break glass. A signer started from `signer.yaml` refuses an answer from the call's own requester unless `self_approval: allow` is set.
- **Audit:** each `approval` record carries the approver's identity as its transport established it, the channel, the reason, `self_approved` and, when it applies, `break_glass`; `approval.consumed` ties the approval to the call that ran.
- **Boundary:** the dev signer runs as the agent's own user and lets the requester answer its own approvals; such answers are recorded `self_approved: true` and the run's assurance stays `dev`. Dev runs record `isolation: same-user`. A signer under another OS user, in a container or on another host records `separate-user` or `remote`.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **Python SDK** | `pip install tracekit-ai`; `tracekit.instrument()` or `RunHandle`; Python 3.9 to 3.13 (framework integrations need 3.10 or newer) |
| **TypeScript SDK** | `npm install @cygnuxlabs/tracekit` (experimental); speaks the signer RPC itself; Node 18 or newer |
| **Framework integrations** | Stable: OpenAI Agents SDK, LangChain / LangGraph, Claude Agent SDK, MCP client. Experimental: CrewAI, Browser Use, Pydantic AI, Google ADK, Haystack, LlamaIndex, Microsoft Agent Framework, Strands Agents, Vercel AI SDK |
| **Coding-agent hooks** | Claude Code (stable); Codex CLI, Cursor, Gemini CLI and OpenCode (experimental), wired by `tracekit init --dev --v2` |
| **MCP gateway** | `tracekit mcp-gateway serve` (experimental): Streamable HTTP for agents; decides each tool call in the signer |
| **Signer RPC** | A versioned request and response contract over a Unix socket, loopback TCP with a token, or HTTPS (experimental) |
| **CLI** | `tracekit approvals list / show / approve / reject`, `tracekit export --v2`, `tracekit verify`, `tracekit view` |
| **Bundle format** | `.tkb`, evidence format v2; verifiers in Python and TypeScript |

---

## Human-in-the-Loop Support

An `ask` rule holds a call until a person answers. Approvers answer from the command line (`tracekit approvals approve` or `reject`, stable) or, experimentally, from a web page with passkeys, from Slack, or through a reviewer agent that approves within bounds. What the approver sees is the signer's copy of the arguments, never what the agent shows; a reason the agent gave is printed as unverified.

The approval covers those exact arguments and works once. Edited arguments, a replayed approval or another run's approval are refused, and each refusal is signed. Approvals expire (one hour by default). With a T2 rule, the call runs exactly as approved, through a gateway or executor outside the agent (experimental).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **The agent's own logs, or a tracer fed by them** | Written by the process being audited, so an agent that can edit its log can hide what it did. A tracer records after the fact; it doesn't decide a call before it runs. Tracekit sits beside one rather than replacing it |
| **A ticket or CI approval step** | Not bound to the exact arguments of the call that later runs, so nothing stops an edited or replayed call, and the answer doesn't return into the agent's control flow at the tool call |
| **A prompt and output guardrail library** | Checks the text going into and out of the model, not each tool call before it runs; Tracekit adds a signed record of each decision and is meant to run beside one ([comparisons](https://github.com/Cygnux-Labs/Tracekit/blob/main/COMPARISONS.md)) |

---

## Use Cases

- **Holding costly actions for a person** — a refund, a force push or a production delete waits until someone approves it; the approval covers those exact arguments and works once
- **Evidence for someone outside the team** — a customer, an auditor or an incident review gets one `.tkb` file per run and checks it offline, with keys they pinned
- **Coding agents** — Claude Code's hooks decide each tool call against the policy before it runs (in dev mode, a record for watching your own agent, not protection against it)
- **MCP tools without handing the agent credentials** — the MCP gateway keeps the upstream servers' credentials and runs each call itself (experimental)
- **Incident review** — `tracekit view` shows each run verified, with its blocked and held calls, approvals and gaps
