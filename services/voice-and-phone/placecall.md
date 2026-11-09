# PlaceCall

> **"Give your agent a phone."**

| | |
|---|---|
| **Website** | https://voygr.tech/placecall/ |
| **Docs** | https://api.voygr.tech/docs |
| **GitHub** | https://github.com/voygr-tech/placecall |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/voygr-tech/placecall?style=social)](https://github.com/voygr-tech/placecall) |
| **Classification** | `agent-native` |
| **Category** | [Voice & Phone Services](README.md) |
| **License** | MIT (client packaging repository; hosted service is closed source) |
| **Publisher** | Voygr Tech (stated in issue #244 disclosure and the packaging repo) |
| **Verified at** | 2026-11-07 |
| **Latest-month signal** | https://voygr.tech/placecall/ returned HTTP 200 with tagline "Give your agent a phone." Remote MCP `https://api.voygr.tech/mcp` answered POST without auth with a Bearer / `X-API-Key` requirement. OpenAPI at https://api.voygr.tech/openapi.json includes `/calls`, `/calls/{call_id}/answer`, and `/v1/places/suggest`. Packaging repo https://github.com/voygr-tech/placecall is MIT with `skills/placecall/SKILL.md` |

---

## Official Website

https://voygr.tech/placecall/

Homepage H1: "The real-world action layer for AI apps and agents." Lead copy: "Give your agent a phone. PlaceCall calls US businesses for your users: quotes, bookings, information."

---

## Official Repo

https://github.com/voygr-tech/placecall

MIT packaging for the Agent Skill, Claude Code / Codex / Cursor plugins, and setup docs. The hosted PlaceCall service is closed source. Repository description: "The phone is your last API. Give your agent a voice to call any US business."

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `MCP` + published Agent Skills

Remote MCP (Streamable HTTP; OAuth 2.1 with dynamic client registration and PKCE, or `X-API-Key`):

```
https://api.voygr.tech/mcp
```

Claude Code plugin (installs the skill and wires MCP; browser sign-in on first use creates an account with free credits):

```
/plugin marketplace add voygr-tech/placecall
/plugin install placecall@placecall
```

Then run `/mcp`, pick `placecall`, and sign in.

Skill-only install (needs a key from https://api.voygr.tech/checkout for placing calls):

```
npx skills add https://clawhub.ai/voygr/skills/placecall
```

Or copy `skills/placecall/SKILL.md` from the packaging repo. OpenAPI / interactive docs: https://api.voygr.tech/openapi.json and https://api.voygr.tech/docs.

---

## Agent Skills

**Status:** ✅ Available

Front matter `name` is `placecall` in [skills/placecall/SKILL.md](https://github.com/voygr-tech/placecall/blob/main/skills/placecall/SKILL.md).

```
/plugin marketplace add voygr-tech/placecall
/plugin install placecall@placecall
```

```
npx skills add https://clawhub.ai/voygr/skills/placecall
```

| Skill | What It Teaches the Agent |
|---|---|
| `placecall` | Call US businesses with a plain-language brief, suggest places when no number is known, answer mid-call questions, and read structured outcomes with transcript and recording |

---

## MCP

**Status:** ✅ Available — auth required

| Detail | Value |
|---|---|
| **Endpoint** | `https://api.voygr.tech/mcp` |
| **Transport** | Streamable HTTP. On 2026-11-07, unauthenticated POST returned a requirement for `Authorization: Bearer` or `X-API-Key` |
| **Registry** | Official MCP Registry name `io.github.voygr-tech/placecall` (stated in issue #244 and packaging docs) |
| **Auth** | OAuth 2.1 with dynamic client registration and PKCE, or `X-API-Key` / bearer from https://api.voygr.tech/checkout |
| **Compatible clients** | Packaging README names Claude Code, Codex, Cursor, Claude chat connectors, ChatGPT / OpenAI plugin directory, OpenClaw, Gemini CLI, and HTTP clients |

This check did not complete OAuth, so it did not call `tools/list`. REST tools named in the proposal and skill include `place_call`, `answer_question`, `get_call_result`, and `suggest_places`.

---

## What It Does

PlaceCall is a hosted outbound phone layer for agents. The calling agent supplies a US phone number (or a place description) and a plain-language `brief`. PlaceCall dials, navigates IVRs and hold, conducts the conversation, and returns a labelled outcome, transcript, and recording. When the call agent needs a detail the brief lacks, it raises a mid-call question that the calling agent answers while the call is still live.

There is no human calling app: the product is the tool an agent invokes. Self-serve signup creates an account with free credits (250 free calls on a new API key per the site); after that, billing is per successful outcome, not per minute. Destination policy is US numbers only, with some states refused server-side before dialing.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: "Give your agent a phone." and "The real-world action layer for AI apps and agents." Repo: "Give your agent a voice to call any US business." — [voygr.tech/placecall](https://voygr.tech/placecall/) and [voygr-tech/placecall](https://github.com/voygr-tech/placecall) |
| **Agent-specific primitive** | Brief-driven `place_call`; mid-call `answer_question` handoff back to the calling agent; structured outcome types with transcript/recording; `suggest_places` that writes a ready call brief |
| **Autonomy-compatible control plane** | Agent loop: optional `suggest_places` → `place_call` → poll result → `answer_question` if asked. Prepaid credits with hold, daily/concurrency ceilings, `Idempotency-Key`, and server-side region policy. No per-action dashboard click |
| **M2M integration surface** | Remote MCP, REST OpenAPI, Agent Skill, and IDE plugins |
| **Identity / delegation** | Call opens with an AI/recording disclosure; `disclosure.on_behalf_of` names who the agent is calling for; OAuth clients get scoped access (`calls:place`, `places:read`); call ids, event stream, transcript, and recording form the audit trail. Attribution is per account/key/OAuth client, not a separate per-agent wallet |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **place_call** | Dial a US number with a plain-language brief; PlaceCall runs the live conversation |
| **answer_question** | Answer a mid-call question from the call agent while the call is still live |
| **get_call_result / call record** | Labelled outcome, summary, transcript, and recording for branching |
| **suggest_places** | Turn a place description into candidates with reasons and a ready call brief |
| **Call events** | Status event stream on `GET /calls/{id}/events` |

---

## Autonomy Model

1. Agent installs the skill/plugin or adds `https://api.voygr.tech/mcp` (owner signs in once, or sets an API key).
2. Optional: `suggest_places` when the agent has a place description instead of a number.
3. Agent calls `place_call` with `target_phone` and `brief` (and an `Idempotency-Key` on creation).
4. If the call agent asks for missing detail, the calling agent answers through `answer_question`.
5. Agent polls the call result (or reads events) and branches on the structured outcome.
6. Failed connects (busy, voicemail, wrong number, etc.) return a clear reason; the site states unsuccessful outcomes are not charged.

---

## Identity and Delegation Model

- Default disclosure on the call names PlaceCall and that the line is recorded; `disclosure.on_behalf_of` can name the person the agent is calling for.
- OAuth clients register dynamically with scoped access; API keys carry their own quota, concurrency, and daily ceilings.
- Every call has an id, status events, outcome, transcript, and recording (kept 90 days per the proposal). Creation can record which client tool placed it (`X-Client-Agent`).
- There is no separate agent credential or wallet minted per agent instance; attribution is per account, key, and OAuth client.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | `https://api.voygr.tech/mcp` (Streamable HTTP, OAuth or API key) |
| REST / OpenAPI | https://api.voygr.tech/openapi.json — docs at https://api.voygr.tech/docs |
| Agent Skill | `skills/placecall/SKILL.md` in voygr-tech/placecall; ClawHub / `npx skills add` routes |
| Plugins | Claude Code marketplace, Codex / Cursor plugins, Claude connector, ChatGPT plugin directory |
| Registry | `io.github.voygr-tech/placecall` |

---

## Human-in-the-Loop Support

Owner signs in once (OAuth) or obtains an API key. The packaging skill tells the agent to confirm the number and brief with the user before dialing; that guidance is not a server-side gate. Mid-call questions are answered by the calling agent, not by opening a human phone UI. Region blocks, credit holds, and rate limits are enforced server-side.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Twilio Programmable Voice** | Telephony infrastructure for developers to build human-facing phone products. The developer owns numbers, call flow, STT/TTS, and result parsing. PlaceCall is the finished brief→outcome capability an agent invokes |
| **A person calling the business** | A human who wants a reservation just dials. The value is that an agent without a voice can delegate the live call and get machine-readable results |
| **A consumer dialer or call-center CRM** | Built for humans operating phones. No mid-call agent-to-agent question handoff or structured outcome types for an autonomous loop |

---

## Use Cases

- **Book or reschedule** — agent places a brief-driven call to a restaurant or clinic and reads the outcome.
- **Quotes and stock checks** — inquire across one or many US businesses; pay only for successful outcomes.
- **Place discovery then call** — `suggest_places` when the agent has intent but no number, then dial with the written brief.
- **Mid-call clarification** — calling agent answers a live question without dropping the conversation.
