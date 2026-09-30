# AgentCall

> **"Your AI agent, in every meeting."**

| | |
|---|---|
| **Website** | https://agentcall.dev |
| **Docs** | https://github.com/pattern-ai-labs/agentcall#readme |
| **GitHub** | https://github.com/pattern-ai-labs/agentcall |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/pattern-ai-labs/agentcall?style=social)](https://github.com/pattern-ai-labs/agentcall) |
| **Classification** | `agent-native` |
| **Category** | [Meeting & Conversation Services](README.md) |
| **License** | MIT (skill package) |
| **Latest-month signal** | Last GitHub push 2026-09-15; latest release v1.1.15 (2026-07-01); MIT; `SKILL.md`, `.claude-plugin/`, and `gemini-extension.json` still present; [agentcall.dev](https://agentcall.dev) HTTP 200 (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

https://agentcall.dev

Dashboard / API keys: https://app.agentcall.dev

---

## Official Repo

https://github.com/pattern-ai-labs/agentcall

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Agent Skill` (not an SDK)

Homepage: ask the agent to install `join-meeting` from `github.com/pattern-ai-labs/agentcall`, or:

```text
/plugin marketplace add pattern-ai-labs/agentcall
/plugin install join-meeting@agentcall
```

Other official paths from the README: `openclaw skills install join-meeting`, Cursor `/add-plugin`, Gemini `gemini extensions install https://github.com/pattern-ai-labs/agentcall`, or clone and point the host at `SKILL.md`.

On first run with no key, the skill can register via a one-time email code, or the operator pastes a key from https://app.agentcall.dev/api-keys. Then: *"Join this meeting: https://meet.google.com/…"*.

---

## Agent Skills

**Status:** ✅ Available

The repository *is* the skill (`SKILL.md` + Python/Node bridges). Claude Code plugin name: `join-meeting@agentcall`.

| Skill | What It Teaches the Agent |
|---|---|
| `join-meeting` | Join Meet/Zoom/Teams as a voice bot; talk, listen, screenshot, screenshare, chat, leave |

---

## MCP

**Status:** ⚠️ Not published

The machine surface is the skill plus REST/WebSocket at `api.agentcall.dev`. No official MCP server is documented.

Search community skills: `npx clawhub@latest search agentcall`. See: https://agentskills.io/specification

---

## What It Does

AgentCall turns a coding agent into a meeting participant. The bot talks (TTS), listens (live transcripts), can screenshot or screenshare, shows an optional avatar, and keeps the agent's full local context — it can still search code and run commands while in the call. Platforms: Google Meet, Zoom, Microsoft Teams. Distributed as an Agent Skill, not a human-imported client library.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: **"Your AI agent, in every meeting."** README: **"Let any AI agent join and participate in video meetings via voice."** — [agentcall.dev](https://agentcall.dev), [repo](https://github.com/pattern-ai-labs/agentcall) |
| **Agent-specific primitive** | Meeting as an I/O channel: transcript events in, `tts.speak` / screenshot / screenshare commands out, while the same agent keeps its coding tools |
| **Autonomy-compatible control plane** | After API key persist (`~/.agentcall/config.json`), "join this URL" is enough. No human operates a Zoom client for the bot |
| **M2M integration surface** | Skill + REST/WSS (`ak_ac_` keys) at `api.agentcall.dev` |
| **Identity / delegation** | Bot joins as the AgentCall participant; key is per operator account (skill can create the account). Events/commands are call-scoped. Not a KYA token for the human attendees |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Join-meeting skill** | Host-native install; subprocess + stdout protocol |
| **Call events** | `transcript.final`, participant join/leave, `tts.done` / interrupted, `call.bot_ready`, `call.ended` |
| **Call commands** | `tts.speak`, chat, screenshot, webpage/avatar, screenshare, leave |
| **Modes** | `audio`, `webpage-av`, `webpage-av-screenshare` |
| **Voice strategies** | `direct` TTS vs `collaborative` GetSun timing |

---

## Autonomy Model

```
Install join-meeting skill
    -> first run: skill registers or stores API key
    -> agent is told a meeting URL
    -> bot joins; transcripts stream to the agent
    -> agent speaks, chats, screenshots, or presents without a human driving the client
    -> leave / call.ended
```

---

## Identity and Delegation Model

- **Account key:** `ak_ac_` prefix, stored at `~/.agentcall/config.json`.
- **Bot presence:** The meeting sees the AgentCall bot, not the human's personal Zoom identity (beyond whatever the platform requires to inject a bot).
- **Session:** Crash recovery reconnects to an active call after agent restart.
- **Billing identity:** Operator account / plan; per-minute usage.
- **No attendee OAuth delegation product** beyond joining the meeting.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Skill / plugin | `join-meeting@agentcall`, OpenClaw, Gemini extension, raw `SKILL.md` |
| REST + WebSocket | `api.agentcall.dev` |
| Dashboard | https://app.agentcall.dev |

---

## Human-in-the-Loop Support

A human supplies the meeting URL (and sometimes the first API key / email code). During the call the agent is the participant. Collaborative mode uses GetSun for group timing; that is conversation intelligence, not an approval gate.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Human Zoom/Meet client** | A person must join and operate the UI |
| **Record-only meeting bot** | Transcripts after the fact; the coding agent is not a live speaker |
| **Generic WebRTC SDK** | You still build join, VAD, barge-in, and host skill wiring |

---

## Use Cases

- **Coding companion in standup** — talk about the repo while staying in the agent session
- **Support or training calls** — avatar + screenshare modes
- **Note-taking with voice replies** — audio-only mode
- **Crash-safe long calls** — reconnect after the agent restarts
