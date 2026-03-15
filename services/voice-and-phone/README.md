# Voice & Phone Services

> Services that give AI agents a **first-class voice and telephony identity** — letting agents make and receive phone calls, conduct voice conversations, and interact via speech with no human operating a phone on their behalf.

## Why This Category Exists

Phone calls and voice conversations were designed for humans. AI agents that need to conduct outbound calls, handle inbound calls, or participate in voice-driven workflows require infrastructure that simply doesn't exist in human-facing telephony:

- **Programmable voice agent lifecycle** — create, deploy, and scale voice agents via API
- **Tool-calling mid-call** — agents invoke external APIs during a live call to fetch data or trigger actions
- **Webhook events per utterance** — agents react to speech events in real time without polling
- **Automated testing** — simulate voice conversations to catch hallucinations before production

No consumer VOIP or call center platform was designed with these requirements as the primary specification.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Vapi](vapi.md) | Build advanced voice AI agents | REST API, Web SDK, Python SDK, TypeScript SDK, Webhooks | ✅ |

---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide **programmable voice agent deployment** — not a human-facing call center tool.
2. Support **agent-controlled call lifecycle** via API (create, route, end calls programmatically).
3. Return **agent-consumable output** — structured transcripts, tool-call events, not raw audio for a human to listen to.
4. Support **tool-calling or function-calling** during live voice calls.
5. Be usable **headlessly** — no human browser session required for operation.
