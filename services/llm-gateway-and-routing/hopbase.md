# HopBase

> **"Built for enterprise — A stable, high-concurrency AI gateway"**

| | |
|---|---|
| **Website** | https://hop-base.com |
| **Docs** | https://hop-base.com/en/docs |
| **GitHub** | Not published (hosted service) |
| **Classification** | `agent-native` |
| **Category** | [LLM Gateway & Routing Services](README.md) |
| **Contact** | victor@hop-base.com |

---

## Official Website

https://hop-base.com

The homepage headline is enterprise-oriented and the same API also serves ordinary applications. The admitted fit is the agent operations surface described below, not a claim that every API call is agent-specific.

---

## Official Repo

No public source repository is published. HopBase is a hosted commercial service with public product and API documentation at https://hop-base.com/en/docs.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** operator-issued API key + agent integration contract + key-scoped MCP.

1. An operator creates an API key in the HopBase console. Each key belongs to one model group. The agent cannot self-register.
2. The agent reads the integration contract and discovers the models its key can call:

```
Read https://hop-base.com/llms.txt and follow the AI Integration Contract.
```

```bash
export HOPBASE_API_KEY=...

curl https://api.hop-base.com/v1/models \
  -H "Authorization: Bearer $HOPBASE_API_KEY"
```

3. Optionally connect the read-only MCP server so the agent can check its own key scope, spend cap, and usage. The MCP endpoint requires the same API key:

```bash
claude mcp add --transport http hopbase https://api.hop-base.com/mcp \
  --header "Authorization: Bearer $HOPBASE_API_KEY"
```

