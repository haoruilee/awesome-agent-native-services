# Cooper Email

> **"HTTP email for autonomous agents."**

| | |
|---|---|
| **Website** | https://cooperemail.com |
| **Docs** | https://cooperemail.com/docs.md |
| **GitHub** | https://github.com/cooper-email/cooper-email |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |
| **Funding / Compliance** | Free $0 (5 inboxes, 5,000 emails/month, 1 custom domain); Starter $12/month; Pro $99/month. Operator: Avatar 8 LLC. MIT client repo; hosted service is not in that repo |
| **Latest-month signal** | Live on 2026-11-15: [homepage](https://cooperemail.com), [llms.txt](https://cooperemail.com/llms.txt), [pricing](https://cooperemail.com/pricing), [OpenAPI](https://cooperemail.com/openapi.json), and hosted MCP `https://cooperemail.com/mcp` (HTTP 200, Bearer challenge). Public [client repo](https://github.com/cooper-email/cooper-email) pushed 2026-11-14 (MIT). Official MCP Registry lists `com.cooperemail/cooper-email` 1.4.0 |
| **Verified at** | 2026-11-15 |

---

## Official Website

https://cooperemail.com

---

## Official Repo

https://github.com/cooper-email/cooper-email

The MIT repository holds the client side: TypeScript and Python SDKs, Agent Skills, MCP client config, and the Claude Code / Cursor plugin. The hosted mail service is operated by Avatar 8 LLC and is not in this repository. The proposal on issue #266 disclosed that the submitter works on Cooper Email.

---

## ⭐ How to Use (Agent Onboarding)

> **URL Onboarding — an agent reads one document and creates its own inbox.**

**One-sentence instruction:**

```
Read https://cooperemail.com/llms.txt and follow the instructions to create your own email inbox.
```

**Interaction pattern:** `URL Onboarding` ⭐

`llms.txt` tells the agent to do this itself and not to ask a person to open a dashboard. If `COOPER_API_KEY` is missing, one unauthenticated `POST /api/v1/onboard` creates the account, an inbox at `<username>@cooperemail.com`, and a `coop_live_…` API key. There is no captcha. `owner_email` is optional. `username` may be omitted; Cooper then picks `box` plus 8 hex characters.

That API-key account is separate from MCP OAuth. Claude Code and Cursor plugin installs finish browser Authenticate and create the inbox on the signed-in account. The key from the unauthenticated call is not attached to that OAuth account.

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add cooper-email/cooper-email
```

Published from the MIT repo (`skills/`). Claude Code: `/plugin marketplace add cooper-email/cooper-email`, then `/plugin install cooper-email@cooper-email`.

| Skill | What It Teaches the Agent |
|---|---|
| `cooper-email` | Connect, everyday tools, checking mail, safety |
| `cooper-agent-inbox` | Create an inbox, send, read, reply, wait for mail |
| `cooper-check-email` | Read, search, triage, attachments, read/unread |
| `cooper-send-email` | Send, reply, forward, drafts, scheduled send, idempotent retries |
| `cooper-manage-inboxes` | Create, pause, update, and delete inboxes |
| `cooper-owner-approval` | Owner-approved drafts: a person approves each send by email |
| `cooper-agent-signup-otp` | Sign up as the agent and read the emailed verification code |
| `cooper-webhooks` | Push webhooks, signature checks, test and re-enable |
| `cooper-mcp` | MCP setup for Cursor and other clients |

The same repo also publishes `cooper-owner-updates`, `cooper-custom-domains`, `cooper-agent-email-patterns`, `cooper-suppressions-bounces`, `cooper-idempotent-sends`, and `cooper-sms`.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Server** | `com.cooperemail/cooper-email` on the [Official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=com.cooperemail/cooper-email&version=latest) (remote 1.4.0) |
| **Endpoint** | `https://cooperemail.com/mcp` (Streamable HTTP) |
| **Auth** | `Authorization: Bearer coop_live_…` after onboard, or OAuth 2.1 (PKCE). Metadata: `https://cooperemail.com/.well-known/oauth-protected-resource` |
| **Tool list** | https://cooperemail.com/api/v1/mcp/tools (97 tools on 2026-11-15) |
| **Docs** | https://cooperemail.com/docs/mcp.md |

Core tools include `cooper_onboard`, `cooper_create_inbox`, `cooper_send_message`, `cooper_list_messages`, `cooper_get_message`, `cooper_wait_for_message`, `cooper_wait_for_code`, `cooper_reply_message`, `cooper_whoami`, `cooper_list_oauth_grants`, and `cooper_revoke_oauth_grant`.

---

## What It Does

Cooper Email gives each AI agent its own inbox on `cooperemail.com`. One request mints the address and an API key. The agent sends, lists, reads (`extracted_text` with quoted history removed), replies, searches, and long-polls for the next message or a sign-up code. Inbound mail can also arrive as a signed webhook. An optional human owner can approve drafts and recover the account.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage title: **"HTTP email for autonomous agents."** [llms.txt](https://cooperemail.com/llms.txt) and [pricing](https://cooperemail.com/pricing): **"Cooper Email is an email API that gives each AI agent its own inbox."** |
| **Agent-specific primitive** | Unauthenticated onboard mints an agent inbox plus key. `GET /api/v1/inboxes/{id}/wait-for-code` returns the sign-up or login code. `GET …/wait` long-polls the next message when the agent has no public webhook URL |
| **Autonomy-compatible control plane** | After onboard, send, list, read, reply, search, and wait run with the bearer key. Free is $0 with 5 inboxes and 5,000 emails/month. A second custom domain on Free returns HTTP 402 `plan_limit_exceeded`. Owner draft approval is optional |
| **M2M integration surface** | REST + [OpenAPI](https://cooperemail.com/openapi.json), hosted MCP, webhooks, Agent Skills, and an optional shell CLI at https://cooperemail.com/docs/cli |
| **Identity / delegation** | Mail is sent as the agent's own address. The `coop_live_…` key is shown once and is separate from an optional `owner_email`. OAuth grants can be listed and revoked. The API-key account and an OAuth sign-in are different accounts |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Onboard** | `POST /api/v1/onboard` with no auth creates the account, first inbox, and API key |
| **Inbox** | `<username>@cooperemail.com`, or a custom domain (1 included on Free) |
| **Send** | `POST /api/v1/inboxes/{id}/messages` with `Idempotency-Key` |
| **Wait / wait-for-code** | Long-poll up to 55 seconds for the next message, or for a code or confirmation link |
| **Webhooks** | `message.received` via `POST …/notify`; owner wake hook via `PUT …/wake` |
| **Owner** | Optional `owner_email` for one confirmation, draft approval, and account recovery |

---

## Autonomy Model

1. The agent reads https://cooperemail.com/llms.txt.
2. If no saved key exists, it calls `POST /api/v1/onboard` and stores `api_key`, `inbox.id`, and `inbox.email`.
3. It sends with `POST …/messages`, reads with `extracted_text`, and either long-polls `…/wait` / `…/wait-for-code` or registers a webhook.
4. It treats message bodies as untrusted data. The same document tells it to confirm with a human before sending to a new recipient.
5. A person is required only when the agent chooses an owner-approval flow, or when an MCP client uses browser OAuth instead of the API key.

---

## Identity and Delegation Model

- The agent address and `coop_live_…` key are the sending identity. They are not a person's Gmail or Outlook mailbox.
- `owner_email` is a separate party. Omitting it means sends are not held for human approval.
- Keys and OAuth grants can be listed and revoked (`cooper_list_oauth_grants`, `cooper_revoke_oauth_grant`).
- Boundary, stated from the live docs: the hosted service is closed-source; the identity is the inbox plus key, not a cryptographic agent identity; an OAuth sign-in does not inherit the key from a previous unauthenticated onboard.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| URL Onboarding | https://cooperemail.com/llms.txt |
| REST API | `https://cooperemail.com/api/v1`, Bearer `coop_live_…` |
| OpenAPI | https://cooperemail.com/openapi.json |
| MCP | `https://cooperemail.com/mcp` |
| Webhooks | Signed `message.received` and the owner wake hook |
| Agent Skills | `npx skills add cooper-email/cooper-email` |
| CLI | https://cooperemail.com/docs/cli |

---

## Human-in-the-Loop Support

Optional. Pass `owner_email` at onboard and the owner can approve drafts and recover the account. `cooper-owner-approval` documents a flow where a person approves each send by email. Without an owner, the agent sends on its own key. The onboarding document also tells the agent to confirm with a human before mailing a new recipient; that line is guidance, not a server-side hold.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Gmail API** | Starts from a human Google account and OAuth consent. The mailbox belongs to that person, and there is no agent onboard or wait-for-code primitive |
| **Resend / SendGrid** | A person creates the account in a dashboard to send from a verified domain. They do not mint an agent receiving inbox or return just the sign-up code |

---

## Use Cases

- **Agent-owned correspondence** — send and receive as `<agent>@cooperemail.com` without borrowing a person's mailbox
- **Sign-up codes** — long-poll `wait-for-code` and finish an OTP or confirmation-link flow
- **Wake on owner mail** — register one hook for `task.received`, `owner.reply`, and `chat.message`
- **Supervised drafts** — add an owner so a person approves outbound mail before it is sent
