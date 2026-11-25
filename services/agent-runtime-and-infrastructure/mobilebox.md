# Mobilebox

> **"Mobile sandboxes for your AI agents."**

| | |
|---|---|
| **Website** | https://mobilebox.dev |
| **Docs** | https://mobilebox.dev/llms.txt |
| **GitHub** | https://github.com/mobilebox-dev/mobilebox |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | MIT for the public clients/docs/skills repo (Copyright 2026 fifteenA, Inc.); the hosted phone fleet is commercial |
| **Latest-month signal** | Checked 2026-11-25: [homepage](https://mobilebox.dev) HTTP 200, H1 "Mobile sandboxes for your AI agents."; [llms.txt](https://mobilebox.dev/llms.txt), [skill.md](https://mobilebox.dev/skill.md), [setup.md](https://mobilebox.dev/setup.md), and [OpenAPI](https://mobilebox.dev/openapi.json) HTTP 200; MCP GET [https://mobilebox.dev/mcp](https://mobilebox.dev/mcp) 401; [repo](https://github.com/mobilebox-dev/mobilebox) MIT, 1 star, pushed 2026-11-25T13:35:19Z |
| **Verified at** | 2026-11-25 |

---

## Official Website

https://mobilebox.dev

Homepage H1: *"Mobile sandboxes for your AI agents."* `llms.txt` lead: *"Mobile sandboxes for AI agents."* This is a different product from [Phonebox](phonebox.md) (`phonebox.dev`).

---

## Official Repo

https://github.com/mobilebox-dev/mobilebox

MIT, Copyright 2026 fifteenA, Inc.: https://github.com/mobilebox-dev/mobilebox/blob/main/LICENSE. The public repository is clients, docs, and skills (1 star, pushed 2026-11-25T13:35:19Z). The hosted phone fleet is a commercial service.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** agent-readable setup document + hosted MCP + REST. Not a one-URL join.

A person supplies an email. [setup.md](https://mobilebox.dev/setup.md) lets the agent mint a key at once for a new address; a 6-digit code from that inbox keeps the workspace. MCP OAuth (no key pasted) is a human Allow click. After that credential exists, taps and types do not each wait on a click. The hosted skill also asks for a yes before the first billed phone of a task unless a standing budget already covers it.

```bash
# Read https://mobilebox.dev/setup.md and follow it.
# MCP (Streamable HTTP): https://mobilebox.dev/mcp
#   Authorization: Bearer $MOBILESANDBOX_API_KEY
pip install mobilebox
```

Machine-readable entry points that returned HTTP 200 on 2026-11-25: https://mobilebox.dev/llms.txt, https://mobilebox.dev/skill.md, https://mobilebox.dev/openapi.json, https://mobilebox.dev/mcp/server-card, and https://mobilebox.dev/.well-known/ai-catalog.json. GET https://mobilebox.dev/mcp returned 401 with the setup instructions.

---

## Agent Skills

**Status:** ✅ Available — hosted `skill.md` (not an `npx skills add` registry package)

```bash
curl -fsSL https://mobilebox.dev/skill.md -o ~/.claude/skills/mobilebox/SKILL.md
```

| Skill | What It Teaches the Agent |
|---|---|
| `mobilebox` | Mint a key via setup.md, then create, observe, act on, and park a cloud phone (https://mobilebox.dev/skill.md) |

---

## MCP

**Status:** ✅ Available — hosted Streamable HTTP

| Detail | Value |
|---|---|
| **MCP Repo** | Hosted. Clients/docs: https://github.com/mobilebox-dev/mobilebox |
| **Endpoint** | `https://mobilebox.dev/mcp` |
| **Transport** | Stateless Streamable HTTP |
| **Auth** | `Authorization: Bearer` API key, or MCP OAuth (human Allow) |
| **Live check** | GET returned 401 on 2026-11-25; server card at https://mobilebox.dev/mcp/server-card returned 200 |
| **Compatible Clients** | Claude, Claude Code, Cursor, Codex, VS Code, Gemini CLI, goose, Windsurf, Cline, GitHub Copilot (named from `llms.txt`) |

`llms.txt` lists 22 tools, including `create_phone`, `observe`, `act`, `park_phone`, `screenshot`, `install_app`, and `watch_phone`.

---

## What It Does

Mobilebox is an agent-first cloud phone. The agent gets an Android 14 (arm64) sandbox, an iPhone or iPad simulator, or an optional real Android device, then reads the screen as numbered elements and taps, types, and swipes. `llms.txt`: *"Your agent supplies the reasoning; Mobilebox supplies the phone."*

Parked phones keep apps, data, and logins and are not billed. `llms.txt` states cloud Android at $0.01 per ready phone-minute (billed per second, one-minute minimum), large phones at $0.02, iPhone and iPad simulators at $0.03, and real Android devices at the cloud Android price. Check https://mobilebox.dev/llms.txt before relying on a price.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage H1: *"Mobile sandboxes for your AI agents."* `llms.txt`: *"Mobile sandboxes for AI agents."* Source: https://mobilebox.dev and https://mobilebox.dev/llms.txt |
| **Agent-specific primitive** | A phone the agent creates, observes, acts on, and parks (`create_phone` / `observe` / `act` / `park_phone`), including install and screen watch. A human remote-desktop session is not the API. |
| **Autonomy-compatible control plane** | After the key or OAuth Allow, the act loop does not require a per-tap click. Constraints: billed minutes, idle park (5 minutes) and default max duration, and the skill's ask-before-first-phone spend check. |
| **M2M integration surface** | REST `https://mobilebox.dev/v1`, OpenAPI, Python client `pip install mobilebox`, hosted MCP, `llms.txt`, and `skill.md`. |
| **Identity / delegation** | Workspace API key (`MOBILESANDBOX_API_KEY`) or MCP OAuth for the signed-in user. The agent acts on that workspace's phones. Watch links are for the user; proofs are unlisted public links. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Phone** | Cloud Android, iOS simulator (`platform: "ios"`), or real Android (`device: "real"`). Optional `size: "large"`. |
| **observe / act** | Numbered screen elements, then taps, typing, and swipes. Up to 20 actions per call (`llms.txt`). |
| **park_phone** | Shut the phone down and keep apps, data, and logins. Parked time is free. |
| **watch_phone** | Live view link for the user. The skill says not to post it in a shared channel. |

---

## Autonomy Model

1. The agent follows setup.md with an email the person supplied, or the MCP client completes OAuth Allow.
2. A 6-digit inbox code keeps the workspace when setup asks for it.
3. The agent creates a phone, observes, and acts until the task is done.
4. The agent parks or deletes the phone. Idle phones park after 5 minutes (`llms.txt`).

---

## Identity and Delegation Model

- The credential is a workspace API key or an MCP OAuth token for the human's Mobilebox user. The agent does not get a separate public agent identity.
- New workspaces get free credit; adding credits is a dashboard action.
- Screen-watch and proof links are capabilities: a watch link shows the phone, and a proof is reachable by anyone with the link for 30 days (`skill.md`).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST | `https://mobilebox.dev/v1` with the same bearer key |
| OpenAPI | https://mobilebox.dev/openapi.json |
| Python client | `pip install mobilebox` |
| Hosted MCP | `https://mobilebox.dev/mcp` |
| Machine-readable docs | https://mobilebox.dev/llms.txt · https://mobilebox.dev/skill.md · https://mobilebox.dev/setup.md |

---

## Human-in-the-Loop Support

Signup needs a human email and, to keep the workspace, a 6-digit inbox code. Keyless MCP connect needs an Allow click. The skill asks before the first billed phone of a task unless a budget already exists, and before publishing a proof. Driving the phone after that does not require a click per tap. `watch_phone` is optional viewing.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Phonebox** (already listed) | A separate hosted Android product at phonebox.dev, with its own key (`pbx_`), setup.md, and MCP. Mobilebox is mobilebox.dev. |
| **A human device farm or VNC** | No agent observe/act/park lifecycle, workspace key, or hosted MCP. |
| **Generic mobile test clouds** | Built for a person to run a test suite, not for an agent to own the phone loop. |

---

## Use Cases

- **App flows with no API** — the agent opens a mobile-only screen, taps through it, and parks the phone.
- **Install and check a build** — `install_app` on cloud Android, an iOS simulator `.zip`, or a real device.
- **Short billed sessions** — create, act, and park so idle time is not billed.
