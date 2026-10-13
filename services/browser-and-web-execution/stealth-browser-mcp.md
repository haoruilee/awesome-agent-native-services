# Stealth Browser MCP

> **"Stealth browser automation for MCP-compatible AI agents."**

| | |
|---|---|
| **Website** | https://github.com/vibheksoni/stealth-browser-mcp |
| **Docs** | https://github.com/vibheksoni/stealth-browser-mcp#readme |
| **GitHub** | https://github.com/vibheksoni/stealth-browser-mcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/vibheksoni/stealth-browser-mcp?style=social)](https://github.com/vibheksoni/stealth-browser-mcp) |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push 2026-07-24 ([repo metadata](https://api.github.com/repos/vibheksoni/stealth-browser-mcp)). Quieter than neighboring browser rows — verify `master` before depending on a weekly release cadence |
| **Verified at** | 2026-10-13 |

---

## Official Website

No separate marketing site is listed. The GitHub README is the official entry:

https://github.com/vibheksoni/stealth-browser-mcp

---

## Official Repo

https://github.com/vibheksoni/stealth-browser-mcp

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `MCP`

```bash
git clone https://github.com/vibheksoni/stealth-browser-mcp.git
cd stealth-browser-mcp
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Claude Code (macOS/Linux) from the official README:

```bash
claude mcp add-json stealth-browser-mcp '{
  "type": "stdio",
  "command": "/path/to/stealth-browser-mcp/venv/bin/python",
  "args": ["/path/to/stealth-browser-mcp/src/server.py"]
}'
```

Requires Python 3.10+ and Chrome, Chromium, or Microsoft Edge. Optional HTTP transport: `python src/server.py --transport http --host 127.0.0.1 --port 8000` with `STEALTH_BROWSER_MCP_AUTH_TOKEN` set. There is no URL-onboarding document.

---

## Agent Skills

**Status:** ✅ Available in-repo (not `npx skills add`).

The repository ships `skills/stealth-browser-mcp` for Codex-style skill clients. It covers tool order, state checks, pre-document CDP scripts, network debugging, and cleanup. Symlink that folder into the client skills directory if the host does not auto-load repo-local skills.

---

## MCP

**Status:** ✅ Available — this project **is** the MCP server.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/vibheksoni/stealth-browser-mcp |
| **Transport** | stdio (recommended) or HTTP with optional bearer token |
| **Compatible Clients** | Claude Code, Claude Desktop, Cursor, FastMCP installers |
| **Tool surface** | Full 97 tools / minimal 20 / per-section disable flags |

---

## What It Does

Stealth Browser MCP is a **local MCP browser** built on [nodriver](https://github.com/ultrafunkamsterdam/nodriver), Chrome DevTools Protocol, and FastMCP. Official copy: navigate Cloudflare challenges, anti-bot checks, and login walls with real Chrome-family browsers. It is not a generic Puppeteer wrapper and not a hosted cloud browser.

Features the README actually claims: anti-bot resistance that has passed Cloudflare and Queue-It style checks in testing (results vary); 97 tools in 11 sections; pixel-accurate element cloning via CDP; network inspection; a restricted Python **dynamic hook** system to intercept, block, redirect, fulfill, or modify request/response flows; CDP/JavaScript execution for trusted local clients.

**Distinctness vs catalog browsers:** [Browser MCP](browser-mcp.md) is a Puppeteer accessibility-tree server. [Playwright MCP](playwright-mcp.md) is Microsoft's Playwright tool surface (the README's own comparison table). [Browserbase](browserbase.md) / [Browser Use Cloud](browser-use-cloud.md) are hosted remote browsers. This project is a local stealth/anti-detect MCP with nodriver + CDP hooks.

**Freshness:** last push 2026-07-24 at verification.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: **"Stealth browser automation for MCP-compatible AI agents."** — [repo](https://github.com/vibheksoni/stealth-browser-mcp). GitHub description: AI-driven network hooks and pixel-perfect UI cloning via chat |
| **Agent-specific primitive** | MCP tools for stealth sessions, CDP cloning, dynamic network hooks, instance state (`get_instance_state`) — not a human Selenium IDE |
| **Autonomy-compatible control plane** | After the MCP server is running, the agent calls `spawn_browser`, `navigate`, hooks, and extractors without a human driving Chrome |
| **M2M integration surface** | stdio/HTTP MCP, FastMCP, in-repo skill |
| **Identity / delegation** | Trust model: the **MCP client/agent is the security principal**. Recommended deployment is local stdio. HTTP must use `STEALTH_BROWSER_MCP_AUTH_TOKEN` and must not be exposed unauthenticated. File uploads are limited to allowlisted dirs |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`spawn_browser` / instance** | Stealth Chrome-family session with idle timeout and state inspection |
| **CDP execution** | JavaScript, raw CDP, pre-document scripts |
| **Element cloning** | Pixel-accurate CSS/DOM/events/assets extraction |
| **Dynamic hooks** | Restricted Python interceptors on the request/response path |
| **Network toolbox** | Headers, payloads, captured bodies for the agent |
| **Modular sections** | Enable 20–97 tools; `--xpool-safe` disables `Runtime.enable` CDP tools |

---

## Autonomy Model

```
Operator installs Chrome + the stdio MCP server
    -> Agent spawn_browser / navigate / interact via MCP tools
    -> Optional hooks mutate or fulfill traffic in-process
    -> Agent clones elements or reads captured network bodies
    -> close_instance or idle reaper tears the browser down
```

No per-click human confirmation after the client is attached.

---

## Identity and Delegation Model

- **Principal:** The connected MCP client. Treat it as full browser control (cookies, JS, hooks, local file upload from allowlisted paths).
- **No cloud agent identity:** Local OS user + optional HTTP bearer token.
- **Not authorization for third-party sites:** Stealth features may pass bot checks; they do not grant legal access to systems the operator may not use.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP stdio | `venv/bin/python src/server.py` |
| MCP HTTP | `--transport http` + `STEALTH_BROWSER_MCP_AUTH_TOKEN` |
| Agent skill | `skills/stealth-browser-mcp` |
| CLI flags | `--minimal`, `--disable-*`, `--list-sections`, `--debug` |

---

## Human-in-the-Loop Support

None required for tool calls. Humans install the browser and decide which MCP client may attach. The README's NodeMaven block is a paid sponsor placement, not part of the protocol.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Browser MCP / Playwright MCP** | Generic automation MCP. Official comparison: they lack nodriver stealth, CDP cloning, and the dynamic hook system |
| **Browserbase / Browser Use Cloud** | Hosted remote browsers. This is a local anti-detect MCP, not a session cloud |
| **Raw Puppeteer** | Library for developers, not an MCP tool surface with instance lifecycle and agent-oriented network hooks |

---

## Use Cases

- **Bot-gated sites** — agent-driven Chrome where Playwright MCP is commonly blocked (upstream's point-in-time claim)
- **UI cloning** — extract a component's CSS/DOM through chat
- **API reverse engineering** — inspect captured request/response bodies via MCP tools
- **Local trusted automation** — stdio-only deployment so the browser never leaves the operator machine
