# Cua

> **"Scale computer fleets for every agent"**

| | |
|---|---|
| **Website** | https://cua.ai |
| **Docs** | https://cua.ai/docs |
| **GitHub** | https://github.com/trycua/cua |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Show HN CUA-S1 2026-09-19 ([item 49767564](https://news.ycombinator.com/item?id=49767564)); mature OSS (~24.6k★) |
| **Verified at** | 2026-09-20 |

---

## Official Website

https://cua.ai

Live document title: *Cua: Scale computer fleets for computer-use agents*. Homepage H1: *Scale computer fleets for every agent*. GitHub README lead: *"Give AI agents computers they can use."*

---

## Official Repo

https://github.com/trycua/cua

MIT (see [LICENSE.md](https://github.com/trycua/cua/blob/main/LICENSE.md)). Monorepo for Cua Driver, Sandbox / Fleets, Lume, Cua Bench, and CUA-S1 research code. Optional extras (for example OmniParser / ultralytics) carry their own licenses.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + **MCP (stdio)** + Sandbox / Fleet SDK

**Cua Driver** (operate a machine you already have):

```bash
# macOS / Linux
/bin/bash -c "$(curl -fsSL https://cua.ai/driver/install.sh)"

# Windows (PowerShell)
irm https://cua.ai/driver/install.ps1 | iex

cua-driver --version
cua-driver call list_apps
cua-driver mcp-config --client <client>
```

Register the stdio MCP server (Claude Code example):

```bash
claude mcp add --transport stdio cua-driver -- cua-driver mcp
```

Generic MCP JSON:

```json
{
  "mcpServers": {
    "cua-driver": {
      "command": "cua-driver",
      "args": ["mcp"]
    }
  }
}
```

Embedded / filesystem skill:

```bash
cua-driver skills install
cua-driver skills status
```

**Cloud Fleets** (isolated desktops at [run.cua.ai](https://run.cua.ai)): a human first creates Fleet credentials, then claims a sandbox through the Sandbox / Fleet SDK. Start at [Your first Cloud Fleet](https://cua.ai/docs/tutorials/your-first-cloud-fleet). Local sandboxes share the Sandbox SDK but use Docker, QEMU, or Apple VZ instead of cloud pools.

This is **not** URL Onboarding. Driver needs OS permissions (for example macOS Accessibility / Screen Recording). Fleets need a billed Cua account. Reading a page does not enroll an agent.

**Not Browser Use Cloud:** Cua provisions and drives *computers* (Linux, Windows, macOS, Android) and native desktop apps. It is not a stealth-browser / CAPTCHA / residential-proxy browser SaaS.

---

## Agent Skills

**Status:** ✅ Available via the Driver binary (filesystem skill + MCP `skill://cua-driver/` resources)

```bash
cua-driver skills install
```

| Skill | What It Teaches the Agent |
|---|---|
| `cua-driver` | How to inspect apps and issue bounded desktop actions through the Driver CLI / MCP tools |

The skill documents action policy; it does **not** grant desktop permissions or approve actions. Some hosts (for example Claude Code) can list the embedded MCP skill resource but still need the filesystem install to activate it as a native skill. See [Connect your agent](https://cua.ai/docs/how-to-guides/driver/connect-your-agent).

---

## MCP

**Status:** ✅ Available (Cua Driver stdio; Cua CLI also documents a CLI MCP server)

| Detail | Value |
|---|---|
| **MCP Repo / binary** | https://github.com/trycua/cua — `cua-driver mcp` |
| **Transport** | stdio (MCP revision `2026-07-28`; legacy clients negotiate `2025-06-18`) |
| **Auth / policy** | Host OS permissions + Driver permission mode (`standard` vs `bounded` capability manifest). An agent cannot widen mode from a tool call. |
| **Compatible Clients** | Claude Code, Codex, Cursor, OpenCode, OpenClaw, Qwen Code, Factory Droid, and others via `cua-driver mcp-config --client <name>` |

Grok Bot is a separate local-command path and does not use stdio MCP.

---

## What It Does

Cua gives computer-use agents real machines and a background driver. **Cua Fleets** keep warm pools of Linux, Windows, macOS, and Android desktops that code can claim for evals, RL, data generation, or batch rollouts. **Cua Driver** lets an agent click, type, scroll, read accessibility trees, and capture window state on macOS, Windows, and Linux without stealing the operator's cursor or focus when the platform supports background delivery. **Lume** manages local Apple Silicon VMs. **Cua Bench** authors and scores computer-use tasks. **CUA-S1** is a family of small specialist models for bounded GUI decisions (first profile: forms).

Computer-Use 2.0 in Cua's docs treats the GUI as one tool surface beside code, shell, files, and APIs — not as a standalone "AI browser" product.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage H1: *"Scale computer fleets for every agent"* — [cua.ai](https://cua.ai). Title: *"Cua: Scale computer fleets for computer-use agents"*. README: *"Give AI agents computers they can use."* Docs: *"Open-source computer-use automation for real machines and isolated desktops."* |
| **Agent-specific primitive** | Fleet claim/release of isolated GUI machines; background computer-use driver (MCP/CLI) that addresses native apps without owning the human cursor; accessibility-tree + screenshot tools; optional CUA-S1 specialist decisions. Distinct from a headless Chromium rental. |
| **Autonomy-compatible control plane** | A provisioned Driver or claimed Fleet sandbox accepts agent actions without a human click per keystroke. Constraints: OS TCC / permissions, Driver `standard` vs `bounded` manifests, Fleet credentials and pool size. |
| **M2M integration surface** | `cua-driver` CLI + stdio MCP + skills; Python Sandbox SDK; TypeScript Fleet SDK; Lume CLI; Cua Bench CLI. Docs: https://cua.ai/docs |
| **Identity / delegation** | Fleet user API keys / OAuth for cloud pools; Driver runtime permission mode and capability manifests bound to the owning process (not widenable by the agent); actions attributed to the Driver / sandbox session. Host OS user remains the desktop principal. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Cua Driver** | Background computer-use driver: MCP, daemon, or one-shot `cua-driver call` |
| **Cua Sandbox** | Disposable GUI environment via Docker, QEMU, Apple VZ, or cloud |
| **Cua Fleets** | Warm pools of machines claimed on demand at run.cua.ai |
| **Lume** | Local macOS / Linux VMs on Apple Silicon (Virtualization.framework) |
| **Cua Bench** | Task authoring, evaluators, trajectory export |
| **CUA-S1** | Small specialist models for scoped GUI decisions (forms first) |

---

## Autonomy Model

```
Operator installs Cua Driver (local desktop) and/or creates Fleet credentials
    ↓
Operator chooses permission mode (standard desktop vs bounded manifest) or a Fleet image
    ↓
Agent connects via MCP / CLI / SDK
    ↓
Agent lists apps, inspects AX trees / screenshots, and issues clicks and keystrokes
    ↓
On Fleets: claim a warm machine, run the rollout, release it back to the pool
    ↓
Optional Bench evaluators or CUA-S1 specialists score or bound the next action
```

Background delivery keeps the human cursor and frontmost app in place when the OS and target app support it.

---

## Identity and Delegation Model

- **Cloud Fleets** — operator-held `CUA_CLIENT_ID` / `CUA_CLIENT_SECRET` (or equivalent Fleet credentials). Agents claim sandboxes inside that account's pools; they do not self-register a Cua user.
- **Driver** — runs as a local binary / `CuaDriver.app` daemon. Permission mode is chosen at launch. `--grant existing-profile` is the only authorization flag `cua-driver mcp` accepts; agents cannot escalate from a tool call.
- **Bounded mode** — capability manifest limits apps, origins, and directories.
- **Host OS** — macOS Accessibility and Screen Recording stay with the signed app for TCC attribution.
- **Audit / eval** — Bench trajectories and Fleet rollouts record agent activity for training or review; that is evidence, not a KYA identity token.
- **CUA-S1** — research models with separate Hugging Face cards and safety notes; weights are not the MIT monorepo by themselves.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Cua Driver CLI / MCP | `cua-driver` — https://cua.ai/docs/how-to-guides/driver/install |
| Agent skill | `cua-driver skills install` + embedded `skill://cua-driver/` |
| Sandbox SDK | Python `cua-sandbox` — local and cloud runtimes |
| Fleet SDK | TypeScript `@trycua/fleet`; cloud pools at https://run.cua.ai |
| Lume CLI | https://cua.ai/lume/install.sh |
| Cua Bench | `uv tool install 'cua-bench[browser]'` |
| Docs index | https://cua.ai/docs |

---

## Human-in-the-Loop Support

Humans install Driver, grant OS permissions, write bounded manifests, and create Fleet accounts. Individual clicks inside an allowed runtime do not require a GUI confirmation. Bench and data-generation paths can add evaluators or human-reviewed golden trajectories. CUA-S1 is a specialist scorer, not a human approval queue.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Browser Use Cloud** | Managed stealth browsers, CAPTCHA, proxies, and NL `run()` tasks — already listed under Browser & Web Execution. Cua is cross-OS computer fleets and a native-desktop driver, not that product. |
| **Playwright / Puppeteer alone** | Browser automation library; no Fleet claim model, no background native-desktop driver |
| **Scrapybara / Cyberdesk** | Related "computer for an agent" runtimes; Cua's sit point is Driver + multi-OS fleets + Bench + CUA-S1 in one OSS monorepo |
| **Generic GPU VM (EC2, etc.)** | Hosts a desktop if you install one; no computer-use driver, MCP tool surface, or warm-pool claim API |

---

## Use Cases

- **Background desktop QA** — agent operates Calculator, LibreOffice, or a WPF app while the operator keeps focus
- **Parallel eval / RL** — claim Fleet replicas, roll out, release, keep trajectories
- **Local macOS isolation** — Lume VM on Apple Silicon, then Driver or SSH
- **Scoped form filling** — CUA-S1-FORMS scores field decisions; Driver executes them one action at a time
