# Pipecat

> **"Open-source framework for real-time voice AI agents."**

| | |
|---|---|
| **Website** | https://pipecat.ai |
| **Docs** | https://docs.pipecat.ai |
| **GitHub** | https://github.com/pipecat-ai/pipecat |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/pipecat-ai/pipecat?style=social)](https://github.com/pipecat-ai/pipecat) |
| **Classification** | `agent-native` |
| **Category** | [Voice & Phone Services](README.md) |

## Official Website
https://pipecat.ai

## Official Repo
https://github.com/pipecat-ai/pipecat

## How to Use (Agent Onboarding)
Build a voice pipeline (STT → LLM → TTS), attach transport (WebRTC/SIP), then run headless agent workers for realtime calls.

## Agent Skills
**Status:** ⚠️ No official AgentSkills package found.

## MCP
**Status:** ⚠️ No standalone official MCP server package.

## What It Does
Provides low-latency orchestration for realtime speech processing, tool calling, and conversational turn management.

## Why It Is Agent-Native
Purpose-built for autonomous voice loops where an agent reasons and acts during live conversations.

## Primary Primitives
- Realtime voice pipeline
- Turn detection
- In-call tool invocation

## Autonomy Model
Agents can run continuously and handle calls without manual intervention.

## Identity and Delegation Model
Per-agent runtime identity and provider credentials define which actions/calls are permitted.

## Protocol Surface
Python SDK, WebRTC/SIP transports, plugin adapters.

## Human-in-the-Loop Support
Escalation to human operators can be added when confidence/intent thresholds are exceeded.

## Why Generic Alternatives Do Not Qualify
Raw telephony APIs do not provide end-to-end realtime agent reasoning orchestration.

## Use Cases
- AI phone receptionists
- Voice support bots
- Real-time outbound/inbound call workflows
