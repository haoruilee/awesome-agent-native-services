A voice agent built on this framework is split between two operators. The agent's logic runs as a worker process your team writes in Python or TypeScript. The media mesh, phone numbers, autoscaling, and session replay are offered by LiveKit Cloud. That split decides where a live conversation can break and who gets paged when it does, so it is the first thing to understand.

### Rooms, sessions, and a worker

The dossier describes [LiveKit Agents](https://docs.livekit.io/agents/) as a framework and cloud platform for real-time voice and video agents. The unit of work is a room. A person joins from a browser, a mobile app, or a SIP call. A worker picks up the job and starts an AgentSession, which wires speech-to-text, the model, text-to-speech, voice activity detection, and turn detection into one loop. The agent listens, plans, speaks, and can call tools between turns. Barge-in and noise cancellation are listed as pipeline features, and they are the part a request-response API cannot give a talking agent.

Integration runs through SDKs rather than a tool protocol. The dossier lists the Python package `livekit-agents` with plugins, a TypeScript Agents SDK, a CLI, WebRTC client SDKs for web, iOS, and Android, and SIP. It marks MCP as not the product's surface. On Agent Skills, it notes that LiveKit advertises coding agent resources on its site but that no install command was verified, so the documented starting point is the voice AI quickstart in the docs.

### Where it sits among voice listings

The [Voice & Phone](/categories/voice-and-phone/) category mixes frameworks with phone-number services. [Pipecat](/services/pipecat/), an open-source framework for real-time voice agents, is the closest neighbor; the comparison turns on how much you want LiveKit's cloud underneath by default. [Vapi](/services/vapi/) is pitched as a place to build voice agents rather than a framework you deploy. [Patter](/services/patter/) and [CosVoice](/services/cosvoice/) start from the other end and hand an agent a phone number. LiveKit reaches telephony through SIP and its phone numbers product, but its center of gravity is the room. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why a real-time session primitive qualifies.

### Before a production call

Auth comes in two layers. Access tokens admit participants, human or agent, to specific rooms; API keys cover server-side deployment and management. Check how tokens are minted, how long they live, and whether the agent's identity is distinguishable from the caller's in logs and recordings.

Then settle who operates which piece. The dossier does not say how much of the stack runs without LiveKit Cloud, which providers sit behind LiveKit Inference, or what session replay retains. Handing a call to a human is left to application logic. Compliance options are described as available on the cloud, so read the trust center instead of assuming coverage.

### Editor's take

The natural fit is a team that wants to own the agent's code but not media servers or SIP trunks. If the goal is a phone number for an agent that already exists, Patter or CosVoice start closer to that. If you want an open framework with no default cloud attached, compare Pipecat first. These notes come from the catalog dossier and LiveKit's published docs; nobody on this project has put a caller through it.
