# Mobilerun

> **"Give your AI Agent a phone."**

| | |
|---|---|
| **Website** | https://mobilerun.ai |
| **Docs** | https://docs.mobilerun.ai |
| **GitHub** | https://github.com/droidrun/mobilerun |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | MIT (open-source framework) |
| **Latest-month signal** | Active on 2026-11-12 (~10.0k★); formerly published as Droidrun |
| **Verified at** | 2026-11-12 |

---

## Official Website

https://mobilerun.ai

Homepage H1: *Give your AI Agent a phone.* The site's `llms.txt` lead: *"Cloud phones for AI agents."* The hosted product is Mobilerun Cloud; the engine underneath is the open-source Mobilerun framework (MIT), published at https://github.com/droidrun/mobilerun (the GitHub org is still `droidrun`).

---

## Official Repo

https://github.com/droidrun/mobilerun — MIT. README lead: *"Mobilerun is an open-source framework for mobile app testing, QA, and running AI agents on real Android and iOS devices."*

Related repos from the same project: [Mobilerun Portal](https://github.com/droidrun/mobilerun-portal) (Android companion app), [mobile-harness](https://github.com/droidrun/mobile-harness) (agent skill), and Cloud SDKs (`mobilerun-sdk` / `@mobilerun/sdk`).

---

## How to Use (Agent Onboarding)

**Interaction pattern:** CLI (local framework) + Cloud REST / Python / TypeScript SDK + hosted MCP.

This is not a one-URL join path. A local run needs the framework, a device (and usually the Portal app). A cloud run needs a Mobilerun account and an API key or OAuth sign-in.

**Local framework** (Python 3.11 to 3.13; Python 3.14 is not supported):

```bash
uv tool install mobilerun
mobilerun setup
mobilerun configure
mobilerun run "Open settings and turn on dark mode"
```

`mobilerun setup` installs the Mobilerun Portal app, enables its accessibility service, and prepares the device. Android needs ADB plus Developer options and USB debugging. iOS setup is documented at the [device-setup guide](https://docs.mobilerun.ai/framework/guides/device-setup).

**Cloud MCP** (hosted, account required) — from [Mobilerun's MCP docs](https://docs.mobilerun.ai/mcp-server):

```
https://cloud.mobilerun.ai/api/mcp
```

In Claude Desktop / claude.ai, add a custom connector with that URL and sign in. In Cursor, add the same URL in MCP settings. API keys are recommended for CI and headless runs; OAuth is recommended for interactive IDE use.

The [mobile-harness](https://github.com/droidrun/mobile-harness) skill teaches a coding agent to drive local devices and Mobilerun Cloud phones:

```text
Set up https://github.com/droidrun/mobile-harness for me.

Read `install.md` and follow the steps to install `mobile-harness`.
```

Start at https://docs.mobilerun.ai and https://mobilerun.ai/llms.txt.

---

## Agent Skills

**Status:** ✅ Available via the [mobile-harness](https://github.com/droidrun/mobile-harness) skill (MIT), linked from the framework README. A separate "Mobilerun Agents · MCP skill" is documented at https://docs.mobilerun.ai/skills/assistant-mcp.md for the hosted-agent approval flow.

| Skill | What It Teaches the Agent |
|---|---|
| `mobile-harness` | Drive local Android/iOS devices and Mobilerun Cloud phones; app cards and shared memory |

---

## MCP

**Status:** ✅ Available (hosted Cloud MCP)

| Detail | Value |
|---|---|
| **Endpoint** | `https://cloud.mobilerun.ai/api/mcp` |
| **Transport** | Streamable HTTP (custom connector / MCP settings) |
| **Auth** | OAuth sign-in, or an API key |
| **Docs** | https://docs.mobilerun.ai/mcp-server |
| **Compatible Clients** | Cursor, Claude Desktop, claude.ai, and other Streamable HTTP clients |

The docs describe tool families for devices (`list_devices`, `create_device`, `device_action_tap`, …), tasks (`run_task`, `get_task_status`, …), and a hosted-agent chat. Policy profiles expose different tool subsets (the full profile is documented as 222 tools). Some actions surface `pending.permissions` and are resolved with `assistant_answer_permission`. The docs warn that the agent acts with the full authority of the API key or signed-in account, and that `always` is not available over MCP.

---

## What It Does

Mobilerun gives an AI agent a real Android or iOS phone — hosted in the cloud, connected from a desk, or driven locally through the MIT framework. The agent inspects the accessibility tree and screenshots, then taps, swipes, and types. Cloud phones can keep apps and data between sessions, use residential network routing, and optionally attach a receive-only number or inbox for verification messages.

The same framework that runs locally is what powers the cloud. `pip`/`uv` install is enough to try it on a device you already own; moving to hosted devices is a Cloud SDK / MCP configuration change.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage H1: *"Give your AI Agent a phone."* `llms.txt`: *"Cloud phones for AI agents."* Source: https://mobilerun.ai and https://mobilerun.ai/llms.txt |
| **Agent-specific primitive** | A phone session the agent drives from the accessibility tree plus screenshots — tap/type/swipe with natural timing, not a human QA script. Cloud phones persist app state across agent sessions. |
| **Autonomy-compatible control plane** | Once a device and credential are in place, `mobilerun run "…"` or MCP `run_task` runs a multi-step task with no per-tap human click. Constraints: billed device minutes, account/key scope, and optional MCP permission prompts. |
| **M2M integration surface** | Local CLI/Python API; Cloud REST, Python and TypeScript SDKs; hosted MCP at `https://cloud.mobilerun.ai/api/mcp`; published `llms.txt` (https://mobilerun.ai/llms.txt, https://docs.mobilerun.ai/llms.txt); mobile-harness skill. |
| **Identity / delegation** | `llms.txt` states "real device and agent identity." Cloud calls use an API key or OAuth account; MCP docs say the agent acts with that credential's full authority. Permission prompts (`assistant_answer_permission` with `once` or `reject`) are the documented approval path. There is no separate cross-service KYA token described in the pages reviewed. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Cloud or local phone** | Hosted Android, dedicated Android, physical iPhone, or a device you connect. A stopped cloud phone keeps apps and data and bills no device minutes (`llms.txt`). |
| **Visual + a11y control** | Accessibility tree combined with screenshots; tap, type, swipe. |
| **Task runner** | Natural-language `mobilerun run` locally, or Cloud `run_task` over MCP/API. |
| **Network and inbox add-ons** | Residential routing (Mobilerun Connect) and optional receive-only numbers / API inbox, per `llms.txt`. |

---

## Autonomy Model

1. Operator installs the framework or creates a Cloud account and key (or signs in with OAuth).
2. Agent lists or creates a device, then runs a task (`mobilerun run` or `run_task`).
3. The agent reads the screen, acts, and repeats until the task finishes. Cloud MCP can stream task status and screenshots.
4. For hosted-agent chat over MCP, pending permissions are resolved with `assistant_answer_permission` after the user confirms.
5. A stopped dedicated phone keeps state for the next run.

---

## Identity and Delegation Model

- Cloud authentication is an API key (automation, CI) or OAuth (interactive IDE), per the MCP docs.
- The agent inherits the key or signed-in account's authority, including billed resources.
- MCP permission prompts are documented; `always` is not offered over MCP.
- `llms.txt` mentions "real device and agent identity"; the pages reviewed do not describe a portable KYA token beyond the account/key and the device it may use.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Local CLI / Python | `uv tool install mobilerun` / `uv pip install mobilerun` — https://github.com/droidrun/mobilerun |
| Hosted MCP | `https://cloud.mobilerun.ai/api/mcp` |
| Cloud SDK | `@mobilerun/sdk`, `mobilerun-sdk` (from `llms.txt`) |
| Machine-readable docs | https://mobilerun.ai/llms.txt · https://docs.mobilerun.ai/llms.txt |

---

## Human-in-the-Loop Support

A live view lets a person watch steps and screenshots. Hosted MCP can require `assistant_answer_permission` for pending permissions. Local setup (`mobilerun setup`, USB debugging, iOS pairing) is an operator step, not an in-loop click.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **ADB / Appium / XCUITest alone** | Generic device-test control. The agent-specific loop here is natural-language tasks over an a11y+screenshot primitive, plus a cloud phone with agent identity and MCP. |
| **Consumer phone-mirroring apps** | Human-facing remote desktops, not an agent control plane. |

---

## Use Cases

- **App QA** — walk a checkout or onboarding flow on real Android and iOS, in parallel.
- **Native-app tasks** — use apps that have no public API (messages, maps, settings) from an agent.
- **Local then cloud** — start on a device you own with the MIT framework, then point the same agent at Mobilerun Cloud.
