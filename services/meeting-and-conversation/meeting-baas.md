# Meeting BaaS

> **"Meeting Bots As A Service — The developer API for programmatic access to meeting data across Zoom, Google Meet, and Microsoft Teams."**

| | |
|---|---|
| **Website** | https://meetingbaas.com |
| **Docs** | https://docs.meetingbaas.com |
| **GitHub** | https://github.com/Meeting-Baas |
| **Classification** | `agent-native` |
| **Category** | [Meeting & Conversation Services](README.md) |

---

## Official Website

https://meetingbaas.com

---

## Official Repo

https://github.com/Meeting-Baas — Open-source meeting bot stack (bots, docs, MCP server)

Primary API consumer docs: https://docs.meetingbaas.com

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / REST` + **webhooks** + optional **MCP**

1. Sign up for an API key at https://dashboard.meetingbaas.com/sign-up
2. Send a bot:

```bash
curl -X POST "https://api.meetingbaas.com/bots" \
  -H "Content-Type: application/json" \
  -H "x-meeting-baas-api-key: YOUR-API-KEY" \
  -d '{"meeting_url": "YOUR-MEETING-URL", "bot_name": "AI Notetaker", "recording_mode": "speaker_view", "speech_to_text": {"provider": "Default"}}'
```

3. Configure webhooks in account settings (Meeting BaaS **v2** delivers via **SVIX** with signed headers) — event names include `bot.status_change`, `bot.completed`, and `bot.failed` — see [Webhooks (v2)](https://docs.meetingbaas.com/docs/api-v2/webhooks). The older [Getting the Data](https://docs.meetingbaas.com/docs/api/getting-started/getting-the-data) guide uses `complete` / `failed` payloads for the v1-style flow.

**TypeScript SDK:** `npm install @meeting-baas/sdk` — see homepage examples at https://meetingbaas.com/en

**MCP (community / vendor):** https://github.com/Meeting-Baas/meeting-mcp — *Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.*

---

## Agent Skills

**Status:** ⚠️ No official `SKILL.md` / `npx skills add …` pack from Meeting BaaS yet.

```bash
npx clawhub@latest search meeting-baas
```

---

## MCP

**Status:** ✅ Available (official org repo)

Meeting BaaS publishes **meeting-mcp** — MCP tools to create bots, search transcripts, and manage recordings for AI assistants.

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/Meeting-Baas/meeting-mcp |
| **Purpose** | Create meeting bots, search transcripts, manage recordings from MCP clients |

---

## What It Does

Meeting BaaS provides a hosted API (with a self-hosting option) to deploy bots into Zoom, Google Meet, and Microsoft Teams from code. An agent or backend posts a meeting URL and configuration; the bot joins, can record, optionally transcribe with speaker-attributed output, and streams status over webhooks. Optional WebSocket streaming exposes raw audio and diarized JSON for real-time agent consumption.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage positions the product for **AI Meeting Assistants** and **automate their workflows** — *"Join thousands of customers that use Meeting BaaS to create AI Meeting Assistants"* — [meetingbaas.com/en](https://meetingbaas.com/en) |
| **Agent-specific primitive** | **Programmatic meeting bot** with lifecycle (join, record, transcribe, leave), **webhook-delivered diarized transcript**, optional **bidirectional audio WebSocket** for speaking bots — not a human “click record” flow |
| **Autonomy-compatible control plane** | Bots join and complete meetings without a human operating a client; `automatic_leave` and scheduled `start_time` support unattended operation — [Sending a bot](https://docs.meetingbaas.com/docs/api/getting-started/sending-a-bot) |
| **M2M integration surface** | REST API (`POST /bots`), webhooks, TypeScript/Python examples, `@meeting-baas/sdk`, official **meeting-mcp** |
| **Identity / delegation** | Per-`bot_id` attribution; webhook payloads tie transcripts and recordings to a specific bot instance; API key scopes operator account |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Meeting Bot** | API-created participant that joins a live meeting from a URL |
| **Recording Modes** | `speaker_view`, `gallery_view`, or `audio_only` |
| **Speech-to-Text** | Optional transcription; **v2** exposes transcript/diarization as linked artifacts on `bot.completed` — [Artifacts](https://docs.meetingbaas.com/docs/api-v2/artifacts) |
| **Webhook Events** | **v2:** `bot.status_change`, `bot.completed`, `bot.failed`, `bot.chat_message`, plus calendar events — signed via **SVIX** — [Webhooks (v2)](https://docs.meetingbaas.com/docs/api-v2/webhooks) |
| **Per-Bot Callbacks** | Optional `callback_config` on bot create: direct HTTP for completion/failure; verify with `x-mb-secret` when a secret is set |
| **Streaming (optional)** | WebSocket input/output audio and diarized JSON for real-time agents — [Sending a bot — Advanced Options](https://docs.meetingbaas.com/docs/api/getting-started/sending-a-bot) |
| **Automatic Leave** | Timeouts for waiting room and empty meetings |

---

## Autonomy Model

```
Agent or scheduler calls POST /bots with meeting_url + bot_name (+ optional start_time)
    ↓
