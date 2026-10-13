# AgentSight

> **"lightweight system-level observability for AI Agents"**

| | |
|---|---|
| **Website** | https://eunomia.dev/agentsight/ |
| **Docs** | https://eunomia.dev/agentsight/ |
| **GitHub** | https://github.com/eunomia-bpf/agentsight |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/eunomia-bpf/agentsight?style=social)](https://github.com/eunomia-bpf/agentsight) |
| **Classification** | `agent-native` |
| **Category** | [Observability & Tracing Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push 2026-08-25 ([repo metadata](https://api.github.com/repos/eunomia-bpf/agentsight)); docs updated 2026-08-24 |
| **Verified at** | 2026-10-13 |

---

## Official Website

https://eunomia.dev/agentsight/

---

## Official Repo

https://github.com/eunomia-bpf/agentsight

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` wrapper (operator-surface track)

```bash
cargo install agentsight
# or: brew tap eunomia-bpf/tap && brew install eunomia-bpf/tap/agentsight

agentsight top
sudo agentsight record -- claude
```

`agentsight top` ranks live sessions. `record -- <command>` wraps any command (official examples: `claude`, `gemini`, `kimi`, `grok`, or a raw binary). Replay local Claude/Codex/Gemini sessions with `agentsight vis`. There is no URL-onboarding document.

This entry is admitted on the **operator-surface track**: wrap a command, observe, report. **Observation is not authorization.** AgentSight does not grant, deny, or enforce tool permissions.

---

## Agent Skills

**Status:** ⚠️ No official Agent Skills package published.

```bash
npx clawhub@latest search agentsight
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ Not an MCP server.

AgentSight can observe MCP stdio traffic from the outside (see upstream `docs/agents.md`). It does not expose itself as MCP tools.

---

## What It Does

AgentSight is a local-first `top`/`strace`-like observer for AI agents. Docs title: **"System-wide AI agent profiling and monitoring with eBPF"**. GitHub description: **"lightweight system-level observability for AI Agents"**. It correlates prompts, model calls, and tool decisions with **real host effects** — processes, files, network, TLS payloads at SSL call boundaries — without an SDK, proxy, or vendor hook inside the agent.

`record` writes `agentsight-*.db` session files. `report` queries them (prompts JSON, token grouping, audit JSON). Optional OTLP/HTTP export emits OpenTelemetry **GenAI** (`gen_ai.*`) spans. `top` / `vis` / `report` can also read native Claude/Codex/Gemini session files without eBPF; `record` and live eBPF need Linux + privileges.

**Complement, don't replace:** [Langfuse](langfuse.md) and [Laminar](laminar.md) are application/trace products (you instrument or proxy the app). [numbat](numbat.md) is endpoint/hook visibility with optional pre-action blocking. AgentSight is **system-level eBPF + session files + OTLP GenAI**, including closed-source CLIs that never called an SDK.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | GitHub: **"lightweight system-level observability for AI Agents"** — [repo](https://github.com/eunomia-bpf/agentsight). Docs: **"System-wide AI agent profiling and monitoring with eBPF"** and **"local-first top/strace-like observability tool for AI agents"** — [eunomia.dev/agentsight](https://eunomia.dev/agentsight/) |
| **Agent-specific primitive** | Session-ranked `top` (model, tokens, tool/file/network activity); wrap-any-command `record`; SQLite session files; GenAI OTLP export; agentpprof token flamegraphs from local Codex/Claude history |
| **Autonomy-compatible control plane** | After install, `record -- claude` runs the agent without per-action human clicks. AgentSight is read-only relative to the agent's permissions |
| **M2M integration surface** | CLI, `agentsight-capture` Rust crate, OTLP/HTTP, JSON/SQLite reports, optional web UI on `127.0.0.1:7395` |
| **Identity / delegation** | State is attributed to a recorded command session / native agent session / SQLite `agentsight-*.db`. **Observation is not authorization or enforcement.** eBPF probes are privileged; the wrapped agent still runs as the normal user |

This is the operator-surface track: purpose-built around live agent sessions (tokens, tools, files, model calls), not a generic process monitor. Autonomy, delegated credentials, and approval enforcement are **absent** and documented as such.

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`agentsight top`** | Live ranked sessions (eBPF when sudo is already available; else snapshots + native session files) |
| **`record -- <cmd>`** | Wrap any command; kernel + TLS boundary capture on Linux |
| **Session DB** | `agentsight-*.db` in the working directory |
| **`report`** | Summary, prompts, tokens, audit JSON, `serve` UI, export snapshot |
| **`vis`** | Replay file effects from local coding-agent sessions |
| **OTLP GenAI** | `debug trace --otel --otel-endpoint …` |
| **agentpprof** | Offline token/system-effect profiles from local session history |

---

## Autonomy Model

```
Operator installs the CLI
    -> agentsight top | sudo agentsight record -- <agent>
    -> Collector writes a session DB and/or live UI
    -> report / vis / OTLP consume the same session identity
    -> Agent keeps executing; AgentSight does not approve or block tools
```

numbat can optionally block; AgentSight's documented product is observe/export.

---

## Identity and Delegation Model

- **Session identity:** The recorded command, native CLI session files, or `--db` path.
- **Attribution:** Process spawns, file opens, API calls, and LLM payloads hang off that session.
- **Privilege split:** eBPF needs root/`CAP_BPF`; the agent process stays the invoking user.
- **Not a policy engine:** Seeing a file write is not permission to have written it, and AgentSight does not stop the write.
- **Sensitive logs:** Official FAQ: captured data can include prompts, paths, headers, and network targets — treat DBs as sensitive.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `cargo install agentsight` / Homebrew tap `eunomia-bpf/tap` |
| Rust library | `agentsight-capture` |
| OTLP/HTTP | GenAI spans |
| Local UI | `http://127.0.0.1:7395` during a session; `report serve` for a saved DB |
| Session files | SQLite `agentsight-*.db`; `~/.agentsight/monitor` for the background service |

---

## Human-in-the-Loop Support

`top`, `vis`, and the web UI are the operator surfaces. They are read-only with respect to agent authority. sudo is a human/ops prerequisite for eBPF `record`, not a per-tool approval product.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Langfuse / Laminar** | App-level traces and evals. They miss subprocesses, local files, and closed-source CLIs unless you instrument or proxy |
| **numbat** | Endpoint/hook visibility and optional pre-action blocking. Complements AgentSight; it is not eBPF system-effect profiling + session DBs |
| **Generic `top` / `strace`** | Host process telemetry. They do not bind model/tool/token state to an agent session or export GenAI OTLP |
| **A vendor LLM gateway** | Sees proxied HTTP only. AgentSight is explicitly zero-SDK / zero-proxy |

---

## Use Cases

- **Debug a stuck coding agent** — correlate a prompt with the files and subprocesses it actually touched
- **Token / resource forensics** — `report token` and agentpprof on local session history
- **Security review** — `report audit --json` for spawns, file opens, and API calls (still not enforcement)
- **Export to an existing APM** — OTLP GenAI spans without adding an SDK to Claude Code / Gemini CLI
