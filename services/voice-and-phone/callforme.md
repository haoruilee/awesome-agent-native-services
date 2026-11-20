# CallForMe

> **"Let your agent call businesses for you."**

| | |
|---|---|
| **Website** | https://callforme.tel/ |
| **Docs** | https://callforme.tel/llms.txt |
| **GitHub** | https://github.com/callforme-tel/callforme |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/callforme-tel/callforme?style=social)](https://github.com/callforme-tel/callforme) |
| **Classification** | `agent-native` |
| **Category** | [Voice & Phone Services](README.md) |
| **License** | MIT (README, Agent Skill and manifests; the hosted service is closed source) |
| **Publisher** | Great Work LLC (maker disclosure in issue #350) |
| **Verified at** | 2026-11-20 |
| **Latest-month signal** | https://callforme.tel/ returned HTTP 200 with H1 "Let your agent call businesses for you." Remote MCP https://callforme.tel/mcp answered an unauthenticated POST with 401 and OAuth metadata; https://callforme.tel/mcp/open listed 15 tools. OpenAPI 1.3.0 at https://callforme.tel/openapi.json. Agent Skill at https://callforme.tel/skill.md and https://github.com/callforme-tel/callforme/tree/main/skills/callforme |

---

## Official Website

https://callforme.tel/

Page title: "CallForMe: your AI agent makes phone calls to businesses for you". There is no human calling app: the product is a remote MCP server and REST API that an agent calls.

---

## Official Repo

https://github.com/callforme-tel/callforme

MIT packaging for the Agent Skill (`skills/callforme/SKILL.md`), plugin manifests and setup docs. The hosted service is closed source. Repository description: "MCP server that lets your AI agent phone businesses for you: quotes, bookings, cancellations, hold."

---

## How to Use (Agent Onboarding)

> **URL Onboarding with human steps: the agent reads one document and can place calls, but a person signs in once (OAuth in the browser) and adds credit through a Stripe link before the first paid call.**

**One-sentence instruction:**

```
Read https://callforme.tel/skill.md and follow the instructions to connect and place a call.
```

**Interaction pattern:** `URL Onboarding` ⚠️ — partial.

People still have to do two things:
- Complete the OAuth sign-in in the browser when the MCP client connects to `https://callforme.tel/mcp` (or store an API key from the account page).
- Open the one-time Stripe link the agent shows on the first real call (`needs_setup`), which adds $5 of credit. The agent then calls `wait_for_setup` and the call starts by itself.

Free demo lines (fictional businesses, no account, no charge) work before either step: `find_business` with query `demo`, or https://callforme.tel/demo.

Remote MCP (Streamable HTTP, OAuth 2.1 with dynamic client registration):

```
https://callforme.tel/mcp
```

REST: base `https://callforme.tel/v1`, OpenAPI at https://callforme.tel/openapi.json, `Authorization: Bearer cfm_...`.

---

## Agent Skills

**Status:** ✅ Available

Front matter `name` is `callforme` in [skills/callforme/SKILL.md](https://github.com/callforme-tel/callforme/tree/main/skills/callforme), also served at https://callforme.tel/skill.md.

```
npx skills add callforme-tel/callforme
```

| Skill | What It Teaches the Agent |
|---|---|
| `callforme` | Find a business number, preview the call with `plan_call`, place one call or call around to several, answer mid-call questions, handle the one-time credit link, and report answers, prices and confirmation numbers exactly |

---

## MCP

**Status:** ✅ Available — auth required

| Detail | Value |
|---|---|
| **Endpoint** | `https://callforme.tel/mcp` |
| **Transport** | Streamable HTTP. On 2026-11-20 an unauthenticated POST returned 401 with OAuth metadata |
| **Auth** | OAuth 2.1 with dynamic client registration (a guest account per connection), or an account key as a Bearer token |
| **Registry** | Official MCP Registry name `tel.callforme/callforme` |
| **Tools** | `find_business`, `plan_call`, `place_call`, `get_call`, `answer_question`, `hang_up`, `redial`, `list_calls`, `share_call`, `call_around`, `get_batch`, `stop_batch`, `account`, `pricing`, `wait_for_setup` |
| **Compatible clients** | Claude (web, desktop, Claude Code), ChatGPT, Codex, Cursor and other MCP clients |

---

## What It Does

CallForMe places real phone calls to businesses in the US and Canada for the user's agent. The agent supplies a goal, details the business may need, pre-approved answers and limits. A voice assistant dials, says up front that it is an assistant calling for the named person on a recorded line, works phone menus, waits on hold, and returns a structured outcome (type, summary, answers, confirmation codes, price), a transcript and a recording link.

When the business asks something the agent did not cover, the question is pushed back to the agent as a `pending_question` while the call is live. The agent answers with `answer_question` (from what it knows, or by asking the user), and the answer goes straight into the conversation. If no answer arrives in about 45 seconds, the assistant tells the business the person will follow up and carries on.

Pricing is prepaid: $1 per answered call (first 2 minutes), then $0.40 per minute, up to 30 minutes. Unanswered and busy calls are free, as are `plan_call`, `find_business` and the demo lines.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage H1: "Let your agent call businesses for you." Title: "CallForMe: your AI agent makes phone calls to businesses for you". https://callforme.tel/llms.txt and https://callforme.tel/skill.md are written for agents — [callforme.tel](https://callforme.tel/) |
| **Agent-specific primitive** | Mid-call `pending_question` / `answer_question` handoff to the calling agent; `plan_call` preflight of what the business will likely ask; `call_around` parallel calls returning a comparison table; `wait_for_setup` so the agent waits while a person completes the one-time credit link |
| **Autonomy-compatible control plane** | After the one-time sign-in and credit link, the agent runs the full loop (find number, plan, call, answer questions, read result) with no clicks. Limits: `max_cost_usd` per call, `if_asked` pre-approved decisions, 30-minute cap, `max_spend_usd` / `stop_after` on batches, prepaid credit, idempotency keys |
| **M2M integration surface** | Remote MCP (15 tools), REST API with OpenAPI, webhooks, Agent Skill |
| **Identity / delegation** | OAuth connection with dynamic client registration creates a guest account per connected agent; each call records `on_behalf_of` (the person the agent is calling for, said in the opener); call ids, transcript, structured outcome and recording link form the audit trail. The agent has no payment API: a person adds credit in their own browser |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **place_call** | Dial a US or Canadian business with a goal, details, pre-approved answers and limits; optional `call_at` to dial later |
| **pending_question / answer_question** | The business's question reaches the agent mid-call; the answer (or a new instruction) goes into the live call |
| **plan_call** | Free preview of the opening line and the questions the business will probably ask |
| **call_around / get_batch / stop_batch** | Call several places of a kind near a location with one goal and get a results table |
| **get_call** | Long-poll for status, pending questions, structured outcome, transcript and recording |
| **wait_for_setup** | Agent waits while the person opens the one-time credit link; the call starts by itself |

---

## Autonomy Model

1. Agent reads https://callforme.tel/skill.md, or connects to `https://callforme.tel/mcp` (a person completes OAuth once).
2. Optional: `find_business` for a number and `plan_call` to see what the business will ask.
3. Agent calls `place_call` with the goal, `on_behalf_of`, details and `if_asked`.
4. First real call only: the result is `needs_setup` with a credit link; the agent shows it to the person and calls `wait_for_setup`.
5. Agent follows the call with `get_call` and answers any `pending_question` with `answer_question`.
6. The call ends with a structured outcome the agent reports; unanswered calls are free and can be retried with `redial` or scheduled with `call_at`.

---

## Identity and Delegation Model

- Each OAuth connection gets its own guest account and credentials; an account key can be used instead for REST.
- Every call carries `on_behalf_of`, and the assistant opens with "an assistant calling for <name>, on a recorded line".
- The agent can spend prepaid credit only; adding credit happens in the person's browser on Stripe, so the agent never holds a card.
- Every call has an id, transcript, structured outcome and recording link (`get_call`, `list_calls`, `share_call`).
- Destinations are businesses in the US and Canada; card numbers, SSNs and one-time codes are never said on a call.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | `https://callforme.tel/mcp` (Streamable HTTP, OAuth 2.1 or Bearer key) |
| REST / OpenAPI | `https://callforme.tel/v1`, spec at https://callforme.tel/openapi.json |
| Agent Skill | https://callforme.tel/skill.md and `skills/callforme/SKILL.md` in callforme-tel/callforme |
| Docs for agents | https://callforme.tel/llms.txt |
| Registry | `tel.callforme/callforme` |

---

## Human-in-the-Loop Support

A person signs in once and adds credit once through a Stripe link. During a call, the agent can bring a business's question to the person before answering, or answer from what it already knows; `if_asked` pre-approves decisions so the agent does not have to ask. `call_around` over more than 10 places returns a preview of the list and cost for the person to confirm first. `hang_up` ends a live call at any time.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Voice-agent platforms (Vapi, Retell, Bland)** | For a developer to configure and operate a calling agent: buy numbers, write prompts, wire tools. CallForMe is the finished goal-to-outcome call an existing agent invokes per request |
| **Twilio Programmable Voice** | Telephony building blocks for human-facing phone products, with no agent question handoff or structured outcome |
| **A person calling the business** | The person would just talk. The loop exists so an agent that cannot speak on a phone can run the call and get machine-readable results |

---

## Use Cases

- **Quotes** — call three mechanics near a zip code for a brake job price and compare them in a table.
- **Bookings** — reserve a table or an appointment and return the confirmation code.
- **Cancellations** — cancel a membership, decline retention offers, and get the effective date.
- **Hold** — wait on hold with a customer-service line and patch the person in with `transfer_to` when the business needs to verify them.
- **Stock and hours checks** — ask a store or pharmacy whether something is in stock or when they close.
