# kwant

> **"Your own team of AI bots in one self-hosted binary: spaces, every account you have, handoffs, approvals and routines. Open-source, self-hosted alternative to Grok Bot, Claude Duet and OpenAI dots."**

| | |
|---|---|
| **Website** | https://kwant.si |
| **Docs** | https://kwant.si/docs/quickstart |
| **GitHub** | https://github.com/alexsergivan/kwant |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/alexsergivan/kwant?style=social)](https://github.com/alexsergivan/kwant) |
| **Classification** | `agent-native` |
| **Category** | [Agent Harnesses & Operator Surfaces](README.md) |
| **License** | AGPL-3.0 |
| **Disclosure** | Proposed by [alexsergivan](https://github.com/alexsergivan), who disclosed being the author of kwant |
| **Latest-month signal** | [0.8.2](https://github.com/alexsergivan/kwant/releases/tag/mac-v0.8.2) released 2026-11-10; 472 stars; AGPL-3.0; [kwant.si](https://kwant.si) returned HTTP 200. Operator-surface evidence is pinned to commit [2c93196](https://github.com/alexsergivan/kwant/commit/2c931968680ce26d65ec79e08cbf2527c0d2d25f) |
| **Verified at** | 2026-11-10 |

---

## Official Website

https://kwant.si

---

## Official Repo

https://github.com/alexsergivan/kwant

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + HTTP/SSE daemon (`kwnt serve`)

kwant is an AGPL-3.0, open-source, self-hosted team of AI bots in one Rust binary. A person installs it and adds an AI account they already have. The quickest server path:

```bash
curl -fsSL https://kwant.si/install.sh | sh
kwnt serve
```

Desktop apps for Mac, Linux (beta), and Windows (beta) use the same `~/.kwnt` data folder as `kwnt serve`. Docs: [quickstart](https://kwant.si/docs/quickstart) and [install](https://kwant.si/docs/install).

After the daemon is running, a person can create a scoped inbound MCP connection under **Settings → All spaces → Coding agents**, so Claude Code, Codex, Cursor, or another MCP client can ask selected kwant bots for work at `https://<server>/api/mcp/agents`. The token is shown once, only reaches the spaces and bots the person picked, and cannot approve work or act as the operator. See [Use kwant from your coding agent](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/agents-connect.md).

Reading a document does not register an agent or grant operator rights. This is not a one-URL join path.

---

## Agent Skills

**Status:** ⚠️ Not yet published as an `npx skills add` package

kwant *consumes* skills per bot. The operator approves new skills. That is not a portable join package for this catalog.

Search community skills: `npx clawhub@latest search kwant`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

Inbound MCP so a coding agent can ask a kwant bot for work. It is not a general operator API.

| Detail | Value |
|---|---|
| **MCP Repo** | Documented in https://github.com/alexsergivan/kwant (`docs/agents-connect.md`). No hosted public MCP URL |
| **Transport** | Streamable HTTP at `/api/mcp/agents` |
| **Auth** | Person-minted bearer token (`kag_…`), scoped to chosen spaces and bots, shown once, revocable |
| **Tools** | `list_bots`, `ask`, `get_reply`, `list_threads` |
| **Compatible Clients** | Claude Code, Codex, Cursor, and other MCP clients that can call a streamable HTTP server |
| **Boundary** | The outside agent is never the operator. It cannot approve anything, act as the person, or call any kwant address other than `/api/mcp/agents` (403 elsewhere, even from the same machine) |

---

## What It Does

kwant is a self-hosted operator surface and harness for a team of named AI bots in one Rust binary (`kwnt`). It runs on a Mac, Linux or Windows (beta) computer, or on a VPS. Bots share chats, hand work to each other with an @mention, and continue on a schedule or while the person is away. Work shows up as cards on a Mission board, and a task turns **Verified** only when kwant runs the check itself. Spaces keep separate bots, accounts, approvals, and routines. Live activity streams what a concrete bot turn is doing — thinking, each tool, waiting for approval or for the person — over SSE, and keeps that state on the reply after a reload.

The primary consumer is the human operator of that bot team. The primary interface is the local app or `kwnt serve` plus CLI. This entry is admitted on the **operator-surface track**.

---

## Why It Is Agent-Native

Operator-surface track (not the standard five infrastructure criteria). Quotes and source URLs below are pinned to kwant commit [`2c93196`](https://github.com/alexsergivan/kwant/commit/2c931968680ce26d65ec79e08cbf2527c0d2d25f), as requested after the Go on [#311](https://github.com/haoruilee/awesome-agent-native-services/issues/311#issuecomment-6783980008). Full evidence comment: https://github.com/haoruilee/awesome-agent-native-services/issues/311#issuecomment-6762975805

| Requirement | Evidence |
|---|---|
| **Agent-operations-first** | Built as a team of AI bots to operate, not a general application dashboard. README: "Your own team of AI bots that check each other’s work before saying “done”." — [README.md#L5](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L5) |
| **Agent-specific live state** | Live activity for thinking, each tool, and waits for approval or for the person, streamed over SSE; Mission-board verification; account usage fallback — [docs/live-activity.md#L6-L7](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/live-activity.md#L6-L7), [README.md#L35](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L35), [README.md#L63](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L63) |
| **Session attribution** | Turn events are scoped with `turn_id`, `kwant_id`, `context_id`, and (in threads) `thread_id`. `get_reply` looks up a turn by `turn_id` and returns `thread_id` and `turn_id` — [docs/live-activity.md#L11-L12](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/live-activity.md#L11-L12), [docs/agents-connect.md#L75](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/agents-connect.md#L75), [docs/agents-connect.md#L84](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/agents-connect.md#L84) |
| **Dedicated operational surface** | `kwnt` CLI starts the HTTP/SSE server and embedded UI (`kwnt serve`); same binary as a systemd unit; desktop app shares `~/.kwnt` — [src/main.rs#L6](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/src/main.rs#L6), [src/main.rs#L21-L22](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/src/main.rs#L21-L22), [README.md#L153](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L153), [README.md#L193](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L193), [README.md#L118](https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L118) |
| **Honest boundary** | Approvals, skills, MCP tool servers, and autonomy *are* present (see quotes below). What is absent or limited: the primary surface remains the local app / `kwnt serve` for the human operator; inbound MCP cannot approve, act as the operator, or reach the rest of the API; bots run on the operator's own accounts, not a separate delegated credential of their own |

### Evidence quotes (pinned to `2c93196`)

**1. Explicitly built to operate or supervise AI agents, not general applications**

> Your own team of AI bots that check each other’s work before saying “done”.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L5

> kwant gives you a team of bots that share chats, hand work to each other with an @mention and get it done on their own, on a schedule or while you're away.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L35

> How is it different from Grok Bot, Claude Duet or OpenAI dots? It's the same idea, a team of named bots you message, but open source, running on your own computer or server, with any of your accounts.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L279

**2. Continuously interprets agent-specific state**

> Live activity: what a bot is doing while it works (thinking, each tool it runs, waits for approval or for the person), streamed over SSE and kept on the reply after a reload.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/live-activity.md#L6-L7

> Work shows up as cards on a Mission board, and a task turns **Verified** only when kwant runs the check itself, never on a bot's word.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L35

> When an account runs out of usage, the turn moves to the next one and the chat says so.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L63

**3. Attributes that state to a concrete agent session or rollout**

> Turn events are *scoped*: `turn_id`, `kwant_id`, `context_id` and (in threads) `thread_id` sit next to `type`.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/live-activity.md#L11-L12

> `get_reply` | Checks a turn that `ask` started, by `turn_id`.
>
> Each answer is `{status, reply_text, attachments, thread_id, turn_id}`.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/agents-connect.md#L75
https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/agents-connect.md#L84

**4. Exposes a dedicated operational surface such as a CLI, wrapper, daemon, hook, or status-line protocol**

The `kwnt` CLI starts the HTTP/SSE server and embedded UI:

> about = "kwant bots: your team of AI bots"
>
> /// Start the Kwants HTTP/SSE server and embedded web UI
> Serve {

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/src/main.rs#L6
https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/src/main.rs#L21-L22

> ./target/release/kwnt serve

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L153

As a systemd unit:

> ExecStart=/usr/local/bin/kwnt serve --host 0.0.0.0 --port 8799

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L193

The desktop app uses the same data dir as the daemon:

> It runs its own kwant on your Mac, with the same `~/.kwnt` data folder as `kwnt serve`, and stays in the menu bar when you close the window.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L118

**5. Documents honestly when autonomy, machine APIs, delegated credentials, approval enforcement, Skills, or MCP are absent**

Several of those are present in kwant, not absent.

Approvals are enforced, and only the person can change the mode or answer cards:

> Only the person changes it: `PUT /api/spaces/:id/approvals` and `PUT /api/kwants/:id/approvals` with `{"approvals": "ask" | "smart" | "off"}` (a bot also takes `inherit`). Bots' own tools refuse it.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/approvals.md#L4-L6

> Person-only routes (sign-in links, saved passwords and the vault, answering approval cards, the approvals switch, deleting a bot or team, undo, Loose ends, Parallel Universe, letters) refuse a bot's turn token, or any bearer that isn't the API token, with 403 from anywhere.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/llm-profiles.md#L103-L106

> Whatever the mode, a call that looks like a payment shows a card, even when `smart` finds it safe or "Always this session" was given

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/approvals.md#L19-L20

Skills and MCP for the bots are present:

> memory and skills per bot (you approve new skills), … MCP tool servers

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L70

Autonomy is present, with a safety net the person controls:

> Autonomous, with a safety net you control. Ordinary work runs without stopping.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L65

What is absent or limited, as documented:

The primary surface is still the local app / `kwnt serve` for the human operator. There is an inbound MCP at `/api/mcp/agents` so a coding agent can ask a kwant bot for work, but it cannot approve, act as the operator, or reach the rest of the API:

> The outside agent is never you. A bot sees its messages marked as coming from that agent, and the agent can't approve anything.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/agents-connect.md#L8-L9

> Approve anything. Approvals, questions and anything else that needs you go to you in kwant, exactly as they do today. The agent only sees that the turn is waiting.
>
> Act as you. Its messages are stored and shown as the agent's, and the bot is told they aren't from you.
>
> Reach anything else. The token only works on `/api/mcp/agents`. On every other kwant address it gets a 403, even from the same machine. It can't read passwords, change settings, manage connections or send chat messages as you.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/docs/agents-connect.md#L94-L99

Bots also run on the operator's own accounts, not a separate delegated credential of their own:

> Run it as an app on your Mac, Linux or Windows (beta) PC, or on a server, with the Claude, Codex or Grok CLI you already use, or your own API keys.

https://github.com/alexsergivan/kwant/blob/2c931968680ce26d65ec79e08cbf2527c0d2d25f/README.md#L35

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Named bot team** | Bots with roles share chats and hand work on with an @mention |
| **Spaces** | Separate bots, accounts, approvals, and routines per space |
| **Live activity** | Thinking, tool calls, and waits for approval or for the person, scoped to a turn and streamed over SSE |
| **Mission board verification** | A task turns Verified only when kwant runs the check itself, never on a bot's word |
| **Enforced approvals** | Person-only approval mode and cards; payments always show a card |
| **Routines** | Scheduled work while the person is away, with an Inbox of what is waiting, finished, or failed |
| **Account fallback** | When an account runs out of usage, the turn moves to the next one and the chat says so |
| **Inbound coding-agent MCP** | A scoped token can ask selected bots for work; it cannot approve or act as the operator |

---

## Autonomy Model

```
Operator installs kwant (desktop app or `kwnt serve`) and adds an existing Claude, Codex, or Grok CLI login, or an API key
    -> Ordinary bot work runs without stopping, including @mention handoffs and routines
    -> Live activity attributes thinking, tools, and waits to a concrete turn_id / kwant_id / context_id
    -> Risky steps can raise a person-only approval card; payments always ask
    -> A Mission-board task turns Verified only when kwant itself runs the check
    -> Optional: a coding agent asks a selected bot over `/api/mcp/agents` and polls `get_reply`
    -> If the turn is waiting_on_person, the coding agent only sees that it is waiting; the person answers in kwant
```

---

## Identity and Delegation Model

- **Bot and turn identity:** Live events carry `turn_id`, `kwant_id`, `context_id`, and (in threads) `thread_id`.
- **No separate delegated credential:** Bots run on the operator's own Claude, Codex, or Grok CLI logins, or on API keys the operator added. There is no distinct agent-owned payment or account credential.
- **Person-only authority:** Changing approval mode, answering approval cards, the vault, sign-in links, and other operator routes refuse a bot's turn token (403).
- **Inbound MCP identity:** A coding-agent connection has its own token and name. Messages are stored and shown as that agent's, not as the operator's. The token only works on `/api/mcp/agents`.
- **Disclosure:** This entry was submitted by [alexsergivan](https://github.com/alexsergivan), the author of kwant.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI / daemon | `kwnt serve` starts the HTTP/SSE server and embedded web UI |
| Desktop app | Mac, Linux (beta), and Windows (beta); same `~/.kwnt` data folder as the daemon |
| systemd | `ExecStart=/usr/local/bin/kwnt serve --host 0.0.0.0 --port 8799` |
| HTTP/SSE | Live activity and the embedded UI against the local or VPS server |
| REST (person) | Person-only routes such as approval mode switches; bots' own tools refuse them |
| Inbound MCP | Streamable HTTP at `/api/mcp/agents` with a scoped bearer token |
| Install | `curl -fsSL https://kwant.si/install.sh \| sh`, desktop downloads, or Docker Compose |

---

## Human-in-the-Loop Support

HITL is enforced, not observational only. Approval modes are `ask`, `smart`, or `off` (a bot may `inherit`). Only the person can change the mode or answer cards. Ordinary work can run without a click. Payments always show a card, even when `smart` finds the call safe or "Always this session" was given. A coding agent using inbound MCP cannot approve; those cards stay in kwant for the person.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Grok Bot, Claude Duet, or OpenAI dots** | Same idea of a team of named bots, but hosted and closed. They are not a self-hosted open-source binary with person-only approval enforcement and local turn-scoped live activity |
| **Generic chat workspace** | A human chat tab. It does not attribute SSE live activity to a `turn_id`, verify Mission-board work itself, or expose `kwnt serve` as the operator daemon |
| **Process monitor or host dashboard** | Shows CPU, memory, and process names. It does not interpret bot tool activity, approval waits, or account-quota fallbacks for a concrete kwant session |

---

## Use Cases

- **Self-hosted bot team** — run named bots in spaces, with @mention handoffs and routines, on a laptop or VPS
- **Watch a live turn** — see thinking, each tool, and waits for approval or for the person, still there after a reload
- **Verified work** — treat a Mission-board card as done only when kwant runs the check itself
- **Enforced approvals** — keep payment and other person-only cards in the operator's hands
- **Coding-agent handoff** — let Claude Code, Codex, or Cursor ask a selected bot for work over inbound MCP, without operator powers
