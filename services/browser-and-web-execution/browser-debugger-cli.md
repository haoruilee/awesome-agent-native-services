# bdg (Browser Debugger CLI)

> **"Give your AI agent a real browser. And the DevTools to go with it."**

| | |
|---|---|
| **Website** | https://github.com/szymdzum/browser-debugger-cli |
| **Docs** | https://github.com/szymdzum/browser-debugger-cli/wiki/For-AI-Agents |
| **GitHub** | https://github.com/szymdzum/browser-debugger-cli |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/szymdzum/browser-debugger-cli?style=social)](https://github.com/szymdzum/browser-debugger-cli) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **License** | MIT |

---

## Official Website

https://github.com/szymdzum/browser-debugger-cli

---

## Official Repo

https://github.com/szymdzum/browser-debugger-cli — Node.js CLI that keeps a Chrome/Chromium/Edge session open and exposes DevTools as shell commands

---

## How to Use (Agent Onboarding)

**Interaction pattern:** **Structured CLI** + **Agent Skill**

```bash
npm install -g browser-debugger-cli
bdg localhost:3000              # start a background browser session
bdg --help --json               # machine-readable command map for the agent
bdg cdp --search cookie         # discover raw CDP methods
bdg install-skill               # install the bdg skill for Claude Code, Codex, Gemini CLI, ...
```

---

## Agent Skills

**Status:** ✅ Ships an agent skill

| Skill | Source | What It Teaches the Agent |
|---|---|---|
| bdg | `bdg install-skill` | Start once, act, read what changed, inspect without screenshots, check network and console |

---

## MCP

**Status:** ❌ Not provided by design — the project describes itself as "no screenshots and no MCP needed"; agents call it as a shell CLI.

---

## What It Does

bdg keeps a **browser session open in the background** and lets an agent drive it **one shell command at a time**: click, fill, navigate, then read requests, console errors, layout, styles and the accessibility tree. Every DevTools capability is reachable through **raw CDP** (`bdg cdp <Method>`), with search and `--describe` introspection. Output is compact and pipes into `jq`, and semantic DOM output cuts tokens versus raw HTML.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"It is built for coding agents like Claude Code, Codex and Gemini CLI"*; wiki page [For AI Agents](https://github.com/szymdzum/browser-debugger-cli/wiki/For-AI-Agents): *"bdg is designed for autonomous AI agents."* |
| **Agent-specific primitive** | Self-describing `--help --json` with task→command mappings; "did you mean" `suggestion` fields and a dedicated exit code (81) for invalid arguments so agents fix rather than retry; token-reduced semantic DOM output |
| **Autonomy-compatible control plane** | Background session persists across commands; the agent acts and inspects without a human at the browser |
| **M2M integration surface** | Structured CLI with `--json` output and stable exit codes; raw CDP passthrough |
| **Identity / delegation** | Custom Chrome profile (`--user-data-dir`) or attach to an existing browser (`--chrome-ws-url`) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Session** | `bdg <url>` starts a background browser session; `--headless`, `--timeout` |
| **DOM / interaction** | `bdg dom …` query, get, click, fill, with semantic output |
| **Telemetry** | Network requests, console messages, performance, accessibility |
| **Raw CDP** | `bdg cdp <Domain.method> --params …`, `--list`, `--search`, `--describe` |

---

## Autonomy Model

```
Agent runs bdg <url> once
    ↓
Agent issues bdg dom / network / console / cdp commands
    ↓
Agent reads compact JSON output and exit codes, corrects mistakes from suggestions
    ↓
Session stops on command or timeout
```

---

## Identity and Delegation Model

- **Session scope:** one background browser session per `bdg` start, optionally with its own profile via `--user-data-dir`.
- **Delegation:** attaching to an existing browser (`--chrome-ws-url`) reuses that browser's logged-in state; the agent acts with whatever access that profile has.
- No separate auth layer — runs with the local user's permissions.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **CLI** | `bdg <url>`, `bdg dom …`, `bdg cdp …`, `--json` output, exit codes |
| **CDP** | Unix socket → worker → Chrome DevTools WebSocket |
| **Skill** | `bdg install-skill` |

---

## Human-in-the-Loop Support

Not required. The same CLI is usable by a developer in a terminal.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Chrome DevTools UI** | Human GUI, not callable by an agent |
| **Raw CDP scripts** | No persistent session, discovery, or agent-oriented errors |

---

## Use Cases

- **Coding agents debugging web apps** — console errors, failed requests, layout and style issues.
- **UI verification** without screenshots, using the accessibility tree and semantic DOM output.
