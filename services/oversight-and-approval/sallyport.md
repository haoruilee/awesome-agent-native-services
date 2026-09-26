# Sallyport

> **"Let your agent touch prod. Keep the keys."**

| | |
|---|---|
| **Website** | https://sallyport.dev |
| **Docs** | https://github.com/OlegSotnikov/sallyport/tree/main/docs |
| **GitHub** | https://github.com/OlegSotnikov/sallyport |
| **Stars** | [192 stars (snapshot: 2026-09-26)](https://github.com/OlegSotnikov/sallyport) |
| **Classification** | `agent-native` |
| **Category** | [Oversight & Approval Services](README.md) |
| **Latest-month signal** | Latest release is still [v0.8.16](https://github.com/OlegSotnikov/sallyport/releases/tag/v0.8.16) (2026-07-17); last push still 2026-07-19; 192 stars on 2026-09-26 (the 2026-08-13 snapshot was 246); license Apache-2.0; [sallyport.dev](https://sallyport.dev) returned HTTP 200 and still uses the catalog tagline ([repo metadata](https://api.github.com/repos/OlegSotnikov/sallyport)) |
| **Verified at** | 2026-09-26 |
| **Status** | Free Apache-2.0 Mac app; Apple Silicon and macOS 14+ only |

---

## Official Website

https://sallyport.dev

---

## Official Repo

https://github.com/OlegSotnikov/sallyport

---

## How to Use (Agent Onboarding)

Install the signed app, create and unlock its vault, add a credential, then register Sallyport as the MCP gate:

```bash
brew install --cask olegsotnikov/tap/sallyport
```

```bash
claude mcp add sallyport -- /Applications/Sallyport.app/Contents/MacOS/sp mcp
```

The shipped `sp` CLI exposes only `mcp` and `version`; credential creation and approval stay inside the signed Sallyport app.

---

## Agent Skills

**Status:** ⚠️ Not yet published by the project.

```bash
npx clawhub@latest search sallyport
```

See the [AgentSkills specification](https://agentskills.io/specification) to contribute one.

---

## MCP

**Status:** ✅ Available — MCP is the primary agent-facing gate.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/OlegSotnikov/sallyport |
| **Agent transport** | stdio through `sp mcp`, relayed to the signed app over a private Unix socket |
| **Built-in tools** | `http.request`, `ssh.exec`, `sallyport.request_credential` |
| **Upstream MCP** | Configured local stdio or remote Streamable HTTP servers, proxied through the same vault/approval/audit ladder |
| **Compatible clients** | MCP clients that can launch a local stdio server; the README gives Claude Code as the verified setup example |

---

## What It Does

Sallyport is a local Mac credential vault and execution gate for AI agents. An agent asks for a structured HTTP request, SSH command, credential-provisioning request, or upstream MCP tool call; Sallyport resolves the bound credential, applies its fixed authorization ladder, writes a durable audit intent, executes the operation, and returns a bounded result without providing a credential-reveal command.

The boundary is intentionally precise. Stored keys remain in the app for HTTP and SSH operations, but configured local stdio MCP servers necessarily receive credentials in their child environments. Target/upstream responses are returned without content inspection and may echo sensitive values. Sallyport protects its own execution path; it cannot govern traffic the agent sends elsewhere.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The project defines Sallyport as a [vault that executes authenticated actions for AI agents](https://github.com/OlegSotnikov/sallyport#readme). |
| **Agent-specific primitive** | Credentialless action execution, kernel-observed agent-process admission, session/per-call approval, agent-requested credential provisioning, and a signed audit intent before every side effect. |
| **Autonomy-compatible control plane** | Approved, observed, or allowlisted live processes can execute non-per-call actions unattended; keys and upstreams can independently require click or Touch ID on every call. |
| **M2M integration surface** | Local MCP server with structured HTTP/SSH tools and transparent local/remote MCP proxying; no human dashboard is needed for actions that policy admits automatically. |
| **Identity / delegation** | The app derives identity from kernel-observed PID/start time, executable path, and code signature, then applies host-scoped allowlists and credential bindings. Each intent/result is added to an encrypted, hash-chained, signed journal with process provenance. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Credentialless authenticated action** | Agent supplies an operation; the app resolves and injects the matching credential without a reveal/export route |
| **Session approval** | Click or Touch ID admits one live process until exit, revoke, vault lock, or app exit |
| **Per-call approval** | One invocation approved by click or Touch ID for marked keys or upstream MCP servers |
| **Kernel-observed process identity** | PID plus start time, executable, parent chain, and signing information revalidated during a session |
| **Host/path binding** | Selects where an HTTP credential may be attached; agent cannot choose the vault key or reserved auth headers |
| **Durable audit intent** | Signed, encrypted, hash-chained row is fsynced before a side effect may execute |
| **Credential request** | Agent asks the user to provision a named purpose/host and receives status, never the secret value |
| **Encrypted SSH recording** | Preserves a bounded asciicast under a vault-derived encryption key |

---

## Autonomy Model

1. A user creates/unlocks the vault, binds credentials to destinations, and chooses session/per-call approval settings.
2. `sp mcp` connects the agent process to the private Sallyport socket; the app derives the caller identity from the kernel rather than trusting a self-declared label.
3. Sallyport verifies vault state, target metadata, per-call requirements, existing session/allowlist status, and the configured session mode.
4. If required, a click or Touch ID card resolves in process; otherwise policy admits the call automatically.
5. A durable signed audit intent is written before execution. Sallyport then performs the HTTP, SSH, credential request, or proxied MCP action and attempts to append its result.

---

## Identity and Delegation Model

- A live agent session is keyed by PID plus process start time; executable and signing data are rechecked on later calls.
- An optional exact code hash or publisher requirement can skip only the session card, optionally scoped to hosts. It cannot bypass vault state, per-call confirmation, binding, audit, or lifecycle checks.
- Credential bindings delegate a key only to configured HTTP host/path targets, SSH inventory entries, or MCP servers. The agent cannot select or retrieve the stored value.
- Audit events include channel, tool, target, bounded arguments, rule/decision, process provenance, result status, and SSH evidence where applicable.
- Sessions are not restart-durable: vault lock or app exit clears live sessions and pending approvals; lifecycle events remain in the journal.
- Identity proves which process connected, not the process's intent or which component authored bytes on an inherited descriptor.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **MCP stdio** | `sp mcp` exposes Sallyport tools to a local MCP client |
| **Private Unix socket** | Connects the minimal shim to `Sallyport.app` with kernel peer identity |
| **HTTP executor** | Structured GET/POST/PUT/PATCH/DELETE/HEAD with bearer, basic, custom-header, AWS SigV4, or OAuth2 client-credentials adapters |
| **SSH executor** | Configured-host command execution with challenge signing and encrypted asciicast recording |
| **Upstream MCP** | Local stdio or remote Streamable HTTP with API key or OAuth 2.1 support |
| **Audit JSONL** | ECIES-sealed rows, hash chain, ECDSA signatures, and an integrity anchor under `~/.sallyport/audit` |

---

## Human-in-the-Loop Support

Session approval is the default and asks once per new process. Operators can require click or Touch ID for each use of selected keys or MCP servers; one card may satisfy both a new-session gate and the current per-call gate. Requests time out after 120 seconds, denial returns a structured error, and vault lifecycle changes invalidate stale approvals.

Approvals are in-process decisions, not signed grants, and they identify a process or operation rather than proving intent. Multi-party approval, remote approvers, policy language, and approval TTL grants are not implemented.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Environment variables / `.env` files** | Put the credential in the same process and dependency graph as the potentially prompt-injected agent. |
| **Traditional secret manager** | Usually delivers a decrypted secret to the workload instead of executing a bounded operation on its behalf. |
| **Ungated MCP proxy** | Does not add kernel-derived caller identity, destination-bound credentials, per-call approval, or a fail-closed signed intent journal. |

---

## Use Cases

- **Production API operations** — let a coding or operations agent call authenticated services without receiving the API key
- **Gated SSH automation** — execute approved remote commands with process attribution and encrypted recordings
- **Credential-safe MCP access** — place third-party MCP tools behind one vault, approval, and audit boundary
- **Just-in-time provisioning** — let an agent request a missing credential while the user enters it directly into the signed app
- **Prompt-injection containment** — require Touch ID for particularly sensitive destinations even inside an admitted session
