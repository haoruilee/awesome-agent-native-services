# ego lite

> **"The fastest browser for AI agents to run browser automation"**

| | |
|---|---|
| **Website** | https://lite.ego.app |
| **Docs** | https://lite.ego.app/document/ |
| **GitHub** | https://github.com/citrolabs/ego-lite |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/citrolabs/ego-lite?style=social)](https://github.com/citrolabs/ego-lite) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **License** | MIT (skill, `ego-browser` CLI package and docs in the repo; the desktop browser itself ships as a free binary) |
| **Latest-month signal** | [v2.1.0](https://github.com/citrolabs/ego-lite/releases/tag/v2.1.0) released 2026-10-16; Windows installer added to the README on 2026-10-19 and the [Windows .exe](https://cdn.ego.app/setup/windows/x64/egoliteSetup-Y7MbxKIuhzFB.exe) returns HTTP 200; last GitHub push 2026-10-23; [lite.ego.app](https://lite.ego.app) HTTP 200 (verified 2026-10-25) |
| **Verified at** | 2026-10-25 |

---

## Official Website

https://lite.ego.app

---

## Official Repo

https://github.com/citrolabs/ego-lite — the `ego-browser` Agent Skill (`skills/ego-browser/`), the `ego-browser` CLI package (`package/ego-browser/`), Claude/Codex plugin manifests and docs. The Chromium-based desktop app is distributed as a download from `cdn.ego.app`; its browser source is not in this repo.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** local desktop browser + Agent Skill / CLI

**Quickest verified path:**

```bash
npx skills add citrolabs/ego-lite
```

On the first browser task the skill walks the person through installing the app. The app can also be installed directly: macOS ([Apple Silicon](https://cdn.ego.app/setup/macos/arm64/egolite-Y7MbxKIuhzFB.dmg), [Intel](https://cdn.ego.app/setup/macos/x64/egolite-Y7MbxKIuhzFB.dmg)) or [Windows x64](https://cdn.ego.app/setup/windows/x64/egoliteSetup-Y7MbxKIuhzFB.exe); installing the app adds the `ego-browser` skill to every agent's skills directory on the machine. Linux is on the [roadmap](https://lite.ego.app/roadmap).

On first launch the person can migrate their Chrome data so the agent inherits existing logins, cookies and extensions. This is a one-time human setup; the browser runs on the person's computer, so a hosted agent cannot reach it unless it runs on the same machine. No account or API key is needed.

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add citrolabs/ego-lite
```

| Skill | What It Teaches the Agent |
|---|---|
| `ego-browser` | Run `ego-browser skill` to print the version-matched usage guide, then drive pages with snapshot, fill, click, wait, navigate and capture tools in the agent's own Space |

---

## MCP

**Status:** ⚠️ No MCP server

ego lite does not publish an MCP server. Agents drive it through the `ego-browser` Agent Skill and CLI instead.

---

## What It Does

ego lite is a Chromium-based browser that a person and their AI agents share. Each agent (Claude Code, Codex, Cursor or a custom CLI agent) works in its own isolated Space inside the browser while the person keeps browsing in theirs. The agent reads pages as structured Snapshots and writes a JavaScript snippet that calls the browser tools in one pass, instead of a command-by-command CLI loop.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | GitHub description: *"The fastest browser for AI agents to run browser automation, built for sharing your logged-in browser state with your AI agents, like Codex or Claude Code, without disturbing you."*; https://github.com/citrolabs/ego-lite |
| **Agent-specific primitive** | Per-agent Spaces (isolated workspaces in the same browser), engine-level page Snapshots that handle nested iframes, and code-based tool calls (`snapshot`, `fill`, `click`, `wait`, `navigate`, `capture`) composed into one JavaScript run |
| **Autonomy-compatible control plane** | After the one-time install the agent runs full browser tasks without the person clicking; the person can see which Space has an agent running and take over or stop it |
| **M2M integration surface** | `ego-browser` CLI and Agent Skill, callable from any agent CLI; Claude Code and Codex plugin manifests in the repo |
| **Identity / delegation** | The agent acts inside the person's signed-in browser profile (optionally migrated from Chrome); browsing data stays on the device. Local delegation only, not a separate agent web identity |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent Spaces** | Each agent or task gets its own Space, so several agents run in parallel without touching the person's tabs |
| **Snapshot** | The page turned into structured text for text-only models |
| **Code-based actions** | In-page JavaScript tools the agent composes into a single multi-step snippet |
| **Shared logins** | Agents reuse the person's cookies and sessions, which also means fewer CAPTCHAs |

---

## Autonomy Model

```
Person installs ego lite (or the skill installs it on first use), optionally migrating Chrome data
    ↓
Agent loads the ego-browser skill and runs `ego-browser skill` for the version-matched guide
    ↓
Agent opens its own Space in the browser
    ↓
Agent reads the page as a Snapshot
    ↓
Agent writes one JavaScript snippet calling snapshot / fill / click / wait / navigate / capture
    ↓
ego-browser runs it on the page and returns results; the agent repeats or reports back
```

Several agents can run at once, each in its own Space, while the person keeps browsing.

---

## Identity and Delegation Model

- **Agent identity** — no separate web identity; each agent works in its own Space inside the person's browser.
- **Delegated scope** — Spaces keep agents out of the person's tabs and out of each other's work.
- **Acting as the person** — websites see the person's own signed-in session (cookies can be migrated from Chrome).
- **Data** — browsing data stays on the device; telemetry is limited to simple product signals per the README.
- **Boundary** — local delegation on one computer, not a cryptographic or cloud-issued agent identity.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Agent Skill | `skills/ego-browser/SKILL.md`, installed with `npx skills add citrolabs/ego-lite` or by the app |
| CLI | `ego-browser skill`, `ego-browser upgrade` and the in-page tool runner (`package/ego-browser/`) |
| Plugins | Claude Code (`.claude-plugin/`) and Codex (`.codex/`) manifests in the repo |
| Desktop app | Chromium-based browser for macOS (Apple Silicon, Intel) and Windows x64 |

---

## Human-in-the-Loop Support

The person installs the app and chooses whether to migrate Chrome data. They can watch any agent's Space and take it over or stop it at any time.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Puppeteer / Playwright scripts** | Libraries for people writing automation code, usually against a fresh profile with no logins |
| **Browser extensions driving the person's own tabs** | Agent and person fight over the same tabs; no isolated workspace per agent |

Playwright MCP, FSB and hosted browsers such as Browserbase are valid agent browser models with their own entries. ego lite's difference is a dedicated desktop browser where agents get their own Spaces next to the person's signed-in session.

---

## Use Cases

- **Signed-in sites** — let Claude Code or Codex act on dashboards and accounts the person is already logged into.
- **Parallel research** — run several agents in separate Spaces, e.g. enriching leads or comparing competitor sites.
- **Web app QA** — dogfood and test web apps with structured snapshots and screenshots.
