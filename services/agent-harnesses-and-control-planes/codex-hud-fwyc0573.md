# Codex HUD (fwyc0573)

> **"Real-time statusline HUD for OpenAI Codex CLI. Lightweight, zero-config, works inside tmux."**

| | |
|---|---|
| **Website** | https://github.com/fwyc0573/codex-hud |
| **Docs** | https://github.com/fwyc0573/codex-hud#readme |
| **GitHub** | https://github.com/fwyc0573/codex-hud |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/fwyc0573/codex-hud?style=social)](https://github.com/fwyc0573/codex-hud) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | MIT in `package.json`; no root `LICENSE` file as of 2026-09-26 |
| **Latest-month signal** | [v1.2](https://github.com/fwyc0573/codex-hud/releases/tag/v1.2) released 2026-09-01; 79 stars; last push 2026-09-06; `package.json` license is MIT and there is still no root `LICENSE` file ([repo metadata](https://api.github.com/repos/fwyc0573/codex-hud)) |
| **Verified at** | 2026-09-26 |

---

## Official Website

No separate website is published; the official GitHub repository is the project home:

https://github.com/fwyc0573/codex-hud

---

## Official Repo

https://github.com/fwyc0573/codex-hud

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Codex wrapper CLI + tmux operator surface`

The upstream README explicitly supports one-prompt installation by an agent:

```text
Install codex-hud (https://github.com/fwyc0573/codex-hud) for the Codex CLI by following the instructions in its README.md.
```

The direct macOS/Linux path is:

```bash
git clone https://github.com/fwyc0573/codex-hud.git
cd codex-hud
git switch main
./bin/codex-hud-install

# Refresh the shell, then launch the wrapper.
codex
```

It requires an existing Codex CLI and Node.js 18+; the installer also uses or offers to install tmux. Review it before running because it installs shell wrappers/aliases and manages local tmux sessions.

---

## Agent Skills

**Status:** ⚠️ Not published

The repository does not include a standard `SKILL.md`. Its natural-language install prompt is convenient agent onboarding, but is not an Agent Skills package.

Search community skills with `npx clawhub@latest search codex-hud`, or contribute one using the [Agent Skills specification](https://agentskills.io/specification).

---

## MCP

**Status:** ⚠️ No MCP server

Codex HUD reads the effective Codex configuration and rollout activity to display configured MCP servers and tool calls. It does not publish MCP tools, proxy MCP requests, or act as an MCP client/server control plane.

---

## What It Does

Codex HUD launches Codex inside a managed tmux layout and renders a persistent terminal surface for model and reasoning effort, context fill, token counts, project/git state, session identity, configured extensions/Skills/hooks/instructions, approval and sandbox state, MCP/tool activity, and direct-child/subagent activity. A multi-session view aggregates active root sessions; typed agent paths preserve the visible subagent tree.

Its wrapper also provides bounded session operations: list, attach, create, diagnose, resume, or kill HUD-owned sessions. It observes Codex rather than replacing its reasoning or permission system, and it does not claim to authorize tool calls merely because it displays their state.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Upstream describes it as a **"Real-time statusline HUD for OpenAI Codex CLI"** and installs it around the Codex command — [README](https://github.com/fwyc0573/codex-hud#readme) |
| **Agent-specific primitive** | It interprets Codex rollout/session identity, context pressure, effective approval/sandbox state, MCP/tools, Skills/hooks, compactions, and typed subagent paths rather than generic process metrics |
| **Autonomy-compatible control plane** | The HUD can remain attached while Codex works and can list/attach/kill its tmux sessions, but it does not plan, approve, retry, or execute agent work; Codex retains its own autonomy and permission boundaries |
| **M2M integration surface** | Shell wrapper/management CLI plus machine-readable Codex config and rollout JSONL inputs; terminal output is operator-oriented and there is no HTTP API, SDK, or MCP server |
| **Identity / delegation** | Root session IDs, cwd-scoped tmux sessions, and typed child-agent paths attribute activity. It displays effective permissions but mints no identity, credential, lease, or delegated authority |

This entry qualifies under the category's explicit operator-surface track, not by pretending a read-only HUD is a full orchestration control plane.

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Live Codex HUD** | Fixed terminal rows for context, tokens, environment, session, tools, and agent activity |
| **Root-session view** | Cwd, Codex session ID, CLI version, elapsed time, model, and git state |
| **Subagent tree** | Direct-child rows and descendant counts derived from typed agent paths |
| **Multi-session overview** | Toggleable view of active root Codex sessions and context usage |
| **Effective-policy display** | Live approval, sandbox, service tier, MCP, Skill, hook, and instruction-file state |
| **tmux lifecycle commands** | `--list`, `--attach`, `--new-session`, `--kill`, and `--self-check` around HUD-owned sessions |

---

## Autonomy Model

```text
Wrapper launches an ordinary Codex CLI session in a managed tmux pane
    -> HUD reads Codex config and rollout/session records
    -> display refreshes context, tools, subagents, and effective policy
    -> Codex continues under its own approvals, sandbox, and agent loop
    -> operator may observe, attach, detach, resume, diagnose, or kill the session
```

The observer itself has no autonomous decision loop. Killing, attaching, and accepting an offered update remain explicit operator actions.

---

## Identity and Delegation Model

- **Root identity:** The displayed Codex session ID and working directory identify each root session.
- **Child attribution:** Typed agent paths associate visible direct children and descendant counts with their owning root session.
- **Local session scope:** Project-readable tmux names and checkout-scoped local state distinguish concurrently running sessions.
- **Permission boundary:** Approval and sandbox modes are read from Codex runtime state and displayed; the HUD neither grants nor enforces them.
- **No credential delegation:** The project does not mint service identities, proxy credentials, or delegate authority between agents.
- **Operational audit:** Rollout records and local HUD state support inspection, but the display is not a cryptographic audit log.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Wrapper CLI | `codex`, `cx`, `codex-resume`, and passthrough Codex arguments |
| Management CLI | `codex-hud --list|--attach|--new-session|--kill|--self-check` plus sync/upgrade/uninstall helpers |
| Codex inputs | Local `config.toml`, rollout/session JSONL, instruction/Skill/hook configuration, and git state |
| Terminal surface | tmux status pane with single-session and multi-session modes |
| Local state | Update/session state and logs under the XDG state directory or `~/.local/state/codex-hud/` |

There is no REST API, language SDK, or MCP transport.

---

## Human-in-the-Loop Support

The operator surface is the human-in-the-loop mechanism: it makes context pressure, current tools/subagents, and the effective security posture visible while Codex runs. Operators can attach, detach, resume, diagnose, or stop a session. `--kill` terminates the matching HUD-owned tmux session, so session identity should be checked first. Permission changes still occur through Codex, not the HUD.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Plain tmux status bar** | Can show processes and host metrics but does not interpret Codex rollout identity, context use, tools, Skills, permissions, or subagent paths |
| **Generic terminal dashboard** | Is not bound to Codex sessions and cannot distinguish root sessions from typed child-agent activity |
| **Raw rollout-log tail** | Exposes events but does not maintain the managed session view, context summaries, or attach/list/kill workflow |

---

## Use Cases

- **Long Codex sessions** — see context pressure, compactions, tokens, and current tool activity without interrupting the agent
- **Parallel work** — compare active root sessions and attach to the correct project-scoped tmux session
- **Subagent supervision** — inspect direct children and active descendant counts under the owning root
- **Security posture checks** — keep effective approval, sandbox, service tier, MCP, Skill, and hook state visible
- **Recoverable terminal operation** — detach from a live Codex session, reattach later, or stop the correct HUD-owned session