Start with the [AI agent integration guide](https://hop-base.com/en/docs/getting-started/ai-agent), or the client guides for [Claude Code](https://hop-base.com/en/docs/tools/claude-code) and [Codex CLI](https://hop-base.com/en/docs/tools/codex-cli).

---

## Agent Skills

**Status:** ⚠️ No `npx skills add` package is published.

The [AI agent integration guide](https://hop-base.com/en/docs/getting-started/ai-agent) offers the per-model-family integration contract as a downloadable `AGENTS.md`, a Cursor rule, or a Claude Code skill (`.claude/skills/hopbase-api/SKILL.md`). These are files an operator downloads from the docs page, not an installable skills-registry package.

```bash
npx clawhub@latest search hopbase
```

---

## MCP

**Status:** ✅ Available (hosted, read-only, API key required)

| Detail | Value |
|---|---|
| **MCP Repo** | Not published (hosted endpoint, no public source) |
| **Endpoint** | `https://api.hop-base.com/mcp` |
| **Transport** | Streamable HTTP |
| **Auth** | `Authorization: Bearer <HopBase API key>`; requests without a key return 401 |
| **Tools** | `list_models`, `get_model_limits`, `search_docs`, `get_balance`, `get_key_info`, `get_usage` |
| **Compatible Clients** | Claude Code and other clients that support Streamable HTTP MCP with a custom header |

Every tool result covers only the key in use. The MCP server does not present model calls as tools; model traffic goes through the REST routes.

---

## What It Does

HopBase is a hosted AI gateway. Through one base URL (`https://api.hop-base.com/v1`) it serves chat, image, and video models over OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, and native Gemini routes, so an agent client keeps the wire protocol it already sends. Each API key belongs to one model group and carries its own spend cap, concurrency limit, expiry, and IP rules.

For agents, HopBase publishes an AI-readable integration contract (`llms.txt` plus per-model-family contracts) and a key-scoped, read-only MCP server. Together they let a coding agent configure itself and check what its key may call, its limits, and its usage before and after it acts.

The control boundary is intentionally narrower than a full agent identity platform. HopBase provides constrained keys and request-level usage records, but it does not mint a cross-service agent identity, KYA token, or delegated user-authorization grant, and an operator must create the key in the console.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "HopBase is a high-performance, high-stability AI gateway for enterprises and agent services. … This file is an AI-readable integration contract." — [llms.txt](https://hop-base.com/llms.txt). "Choose a HopBase model family and give its focused integration contract to a coding agent." — [AI agent guide](https://hop-base.com/en/docs/getting-started/ai-agent). The homepage headline is enterprise-oriented and the API also serves ordinary applications; the admitted fit is the agent operations surface. |
| **Agent-specific primitive** | Per-model-family integration contracts written for coding agents (base URL, key group, exact model IDs, parameter bounds, async task flow, retries) that tell the agent to read the key only from `HOPBASE_API_KEY`, never ask for it in conversation, and discover callable models with `GET /v1/models` first. A key-scoped MCP server lets the agent inspect its own models, limits, spend cap, and usage. |
| **Autonomy-compatible control plane** | After an operator creates a key, the agent makes model calls with no per-request confirmation. The key constrains that loop: one model group, USD spend cap, max concurrency, expiry, IP allowlist / blocklist, and active/disabled status. Within a group, requests fail over automatically without the agent changing its config. |
| **M2M integration surface** | REST routes for OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, native Gemini, image/video task endpoints, and key-scoped model discovery; MCP over Streamable HTTP. |
| **Identity / delegation** | A dedicated API key is the attributable runtime identity at the HopBase boundary. Usage records attribute each request (model, tokens, billed cost, status) to that key, and team keys can be attributed to a member or department. This is not a KYA credential or delegated user-authorization protocol. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent integration contract** | Copy-paste, per-model-family instructions for coding agents, downloadable as `AGENTS.md`, a Cursor rule, or a Claude Code `SKILL.md`. |
| **Key-scoped MCP server** | Read-only tools (`list_models`, `get_model_limits`, `search_docs`, `get_balance`, `get_key_info`, `get_usage`) whose results cover only the key in use. |
| **Scoped API key** | One model group per key, with USD spend cap, max concurrency, expiry, IP allowlist / blocklist, and active/disabled status. |
| **Key-scoped model discovery** | `GET /v1/models` requires the key and lists only the model IDs that key can call. |
| **Native protocol routes** | Chat Completions, Responses, Anthropic Messages, and native Gemini through one base URL. |
| **Request usage record** | Per-request model, tokens, billed cost, and status attributed to the key, and optionally to a team member or department. |

---

## Autonomy Model

1. An operator creates a dedicated HopBase key in the console and sets its model group, spend cap, concurrency, expiry, and IP rules.
2. The operator gives the coding agent the integration contract (or `llms.txt`) and sets `HOPBASE_API_KEY` in the agent's environment.
3. The agent calls `GET /v1/models` (or the MCP `list_models` / `get_key_info` tools) to learn what the key may call and its limits.
4. The agent sends model requests through the route its client natively speaks, without a human approving each call.
5. HopBase authenticates the key, enforces its scope and limits, and fails over within the key's group when needed.
6. The agent can check `get_usage` / `get_balance`; the operator can audit the same requests in usage records and disable or narrow the key.

Account funding, key creation, and client configuration remain human-controlled setup steps.

---

## Identity and Delegation Model

- A dedicated API key identifies one client or agent deployment at the HopBase boundary.
- The key's model group, spend cap, concurrency limit, expiry, and IP rules define what it may do.
- Usage records attribute model, tokens, billed cost, and status to the request made with that key; team keys can be attributed to a member or department.
- `get_key_info` and `get_usage` expose the same scope to the agent itself.
- Upstream provider credentials are not placed in the agent client.
- HopBase does not mint a cross-service agent identity, KYA token, or delegated user-authorization grant; the key is an operator-issued credential.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| `GET /v1/models` | Lists only the model IDs the current key can call; 401 without a key. |
| `POST /v1/chat/completions` | OpenAI Chat Completions route. |
| `POST /v1/responses` | OpenAI Responses route for Codex and Responses clients. |
| `POST /v1/messages` | Anthropic Messages route for Claude Code and Anthropic SDKs. |
| Native Gemini | Gemini-format route for Gemini clients. |
| Image / video tasks | Task endpoints for image and video generation models. |
| MCP | `https://api.hop-base.com/mcp`, Streamable HTTP, read-only, API key required. |

Base URL: `https://api.hop-base.com/v1`. See the [docs](https://hop-base.com/en/docs) for per-route details.

---

## Human-in-the-Loop Support

Humans control account funding, key creation, client configuration, and later review or revocation. The runtime model call path does not require per-request approval. HopBase does not provide a separate approval inbox or human-escalation primitive.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Separate vendor API keys** | Separate credentials, billing, and model IDs per vendor, with no shared key scope or usage ledger. |
| **Plain OpenAI-compatible base URL** | Does not cover clients that send OpenAI Responses or Anthropic Messages, and gives the agent no key-scoped way to discover its models, limits, spend cap, or usage. |

---

## Use Cases

- **Coding agents** — point Claude Code or Codex CLI at HopBase with the protocol each client actually sends.
- **Self-configuring agents** — hand a coding agent the integration contract so it wires the base URL, model IDs, and parameter bounds without asking for the key in conversation.
- **Constrained agent deployments** — issue a dedicated key limited by model group, spend cap, concurrency, expiry, and IP rules.
- **Self-checking spend** — let the agent read its own key scope, balance, and usage over MCP before and after a task.
