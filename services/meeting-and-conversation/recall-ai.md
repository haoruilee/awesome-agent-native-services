# Recall.ai

> **"The meeting bot API for every platform."**

| | |
|---|---|
| **Website** | https://recall.ai |
| **Docs** | https://docs.recall.ai |
| **Meeting Bot API** | https://www.recall.ai/product/meeting-bot-api |
| **Calendar API** | https://www.recall.ai/product/calendar-integration-api |
| **Classification** | `agent-native` |
| **Category** | [Meeting & Conversation Services](README.md) |

---

## Official Website

https://recall.ai

---

## Official Repo

https://github.com/recallai — GitHub organization (SDKs and integration libraries)

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official skill published by Recall.ai yet.

Recall.ai does not currently publish a `SKILL.md`-based skill. Integration is via REST API and webhook events.

```bash
# No official install command yet — watch the GitHub org:
# https://github.com/recallai
```

> Note: `recallnet/recall-mcp` on npm is a different product (blockchain storage), not the Recall.ai meeting bot platform.

---

## MCP

**Status:** ⚠️ No dedicated MCP server from Recall.ai

Recall.ai does not currently publish a standalone MCP server. Integration is via REST API and webhook events. A third-party recall-themed MCP exists (`recallnet/recall-mcp`) but is for a different product (blockchain storage, not the meeting bot platform).

| Detail | Value |
|---|---|
| **API Docs** | https://docs.recall.ai |
| **Meeting Bot API** | https://www.recall.ai/product/meeting-bot-api |
| **Calendar API** | https://www.recall.ai/product/calendar-integration-api |
| **Primary Interface** | REST API + webhook events |

---

## What It Does

Recall.ai provides a unified API for deploying bots into Zoom, Google Meet, Microsoft Teams, Webex, Slack Huddles, and GoTo Meeting. Agents create bots via API, bots join scheduled or live meetings, and Recall.ai streams back real-time speaker-diarized transcripts, audio/video, and meeting metadata within 10 seconds — all without a human operating a meeting client.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The bot *is* the agent's presence in the meeting; the entire API is designed for programmatic bot lifecycle management |
| **Agent-specific primitive** | Meeting bot with autonomous lifecycle; real-time diarized transcript stream; calendar event trigger; per-event bot configuration |
| **Autonomy-compatible control plane** | Bots join, record, and stream without human intervention; calendar V2 handles edge cases automatically |
| **M2M integration surface** | REST API, webhook events for transcript updates, Calendar Integration API |
| **Identity / delegation** | Per-bot session IDs; per-calendar-event bot configuration; attribution of transcript to specific participants |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Meeting Bot** | Autonomous agent presence in a video meeting, joinable via API |
| **Real-Time Diarized Transcript** | Speaker-attributed transcript delivered as a stream within 10 seconds of speaking |
| **Audio/Video Stream** | Raw audio and video feed accessible programmatically |
| **Meeting Metadata** | Participants, timestamps, recording status, meeting platform |
| **Calendar Integration V2** | Connect Google Calendar and Outlook to auto-deploy bots for scheduled meetings |
| **Edge Case Handling** | Automatic management of calendar changes, back-to-back meetings, duplicate bot prevention |

---

## Supported Platforms

| Platform | Support |
|---|---|
| Zoom | Full (including free plans and non-host users) |
| Google Meet | Full |
| Microsoft Teams | Full |
| Webex | Full |
| Slack Huddles | Full |
| GoTo Meeting | Full |

---

## Autonomy Model

**Manual deployment:**
```
Agent calls POST /bots with meeting URL
    ↓
Bot joins meeting within seconds
    ↓
Real-time transcript events delivered via webhook
    ↓
Agent processes transcripts, takes actions (notes, summaries, responses)
    ↓
Agent calls DELETE /bots/{id} when done
```

**Calendar-driven deployment (fully autonomous):**
```
Operator connects Google Calendar / Outlook via Calendar V2 API
    ↓
Recall.ai detects upcoming meeting on calendar
    ↓
Bot automatically deployed 10 minutes before meeting start
    ↓
Transcript + metadata streamed to agent's webhook
    ↓
Bot automatically leaves when meeting ends
```

No human clicks "start recording" or manages the bot.

---

## Identity and Delegation Model

- Per-bot session ID enables attribution of transcripts to specific agent runs
- Calendar V2 provides per-event bot configuration (different recording rules per meeting type)
- Bot can be configured to announce itself to meeting participants (transparency disclosure)
- Recording permissions managed by the operator, not per-meeting participants

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Bot lifecycle: create, list, retrieve, delete |
| Webhooks | Real-time events: transcript segments, participant join/leave, recording status |
| Calendar Integration API V1 | Basic calendar connection and auto-scheduling |
| Calendar Integration API V2 | Granular per-event configuration, advanced edge case handling |

---

## Human-in-the-Loop Support

None required for operation. Humans can review transcripts and recordings post-meeting. The bot's presence in the meeting can be disclosed to participants, maintaining transparency without requiring human operation.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Zoom Recording (built-in)** | Human-initiated; recordings must be manually started by a human meeting participant |
| **Google Meet recording** | Host-initiated; no programmatic API for bot deployment or real-time transcript streaming |
| **OBS Studio** | Screen capture tool for human operators; not an agent-controlled bot |
| **Rev.ai / AssemblyAI** | Speech transcription APIs; agents must separately handle meeting joining, audio capture, and diarization |
| **Otter.ai** | Human-facing meeting notes tool; no programmatic bot API for autonomous agent use |

---

## Calendar V2 Edge Cases Handled Automatically

- Meeting URL changes after bot scheduled → bot updates automatically
- Back-to-back meetings → pause/resume or split recording
- Meeting cancelled → bot deployment cancelled
- Duplicate bot detection → prevents multiple bots joining the same meeting
- Custom recording rules per calendar event type

---

## Use Cases

- **Meeting summarization agents** — bot joins, transcribes, generates action items and summaries autonomously
- **Real-time coaching** — agent analyzes transcript live and provides suggestions during sales or support calls
- **Compliance recording** — agent maintains auditable records of all customer conversations
- **Research interviews** — agent transcribes and structures qualitative research conversations
- **Multi-meeting monitoring** — agent deploys bots across multiple simultaneous meetings and synthesizes cross-meeting insights
