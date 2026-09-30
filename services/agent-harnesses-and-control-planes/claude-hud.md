# Claude HUD

> **"A Claude Code plugin that shows what's happening"**

| | |
|---|---|
| **Website** | https://github.com/jarrodwatts/claude-hud |
| **Docs** | https://github.com/jarrodwatts/claude-hud#readme |
| **GitHub** | https://github.com/jarrodwatts/claude-hud |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=social)](https://github.com/jarrodwatts/claude-hud) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | MIT |
| **Latest-month signal** | [v0.8.0](https://github.com/jarrodwatts/claude-hud/releases/tag/v0.8.0) released 2026-08-18; last GitHub push 2026-09-26; 28,233 stars; MIT; `.claude-plugin/marketplace.json` still present (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

No separate website. The official home is:

https://github.com/jarrodwatts/claude-hud

---

## Official Repo

https://github.com/jarrodwatts/claude-hud

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Claude Code plugin` + **status-line protocol**

Inside Claude Code:

```text
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud
/reload-plugins
/claude-hud:setup
```

CLI equivalent:

```bash
claude plugin marketplace add jarrodwatts/claude-hud
claude plugin install claude-hud@claude-hud
```

Then run `/reload-plugins` and `/claude-hud:setup` in the session. The HUD uses Claude Code's native statusline API (stdin JSON in, stdout rendered). It also reads the session transcript JSONL for tools, agents, and todos.

---

## Agent Skills

**Status:** ⚠️ Plugin commands, not a portable `SKILL.md` package

The plugin exposes `/claude-hud:setup` and `/claude-hud:configure`. That is Claude Code plugin UX, not `npx skills add`.

Search community skills: `npx clawhub@latest search claude-hud`. See: https://agentskills.io/specification

---

## MCP

**Status:** ⚠️ No MCP server

Claude HUD can *display* configured MCP/Skills in the status line when those elements are enabled. It does not publish MCP tools or proxy MCP calls.

---

## What It Does

Claude HUD is a purpose-built operator surface for a live Claude Code session. It renders model/provider, project/git, context-window fill, usage/rate-limit windows, and optional lines for in-flight tools, subagents, and todos. It is read-only observation: it does not enqueue work, approve tools, or mint credentials.

This is the same class of surface as the catalog's Codex HUD entries, admitted on the **operator-surface track**.

---

## Why It Is Agent-Native

Operator-surface track (not the standard five infrastructure criteria):

| Requirement | Evidence |
|---|---|
| **Agent-operations-first** | README: **"A Claude Code plugin that shows what's happening — context usage, active tools, running agents, and todo progress."** — [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) |
| **Agent-specific live state** | Native token/context data from Claude Code, plus transcript-parsed tool activity, subagent lines, todos, Skills/MCP display, usage windows |
| **Session attribution** | State is the current Claude Code session (model, project, git, transcript). Not host CPU charts |
| **Dedicated operational surface** | Statusline command protocol: Claude Code → stdin JSON → `claude-hud` → stdout in the terminal |
| **Honest boundary** | Observation only. No autonomy, no approval enforcement, no delegated credentials, no MCP server, no portable Agent Skill package |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Context health bar** | Live context-window fill from Claude Code (including 1M-context sessions) |
| **Usage window** | Rate-limit / usage bar from native session data |
| **Tool activity line** | In-progress and recent Read/Edit/Grep-style activity from the transcript |
| **Agent / subagent line** | Running subagents with model and elapsed time |
| **Todo line** | Current todo progress when enabled |

---

## Autonomy Model

```
Operator installs the plugin and runs /claude-hud:setup
    -> Claude Code invokes the statusline after interactions
    -> HUD reads stdin JSON + transcript JSONL
    -> terminal shows session state
    -> no enqueue, cancel, or approval actions
```

There is no autonomous control loop. The Claude Code agent continues as usual; the HUD only renders.

---

## Identity and Delegation Model

- **Session identity:** The active Claude Code session and its transcript.
- **No delegated authority:** Display is not permission to act.
- **Config:** `~/.claude/plugins/claude-hud/config.json` or `$CLAUDE_CONFIG_DIR/claude-hud.json` overlays.
- **MCP/Skills:** Shown when configured; not controlled by the HUD.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Plugin | `/plugin marketplace add jarrodwatts/claude-hud` |
| Statusline | stdin JSON → stdout render; 300ms debounce |
| Transcript | JSONL for tools, agents, todos |
| Configure | `/claude-hud:configure` or edit config JSON |

---

## Human-in-the-Loop Support

The HUD *is* the human operator surface. It does not implement approval gates. Permission changes in Claude Code can trigger a re-render; the HUD does not decide them.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Generic terminal theme** | Colors a shell; does not interpret Claude Code context, tools, or subagents |
| **Process monitor** | Host CPU/RAM, not a concrete agent session transcript |
| **IDE activity panel** | File-save telemetry, not Claude Code statusline + JSONL agent state |

---

## Use Cases

- **Watch context pressure** — see fill before a compact is forced
- **Follow tool/subagent work** — optional activity lines during a long turn
- **Multi-directory Claude configs** — per-directory `claude-hud.json` overlays
- **Codex cousins** — same operator-surface idea as the catalog Codex HUD entries, for Claude Code
