# Meeting & Conversation Services

> Services that give AI agents a **programmatic presence in voice and video conversations** — letting agents join meetings, process real-time audio, and participate in synchronous communication without a human operating a client.

## Why This Category Exists

Video conferencing platforms (Zoom, Google Meet, Microsoft Teams) were built for humans joining from computers or phones. An AI agent that needs to participate in meetings — taking notes, providing real-time analysis, or acting as an autonomous participant — cannot use a human-facing client.

The challenges are significant:
- Every platform has a different protocol for joining and recording meetings
- Transcripts require speaker diarization to be useful for agents
- Meeting metadata (participants, calendar context, recording permissions) must be programmatically accessible
- Calendar events must trigger bot deployment without human intervention

Agent-native meeting services provide a unified API for bot lifecycle management across all major platforms — abstracting away the per-platform complexity so agents can focus on what to do in meetings, not how to join them.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Recall.ai](recall-ai.md) | The meeting bot API for every platform | REST API, Webhooks, Calendar Integration API | ❌ |
| [Meeting BaaS](meeting-baas.md) | Meeting bots as a service — Zoom, Meet, Teams | REST API, Webhooks, TypeScript SDK, meeting-mcp | ✅ |
| [MeetStream](meetstream.md) | Unified API for meeting bots, transcripts, and interactive AI agents | REST API, Webhooks, WebSockets | ⚠️ |
| [Vexa](vexa.md) [![⭐](https://img.shields.io/github/stars/Vexa-ai/vexa?style=social)](https://github.com/Vexa-ai/vexa) | Open-source meeting transcription + interactive bot for Meet/Teams/Zoom | REST API, WebSocket, MCP server (17 tools), self-host | ✅ |
| [Daily Agent Toolkit](daily-agent.md) [![⭐](https://img.shields.io/github/stars/daily-co/daily-python?style=social)](https://github.com/daily-co/daily-python) | Build realtime meeting agents on Daily | Programmatic room control, media stream hooks, bot orchestration | ⚠️ |
| [Looped Meet](looped-meet.md) [![⭐](https://img.shields.io/github/stars/loopedautomation/meet?style=social)](https://github.com/loopedautomation/meet) | Self-hostable video meetings with first-class, full-duplex AI agent participants | TTY WebSocket/webhook brain bridge, LiveKit/WebRTC, HTTP routes, cal.com webhook | ❌ |
| [AgentCall](agentcall.md) [![⭐](https://img.shields.io/github/stars/pattern-ai-labs/agentcall?style=social)](https://github.com/pattern-ai-labs/agentcall) | Your AI agent, in every meeting. | join-meeting Skill, REST/WSS, Meet/Zoom/Teams voice bot | ⚠️ |
| [joinly.ai](joinly.md) [![⭐](https://img.shields.io/github/stars/joinly-ai/joinly?style=social)](https://github.com/joinly-ai/joinly) | Make your meetings accessible to AI Agents! | Docker MCP, `joinly-client`, Zoom/Meet/Teams tools | ✅ |


---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide **programmatic bot deployment** into meetings — not a human-operated recording tool.
2. Return **agent-consumable output** — diarized transcripts, structured metadata, not raw audio.
3. Support **calendar-triggered deployment** — bots join scheduled meetings autonomously.
4. Abstract **multi-platform complexity** — agents shouldn't need per-platform implementation.
5. Provide **webhook events** — real-time transcript and participant events pushed to the agent.
