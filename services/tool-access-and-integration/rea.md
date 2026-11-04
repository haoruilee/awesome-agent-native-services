# REA (Reverse Engineer Anything)

> **"One MCP for reverse engineering across binaries, applications, and runtime behavior."**

| | |
|---|---|
| **Website** | https://rea.tools |
| **Docs** | https://github.com/morluto/rea/blob/main/docs/installation.md |
| **GitHub** | https://github.com/morluto/rea |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/morluto/rea?style=social)](https://github.com/morluto/rea) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | MIT |

---

## Official Website

https://rea.tools

---

## Official Repo

https://github.com/morluto/rea — MCP server + CLI, published to npm as `rea-agents`

---

## How to Use (Agent Onboarding)

**Interaction pattern:** **MCP (stdio)** + **CLI** + agent workflow instructions

```bash
# Preview the config changes first, then apply
npx -y rea-agents setup --dry-run
npx rea-agents setup        # choose agents, review, approve (backs up existing config)
# restart the agent, then verify
rea doctor --json
```

Setup guide: https://github.com/morluto/rea/blob/main/docs/installation.md

---

## Agent Skills

**Status:** ✅ `setup` installs matching workflow instructions for each selected agent alongside the MCP server.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Docs** | https://github.com/morluto/rea |
| **Transport** | stdio |
| **Install** | `npx rea-agents setup` registers the server in supported clients (Claude Code, Codex, Cursor, Gemini CLI and others) |
| **Uninstall** | `rea uninstall` reverts the configuration changes |

---

## What It Does

REA connects a coding agent to local reverse-engineering tools for **native binaries** (pseudocode, assembly, strings, symbols via Hopper, Ghidra or IDA), **JavaScript and Electron apps** (modules, source maps, IPC channels, native add-ons), **.NET assemblies** (metadata and CIL), **Android APKs** (via JADX) and **websites** (structure, scripts, observed traffic via a Chrome-family browser). It can also capture runtime process behavior. Analysis runs locally, and results include the evidence and limitations behind each conclusion, so the agent can ask follow-up questions or write and test an implementation.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repo description: *"Reverse engineer anything with agents, from app behavior down to native binaries."* |
| **Agent-specific primitive** | Evidence-backed findings (with stated limitations) returned to the agent over MCP; per-agent setup that writes MCP config plus workflow instructions |
| **Autonomy-compatible control plane** | After one approved setup, the agent calls analysis tools itself and iterates on findings without per-call human action |
| **M2M integration surface** | MCP server; CLI with the same workflows and `--json` output (`rea doctor --json`) |
| **Identity / delegation** | ⚠️ Runs locally with the user's permissions; no separate agent identity |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Binary analysis** | Pseudocode, assembly, strings, symbols, references through Hopper/Ghidra/IDA |
| **JS / Electron analysis** | Static walk of app bundles: modules, source maps, IPC, native add-ons |
| **.NET / Android** | Assembly metadata and CIL; APK decompilation via JADX |
| **Web observation** | Page structure, scripts and traffic through a browser |
| **Process capture** | Run one selected command and record bounded evidence of its behavior |

---

## Autonomy Model

```
User runs rea-agents setup once (reviews and approves config changes)
    ↓
Agent calls REA MCP tools on a target
    ↓
REA analyzes locally and returns findings with evidence and limits
    ↓
Agent follows up, explains the behavior, or implements and tests
```

---

## Identity and Delegation Model

- REA runs on the local machine as the current user; static analysis reads files without executing them.
- Runtime/process capture runs the target with the user's permissions and is not a sandbox — use a disposable VM for untrusted binaries.
- `setup` rewrites agent configuration with backups; `rea uninstall` reverts it.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **MCP** | stdio server registered by `rea-agents setup` |
| **CLI** | `rea …` commands sharing the MCP workflows; `rea doctor --json` |
| **npm** | `rea-agents` |

---

## Human-in-the-Loop Support

Setup asks the user to review and approve configuration changes (with `--dry-run` preview). Analysis calls then run without confirmation.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Ghidra / IDA / Hopper alone** | Human GUI tools without an agent-facing interface across target types |
| **Single-engine MCP wrappers** | Cover one disassembler, not binaries, Electron, .NET, Android and web in one evidence-returning surface |

---

## Use Cases

- **Understanding how an app feature works** down to the binary, then reimplementing it.
- **Auditing Electron apps** for IPC channels and native add-ons.
- **Malware or binary triage** inside a disposable VM with an agent driving the analysis.
