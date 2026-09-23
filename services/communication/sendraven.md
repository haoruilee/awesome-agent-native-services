# SendRaven

> **"Email infrastructure for AI agents."**

| | |
|---|---|
| **Website** | https://sendraven.ai |
| **Docs** | https://sendraven.ai/docs |
| **GitHub** | https://github.com/CommonNinja/sendraven-mcp-server (MCP server, MIT; the platform itself is closed source) |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |
| **Funding / Compliance** | Built by Common Ninja; free tier of 3,000 emails/month (a payment method is required before any outbound email, and is never charged on the free tier) |

---

## Official Website

https://sendraven.ai

---

## Official Repo

https://github.com/CommonNinja/sendraven-mcp-server

The MCP server is open source (MIT) and published as [`@sendraven/mcp`](https://registry.npmjs.org/@sendraven%2fmcp) and as `ai.sendraven/mcp` in the official MCP Registry. The platform itself is closed source; its machine-readable surface is the OpenAPI spec at https://sendraven.ai/openapi.json and the agent-facing summary at https://sendraven.ai/llms.txt.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** MCP server (remote Streamable HTTP with OAuth, or stdio with an API key); REST for everything else

```bash
npx -y @sendraven/mcp   # with SENDRAVEN_API_KEY=sk_live_... in the environment
```

Add to MCP client configuration:

```json
{
  "mcpServers": {
    "sendraven": {
      "command": "npx",
      "args": ["-y", "@sendraven/mcp"],
      "env": { "SENDRAVEN_API_KEY": "sk_live_..." }
    }
  }
}
```

Or connect a remote-capable client to `https://mcp.sendraven.ai/mcp` and sign in with OAuth. Over REST, the first useful call for an agent is:

```bash
curl "https://api.sendraven.ai/v1/threads?awaiting_reply=true" -H "Authorization: Bearer sk_live_..."
```

A person sets up the workspace first: creates it, verifies a sending domain and adds a payment method. An agent cannot self-register, because sending from a domain requires a person to prove control of its DNS.

---

## Agent Skills

**Status:** ⚠️ Not yet published

Search community skills: `npx clawhub@latest search sendraven`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/CommonNinja/sendraven-mcp-server |
| **MCP Docs** | https://sendraven.ai/docs/mcp |
| **Transport** | Streamable HTTP (`https://mcp.sendraven.ai/mcp`, OAuth) and stdio (`npx -y @sendraven/mcp`, API key) |
| **Tools** | 55, each annotated read-only or destructive |
| **Compatible Clients** | Claude Desktop, Claude Code, Cursor, Cline, any MCP-compatible client |

The MCP server is a thin proxy over the public REST API and holds no credentials of its own, so every guardrail on the key or token applies to MCP calls exactly as to REST calls.

---

## What It Does

SendRaven is an email platform whose stated primary caller is an AI agent. An agent sends transactional email from the customer's own verified domain, receives the replies, and reads them as thread state: each reply is joined to its conversation on `Message-ID` (never on subject), quoted history is stripped, and a thread carries an `awaiting_reply` flag, so the agent can ask "what needs an answer?" and reply in the same thread.

The second half is the constraint model. Limits live on the credential the agent holds, not on the workspace: a per-key daily send cap, a recipient allowlist, and an approval hold that turns every send from that key into a draft a person releases. A key cannot edit its own limits, mint a looser key, or approve its own drafts.

The same platform also runs campaigns, automations and ordinary transactional mail (it replaced the email providers of its builders' own products), so it is not agent-only; agents are the primary consumer on the homepage, the docs and the MCP page.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"Email infrastructure for AI agents. Let your AI agents run real email conversations."* — https://sendraven.ai; MCP page: https://sendraven.ai/mcp |
| **Agent-specific primitive** | Inbound replies as structured thread state for an agent (`GET /v1/threads?awaiting_reply=true`, stripped reply text, `sender_authenticated` from DMARC or aligned DKIM), and guardrails on the agent's credential (daily cap, recipient allowlist, approval hold) — https://sendraven.ai/docs/agents |
| **Autonomy-compatible control plane** | An agent with an unguarded or capped key completes send → inbound webhook → read thread → reply with no human click. Constraints: `429 daily_limit`, `403 recipient_not_allowed`, and the approval hold — https://sendraven.ai/docs/approvals |
| **M2M integration surface** | REST API with Bearer keys, OpenAPI at https://sendraven.ai/openapi.json, remote and stdio MCP, signed webhooks. The dashboard is used by a person for setup only. |
| **Identity / delegation** | Each agent holds its own API key or OAuth token, separate from the human's dashboard session, carrying its own scopes and guardrails. Approvals record the requesting key and who decided them. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Awaiting-reply thread** | Conversation joined on `Message-ID`; `awaiting_reply` is set when a person writes and cleared when the agent answers (or calls `POST /v1/threads/{id}/handled`) |
| **Inbound webhook** | `inbound` event carrying `thread_id`, the stripped reply `text`, and `sender_authenticated` |
| **Reply in thread** | `POST /v1/emails` with `reply_to_message_id` sets the threading headers so the reply lands in the recipient's existing conversation |
| **Per-key daily cap** | Counted in recipients (`to`, `cc`, `bcc`) per UTC day; `429 daily_limit` is a stop, not a retry |
| **Recipient allowlist** | Addresses or domains a key may mail; anything else answers `403 recipient_not_allowed` |
| **Approval hold** | `requires_approval` on a key turns each send into a draft in an approvals queue for a person to release |

---

## Autonomy Model

1. A person creates the workspace, verifies a domain, and issues the agent a key with the guardrails they want.
2. The agent sends: `POST /v1/emails` (or the `send_email` MCP tool).
3. The recipient replies; SendRaven posts an `inbound` webhook with the thread id and stripped text.
4. The agent reads the thread (`GET /v1/threads/{id}`), or polls `GET /v1/threads?awaiting_reply=true`.
5. The agent replies in the same thread with `reply_to_message_id`.

No step needs a human unless the key carries the approval hold, in which case step 2 and step 5 wait for a person to release the draft.

---

## Identity and Delegation Model

- Each agent gets its own API key (or OAuth access token through MCP), separate from any person's dashboard session.
- Delegated permission is expressed on that credential: scopes, sends per day, which recipients, and whether a person must approve.
- A key cannot raise its own limits, create a key with scopes or guardrails looser than its own, or approve its own drafts; OAuth tokens and guarded keys cannot decide approvals at all.
- Approvals record the requesting key and who decided them; per-key send counters are kept per day.
- Boundary, stated honestly: mail is sent from the customer's own verified domain, not from a separate per-agent mailbox, and the message log does not yet attribute each sent message to the key that sent it (approvals and per-key counters do).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `https://api.sendraven.ai/v1`, Bearer `sk_live_…` keys, snake_case JSON, one error vocabulary |
| OpenAPI | https://sendraven.ai/openapi.json |
| MCP Server | Remote Streamable HTTP with OAuth, or `npx -y @sendraven/mcp` over stdio |
| Webhooks | Signed deliveries for `inbound`, `delivery`, `bounce`, `complaint`, `open`, `click` and more |
| llms.txt | https://sendraven.ai/llms.txt |

---

## Human-in-the-Loop Support

Built in, per key. A key with `requires_approval` never sends directly: each message becomes an approval a person releases or rejects in the dashboard (or through an unguarded API key). Held messages keep their schedule, a release re-checks suppression and opt-outs because a hold can last days, and stale approvals expire. Keys without the hold run fully autonomously within their cap and allowlist.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **SendGrid** | Built for a backend that sends and forgets; replies are not returned as thread state an agent can act on, and there are no per-credential caps, allowlists or approval holds |
| **Mailgun** | Inbound routing forwards raw messages to a URL; no conversation state, no `awaiting_reply`, no guardrails on the calling key |
| **Amazon SES** | Delivery infrastructure only; inbound, threading, quoted-text stripping and any limit on an autonomous caller are left to the developer |

---

## Use Cases

- **Support or sales follow-up agent** — sends from the company's own domain, answers replies in thread, and lists what still needs an answer
- **Supervised outreach** — an agent drafts every message under an approval-hold key and a person releases each one
- **Bounded autonomy** — an agent limited to 50 recipients a day at one customer's domain, enforced by the key rather than by the prompt
- **Transactional mail from an agent** — receipts, reminders and notifications sent through MCP, with bounces and complaints suppressed automatically
