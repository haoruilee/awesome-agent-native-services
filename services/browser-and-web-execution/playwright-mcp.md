# Playwright MCP

> **"A Model Context Protocol (MCP) server that provides browser automation capabilities using Playwright."**

| | |
|---|---|
| **Website** | https://playwright.dev/docs/getting-started-mcp |
| **Docs** | https://playwright.dev/mcp/configuration/options |
| **GitHub** | https://github.com/microsoft/playwright-mcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=social)](https://github.com/microsoft/playwright-mcp) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **License** | Apache-2.0 |

---

## Official Website

https://playwright.dev/docs/getting-started-mcp

---

## Official Repo

https://github.com/microsoft/playwright-mcp

---

## How to Use (Agent Onboarding)

**Interaction pattern:** MCP server (stdio by default; optional HTTP transport)

```bash
npx @playwright/mcp@latest
```

Add to MCP client configuration:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Optional standalone HTTP mode:

```bash
npx @playwright/mcp@latest --port 8931
# MCP URL: http://localhost:8931/mcp
```

---

## Agent Skills

**Status:** ⚠️ No standalone `SKILL.md` package found from the Playwright MCP repository.

```bash
npx clawhub@latest search playwright mcp
```

---

## MCP

**Status:** ✅ Native MCP server

| Detail | Value |
|---|---|
| **Package** | `@playwright/mcp` |
| **Transport** | stdio (default), HTTP (with `--port`) |
| **Install/Run** | `npx @playwright/mcp@latest` |
| **Docs** | https://playwright.dev/docs/getting-started-mcp |

---

## What It Does

Playwright MCP exposes browser automation as MCP tools so coding agents can open pages, inspect structure, click/type, and extract information from real web sessions. It uses accessibility snapshots and structured tool responses, reducing reliance on pixel-based screenshot interpretation.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repository tagline explicitly defines it as an MCP server for LLM-driven browser automation. |
| **Agent-specific primitive** | Structured accessibility snapshot workflow and browser actions exposed directly as MCP tools. |
| **Autonomy-compatible control plane** | Agents can run full browser action loops (navigate, interact, extract) without per-action human confirmation. |
| **M2M integration surface** | npm package + MCP server protocol (stdio/HTTP) as the primary interface. |
| **Identity / delegation** | Supports isolated local/browser sessions and configurable network constraints (`--allowed-hosts`, origins, blocked origins) for controlled agent execution contexts. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Browser automation tools** | Navigate, click, type, extract via MCP tool calls |
| **Accessibility snapshots** | Structured page representation for LLM tool reasoning |
| **Configurable runtime policy** | Allowed hosts/origins, blocked origins, file access controls |
| **Dual transport** | stdio for local MCP clients, HTTP when launched as standalone service |

---

## Autonomy Model

```
Agent host starts Playwright MCP server
    ↓
Agent invokes browser tools via MCP (navigate/interact/extract)
    ↓
Server executes actions in Playwright browser context
    ↓
Structured outputs return to agent for next decision step
```

---

## Identity and Delegation Model

- Browser session state is scoped to the running MCP server context.
- Operators can constrain delegated web access using allow/block host/origin flags.
- Action traces are attributable through agent host logs + MCP tool invocation history.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP stdio | `npx @playwright/mcp@latest` |
| MCP HTTP | `--port` mode, e.g. `http://localhost:8931/mcp` |
| npm package | `@playwright/mcp` |
| Docker | `mcr.microsoft.com/playwright/mcp` |

---

## Human-in-the-Loop Support

Not required for baseline operation. Human operators can supervise via host-side tooling/logs and enforce runtime policies (hosts/origins/capabilities) before enabling autonomous runs.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Raw Playwright scripts** | Requires custom wrapper logic; no standard MCP tool contract for agent interoperability. |
| **Screenshot-only browser tools** | Less deterministic for many tasks; Playwright MCP is built around structured accessibility snapshots and tool calls. |
| **Manual browser testing workflows** | Human-driven and non-autonomous by default. |

---

## Use Cases

- Coding agents validating UI flows before generating or updating tests.
- Web research agents that must interact with JavaScript-heavy pages.
- Autonomous regression checks integrated into agentic CI loops.
- Multi-agent systems where one specialist agent handles browser interaction over MCP.
