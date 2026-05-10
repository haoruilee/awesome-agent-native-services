# Vexa

> **"Open-source meeting transcription API for Google Meet, Microsoft Teams & Zoom. Auto-join bots, real-time WebSocket transcripts, MCP server for AI agents. Self-host or use hosted SaaS."**

| | |
|---|---|
| **Website** | https://vexa.ai |
| **Docs** | https://github.com/Vexa-ai/vexa#readme |
| **GitHub** | https://github.com/Vexa-ai/vexa |
| **Classification** | `agent-native` |
| **Category** | [Meeting & Conversation](README.md) |
| **Stars** | 2,000+ · explicit open-source alternative to Recall.ai / Otter.ai / Fireflies.ai |

---

## Official Website

https://vexa.ai

---

## Official Repo

https://github.com/Vexa-ai/vexa

---

## How to Use (Agent Onboarding)

```
# Self-hosted:
git clone https://github.com/Vexa-ai/vexa
cd vexa && docker compose up -d

# Or hosted SaaS via vexa.ai

# Send a bot to a meeting:
curl -X POST https://<host>/v1/bots \
  -H "X-API-Key: $KEY" \
  -d '{"meeting_url":"https://meet.google.com/abc-defg-hij","platform":"google_meet"}'
```

For agent runtimes, point any MCP host at Vexa's MCP server — 17 tools cover join / transcribe / speak / share-screen.

---

## Agent Skills

**Status:** ⚠️ Not yet published.

```bash
npx clawhub@latest search vexa
```

---

## MCP

**Status:** ✅ Available — first-party MCP server with 17 tools.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/Vexa-ai/vexa (subdirectory) |
| **Transport** | stdio / Streamable HTTP |
| **Compatible Clients** | Claude Desktop, Cursor, Windsurf, any MCP host |

---

## What It Does

Vexa is an **open-source meeting bot platform** that lets an agent send a bot into Google Meet, Microsoft Teams, or Zoom, capture real-time diarized transcripts (REST + WebSocket), and — distinctively — let the bot **speak and share its screen** mid-meeting. The MCP server exposes 17 tools so any MCP-compatible agent (Claude Desktop, Cursor, etc.) can drive the bot end-to-end.

It is positioned by its maintainers as an explicit open-source alternative to Recall.ai / Otter.ai / Fireflies.ai. The differentiators against the existing entries in this catalog (Recall.ai, Meeting BaaS, MeetStream — all SaaS) are:

- **Self-host** — data never leaves your infrastructure.
- **Interactive bot** — the bot can speak (TTS) and share content, not just listen.
- **First-party MCP** — 17 tools usable from any MCP host without writing REST glue.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repo description includes *"MCP server for AI agents"* and explicitly markets the bot as agent-driven |
| **Agent-specific primitive** | Programmable meeting bot lifecycle, real-time WebSocket transcript with speaker diarization, in-meeting speak / share-screen as MCP tools |
| **Autonomy-compatible control plane** | Bot is dispatched via API; calendar-trigger or webhook-trigger workflows; no human button click in the meeting flow |
| **M2M integration surface** | REST + WebSocket + MCP server (17 tools) |
| **Identity / delegation** | Each bot run has its own ID; per-tenant API keys; audit log of all transcripts and actions |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Meeting Bot Lifecycle** | Spawn / join / leave / cancel; per-bot ID |
| **Real-time Transcript** | WebSocket stream of diarized utterances |
| **In-meeting Speech** | Bot speaks via TTS while in the meeting |
| **Screen Share** | Bot shares its own content into the meeting |
| **MCP Toolset (17 tools)** | Direct agent control of all of the above |
| **Self-hosted runtime** | Docker Compose / Kubernetes |

---

## Autonomy Model

1. Agent calls `POST /v1/bots` (or the equivalent MCP tool) with a meeting URL.
2. Bot joins; WebSocket starts streaming diarized transcript.
3. Agent can call MCP tools to make the bot speak, share screen, or send chat into the meeting.
4. Agent calls `DELETE /v1/bots/{id}` to remove the bot.

No human click in the meeting; calendar-triggered dispatch is supported.

---

## Identity and Delegation Model

- Each bot run has a unique ID.
- Per-tenant API keys.
- Optional bot display name; can carry a per-agent identity into the meeting.
- Audit log: full transcript + every action the bot took.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Bot CRUD, transcript download |
| WebSocket | Real-time diarized transcript stream |
| MCP server | 17 tools for full bot control |
| Self-host | Docker Compose / Helm |
| Hosted SaaS | vexa.ai |

---

## Human-in-the-Loop Support

Operator UI shows live bot status; bot can be dismissed or reconfigured at any time. Speech / screen-share actions can be gated behind HumanLayer / Inferable approvals.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Recall.ai / Meeting BaaS / MeetStream** | Excellent SaaS APIs (already in this catalog) — Vexa differs by being self-hostable + having an interactive (speaking, screen-sharing) bot + first-party MCP |
| **Calling Zoom SDK directly** | No agent-shaped lifecycle, no diarized real-time transcript, no MCP, no out-of-the-box TTS path |
| **Otter.ai / Fireflies** | Human-facing transcription products; bots are batch-recording, not agent-driven actors |

---

## Use Cases

- **Agent attendee** — agent joins a meeting, transcribes, speaks summary at the end, posts notes
- **Compliance recording** — self-hosted Vexa keeps audio + transcript inside the tenant's perimeter
- **Multi-meeting parallelism** — fleet of bots on dozens of meetings; each one driven by a separate agent run
- **MCP-native voice copilot** — Claude Desktop / Cursor agents drive the bot directly via the 17-tool MCP server
