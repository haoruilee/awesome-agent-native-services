# Agentik

> **"The tool gateway for your agents."**

| | |
|---|---|
| **Website** | https://www.agentik.cc |
| **Docs** | https://www.agentik.cc/docs |
| **GitHub** | https://github.com/agent-tool-router/agentik |
| **License** | MIT for the SDK, CLI, and Claude Code plugin. The hosted service is closed-source |
| **Classification** | `agent-native` |
| **Category** | [Tool Access & Integration Services](README.md) |
| **Operator** | BURIZA, named on https://www.agentik.cc/about.md |
| **Interest disclosure** | [Issue #307](https://github.com/haoruilee/awesome-agent-native-services/issues/307) was opened by gaultier-1337, who disclosed that they make Agentik and have a financial interest in it. No payment was asked or offered for the listing |
| **Latest-month signal** | Checked 2026-11-24: [index.md](https://www.agentik.cc/index.md) HTTP 200, “The tool gateway for your agents.” and “3,539 tools from 165 providers.”; [docs](https://www.agentik.cc/docs) HTTP 200; [SKILL.md](https://www.agentik.cc/SKILL.md), [llms.txt](https://www.agentik.cc/llms.txt), [pricing.md](https://www.agentik.cc/pricing.md), and [connect.md](https://www.agentik.cc/connect.md) HTTP 200; [OpenAPI](https://api.agentik.cc/openapi/agent.json) HTTP 200, Agentik agent API 0.1.0; public MCP `https://ai.agentik.cc/mcp/public` `initialize` HTTP 200, `serverInfo` name `agentik` version `0.0.2`; `tools/list` returns `discover_tools` and `inspect_tool`; `POST https://ai.agentik.cc/mcp` `initialize` HTTP 401, message expects OAuth or `Authorization: Bearer trk_...`; `POST https://api.agentik.cc/v1/discover` HTTP 200; [agent-tool-router/agentik](https://github.com/agent-tool-router/agentik) SPDX MIT, 0 stars, last push 2026-11-04; npm `@get-agentik/cli` and `@get-agentik/sdk` 0.1.0, license MIT |
| **Verified at** | 2026-11-24 |

---

## Official Website

https://www.agentik.cc

The markdown homepage (HTTP 200 at https://www.agentik.cc/index.md on 2026-11-24) opens with “The tool gateway for your agents.” and states that Agentik connects Claude, ChatGPT, Codex, and Cursor to tools through one MCP connection, with each call charged at the provider's price. The same page says “3,539 tools from 165 providers.”

---

## Official Repo

https://github.com/agent-tool-router/agentik

The CLI, TypeScript SDK, and Claude Code plugin are in this MIT repository. The repository description calls it the Claude Code plugin, CLI, and TypeScript SDK for Agentik. Its README says the hosted catalog, billing, and provider accounts stay at https://www.agentik.cc. Checked 2026-11-24: SPDX MIT, 0 stars, last push 2026-11-04. npm publishes `@get-agentik/cli` and `@get-agentik/sdk` at 0.1.0, both MIT.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** MCP. A person must approve OAuth or create an API key, and add prepaid credit before a paid run.

**One-sentence instruction:** Connect the authenticated MCP server, then have a person approve access and top up the workspace.

```bash
npx @get-agentik/cli connect <client>
```

`connect` prints setup for Claude Desktop, ChatGPT, Codex, Cursor, Hermes, Claude Code, and other Streamable HTTP clients. The authenticated server is `https://ai.agentik.cc/mcp`. Public discovery is a separate read-only server and cannot replace it:

```bash
claude mcp add --transport http agentik-catalog https://ai.agentik.cc/mcp/public
```

Execution uses the authenticated endpoint. The person finishes OAuth in the browser, or sets `AGENTIK_API_KEY` in the environment that launches the client. https://www.agentik.cc/connect.md says: “Agentik creates a workspace when requested and a dedicated execution key with the approved permissions.” The same page says never to ask for a key in chat. A paid call also needs a human top-up. Reading the site index does not create that workspace or add credit.

Developer entry point: https://www.agentik.cc/docs

---

## Agent Skills

**Status:** ✅ Available

The published skill is https://www.agentik.cc/SKILL.md (`name: agentik`). The CLI installs it, and the Claude Code plugin ships the same skill. Checked 2026-11-24: both the skill URL and the plugin repository returned HTTP 200.

```bash
npx @get-agentik/cli skill --install
```

```text
/plugin marketplace add agent-tool-router/agentik
/plugin install agentik@agentik
```

| Skill | What It Teaches the Agent |
|---|---|
| `agentik` | Discover a tool, inspect its schema and price, run it with an idempotency key, follow a `RUNNING` job with `get_run`, and reuse a saved Play. Tells the agent to read `AGENTIK_API_KEY` from the environment and to hand a `topup_url` to a person. |

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Public endpoint** | `https://ai.agentik.cc/mcp/public` |
| **Authenticated endpoint** | `https://ai.agentik.cc/mcp` |
| **Transport** | Remote Streamable HTTP |
| **Server** | `agentik` 0.0.2. Checked 2026-11-24 |
| **Public tools** | `tools/list` returned `discover_tools` and `inspect_tool`. Both are documented as free and non-executing |
| **Authenticated tools** | `SKILL.md` and the quickstart name `run_tool`, `get_run`, `get_account`, and `prepare_topup`. Plays are `list_plays`, `get_play`, `save_play`, and `record_play_run`. Those calls were not on the public tool list |
| **Auth** | None on `/mcp/public`. On `/mcp`, unauthenticated `initialize` returned HTTP 401. `WWW-Authenticate` points at the OAuth protected-resource metadata. The body says to authorize through OAuth or send `Authorization: Bearer trk_...` |
| **Repo** | https://github.com/agent-tool-router/agentik (MIT). The hosted MCP server source is not in that repository |
| **Compatible Clients** | Claude, ChatGPT, Codex, Cursor, Hermes, and other remote-HTTP MCP clients, per https://www.agentik.cc/connect.md |

---

## What It Does

Agentik is a hosted tool gateway. An agent discovers third-party data and media tools, reads the input schema and the price, then runs the chosen tool against one prepaid workspace balance. The markdown homepage describes one MCP connection for Claude, ChatGPT, Codex, and Cursor, charged at the provider's price. On 2026-11-24 that page listed 3,539 tools from 165 providers.

Discovery and inspection are public. `POST https://api.agentik.cc/v1/discover` returned HTTP 200 on 2026-11-24 for a catalog search and did not call a provider. Running a tool, including a zero-price tool, needs an authorised workspace. The OpenAPI summary is: “Pay-per-call tools for AI agents: one API key, one prepaid balance, many providers.”

The open-source pieces are the CLI, the TypeScript SDK, and the Claude Code plugin. The hosted catalog and billing stay closed.

The published skill also covers the user's own ad and analytics accounts, and webhooks the user creates for Slack, Discord, Zapier, Make, n8n, or Pipedream. Agentik's own comparison says it does not sign in to mail, chat, or CRM apps. Composio and Arcade, already in this category, are the listings for that job.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: “The tool gateway for your agents.” `llms.txt`: “Agentik connects agents to third-party tools through MCP and REST, with public discovery, explicit tool contracts and an authorised prepaid workspace for execution.” https://www.agentik.cc/index.md and https://www.agentik.cc/llms.txt |
| **Agent-specific primitive** | Discover, then inspect, then run. `inspect_tool` returns the input schema, the price, and what a call can reserve before anything runs. `run_tool` takes an idempotency key so a retry does not run twice. A long job returns a run ID for `get_run`. Plays save a multi-step job for later replay. https://www.agentik.cc/SKILL.md |
| **Autonomy-compatible control plane** | After a person has funded a workspace and approved a key, the agent runs the loop without a click per call. Keys can carry hourly, daily, lifetime, and per-tool spending caps. When credit runs out, the error carries a `topup_url` only a person can complete. Tools marked actual-cost bill the provider receipt and cannot run on a capped key. https://www.agentik.cc/pricing.md |
| **M2M integration surface** | Authenticated and public remote MCP, OpenAPI 0.1.0 at https://api.agentik.cc/openapi/agent.json, `npx @get-agentik/cli`, `npm install @get-agentik/sdk`, and the `agentik` skill |
| **Identity / delegation** | OAuth “creates a workspace when requested and a dedicated execution key with the approved permissions.” Each API key is its own credential, separate from the human login, and can carry its own caps and allowed tools. Every paid call has a run ID and a reservation that `get_run` can read back. https://www.agentik.cc/connect.md and https://www.agentik.cc/docs/authentication.md |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **discover_tools** | Natural-language catalog search. Free. Public MCP `tools/list` included it on 2026-11-24. REST: `POST /v1/discover`, HTTP 200 without a key |
| **inspect_tool** | Input schema, price, and reservation limit for one tool, before a run. Free. Public MCP included it on 2026-11-24. REST: `GET /v1/tools/{provider}/{tool}` |
| **run_tool** | Executes one tool with an idempotency key. Needs a workspace key. REST: `POST /v1/run`. A paid run reserves its quoted maximum first |
| **get_run** | Reads a run ID, including a job that came back `RUNNING`, instead of starting it again. REST: `GET /v1/runs/{id}` |
| **Plays** | `list_plays`, `get_play`, `save_play`, and `record_play_run`. Documented in `SKILL.md` as saved multi-step jobs. The skill says these calls are free and run nothing. They were not on the public tool list |
| **Capped execution key** | OAuth mints a dedicated execution key, or a person creates one. Optional hourly, daily, lifetime, and per-tool caps. Capped keys cannot run actual-cost tools |

---

## Autonomy Model

1. The agent connects to `https://ai.agentik.cc/mcp/public` or calls `POST https://api.agentik.cc/v1/discover`.
2. It inspects one exact tool and reads the schema, price, and reservation before choosing inputs.
3. A person approves OAuth or creates an API key, and completes a top-up. `prepare_topup` only prepares a human review link. It does not charge a card.
4. The agent calls `run_tool` with an idempotency key. A retry of the same intention reuses that key.
5. If the run is `RUNNING`, the agent polls `get_run`. It does not start a second paid run.
6. If the balance is gone, the agent shows the `topup_url` to a person and stops. Pricing says there is no crypto and no wallet: money comes in through a human on a top-up page, and the agent spends a balance.

---

## Identity and Delegation Model

- Human account: sign-in and the top-up page stay with a person. https://www.agentik.cc/about.md names the publisher as BURIZA.
- OAuth: the person approves access at the signed-in account. Agentik creates a dedicated execution key with the approved permissions. The client receives scoped tokens through PKCE. https://www.agentik.cc/connect.md
- API key: `Authorization: Bearer` with a `trk_` key, or `AGENTIK_API_KEY` in the client environment. New keys have no optional spending caps until someone sets them. https://www.agentik.cc/docs/authentication.md
- Caps and allowlists: hourly, daily, lifetime, and per-tool caps, plus an allowed-tool list per key. https://www.agentik.cc/pricing.md
- Audit: each paid execution has a run ID, a reservation, and a settled charge readable with `get_run`. The skill says Agentik stores billing and execution metadata, not the contents of inputs and outputs.
- Public tier: anonymous discovery and inspection only. It is not an execution identity.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| Remote MCP | `https://ai.agentik.cc/mcp` (OAuth or `trk_` bearer); `https://ai.agentik.cc/mcp/public` (no key, discover and inspect only) |
| REST / OpenAPI | https://api.agentik.cc/openapi/agent.json version 0.1.0, title “Agentik agent API”. Customer paths include `/v1/discover`, `/v1/tools/{provider}/{tool}`, `/v1/run`, `/v1/runs/{id}`, `/v1/wallet/balance`, and `/v1/topups` |
| CLI | `npx @get-agentik/cli` 0.1.0 (MIT). `connect <client>`, `skill --install` |
| SDK | `npm install @get-agentik/sdk` 0.1.0 (MIT). TypeScript client with OpenAI, Anthropic, and AI SDK adapters |
| Agent Skill | https://www.agentik.cc/SKILL.md and `npx @get-agentik/cli skill --install` |
| Docs | https://www.agentik.cc/docs |

---

## Human-in-the-Loop Support

A person is required to create the workspace, approve OAuth or mint a key, and pay the top-up. Checkout shows the total before confirmation. The published fee on a credit purchase is 5.5%, with a minimum fee of $0.80 and a minimum credit purchase of $5.00. The first successful top-up of $10 or less has no platform fee. Tool calls themselves have no markup. https://www.agentik.cc/pricing.md

After that, ordinary discover, inspect, and run calls do not ask for another click. The agent must stop for a new top-up, for a cap that blocks an actual-cost tool, and for any ad-account or webhook setup the person has not already approved. The skill tells the agent to state the expected total before a loop over many inputs.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **One human account, card, and API key per provider** | Each provider's billing belongs to a person, and the agent does not get a price and a reservation before the call. Agentik gives one connection, a public inspect step, and a capped workspace key |
| **A human API marketplace** | Built for a developer to pick an API and paste a key. It does not give the agent `discover_tools` / `inspect_tool` with a maximum reservation, an idempotency key, and a run ID the agent can poll |
| **Acting inside the user's own mail, chat, or CRM** | That is a different job. Agentik's comparison says it does not sign in to those apps. Composio and Arcade in this category are the listings for delegated access to apps the person already uses |

---

## Use Cases

- **Priced data calls** — inspect an SEO, search, or media tool, show the reservation, then run it once on the workspace balance.
- **Safe retries** — reuse the idempotency key after a dropped connection, and poll `get_run` when the first response is `RUNNING`.
- **Catalog browsing without a key** — use the public MCP to choose a tool before anyone creates a workspace.
- **Saved multi-step jobs** — list Plays before rebuilding a job that already worked, then record the new run.
