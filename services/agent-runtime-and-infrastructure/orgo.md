# Orgo

> **"Computers for Agents."**

| | |
|---|---|
| **Website** | https://www.orgo.ai |
| **Docs** | https://docs.orgo.ai/for-agents |
| **GitHub** | No official public platform repository (hosted product is closed-source) |
| **Classification** | `agent-native` |
| **Category** | [Agent Runtime & Infrastructure Services](README.md) |
| **License** | Hosted product closed-source. https://github.com/nickvasilescu/orgo-mcp is MIT and is an API wrapper, not the platform source |
| **Operator** | Organic Intelligence, Inc. |
| **Latest-month signal** | Checked 2026-11-25: [homepage](https://www.orgo.ai) HTTP 200, H1 "Computers for Agents"; [orgo.md](https://www.orgo.ai/orgo.md), [for-agents](https://docs.orgo.ai/for-agents), [MCP guide](https://docs.orgo.ai/guides/mcp), [llms.txt](https://docs.orgo.ai/llms.txt), and [computer skill](https://orgo.ai/skills/computer/SKILL.md) HTTP 200; MCP GET [https://www.orgo.ai/mcp](https://www.orgo.ai/mcp) 405 |
| **Verified at** | 2026-11-25 |

---

## Official Website

https://www.orgo.ai

Homepage H1: *"Computers for Agents."* Title: *"Orgo - Computers for AI agents."* Meta description: *"Secure, always-on Linux, Windows and Mac computers for AI agents."* Operator: Organic Intelligence, Inc. Docs `llms.txt`: *"Orgo is cloud computers for AI agents, with your own agents inside."* Linux and Windows are self-serve. A Mac, or an iPhone offered in the app, is stock-dependent and is not the same self-serve create path (`llms.txt`).

---

## Official Repo

No public platform source repository is published. The hosted computers product is closed-source.

https://github.com/nickvasilescu/orgo-mcp is MIT (32 stars, pushed 2026-08-28T01:45:30Z). Its README calls itself an MCP server for the Orgo API. This listing does not treat that repository as the Orgo platform, and it does not call the platform open source.

---

## ⭐ How to Use (Agent Onboarding)

> **⭐ URL Onboarding — the agent reads one document and can create its own account. Read the expiry and busy-signup limits before treating that as a finished join.**

**Interaction pattern:** `URL Onboarding` ⭐ + REST + hosted MCP. Unclaimed accounts that have added less than $5 expire 72 hours after signup. While signups are busy, `verification.required` blocks launches until a person opens `claim.url` or credit is added. The usual `claude mcp add` sign-in is a person clicking Allow, which is not this URL path.

**One-sentence instruction:**

```
Read https://www.orgo.ai/orgo.md and follow the instructions to create an agent account.
```

[orgo.md](https://www.orgo.ai/orgo.md) (HTTP 200 on 2026-11-25) tells an agent with nobody present to approve:

```bash
curl -s -X POST https://www.orgo.ai/api/v1/agents \
  -H 'Content-Type: application/json' \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{"name": "<your name>"}'
```

That call creates an agent account with $2 of starting credit and no email. Save `api_key` once. Give the person `claim.url` when you can.

Limits from the same document:

- An account that has added less than $5 and is never claimed expires 72 hours after signup. Computers stop and keys stop working.
- After $5 has been added in all, the account no longer expires that way, and the cap rises (the page says up to 5 computers and 5 workspaces).
- While agent signups are unusually busy, the response carries `verification.required`. Until a person opens `claim.url` and verifies, or credit is added, a launch answers 403 `agent_verification_required`.

If a person is already here, orgo.md says not to create another account. Use `npx -y orgo@latest init` or the device-code curl, and the person signs in and clicks Allow. That path is a human sign-in. Hosted MCP at `https://www.orgo.ai/mcp` is the same class of connect (`claude mcp add --transport http orgo https://www.orgo.ai/mcp`). GET that URL returned 405 on 2026-11-25; the server is POST-only.

---

## Agent Skills

**Status:** ✅ Available — Claude Code skill `computer`

The skill assumes an Orgo account, the `orgo` CLI, and `orgo login`. It does not replace the agent-signup URL above.

```bash
mkdir -p ~/.claude/skills/computer && \
  curl -fsSL https://orgo.ai/skills/computer/SKILL.md \
    -o ~/.claude/skills/computer/SKILL.md
```

| Skill | What It Teaches the Agent |
|---|---|
| `computer` | When to start an Orgo computer, run `orgo run`, and screenshot, after a CLI login (https://docs.orgo.ai/guides/skill.md) |

---

## MCP

**Status:** ✅ Available — hosted Streamable HTTP, POST-only

| Detail | Value |
|---|---|
| **MCP Repo** | Hosted by Orgo. Do not cite nickvasilescu/orgo-mcp as the platform source |
| **Endpoint** | `https://www.orgo.ai/mcp` |
| **Transport** | Streamable HTTP. GET returned 405 on 2026-11-25 |
| **Auth** | Person sign-in (Allow) for the documented `claude mcp add` path, or a bearer API key |
| **Docs** | https://docs.orgo.ai/guides/mcp |
| **Compatible Clients** | Claude Code and other clients that POST to a remote MCP URL |

---

## What It Does

Orgo rents an isolated cloud computer to an agent: Linux or Windows (and Mac when the app has stock), with a desktop, a browser, and a terminal. The agent screenshots, clicks, types, and runs bash. Each computer is its own VM. Docs `llms.txt`: *"A new computer is online in seconds and runs until you stop it."* Orgo does not supply the agent model. The caller brings Claude Computer Use, another computer-use model, or its own loop.

The hosted product is closed-source. API keys begin with `sk_live_` (docs). A computer status moves through creating, running, frozen/stopped, and deleted. `stop` freezes the machine.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage H1: *"Computers for Agents."* `llms.txt`: *"Orgo is cloud computers for AI agents, with your own agents inside."* Sources: https://www.orgo.ai and https://docs.orgo.ai/llms.txt |
| **Agent-specific primitive** | An isolated computer with screenshot, click, type, and bash, plus an agent account created by `POST /api/v1/agents`. |
| **Autonomy-compatible control plane** | After a working key, the agent creates a computer and acts with no per-click approval. Busy signups and unclaimed expiry can still stop a launch until a person claims the account or credit is added. |
| **M2M integration surface** | `POST /api/v1/agents`, the computers API, `orgo` CLI, hosted MCP, `orgo.md`, and https://docs.orgo.ai/llms.txt. |
| **Identity / delegation** | Agent signup returns an `api_key` and a `claim.url` for a person. Workspace keys and computer ids scope later calls. Unclaimed accounts are time-limited. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent account** | `POST https://www.orgo.ai/api/v1/agents` — no email, $2 starting credit, `claim.url`. |
| **Computer** | Isolated Linux/Windows VM (Mac via the app). Screenshot, click, type, bash. |
| **Workspace** | Computers sit in a workspace. Starting credit allows one computer at a time until $5 has been added. |
| **MCP / CLI** | `https://www.orgo.ai/mcp` and `orgo` (`curl -fsSL https://orgo.ai/install.sh \| bash` per the skill guide). |

---

## Autonomy Model

1. The agent reads https://www.orgo.ai/orgo.md.
2. If nobody is present to approve, it `POST`s `/api/v1/agents` and stores the key.
3. It creates a workspace computer and runs the screenshot / click / type / bash loop.
4. If the response is `verification.required` or HTTP 403 `agent_verification_required`, it stops and sends `claim.url` to a person, or adds credit. It does not keep retrying launches.
5. If the account is still unclaimed and under $5 added, it expires 72 hours after signup.

---

## Identity and Delegation Model

- Agent signup is a distinct account from a person's device-code login. orgo.md says not to create an agent account when a person is already present.
- The API key is shown once. The document says not to print it into chat.
- `claim.url` is how a person keeps the account. Until claim, invites and invoicing are unavailable, and the 72-hour expiry applies if less than $5 has been added.
- A computer is scoped to the workspace of that key.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Agent signup | `POST https://www.orgo.ai/api/v1/agents` |
| Claim | `POST https://www.orgo.ai/api/v1/agents/claim` |
| REST | `https://www.orgo.ai/api` — bearer `sk_live_…` key |
| CLI | `npx -y orgo@latest init` or https://orgo.ai/install.sh |
| Hosted MCP | `https://www.orgo.ai/mcp` (POST-only) |
| Docs | https://docs.orgo.ai/for-agents · https://docs.orgo.ai/llms.txt · https://www.orgo.ai/orgo.md |

---

## Human-in-the-Loop Support

The URL path needs no email and no Allow click to create the account. A person is required to keep it (claim) and, when Orgo sets `verification.required`, to open `claim.url` or to add credit before a computer will launch. The MCP add command and `orgo init` are person sign-in paths. VNC lets a person watch a running computer.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **nickvasilescu/orgo-mcp as "the product"** | An MIT API wrapper. The computers, billing, and agent signup are the hosted service, which does not publish platform source. |
| **E2B Desktop** (already listed) | A different vendor's Linux desktop SDK. Orgo's agent account, claim URL, and Windows/Mac offering are not that SDK. |
| **A VPS plus VNC** | No agent-signup document, no computer-use action API, and no per-agent key lifecycle. |

---

## Use Cases

- **An agent that needs a desktop without a human account** — `POST /api/v1/agents`, then a Linux computer, within the $2 credit and the 72-hour claim window.
- **Computer use with a person's Orgo account** — device-code or MCP Allow, then screenshot and click on that workspace.
- **A long-lived computer after claim** — once $5 has been added, orgo.md says the unclaimed expiry no longer applies.
