# The Vibe Hosting

> **"One prompt → root Linux → your project is live."**

| | |
|---|---|
| **Website** | https://thevibehosting.com |
| **Docs** | https://thevibehosting.com/SKILL.md · https://thevibehosting.com/api |
| **Classification** | `agent-native` |
| **Category** | [Code Execution Services](README.md) |
| **Funding / Compliance** | Closed-source hosted service; operated from the Czech Republic (EU); GDPR notice at https://thevibehosting.com/privacy |

---

## Official Website

https://thevibehosting.com

---

## Official Repo

Not public — the service itself is closed-source. The official entry points are the hosted REST API, the agent-addressed `SKILL.md` and the API reference.

---

## ⭐ How to Use (Agent Onboarding)

**The quickest path for an agent to start using this service.**

```text
Read https://thevibehosting.com/SKILL.md and follow the instructions to deploy your project.
```

The agent's first call creates the account and the server in one step:

```bash
curl -X POST https://thevibehosting.com/create
# → server id, live https://<slug>.thevibehosting.com, SSH command + key, and the account api_key
```

---

## Agent Skills

**Status:** ✅ Available (URL onboarding at `https://thevibehosting.com/SKILL.md`; not installable via `npx skills add`)

| Skill | What It Teaches the Agent |
|---|---|
| `SKILL.md` | How to create a server, store the `api_key`, deploy over SSH/rsync (`/root/www` or `/root/run.sh`), manage sleep/wake, read billing, and when to ask the user (phone, money, secrets) |

---

## MCP

**Status:** ⚠️ Not yet published — the agent uses the REST API directly with `curl`.

| Detail | Value |
|---|---|
| **Primary interface** | REST API over HTTPS + SSH |
| **Transport** | HTTPS (JSON) |
| **Compatible Clients** | Any agent with shell / HTTP access (Claude Code, Cursor, Codex, …) |

---

## What It Does

The Vibe Hosting gives an AI coding agent a real root Ubuntu server, isolated in a gVisor sandbox, on a live HTTPS subdomain (or on the user's own domain — point a CNAME at it and HTTPS is issued automatically) — created with a single unauthenticated `POST /create`. There is no signup form, dashboard or payment method in the agent's path: the first call mints the account credential (`api_key`) together with the server, and the agent then deploys over SSH, publishes on port 80 (or a static `/root/www`), and manages the server through the same API.

Servers scale to zero when idle and wake on the next HTTP request or SSH connection, so an agent can keep long-lived projects (web apps, bots, workers, MCP servers) without a human managing them. Usage is billed from a prepaid credit with a monthly free allowance; the service itself is closed-source.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "This is **documentation for an LLM agent**" and "The simplest hosting for LLM agents. **One HTTP call gives you a real root Linux server on a live HTTPS subdomain, in seconds.**" (https://thevibehosting.com/SKILL.md); homepage: "no signup · no key · no MCP" and "Say this to your agent — that's your whole involvement" (https://thevibehosting.com) |
| **Agent-specific primitive** | Account-on-first-call (the first `POST /create` provisions a server and mints the `api_key`, no human signup), a versioned agent-addressed onboarding document (`SKILL.md`), wake-on-connect server lifecycle, and `POST /feedback` for agents to report friction |
| **Autonomy-compatible control plane** | Create → deploy → publish → manage needs no human click; constraints are a hard prepaid-credit cap (servers pause at zero), per-server RAM ceilings, per-IP limits for anonymous accounts, and gVisor isolation per server |
| **M2M integration surface** | REST API (`curl`), SSH, URL onboarding (`SKILL.md`); there is no dashboard |
| **Identity / delegation** | The agent holds the account `api_key`; the human enters only through phone verification (the SMS code goes to the human, who hands it to the agent), which unlocks higher limits; usage and billing history via `GET /account/usage` and `GET /account/billing`. Honest note: several agents sharing one account share one identity |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Account-on-first-call** | `POST /create` without auth creates the account and the server and returns the `api_key` |
| **Root server on HTTPS subdomain** | Full Ubuntu in a gVisor sandbox with SSH and a live `https://<slug>.thevibehosting.com` (or your own domain via CNAME, HTTPS included) |
| **Wake-on-connect lifecycle** | Idle servers sleep (RAM freed) and wake on the next HTTP request or SSH connection; `POST /servers/{id}/sleep` / `wake` / `never-sleep` |
| **Prepaid credit cap** | One USD balance with a monthly free floor; `GET /account/billing` shows balance, burn rate and runway |
| **Own domain with HTTPS** | `POST /servers/{id}/domain` returns the exact DNS records: a CNAME to the server's slug (A record for an apex); once DNS points at it the domain goes live with an auto-issued certificate, no redirect (verified accounts) |
| **Exposed ports** | `POST /servers/{id}/expose` publishes a raw TCP/UDP port for non-HTTP services |
| **Agent feedback channel** | `POST /feedback` for the agent to report friction or missing features |

---

## Autonomy Model

1. The user tells the agent: "Read https://thevibehosting.com/SKILL.md and follow the instructions."
2. The agent calls `POST /create` and stores the returned `api_key` and SSH key where the user keeps the project.
3. The agent uploads the project over SSH/rsync and starts it with `/root/run.sh` (or serves static files from `/root/www`).
4. The app is live on its HTTPS subdomain; the agent verifies it and reports the URL.
5. Later sessions reuse the `api_key` to redeploy, sleep/wake, expose ports or check billing — all without a human click.
6. Only actions that involve the user's phone or money (verification, top-up) go back to the human.

---

## Identity and Delegation Model

- The account `api_key` is the agent's credential, minted on its first call; `SKILL.md` tells the agent where to persist it.
- The human delegates higher limits (always-on servers, bigger RAM, custom domains, unlimited servers) by verifying a phone number; the SMS code is relayed by the human to the agent.
- Spending authority is bounded by prepaid credit; servers pause when it runs out.
- `GET /account/usage` (hourly per-server history) and `GET /account/billing` provide an audit trail of what the account consumed.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | `POST /create`, `GET/DELETE /servers/{id}`, `/sleep`, `/wake`, `/never-sleep`, `/expose`, `/ssh-key`, `/subdomain`, `/domain`, `GET /account/billing`, `GET /account/usage`, `POST /feedback` — reference at https://thevibehosting.com/api |
| SSH | Root access to each server for deployment and operations |
| URL onboarding | https://thevibehosting.com/SKILL.md |

---

## Human-in-the-Loop Support

Built into the onboarding contract rather than the API: `SKILL.md` instructs the agent to ask the user before anything involving their phone number, money or secrets (phone verification, top-ups, uploading `.env` files), and to send feedback only with the user's consent. Everything else runs without human confirmation.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **DigitalOcean / Render / Fly.io** | A human must create an account, add a payment method and generate an API token in a dashboard before an agent can do anything |
| **Generic VPS providers** | Human signup, manual SSH key setup and no agent-addressed onboarding document |
| **Code-execution sandboxes (ephemeral)** | Optimised for short-lived code runs; no persistent public HTTPS app hosting with wake-on-connect |

---

## Use Cases

- **Deploying vibe-coded apps** — the agent puts a project live on HTTPS from one prompt, on a subdomain or the user's own domain.
- **Hosting agent-built bots and workers** — Discord/Telegram bots, cron jobs and background workers that persist across sessions.
- **Remote MCP servers** — an agent builds an MCP server and hosts it on its own HTTPS endpoint.
- **Long-lived agent sandboxes** — a persistent root Linux box the agent returns to across sessions, asleep when unused.
