# Loom

> **"Shared memory, document search and code intelligence for AI agents."**

| | |
|---|---|
| **Website** | https://clickhouse.github.io/loom/ |
| **Docs** | https://github.com/ClickHouse/loom/blob/v1.2.0/README.md |
| **GitHub** | https://github.com/ClickHouse/loom |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/ClickHouse/loom?style=social)](https://github.com/ClickHouse/loom) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **Reviewed release** | [v1.2.0](https://github.com/ClickHouse/loom/releases/tag/v1.2.0) |

---

## Official Website

https://clickhouse.github.io/loom/

---

## Official Repo

https://github.com/ClickHouse/loom

---

## How to Use (Agent Onboarding)

**Interaction pattern:** MCP Tool

Deploy a Loom server and configure providers using the [released README](https://github.com/ClickHouse/loom/blob/v1.2.0/README.md). Configure a real LLM for meaningful fact extraction; the stock fake provider is a deterministic development/test client. For a shared authenticated deployment, obtain a writer token with access to the intended namespace.

Connect a Streamable HTTP MCP client to the deployed server's `/mcp` endpoint with `Authorization: Bearer <JWT>`. The [released connection guide](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/integrations/mcp-clients.md) provides this entry shape; replace the example host and token:

```json
{
  "url": "https://loom.example.com/mcp?toolset=coding",
  "headers": { "Authorization": "Bearer <JWT>" }
}
```

On this coding toolset, call `loom_op` with `op="memory.set_from_messages"` and the extraction arguments to retain durable facts, then use `loom_search` to recall them in a later session. The per-store `memory.search` operation is an HTTP/SDK surface. This requires deployment and credentials; URL onboarding is not claimed. Connection details and commands were checked against release sources; installation and live calls were not run for this entry.

---

## Agent Skills

**Status:** ✅ Bundled with the official coding-agent plugin

The [released plugin guide](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/integrations/claude-code.md) documents installation against an existing server:

```bash
claude plugin marketplace add ClickHouse/loom
claude plugin install loom@loom \
  --config server_url=https://loom.example.com \
  --config 'token=REPLACE_WITH_WRITER_JWT'
```

Replace the host and token placeholder with the deployment's values. This is the documented plugin installation path; a separate `npx skills add` command is not claimed.

| Skill | What It Teaches the Agent |
|---|---|
| [`loom-code`](https://github.com/ClickHouse/loom/blob/v1.2.0/integrations/claude-code-plugin/skills/loom-code/SKILL.md) | Use Loom's index to find symbols, callers and relevant code in an indexed repository. |

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/ClickHouse/loom |
| **Transport** | Streamable HTTP at the deployed server's `/mcp`; a stdio-only client can use a bridge. |
| **Auth** | Bearer token for shared authenticated deployments; namespace grants and roles constrain access. |
| **Compatible Clients** | Streamable HTTP MCP clients; see the [released client guide](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/integrations/mcp-clients.md). |

---

## What It Does

Loom is self-hosted infrastructure for shared agent memory across sessions. `memory.set_from_messages` selects durable facts from transcripts, removes repeated content and writes through conflict checks while preserving source evidence. Agents retrieve memories semantically over MCP, HTTP or SDKs. [Released extraction guide](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/memory/extraction.md).

Memory lifecycle includes [deduplication and conflict policies](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/memory/conflicts-and-refusal.md), [semantic retrieval](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/memory/search-and-ask.md) and [writer-set expiry or configured retention](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/memory/retention-and-erasure.md). There is no default age-based eviction: removal follows a writer, owner or operator instruction.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Shared memory, document search and code intelligence for AI agents." — [released README](https://github.com/ClickHouse/loom/blob/v1.2.0/README.md). |
| **Agent-specific primitive** | "`memory.set_from_messages` takes a transcript and the server decides what in it is durable." — [extraction](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/memory/extraction.md). |
| **Autonomy-compatible control plane** | "The token fixes the caller (`sub`), the org, the namespaces it may read and the roles it holds." — [tokens and grants](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/guides/tokens-and-grants.md). Agents can perform permitted memory operations without per-call human confirmation. |
| **M2M integration surface** | "The plugin's `.mcp.json` points at `<server_url>/mcp?toolset=<toolset>`" — [plugin guide](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/integrations/claude-code.md). MCP, HTTP, Python and TypeScript SDKs are documented in the [released README](https://github.com/ClickHouse/loom/blob/v1.2.0/README.md). |
| **Identity / delegation** | "`agent` records who wrote a row; it is not a boundary." — [identity model](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/concepts/identities-and-namespaces.md). Authenticated tokens and namespace grants govern access. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| `memory.set_from_messages` | Extract durable facts from a transcript with source evidence. |
| `loom_search` / HTTP/SDK `memory.search` | Recall relevant memories semantically across sessions. |
| Memory revision and refusal | Reconcile conflicting facts and reject blacklisted content. |
| Shared namespaces | Keep persistent memory available to authorized agents. |

---

## Autonomy Model

1. An operator deploys Loom, configures providers and grants namespace access.
2. The agent connects with its credential and retrieves relevant memory.
3. It submits transcript messages for durable-fact extraction.
4. Loom applies memory conflict policies and persists accepted facts with evidence.
5. An authorized later session retrieves those facts without a person confirming each operation.

---

## Identity and Delegation Model

- Rows carry organization, namespace, agent, user and session identity.
- The server stamps `actor` from the authenticated token. The caller-supplied `agent` label records authorship and is not an access boundary.
- Token roles, namespace grants and optional read ceilings constrain access. Sharing a namespace does not isolate its members by agent label.
- Memory writes retain audit and source-evidence records. Memory access grants do not delegate authority to act in external systems.

Sources: [identity model](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/concepts/identities-and-namespaces.md), [tokens and grants](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/guides/tokens-and-grants.md).

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP | Streamable HTTP tools at `/mcp`. |
| HTTP API | Operations at `POST /v1/<op>`. |
| Python SDK | Programmatic memory operations. |
| TypeScript SDK | Programmatic memory operations. |

Sources: [released README](https://github.com/ClickHouse/loom/blob/v1.2.0/README.md), [MCP client guide](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/integrations/mcp-clients.md).

---

## Human-in-the-Loop Support

An operator configures providers, credentials, namespace grants and retention policy. Authorized memory calls do not require per-action confirmation. The optional dashboard supports administration; this listing does not claim an external-action approval gate. [Released README](https://github.com/ClickHouse/loom/blob/v1.2.0/README.md).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| Raw vector storage | Vector similarity alone does not select durable facts from transcripts, reconcile conflicting memories or preserve extraction evidence. |
| Conversation log | Persisting messages alone does not extract and semantically retrieve durable facts across agent sessions. |

---

## Use Cases

- **Session continuity** — recall decisions and preferences after an agent restarts.
- **Shared project memory** — let authorized agents retrieve facts in a shared namespace.
- **Evidence-backed recall** — keep transcript evidence with extracted durable facts.

Sources: [released README](https://github.com/ClickHouse/loom/blob/v1.2.0/README.md), [extraction guide](https://github.com/ClickHouse/loom/blob/v1.2.0/docs/features/memory/extraction.md).
