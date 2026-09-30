# Kernel

> **"you build agents. we give them the internet."**

| | |
|---|---|
| **Website** | https://www.kernel.sh/ |
| **Docs** | https://www.kernel.sh/docs |
| **GitHub** | https://github.com/kernel/kernel-images |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/kernel/kernel-images?style=social)](https://github.com/kernel/kernel-images) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **License** | Apache-2.0 (`kernel/kernel-images`, `kernel/cli`) |
| **Latest-month signal** | `kernel/kernel-images` last push 2026-09-29; [`kernel/cli` v0.41.0](https://github.com/kernel/cli/releases/tag/v0.41.0) released 2026-09-24 (npm `@onkernel/cli` 0.41.0); both Apache-2.0; hosted MCP server documented at [kernel.sh/docs/reference/mcp-server](https://www.kernel.sh/docs/reference/mcp-server) (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

https://www.kernel.sh/

Product documentation: https://www.kernel.sh/docs

---

## Official Repo

https://github.com/kernel/kernel-images — open-source browser images that power the hosted service

https://github.com/kernel/cli — official CLI (`@onkernel/cli`)

https://github.com/kernel/skills — official `kernel-cli` Agent Skill

The GitHub org slug is `kernel` (the `onkernel/…` paths resolve to the same org). There is no separate `onkernel/kernel` application repo as of 2026-08-19.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + **published Agent Skill**

Official docs tell a coding agent to read the Kernel CLI skill, then install and authenticate:

```bash
brew install kernel/tap/kernel
# or
npm install -g @onkernel/cli

kernel --version
export KERNEL_API_KEY=your_api_key
# fallback: kernel login
kernel browsers create -o json
```

Skill source: https://github.com/kernel/skills/blob/main/plugins/kernel-cli/skills/kernel-cli/SKILL.md

Serverless agent loops (co-located with the browser):

```bash
kernel create --template computer-use
kernel deploy agent.ts
kernel invoke my-agent my-task --payload '{"url": "https://example.com"}'
```

Self-host the images from `kernel/kernel-images` via Docker or Unikraft; CDP is on port 9222.

---

## Agent Skills

**Status:** ✅ Available

Official skill at [kernel/skills](https://github.com/kernel/skills):

| Skill | What It Teaches the Agent |
|---|---|
| `kernel-cli` | Install/auth the CLI, create browsers, run Playwright in-session, computer-use screenshots, deploy/invoke apps, manage profiles, auth, proxies, and pools |

---

## MCP

**Status:** ✅ Available (hosted remote MCP)

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/kernel/kernel-mcp-server (MIT) |
| **Endpoint** | `https://mcp.onkernel.com/mcp` |
| **Transport** | Streamable HTTP; stdio via `npx -y mcp-remote https://mcp.onkernel.com/mcp` for clients without remote MCP |
| **Auth** | OAuth 2.1 with dynamic client registration; authorization can be org-wide or limited to one Kernel project |
| **Compatible Clients** | Cursor, Claude Desktop, Claude Code (`kernel mcp install --target <target>`), and other MCP clients |
| **Docs** | https://www.kernel.sh/docs/reference/mcp-server |

Tools cover browser sessions and pools, Playwright execution, a browser REPL, computer-use actions, WebMCP, profiles, managed auth connections, and proxies (per the official `kernel-mcp` skill in [kernel/skills](https://github.com/kernel/skills)). Checked 2026-09-30; an earlier revision of this dossier wrongly said no MCP server was published.

---

## What It Does

Kernel is cloud browser infrastructure for AI agents. It spins up sandboxed Chromium (hosted unikernel images, advertised cold start under 30ms) that agents drive with Playwright, CDP, WebDriver BiDi, or computer-use actions. The platform adds stealth/CAPTCHA/proxy handling, managed auth, live view, MP4 replay, browser pools, and a serverless app platform that runs agent loops next to the browser.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: **"you build agents. we give them the internet."** Docs: **"We build crazy fast, open source infra for AI agents to access the internet."** — [kernel.sh](https://www.kernel.sh/), [docs](https://www.kernel.sh/docs) |
| **Agent-specific primitive** | Remote sandboxed Chromium plus managed auth, stealth, live view, replay, and `btel` browser telemetry so an agent can act on the web and debug failures |
| **Autonomy-compatible control plane** | `KERNEL_API_KEY` + CLI/SDK create, drive, and delete sessions without a human clicking the browser. `kernel login` is only the interactive fallback |
| **M2M integration surface** | CLI (`brew` / `npm i -g @onkernel/cli`), JSON output, Playwright execute, CDP, computer-use, deploy/invoke, official Skill |
| **Identity / delegation** | Browser sessions, optional names/tags, projects, API keys, and org concurrency limits. Managed auth keeps site credentials out of the agent transcript |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Sandboxed Chromium session** | Cloud browser the agent creates, drives, and deletes |
| **Computer-use / Playwright execute** | In-session automation and OS-level screenshot/input |
| **Managed auth** | Platform-handled login so agents do not complete site auth themselves |
| **Live view + replay** | Operator watch URL and MP4 recording |
| **Browser pools** | Pre-warmed browsers for low-latency acquire |
| **App platform** | Deploy and `invoke` an agent loop co-located with its browser |

---

## Autonomy Model

```
Agent installs CLI / reads kernel-cli skill
    -> authenticate with KERNEL_API_KEY (or human completes kernel login once)
    -> kernel browsers create -o json
    -> drive via Playwright execute, CDP, or computer-use
    -> optional live view / replay for debugging
    -> kernel browsers delete when done
    -> or deploy + invoke a long-running app on the app platform
```

---

## Identity and Delegation Model

- **Session identity:** Each browser has an ID; CLI JSON is the machine handle.
- **Project / API key:** Keys are scoped; `--project` or `KERNEL_PROJECT` selects the project.
- **Managed auth:** Site credentials stay with Kernel's auth connections, not in the LLM context.
- **No long-lived agent passport:** Kernel models browser and project identity, not a KYA token.
- **Self-host warning:** Unikraft live-view URLs in the image README are public if leaked.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `kernel browsers`, `deploy`, `invoke`, `auth`, pools, profiles, proxies |
| Agent Skill | `kernel-cli` in [kernel/skills](https://github.com/kernel/skills) |
| MCP | Hosted Streamable HTTP at `https://mcp.onkernel.com/mcp` (OAuth 2.1); source https://github.com/kernel/kernel-mcp-server |
| CDP / Playwright / BiDi | Connect to hosted or self-hosted Chromium |
| Open-source images | https://github.com/kernel/kernel-images |

---

## Human-in-the-Loop Support

Live view and MP4 replay are the operator surfaces. `kernel login` is an interactive OAuth fallback when no API key is set. Destructive CLI actions keep confirmation prompts unless the agent opts into non-interactive flags.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Local Playwright** | No hosted session isolation, managed auth, stealth, or agent-facing live view |
| **Generic cloud VM + Chrome** | Not an agent browser primitive; no pools, replay API, or managed auth |
| **Human remote-desktop** | Requires a person to operate the browser |

---

## Use Cases

- **Computer-use agents** — screenshots, mouse/keyboard, and Playwright in a sandboxed browser
- **Agentic checkout / form filling** — stealth, proxies, and managed auth
- **QA agents** — parallel sessions and live/replay debugging
- **Self-host experiments** — run `kernel-images` on Docker or Unikraft
