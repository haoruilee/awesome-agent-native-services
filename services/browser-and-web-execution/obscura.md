# Obscura

> **"The open-source headless browser for AI agents and web scraping."**

| | |
|---|---|
| **Website** | https://obscura.sh |
| **Docs** | https://docs.obscura.sh |
| **GitHub** | https://github.com/h4ckf0r0day/obscura |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/h4ckf0r0day/obscura?style=social)](https://github.com/h4ckf0r0day/obscura) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **License** | Apache-2.0 |

---

## Official Website

https://obscura.sh

---

## Official Repo

https://github.com/h4ckf0r0day/obscura — Rust engine (V8), CDP server, CLI, built-in MCP server, Rust crate

---

## How to Use (Agent Onboarding)

**Interaction pattern:** **MCP (stdio or HTTP)** + `Daemon (CDP)` + **CLI**

```bash
# Download a release binary or Docker image (see GitHub releases), then:
obscura mcp                         # stdio MCP for Claude Desktop / Cursor / Claude Code
obscura mcp --http --port 3000      # Streamable HTTP MCP at http://127.0.0.1:3000/mcp
obscura serve                       # CDP server at ws://127.0.0.1:9222 for Puppeteer/Playwright
obscura fetch https://example.com   # one-shot fetch
```

MCP guide: https://docs.obscura.sh/guides/use-the-mcp-server

---

## Agent Skills

**Status:** ⚠️ No official Agent Skill bundle; agents use the built-in MCP server or CDP.

See: https://agentskills.io/specification to contribute a portable `SKILL.md`.

---

## MCP

**Status:** ✅ Available (built into the `obscura` binary)

| Detail | Value |
|---|---|
| **Docs** | https://docs.obscura.sh/guides/use-the-mcp-server |
| **Transport** | stdio (default) or Streamable HTTP (`--http`) |
| **Invocation** | `obscura mcp` |
| **Tools** | `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_fill`, `browser_type`, `browser_evaluate`, `browser_wait_for`, `browser_screenshot`, `browser_pdf`, `browser_network_requests`, … |
| **Compatible Clients** | Claude Desktop, Claude Code, Cursor, any MCP host |

---

## What It Does

Obscura is a **from-scratch headless browser engine written in Rust** that runs real JavaScript via V8 and speaks the **Chrome DevTools Protocol**, so it works as a drop-in replacement for headless Chrome with Puppeteer and Playwright. The project reports ~30 MB memory per instance versus 200+ MB for headless Chrome. Release builds include a native rendering engine (screenshots, screencast, PDF export without Chromium), and an optional stealth build adds anti-detection. A built-in **MCP server** keeps a live browser session and exposes snapshot/act tools with element references to agents.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README tagline: *"The open-source headless browser for AI agents and web scraping."* — [github.com/h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) |
| **Agent-specific primitive** | Persistent MCP browser session with `browser_snapshot` (readable text + element references) and reference-based `browser_click` / `browser_fill` |
| **Autonomy-compatible control plane** | Agent navigates, acts and reads the page over MCP or CDP with no human window; HTTP MCP is guarded by bearer token, origin allowlist and resource bounds |
| **M2M integration surface** | MCP (stdio/HTTP), CDP WebSocket server, CLI `fetch`, embeddable Rust crate |
| **Identity / delegation** | Per-session proxy and user-agent flags; HTTP MCP requires `OBSCURA_MCP_TOKEN` for non-loopback binds |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **MCP server** | `obscura mcp` — live browser session exposed as tools |
| **CDP server** | `obscura serve` — Puppeteer/Playwright connect over WebSocket |
| **`fetch` CLI** | Load a URL, print content, evaluate JS, or capture a screenshot |
| **Rust crate** | `Browser` / `Page` / `Element` API with request interception |

---

## Autonomy Model

```
Agent host launches obscura mcp (or connects to obscura serve)
    ↓
browser_navigate → browser_snapshot (text + element refs)
    ↓
browser_click / browser_fill / browser_evaluate on refs
    ↓
Agent reads results and repeats — no human in the loop
```

---

## Identity and Delegation Model

- **Isolation:** each MCP server process keeps its own live browser session; run separate processes per agent or task.
- **Access control:** HTTP MCP binds loopback by default; non-loopback binds require `OBSCURA_MCP_TOKEN` (≥32 bytes) bearer auth, plus an origin allowlist.
- **Outbound identity:** `--proxy` and `--user-agent` flags; optional stealth build.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **MCP** | `obscura mcp` (stdio) or `obscura mcp --http --port 3000` (`/mcp`) |
| **CDP** | `obscura serve` — `ws://127.0.0.1:9222` |
| **CLI** | `obscura fetch <url>` with `--eval`, `--screenshot`, `--output` |
| **Library** | Rust crate via git dependency |

---

## Human-in-the-Loop Support

Not required. Operators control exposure through transport choice (stdio vs HTTP), bearer tokens and origin allowlists.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Headless Chrome** | Heavier per instance and no built-in agent tool surface |
| **Raw HTTP fetch** | No JavaScript execution or DOM interaction |

---

## Use Cases

- **Coding and research agents** that need a lightweight local browser through MCP.
- **High-parallel scraping** where per-instance memory matters.
- **Existing Puppeteer/Playwright stacks** swapping in a lighter engine over CDP.
