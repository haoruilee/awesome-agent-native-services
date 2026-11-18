# SpecStream

> **"The live web data engine for teams and agents."**

| | |
|---|---|
| **Website** | https://specstream.ai |
| **Docs** | https://specstream.ai/agents.md · https://specstream.ai/llms.txt · https://specstream.ai/docs/sdk |
| **GitHub** | https://github.com/specstream/specstream-tools |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |
| **Interest disclosure** | Operator-submitted: the proposer works on SpecStream |

---

## Official Website

https://specstream.ai

Tagline, read 2026-11-18 from [llms.txt](https://specstream.ai/llms.txt): "SpecStream is the live web data engine for teams and agents."

---

## Official Repo

https://github.com/specstream/specstream-tools

The public repository for what is installed around the hosted service: MCP client setup, agent plugins, the SDKs and examples. The service itself is hosted at specstream.ai and has no public source. The official packages, documented at https://specstream.ai/docs/sdk, are `specstream-client` (Python, `pip install specstream-client`) and `@specstream/sdk` (TypeScript, `npm install @specstream/sdk`).

---

## ⭐ How to Use (Agent Onboarding)

**Interaction pattern:** URL Onboarding

**One-sentence instruction:**

```
Read https://specstream.ai/agents.md and follow the instructions.
```

What the agent finds there, checked live on 2026-11-18:

- **Pay per call, no account.** An unauthenticated `GET https://api.specstream.ai/v1/web-search?q=...` returns HTTP 402 with x402 terms in the `PAYMENT-REQUIRED` header. `GET https://api.specstream.ai/v1/agent/lists` returns the pay-per-request steps as JSON, and https://api.specstream.ai/.well-known/x402 lists the x402 calls.
- **Agent sign-up.** Following https://specstream.ai/auth.md, the agent posts the person's email address to `POST /v1/agent/signup`, asks the person for the 6-digit code from that email, and sends it to `POST /v1/agent/signup/verify`, which returns an API key.
- **MCP on the person's account.** `https://api.specstream.ai/mcp` (Streamable HTTP) answers an unauthenticated `initialize` with HTTP 401. It is not keyless: it needs a SpecStream API key as a Bearer token or an OAuth token.

---

## Agent Skills

**Status:** ⚠️ Not yet published

Search community skills: `npx clawhub@latest search specstream`. For faster access in China, use the official ClawHub mirror: set `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or `--registry https://cn.clawhub-mirror.com` — [mirror-cn.clawhub.com](https://mirror-cn.clawhub.com).

See: https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/specstream/specstream-tools |
| **Endpoint** | `https://api.specstream.ai/mcp` |
| **Transport** | Streamable HTTP |
| **Authentication** | OAuth, or a SpecStream API key as a Bearer token (unauthenticated `initialize` returns 401) |
| **Compatible Clients** | Any MCP client; setup guides at https://specstream.ai/docs/mcp/clients |

---

## What It Does

SpecStream finds data on the live web and returns each value with its source URL and read time. It has three products: the Search API (`GET /v1/web-search`), the Extract API (`POST /v1/extract`), and Deep Search, which turns a request in plain words into structured rows.

Agents use it through the REST API, the hosted MCP server, an A2A endpoint, or the Python and TypeScript SDKs. A client written for another search API can move to SpecStream by changing its base address and key (drop-in routes).

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "You're an agent, and someone needs data [...] SpecStream finds it on the live web and returns each value with its source URL and read time." ([agents.md](https://specstream.ai/agents.md)). Tagline: "The live web data engine for teams and agents." ([llms.txt](https://specstream.ai/llms.txt)) |
| **Agent-specific primitive** | Quotes before work: "`quote_capacity_work`: get a quote for that exact request. Quotes last 30 minutes." and "Ask your person to approve the maximum, unless they've delegated it to you explicitly." ([agents.md](https://specstream.ai/agents.md)) |
| **Autonomy-compatible control plane** | Payments with no account: "Buy one list with a machine payment: no account and no key." with MPP or x402, and "One search or one page read can be bought the same way, one call at a time, with x402's `exact` scheme" ([agents.md](https://specstream.ai/agents.md)). Spending limits: "On an account, stay inside the key's limits: total, per run, monthly, and the operations it allows." ([agents.md](https://specstream.ai/agents.md)) |
| **M2M integration surface** | REST API, MCP at `https://api.specstream.ai/mcp`, A2A at `https://api.specstream.ai/a2a`, x402 discovery at https://api.specstream.ai/.well-known/x402, SDKs `specstream-client` and `@specstream/sdk` ([agents.md](https://specstream.ai/agents.md), [docs/sdk](https://specstream.ai/docs/sdk)) |
| **Identity / delegation** | Agent sign-up: "You can open your person's account and get an API key with no form, no browser and no card" ([agents.md](https://specstream.ai/agents.md), [auth.md](https://specstream.ai/auth.md)). OAuth: "Authentication: OAuth (your client signs your person in), or their SpecStream API key as a Bearer token" ([agents.md](https://specstream.ai/agents.md)) |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Search API** | `GET /v1/web-search`: answers a question from the live web; each source carries `read_at`. |
| **Extract API** | `POST /v1/extract`: the text of the pages asked for. |
| **Deep Search** | `compile`, `quote_capacity_work`, `authorize_capacity_work`: a request in plain words becomes structured rows within an approved maximum. |
| **Pay per request** | `POST /v1/agent/lists`, and Search or Extract calls without a key, answered with HTTP 402 and paid with MPP or x402. |
| **Agent sign-up** | `POST /v1/agent/signup` and `POST /v1/agent/signup/verify` mint an API key after the person shares an email code. |

---

## Autonomy Model

1. The agent reads https://specstream.ai/agents.md.
2. With no account, it calls the Search or Extract API, receives HTTP 402 with x402 terms, signs the payment, and sends the same request again.
3. Or it opens the person's account through agent sign-up (the person reads it a 6-digit email code) and calls the API or MCP with the key it receives.
4. For a list, it compiles the request, gets a quote, asks the person to approve the maximum (unless delegated), and authorizes the work with that maximum.

---

## Identity and Delegation Model

- No-account payers pay each call with x402 or MPP; no key is involved.
- API keys belong to the person's account and carry scopes and spending limits (total, per run, monthly, and the operations allowed).
- MCP clients sign the person in with OAuth or send the person's API key as a Bearer token.
- Charged calls are kept in the account's history and request log.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| HTTP API | `https://api.specstream.ai` (Search, Extract, Deep Search, research reports) |
| MCP | `https://api.specstream.ai/mcp`, Streamable HTTP, OAuth or API key |
| A2A | Agent Card at `https://api.specstream.ai/.well-known/agent-card.json` |
| x402 / MPP | `https://api.specstream.ai/.well-known/x402` |
| SDKs | `specstream-client` (Python), `@specstream/sdk` (TypeScript) |

---

## Human-in-the-Loop Support

A Deep Search run starts only after the person approves the quoted maximum, unless they have delegated it explicitly. Agent sign-up needs the person to read back the email code. Key spending limits are set by the account owner.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Consumer web search pages** | Designed for people reading a results page, with no per-call machine payment, quote, or source URL and read time on each value. |

---

## Use Cases

- **Single facts** — the Search API or the `search_web` MCP tool for one answer with its sources.
- **Page text** — the Extract API for the text of known pages.
- **Lists** — Deep Search for every match of a request as structured rows, priced before the run.
