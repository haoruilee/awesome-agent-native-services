# acpx

> **"Headless CLI client for stateful Agent Client Protocol (ACP) sessions — so AI agents and orchestrators can talk to coding agents over a structured protocol instead of PTY scraping."**

| | |
|---|---|
| **Website** | https://github.com/openclaw/acpx |
| **Docs** | https://github.com/openclaw/acpx/blob/main/docs/CLI.md |
| **GitHub** | https://github.com/openclaw/acpx |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **Protocol** | [Agent Client Protocol (ACP)](https://agentclientprotocol.com) |

---

## Official Website

https://github.com/openclaw/acpx

---

## Official Repo

https://github.com/openclaw/acpx

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Coding-time Skill + CLI`

```bash
# Install acpx globally (recommended for session reuse)
npm install -g acpx@latest

# Install the acpx skill for full command reference
npx acpx@latest --skill install acpx

# Read the skill reference for all commands and workflows
# Read https://raw.githubusercontent.com/openclaw/acpx/main/skills/acpx/SKILL.md

# Delegate to a coding agent via ACP
npx acpx@latest codex "fix the failing tests"
npx acpx@latest claude "refactor the auth module"
npx acpx@latest exec "one-shot: summarize this repo"
```

---

## Agent Skills

**Status:** ✅ Available

```bash
npx acpx@latest --skill install acpx
```

| Skill | What It Teaches the Agent |
|---|---|
| `acpx` | Use acpx as headless ACP CLI for agent-to-agent communication: prompt/exec/sessions workflows, session scoping, queueing, permissions, and output formats |

---

## MCP

**Status:** ⚠️ Not applicable — acpx is a CLI client that implements the ACP protocol. Agents invoke it as a subprocess; it does not expose an MCP server.

---

## What It Does

acpx is a **headless CLI client for the Agent Client Protocol (ACP)**. It enables AI agents and orchestrators to delegate work to coding agents (Pi, OpenClaw, Codex, Claude, etc.) over a structured protocol instead of scraping PTY sessions. One command surface for all ACP-compatible agents.

Core value: **typed ACP messages** (thinking, tool calls, diffs) instead of ANSI scraping. Agents get structured, parseable output and can manage persistent sessions, queue prompts, and cancel in-flight work cooperatively.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | *"Your agents love acpx! They hate having to scrape characters from a PTY session"* — *"so AI agents and orchestrators can talk to coding agents over a structured protocol"* — [README](https://github.com/openclaw/acpx) |
| **Agent-specific primitive** | Persistent multi-turn sessions per repo; named sessions for parallel workstreams; prompt queueing with fire-and-forget; cooperative `session/cancel`; structured ACP output. No human-facing equivalent — a human would use a terminal directly |
| **Autonomy-compatible control plane** | Fire-and-forget (`--no-wait`), queue owner TTL, graceful cancel on interrupt; agents operate without per-action human confirmation |
| **M2M integration surface** | CLI as primary interface. Agents invoke via `npx acpx` or `acpx`; config via JSON files; SKILL.md for machine-readable onboarding |
| **Identity / delegation** | Sessions scoped per repo/cwd; named sessions isolate parallel workstreams; session state persisted in `~/.acpx/` with per-session isolation |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Persistent Sessions** | Multi-turn conversations that survive across invocations, scoped per repo |
| **Named Sessions** | Parallel workstreams in the same repo (`-s backend`, `-s frontend`) |
| **Prompt Queueing** | Submit prompts while one is running; they execute in order |
| **Fire-and-Forget** | `--no-wait` queues a prompt and returns immediately |
| **Cooperative Cancel** | `cancel` sends ACP `session/cancel` via queue IPC; `Ctrl+C` does graceful cancel before force-kill |
| **Structured Output** | Typed ACP messages (thinking, tool calls, diffs) instead of ANSI scraping |
| **One-Shot Mode** | `exec` for stateless fire-and-forget tasks |
| **Session Controls** | `set-mode`, `set <key> <value>` for `session/set_mode` and `session/set_config_option` |
| **Agent Registry** | Built-in support for Pi, OpenClaw, Codex, Claude, Gemini, Cursor, Copilot; `--agent` escape hatch for custom servers |

---

## Autonomy Model

```
Orchestrator agent installs acpx or uses npx acpx@latest
    ↓
Agent creates session (explicit or implicit via directory-walk)
    ↓
Agent submits prompt via acpx codex "fix the tests"
    ↓
acpx spawns ACP-compatible coding agent (Codex, Claude, etc.)
    ↓
Structured ACP messages stream back (thinking, tool calls, diffs)
    ↓
Agent parses output; no PTY scraping required
    ↓
Optional: agent queues follow-up with --no-wait; or cancels with acpx cancel
    ↓
Session persists across invocations; agent can resume later
```

---

## Identity and Delegation Model

- Sessions are scoped per repository (cwd). Each agent run gets its own session context.
- Named sessions (`-s <name>`) allow parallel workstreams with isolated state.
- Session state stored in `~/.acpx/` with per-session isolation.
- ACP `authenticate` handshake supports env/config credentials for delegated access.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `acpx` — primary interface; agents invoke via subprocess |
| Config | JSON config files: global + project merge; `acpx config show|init` |
| Skill | `npx acpx@latest --skill install acpx` — installs SKILL.md for agent reference |
| Protocol | Implements [Agent Client Protocol (ACP)](https://agentclientprotocol.com) |

---

## Human-in-the-Loop Support

Not required. Agents operate fully autonomously. acpx is designed for agent-to-agent delegation; no human approval gates in the protocol. Optional: human can inspect session history via `acpx sessions history`.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw PTY / terminal** | Unstructured ANSI output; agents must scrape; no session semantics, no cooperative cancel, no typed messages |
| **Generic subprocess** | No persistent sessions, no prompt queueing, no ACP protocol; output is unstructured |
| **IDE extensions** | Human-facing; require GUI; not designed for agent orchestration or M2M delegation |

---

## Use Cases

- **Orchestrator-to-coding-agent delegation** — a planning agent delegates coding tasks to Codex/Claude via acpx without PTY scraping
- **Parallel workstreams** — named sessions allow one agent to run `-s api` and `-s docs` concurrently
- **Fire-and-forget pipelines** — queue prompts with `--no-wait` for long-running tasks; agent returns immediately
- **Structured output consumption** — agents parse typed ACP messages (thinking, tool calls) instead of ANSI
- **Multi-agent coding workflows** — Pi, OpenClaw, Codex, Claude, and other ACP agents share one CLI surface
