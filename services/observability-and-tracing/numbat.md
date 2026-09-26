# numbat

> **"Endpoint visibility into AI agent activity, with local detection, optional pre-action blocking, and forensic reconstruction."**

| | |
|---|---|
| **Website** | https://github.com/perplexityai/numbat |
| **Docs** | https://github.com/perplexityai/numbat/tree/main/docs |
| **GitHub** | https://github.com/perplexityai/numbat |
| **Latest-month signal** | [v0.2.0](https://github.com/perplexityai/numbat/releases/tag/v0.2.0) released 2026-08-17; 1,073 stars; license Apache-2.0; repository `pushed_at` 2026-09-15 and default-branch commit 2026-08-17 ([repo metadata](https://api.github.com/repos/perplexityai/numbat)) |
| **Verified at** | 2026-09-26 |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |
| **License** | Apache-2.0 |

---

## Official Website

The official GitHub repository is the canonical project and documentation site:

https://github.com/perplexityai/numbat

---

## Official Repo

https://github.com/perplexityai/numbat

---

## How to Use (Agent Onboarding)

**Interaction pattern:** endpoint CLI + agent hooks/plugins + OTLP/HTTP

Install the single binary, inventory supported agents, and perform a read-only scan:

```bash
go install github.com/perplexityai/numbat/cmd/numbat@latest
numbat agents
numbat scan --agent codex
```

For live monitoring, install the agent-specific integration. Hooks start monitor-only and can write the complete typed record stream to a local file:

```bash
numbat hook install --agent codex --emit all
numbat hook status --agent codex
```

Use the release binaries and checksums when a Go toolchain is unavailable. See the official [Quick start](https://github.com/perplexityai/numbat/blob/main/README.md#quick-start) and authoritative [coverage matrix](https://github.com/perplexityai/numbat/blob/main/docs/agent-coverage.md#matrix).

---

## Agent Skills

**Status:** ⚠️ Not yet published — numbat installs native hook/plugin/extension integrations, not an Agent Skills `SKILL.md` package.

```bash
npx clawhub@latest search numbat agent-security
```

For faster access in China, use `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or pass `--registry https://cn.clawhub-mirror.com`.

See https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ No MCP server is published.

| Detail | Value |
|---|---|
| **MCP role** | numbat observes and normalizes MCP configuration and tool activity emitted by supported agents |
| **Normalized fields** | `mcp_server` and `mcp_tool` remain facets on the underlying tool/network event |
| **Important distinction** | Detecting MCP calls does not expose numbat itself as an MCP tool server |
| **Primary interfaces** | CLI, native hooks/plugins/extensions, OTLP/HTTP ingest, NDJSON/file/HTTP output, JSON Schema |

---

## What It Does

numbat is endpoint observability and policy infrastructure specifically for AI agents. It discovers supported agent installations, reconstructs existing sessions from on-disk artifacts, receives live activity from agent-native hooks/plugins or OTLP/HTTP, and normalizes all sources into one closed event vocabulary. A shared CEL engine evaluates both live and at-rest events for single-step and multi-step behaviors.

The output is a versioned NDJSON evidence stream: events, findings, enforcement decisions, indicators, and scan summaries retain endpoint, source agent, session/run, tool-call, and evidence references. `timeline` reconstructs session activity; `case build` creates portable evidence bundles with SHA-256 manifests. Optional enforcement can ask supported synchronous pre-action hooks to deny a clean match, while monitor-only behavior remains the default and every shipped rule is non-enforcing.

Coverage is deliberately bounded by each host's published artifacts and hooks. At-rest reconstruction cannot recover unpersisted actions, findings are not proof of compromise, and hook enforcement is not a complete endpoint security boundary.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The official README describes *"Endpoint visibility into AI agent activity"* and supports desktop, CLI, IDE, and gateway agents through their native artifacts and lifecycle hooks — [source](https://github.com/perplexityai/numbat/blob/main/README.md) |
| **Agent-specific primitive** | Normalized agent sessions, prompts, assistant/tool events, MCP facets, sub-agent identity, permission decisions, trajectories, evidence references, and host-native pre-action deny responses have no generic infrastructure-log equivalent ([event model](https://github.com/perplexityai/numbat/blob/main/docs/event-model.md)) |
| **Autonomy-compatible control plane** | Once installed, lifecycle hooks evaluate CEL rules and emit records without per-action operator input; an opt-in `enforce: true` rule can automatically request host-native denial on clean synchronous matches, otherwise the host's normal permission flow remains intact ([enforcement](https://github.com/perplexityai/numbat/blob/main/docs/enforcement.md)) |
| **M2M integration surface** | Single CLI binary, generated agent hooks/plugins/extensions, OTLP/HTTP collector, versioned NDJSON, HTTP delivery with bearer/HMAC options, and published JSON Schemas ([CLI](https://github.com/perplexityai/numbat/blob/main/docs/cli.md)) |
| **Identity / delegation** | Records preserve `source_agent`, optional `sub_agent`, `actor`, endpoint identity, `run_id`, `session_id`, `tool_call_id`, and evidence references; installation scopes (user/project/managed) and operator-controlled rules define the delegated policy boundary and produce attributable enforcement records ([coverage](https://github.com/perplexityai/numbat/blob/main/docs/agent-coverage.md), [deployment](https://github.com/perplexityai/numbat/blob/main/docs/deployment.md)) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent inventory** | Discovers supported local agent config, artifacts, live-capture mode, and hook wiring without executing the agent |
| **Artifact scan** | Read-only reconstruction of supported on-disk agent sessions with secret redaction and rules evaluation |
| **Live hook/plugin** | Host-specific lifecycle capture for prompts, tools, results, permissions, subagents, and session boundaries |
| **OTLP/HTTP collector** | Receives supported agent log exporters and maps them into the same normalized event model |
| **CEL rule engine** | Built-in and operator YAML rules, including multi-step sequences and companion tests |
| **Enforcement decision** | `deny` or `no_override` record tied to findings and proposed action IDs; only supported synchronous pre-action hooks can block |
| **Versioned record stream** | JSON-Schema-defined NDJSON for events, findings, enforcement, indicators, and scan summaries |
| **Timeline** | Per-source-agent/per-session chronological reconstruction retaining evidence references |
| **Case bundle** | Portable findings, decisions, cited events, optional raw evidence, and SHA-256 manifest verification |
| **Record shipping** | File/stdout and HTTP sinks; `ship` tails a capture file for at-least-once delivery while source segments remain available |

---

## Autonomy Model

```text
Operator selects agent targets, install scope, output sink, and monitor policy
    ↓
numbat installs the native hook/plugin or receives agent OTLP records
    ↓
Agent proposes actions and continues its normal task loop
    ↓
numbat normalizes each supported event and evaluates local CEL rules
    ↓
Monitor mode emits events/findings; enforce mode may return a clean native deny
    ↓
Versioned records flow to file/stdout/HTTP with source and evidence identity
    ↓
Investigators reconstruct timelines or build verifiable case bundles later
```

---

## Identity and Delegation Model

- **Agent identity** — `source_agent` identifies the host; `sub_agent` is retained when the source provides it; `actor` distinguishes assistant/user/system activity.
- **Execution attribution** — `run_id`, `session_id`, and `tool_call_id` correlate a proposal, its result, permission telemetry, finding, and enforcement decision when upstream supplies identifiers.
- **Endpoint identity** — Every record carries hostname, OS, architecture, username, and UID; operators may add a stable opaque `NUMBAT_DEVICE_ID` for fleet joins.
- **Delegated policy scope** — Hooks can target an upstream-supported user, project/explicit path, or managed machine policy. Operator rule directories and `enforce: true` determine what the monitored agent may be asked not to do.
- **Evidence trail** — Events/findings retain source references; case bundles include cited records and SHA-256 manifests. Unsigned bundles establish internal consistency, not independent source authenticity.
- **Boundary** — numbat does not issue agent credentials or impersonate users. A user-controlled hook can be edited or removed unless the binary, policy, output, and configuration are protected by OS/MDM controls.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **CLI** | `agents`, `scan`, `timeline`, `collect`, `ship`, `hook`, `rules`, `case`, and `version`; JSON/NDJSON-oriented automation and stable exit behavior |
| **Native agent integrations** | Generated hooks, plugins, or extensions for supported CLI, IDE, desktop, and gateway agents |
| **OTLP/HTTP ingest** | Local collector for supported protobuf log exporters; default endpoint pattern `127.0.0.1:4318/v1/logs` |
| **NDJSON output** | Version `0.2.0` typed records to stdout or file |
| **HTTP output** | `application/x-ndjson`, optional gzip, bearer or HMAC-SHA256 auth; direct delivery is not a durable queue |
| **JSON Schema** | Per-record and union-stream schemas under `docs/schema/v0.2.0/` |
| **Rule format** | YAML rules with CEL expressions, sequence steps, tests, versioning, and optional `enforce: true` |

---

## Human-in-the-Loop Support

Humans choose collection scope, review host trust/consent prompts, approve the rule catalog, and explicitly opt into enforcement; all shipped rules are monitor-only. After activation, capture, detection, record delivery, and clean enforced decisions run unattended. A `no_override` preserves the host agent's normal permission/approval flow, and even a numbat `deny` is a request interpreted by that host—not proof that the action was blocked. Operators should validate monitor coverage and durable output before enabling enforcement.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Generic log shipper** | Moves text or OTLP records but does not parse native agent artifacts/hooks into sessions, tool calls, MCP facets, permission decisions, subagents, and evidence-linked findings |
| **Traditional EDR rule** | Sees endpoint processes/files/network but usually lacks the agent's proposed action, host lifecycle, session/tool-call IDs, and native pre-action response contract |
| **Manual transcript review** | Cannot continuously normalize many agent products, evaluate sequence rules locally, emit versioned machine-readable findings, or preserve a reproducible evidence bundle |

---

## Use Cases

- **Coding-agent audit** — Attribute commands, file changes, MCP calls, and permission decisions to a Codex/Claude/Cursor session and tool call
- **Pre-action guardrails** — Monitor first, then opt selected tested rules into host-native denial for supported actions
- **Incident reconstruction** — Scan retained agent artifacts after an event, rebuild session timelines, and package cited evidence
- **Fleet agent inventory** — Discover which agent products, histories, and live integration surfaces exist on developer endpoints
- **Agent-security telemetry** — Feed normalized events, findings, and indicators to an existing SIEM/EDR pipeline through NDJSON or authenticated HTTP
