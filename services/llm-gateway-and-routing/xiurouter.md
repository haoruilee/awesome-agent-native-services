# XiuRouter

> **"Claude, GPT, Gemini, and more through one API"**

| | |
|---|---|
| **Website** | https://router.xiu.ai/en |
| **Docs** | https://docs.xiu.ai/en/router/ |
| **GitHub** | Not published (hosted service) |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |
| **Operator** | XiuLab Inc, a U.S. corporation |
| **Contact** | contact@xiu.ai |

---

## Official Website

https://router.xiu.ai/en

The savings statement applies to selected models and service tiers versus displayed provider reference prices. The live [pricing page](https://router.xiu.ai/en/pricing) is the source for current rates.

---

## Official Repo

No public product repository is published. XiuRouter is a hosted commercial service with public product and protocol documentation.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** scoped API key + the native protocol used by the agent client.

1. An operator signs in, adds account credit, and creates a dedicated API key with the required model and service-tier scope.
2. The agent or client lists the models visible to that key:

```bash
export XIUROUTER_API_KEY=...

curl https://router-api.xiu.ai/v1/models \
  -H "Authorization: Bearer $XIUROUTER_API_KEY"
```

3. Point the client at the protocol-specific base URL and verify a small real request in XiuRouter usage records.

Start with the [Agent integrations workspace](https://router.xiu.ai/en/integrations) or the [Router quickstart](https://docs.xiu.ai/en/router/quickstart/).

---

## Agent Skills

**Status:** ⚠️ No official XiuRouter Agent Skill is published.

```bash
npx clawhub@latest search xiurouter
```

The official integration workspace currently provides client-specific setup instructions rather than an installable `SKILL.md`.

---

## MCP

**Status:** ⚠️ No official XiuRouter MCP server is published.

XiuRouter is the model transport used by agent clients. It does not present model calls as MCP tools.

---

## What It Does

XiuRouter is a hosted model API for developers and AI agents. One account and scoped API key can call models through OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, or Gemini GenerateContent. The public Agent integrations workspace documents protocol-aware setup and replacement paths for 14 supported clients, including Codex, Claude Code, Cursor, Cline, Continue, OpenClaw, Hermes Agent, Aider, Open WebUI, LibreChat, and Vercel AI SDK.

The control boundary is intentionally narrower than a full agent identity platform. XiuRouter provides constrained keys and request-level usage records, but it does not claim persistent cross-service agent identity, delegated user authorization, automatic provider fallback, or trajectory-level tracing.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The dedicated [Agent integrations workspace](https://router.xiu.ai/en/integrations) provides setup, replacement, rollback, and real-request verification for 14 agent and developer clients. The underlying API also serves ordinary applications; the admitted fit is the agent operations surface rather than a claim that every API call is agent-specific. |
| **Agent-specific primitive** | Protocol-aware setup identifies the wire format each client actually sends, keeps credentials out of agent conversations, preserves the previous provider as a rollback point, and verifies the configured key, model, path, and usage record with a small real task. |
| **Autonomy-compatible control plane** | After an operator provisions the account and dedicated key, the agent makes model calls without per-request human confirmation. Key quota, model scope, service-tier scope, expiration, and optional IP restrictions constrain that loop. |
| **M2M integration surface** | Public REST routes for OpenAI Responses, OpenAI Chat Completions, Anthropic Messages, Gemini GenerateContent, and model discovery. |
| **Identity / delegation** | A dedicated API key is the attributable runtime identity. Usage records show key-scoped request status, model, service tier, token usage, latency, and settlement. This is not a KYA credential or delegated user-authorization protocol. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Protocol-aware client setup** | Uses the actual Responses, Chat Completions, Messages, or Gemini wire protocol instead of treating every agent as generic OpenAI-compatible. |
| **Scoped API key** | Restricts callable models, service tiers, quota, expiration, and optional source IPs. |
| **Native protocol routes** | Preserves the request format expected by OpenAI, Anthropic, and Gemini clients. |
| **Request usage record** | Records status, model, service tier, tokens, latency, and settlement for the real request made by the configured client. |
| **Provider replacement path** | Separates first-time setup from replacing an existing provider and keeps the previous configuration available for rollback. |
| **Public pricing reference** | Shows current per-model and per-service-tier prices before a request is sent. |

---

## Autonomy Model

1. An operator creates a dedicated XiuRouter key and limits its quota, models, service tiers, expiration, and optional IP range.
2. The operator configures the agent client with the native base URL, key, and model ID documented for that client.
3. The agent sends normal model requests without a human approving each call.
4. XiuRouter authenticates the key, checks its scope and balance boundary, and sends the request through the selected model and service tier.
5. The response returns through the client's native protocol.
6. The operator can audit the real request in usage records and revoke or narrow the key when necessary.

Account funding, initial key creation, and client configuration remain human-controlled setup steps.

---

## Identity and Delegation Model

- A dedicated API key identifies one client or agent deployment at the XiuRouter boundary.
- Model, service-tier, quota, expiration, and optional IP restrictions define what that key may call.
- Usage records attribute status, model, service tier, tokens, latency, and settlement to the request made with that key.
- Upstream provider credentials are not placed in the agent client.
- XiuRouter does not currently mint a persistent cross-service agent identity, KYA token, or delegated user authorization grant.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| `GET /v1/models` | Lists models visible to the current API key. |
| `POST /v1/chat/completions` | OpenAI Chat Completions route. |
| `POST /v1/responses` | OpenAI Responses route for Codex and Responses clients. |
| `POST /v1/messages` | Anthropic Messages route for Claude Code and Anthropic SDKs. |
| `POST /v1beta/models/{model}:generateContent` | Gemini GenerateContent route. |
| Agent integrations | Client-specific setup, replacement, rollback, and real-request verification for 14 apps. |

OpenAI-style clients use `https://router-api.xiu.ai/v1`; Messages and Gemini clients use the API root when they append their own route.

---

## Human-in-the-Loop Support

Humans control account funding, key creation, client configuration, and later review or revocation. The runtime model call path does not require per-request approval. XiuRouter does not provide a separate approval inbox or human-escalation primitive.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Separate provider keys** | Requires independent credentials, billing, model IDs, and client configuration for each provider, with no shared key scope or usage ledger. |
| **Generic OpenAI-compatible base URL** | Does not cover clients that actually send OpenAI Responses, Anthropic Messages, or Gemini GenerateContent, and provides no protocol-specific replacement or rollback guidance. |
| **Plain reverse proxy** | Does not provide model/service-tier key restrictions, public reference pricing, or request usage records tied to the configured client. |

---

## Use Cases

- **Coding agents** — configure Codex, Claude Code, Cursor, Cline, Continue, or Aider with the protocol each client actually sends.
- **Constrained agent deployments** — issue a dedicated key limited by model, service tier, quota, expiration, and optional IP range.
- **Multi-protocol applications** — use Responses, Chat Completions, Messages, and Gemini routes through one account.
- **Request verification** — compare a small real agent task with the corresponding usage record, token count, latency, status, and settlement.
