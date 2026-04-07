# LiveKit Agents

> **"Build, run, and observe AI agents"** — voice, video, and physical AI on LiveKit.

| | |
|---|---|
| **Website** | https://livekit.io/agents |
| **Docs** | https://docs.livekit.io/agents/ |
| **GitHub** | https://github.com/livekit/agents |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/livekit/agents?style=social)](https://github.com/livekit/agents) |
| **Classification** | `agent-native` |
| **Category** | [Voice & Phone Services](README.md) |

---

## Official Website

https://livekit.io/agents

---

## Official Repo

https://github.com/livekit/agents — Python & TypeScript agent server framework

---

## How to Use (Agent Onboarding)

**SDK — open-source Agents framework + LiveKit Cloud for deploy and telephony.**

```bash
# Follow https://docs.livekit.io/agents/start/voice-ai/
# Typical: pip install livekit-agents + plugins (STT, LLM, TTS), then livekit agents CLI
```

**LiveKit Cloud** — managed agent deployment, inference routing, SIP / phone numbers — see [Agent Cloud deployment](https://livekit.io/products/agent-cloud-deployment) and [docs](https://docs.livekit.io/intro/cloud/).

---

## Agent Skills

**Status:** ⚠️ LiveKit publishes **coding agent resources** (Claude Code, Cursor, etc.) per marketing site; no single `npx skills add livekit/...` verified in-repo — see LiveKit docs **Coding agent resources**.

---

## MCP

**Status:** ⚠️ Not primarily an MCP product; integration is **SDK + WebRTC + SIP**.

---

## What It Does

LiveKit **Agents** is a framework and cloud platform for **real-time voice (and video) AI agents**: **STT → LLM → TTS** pipelines with **VAD**, **turn detection**, **barge-in**, **noise cancellation**, and **tool use** during live sessions. **LiveKit Cloud** provides global **WebRTC** media mesh, **autoscaling**, **SIP telephony**, **session replay**, **metrics**, and **logs** — infrastructure aimed at **conversational agents**, not traditional CRUD APIs.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Product page: *"Build, run, and observe AI agents"*; SDK examples define `Agent` classes and `AgentSession` for voice loops |
| **Agent-specific primitive** | **Real-time multimodal session** with **interruption handling**, **turn detection**, **noise cancellation**, and **mid-session tool/model plugins** — no human phone UI |
| **Autonomy-compatible control plane** | Agents join rooms and handle calls **headlessly** via APIs; scaling and routing are platform-managed |
| **M2M integration surface** | Python & TypeScript SDKs, CLI, **SIP**, web & mobile **client SDKs** |
| **Identity / delegation** | **LiveKit tokens** gate room access; **org/project** controls on cloud; **HIPAA / SOC2** options per trust center |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **AgentServer / JobContext** | Entry point for agent worker processes |
| **AgentSession** | Wires STT, LLM, TTS, VAD, turn detection |
| **Room / participant** | WebRTC session model for human ↔ agent |
| **SIP & phone numbers** | PSTN ingress/egress for voice agents |
| **Inference** | Routed STT/LLM/TTS via LiveKit Inference or plugins |
| **Observability** | Session replay, logs, agent metrics |

---

## Autonomy Model

```
Client joins LiveKit room (web, mobile, or SIP)
    ↓
Agent worker receives job → starts AgentSession with audio pipeline
    ↓
Agent listens → LLM plans → speaks; may call tools between turns
    ↓
Cloud handles media routing, scaling, recording exports
```

---

## Identity and Delegation Model

- **Access tokens** authorize participants (users vs. agents) to specific rooms.
- **API keys** for server-side agent deployment and management.
- **Enterprise** compliance and data controls on LiveKit Cloud.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Python | `livekit-agents` + plugins — see GitHub |
| TypeScript | Agents SDK — see docs |
| WebRTC | Client SDKs (web, iOS, Android) |
| SIP | Telephony product — see LiveKit Phone Numbers |

---

## Human-in-the-Loop Support

Voice agents may escalate to humans via application logic; platform provides **session inspection** for supervisors.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Plain Twilio + REST** | No built-in real-time agent audio pipeline, turn detection, or WebRTC mesh |
| **Batch STT/TTS APIs** | Latency model wrong for live conversation |
| **Generic video SaaS** | Not optimized for **AI agent** workers, tool calls, and telephony-native noise profiles |

---

## Use Cases

- **Customer support voice bots** with tool calling during calls
- **Realtime copilots** — low-latency speech ↔ LLM loops
- **Phone agents** — SIP trunking without operating media servers yourself
