# Dial

> **"Your agent needs a number."**

| | |
|---|---|
| **Website** | https://getdial.ai |
| **Docs** | https://docs.getdial.ai |
| **GitHub** | https://github.com/GetDial-AI/cli |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/GetDial-AI/cli?style=social)](https://github.com/GetDial-AI/cli) |
| **Classification** | `agent-native` |
| **Category** | [Voice & Phone Services](README.md) |
| **License** | MIT declared in `package.json` and the README only; there is no LICENSE file in the GetDial-AI/cli tree (GitHub detects no license). The hosted service is closed source |
| **Publisher** | Dial (maker disclosure in issue #377) |
| **Verified at** | 2026-11-25 |
| **Latest-month signal** | https://getdial.ai, https://getdial.ai/skills.md, https://getdial.ai/pricing, https://docs.getdial.ai and https://docs.getdial.ai/openapi.json returned HTTP 200. An unauthenticated MCP `initialize` POST to https://getdial.ai/mcp returned 401 with `WWW-Authenticate: Bearer resource_metadata="https://getdial.ai/.well-known/oauth-protected-resource/mcp"`, and that metadata URL returned 200. https://github.com/GetDial-AI/cli was pushed on 2026-11-24 (npm `@getdial/cli` 0.64.1) |

---

## Official Website

https://getdial.ai

Page title: "Dial: Your agent needs a number." The line under it reads "Communication stack for AI agents. Calls, SMS, WhatsApp and iMessage through one API." The MCP Registry entry `ai.getdial/dial` describes it as "Real phone numbers for AI agents: SMS, iMessage, WhatsApp, AI voice calls, and inbound events."

---

## Official Repo

https://github.com/GetDial-AI/cli

The `dial` CLI (npm `@getdial/cli`), its local stdio MCP server (`dial mcp`), the `dial-cli` Agent Skill, and plugin packaging with the `dial` and `dial-calls` skills. `package.json` and the README declare MIT, but there is no LICENSE file in the tree. The phone numbers, messaging and calls are the hosted service, which is closed source.

---

## How to Use (Agent Onboarding)

> **URL Onboarding with human steps: the agent reads one document and runs the setup, but the CLI has to be installed first and a person verifies an email address and a personal phone number before the agent can operate.**

**One-sentence instruction:**

```
Read https://getdial.ai/skills.md and follow the instructions to get a Dial phone number.
```

**Interaction pattern:** `URL Onboarding` ⚠️ — partial.

People still have to do these things:
- Install the `dial` CLI (Node.js 22+ and git) on the machine, or let the agent run `curl -fsSL https://getdial.ai/install | bash` where it is allowed to install software.
- Give the agent an email address and enter the code Dial emails to it (`dial auth login`, then `dial auth verify-otp`).
- Give the agent a personal phone number that can receive SMS and enter the code texted to it (`dial auth register-number`, then `dial auth verify-otp --number`). A Dial number is refused here. This step creates the account.
- Optionally say yes when the agent asks to install the background notification listening service.

After that, the agent works on its own: `dial doctor --json` reports the next step, `--agent <name>` installs the Dial skill into the agent's own config, the API key is saved locally (mode 0600) and the first number is provisioned.

MCP alternative (a person approves the OAuth consent page in a browser on first connect):

```
https://getdial.ai/mcp
```

---

## Agent Skills

**Status:** ✅ Available

Front matter `name` is `dial-cli` in [skills/dial-cli/SKILL.md](https://github.com/GetDial-AI/cli/tree/main/skills/dial-cli). `dial auth verify-otp --agent <name>` also installs it into the agent's config during onboarding (`claude-code`, `cursor`, `codex`, `opencode`, `pi`, `openclaw`, `nanoclaw`, `hermes`).

```bash
npx skills add GetDial-AI/cli
```

| Skill | What It Teaches the Agent |
|---|---|
| `dial-cli` | Drive the `dial` CLI: onboarding, numbers, messages, calls, waiting for inbound events, `--json` output and docs lookup |
| `dial` | Plugin skill: text, iMessage or WhatsApp people, read and search messages, check which channels a number can receive, and manage Dial numbers |
| `dial-calls` | Plugin skill: place AI voice calls, read how they went and their transcripts, and change how a number answers calls |

---

## MCP

**Status:** ✅ Available — auth required

| Detail | Value |
|---|---|
| **Endpoint** | `https://getdial.ai/mcp` (remote) · `npx @getdial/cli mcp` (local stdio) |
| **Transport** | Streamable HTTP (remote; no SSE variant), stdio (local). On 2026-11-25 an unauthenticated `initialize` returned 401 with OAuth resource metadata |
| **Registry** | Official MCP Registry name `ai.getdial/dial` |
| **Auth** | Remote: OAuth 2.1 with dynamic client registration and browser consent. Local: the API key saved by `dial auth verify-otp`. Tokens are scoped to one account |
| **Tools** | Same operational tools on both: `send_message`, `list_messages`, `lookup_number`, `place_call`, `get_call`, `stop_call`, `wait_for_event`, `list_numbers`, `purchase_number`, `set_number_properties`, allow-list and webhook tools. Local adds `auth_*` onboarding, `listen_*` and local-target tools |
| **Compatible clients** | Docs name Claude Code, Claude chat and Cursor; any MCP client |

---

## What It Does

Dial gives an agent real phone numbers it controls: send and receive SMS, iMessage and WhatsApp, place and answer AI voice calls, and get inbound messages and completed calls back as events. One number can carry several channels, and `lookup_number` tells the agent which channels a recipient can receive on.

Calls run on a Dial-hosted voice agent from a plain-language instruction, or in Self-Hosted mode on the builder's own LLM or audio stack over WebSocket. After a call the agent reads the status and transcript with `get_call`. Inbound calls are answered by the number's inbound instruction, and can be limited to known callers with allow lists.

Pricing on https://getdial.ai/pricing (checked 2026-11-25): pay-as-you-go at $3 per number per month plus metered calls and messages, with a $5 starting credit and no card required; spend pauses at $0. iMessage and WhatsApp need a Local number with add-ons, or the All channels plan. Accounts that have not topped up are capped at 5 minutes per call and 2 concurrent calls.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage title: "Dial: Your agent needs a number." Subline: "Communication stack for AI agents. Calls, SMS, WhatsApp and iMessage through one API." https://getdial.ai/skills.md is written for the agent to follow — [getdial.ai](https://getdial.ai) |
| **Agent-specific primitive** | An agent-owned number used across SMS, iMessage, WhatsApp and calls, plus `wait_for_event` to block on inbound traffic inside the agent loop and the listen service that captures inbound events while no agent is connected |
| **Autonomy-compatible control plane** | After the one-time sign-up, the agent provisions numbers, sends, calls and waits without per-action clicks, bounded by prepaid credit (spend pauses at $0), call-length and concurrency caps on unfunded accounts, inbound allow lists and per-number instructions |
| **M2M integration surface** | Remote + local MCP, `dial` CLI with `--json`, REST with OpenAPI 3.1, Node and Python SDKs, signed webhooks, account event stream, Agent Skills |
| **Identity / delegation** | The agent acts from its own number, not the owner's phone; access is an account-scoped API key or revocable OAuth token; messages and calls (with transcripts) are listable as an audit trail |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Number** | `list_numbers`, `purchase_number`, `set_number_properties` (inbound instruction, language, voice, nickname) |
| **send_message** | Send to a number or group on the number's default channel or a named one |
| **place_call** | Outbound AI voice call from an instruction; `get_call` returns status, duration and transcript; `stop_call` ends it |
| **wait_for_event** | Block until a matching inbound message or completed call arrives |
| **lookup_number** | Which channels a phone number can receive on |
| **Allow list** | `create_policy` / `add_policy_entries`: decline inbound calls from unknown callers |
| **Webhook** | `create_webhook`: signed HTTP POSTs of account events |

---

## Autonomy Model

1. The agent reads https://getdial.ai/skills.md, makes sure the CLI is installed, and checks state with `dial doctor --json`.
2. A person verifies an email address and a personal phone number once; the CLI saves the API key and provisions the first number.
3. The agent sets the number's inbound instruction and allow list.
4. It sends messages and places calls, and reads outcomes with `list_messages` and `get_call`.
5. It waits for replies or inbound calls with `wait_for_event` (or the listen service, or webhooks) and continues the task.

---

## Identity and Delegation Model

- The number is the agent's own; a Dial number cannot be used to register a Dial account.
- API keys (`sk_live_…`) and OAuth tokens are scoped to one account; a tool only sees that account's numbers, messages and calls.
- The account owner can sign in to https://getdial.ai/dashboard with the sign-up email.
- Message and call history (with transcripts) is readable through the API, CLI and MCP.
- Inbound calls can be limited to known callers with allow lists.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| URL onboarding | https://getdial.ai/skills.md |
| MCP | `https://getdial.ai/mcp` (Streamable HTTP, OAuth) · `npx @getdial/cli mcp` (stdio) |
| REST | `https://api.getdial.ai`, Bearer key; OpenAPI 3.1 at https://docs.getdial.ai/openapi.json |
| CLI | `dial` (npm `@getdial/cli`), `--json` output |
| SDKs | Node `@getdial/sdk`, Python; LangChain, Vercel AI SDK, CrewAI, AutoGen and Microsoft Agent Framework integrations |
| Events | Signed webhooks (HMAC) and a live account event stream |
| Docs for agents | https://docs.getdial.ai/llms.txt (append `.md` to any docs URL) |

---

## Human-in-the-Loop Support

A person creates the account once (email and personal phone number) and decides whether to install the background listening service. Spend is drawn from prepaid credit and pauses at $0; top-ups and billing happen in the owner's dashboard. Calls can cold-transfer to a human once one is on the line. Secret webhook header values are typed by the owner through dashboard links rather than pasted into the agent's chat.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **A general-purpose communications API account** | A developer buys a number and writes webhook and call-flow code; no agent skill or MCP session provisions the number, works across SMS/iMessage/WhatsApp, runs the AI call and returns inbound events to the same agent |
| **A personal mobile number** | It belongs to a person, has no machine interface, and mixes the owner's identity with the agent's |

---

## Use Cases

- **Give an agent its own number** — the agent reads skills.md; a person verifies once; the number is provisioned.
- **Text the people the agent works with** — `send_message` on SMS, iMessage or WhatsApp, then `wait_for_event` for the reply.
- **Call a business or person** — `place_call` with an instruction, then read the transcript with `get_call`.
- **Answer inbound** — set the number's inbound instruction and allow list; inbound calls and texts come back as events.
