# Patter

> **"Patter is the open-source SDK that gives your AI agent a phone number."**

| | |
|---|---|
| **Website** | https://getpatter.com |
| **Docs** | https://docs.getpatter.com |
| **GitHub** | https://github.com/PatterAI/Patter |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/PatterAI/Patter?style=social)](https://github.com/PatterAI/Patter) |
| **Classification** | `agent-native` |
| **Category** | [Voice & Phone Services](README.md) |
| **License** | MIT |
| **Latest-month signal** | v0.7.0 (2026-06-30) is still the latest release (npm and PyPI `getpatter` 0.7.0); last GitHub push 2026-08-25; 1,062 stars; MIT; [`PatterAI/skills`](https://github.com/PatterAI/skills) present; [getpatter.com](https://getpatter.com) and [docs](https://docs.getpatter.com) HTTP 200 (verified 2026-09-30) |
| **Verified at** | 2026-09-30 |

---

## Official Website

https://getpatter.com

---

## Official Repo

https://github.com/PatterAI/Patter

Skills live in a separate official repo: https://github.com/PatterAI/skills

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `SDK` + **published Agent Skills**

```bash
npx skills add patterai/skills
npm install getpatter
# or
pip install getpatter
```

TypeScript (from the official README):

```typescript
import { Patter, Twilio, OpenAIRealtime } from "getpatter";

const phone = new Patter({ carrier: new Twilio(), phoneNumber: "+15550001234" });
const agent = phone.agent({
  engine: new OpenAIRealtime(),
  systemPrompt: "You are a friendly receptionist for Acme Corp.",
  firstMessage: "Hello! How can I help?",
});
await phone.serve({ agent, tunnel: true });
```

Python uses the same objects via `from getpatter import Patter, Twilio, OpenAIRealtime`. Credentials come from environment variables documented at https://docs.getpatter.com. `tunnel: true` starts a Cloudflare quick tunnel for local dev.

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add patterai/skills
```

Official index: https://www.skills.sh/patterai/skills — README says the bundle works in Agent Skills-compatible harnesses.

| Skill | What It Teaches the Agent |
|---|---|
| Patter skills bundle | How to compose the voice stack (carrier, STT/TTS/realtime, tools, tunnel) in Python or TypeScript |

Exact skill names live in `PatterAI/skills`; install via the command above rather than inventing filenames.

---

## MCP

**Status:** ⚠️ Not published

Primary surfaces are the Python/TypeScript SDKs, docs, and Skills. No official MCP server is documented in the README.

Search community skills: `npx clawhub@latest search patter`. See: https://agentskills.io/specification

---

## What It Does

Patter is an open-source voice stack between an application and the phone network. It runs the agent loop and lets you swap LLM, STT, TTS, realtime, and carrier providers (Twilio, Telnyx, Plivo). Modes: Realtime, Pipeline, Hybrid. Built-in tools, transfer, guardrails, and OpenTelemetry traces are vendor-neutral across carriers. Same API in Python and TypeScript.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README: **"Patter is the open-source SDK that gives your AI agent a phone number."** GitHub: **"Give your AI agent a phone number in 4 lines"** — [PatterAI/Patter](https://github.com/PatterAI/Patter) |
| **Agent-specific primitive** | A phone number bound to an agent loop with mid-call tools, transfer, and guardrails — not a human softphone |
| **Autonomy-compatible control plane** | `phone.serve({ agent })` answers/places calls without a person holding a handset. Provider keys are env, not per-utterance clicks |
| **M2M integration surface** | `getpatter` npm/PyPI, docs, Skills, webhooks/tunnel |
| **Identity / delegation** | The agent's telephony identity is the provisioned number + carrier account. OTel traces each call. No KYA wallet |

Same catalog neighborhood as Vapi/Retell, but the official positioning is the self-hosted OSS alternative.

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`Patter` + `phone.agent`** | Bind a number to an engine and prompts |
| **Provider layers** | Swap LLM/STT/TTS/realtime/carrier in one line |
| **Tools / transfer / guardrails** | Same behavior on every carrier |
| **Tunnel** | Cloudflare quick tunnel for local `serve` |
| **OpenTelemetry** | Vendor-neutral call trace |

---

## Autonomy Model

```
Install SDK + set carrier and model env vars
    -> construct Patter + agent
    -> serve (tunnel or static webhook_url)
    -> inbound/outbound calls hit the agent loop
    -> tools/transfer/guardrails run mid-call
    -> call ends; trace is recorded
```

---

## Identity and Delegation Model

- **Number identity:** The phone number you attach is the agent's reachable identity.
- **Carrier account:** Twilio/Telnyx/Plivo credentials stay in env.
- **Call trace:** OpenTelemetry, not a human recording inbox.
- **Telemetry opt-out:** Anonymous SDK telemetry is documented; disable with `telemetry=False`, `getpatter telemetry disable`, or `PATTER_TELEMETRY_DISABLED=1` (also honors `DO_NOT_TRACK=1`). Official note: no call content, prompts, numbers, or keys.
- **You run the loop:** Patter is infrastructure you host, not a hosted agent identity provider.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| npm | `getpatter` |
| PyPI | `getpatter` |
| Skills | `npx skills add patterai/skills` |
| Docs | https://docs.getpatter.com |
| Templates | Separate example repos listed in the README |

---

## Human-in-the-Loop Support

Not required per utterance. Guardrails and call transfer can escalate to a human. A local dashboard template exists for operators. Production needs a static webhook rather than only the dev tunnel.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Human PBX / softphone** | A person places and answers calls |
| **Carrier API only** | Media + STT/TTS + agent loop are still yours to invent |
| **Chat-only voice widget** | Not a first-class PSTN number the agent owns |

---

## Use Cases

- **Inbound receptionist** — answer a number with a realtime engine
- **Outbound + AMD** — official outbound template
- **BYO voice pipeline** — Deepgram + ElevenLabs (or other listed providers)
- **Own the stack** — MIT SDK instead of a closed voice-agent SaaS
