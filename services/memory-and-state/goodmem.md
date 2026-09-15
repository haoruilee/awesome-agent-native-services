# GoodMem

> **"Memory that survives context windows."**

| | |
|---|---|
| **Website** | https://goodmem.ai/ |
| **Docs** | https://docs.goodmem.ai/ |
| **GitHub** | https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin (plugin, skills, and MCP configuration) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **Deployment / License** | GoodMem Cloud or self-hosted proprietary core under the [free binary license](https://goodmem.ai/license) |

---

## Official Website

https://goodmem.ai/

---

## Official Repo

https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin — official plugin, published agent skills, and configuration for the npm MCP package.

The [LlamaIndex integration](https://github.com/PAIR-Systems-Inc/goodmem-llamaindex) is also public. These integration repositories do not contain the proprietary GoodMem server core.

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `MCP (Streamable HTTP)`

A human first deploys GoodMem or provisions a GoodMem Cloud instance, creates a workload service identity, and grants access to the intended memory spaces. Follow the [service-identity setup guide](https://docs.goodmem.ai/docs/how-to/access-control/service-identities/) to issue its scoped API key.

The built-in MCP server starts with GoodMem and serves `/mcp` on the REST port. For retrieval, connect an HTTP MCP client directly; no local npm server is needed. A representative configuration is:

```json
{
  "mcpServers": {
    "goodmem": {
      "url": "https://goodmem.example.com/mcp",
      "headers": {
        "x-api-key": "gm_your_key"
      }
    }
  }
}
```

Replace the example host and key with the provisioned instance and workload credential, using the client's supported configuration format. Discover permitted spaces with `goodmem_list_spaces`, then search with `goodmem_retrieve`.

**One-sentence instruction:** After workload provisioning, connect an HTTP MCP client to your GoodMem instance's `/mcp` endpoint with an `x-api-key` header; follow the [native MCP setup](https://docs.goodmem.ai/docs/reference/mcp/).

The native endpoint currently provides read-only retrieval and diagnostics. For ingestion or management, use REST, an SDK, or the separate stdio adapter described below.

Account and credential provisioning require a human; reading a document alone does not register the agent or grant access.

---

## Agent Skills

**Status:** ✅ Available in the official Claude Code plugin.

Install the plugin and its skills from the public repository:

```text
/plugin marketplace add PAIR-Systems-Inc/goodmem-claude-code-plugin
/plugin install goodmem@goodmem-plugins
```

| Skill | What It Teaches the Agent |
|---|---|
| [`goodmem:help`](https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin/blob/main/skills/help/SKILL.md) | Setup, available capabilities, and example memory workflows |
| [`goodmem:mcp`](https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin/blob/main/skills/mcp/SKILL.md) | MCP tools and parameters for operating GoodMem |
| [`goodmem:python`](https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin/blob/main/skills/python/SKILL.md) | Python SDK methods, parameters, and examples |

---

## MCP

**Status:** ✅ Available through two distinct interfaces.

| Detail | Built-in GoodMem MCP | Separate npm adapter |
|---|---|---|
| **Documentation / source** | [Native MCP reference](https://docs.goodmem.ai/docs/reference/mcp/); implemented in the proprietary GoodMem server | [Plugin and launch configuration](https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin/blob/main/.mcp.json); [`@pairsystems/goodmem-mcp`](https://www.npmjs.com/package/@pairsystems/goodmem-mcp) distributes the adapter |
| **Transport** | Streamable HTTP at the instance's `/mcp` endpoint | Local stdio process calling the GoodMem REST API |
| **Authentication** | `x-api-key`, or `Authorization: Bearer` with a GoodMem API key | `GOODMEM_BASE_URL` and `GOODMEM_API_KEY` in the MCP client's process environment |
| **Capabilities** | Read-only memory/retrieval tools and inference diagnostics | Broader operations including ingestion, space management, and model configuration, subject to permissions |
| **Compatible Clients** | Clients supporting Streamable HTTP and API-key headers | Claude Code through the plugin, or clients supporting local stdio servers |

The built-in tools are `goodmem_list_spaces`, `goodmem_list_memories`, `goodmem_retrieve`, `goodmem_read_memory`, `goodmem_list_retrieval_models`, and `goodmem_ping_inference`. Native MCP is documented as early access; tool names and schemas may change.

For the stdio adapter, install Node.js and configure the client to launch:

```bash
npx -y @pairsystems/goodmem-mcp
```

See the [adapter configuration guide](https://github.com/PAIR-Systems-Inc/goodmem-claude-code-plugin#configuration). The plugin's MCP skill documents this broader adapter surface.

---

## What It Does

GoodMem gives agents persistent, searchable memory outside their context windows. Agents store documents, prior findings, and task history in memory spaces. The service handles configured chunking and embedding, then retrieves relevant context with optional reranking. Spaces can be isolated for one workload or shared between authorized agents. See the [integration overview](https://docs.goodmem.ai/docs/integrations/).

**Dual-use boundary:** GoodMem also supports conventional RAG, including document Q&A and knowledge search. Its storage and retrieval APIs are useful to ordinary applications as well as agents; those APIs are not exclusively agent-specific. This entry covers the persistent agent-memory workflow, published MCP/skills, and workload identity model. It does not claim automatic conversation-fact extraction, conflict resolution, or autonomous forgetting merely from storing a memory.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "GoodMem is memory infrastructure for AI agents." — [official homepage](https://goodmem.ai/) |
| **Agent-specific primitive** | Persistent, access-controlled memory spaces provide context across agent sessions and can be shared between agents. The combined memory workflow and agent interfaces are the basis for this entry; the underlying RAG APIs remain dual-use. |
| **Autonomy-compatible control plane** | A provisioned workload can ingest and retrieve within its grants and credential ceiling without per-operation dashboard interaction. See [service identities](https://docs.goodmem.ai/docs/how-to/access-control/service-identities/). |
| **M2M integration surface** | Built-in HTTP MCP for retrieval, a separate stdio MCP adapter, REST and gRPC APIs, SDKs, CLI, and [framework integrations](https://docs.goodmem.ai/docs/integrations/). GoodMem Cloud exposes REST over HTTPS, not gRPC. |
| **Identity / delegation** | [Service identities](https://docs.goodmem.ai/docs/concepts/users-and-service-identities/) represent workloads separately from humans; [scoped API keys](https://docs.goodmem.ai/docs/concepts/api-keys-and-ceilings/) constrain their authority. |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Memory space** | Persistent context container with configured embedding and access controls; usable by an individual agent or an authorized group |
| **Memory and retrieval** | Stored content and associated metadata, with server-side ingestion and semantic retrieval of relevant context |
| **Service identity** | Workload principal distinct from its human administrator |
| **Scoped credential** | API key whose immutable permission ceiling limits the authority available to an agent |

---

## Autonomy Model

1. A human provisions the instance, model configuration, memory space, workload identity, grants, and credential.
2. Content is ingested through REST, an SDK, or the stdio adapter; the configured pipeline chunks and embeds it.
3. The agent connects to the built-in HTTP MCP endpoint with its credential and discovers permitted spaces.
4. On later tasks or sessions, it retrieves relevant context from those spaces and uses it in the model's context window.
5. An agent authorized to store new findings uses REST, an SDK, or the stdio adapter. The built-in MCP endpoint does not expose writes.

The application or agent chooses what to retain and when to retrieve; GoodMem does not require a human to approve each permitted memory operation.

---

## Identity and Delegation Model

- A [service identity](https://docs.goodmem.ai/docs/concepts/users-and-service-identities/) authenticates as the workload, with its human creator and administrative owner recorded separately.
- Grants can scope access to particular spaces and their memories. A request must pass both the principal's current authority and the API key's immutable [permission ceiling](https://docs.goodmem.ai/docs/concepts/api-keys-and-ceilings/).
- Service identities cannot create other service identities or issue their own API keys. Human provisioning is required; this is not autonomous account registration.
- [Retrieval logging](https://docs.goodmem.ai/docs/reference/security/retrieve-memory-logging/) can record request/response envelopes with caller and API-key identifiers. It depends on caller opt-in or administrator policy and is best effort, rather than an unconditional audit log of every operation.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Memory, space, model, and access-control operations; see the [API reference](https://docs.goodmem.ai/docs/reference/api-reference/) |
| gRPC | Available for self-hosted deployments; GoodMem Cloud does not expose gRPC |
| Language SDKs | SDK access to GoodMem; the plugin includes a Python SDK skill |
| CLI | Structured commands for provisioning and operations; the service-identity guide documents workload setup |
| Native MCP | Built-in Streamable HTTP at `/mcp`; read-only retrieval and diagnostics |
| Stdio MCP adapter | Published npm server with additional ingestion and management operations |
| Framework integrations | [LlamaIndex and other integrations](https://docs.goodmem.ai/docs/integrations/) for memory ingestion and retrieval |

---

## Human-in-the-Loop Support

Humans provision workloads, assign grants, issue credentials, and manage access. Those controls constrain what an agent can do; this entry does not claim a built-in approval queue or denial-feedback workflow for individual memory operations. Applications can add their own approval steps around calls when needed.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Bare vector index** | Similarity search alone does not provide the combined agent-memory ingestion/retrieval workflow, published skills and MCP tools, and workload delegation model described here. |
| **Application-owned chat history** | A transcript in one application does not by itself provide an independently accessible memory service shared across authorized workloads and sessions. |

GoodMem's admission rests on that combined agent-facing service surface. Its support for conventional RAG remains an explicit boundary, not a claim that ordinary applications cannot use it.

---

## Use Cases

- **Research continuity** — Store source documents and findings, then retrieve relevant evidence in later agent sessions.
- **Support memory** — Retrieve prior incidents and resolutions; store newly established fixes for future troubleshooting.
- **Shared team context** — Give multiple service identities scoped access to a common memory space while keeping other spaces isolated.
- **Document-grounded assistants** — Retrieve relevant knowledge for answers; this also serves conventional RAG applications.
