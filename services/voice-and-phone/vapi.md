# Vapi

> **"Build advanced voice AI agents."**

| | |
|---|---|
| **Website** | https://vapi.ai |
| **Docs** | https://docs.vapi.ai |
| **Classification** | `agent-native` |
| **Category** | [Voice & Phone Services](README.md) |
| **Scale** | 300M+ calls · 2.5M+ assistants · 500K+ developers |

---

## Official Website

https://vapi.ai

---

## Official Repo

https://github.com/VapiAI/server-sdk-python — Python SDK

https://github.com/VapiAI/server-sdk-typescript — TypeScript SDK

---

## Agent Skills

**Status:** ⚠️ No official skill published by Vapi yet.

```bash
npx clawhub@latest search vapi
```

---

## MCP

**Status:** ✅ Available

Vapi provides an MCP server enabling agents to manage voice assistants, phone numbers, calls, and tools directly through the Model Context Protocol.

| Detail | Value |
|---|---|
| **MCP Docs** | https://docs.vapi.ai/mcp |
| **Transport** | stdio |
| **Compatible Clients** | Claude Desktop, Cursor, any MCP-compatible client |

---

## What It Does

Vapi is an API platform for building, deploying, and scaling voice AI agents. Developers create voice assistants programmatically, deploy them to phone numbers or web calls, and configure tool-calling so agents can invoke external APIs mid-conversation. The entire voice agent lifecycle — provisioning, routing, call handling, transcription, and analytics — is controlled via API with no human telephone operator in the loop.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Build Advanced Voice AI Agents"*; product is exclusively about building and deploying AI voice agents, not a human call center tool |
| **Agent-specific primitive** | Voice assistant lifecycle API; tool-calling during live calls (agents invoke functions mid-conversation); webhook events per utterance; automated voice simulation testing |
| **Autonomy-compatible control plane** | Agents handle millions of daily inbound calls without human operators; auto-scaling across providers; A/B testing voice agent variants |
| **M2M integration surface** | REST API, Python SDK, TypeScript SDK, Web SDK, webhook events; MCP server |
| **Identity / delegation** | Per-assistant IDs; per-call trace IDs; phone numbers scoped to assistants; audit logs per call |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Voice Assistant** | Programmatically defined AI phone agent with model, voice, and tool configuration |
| **Phone Number** | Inbound/outbound number provisioned and scoped to an assistant via API |
| **Tool Call (mid-call)** | Agent invokes an external function during a live voice conversation (OpenAI-style function calling) |
| **Server Webhook** | Real-time POST on speech events, tool calls, call end, assistant request |
| **Phone Number Hook** | Actions triggered on specific call lifecycle events (e.g., `call.ringing`) |
| **Voice Simulation** | Automated testing using simulated voice agents to catch hallucinations before deployment |
| **Web Call** | Browser-based voice call for agent-to-human or agent-to-agent voice interaction |

---

## Autonomy Model

```
Operator provisions a phone number and assigns it to a voice assistant via API
    ↓
Inbound call arrives at the number
    ↓
Vapi routes call to the configured voice assistant
    ↓
Agent processes speech in real time (STT → LLM → TTS loop)
    ↓
Agent invokes tool calls mid-conversation (e.g., fetch order status from CRM)
    ↓
Vapi sends webhook events to operator's server for each utterance / tool call
    ↓
Call ends — analytics and transcript delivered via webhook
```

No human operator required. 400,000+ daily inbound calls processed autonomously.

---

## Identity and Delegation Model

- Each assistant has a unique ID used for routing, logging, and billing
- Phone numbers are scoped to specific assistants (one number → one agent identity)
- Per-call trace IDs enable fine-grained audit of every conversation
- Virtual API keys allow scoping credentials per assistant without exposing provider keys

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Full assistant, phone number, call, and analytics management |
| Python SDK | `pip install vapi-server-sdk` |
| TypeScript SDK | `npm install @vapi-ai/server-sdk` |
| Web SDK | Browser-based voice calls |
| Webhooks | `speech-update`, `tool-calls`, `end-of-call-report`, `assistant-request`, `transfer-destination-request` |
| MCP Server | Manage assistants, numbers, and calls via Model Context Protocol |

---

## Human-in-the-Loop Support

Optional. Vapi supports call transfer to a human agent as a tool action (`transfer` destination). Otherwise, all call handling is fully autonomous. Automated testing via voice simulation helps catch issues before they reach a human caller.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Twilio** | Built for human developers routing human calls; no voice agent lifecycle API, no mid-call tool calling primitive, no agent testing simulation |
| **Amazon Connect** | Human call center platform; agents are a UI feature, not an API primitive |
| **Vonage** | Telecom infrastructure for humans; no concept of AI assistant deployment or mid-call function calling |
| **ElevenLabs (voice only)** | TTS synthesis API; no phone call handling, no tool calling, no call routing |

---

## Use Cases

- **Inbound customer support** — voice agent handles support calls, looks up order status via tool call, escalates edge cases to human
- **Outbound sales** — agent makes outbound calls to leads, qualifies them, books meetings
- **Appointment reminders** — agent calls patients/customers to confirm appointments
- **Survey collection** — agent conducts voice surveys at scale with structured data collection
- **Multilingual support** — agent handles calls in 100+ languages without separate deployments
