# Stimm

> **"The Open Source Voice Agent Platform. Orchestrate ultra-low latency AI pipelines for real-time conversations over WebRTC."**

| | |
|---|---|
| **Website** | https://stimm.ai |
| **Docs** | https://github.com/stimm-ai/stimm#readme |
| **GitHub** | https://github.com/stimm-ai/stimm |
| **Classification** | `agent-native` |
| **Category** | [Voice & Phone](README.md) |
| **Status** | Open source · early-stage but rapid 2026 iteration |

---

## Official Website

https://stimm.ai

---

## Official Repo

https://github.com/stimm-ai/stimm

---

## How to Use (Agent Onboarding)

```
git clone https://github.com/stimm-ai/stimm
# follow README to install + run the orchestrator
# then connect your STT / LLM / TTS providers and a WebRTC client
```

The platform is BYO STT/LLM/TTS — operators wire providers into the pipeline.

---

## Agent Skills

**Status:** ⚠️ Not yet published.

```bash
npx clawhub@latest search stimm
```

---

## MCP

**Status:** ⚠️ Not yet published as a first-party MCP server.

| Detail | Value |
|---|---|
| **Transport** | n/a — primary surface is SDK + WebRTC |
| **Compatible Clients** | any agent runtime that orchestrates the pipeline |

---

## What It Does

Stimm is an **open-source orchestrator for real-time voice agents** over WebRTC. Its design center is **ultra-low latency** with two distinguishing primitives:

1. **Dual-agent architecture** — a small, fast agent handles immediate verbal feedback (filler / acknowledgment) while a larger, slower agent handles the substantive reasoning. The pipeline coordinates the two so the user never feels a long silence.
2. **Optimistic VUI** — speak interim feedback before the full LLM response is finalized, cancel or amend if reasoning diverges.

Operators bring their own STT, LLM, and TTS providers; Stimm orchestrates the WebRTC media plane and the dual-agent control plane. It is an open-source contender to LiveKit Agents and the closed-source Vapi / Retell, with a tighter focus on perceived-latency engineering.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Repo tagline: *"The Open Source Voice Agent Platform"* |
| **Agent-specific primitive** | Dual-agent (fast + slow) coordination; optimistic VUI; sub-perception-threshold latency budget enforced by the runtime |
| **Autonomy-compatible control plane** | Voice agent runs end-to-end; operator only sets up providers; no per-utterance human input |
| **M2M integration surface** | Orchestrator + WebRTC + provider adapters |
| **Identity / delegation** | Per-call agent identity; per-room session isolation |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Dual-Agent Pipeline** | Small fast agent emits immediate response while large agent reasons in the background |
| **Optimistic VUI** | Speak interim feedback; cancel / amend on divergence |
| **WebRTC Media Plane** | Low-latency audio in / out |
| **BYO STT/LLM/TTS** | Pluggable providers for each stage |
| **Real-time Conversation Loop** | Turn-taking, interruption handling, barge-in |

---

## Autonomy Model

1. Operator wires up STT, LLM, TTS, and a WebRTC entry point.
2. Caller connects via WebRTC; Stimm starts streaming.
3. Fast agent emits immediate verbal acknowledgment.
4. Slow agent reasons; if its conclusion diverges from the fast agent's prefix, Stimm amends gracefully.
5. Conversation loops with barge-in / interruption support.

---

## Identity and Delegation Model

- Each call is a discrete session.
- Per-call provider credentials are scoped (STT/LLM/TTS keys can be tenant-specific).
- Audit log per session.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| WebRTC | Real-time audio media plane |
| Orchestrator API | Pipeline configuration, session lifecycle |
| Provider adapters | STT, LLM, TTS — pluggable |

---

## Human-in-the-Loop Support

A "barge-in" surface exists for the operator (warm transfer pattern); compose with HumanLayer / Inferable for explicit approval gates.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **LiveKit Agents** | Excellent open-source WebRTC platform (already in catalog) — Stimm differs by making the dual-agent / optimistic-VUI latency model a first-class primitive |
| **Vapi / Retell** | Closed-source; can't tune the dual-agent split or optimistic-VUI policy |
| **Plain Twilio + LLM** | No real-time orchestrator; latency is whatever the LLM round-trip happens to be |

---

## Use Cases

- **Customer support voice agent** — fast verbal acknowledgments + accurate slow reasoning
- **Outbound calls with low perceived latency** — agent feels responsive even when the LLM is slow
- **Self-hosted voice agents** — open-source alternative when SaaS voice platforms are off-limits
