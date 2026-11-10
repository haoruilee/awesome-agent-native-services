The agent has to be a long-running process that can hold a WebRTC connection into a room and react to events while the meeting is live. The dossier lists REST APIs, a Python SDK, WebRTC transports, and webhooks. It found no standalone MCP server and no Agent Skill, so a tool-calling assistant cannot simply add this as one more tool.

### Rooms the bot joins

The tagline is "Build realtime meeting agents on Daily." The How to Use path has two steps: create a Daily room through the API, then run a bot process that joins it and handles meeting events in code. The primitives are programmatic room join and leave, media stream callbacks, and realtime meeting events.

Identity separation is explicit in the dossier. The bot is a participant distinct from the humans, and room and API credentials scope what it may do. Supervision is literal: a human can join the same room and step in.

The entry stops at that level. It does not say which events are delivered, what form media arrives in, or how webhooks relate to in-room callbacks. The [Daily docs](https://docs.daily.co) and the [daily-python repository](https://github.com/daily-co/daily-python) are where to read those details.

### Own the room or join someone else's

Most of [Meeting & Conversation](/categories/meeting-and-conversation/) solves a different problem: getting a bot into a meeting hosted on Zoom, Google Meet, or Microsoft Teams. [Recall.ai](/services/recall-ai/) and [Meeting BaaS](/services/meeting-baas/) describe themselves as meeting bot APIs across those platforms. [Vexa](/services/vexa/) adds open-source transcription with an MCP server. [joinly.ai](/services/joinly/) and [AgentCall](/services/agentcall/) put an agent into existing meetings.

Daily's dossier describes rooms you create on Daily's own infrastructure. That is a better fit when you run the meeting, as in a support call or an interview product, and want the bot as a native participant with media access. It does not help if your users meet on Teams and expect the agent to show up there. The [agent-native guide](/guides/what-makes-a-service-agent-native/) frames why bot lifecycle controls count as agent primitives.

### Open questions in the entry

Confirm how room credentials are minted and how narrowly a bot's permissions can be set. Decide where the bot process runs and how it scales with concurrent rooms, because the dossier leaves operation to you. Check whether recordings and transcripts are platform features or something the bot must produce itself. Price is on Daily's site.

### Editor's take

Teams building their own meeting or call product, with Python available and a reason to process live media, are the ones this listing serves. If the meetings happen on Zoom, Meet, or Teams, Recall.ai, Meeting BaaS, or Vexa matches the job better. My reading is limited to the dossier and Daily's developer pages; no bot was deployed into a room for this note.
