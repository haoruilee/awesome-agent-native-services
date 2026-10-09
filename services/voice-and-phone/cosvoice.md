# CosVoice

> **"Your AI Agent gets its own phone number."**

| | |
|---|---|
| **Website** | https://cosvoice.com |
| **Docs** | https://cosvoice.com/skill |
| **GitHub** | https://github.com/CosVoice/cosvoice-mcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/CosVoice/cosvoice-mcp?style=social)](https://github.com/CosVoice/cosvoice-mcp) |
| **Classification** | `agent-native` |
| **Category** | [Voice & Phone Services](README.md) |
| **License** | MIT (packaging repository) |
| **Publisher** | MimesisIQ, stated in the repository license and README |
| **Verified at** | 2026-10-09 |
| **Latest-month signal** | https://cosvoice.com and https://cosvoice.com/skill returned HTTP 200. `https://cosvoice.com/mcp` returned GET 405, POST 401, OPTIONS 204. Packaging repo https://github.com/CosVoice/cosvoice-mcp is MIT |

---

## Official Website

https://cosvoice.com

The homepage line under the title is "A real phone line for your AI Bot."

---

## Official Repo

https://github.com/CosVoice/cosvoice-mcp

This repository is the packaging: `skills/cosvoice/SKILL.md` (the same text as https://cosvoice.com/skill), `.mcp.json`, plugin manifests, and `server.json`. The README says no code runs on the caller's machine. The phone line is the hosted service.

---

## How to Use (Agent Onboarding)

> **URL Onboarding — the skill page is written for the assistant.**

**Interaction pattern:** `URL Onboarding`

https://cosvoice.com/skill says an assistant that speaks MCP can follow it end to end. The owner still has a step: the MCP client opens a browser, the owner signs in and clicks Allow, and a number is issued only after a plan is on file. The same page says a person can use https://cosvoice.com/grok-bot.

**One-sentence instruction:**

```
Read https://cosvoice.com/skill and follow the instructions to connect CosVoice.
```

The remote server:

```
https://cosvoice.com/mcp
```

Transport is Streamable HTTP. Authentication is OAuth 2.1 with PKCE and dynamic client registration. Discovery documents checked on 2026-10-09: https://cosvoice.com/.well-known/oauth-protected-resource and https://cosvoice.com/.well-known/oauth-authorization-server (`authorization_endpoint`, `token_endpoint`, and `registration_endpoint` on `cosvoice.com`). Clients that only support a static header can use a key from Settings as `Authorization: Bearer cv_live_…`.

If `create_line` has no plan on file, the skill says it returns a checkout link. The owner pays, then the agent calls `create_line` again.

---

## Agent Skills

**Status:** ✅ Available

The hosted skill and `skills/cosvoice/SKILL.md` in the packaging repo are the same document. Front matter `name` is `cosvoice`.

```
Read https://cosvoice.com/skill and follow the instructions to connect CosVoice.
```

| Skill | What It Teaches the Agent |
|---|---|
| `cosvoice` | Connect the MCP server, provision a line after the owner pays, place and read calls, book by phone, and use the line's email |

No `npx skills add` command is printed in the README. Use the URL above, or the file in [CosVoice/cosvoice-mcp](https://github.com/CosVoice/cosvoice-mcp/blob/main/skills/cosvoice/SKILL.md).

---

## MCP

**Status:** ✅ Available — auth required

| Detail | Value |
|---|---|
| **Endpoint** | `https://cosvoice.com/mcp` |
| **Transport** | Streamable HTTP. On 2026-10-09, GET returned 405, OPTIONS returned 204, and POST without a token returned 401 with instructions to use OAuth or `Authorization: Bearer <CosVoice API key>` |
| **Registry** | `com.cosvoice/cosvoice` in [server.json](https://github.com/CosVoice/cosvoice-mcp/blob/main/server.json), remote URL `https://cosvoice.com/mcp` |
| **Auth** | OAuth 2.1 PKCE with dynamic client registration, or a `cv_live_` bearer. The skill says the token is scoped to one account and can be revoked in Settings |
| **Compatible clients** | The README names Grok, Claude, ChatGPT, and Cursor |

Tool names below are from the skill page and the packaging README. This check did not complete OAuth, so it did not call `tools/list`.

---

## What It Does

CosVoice provisions a phone number and an email address for an assistant. The homepage describes three uses: the owner calls or texts the line, the assistant places calls (including booking a table), and the line answers when the owner cannot. After a call, the owner gets a written summary. The skill says the voice is full duplex and that the line says it is an AI assistant when asked.

The agent drives the line over MCP: search numbers, create the line, place a call, poll for the outcome, read transcripts and email, and send email from the line's own address (`handle@bot.cosvoice.com` on the skill page). Calls are asynchronous. The skill says to poll `get_call` or wait for a `call.completed` webhook. A call is capped at 10 minutes. The line never pays and never reads out a card.

Current prices are the live pricing page and the skill page, checked 2026-10-09: Starter $29/month with 100 minutes, Plus $79/month with 300 minutes, Pro $199/month with 1,000 minutes, overage $0.25 per minute on paid plans. A 7-day trial is described as $0, with a card on file, then $29 for Starter unless the owner cancels or moves plans. The packaging README still lists older bundles (Starter 60 minutes, Plus $69/200, Pro $149/600). Those README figures are not the live page.

The skill says calls and texts go to US and Canada numbers only. The pricing page says available numbers are US area codes and that Canada is next. One new number per paid month per plan is the skill's account rule.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: "Your AI Agent gets its own phone number." Skill page: "This page is written for the assistant. If you are a Grok Bot, an OpenAI dot, Claude, ChatGPT, Cursor, or any agent that speaks MCP, you can follow it end to end." — [cosvoice.com](https://cosvoice.com) and [cosvoice.com/skill](https://cosvoice.com/skill) |
| **Agent-specific primitive** | A line that is a phone number plus an inbox, with MCP tools (`place_call`, `book_reservation`, `get_call`, email tools) instead of a person operating a dialer. The token is scoped to one line |
| **Autonomy-compatible control plane** | After the owner approves the connection and a plan is on file, the agent places calls, reads summaries, and sends line email without a dashboard click per action. `create_line` does not issue a number until payment is on file |
| **M2M integration surface** | Remote MCP, the skill URL, OpenAPI 3.1 at https://cosvoice.com/openapi.json (base `https://cosvoice.com/api/v1`), and `set_webhook` / `set_bot_push` as documented on the skill page |
| **Identity / delegation** | The line has its own number and email. The skill says the line identifies itself as an AI assistant, uses its own callback unless the owner allows otherwise, and accepts owner instructions from the owner's mobile only when the network vouches for caller ID or the caller enters the owner PIN |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Line** | A US number plus an email address, created with `create_line` after the owner chooses an area code and a plan is on file |
| **place_call** | Outbound call with `to` and a `purpose` (the skill caps `purpose` at 1,200 characters). Poll `get_call` until `completed` |
| **book_reservation** | Phone booking with party size, date, time window, and fallbacks. Outcomes include confirmed, waitlisted, no availability, and voicemail |
| **Call record** | Summary, structured details, and transcript from `get_call` / `list_calls` |
| **Line email** | `send_email` from the line address. The skill limits recipients to people who emailed the line first, the owner, or the bot inbox, and caps the line at 40 a day |
| **Owner instruction** | A text or verified call from the owner's mobile. The agent acknowledges it with `ack_instructions` |
| **Bot push** | `set_bot_push` so CosVoice starts the assistant on owner instructions, inbound email, or a finished call |

---

## Autonomy Model

1. The agent reads https://cosvoice.com/skill and adds `https://cosvoice.com/mcp`.
2. The owner signs in and clicks Allow. The token is scoped to one account.
3. The agent calls `get_account`, asks the owner for an area code and a line name, and calls `search_numbers`.
4. If no plan is on file, `create_line` returns a checkout link. The owner pays. The agent calls `create_line` again.
5. The agent places a call with `place_call` or `book_reservation` and polls `get_call`, or waits for the webhook.
6. It reports only what the call outcome says. The line does not pay and does not read a card.
7. Inbound calls and owner texts show up as messages, history, or bot-push events. The agent uses `ack_instructions` after it handles an owner instruction.

---

## Identity and Delegation Model

- The MCP token is scoped to one CosVoice account and, on the skill page, to one line. Another line means connecting again and picking it on the approval screen.
- The owner can revoke the connection in Settings. A static `cv_live_` key is an alternative for clients that cannot run OAuth.
- The line's number and `…@bot.cosvoice.com` address are the default callback. Sharing the owner's mobile requires `owner_phone_ok`.
- Owner instructions from a call require the network to vouch for caller ID or the owner PIN. The skill says not to ask the owner for the PIN and not to set it; the owner sets it in Settings.
- A blocked number is turned away before the line answers. STOP opt-outs apply to texts.
- The line says it is an AI assistant when asked and does not pretend to be the owner.
- Plan, password, owner PIN, and — once set — the owner's mobile and notification inboxes are owner-only. The skill says a bot cannot change them.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| URL onboarding | https://cosvoice.com/skill |
| MCP | `https://cosvoice.com/mcp` (Streamable HTTP, OAuth or bearer) |
| OpenAPI | https://cosvoice.com/openapi.json — REST base `https://cosvoice.com/api/v1` |
| OAuth discovery | `/.well-known/oauth-protected-resource` and `/.well-known/oauth-authorization-server` |
| Webhook | `set_webhook` for `call.completed`, and `set_bot_push` for assistant wakeups, as written on the skill page |
| Registry | `com.cosvoice/cosvoice` |

---

## Human-in-the-Loop Support

The owner approves the OAuth connection and pays before a number exists. After that, the agent places and reads calls through MCP without a dashboard click on each one. The OpenAPI section of the skill tells the assistant to confirm with the owner before placing a call and to say who it is about to ring. The line itself will not pay, will not read a card, and turns deposits into "needs owner." Closing the line, changing the plan, and changing the owner PIN stay in Settings.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Twilio (or another human CPaaS account)** | A developer buys a number and writes the call flow. There is no assistant skill that provisions the line, places the call, and returns a structured outcome to the same MCP session |
| **A personal mobile number** | The phone is a person's. It has no separate line email, no per-line MCP token, and no written call outcome for an assistant |
| **A consumer voicemail app** | It records audio for a human. It does not expose `place_call`, reservation statuses, or a line-scoped inbox to an agent |

---

## Use Cases

- **Give an assistant a number** — the owner approves MCP and a plan; `create_line` issues the number and email.
- **Book or inquire by phone** — `book_reservation` or `place_call`, then read `get_call` before telling the owner it is confirmed.
- **Answer when the owner cannot** — inbound calls land on the line; the agent reads the summary and transcript.
- **Use the line's inbox** — read mail sent to the line and reply from its own address, inside the skill's recipient limits.
