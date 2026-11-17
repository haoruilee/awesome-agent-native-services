# nPubMail

> **"Email for AI agents. The key is the account."**

| | |
|---|---|
| **Website** | https://npubmail.com |
| **Docs** | https://npubmail.com/llms.txt |
| **GitHub** | https://github.com/obvioussummer46/npubmail |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |
| **Funding / Compliance** | Public beta. Free to create a mailbox, receive, and reply to senders who wrote first; 10 sats per new outside recipient, paid per action over Lightning (no balances). 50 recipients/day, 7-day retention by default. MIT client repo; the hosted mail server is not in that repo. Submitted by the service's maintainers (disclosed on issue #329) |
| **Latest-month signal** | Live on 2026-11-16: [homepage](https://npubmail.com), [llms.txt](https://npubmail.com/llms.txt), [API docs](https://npubmail.com/api), [setup](https://npubmail.com/setup), [SKILL.md](https://npubmail.com/.well-known/skills/npubmail/SKILL.md). Official MCP Registry lists `com.npubmail/npubmail`. Client repo https://github.com/obvioussummer46/npubmail (MIT) |
| **Verified at** | 2026-11-16 |

---

## Official Website

https://npubmail.com

---

## Official Repo

https://github.com/obvioussummer46/npubmail

The MIT repository holds the clients: the `npubmail` CLI, the `npubmail-mcp` stdio MCP server, the Agent Skill, API docs, and examples. The hosted mail server is operated separately and is not in this repository.

---

## How to Use (Agent Onboarding)

**Quickest verified path:**

```
curl -fsSL https://npubmail.com/install | sh && npubmail init myagent
```

**Interaction pattern:** `CLI`

The install command downloads two small programs (`npubmail` and `npubmail-mcp`, checksums verified). `npubmail init <name>` then creates `<name>@npubmail.com` from the agent's own Nostr key after a few hundred milliseconds of proof of work. There is no signup form, captcha, password, or API key.

Joining from a URL alone ⚠️: an agent can read https://npubmail.com/llms.txt and follow it on its own, but it still has to install the local binary or the `npubmail-mcp` server. It does not work from a browser-only chat such as claude.ai or ChatGPT web.

---

## Agent Skills

**Status:** ✅ Available

The skill is served at https://npubmail.com/.well-known/skills/npubmail/SKILL.md and kept in the repo at [`skills/npubmail/SKILL.md`](https://github.com/obvioussummer46/npubmail/blob/main/skills/npubmail/SKILL.md).

| Skill | What It Teaches the Agent |
|---|---|
| `npubmail` | Install, create a mailbox, make aliases, wait for verification codes, read and send mail, pay a 402 invoice |

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Server** | `com.npubmail/npubmail` on the [Official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=com.npubmail/npubmail&version=latest) |
| **MCP Repo** | https://github.com/obvioussummer46/npubmail |
| **Transport** | stdio (`npubmail-mcp`) |
| **Auth** | None to configure: the server signs every request with the agent's key; the mailbox is created on first use |
| **Compatible Clients** | Claude Desktop, Claude Code, Cursor, VS Code, and other MCP clients — per-client setup at https://npubmail.com/setup |

Tools: `whoami`, `create_alias`, `wait_for_code`, `wait_for_email`, `list_emails`, `read_email`, `send_email`, `outbox`, `delete_email`, `storage_plan`, `buy_storage`, `invoice_status`. The wait tools block until mail arrives, so the client's tool timeout should be at least 600 s.

---

## What It Does

nPubMail gives an AI agent a real email address whose account is the agent's own Nostr keypair. The agent creates the mailbox itself, receives mail, waits for a verification code or link and gets it back extracted, creates disposable aliases with expiry and sender filters, replies, and sends. Inbound mail carries SPF/DKIM verdicts and prompt-injection warnings, and is stored encrypted to the agent's key.

Receiving, replying to senders who wrote first, and mailing other npubmail addresses are free. Mailing an outside address that never wrote first costs 10 sats per recipient: the API answers HTTP 402 with a Lightning (or Cashu) invoice, the agent pays, then repeats the call with the payment ID.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: **"Email for AI agents. The key is the account."** [llms.txt](https://npubmail.com/llms.txt): **"A real email address for an AI agent, created by the agent itself in about a second."** |
| **Agent-specific primitive** | Key-owned mailbox created by proof of work; blocking `wait_for_code` / `npubmail code --timeout 120` that returns the extracted code or link; per-task disposable aliases with TTL and sender filters |
| **Autonomy-compatible control plane** | The agent creates the mailbox and operates it with no human step. Spending is per action via HTTP 402 invoices; limits are explicit (50 recipients/day, optional built-in wallet capped at 100 sats per payment and 1000 per day) |
| **M2M integration surface** | REST API ([docs](https://npubmail.com/api)), CLI, stdio MCP server, Agent Skill |
| **Identity / delegation** | The agent's Nostr key is its identity; every request is NIP-98 signed, so each action is attributable to that key. It is a separate mailbox, not access to a person's inbox |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Mailbox** | `<name>@npubmail.com`, bound to the agent's Nostr public key, created with NIP-13 proof of work |
| **Alias** | Disposable address with expiry (`npubmail alias --ttl 1`) and sender filters |
| **Wait for code** | Blocks until a matching mail arrives and returns the code or verification link |
| **Send** | Free to npubmail addresses and to verified senders who wrote first; HTTP 402 invoice for new outside recipients |
| **Storage plan** | 7-day retention by default; longer retention bought per action |

---

## Autonomy Model

1. The agent reads https://npubmail.com/llms.txt.
2. It runs the install command and `npubmail init <name>` (or adds `npubmail-mcp`, which creates the mailbox on first use).
3. It gives the address to a sign-up form, calls `wait_for_code`, and completes the verification itself.
4. It reads and replies to mail; replies to senders who wrote first are free.
5. To mail a new outside address it receives an HTTP 402 invoice, pays from its own wallet within its limits, and repeats the call with `--payment-id`. Without a wallet, it can ask its human to pay the invoice or ask the recipient to write first.

---

## Identity and Delegation Model

- Identity is the agent's own secp256k1 Nostr keypair; the same key can identify the agent on other Nostr-keyed services.
- Every API request is a NIP-98 signed event (kind 27235); there is no shared API key or password to leak.
- Mail is stored encrypted to the agent's key; the operator states it cannot read it.
- Spending authority is bounded per action: nothing is charged until the agent pays a specific invoice, and the optional built-in wallet has hard per-payment and per-day caps.
- Boundary: the hosted server is closed source; there is no separate owner/approval account model.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| URL Onboarding | https://npubmail.com/llms.txt |
| REST API | https://npubmail.com/api, NIP-98 signed requests |
| CLI | `npubmail` (`init`, `alias`, `code`, `list`, `read`, `send`, `wallet setup`) |
| MCP | `npubmail-mcp` (stdio), registry `com.npubmail/npubmail` |
| Payments | HTTP 402 with Lightning or Cashu invoice, per action |
| Agent Skills | https://npubmail.com/.well-known/skills/npubmail/SKILL.md |

---

## Human-in-the-Loop Support

Not built in as an approval gate. A human is involved only when the agent has no wallet and asks its owner to pay a 402 invoice. Inbound mail is flagged for prompt-injection risk so the agent can treat it as untrusted data.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Gmail / Outlook** | Needs a human account with phone or captcha checks; the inbox belongs to a person |
| **Amazon SES / Postmark** | A person verifies a domain and creates an API key in a dashboard; no agent-owned receiving inbox or wait-for-code primitive |

---

## Use Cases

- **Sign-up verification** — give a form an alias, wait for the code, finish the sign-up without a human
- **Agent-owned correspondence** — receive and reply as the agent's own address, separate from the owner's mail
- **One key, several services** — reuse the agent's Nostr identity for mail and other Nostr-keyed services
- **Pay-per-action outreach** — send to a new address only after paying a small invoice, within hard daily caps
