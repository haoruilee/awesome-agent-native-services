# CLI-Anything

> **"CLI-Anything: Making ALL Software Agent-Native"**

| | |
|---|---|
| **Website** | https://clianything.cc |
| **Docs** | https://github.com/HKUDS/CLI-Anything/blob/main/cli-anything-plugin/HARNESS.md |
| **GitHub** | https://github.com/HKUDS/CLI-Anything |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/HKUDS/CLI-Anything?style=social)](https://github.com/HKUDS/CLI-Anything) |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **License** | Apache-2.0 |

---

## Official Website

https://clianything.cc — CLI-Hub registry of agent-ready CLIs

---

## Official Repo

https://github.com/HKUDS/CLI-Anything — harness generator plugin/skill, generated CLIs, CLI-Hub manager. Paper: https://arxiv.org/abs/2606.03854

---

## How to Use (Agent Onboarding)

**Interaction pattern:** **Agent Skill** + **Structured CLI** (`--json`) + registry

```bash
# Let the agent find and install CLIs from CLI-Hub
npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y
# then prompt: "Find appropriate CLI software in CLI-Hub and complete the task: ..."

# Or manage CLIs yourself
pip install cli-anything-hub
cli-hub search <keyword>
cli-hub install <name>
```

---

## Agent Skills

**Status:** ✅ Available

| Skill | Source | What It Teaches the Agent |
|---|---|---|
| cli-hub-meta-skill | `npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill` | Discover and install CLIs from CLI-Hub to complete a task |
| CLI-Anything plugin | https://github.com/HKUDS/CLI-Anything/tree/main/cli-anything-plugin | Seven-phase harness generator that builds a new agent CLI for a codebase |

---

## MCP

**Status:** ⚠️ Not the primary surface — CLI-Anything targets shell-capable agents through generated CLIs and Skills.

---

## What It Does

CLI-Anything turns existing software (GUI applications, codebases and web APIs) into **agent-operable CLI harnesses**. A coding agent follows the project's seven-phase **HARNESS.md** procedure to analyze the target, map GUI actions to its real backend, and generate a stateful CLI with a REPL mode and subcommands. Every generated command supports `--json`. **CLI-Hub** is a registry where community-built CLIs can be searched and installed with one command.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"Today's Software Serves Humans. Tomorrow's Users will be Agents."*; tagline *"Making ALL Software Agent-Native"* |
| **Agent-specific primitive** | Agent-run harness generator (HARNESS.md SOP) and a meta-skill that lets an agent search and install CLIs from a registry at task time |
| **Autonomy-compatible control plane** | Agents install and operate CLIs without a GUI, display or mouse; deterministic commands with structured output |
| **M2M integration surface** | Generated CLIs with `--json` on every command, `--help` self-description, `cli-hub` package manager |
| **Identity / delegation** | ⚠️ Inherits the credentials and permissions of the host process and the wrapped software |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Harness generator** | Plugin/skill that builds an agent CLI for a target codebase |
| **Generated CLI** | Stateful REPL + subcommands with `--json` output |
| **CLI-Hub** | `cli-hub list / search / install / info / update / uninstall` |
| **Meta-skill** | Lets an agent pick and install the right CLI for a task |

---

## Autonomy Model

```
Agent receives a task needing some software
    ↓
Meta-skill → cli-hub search / install
    ↓
Agent drives the installed CLI with --json output
    ↓
(If none exists) agent runs the harness generator to build one
```

---

## Identity and Delegation Model

- Generated CLIs run as the local user and call the real backend software, so they inherit its credentials and file permissions.
- No built-in per-agent credential vault or scoping; isolate by running agents in separate environments.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **CLI** | Generated `cli-anything-*` CLIs with REPL + subcommands and `--json` |
| **Registry** | `cli-hub` (PyPI `cli-anything-hub`) and https://clianything.cc |
| **Skill** | `cli-hub-meta-skill`, CLI-Anything plugin |

---

## Human-in-the-Loop Support

Not required. Humans can contribute CLIs to the hub via pull request.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **GUI computer-use agents** | Pixel-level, brittle interaction with human interfaces |
| **Hand-written wrappers** | No shared methodology, registry, or agent install flow |

---

## Use Cases

- **Desktop software automation** (office, CAD, 3D, media editing) from a coding agent.
- **Extending agent toolsets** at task time by installing a CLI from the hub.
