# Chrome DevTools MCP

> **"`chrome-devtools-mcp` lets your coding agent (such as Gemini, Claude, Cursor or Copilot) control and inspect a live Chrome browser."**

| | |
|---|---|
| **Website** | https://github.com/ChromeDevTools/chrome-devtools-mcp |
| **GitHub** | https://github.com/ChromeDevTools/chrome-devtools-mcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=social)](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | Apache-2.0 (per repository) |

---

## Official Website

https://github.com/ChromeDevTools/chrome-devtools-mcp

---

## Official Repo

https://github.com/ChromeDevTools/chrome-devtools-mcp

---

## How to Use (Agent Onboarding)

**MCP — add to your MCP client config** (see [README](https://github.com/ChromeDevTools/chrome-devtools-mcp)):

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

**Slim + headless** (basic browser tasks only):

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--slim", "--headless"]
    }
  }
}
```

**Requirements:** Node.js v20.19+ (LTS), Chrome stable+, npm — [Getting started](https://github.com/ChromeDevTools/chrome-devtools-mcp#getting-started).

---

## Agent Skills

**Status:** ⚠️ Not yet published as a dedicated `npx skills add …` pack

Search community skills: `npx clawhub@latest search chrome-devtools-mcp`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ This project **is** an MCP server

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/ChromeDevTools/chrome-devtools-mcp |
| **Transport** | stdio (via `npx`) |
| **Compatible Clients** | Cursor, Claude Desktop, Gemini, Copilot, VS Code MCP hosts, other MCP-compatible clients |

---

## What It Does

Chrome DevTools MCP exposes **live Chrome** to coding agents through the Model Context Protocol: **Puppeteer-driven automation** with waits for action results, **DevTools-level debugging** (network, console with source maps, screenshots), and **performance tooling** (traces and lab/field insights). It is explicitly built so **coding agents** can drive and inspect a real browser session rather than guessing from static HTML.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: *"`chrome-devtools-mcp` lets your **coding agent** (such as Gemini, Claude, Cursor or Copilot) control and inspect a live Chrome browser"* and *"giving your **AI coding assistant** access to the full power of Chrome DevTools"* — [repo README](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| **Agent-specific primitive** | **MCP tool surface for DevTools + reliable browser automation** — combines instrumented debugging (traces, network, console) with agent-directed Puppeteer actions; not a generic "open Chrome" human shortcut |
| **Autonomy-compatible control plane** | Once the MCP server is configured, the agent invokes tools in a loop without per-click human confirmation (subject to host policies) |
| **M2M integration surface** | MCP over stdio; distributed via `npx` / npm |
| **Identity / delegation** | Runs under the **developer's local Chrome** and OS user; access boundary is the user's machine and any optional usage/telemetry flags documented in the README (`--no-usage-statistics`, etc.) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **MCP tool: automation** | Puppeteer-based actions with automatic waiting for results |
| **MCP tool: debugging** | Network inspection, console messages, screenshots, source-mapped stacks |
| **MCP tool: performance** | Recording traces and performance insights (with documented CrUX/telemetry options) |
| **`--slim` mode** | Reduced tool set for lighter agent workloads |
| **Headless / headed** | Configurable Chrome launch for agent scenarios |

---

## Autonomy Model

```
MCP host starts chrome-devtools-mcp via npx
  ↓
Agent issues MCP tool calls (navigate, click, evaluate, performance, network, …)
  ↓
Server drives local Chrome (Puppeteer) and/or DevTools capabilities
  ↓
Structured results return to the agent context window
```

---

## Identity and Delegation Model

- **No cloud agent identity** — the agent operates **through the developer's workstation** and **local Chrome profile** (unless configured otherwise).
- **Trust boundary** is the user's machine; README warns that MCP clients can inspect or modify browser/DevTools data exposed by the server.
- **Optional telemetry** is documented and opt-out via flags or environment variables per [README](https://github.com/ChromeDevTools/chrome-devtools-mcp).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **MCP** | stdio server launched with `npx -y chrome-devtools-mcp@latest` |
| **npm** | Package `chrome-devtools-mcp` |
| **Chrome** | Official support for Google Chrome and Chrome for Testing |

---

## Human-in-the-Loop Support

Initial setup (install Node, Chrome, add MCP config) is human-driven. Routine tool calls are autonomous from the agent's perspective. Sensitive flows should rely on the user's local browser policies and MCP host governance.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw Puppeteer/Playwright scripts** | No MCP-standard tool schema for agents; no bundled DevTools performance/debugging workflow |
| **Remote cloud browsers alone** | Do not replace **local live DevTools** integration for the same debugging/performance primitives |
| **Paste-screenshot workflows** | Lose structured console/network/trace data agents need for iterative fixes |

---

## Use Cases

- **UI bug triage** — agent reads console stacks and network failures directly from DevTools tools
- **Performance fixes** — agent captures traces and interprets lab/field signals (per product docs)
- **Reliable web automation in IDE** — agent uses waited Puppeteer actions instead of brittle line-based edits
- **One-shot UI implementation** — combine with design-context MCPs (e.g. Figma) for faster iteration
