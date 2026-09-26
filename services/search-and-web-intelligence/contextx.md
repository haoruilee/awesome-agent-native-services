# contextX

> **"contextX is a remote MCP server that provides normal search powered by Grok 4.3 and deep search powered by Grok 4.20 Multi-Agent 0309."**

| | |
|---|---|
| **Website** | https://github.com/KayanoLiam/ContextX |
| **Docs** | https://github.com/KayanoLiam/ContextX/blob/main/README.en.md |
| **GitHub** | https://github.com/KayanoLiam/ContextX |
| **Public MCP** | `https://mcp.twitter.monster/mcp` |
| **Latest-month signal** | Still no GitHub release and still no `LICENSE` file; 175 stars; last push 2026-09-09. README still documents the public MCP at [mcp.twitter.monster/mcp](https://mcp.twitter.monster/mcp), which on 2026-09-26 answered HTTP 406 until the client accepted both `application/json` and `text/event-stream` ([repo metadata](https://api.github.com/repos/KayanoLiam/ContextX)) |
| **Verified at** | 2026-09-26 |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |
| **License** | ⚠️ No repository license detected as of 2026-09-26 ([GitHub metadata](https://api.github.com/repos/KayanoLiam/ContextX)) |

---

## Official Website

No separate website is published. The official repository is the canonical project page, and its README publishes the remote endpoint:

https://github.com/KayanoLiam/ContextX

---

## Official Repo

https://github.com/KayanoLiam/ContextX

---

## How to Use (Agent Onboarding)

**Interaction pattern:** remote MCP over Streamable HTTP

No binary, account, or API key is required for the public endpoint. Claude Code has a one-command setup:

```bash
claude mcp add --transport http contextX https://mcp.twitter.monster/mcp
```

For Cursor or another Streamable HTTP MCP client, register the URL directly:

```json
{
  "mcpServers": {
    "contextX": {
      "url": "https://mcp.twitter.monster/mcp"
    }
  }
}
```

Then ask the agent to use `grok_search`, or explicitly request deep search so it selects `grok_deep_search`. See the official [client setup](https://github.com/KayanoLiam/ContextX/blob/main/README.en.md#adding-to-mcp-clients).

---

## Agent Skills

**Status:** ⚠️ Not yet published — the repository provides MCP instructions, but no `SKILL.md` package.

```bash
npx clawhub@latest search contextx web-search
```

For faster access in China, use `CLAWHUB_REGISTRY=https://cn.clawhub-mirror.com` or pass `--registry https://cn.clawhub-mirror.com`.

See https://agentskills.io/specification to contribute one.

---

## MCP

**Status:** ✅ Available — public remote server

| Detail | Value |
|---|---|
| **Endpoint** | `https://mcp.twitter.monster/mcp` |
| **Transport** | Streamable HTTP |
| **Authentication** | None; no headers, tokens, or API keys required |
| **Tools** | `grok_search`, `grok_deep_search` |
| **Clients documented upstream** | Pi Agent (through `pi-mcp-adapter`), Claude Code, Cursor, and other Streamable HTTP clients |
| **Suggested deep-search timeout** | `360000` ms in the upstream Pi example |

---

## What It Does

contextX turns two hosted search modes into MCP tools. `grok_search` handles fast everyday retrieval, while `grok_deep_search` uses a multi-agent deep-search model for slower, broader investigation and cross-referencing. The server forwards MCP queries to OpenAI-compatible Responses API upstreams and continuously consumes their stream before returning the generated content as the MCP tool result, reducing long-search gateway timeout risk.

The public endpoint fixes the upstream models and requires no caller credential. Operators who need their own keys or endpoint policy can self-host the Rust server by supplying normal- and deep-search Responses API URLs and bearer tokens through environment variables.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | The official README defines contextX as a *"remote MCP server"* and documents direct setup for Pi Agent, Claude Code, Cursor, and other MCP clients — [source](https://github.com/KayanoLiam/ContextX/blob/main/README.en.md) |
| **Agent-specific primitive** | Two tool-level search actions let an agent choose between a fast search and a long-running multi-agent deep search; results return through the MCP tool-result contract rather than a human SERP |
| **Autonomy-compatible control plane** | After one-time MCP registration, an agent can call either tool without an account, API key, model selection, or per-search human confirmation; the upstream README states that the public tools require no authentication and have no rate limits ([source](https://github.com/KayanoLiam/ContextX/blob/main/README.en.md#mcp-tools)) |
| **M2M integration surface** | Remote Streamable HTTP MCP is the primary and only public interaction surface; a self-hosted Rust server exposes `/mcp` and `/health` ([source](https://github.com/KayanoLiam/ContextX/blob/main/README.en.md#self-hosting)) |
| **Identity / delegation** | **Not applicable to external-action delegation:** these tools perform read-only search and do not act as a user. The public endpoint intentionally has no auth, so it also provides no per-agent identity, delegated scopes, or caller-attributed audit trail; operators needing attribution must self-host behind their own gateway |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **`grok_search`** | Fast normal search for everyday questions and simple retrieval; accepts a `query` string |
| **`grok_deep_search`** | Longer multi-agent research for detailed investigation and cross-source comparison; accepts a `query` string |
| **Stream-draining proxy** | Continuously receives the upstream Responses API stream before returning the MCP tool result, reducing idle gateway timeouts |
| **Fixed model routing** | Public users select a search mode, not arbitrary models or upstream configuration |
| **Self-hosted upstream split** | Separate URL/key pairs for normal and deep Responses API backends |

---

## Autonomy Model

```text
Operator registers the public Streamable HTTP MCP URL once
    ↓
Agent discovers grok_search and grok_deep_search
    ↓
Agent chooses fast or deep mode from task complexity
    ↓
contextX streams from its fixed upstream Responses API
    ↓
Generated search content returns as the MCP tool result
    ↓
Agent continues its research loop without a login or per-query approval
```

---

## Identity and Delegation Model

- **Read-only boundary** — contextX searches and returns generated content; it does not send messages, modify accounts, purchase items, or otherwise act on behalf of a user.
- **No public caller identity** — The official endpoint accepts no authentication headers or tokens, so requests are not exposed as named agent principals.
- **No delegated scopes** — There is no per-agent permission or quota model in the published service.
- **No caller audit contract** — The repository does not document per-agent request logs or durable trace IDs for the public endpoint.
- **Self-hosting option** — An operator can place the Rust server behind an authenticated proxy and control upstream keys, but those identity controls are deployment-provided rather than contextX primitives.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| **Remote MCP** | Streamable HTTP at `https://mcp.twitter.monster/mcp` |
| **MCP tools** | `grok_search({query})`, `grok_deep_search({query})` |
| **Health endpoint** | `/health` on a self-hosted instance |
| **Upstream protocol** | OpenAI-compatible Responses API with streaming, configured independently for normal and deep search |
| **Self-hosted runtime** | Rust server started with `cargo run`; default MCP listener `127.0.0.1:3000/mcp` |

---

## Human-in-the-Loop Support

No human is required during search. A user may explicitly request deep search, but the agent can select either MCP tool itself. contextX provides no approval workflow, result-review queue, source-verification gate, or per-query access policy; callers must evaluate generated claims and citations in their own agent workflow.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Human search-engine page** | Returns a visual SERP/HTML and requires browser operation and parsing instead of one MCP tool result |
| **Raw Responses API integration** | Requires the agent developer to own credentials, streaming, timeout handling, tool schemas, and fast/deep routing |
| **Single-mode MCP search wrapper** | Does not expose a distinct long-running multi-agent research primitive alongside fast retrieval |

---

## Use Cases

- **Coding-agent fact checks** — Fetch a current version, API change, or error explanation without leaving the MCP loop
- **Deep technical comparisons** — Ask the multi-agent search mode to investigate and cross-reference several approaches
- **Zero-key agent prototypes** — Add web intelligence to a local MCP client without provisioning a search API account
- **Self-hosted search routing** — Put normal and deep Responses API providers behind one fixed MCP tool contract

> **Current caveats (2026-09-26):** contextX has no GitHub release, no detected repository license, no public authentication, and no documented service-level guarantees. Review those constraints before production or commercial use.
