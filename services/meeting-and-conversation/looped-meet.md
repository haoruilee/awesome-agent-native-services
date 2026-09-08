# Looped Meet

> **"Dial your agent into your next meeting."**

| | |
|---|---|
| **Website** | https://github.com/loopedautomation/meet#readme |
| **Docs** | https://github.com/loopedautomation/meet#readme |
| **GitHub** | https://github.com/loopedautomation/meet |
| **Classification** | `agent-native` |
| **Category** | [Meeting & Conversation Services](README.md) |
| **License** | FSL-1.1-ALv2; each version converts to Apache 2.0 two years after release |
| **Latest-month signal** | Created 2026-07-16; [v0.1.2](https://github.com/loopedautomation/meet/releases/tag/v0.1.2) released 2026-08-05; last push 2026-08-12; **6 stars on 2026-08-13** ([GitHub metadata](https://api.github.com/repos/loopedautomation/meet)) — new and actively shipping, but still a low-star emerging project; former hosted site `meet.looped.sh` DNS NXDOMAIN as of 2026-09-08; website field is the GitHub README until DNS returns |
| **Verified at** | 2026-09-08 |

---

## Official Website

https://github.com/loopedautomation/meet#readme

README lead (live 2026-09-08): **"Dial your agent into your next meeting."** Former official site `meet.looped.sh` is DNS NXDOMAIN as of 2026-09-08. Use this GitHub README as the website field until that host returns.

---

## Official Repo

https://github.com/loopedautomation/meet

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `Daemon / WebSocket bridge`

```bash
git clone https://github.com/loopedautomation/meet.git
cd meet
cp .env.example .env
# Set LIVEKIT_API_SECRET, BRIDGE_TOKEN, SCOUT_TTY_TOKEN,
# OPENAI_API_KEY, and the demo agent's model key.
docker compose up
```

Open `http://localhost:3000`, create a room, and invite Scout. To bring an existing Looped Agent Framework agent, paste its TTY WebSocket URL and token into the room's Agents panel, or add it to `agent-registry.yaml` for a permanent roster.

---

## Agent Skills

**Status:** ⚠️ No official Looped Meet skill published in the repository.

Search community skills: `npx clawhub@latest search looped-meet`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ⚠️ No Looped Meet MCP server published. Invited agents connect through the Looped TTY WebSocket or webhook bridge and retain any MCP tools their own brain already has.

---

## What It Does

Looped Meet is a self-hostable video-meeting environment where AI agents are native participants rather than silent transcript bots. An invited agent receives its own tile and live listening/thinking/speaking state, can hear and speak in full duplex, can be interrupted, sees shared-screen frames, streams tool activity, and can edit the room's shared document and whiteboard.

The meeting surface is separated from the agent brain. A LiveKit-based bridge carries audio, room context, and controls to an unchanged Looped Agent Framework agent over its TTY trigger, preserving that agent's tools, memory, permissions, and audit trail. The repository is new and only lightly starred; its signal is release velocity and unusually complete agent-participant mechanics, not established adoption. Its FSL license restricts competing commercial products until each version converts to Apache 2.0 two years later.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The README calls it *"Self-hostable video meetings with first-class AI agent participants"* — [README](https://github.com/loopedautomation/meet#readme) |
| **Agent-specific primitive** | Agent participant tiles and state, turn policies (`open`, `on-mention`, `raise-hand`), barge-in, mute awareness, screen vision, tool-activity streaming, and agent edits to shared docs/whiteboards |
| **Autonomy-compatible control plane** | Once invited, an agent listens, answers, invokes its existing tools, updates shared artifacts, and reports results without per-action clicks; hosts retain room-level constraints and cancellation |
| **M2M integration surface** | TTY WebSocket or webhook connection to the agent brain, LiveKit/WebRTC media and data channels, HTTP room endpoints, and signed cal.com webhooks |
| **Identity / delegation** | Each roster entry has an agent ID, display identity, brain URL, token reference, voice, and turn policy; the underlying agent keeps its own permissions and audit trail while meeting activity remains attributable to its participant tile |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent Participant** | Named meeting member with its own media tile, voice, and listening/thinking/speaking state |
| **Brain Bridge** | TTY WebSocket or webhook link to an unchanged Looped Agent Framework agent |
| **Turn Policy** | Host-adjustable etiquette: speak freely, answer on mention, or raise a hand |
| **Barge-in / Mute** | Stops agent speech when a person interrupts and tells the brain when it must respond in chat |
| **Tool Activity Feed** | Streams the agent's tool calls into the live room while work is in progress |
| **Screen Vision** | Supplies current shared-screen context to pipeline or realtime agents |
| **Shared Doc / Whiteboard** | Persistent collaborative artifacts that humans and agents can edit together |
| **Persistent Voice Channel** | Invite-only account-backed channel with durable membership and live presence |

---

## Autonomy Model

```text
Operator deploys Meet and registers an agent brain URL + token
    ↓
Host or room policy invites the named agent participant
    ↓
LiveKit bridge carries room audio, transcript, chat, and shared-screen context
    ↓
Turn policy decides when the agent may take the floor
    ↓
Agent brain reasons with its existing memory, tools, MCP servers, and permissions
    ↓
Speech and tool activity stream back into the room
    ↓
Agent may update the shared document or whiteboard; host can interrupt or mute it
```

---

## Identity and Delegation Model

- `agent-registry.yaml` assigns each agent a stable ID, name, description, brain endpoint, token environment reference, and conversation policy.
- On-demand external agents join with a TTY URL and token; permanent roster entries avoid sharing credentials through meeting chat.
- The meeting bridge delegates substantive work to the registered Looped agent brain rather than impersonating it; that brain retains its own tool permissions, memory, and audit trail.
- Participant identity, tool activity, speech state, transcript contributions, and shared-artifact changes make the agent's meeting actions visible.
- Hosts control invitation, turn policy, mute, interruption, and room access; agent credentials remain server-side.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| TTY WebSocket | Streaming connection to a Looped Agent Framework brain, including tool feed and task cancellation |
| Webhook | Simpler request/reply brain integration for agents that do not need full streaming |
| LiveKit | WebRTC media transport, participant state, room data, and realtime agent bridge |
| HTTP Routes | Room, agent, token, moderation, shared document, whiteboard, channel, and presence operations |
| cal.com Webhook | HMAC-SHA256-verified booking events create a stable room link and write it back to the booking |
| Registry | YAML roster for persistent agent identities, voices, endpoints, and turn policies |

---

## Human-in-the-Loop Support

HITL is built into the conversation mechanics. A host chooses which agent joins, changes its turn policy during the call, can require it to raise a hand, and can mute or interrupt it immediately. Humans see tool calls, transcript contributions, screen-vision disclosure, and edits to shared artifacts. Calendar provisioning can be automatic, but starting a protected booked room still requires a host credential.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Google Meet / Zoom alone** | Human-first clients with no native agent participant identity, brain bridge, tool feed, agent turn policy, or shared-artifact control |
| **Transcription bot** | Observes and summarizes but cannot hold the floor, be interrupted naturally, call tools visibly, see the screen, or co-edit artifacts |
| **Raw LiveKit deployment** | Supplies media infrastructure but not a reusable agent-brain bridge, host-governed agent etiquette, task cancellation, or agent-aware room UI |
| **Generic chat UI** | Lacks synchronous full-duplex presence, participant media state, screen context, and meeting-floor controls |

---

## Use Cases

- **Engineering design meeting** — an agent listens, looks at a shared error, researches it, and draws the proposed architecture while explaining it
- **Agent-assisted standup** — a persistent channel keeps a project agent present with its existing memory and tools
- **Live research participant** — attendees ask an agent to verify facts while its searches and progress remain visible
- **Collaborative planning** — humans and an agent build the plan in a shared document or Excalidraw board during the discussion
- **Calendar-provisioned agent meetings** — cal.com bookings create stable room links automatically, ready for the configured agent roster
