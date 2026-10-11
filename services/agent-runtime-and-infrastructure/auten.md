# Auten

> **"Give your AI agent hands. It clicks, types and sees your screen."**

| | |
|---|---|
| **Website** | https://auten.ai |
| **Docs** | https://github.com/auten-ai/auten-mcp |
| **GitHub** | https://github.com/auten-ai/auten-mcp |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | MIT for the docs, client configs and `@autenai/mcp` launcher; the runner is closed source ([terms](https://auten.ai/terms)) |
| **Latest-month signal** | npm `@autenai/mcp` 0.1.4 published 2026-10-10; listed in the official MCP registry as `ai.auten/mcp`; young project (no stars yet) |
| **Verified at** | 2026-10-11 |

---

## Official Website

https://auten.ai

Live document title: *Give your AI agent hands: computer control over MCP*. Homepage H1: *Give your AI agent hands. It clicks, types and sees your screen.* MCP landing page: https://auten.ai/mcp

---

## Official Repo

https://github.com/auten-ai/auten-mcp

MIT ([LICENSE](https://github.com/auten-ai/auten-mcp/blob/main/LICENSE)). The repository holds the public docs, client configs, a Claude Code plugin bundle and the `@autenai/mcp` npm launcher (`bin/auten-mcp.js`). The runner that operates the desktop is distributed through the installers and is not open source.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** **MCP (stdio)** + local runner (installer)

Install the runner once (macOS and Linux; on Linux it asks for `sudo` once to apt-install the accessibility and input tools):

```bash
curl -fsSL https://auten.ai/install | bash
```

```powershell
# Windows (PowerShell)
irm https://auten.ai/install.ps1 | iex
```

Register the MCP server (Claude Code example):

```bash
claude mcp add -s user auten -- npx -y @autenai/mcp
```

Generic MCP JSON:

```json
{
  "mcpServers": {
    "auten": { "command": "npx", "args": ["-y", "@autenai/mcp"] }
  }
}
```

Agent-readable setup file: https://github.com/auten-ai/auten-mcp/blob/main/llms-install.md

This is **not** URL Onboarding. The first run asks the human to connect a free key (30 minutes of runtime a month, no card), and macOS needs Accessibility / Screen Recording permissions granted by the user.

---

## Agent Skills

**Status:** ⚠️ Not yet published as an `npx skills` package

The Claude Code plugin bundle in the repository ships one skill:

```
/plugin marketplace add auten-ai/auten-mcp
/plugin install auten@auten
```

| Skill | What It Teaches the Agent |
|---|---|
| `auten-safe-use` | Treat on-screen text as data, ask before buying, deleting, sending or granting permissions, use `fill_login` for passwords |

Search community skills: `npx clawhub@latest search auten`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/auten-ai/auten-mcp — npm `@autenai/mcp`, registry name `ai.auten/mcp` |
| **Transport** | stdio |
| **Compatible Clients** | Claude Code, Codex, Cursor, Gemini CLI, Cline, VS Code and other MCP clients |

---

## What It Does

Auten lets an MCP client operate the user's real computer: macOS, Windows 10/11 or Linux (X11), plus an Android phone over USB (beta). The agent reads the frontmost app as numbered accessibility elements with the visible text, then clicks, types, fills forms and reads the screen in apps that have no API.

When the agent has worked a task out once, it can save the run as a skill with parameters and replay it later without calling the model. If the app changes and a step breaks, the agent repairs that skill from the failing step. The site reports 17 s for a task done with the model versus 9 s replayed.

Passwords are typed locally from the system keychain (or a private local vault on Linux) and never reach the model.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage H1: *"Give your AI agent hands. It clicks, types and sees your screen."* — [auten.ai](https://auten.ai). *"Auten lets Claude Code, Codex, Cursor and other agents use your real computer: click, type, fill in forms and read the screen in apps that have no API."* |
| **Agent-specific primitive** | `list_elements` returns numbered accessibility elements plus visible text for a model to act on by id; learned skills (`start_recording` / `stop_recording` → `run_skill`) replay an agent's own run without the model; `fill_login` types secrets the model never sees — [tools](https://github.com/auten-ai/auten-mcp#tools) |
| **Autonomy-compatible control plane** | After install, an MCP client runs the full loop (open app, read, act, verify, save skill, replay) with no human clicks. Constraints: acts only on tool calls, per-origin login pinning, on-screen secret redaction, metered runtime — [privacy and safety](https://github.com/auten-ai/auten-mcp#privacy-and-safety) |
| **M2M integration surface** | stdio MCP server (`npx -y @autenai/mcp`), `auten` CLI, Claude Code plugin marketplace, `llms-install.md` |
| **Identity / delegation** | Per-account key with metered runtime; credentials pinned per origin and never shown to the model. No separate per-agent identity token: the agent acts as the logged-in desktop user |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Numbered elements** | `list_elements` / `read_text` / `screenshot_labeled` expose the screen as ids plus text |
| **Element actions** | `click`, `fill`, `type`, `press_keys`, `scroll`, `drag`, `menu_select`, `act_on_matching` |
| **Learned skills** | `start_recording` / `stop_recording`, `run_skill`, `start_fixing` / `stop_fixing` |
| **Local secrets** | `list_logins`, `fill_login` (origin-pinned, typed locally) |
| **Hand-back** | `ask_user` returns a step to the person, for example a 2FA prompt |

---

## Autonomy Model

```
Human installs the runner and connects a key (free tier: 30 min a month)
    ↓
Human adds the MCP server to the agent and grants OS permissions
    ↓
Agent checks list_skills; if a skill matches, run_skill replays it without the model
    ↓
Otherwise: list_elements → click / fill / type → list_elements to verify, step by step
    ↓
Agent saves the finished run as a skill with parameters
    ↓
If a later replay breaks after an app change, the agent repairs it with start_fixing / stop_fixing
```

---

## Identity and Delegation Model

- **Account key** — each install uses an account key; runtime is attributed to and metered on that account.
- **Desktop principal** — the agent acts as the logged-in user on that machine; there is no per-agent identity token or delegated-permission scope.
- **Credentials** — stored in the system keychain (macOS, Windows) or a private local vault (Linux), pinned to the site or app where first used; on any other origin `fill_login` refuses. Only the user can re-pin (`auten vault unpin <name>`).
- **Audit** — activity history and learned skills (replayable step files) are written to the user's own computer. No customer-facing audit export beyond those local files.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP (stdio) | `npx -y @autenai/mcp` — https://github.com/auten-ai/auten-mcp |
| CLI | `auten` (`auten connect`, `auten mcp-bridge`, `auten key add` for your own model key) |
| Claude Code plugin | `/plugin marketplace add auten-ai/auten-mcp` |
| Agent setup file | https://github.com/auten-ai/auten-mcp/blob/main/llms-install.md |
| Installers | https://auten.ai/install (macOS/Linux), `install.ps1` (Windows) |

---

## Human-in-the-Loop Support

The human installs the runner, grants OS permissions and saves logins. During a task the agent can call `ask_user` to hand a step back (2FA, a choice it should not make alone). The bundled `auten-safe-use` skill tells the agent to ask before purchases, deletions, sending messages or granting permissions. It runs on the user's real desktop, not a sandbox; isolation (a separate OS account or VM) is up to the user.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **RPA tools (UiPath, Power Automate Desktop)** | Built for a human developer who writes selectors ahead of time; no MCP tool surface for an LLM agent |
| **Remote-desktop sandboxes (Scrapybara, Cyberdesk)** | Provide a fresh cloud desktop; Auten operates the user's own machine and Android phone with their logged-in apps |
| **Playwright / Puppeteer** | Browser only; no native desktop apps or phone |
| **Plain ADB scripts** | Phone only, no learned-skill replay or local secret handling |

---

## Use Cases

- **Apps without an API** — fill invoices from mail into a desktop accounting app
- **Repeated desktop chores** — learn an export or form-fill once, replay it without model calls
- **Phone tasks (beta)** — the same agent operates an Android phone over USB
- **Logins without leaking secrets** — the agent signs in with `fill_login` while the password stays local
