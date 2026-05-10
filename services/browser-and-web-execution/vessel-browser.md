# Vessel Browser

> **"Built from the ground-up for agents, Vessel Browser is an open source AI browser for Linux/Windows that provides a durable state, MCP control, and BYOK with full autonomous browsing."**

| | |
|---|---|
| **Website** | https://github.com/unmodeled-tyler/vessel-browser |
| **Docs** | https://github.com/unmodeled-tyler/vessel-browser#readme |
| **GitHub** | https://github.com/unmodeled-tyler/vessel-browser |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution](README.md) |
| **Status** | Open source · Linux AppImage / npm · early-stage but agent-first by design |

---

## Official Website

https://github.com/unmodeled-tyler/vessel-browser

---

## Official Repo

https://github.com/unmodeled-tyler/vessel-browser

---

## How to Use (Agent Onboarding)

```
# Linux AppImage:
download AppImage from releases → chmod +x → run

# npm:
npm install -g vessel-browser
vessel-browser --mcp   # exposes MCP server for any MCP-compatible agent
```

Designed to plug into Hermes Agent or OpenClaw out of the box, or any agent that speaks MCP / brings its own LLM key (BYOK).

---

## Agent Skills

**Status:** ⚠️ Not yet published.

Search:

```bash
npx clawhub@latest search vessel-browser
```

---

## MCP

**Status:** ✅ Available — MCP control plane is a first-class feature.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/unmodeled-tyler/vessel-browser |
| **Transport** | stdio |
| **Compatible Clients** | Claude Desktop, Cursor, Hermes Agent, OpenClaw, any MCP host |

---

## What It Does

Vessel Browser is a Chromium-based browser whose primary user is an AI agent. It exposes named, **persistent ("durable") browser sessions** that survive restarts, with a human-visible supervisory UI on top so operators can watch what the agent is doing without taking control. Distinguishing primitives include **action undo** (rewind a misclick the agent made), **checkpoints** (snapshot a tab's state and roll back to it), and **editable bookmarks** that the agent reads and writes.

The browser is BYOK — operators connect their own LLM provider — and the data plane (DOM, screenshots, action calls) is mediated through MCP, so any MCP-compatible agent runtime can drive it without a per-agent integration.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repo tagline opens with *"Built from the ground-up for agents"* |
| **Agent-specific primitive** | Durable named sessions, action undo, checkpoints, agent-readable bookmarks — none of these have meaningful human-facing equivalents in Chrome / Edge |
| **Autonomy-compatible control plane** | Agent drives the browser via MCP; the human-visible UI is for oversight, not operation |
| **M2M integration surface** | MCP server + npm CLI + AppImage; no SaaS dashboard in the operational path |
| **Identity / delegation** | Each named session is its own identity (cookies, storage, BYOK key scope); operator can spin up many in parallel |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Durable Session** | Named browser session with persistent cookies / storage that survives restarts |
| **Action Undo** | Rewind the last DOM action the agent took |
| **Checkpoint** | Snapshot a tab's state; restore later |
| **Agent-Editable Bookmarks** | Bookmarks are first-class data the agent reads and writes |
| **MCP Control** | Full browser control surface exposed over MCP stdio |
| **BYOK** | Operator provides the LLM API key; no LLM lock-in |

---

## Autonomy Model

1. Operator runs `vessel-browser --mcp`; configures the agent's MCP host to point at it.
2. Agent calls MCP tools to open / focus / navigate a named session.
3. As the agent acts, every action is recorded; undo and checkpoint are agent-callable tools.
4. Operator watches the supervisory UI (optional); does not click on the agent's behalf.

---

## Identity and Delegation Model

- A named session encapsulates one identity: cookies, local storage, login state.
- Multiple sessions run in parallel with isolated state.
- BYOK means each operator's LLM credentials never leave their machine.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP (stdio) | Browser control tools: navigate, click, type, screenshot, undo, checkpoint, bookmarks |
| CLI | `vessel-browser` for session lifecycle management |
| Linux AppImage / Windows | Local install; no cloud dependency |

---

## Human-in-the-Loop Support

The supervisory UI is the HITL surface: an operator can watch the agent's browser in real time and pause / take over. Action undo lets a human or the agent itself revert mistakes without restarting a session.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Chrome + Playwright** | No durable named-session abstraction, no action undo, no agent-editable bookmarks; primary user is a human dev |
| **Browserbase / Steel** | Cloud-only, less suited for desktop autonomy with BYOK and local supervisory UI; different design center |
| **Lightpanda** | Headless / fast crawl focus; not designed for stateful interactive browsing with human-visible oversight |

---

## Use Cases

- **Long-running web autonomy** — agent maintains a logged-in session over days, surviving restarts
- **Reversible agent shopping / booking** — checkpoint before high-stakes actions; undo if the agent picks the wrong option
- **Local-first browser autonomy** — privacy-sensitive tasks where the data must not leave the operator's machine
- **MCP-driven browser tooling** — any MCP host (Claude Desktop, Hermes, OpenClaw) gets a browser without a vendor SDK
