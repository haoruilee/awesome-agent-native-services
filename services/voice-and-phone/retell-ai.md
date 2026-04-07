# Retell AI

> **"#1 AI Voice Agent Platform for Automating Calls."**

| | |
|---|---|
| **Website** | https://www.retellai.com |
| **Docs** | https://docs.retellai.com |
| **GitHub** | https://github.com/RetellAI/retell-python-sdk |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/RetellAI/retell-python-sdk?style=social)](https://github.com/RetellAI/retell-python-sdk) |
| **Classification** | `agent-native` |
| **Category** | [Voice & Phone Services](README.md) |
| **Compliance** | HIPAA · SOC 2 Type II · GDPR (per marketing site) |

---

## Official Website

https://www.retellai.com

---

## Official Repo

https://github.com/RetellAI/retell-python-sdk — Python SDK

https://github.com/RetellAI/retell-typescript-sdk — TypeScript SDK

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK / REST` + **webhooks** + optional **MCP** (mid-call tools and assistant management)

1. Create an account and API key from the Retell dashboard (free trial credits on signup).
2. Define a voice agent (conversation-flow or single/multi-prompt) in the API or dashboard.
3. Attach telephony (Retell numbers or custom SIP) and optional **MCP servers** so the agent can call tools during live calls — see [MCP](https://docs.retellai.com/build/single-multi-prompt/mcp).

```bash
pip install retell-sdk
# or: npm install retell-sdk
```

Use the REST API for outbound/inbound calls, agent lifecycle, and webhooks for per-call events — [Introduction](https://docs.retellai.com).

---

## Agent Skills

Agent Skills are portable `SKILL.md` instruction sets following the [AgentSkills open standard](https://agentskills.io/) that teach AI coding assistants (Claude Code, Cursor, Codex, Windsurf, etc.) how to use this service correctly.

**Status:** ⚠️ No official `npx skills add …` pack from Retell yet.

```bash
npx clawhub@latest search retell
```

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available (product-native)

Retell supports the **Model Context Protocol** in two ways: voice agents can invoke MCP tools **during a phone call** (configured in the dashboard), and assistants like Claude can manage Retell resources via an MCP integration — see [MCP](https://docs.retellai.com/build/single-multi-prompt/mcp) and the [MCP node guide](https://www.retellai.com/blog/connect-any-ai-voice-agent-to-mcp-with-retell-ai-mcp-node).

| Detail | Value |
|---|---|
| **Docs** | https://docs.retellai.com/build/single-multi-prompt/mcp |
| **Mid-call tools** | MCP server URL + tool allowlist + response mapping into conversation variables |
| **Compatible clients** | Retell-managed voice runtime; external MCP clients per Retell/blog guides |

---

## What It Does

Retell is a platform to build, test, deploy, and monitor **AI phone agents**: inbound and outbound calls, custom telephony via SIP, real-time function calling during speech, webhooks for call lifecycle and analytics, and simulation testing before production. The product is scoped around autonomous voice agents—not a human-operated contact center UI as the primary control plane.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"#1 AI Voice Agent Platform for Automating Calls"* and *"Build, deploy, and manage next-generation AI voice agents"* — [retellai.com](https://www.retellai.com) |
| **Agent-specific primitive** | Programmatic **voice agent** lifecycle; **real-time function calling** during live calls; **webhooks** for call events; **simulation testing** for voice agents |
| **Autonomy-compatible control plane** | Agents handle calls at scale without a human on the phone; batch calling and automated testing are first-class |
| **M2M integration surface** | REST API, Python SDK, TypeScript SDK, webhooks, SIP integration, MCP |
| **Identity / delegation** | Per-agent configuration, per-call IDs, webhook payloads and analytics attributable to specific calls and assistants |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Voice agent** | LLM-driven phone agent with prompts, voices, and tool/MCP configuration |
| **Phone call** | Inbound/outbound call session with transcription and analysis hooks |
| **Mid-call function / MCP tool** | Agent invokes external tools while the caller is on the line |
| **Webhook** | Server-side events for call state, transcripts, and post-call analysis |
| **Simulation** | Automated conversational tests before deploying agents |
| **Custom telephony** | SIP trunking to bring your own numbers and carriers |

---

## Autonomy Model

```
Agent (or orchestrator) creates/updates a Retell voice agent via API
    ↓
Provisioning: phone number or SIP, model, voice, tools/MCP
    ↓
Inbound or outbound call starts — no human operator on the handset
    ↓
During call: STT → LLM → TTS; tools/MCP run on demand
    ↓
Webhooks deliver structured events and analysis to the agent backend
```

---

## Identity and Delegation Model

- **Assistant / agent IDs** — configuration and versioning per deployed voice agent
- **Call IDs** — correlate transcripts, recordings, and webhook payloads
- **API keys** — operator credentials; scoped access via dashboard roles (enterprise)
- **Tool/MCP allowlists** — explicit delegation of which external actions a voice agent may take mid-call

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Call creation, agent management, analytics — see [docs.retellai.com](https://docs.retellai.com) |
| Python SDK | `pip install retell-sdk` — [retell-python-sdk](https://github.com/RetellAI/retell-python-sdk) |
| TypeScript SDK | `npm install retell-sdk` — [retell-typescript-sdk](https://github.com/RetellAI/retell-typescript-sdk) |
| Webhooks | Real-time and post-call events for integrations |
| SIP | Custom telephony interconnection |

---

## Human-in-the-Loop Support

Optional at the application layer (e.g., human review of flagged calls). Retell does not require a human on every call; escalation patterns are implemented via agent design, transfers, or downstream workflows.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Twilio Programmable Voice** | Telephony API for developers; AI voice agent orchestration, mid-call LLM tool loops, and agent-specific simulation are not first-class primitives |
| **Human call center software** | Built for human agents; not a headless voice-agent runtime |
| **Consumer VoIP** | No API-first agent lifecycle or mid-call tool execution |

---

## Use Cases

- **Outbound scheduling and reminders** — autonomous calls with calendar tools
- **Inbound support** — 24/7 voice agents with knowledge and ticketing tools
- **Lead qualification** — voice agents with CRM MCP tools
- **Debt collection / surveys** — high-volume batch calling with compliance-oriented configuration
