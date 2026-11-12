# Mobile Next

> **"Real iOS and Android devices for AI agents."**

| | |
|---|---|
| **Website** | https://mobilenext.ai |
| **Docs** | https://mobilenext.ai/docs/ |
| **GitHub** | https://github.com/mobile-next/mobile-mcp |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | Apache-2.0 (open-source Mobile MCP) |
| **Latest-month signal** | Active on 2026-11-11 (~10.5k★ on mobile-mcp) |
| **Verified at** | 2026-11-12 |

---

## Official Website

https://mobilenext.ai

The site's `llms.txt` lead: *"Real iOS and Android devices for AI agents. Mobile Next Cloud gives agents (Claude Code, Cursor, Codex, Gemini CLI, ChatGPT, etc.) deterministic control of hosted real phones — tap, type, screenshot, run app flows — through the Model Context Protocol (MCP) and a REST API, billed per minute."*

---

## Official Repo

https://github.com/mobile-next/mobile-mcp — Apache-2.0. GitHub description: *"Mobile MCP: let AI agents drive your iOS and Android apps. MCP server for simulators, emulators and real devices."*

npm package: `@mobilenext/mobile-mcp`. Related repos: [mobilecli](https://github.com/mobile-next/mobilecli), [mobilewright](https://github.com/mobile-next/mobilewright) (test-authoring on top of the same stack).

---

## How to Use (Agent Onboarding)

**Interaction pattern:** MCP (local stdio or hosted Streamable HTTP) + REST API.

This is not a one-URL join path. The local server needs a connected simulator, emulator, or real device (and the usual platform tooling). The cloud server needs a Mobile Next account (OAuth on first connect, or a Bearer API key).

**Local Mobile MCP** (open source), from the [repo README](https://github.com/mobile-next/mobile-mcp):

```bash
npx @mobilenext/mobile-mcp@latest install
```

Manual stdio config:

```json
{
  "mcpServers": {
    "mobile-mcp": {
      "command": "npx",
      "args": ["-y", "@mobilenext/mobile-mcp@latest"]
    }
  }
}
```

Claude Code (plugin):

```
/plugin marketplace add mobile-next/mobile-mcp
/plugin install mobile-mcp@mobile-mcp
```

Or: `claude mcp add mobile-mcp -- npx -y @mobilenext/mobile-mcp@latest`

**Mobile Next Cloud MCP**, from https://mobilenext.ai/llms.txt:

```bash
claude mcp add mobilenext --transport http https://app.mobilenext.ai/mcp
```

Authenticate via the OAuth flow on first connect. REST is `https://app.mobilenext.ai` with a Bearer API key (`mob_...`). OpenAPI: https://mobilenext.ai/openapi.json. New accounts include free starting credit — see https://mobilenext.ai/pricing.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package was found on the pages reviewed. The Claude Code plugin (`mobile-mcp@mobile-mcp`) and `/mobile-mirror` are the documented agent install path for the local server.

```bash
npx clawhub@latest search mobile-mcp
```

---

## MCP

**Status:** ✅ Available (open-source stdio + hosted Cloud MCP)

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/mobile-next/mobile-mcp |
| **Local transport** | stdio (`npx -y @mobilenext/mobile-mcp@latest`) |
| **Cloud endpoint** | `https://app.mobilenext.ai/mcp` (Streamable HTTP; unauthenticated requests return 401, verified 2026-11-12) |
| **Cloud auth** | OAuth on first connect, or Bearer API key |
| **Compatible Clients** | Claude Code, Codex, Cursor, Gemini CLI, ChatGPT, VS Code, and other MCP clients listed in the README |

The README describes an accessibility-first control loop (native UI tree, with screenshot+coordinates as fallback), plus device, app, screen, input, and log tools. The same tools work across iOS and Android — simulators, emulators, and real devices. Cloud tools and prompts: https://mobilenext.ai/docs/cloud/tools-and-prompts.

---

## What It Does

Mobile Next is a programmable mobile runtime for AI agents. The open-source Mobile MCP server attaches to a simulator, emulator, or cable-connected phone and lets an agent read the accessibility tree, tap, type, swipe, install and launch apps, and record the screen. Mobile Next Cloud is the same control surface on hosted real iOS and Android devices, billed per minute, over a hosted MCP server and a REST API.

Mobilewright sits on top when a working agent flow should become a repeatable CI test.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | `llms.txt`: *"Real iOS and Android devices for AI agents."* GitHub: *"let AI agents drive your iOS and Android apps."* Sources: https://mobilenext.ai/llms.txt, https://github.com/mobile-next/mobile-mcp |
| **Agent-specific primitive** | Accessibility-tree device control designed for an LLM (structured elements, not XCUITest/Espresso scripts). Cloud sessions are allocated, driven, and released as a mid-task "hands on a phone" step. |
| **Autonomy-compatible control plane** | After MCP is connected (and, for cloud, authenticated), the agent can allocate a device, walk a flow, and release it with no per-tap human click. Billing is per minute. |
| **M2M integration surface** | Open-source stdio MCP; hosted Streamable HTTP MCP; REST + OpenAPI (https://mobilenext.ai/openapi.json); `llms.txt` and `llms-full.txt`. |
| **Identity / delegation** | Cloud REST uses Bearer keys (`mob_...`). Hosted MCP uses OAuth or the same key. The local server can require `MOBILEMCP_AUTH` as a Bearer token. Pages reviewed do not describe a portable KYA identity beyond account/key and the device session. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Mobile MCP (local)** | Apache-2.0 MCP server for simulators, emulators, and real devices you already have. |
| **Mobile Next Cloud** | Hosted real iOS/Android devices via MCP and REST, billed per minute. |
| **Accessibility-first control** | Native UI tree first; screenshots only when needed. |
| **Mobilewright** | Optional test-authoring layer that turns a flow into a CI test. |

---

## Autonomy Model

1. Operator installs Mobile MCP locally (device tooling required) or signs in to Mobile Next Cloud.
2. Agent lists available devices, allocates one (cloud) or attaches to a local target, and inspects the UI tree.
3. Agent taps, types, swipes, installs or launches apps, and repeats until the task is done.
4. Cloud sessions are released; billing is per minute. See [pricing](https://mobilenext.ai/pricing) for current rates and free credit.

---

## Identity and Delegation Model

- Cloud: OAuth for interactive MCP, Bearer `mob_...` keys for REST and headless use (https://mobilenext.ai/docs/api/api-keys).
- Local HTTP mode can set `MOBILEMCP_AUTH` so every request needs a Bearer token (README).
- Scope is the signed-in account or key, plus the device the agent is attached to. No separate delegated-agent token was found in the pages reviewed.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Local MCP | `npx -y @mobilenext/mobile-mcp@latest` (stdio) |
| Cloud MCP | `https://app.mobilenext.ai/mcp` |
| REST | `https://app.mobilenext.ai` — OpenAPI at https://mobilenext.ai/openapi.json |
| Docs | https://mobilenext.ai/docs/ · https://mobilenext.ai/llms.txt |

---

## Human-in-the-Loop Support

The Claude Code plugin's `/mobile-mirror` shows a live screen the person can also tap. Cloud usage is watched through the usual account/console path. The agent loop itself does not require a human click per action.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Appium / XCUITest / Espresso** | Human-authored test scripts and selectors, not an agent-facing a11y-tree MCP. |
| **Consumer device clouds** | Built for manual QA or Appium suites; Mobile Next's primary published consumer is an AI agent over MCP. |

---

## Use Cases

- **Give a coding agent a real phone** — install an `.apk`/`.ipa`, walk a signup flow, screenshot a bug.
- **Local device control** — drive a USB-connected phone or simulator from Claude Code, Codex, or Cursor with the Apache-2.0 server.
- **CI graduation** — turn an agent-explored flow into a Mobilewright test.
