# Lightpanda

> **"The headless browser built from scratch for AI agents and automation."**

| | |
|---|---|
| **Website** | https://lightpanda.io |
| **Docs** | https://lightpanda.io/docs |
| **GitHub** | https://github.com/lightpanda-io/browser |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/lightpanda-io/browser?style=social)](https://github.com/lightpanda-io/browser) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **License** | AGPL-3.0 |

---

## Official Website

https://lightpanda.io

---

## Official Repo

https://github.com/lightpanda-io/browser — Zig implementation, CDP server, CLI, built-in MCP mode

https://github.com/lightpanda-io/agent-skill — OpenClaw-oriented skill (community)

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Daemon (CDP)` + **MCP (stdio)** + **CLI**

```bash
# Nightly binary (see releases) or Docker:
# docker run -d -p 127.0.0.1:9222:9222 lightpanda/browser:nightly

./lightpanda serve --host 127.0.0.1 --port 9222
```

```js
// Puppeteer (same pattern as headless Chrome)
import puppeteer from 'puppeteer-core';
const browser = await puppeteer.connect({
  browserWSEndpoint: 'ws://127.0.0.1:9222',
});
```

**MCP:** Add to MCP config (stdio) per [MCP server guide](https://lightpanda.io/docs/open-source/guides/mcp-server):

```json
{
  "mcpServers": {
    "lightpanda": {
      "command": "/path/to/lightpanda",
      "args": ["mcp"]
    }
  }
}
```

**One-shot fetch (markdown or HTML):**

```bash
./lightpanda fetch --dump markdown https://example.com
```

---

## Agent Skills

**Status:** ⚠️ No single official `npx skills add …` bundle from the browser repo; see companion repo for OpenClaw.

| Skill | Source | What It Teaches the Agent |
|---|---|---|
| OpenClaw skill | https://github.com/lightpanda-io/agent-skill | Using Lightpanda from OpenClaw-style workflows |

```bash
npx clawhub@latest search lightpanda
```

See: https://agentskills.io/specification to contribute a portable `SKILL.md`.

---

## MCP

**Status:** ✅ Available (built into the `lightpanda` binary)

| Detail | Value |
|---|---|
| **Docs** | https://lightpanda.io/docs/open-source/guides/mcp-server |
| **Transport** | stdio (JSON-RPC 2.0) |
| **Invocation** | `lightpanda mcp` |
| **Compatible Clients** | Cursor, Claude Desktop, Codex, any MCP host that supports stdio servers |

---

## What It Does

Lightpanda is a **from-scratch headless browser** (Zig, V8, not Chromium/WebKit) aimed at **AI agents and automation**. It runs a **Chrome DevTools Protocol (CDP)** server so existing stacks (for example **Puppeteer** via `browserWSEndpoint`) can drive navigation, clicks, and extraction with a small memory footprint versus full Chrome. A **`fetch` CLI** can dump **HTML or markdown** for RAG-style ingestion. A **native MCP mode** exposes browser control directly to MCP clients without a separate adapter process.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README opening line: *"The headless browser built from scratch for AI agents and automation."* — [github.com/lightpanda-io/browser](https://github.com/lightpanda-io/browser) |
| **Agent-specific primitive** | **Headless browser session** with CDP wire-up for programmatic control; **`--dump markdown`** for LLM-ready page text; **MCP** as a first-class invocation mode (`lightpanda mcp`) |
| **Autonomy-compatible control plane** | Agent connects over CDP or MCP and drives navigation and DOM actions without a human-operated window; optional `--obey-robots` for policy-aware fetching |
| **M2M integration surface** | CDP WebSocket server (`serve`), Puppeteer-compatible `connect`, MCP stdio, CLI `fetch` |
| **Identity / delegation** | **Per-browser-context isolation** via standard CDP/Puppeteer patterns (separate `BrowserContext` / pages); custom headers and proxy support for attributable, configurable outbound identity |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **CDP server** | `lightpanda serve` — WebSocket endpoint for Puppeteer/Playwright-style clients |
| **MCP server** | `lightpanda mcp` — stdio MCP for tool-calling agents |
| **`fetch` CLI** | Non-interactive URL dump (`--dump html` or `--dump markdown`) with wait options |
| **Browser contexts / pages** | Standard multi-context isolation for parallel agent workloads |

---

## Autonomy Model

```
Agent (or MCP host) starts lightpanda serve OR runs lightpanda mcp
    ↓
Agent connects via CDP (Puppeteer) or invokes MCP tools
    ↓
Agent navigates, clicks, evaluates scripts, extracts structured data
    ↓
Agent disconnects or tears down context — no human in the browser loop
```

For read-only ingestion, the agent may skip CDP and call `lightpanda fetch` to obtain markdown.

---

## Identity and Delegation Model

- **Isolation:** Separate browser contexts and pages map cleanly to separate agent tasks or tenants.
- **Outbound attribution:** Custom HTTP headers and proxy configuration (per README feature list) let the operator scope how the browser presents itself on the network.
- **Policy:** Optional `robots.txt` respect (`--obey-robots`) for autonomous but policy-aware crawling.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **CDP** | WebSocket server — connect with `puppeteer.connect({ browserWSEndpoint })` |
| **MCP** | stdio — `lightpanda mcp` — [documentation](https://lightpanda.io/docs/open-source/guides/mcp-server) |
| **CLI** | `lightpanda fetch`, `lightpanda serve` |
| **Docker** | Official image `lightpanda/browser` (see repo README) |

---

## Human-in-the-Loop Support

Not required for core automation. Operators may enforce **robots.txt** and network policies via flags. The upstream project **collects telemetry by default**; disable with `LIGHTPANDA_DISABLE_TELEMETRY=true` — see [privacy policy](https://lightpanda.io/privacy-policy).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Headless Chrome / Chromium** | Full browser stack; far heavier RAM/CPU per tab — opposite of the “built for automation scale” goal Lightpanda states |
| **Raw HTTP + `curl`** | No JS execution or DOM — fails on SPAs and dynamic sites Lightpanda targets |
| **Remote cloud browser APIs** | Different tradeoff: vendor-hosted sessions vs **self-hosted, AGPL** browser you run entirely on your own metal |

---

## Use Cases

- **Coding agents** — drive internal or public web UIs via MCP or Puppeteer without launching Chrome.
- **Research / RAG agents** — `fetch --dump markdown` for clean text from JavaScript-heavy pages.
- **High-parallel crawlers** — many isolated contexts with lower per-instance overhead than full Chromium (see project benchmarks).
- **Self-hosted compliance** — run the browser stack entirely inside your network boundary.
