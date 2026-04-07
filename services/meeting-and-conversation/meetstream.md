# MeetStream

> **"API & Infrastructure to capture recordings, transcripts & metadata from meetings."**

| | |
|---|---|
| **Website** | https://meetstream.ai |
| **Docs** | https://docs.meetstream.ai |
| **GitHub** | N/A (hosted API; integrate via REST, WebSockets, and webhooks per docs) |
| **Classification** | `agent-native` |
| **Category** | [Meeting & Conversation Services](README.md) |
| **Compliance** | SOC 2 Type 2 · ISO 27001 · GDPR (per marketing site) |

---

## Official Website

https://meetstream.ai

---

## Official Repo

⚠️ No single primary open-source repo identified for the hosted API — integration is via **REST API**, **WebSockets**, and **webhooks** per [docs.meetstream.ai](https://docs.meetstream.ai).

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `REST` + **Webhooks** + **WebSockets** (real-time media/transcripts)

1. Request access via [Get Early Access](https://forms.fillout.com/t/gPynZ3UyiKus) or [app.meetstream.ai](https://app.meetstream.ai) (per site), then obtain an API key.
2. Create a bot with the documented endpoint (OpenAPI: `Authorization: Token <your_api_key>`):

```bash
curl -X POST "https://api.meetstream.ai/api/v1/bots/create_bot" \
  -H "Authorization: Token YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"meeting_link":"https://meet.google.com/xxx-xxxx-xxx","bot_name":"Meetstream Agent","video_required":true}'
```

3. Add `callback_url` for **webhooks**, or configure `live_transcription_required`, `live_audio_required`, and `socket_connection_url` for streaming (see [Create Bot](https://docs.meetstream.ai/api-reference/ap-is/bot-endpoints/create-bot.mdx)).

Full capability list: [Welcome to MeetStream](https://docs.meetstream.ai/welcome.mdx) · [OpenAPI JSON](https://docs.meetstream.ai/openapi.json)

---

## Agent Skills

**Status:** ⚠️ No `npx skills add …` registry entry — MeetStream publishes a **downloadable Claude Skill** (ZIP with `SKILL.md`) for API patterns, webhooks, and WebSockets.

Install: [AI Integrations](https://docs.meetstream.ai/build-with-ai/ai-integrations.mdx) → download the skill ZIP → upload in Claude **Settings → Capabilities**.

```bash
npx clawhub@latest search meetstream
```

---

## MCP

**Status:** ✅ Available (documentation MCP)

MeetStream hosts an SSE MCP server so coding agents can **search live API documentation** — not remote control of meetings, but accurate doc-grounded integration.

| Detail | Value |
|---|---|
| **MCP URL** | `https://docs.meetstream.ai/_mcp/server` (SSE) |
| **Docs** | [AI Integrations](https://docs.meetstream.ai/build-with-ai/ai-integrations.mdx) |
| **Example (Claude Code)** | `claude mcp add meetstream-docs --transport sse https://docs.meetstream.ai/_mcp/server` |

---

## What It Does

MeetStream provides a **unified meeting-bot API** to join **Zoom, Google Meet, and Microsoft Teams**, capture **recordings and real-time audio/video**, stream **speaker-attributed transcripts** (live and async), expose **participant and chat metadata**, and support **interactive agents** (e.g., TTS, chat, display) — so downstream **AI agents** consume structured meeting data without building per-platform media pipelines.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Docs: *"unified API to deploy interactive bots and AI agents into meeting platforms"*; homepage positions the product so teams *"focus on building the AI agent itself"* — [docs.meetstream.ai](https://docs.meetstream.ai), [meetstream.ai](https://meetstream.ai) |
| **Agent-specific primitive** | **Programmatic meeting bot** with join/record/stream; **real-time diarized transcript webhooks**; **WebSocket media**; **in-meeting chat R/W**; **active AI participants** (TTS, video, screen) |
| **Autonomy-compatible control plane** | **Calendar sync** and **auto-dispatch**; **auto-leave** rules; pause/mute/resume via API (per docs) |
| **M2M integration surface** | REST (`/api/v1/...`), webhooks, WebSockets |
| **Identity / delegation** | Per-bot sessions; participant and speaking metadata for attribution |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Meeting bot** | API-spawned participant that joins from a meeting URL |
| **Real-time transcript** | Speaker-labeled streaming events via webhook |
| **Media stream** | Low-latency audio/video over WebSocket |
| **Recording** | MP4 / isolated tracks export |
| **Calendar integration** | Auto-join scheduled meetings |
| **In-meeting interaction** | Chat messages, TTS, images/video injection (per docs) |

---

## Autonomy Model

```
Scheduler or agent POSTs meeting URL to MeetStream API
    ↓
Bot joins platform (Zoom / Meet / Teams) without a human client
    ↓
Streams transcripts + metadata to agent via webhook/WebSocket
    ↓
Optional: agent speaks or posts chat through API
    ↓
Auto-leave and completion events close the session
```

---

## Identity and Delegation Model

- **Bot/session IDs** — correlate recordings, transcripts, and callbacks
- **API keys / Bearer tokens** — control who can create or control bots
- **Speaker attribution** — transcript events tied to participant identity where platform allows

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Bot lifecycle, transcripts, metadata — [docs.meetstream.ai](https://docs.meetstream.ai) |
| Webhooks | Live events (e.g., diarized speech) |
| WebSockets | Real-time audio/video stream consumption |

---

## Human-in-the-Loop Support

Organizational: consent, compliance, and calendar policies. Runtime bot operation is API-driven without a human clicking “Join” in a desktop client.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Manual recording** | Human-operated; not programmatic multi-platform bot lifecycle |
| **Single-vendor SDK only** | Requires one integration per conferencing provider; no unified agent-oriented transcript + media contract |
| **Recall.ai / Meeting BaaS** | Also qualify; MeetStream is an additional vendor in the same agent-native meeting-bot segment |

---

## Use Cases

- **Sales coaching agents** — live transcripts + intent signals during customer calls
- **Meeting notetaker agents** — structured action items from diarized streams
- **Interactive meeting agents** — speak or display visuals via API during the call
