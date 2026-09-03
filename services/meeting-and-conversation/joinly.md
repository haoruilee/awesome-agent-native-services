# joinly.ai

> **"Make your meetings accessible to AI Agents!"**

| | |
|---|---|
| **Website** | https://joinly.ai |
| **Docs** | https://github.com/joinly-ai/joinly#readme |
| **GitHub** | https://github.com/joinly-ai/joinly |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/joinly-ai/joinly?style=social)](https://github.com/joinly-ai/joinly) |
| **Classification** | `agent-native` |
| **Category** | [Meeting & Conversation](README.md) |
| **License** | MIT |
| **Latest-month signal** | Last GitHub push 2026-09-01 ([repo metadata](https://api.github.com/repos/joinly-ai/joinly)); image `ghcr.io/joinly-ai/joinly`; PyPI `joinly-client`; optional cloud https://cloud.joinly.ai |
| **Verified at** | 2026-09-03 |

---

## Official Website

https://joinly.ai

Homepage H1 (live 2026-09-03): **"Make your meetings accessible to AI Agents!"** (exclamation mark is official).

---

## Official Repo

https://github.com/joinly-ai/joinly

README lead: **"Make your meetings accessible to AI Agents 🤖"** — same sentence, emoji instead of `!`. GitHub description matches the homepage wording without the bang. The catalog tagline is the **homepage H1**.

**joinly.ai** is OSS **MCP meeting middleware**: a connector that gives any agent `join_meeting` / `speak_text` / live transcript tools. Optional [joinly cloud](https://cloud.joinly.ai) is a hosted convenience, not the listed core.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `CLI` + MCP server

```bash
docker pull ghcr.io/joinly-ai/joinly:latest
# Quickstart client-in-container (no external MCP):
docker run --env-file .env ghcr.io/joinly-ai/joinly:latest --client <MeetingURL>

# Server mode — bind localhost only:
docker run -p 127.0.0.1:8000:8000 ghcr.io/joinly-ai/joinly:latest
uvx joinly-client --env-file .env <MeetingUrl>
```

`.env` needs an LLM key (`JOINLY_LLM_PROVIDER` / `OPENAI_API_KEY` or Anthropic / Ollama — see `.env.example`). Extra MCP servers can be attached to `joinly-client` via `--mcp-config`.

**Official warning:** the MCP server has **no authentication** and accepts client-supplied configuration. Bind to `localhost`; do not expose the port.

There is no URL-onboarding document.

---

## Agent Skills

**Status:** ⚠️ No official `npx skills add` package published yet.

```bash
npx clawhub@latest search joinly
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — MCP is the backbone (homepage: “MCP: The backbone of joinly”)

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/joinly-ai/joinly |
| **Transport** | Streamable HTTP (Docker `:8000`); client package speaks MCP to that server |
| **Compatible Clients** | `joinly-client`, custom MCP agents, extra MCP servers via JSON config |
| **Auth** | **None** — local trusted client only |

### Tools (upstream README)

`join_meeting`, `leave_meeting`, `speak_text`, `send_chat_message`, `mute_yourself` / `unmute_yourself`, `get_chat_history`, `get_participants`, `get_transcript`, `get_video_snapshot`

### Resources

`transcript://live` — subscribable live transcript with timestamps and speakers.

---

## What It Does

joinly.ai puts an **AI participant** into Zoom, Google Meet, or Microsoft Teams (browser-based). Official README: live voice/chat interaction, interruption-aware conversational flow, bring-your-own LLM, pluggable STT/TTS (Whisper/Kokoro local defaults; Deepgram/ElevenLabs optional). Self-host via Docker (~2.3 GB with browser + models); CUDA image available.

**Distinct from catalog peers:**

| Peer | Difference |
|---|---|
| [Vexa](vexa.md) | Self-host **transcription + interactive bot API** (17 MCP tools, REST). joinly is middleware: any agent talks MCP to a meeting connector |
| [AgentCall](agentcall.md) | Hosted **join-meeting Skill** (`ak_ac_` keys), not an OSS MCP server you run |
| [Looped Meet](looped-meet.md) | Self-hosted **room product** with a TTY brain bridge — you host the meeting, not join Zoom/Meet/Teams |

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage H1: **"Make your meetings accessible to AI Agents!"** — [joinly.ai](https://joinly.ai). README: connector middleware whose MCP server equips **any** AI agent |
| **Agent-specific primitive** | Meeting as MCP tools/resources: join/leave/speak/chat/transcript/snapshot + `transcript://live` |
| **Autonomy-compatible control plane** | After Docker + `.env`, `joinly-client` or a custom agent joins and speaks without a human operating Zoom |
| **M2M integration surface** | Docker MCP server, `uvx joinly-client`, extra MCP servers via JSON, Python client package |
| **Identity / delegation** | **C5-weak:** MCP server is **unauthenticated** (documented). Meeting identity is `--name` (default `joinly`). LLM/STT/TTS keys are provider credentials, not a per-agent KYA token. Cloud is a separate hosted identity. Do not expose `:8000` |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`join_meeting` / `leave_meeting`** | URL + display name + optional passcode |
| **`speak_text`** | TTS into the call |
| **`transcript://live`** | Subscribable diarized transcript |
| **Chat / mute / snapshot** | In-meeting I/O tools |
| **BYO LLM + STT/TTS** | OpenAI, Anthropic, Ollama; Whisper/Kokoro or cloud providers |
| **Client package** | `joinly-client` — reference agent; attach more MCP servers |

---

## Autonomy Model

```
Start joinly Docker as MCP server on 127.0.0.1:8000
    -> joinly-client (or custom agent) connects
    -> join_meeting <url>
    -> Live transcript resource updates; agent speaks / chats / calls other MCP tools
    -> leave_meeting
```

No human in the Zoom client. Calendar auto-join is not the primary documented path (unlike some SaaS bots).

---

## Identity and Delegation Model

- **Participant name:** `--name` in the meeting roster.
- **MCP trust boundary:** localhost, single trusted client — **no auth**.
- **Provider keys:** LLM/STT/TTS in `.env`; not delegated attendee OAuth.
- **Cloud (optional):** hosted identity at cloud.joinly.ai — outside the MIT self-host core.
- **Honest C5:** observation and speech are attributable to the joinly participant, not to a minted user-delegated meeting token.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Docker MCP | `ghcr.io/joinly-ai/joinly:latest` (`--client` or server `:8000`) |
| Client | `uvx joinly-client` / PyPI `joinly-client` |
| Extra tools | `--mcp-config` JSON (`mcpServers`) |
| Cloud | https://cloud.joinly.ai (optional, not required) |

---

## Human-in-the-Loop Support

A human supplies the meeting URL and `.env` keys. Optional VNC (`--vnc-server`) for debugging the browser. Roadmap lists an in-meeting human-approval mechanism — not shipped. During the call the agent is the participant.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Vexa** | Bot platform + REST/MCP for transcription/TTS. joinly is OSS **middleware** so *your* agent (plus extra MCP servers) sits in the meeting |
| **AgentCall** | Hosted skill + API keys; not a self-hosted MCP connector |
| **Looped Meet** | You host the room; joinly **joins** Zoom/Meet/Teams |
| **Recall.ai / Meeting BaaS** | SaaS bot APIs already in this catalog — not OSS MCP middleware |
| **A raw WebRTC SDK** | No meeting join, VAD/barge-in, or MCP tool surface |

---

## Use Cases

- **Agent in standup** — speak, listen, open a GitHub issue mid-call (demo)
- **Notion/docs in the meeting** — attach extra MCP servers to the client
- **Self-hosted, privacy-first** — browser + models in your Docker
- **Custom meeting agent** — write a client against the documented tools/resources
