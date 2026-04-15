# Agent Sandbox

> **"The trusted runtime for untrusted code."**

| | |
|---|---|
| **Website** | https://agentsandbox.co |
| **Docs** | https://agentsandbox.co/docs |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |

---

## Official Website

https://agentsandbox.co

---

## Official Repo

Not publicly listed. Official entry points are the hosted API, docs, and `skill.md` onboarding URL.

---

## ⭐ How to Use (Agent Onboarding)

Read:

```text
https://agentsandbox.co/skill.md
```

Then follow the skill instructions to start a sandbox session and run code.

SDK path:

```bash
pip install agentsandbox-sdk
```

---

## Agent Skills

**Status:** ✅ Available (URL onboarding at `https://agentsandbox.co/skill.md`)

| Skill | What It Teaches the Agent |
|---|---|
| `agentsandbox` (`skill.md`) | How to authenticate, create sessions, run code, and handle files/artifacts |

---

## MCP

**Status:** ⚠️ Not yet published as a dedicated official MCP server (as of April 15, 2026).

| Detail | Value |
|---|---|
| **Primary interface** | REST API + Python SDK |
| **URL onboarding** | `https://agentsandbox.co/skill.md` |
| **Compatible clients** | Any agent runtime that can call HTTPS APIs |

---

## What It Does

Agent Sandbox provides a managed, isolated runtime where AI agents can execute Python and shell commands, install dependencies, and exchange files through a single API. The product is positioned around giving each agent a personal remote computer and drive, with explicit support for sessioned execution and artifact pipelines.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage headline and copy: “SHIP AGENTS THAT EXECUTE CODE”, “Your agents need a computer and a drive. Here’s the API.” and “The trusted runtime for untrusted code.” — https://agentsandbox.co/ |
| **Agent-specific primitive** | Agent-oriented secure execution session, dependency manifest install, and file artifact pipeline (“Upload. Execute. Retrieve. One API for code, sessions, and artifacts.”) |
| **Autonomy-compatible control plane** | API-key + API-driven workflow for code execution; agents can run full loops without per-action human confirmation |
| **M2M integration surface** | REST docs + Python SDK install command (`pip install agentsandbox-sdk`) + URL onboarding |
| **Identity / delegation** | API key model and per-session execution context allow attributable, bounded agent operations |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Sandbox session** | Isolated runtime where an agent executes Python/shell commands |
| **Dependency manifest** | Per-run dependency installation for reproducible execution |
| **Artifacts pipeline** | Upload input files, process in sandbox, retrieve output files |
| **Skill onboarding URL** | Machine-readable bootstrap path for autonomous agent setup |

---

## Autonomy Model

1. Agent reads `https://agentsandbox.co/skill.md`.
2. Agent authenticates with API key and creates/uses a sandbox session.
3. Agent uploads input data and executes code inside isolated runtime.
4. Agent downloads generated artifacts and continues downstream tasks.
5. Human oversight is optional (dashboard), not required for every action.

---

## Identity and Delegation Model

- **Agent identity:** API key-backed service identity.
- **Delegation:** Operator decides which agent gets key access and budget.
- **Auditability:** Session/artifact operations are attributable to the authenticated key.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | https://agentsandbox.co/docs |
| Python SDK | `pip install agentsandbox-sdk` |
| URL Onboarding | `https://agentsandbox.co/skill.md` |

---

## Human-in-the-Loop Support

Optional dashboard-level monitoring and controls are available, but runtime execution is API-first and autonomous.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw VPS / shell hosting** | Not agent-first; lacks built-in autonomous onboarding and agent-oriented execution primitives |
| **Generic CI runners** | Optimized for build jobs, not persistent agent interaction loops with tool-call style runtime semantics |
| **Local Docker only** | Requires human-operated infra and does not provide hosted agent identity/control plane out of the box |

---

## Use Cases

- **Code interpreter tools** — secure execution for generated code.
- **Artifact generation** — transform data into reports/charts/files.
- **Agentic workflows** — run shell/Python steps inside a bounded environment.
- **Evaluation harnesses** — execute and verify generated code in isolation.
