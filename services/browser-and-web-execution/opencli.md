# OpenCLI

> **"Make any website, Electron App, or Local Tool your CLI."**

| | |
|---|---|
| **Website** | https://opencli.info/ |
| **Docs** | https://github.com/jackwener/opencli/blob/main/README.md |
| **GitHub** | https://github.com/jackwener/opencli |
| **npm** | https://www.npmjs.com/package/@jackwener/opencli |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **License** | Apache-2.0 |

---

## Official Website

https://opencli.info/

---

## Official Repo

https://github.com/jackwener/opencli

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI (Bash) + optional repo SKILL.md`

```bash
npm install -g @jackwener/opencli

# Discover every site command and external CLI passthrough
opencli list
opencli list -f yaml

# Example: structured output for agents
opencli hackernews top --limit 5 -f json
opencli bilibili hot --limit 5 -f json
```

Browser-backed commands need **Chrome running**, the **opencli Browser Bridge** extension (see [README](https://github.com/jackwener/opencli/blob/main/README.md)), and an active login in Chrome for the target site. Point agents at the machine-readable command reference:

```
Read https://raw.githubusercontent.com/jackwener/opencli/main/SKILL.md for command patterns, adapter workflow, and output formats.
```

Optional: add to global `AGENT.md` or `.cursorrules` so the agent runs `opencli list` via Bash to discover tools, as described in the [README](https://github.com/jackwener/opencli/blob/main/README.md).

---

## Agent Skills

**Status:** ✅ Published in the upstream repository (AgentSkills-style front matter)

The project ships [SKILL.md](https://raw.githubusercontent.com/jackwener/opencli/main/SKILL.md) with install steps, 150+ command examples, YAML pipeline templates, and the `explore` / `synthesize` / `generate` / `cascade` adapter workflow for agents extending the tool.

```bash
# Reference (read in browser or fetch raw)
# https://raw.githubusercontent.com/jackwener/opencli/main/SKILL.md
```

Adapter development requires reading [CLI-EXPLORER.md](https://raw.githubusercontent.com/jackwener/opencli/main/CLI-EXPLORER.md) first — called out inside `SKILL.md`.

---

## MCP

**Status:** ⚠️ Not applicable as **Model Context Protocol** — OpenCLI is a **CLI** and local browser bridge. (The codebase uses an internal `BrowserBridge` type historically aliased in `mcp.ts`; it is not an MCP server.)

Agents integrate by invoking `opencli` as a subprocess and consuming `json` / `yaml` / `md` / `csv` output (`-f` / `--format`).

---

## What It Does

OpenCLI turns websites, **Electron desktop apps** (e.g. Cursor, Codex, Notion, Discord), and **local binaries** into a **unified CLI** with structured output. A Chrome extension plus localhost daemon reuses the user’s real browser session for authenticated sites; public API sites can run without the bridge. It also **passthroughs** external CLIs (`gh`, `docker`, `kubectl`, etc.) and lets users **`opencli register`** custom local tools so `opencli list` exposes one discovery surface for an agent.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"**Built for AI Agents**: Simply configure an instruction in your global `AGENT.md` or `.cursorrules` guiding the AI to execute `opencli list` via Bash"* — [README](https://raw.githubusercontent.com/jackwener/opencli/main/README.md). Chinese README: *"专为 AI Agent 打造"* — [README.zh-CN](https://raw.githubusercontent.com/jackwener/opencli/main/README.zh-CN.md) |
| **Agent-specific primitive** | **Session-reuse bridge** — commands execute in the user’s logged-in Chrome or attached Electron/CDP context without the agent handling credentials; plus **machine-readable registry** (`opencli list -f yaml`) and **AI-driven adapter synthesis** (`explore`, `synthesize`, `generate`, `cascade`) aimed at agents building new commands |
| **Autonomy-compatible control plane** | After one-time extension setup on the workstation, agents run `opencli …` headlessly with structured flags; `opencli doctor` auto-starts the daemon |
| **M2M integration surface** | Global CLI (`@jackwener/opencli`), `exports` entry `./registry` for programmatic use, JSON/YAML/MD/CSV outputs, published `SKILL.md` |
| **Identity / delegation** | Actions run **as the human’s existing browser or desktop app session** (cookies, logged-in tabs, Electron CDP) — same delegation pattern as other “your browser is the API” tools: the user delegates their session to the agent process on that machine |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Browser Bridge** | Chrome extension + daemon (default port `19825`) connecting CLI to live browser pages |
| **Site / app adapters** | Declarative YAML pipelines or TypeScript adapters under `clis/` with strategies from public API through cookie, intercept, and UI automation |
| **External CLI hub** | `opencli gh …`, `opencli docker …`, auto-install when missing, unified discovery |
| **`opencli register`** | Register arbitrary local CLIs into the same registry agents see via `opencli list` |
| **Adapter AI workflow** | `explore` → `synthesize` → `generate` / `cascade` for generating new command definitions |
| **Structured output** | `-f json|yaml|md|csv|table` on commands and on `list` |

---

## Autonomy Model

```
Agent (or human) installs Chrome extension + npm global package once
    ↓
Agent runs opencli list -f yaml → discovers sites + external CLIs
    ↓
Agent invokes opencli <site> <cmd> -f json
    ↓
CLI talks to daemon → browser/Electron executes with existing login
    ↓
Structured stdout returned to agent context
    ↓
(Optional) Agent extends catalog via explore/synthesize or new YAML in clis/
```

---

## Identity and Delegation Model

- **Browser / Electron path:** The agent does not receive raw passwords; it inherits **session state already present** in Chrome or the target desktop app on that host.
- **Scope:** All bridge traffic is **local** (localhost daemon); credentials stay in the browser/app per project docs.
- **Custom tools:** Registered CLIs run as the **OS user** invoking `opencli`, with that user’s environment and permissions.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `opencli` — primary agent integration |
| npm | `npm install -g @jackwener/opencli` |
| Module | `import … from '@jackwener/opencli/registry'` (see package `exports`) |
| HTTP (local) | Daemon status/logs on configurable port (default `19825`) — operational, not the main agent API |
| Docs | `SKILL.md`, `CLI-EXPLORER.md`, `CLI-ONESHOT.md` in repo |

---

## Human-in-the-Loop Support

Initial setup is human-driven: install Node 20+, load the Browser Bridge extension, log into sites in Chrome. Ongoing runs do not require per-command human clicks. Desktop app adapters may require the target app to be installed and running.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw Playwright/Puppeteer in CI** | Does not reuse the user’s **existing** interactive Chrome login; different trust and setup model |
| **Per-site official APIs** | Incomplete coverage; OpenCLI targets sites and apps **without** a single public API surface |
| **bb-browser** | Sibling pattern (Chrome session + agent CLI); OpenCLI adds **Electron/CDP desktop adapters**, **YAML pipeline** authoring, **external CLI hub**, and **explore/synthesize** tooling — different breadth and adapter workflow |

---

## Use Cases

- **Research / social / media agents** — fetch timelines, search, and exports as JSON from logged-in sites
- **Desktop-copilot agents** — drive Cursor, Codex, Antigravity, Notion, Discord from structured CLI
- **Tooling consolidation** — one `opencli list` registry for site adapters plus `gh`, `docker`, and custom binaries
