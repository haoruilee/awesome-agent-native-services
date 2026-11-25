# Mandala Computer

> **"Computers for AI Agents."**

| | |
|---|---|
| **Website** | https://mandala.computer |
| **Docs** | https://app.mandala.computer/docs |
| **GitHub** | No public product monorepo (hosted service is closed-source) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | Hosted service closed-source. Local MCP package `mandala-computer-mcp` on npm |
| **Latest-month signal** | Checked 2026-11-25: [homepage](https://mandala.computer) HTTP 200, title "Mandala Computer — Computers for AI Agents"; [llms.txt](https://mandala.computer/llms.txt) and [API docs](https://app.mandala.computer/docs) HTTP 200; MCP GET [https://app.mandala.computer/mcp](https://app.mandala.computer/mcp) 401 |
| **Verified at** | 2026-11-25 |

---

## Official Website

https://mandala.computer

Title: *"Mandala Computer — Computers for AI Agents."* H1: *"Give your agent a computer."* Meta description: *"Persistent cloud computers your AI agents can see, control, and operate. Real desktops, not headless browsers."* `llms.txt`: *"Full cloud computers your AI agents can see, control, and operate."*

The desktop is persistent Linux. macOS is available on request. Windows is not generally offered yet.

---

## Official Repo

No public product monorepo is published. The hosted service is closed-source.

The local stdio MCP package is `mandala-computer-mcp` on npm (`npx mandala-computer-mcp`). That package is a client of the hosted API, not the computer fleet.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** hosted MCP with browser OAuth, or a human-minted API key. Not a one-URL join.

Key minting is not on the MCP tool surface. A person signs in through hosted MCP OAuth, or creates a `com_…` key and the agent sends it as a bearer token.

```bash
# Hosted MCP: https://app.mandala.computer/mcp
# Local stdio: npx mandala-computer-mcp
```

GET https://app.mandala.computer/mcp returned 401 on 2026-11-25 with a JSON-RPC authorization error (OAuth or Bearer). API reference: https://app.mandala.computer/docs (HTTP 200; *"Create, control and snapshot cloud computers over HTTP."*).

---

## Agent Skills

**Status:** ⚠️ Not yet published

No official `SKILL.md` or `npx skills add` package was found on the pages reviewed on 2026-11-25.

Search community skills: `npx clawhub@latest search mandala-computer`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — hosted Streamable HTTP, plus a local stdio package

| Detail | Value |
|---|---|
| **MCP Repo** | No product monorepo. Local package: `mandala-computer-mcp` |
| **Endpoint** | `https://app.mandala.computer/mcp` |
| **Transport** | Streamable HTTP, or stdio via `npx mandala-computer-mcp` |
| **Auth** | Browser OAuth, or `Authorization: Bearer com_…` |
| **Live check** | GET returned 401 on 2026-11-25 (authorization required) |
| **Docs** | https://app.mandala.computer/docs |
| **Compatible Clients** | Remote MCP clients that can OAuth or send a bearer token; stdio clients that can run npx |

The hosted MCP exposes most of the HTTP API, including screenshot, input, exec, windows, clipboard, and snapshots.

---

## What It Does

Mandala Computer is a persistent cloud desktop for an agent. `llms.txt` describes creating a Linux machine, watching the screen, clicking and typing, running commands, opening a terminal, moving files, and snapshotting. Each computer has a websocket event stream, and webhooks can POST the same events. A built-in agent loop can drive a computer from one prompt, with threads and background runs (`POST /computers/{id}/agent/runs` in `llms.txt`). Public HTTPS URLs can front a port inside the computer.

The computer stays. It is not a headless browser session and not a one-shot sandbox that disappears with the process.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Title: *"Computers for AI Agents."* H1: *"Give your agent a computer."* `llms.txt`: *"Full cloud computers your AI agents can see, control, and operate. Real desktops, not headless browsers."* Source: https://mandala.computer and https://mandala.computer/llms.txt |
| **Agent-specific primitive** | A computer lifecycle plus screenshot, input, exec, windows, clipboard, and snapshots, with an optional in-product agent thread. |
| **Autonomy-compatible control plane** | After OAuth or a `com_…` key, the agent creates and drives the computer with no per-action click. Key minting stays with the person. |
| **M2M integration surface** | HTTP API (https://app.mandala.computer/docs), hosted MCP, local stdio MCP, websockets, and webhooks (`llms.txt`). |
| **Identity / delegation** | Account OAuth or a bearer key the person minted. The agent operates that account's computers. Keys are not minted by an MCP tool. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Computer** | Persistent Linux desktop (macOS on request; Windows not generally offered). |
| **Screen and input** | Screenshot, click, type, windows, clipboard. |
| **exec** | Commands and an interactive terminal inside the computer. |
| **Snapshot** | Save the machine. `llms.txt` also keeps agent-run screenshots for replay, with retention limits. |
| **Agent thread** | Optional built-in loop: one prompt, background runs, 60-minute wall-clock cap (`llms.txt`). |

---

## Autonomy Model

1. A person completes hosted MCP OAuth, or creates a `com_…` key outside the tool list.
2. The agent calls the HTTP API or the MCP server to create a computer.
3. The agent screenshots, clicks, types, and execs until the task is done.
4. The computer persists. The agent snapshots it when it needs a restore point.

---

## Identity and Delegation Model

- The account is a person's Mandala account. The agent is a bearer of that account's OAuth token or `com_…` key.
- Minting a key is not an MCP tool, so an agent that only has the MCP session cannot create a new key from the tool list.
- Webhooks and the event stream attribute computer events to that computer id.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP API | https://app.mandala.computer/docs |
| Hosted MCP | `https://app.mandala.computer/mcp` |
| Local MCP | `npx mandala-computer-mcp` |
| Index | https://mandala.computer/llms.txt |
| Events | Websocket stream and webhooks (`llms.txt`) |

---

## Human-in-the-Loop Support

Browser OAuth is a human sign-in. Creating a `com_…` key is a human step. After either, desktop actions do not require a per-action click. The dashboard can replay an agent run. That replay is not an approval gate.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A headless browser** | The product is a persistent desktop (screen, shell, files, windows), which `llms.txt` distinguishes from a browser session. |
| **Orgo / box by Simular / E2B Desktop** | Other computer-use vendors. Mandala's computer API, `com_…` keys, and macOS-on-request offer are its own. |
| **The npm package alone** | `mandala-computer-mcp` is a local client. It does not run the desktop. |

---

## Use Cases

- **A desktop that is still there tomorrow** — the agent returns to the same Linux machine, files included.
- **Screenshot, shell, and clipboard in one API** — GUI steps and `exec` on the same computer.
- **A client that only speaks stdio** — `npx mandala-computer-mcp` with a key the person already created.
