Start with the transport. A voice agent built this way runs as a Python process attached to a WebRTC or SIP connection, and someone has to host that process. The dossier names a Python SDK, those two transports, and plugin adapters. There is no standalone MCP server and no Agent Skill. Pipecat is a framework your code imports, not a service your agent calls.

### A pipeline, not a phone number

The tagline is "Open-source framework for real-time voice AI agents." The dossier's How to Use section describes the shape: build a pipeline of speech-to-text, LLM, and text-to-speech, attach a transport, then run headless agent workers for live calls. The listed primitives are the realtime voice pipeline, turn detection, and in-call tool invocation.

Turn detection is often the hard part. Deciding when a caller has finished speaking, and what to do when they interrupt, determines whether the agent is usable on a real call. Having it as a named primitive is the main reason to start from a framework rather than wiring speech providers together yourself.

Identity is described as per-agent runtime identity plus provider credentials. In practice your speech, model, and telephony keys define what the agent can do. Escalation to a human can be added when confidence or intent thresholds are crossed, but the dossier presents it as something you build.

### Framework or hosted voice

[Voice & Phone](/categories/voice-and-phone/) splits roughly in two. [Vapi](/services/vapi/) is listed as a platform for building voice agents, and [CosVoice](/services/cosvoice/) and [PlaceCall](/services/placecall/) give an existing agent a phone. Those reduce the code you own. [LiveKit Agents](/services/livekit-agents/) and [Patter](/services/patter/) sit nearer to Pipecat as SDKs that run in your process. LiveKit pairs its agent framework with its own media infrastructure, while the dossier describes Pipecat as transport-pluggable.

That flexibility cuts both ways. You choose the speech-to-text, model, and voice providers, and you also own their failure modes. The [agent-native guide](/guides/what-makes-a-service-agent-native/) explains why a framework qualifies for the catalog: what it produces is an agent loop that reasons and acts during the call.

### Checks before a live call

Look up which providers the plugin adapters currently cover in the [Pipecat docs](https://docs.pipecat.ai). Decide who operates the workers and the SIP trunk, because the dossier leaves hosting to you. Confirm how tool calls behave mid-utterance and how a call is handed to a person. Responsiveness depends on your provider choices and deployment, so measure it in your own setup rather than relying on a published figure.

### Editor's take

Pipecat fits a team with Python engineers who want to own the voice stack and swap providers freely. If you want an agent answering a phone number with little code of your own, CosVoice, PlaceCall, or Vapi is the shorter path. If you already run LiveKit for media, its agent framework is the natural comparison. This is an opinion drawn from the dossier and the public docs; the project has not built or run a Pipecat pipeline.