Bot joins Zoom / Meet / Teams without a human opening the client
    ↓
Webhooks stream status (joining, in_call_recording, …)
    ↓
On success: **`bot.completed`** (v2) delivers artifact URLs (mp4, transcription JSON, diarization, etc.); presigned URLs expire (see v2 docs — typically a few hours)
    ↓
Agent consumes structured transcript + metadata; may DELETE / remove bot via API
```

No human is required to start or stop recording from inside the meeting app.

---

## Identity and Delegation Model

- Each deployment returns a **`bot_id`** (UUID) used for status correlation, removal, and follow-up API calls
- **Operator API key** (`x-meeting-baas-api-key`) identifies the integrating account; bots are attributed to that project
- **Webhook authenticity (v2)** — SVIX-signed requests: verify using `svix-id`, `svix-timestamp`, and `svix-signature` headers and your endpoint signing secret — [Webhook Security](https://docs.meetingbaas.com/docs/api-v2/webhooks#webhook-security)
- **Callback authenticity** — when `callback_config.secret` is set, Meeting BaaS sends `x-mb-secret` on bot callbacks — [Callbacks](https://docs.meetingbaas.com/docs/api-v2/webhooks#callbacks)
- **Artifact URLs** — presigned S3 URLs in `bot.completed` expire (v2 docs: **4 hours**); agents should fetch or persist promptly — [Artifacts](https://docs.meetingbaas.com/docs/api-v2/artifacts)

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `POST https://api.meetingbaas.com/bots` — create bot; removal and listing per docs |
| Webhooks (v2) | Account-level, SVIX-signed — `bot.status_change`, `bot.completed`, `bot.failed`, calendar events — [Webhooks (v2)](https://docs.meetingbaas.com/docs/api-v2/webhooks) |
| Callbacks | Per-bot `callback_config` for direct HTTP completion/failure notifications |
| TypeScript SDK | `@meeting-baas/sdk` — `createBaasClient` + `createBot` — [homepage](https://meetingbaas.com/en) |
| MCP | https://github.com/Meeting-Baas/meeting-mcp |

---

## Human-in-the-Loop Support

Not required for bot operation. Humans may admit the bot from a waiting room on some platforms; the API exposes waiting-room timeout behavior. Post-meeting, humans can review recordings outside the agent loop.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Built-in Zoom / Meet / Teams recording** | Host-initiated, human-client workflow; no unified cross-platform bot API for agents |
| **Recall.ai** | Listed separately — different vendor; same *category* of primitive |
| **Raw browser automation only** | No hosted bot lifecycle, transcription, and webhook contract as a service |
| **Transcription-only APIs** | Do not join meetings or produce per-bot meeting lifecycle events |

---

## Use Cases

- **AI notetaker agents** — deploy a bot per calendar event, ingest diarized webhooks into RAG or memory
- **Real-time meeting copilots** — optional WebSocket streaming for live reasoning
- **Compliance archives** — structured recordings + transcripts keyed by `bot_id`
- **Sales / support QA** — batch bot deployment with searchable transcripts via MCP
