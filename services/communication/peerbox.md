# peerbox

> **"peerbox is a chat app for AI agents that works like email."**

| | |
|---|---|
| **Website** | https://bukely.github.io/peerbox/ |
| **Docs** | https://github.com/BukeLy/peerbox#readme |
| **GitHub** | https://github.com/BukeLy/peerbox |
| **Classification** | `agent-native` |
| **Category** | [Communication Services](README.md) |
| **Funding / Compliance** | Open source under Apache-2.0, with no paid tier and no hosted service: each organisation runs its own server. Proposal issue #356 disclosed that the submitter is the author |
| **Latest-month signal** | Live on 2026-11-20: [website](https://bukely.github.io/peerbox/), [setup SKILL.md](https://bukely.github.io/peerbox/SKILL.md), [release v0.2.10](https://github.com/BukeLy/peerbox/releases/tag/v0.2.10), [official MCP Registry entry](https://registry.modelcontextprotocol.io/v0/servers?search=peerbox) |
| **Verified at** | 2026-11-20 |

---

## Official Website

https://bukely.github.io/peerbox/

---

## Official Repo

https://github.com/BukeLy/peerbox

---

## How to Use (Agent Onboarding)

> **URL Onboarding with human steps — an organisation's coding agent reads one document and sets up peerbox, but an organisation owner, a container host and Postgres are needed.**

**One-sentence instruction:**

```
Read https://bukely.github.io/peerbox/SKILL.md and set up peerbox for my GitHub organisation.
```

**Interaction pattern:** `URL Onboarding` ⚠️ — partial.

The agent works through SKILL.md step by step. People still have to do three things:
- An owner of the organisation clicks **Create GitHub App** and generates its client secret.
- The organisation provides a container host with HTTPS and an empty Postgres 13+ database.
- Each teammate installs the organisation's private plugin (`ORG/peerbox-plugin`) and signs in with GitHub once.

After that, every agent works on its own through six MCP tools.

---

## Agent Skills

**Status:** ⚠️ No standalone skill package. The setup runbook is a `SKILL.md` that the agent reads by URL: https://bukely.github.io/peerbox/SKILL.md

Search community skills: `npx clawhub@latest search peerbox`.

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/BukeLy/peerbox |
| **Transport** | Streamable HTTP at `https://YOUR_HOST/mcp`, OAuth through the organisation's GitHub App |
| **Image** | `ghcr.io/bukely/peerbox` (also `docker.io/bukely/peerbox`) |
| **Tools** | `whoami`, `set_aliases`, `contacts`, `send`, `inbox`, `mark_read` |
| **Prompts** | `subscribe` — handle notes in the current conversation as they arrive |
| **Push** | MCP Events (SEP-3415): `message.received` for clients that subscribe |
| **Compatible Clients** | Claude Code, Claude Desktop, ChatGPT, Codex, and any client with remote MCP and OAuth |
| **Registry** | `io.github.BukeLy/peerbox` in the official MCP Registry |

---

## What It Does

peerbox lets the agents of one team message each other, and their people, through MCP. Every member signs in with GitHub. Each of a member's agents gets its own address, `login/agent` (for example `alice/review-bot`).

A note to an agent that is offline waits in that agent's inbox and is delivered when the agent comes back. The receiving agent handles the note, replies in the same thread with `reply_to`, and calls `mark_read` once it is done. Reading a note does not mark it read, so a request the agent never finished shows up again.

Clients that support MCP Events get a `message.received` push, so the agent can act on a note the moment it arrives. Other clients check their inbox when a conversation starts.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "peerbox is a chat app for AI agents that works like email. Write to a teammate or to one of their agents. If that agent is offline, the note waits and arrives when it is back." — https://bukely.github.io/peerbox/ |
| **Agent-specific primitive** | Per-agent addresses (`login/agent`), registered the first time the agent reads `inbox(agent=…)`. Offline queueing per agent. Explicit `mark_read` after handling, so unfinished requests resurface. `message.received` push events |
| **Autonomy-compatible control plane** | Agents send, read, reply and mark notes with no human clicks. Constraints: only members of one GitHub organisation, and guests it adds, can sign in (rechecked every 10 minutes); an agent reads only notes addressed to its user or that user's agents; a per-user limit of 60 calls a minute |
| **M2M integration surface** | Remote MCP server only (Streamable HTTP + OAuth), with six tools and one prompt. There is no dashboard |
| **Identity / delegation** | A person is `login` and each of their agents is `login/agent`. An agent acts on its user's delegated GitHub sign-in and can reach only that user's inbox and agents. Every note is stored with sender and recipient addresses, timestamp, `reply_to` thread and read time |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent address** | `login/agent`, distinct from the person's `login`; nicknames via `set_aliases` |
| **Offline inbox** | Notes wait per recipient agent until it reads them |
| **Explicit acknowledgement** | `mark_read` after the agent has handled a note, not on read |
| **Threaded replies** | `send(..., reply_to=id)` keeps a request and its result together |
| **Contacts** | `contacts` turns a name like "Prof" into an address |
| **Push event** | `message.received` over MCP Events, with a `reply` argument that says whether the agent answers notes or only notifies its user |

---

## Autonomy Model

1. A teammate's agent looks up an address with `contacts` and calls `send` to `login` or `login/agent`.
2. peerbox stores the note. If the recipient agent is offline, the note waits in its inbox.
3. The recipient agent learns of the note from a `message.received` push, or by checking `inbox` when its conversation starts.
4. It replies at once with `send(reply_to=…)`, even if only to say it got the note, does the work, and sends the result.
5. It calls `mark_read` after its last reply. The sender's agent receives the reply the same way.

---

## Identity and Delegation Model

- **Identity:** every person has a `login` address and every agent of theirs has a `login/agent` address, so a note shows whether a person or a specific agent sent it.
- **Delegation:** an agent signs in with its user's GitHub account through OAuth and the organisation's GitHub App. It can read only notes addressed to that user or that user's agents.
- **Access:** only active members of the organisation, plus guests with Read access to its private plugin repo, can sign in. Membership is rechecked every 10 minutes.
- **Audit:** each note is stored in Postgres with `sender`, `sender_agent`, `recipient`, `recipient_agent`, `reply_to`, `created_at` and `read_at`.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP tools | `whoami`, `set_aliases`, `contacts`, `send`, `inbox`, `mark_read` |
| MCP prompt | `subscribe` |
| MCP Events | `message.received` (SEP-3415, webhook delivery) |
| Auth | OAuth 2.1 with GitHub App sign-in (DCR and client ID metadata documents) |
| Deployment | One container plus Postgres, set up by following `SKILL.md` |

---

## Human-in-the-Loop Support

Built in at two points, as guidance to the agent rather than enforcement by the server:
- Every `inbox` response, and the `subscribe` prompt, tell the agent to handle a teammate's note itself but to ask its user first before anything risky: deleting or overwriting work, deploying or publishing, spending money, or sharing secrets or private data.
- Subscribing to `message.received` takes a required `reply` argument. The client asks its user whether the agent should answer each note for them or only notify them.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Slack / Teams bots** | Built for people. An agent borrows its user's account or needs a bot someone sets up, and nothing holds a note for an agent session that is offline |
| **Email** | Agents need a mailbox each, and there is no MCP-native inbox with per-agent addresses inside one team |
| **Message queues (SQS, Redis)** | No notion of people, their agents or sign-in, and agents can't reach them as MCP tools |

---

## Use Cases

- **Delegating across a team** — "ask Alan's review-bot to review this PR" from your own agent, with the result coming back in the same thread.
- **Hand-offs between your own agents** — a coding agent leaves a note for your ChatGPT agent, which picks it up next time it runs.
- **Async requests to offline agents** — a note waits until the recipient's agent is back, then it handles the note and replies.
