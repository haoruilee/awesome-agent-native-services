# Mnemoverse

> **"Persistent memory for AI agents."**

| | |
|---|---|
| **Website** | https://mnemoverse.com/ |
| **Docs** | https://mnemoverse.com/docs/api/reference |
| **GitHub** | https://github.com/mnemoverse/mcp-memory-server |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/mnemoverse/mcp-memory-server?style=social)](https://github.com/mnemoverse/mcp-memory-server) |
| **Classification** | `agent-native` |
| **Category** | [Memory & State Services](README.md) |
| **License** | MCP server MIT, Python SDK MIT; the memory engine they call is a proprietary hosted service with a free tier. No self-hostable build of the engine is published; Enterprise customers can self-host it by agreement |
| **Latest-month signal** | npm `@mnemoverse/mcp-memory-server` 0.10.2 published 2026-09-20 ([npm](https://www.npmjs.com/package/@mnemoverse/mcp-memory-server)); PyPI `mnemoverse` 0.3.0 ([PyPI](https://pypi.org/project/mnemoverse/)); an unauthenticated POST to https://mcp.mnemoverse.com/mcp answered 401 with OAuth resource metadata on 2026-09-20 |
| **Verified at** | 2026-09-20 |

---

## Official Website

https://mnemoverse.com/

Homepage H1, read 2026-09-20: **"Persistent memory for AI agents"**. Supporting line: "One memory. Every AI tool. Write once, recall anywhere: across Claude Code, Cursor, VS Code, ChatGPT, and Python, with one API key or OAuth."

---

## Official Repo

https://github.com/mnemoverse/mcp-memory-server

README lead: **"Persistent memory for AI agents over MCP. Tell it a recalled memory helped or misled, and it re-ranks what comes back next. One key across Claude Code, Cursor, VS Code and ChatGPT."**

The MCP server is MIT (`LICENSE` in the repository, `"license": "MIT"` on npm), and so is the Python SDK (`mnemoverse` on PyPI carries the MIT classifier). The memory engine behind both is proprietary and hosted, with a free tier, and only the clients are published as source. No self-hostable build of the engine is published; Enterprise customers can self-host it by agreement ([pricing](https://mnemoverse.com/docs/api/pricing)).

Other public client repositories: [claude-plugin](https://github.com/mnemoverse/claude-plugin), [cursor-plugin](https://github.com/mnemoverse/cursor-plugin), [gemini-extension](https://github.com/mnemoverse/gemini-extension), [mnemoverse-vscode](https://github.com/mnemoverse/mnemoverse-vscode), and the CC0 skill [agent-memory-discipline](https://github.com/mnemoverse/agent-memory-discipline).

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `MCP (Streamable HTTP)`

A stdio package is the alternative. Both paths reach the same memory and expose the same tools. They differ only in how the agent authenticates.

**Remote connector (OAuth, no key to paste).** Point the client at the hosted endpoint:

```json
{
  "mcpServers": {
    "mnemoverse": {
      "url": "https://mcp.mnemoverse.com/mcp"
    }
  }
}
```

In Claude Code the same server is added, then signed in, with:

```bash
claude mcp add -s user --transport http mnemoverse https://mcp.mnemoverse.com/mcp
```

The first connect or first tool call opens a browser consent screen once, and the client stores the tokens itself. VS Code needs `"type": "http"` on the entry or it tries to launch a local process instead.

**Local package (API key).** For scripts, CI, and unattended agents, whose host app session must not be able to drop the connection:

```bash
claude mcp add mnemoverse -s user -e MNEMOVERSE_API_KEY=mk_live_YOUR_KEY -e MNEMOVERSE_API_URL=https://core.mnemoverse.com/api/v1 -- npx -y @mnemoverse/mcp-memory-server@latest
```

Creating the account and the first credential needs a human: there is no self-service registration an agent can complete on its own, so this is not URL onboarding. After that one step the agent works unattended.

**One-sentence instruction:** Add `https://mcp.mnemoverse.com/mcp` as a remote MCP server and complete the browser sign-in, or run `npx -y @mnemoverse/mcp-memory-server@latest` with `MNEMOVERSE_API_KEY` set to a key from https://console.mnemoverse.com .

---

## Agent Skills

**Status:** ✅ Available, published separately from the server.

```text
/plugin marketplace add mnemoverse/agent-memory-discipline
/plugin install agent-memory-discipline@agent-memory-discipline
```

| Skill | What It Teaches the Agent |
|---|---|
| [`agent-memory-discipline`](https://github.com/mnemoverse/agent-memory-discipline) | When a task warrants a recall before acting and when it does not; which events are worth saving afterwards; what an entry needs to still be usable weeks later; how to close a superseded entry instead of overwriting it; how to keep two entries that disagree visible with their dates |

The skill is CC0 and backend neutral: it installs no backend and assumes no particular store, so it also applies to a folder of Markdown notes or a different memory server. The same skill ships inside the [Claude Code plugin](https://github.com/mnemoverse/claude-plugin).

---

## MCP

**Status:** ✅ Available on two transports, with the same ten tools on each.

| Detail | Remote connector | Local package |
|---|---|---|
| **MCP Repo** | Hosted endpoint `https://mcp.mnemoverse.com/mcp`; OAuth discovery metadata and the server card are public | https://github.com/mnemoverse/mcp-memory-server |
| **Transport** | Streamable HTTP, POST only (a browser GET returns 404 by design) | stdio, spawned with `npx` |
| **Authentication** | OAuth 2.1 + PKCE; the endpoint answers an unauthenticated call with 401 and a pointer to its protected-resource metadata | `MNEMOVERSE_API_KEY` in the client config |
| **Compatible Clients** | Claude Code, Claude Desktop, Cursor, Windsurf, VS Code, ChatGPT developer-mode connectors | Any stdio MCP client: Claude Code, Cursor, VS Code, Windsurf, Zed, JetBrains AI Assistant, Cline, Continue |

The ten tools are `memory_write`, `memory_read`, `memory_list_recent`, `memory_feedback`, `memory_stats`, `memory_create_room`, `memory_invite_to_room`, `memory_join_room`, `memory_list_rooms`, and `vault_list`. The four room tools are Beta. `vault_list` returns secret aliases and purposes, never values. Per the published tool-surface policy, `tools/list` is frozen inside a patch release and tools may only be added inside a minor one, so a client can diff the list it saw against the list served today.

Removing stored memory is not an MCP tool on either path: it is an administrative REST operation called directly against the API.

---

## What It Does

Mnemoverse keeps what an agent learns outside its context window and returns it in whatever tool the agent is running in next. A decision made while pairing in Claude Code is available in Cursor an hour later under the same account, and in a ChatGPT connector the same evening, because all of them talk to one hosted store rather than to per-tool instruction files.

The primitive that separates it from a vector index is outcome feedback. After a recall the agent calls `memory_feedback` with the identifiers it used and an outcome score, and the service moves those entries in future ranking. Similarity alone never changes because advice turned out to be wrong; a reported outcome does. Recall also expands along Hebbian links between the concepts attached to entries, so a query can reach an entry that shares no wording with it.

**Boundary, stated rather than implied.** The agent decides what to offer for storage; `memory_write` is an explicit call, not a transcript miner. What the service does on its own at write time is score the candidate and decide whether it clears an importance gate, returning `stored`, the computed `importance`, and a `reason` for each atom. A read returns provenance with each hit, including the author principal, and a read can exclude one author. Several other entries in this category are explicit-write services on the same terms.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | "Persistent memory for AI agents" is the homepage H1, https://mnemoverse.com/ . The server README opens with "Persistent memory for AI agents over MCP", https://github.com/mnemoverse/mcp-memory-server |
| **Agent-specific primitive** | `memory_feedback`: the agent marks recalled entries as helpful or misleading and later recall is re-ranked from that outcome. A human has no reason to grade retrieval results one by one inside a task loop. https://mnemoverse.com/docs/api/remote-mcp-server |
| **Autonomy-compatible control plane** | After one sign-in or one key, the agent writes, reads and reports outcomes with no per-action confirmation. The ceiling is explicit: per-organization rate limits (free plan 60 requests per minute, 1,000 queries per day, 10,000 atoms), OAuth scopes that can be read-only, and room membership fixed at `read` or `read_write`. https://mnemoverse.com/docs/api/reference , https://mnemoverse.com/docs/api/rooms |
| **M2M integration surface** | Streamable HTTP MCP at `https://mcp.mnemoverse.com/mcp`, stdio MCP via `npx -y @mnemoverse/mcp-memory-server@latest`, REST at `https://core.mnemoverse.com/api/v1`, a Python SDK (`pip install mnemoverse`), plus a Claude Code plugin, a Cursor plugin, a Gemini CLI extension and a VS Code extension. https://mnemoverse.com/docs/api/agent-setup , https://github.com/mnemoverse/mcp-memory-server |
| **Identity / delegation** | OAuth 2.1 with PKCE and the scopes `memory:read`, `memory:write`, `offline_access`, revocable from the console; a connector granted only `memory:read` can recall but not write. Dynamic client registration is restricted to an allowlist of callback hosts plus loopback. Room invite codes carry a `read` or `read_write` scope fixed when the code is minted. https://mnemoverse.com/docs/api/remote-mcp-server |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Atom** | One stored memory with its content, concepts, and domain; the write returns whether it cleared the importance gate, its computed importance, and the reason |
| **Outcome feedback** | `memory_feedback` reports that recalled atoms helped or misled; the report changes how those atoms rank in later recall, alongside similarity rather than instead of it |
| **Hebbian concept link** | Associations between the concepts carried by atoms; a read can expand along them, and reported outcomes update them |
| **Domain** | A named partition of one account's memory, and also the address form a shared room takes on read and write |
| **Room (Beta)** | A memory pool several accounts read and write, entered with a `mnvr_...` invite code whose scope is fixed at mint, with membership checked on every request |
| **Vault alias** | A named reference to a stored secret that an agent can list and use by name; the value is never returned to the model |

---

## Autonomy Model

1. A human creates the account once and either completes the OAuth consent screen in the browser or copies one API key from the console.
2. The agent connects: the remote connector negotiates OAuth 2.1 with PKCE and stores its own tokens, or the local package starts under `npx` with the key from its config.
3. During work the agent calls `memory_read` or `memory_list_recent` before acting, and `memory_write` when a decision, correction or preference is worth keeping. No approval step stands between the call and the store.
4. After using what came back, the agent calls `memory_feedback` with the atom identifiers and an outcome score, which moves those atoms for later recall.
5. In a later session, in a different tool, the same account recalls the same memory. For work shared across accounts the agent creates a room, mints an invite, and the other side joins with the code.
6. The agent stays inside the ceiling it was given: scopes, per-organization rate limits, and room scope. Exceeding a limit returns `429 RATE_LIMITED` with the headers needed to back off.

---

## Identity and Delegation Model

- The remote connector is an OAuth 2.1 resource server. The agent's client registers dynamically (RFC 7591), obtains scoped access and refresh tokens, and sends the access token on every request; no key is ever pasted.
- Scopes are granted at consent and enforced afterwards: a connector granted only `memory:read` recalls but cannot write, and `offline_access` is what lets it keep working without the human present. Access is revoked from the console.
- Dynamic registration only accepts callbacks on known connector hosts plus RFC 8252 loopback addresses. That is an anti-phishing control, and it means a client served from a custom domain is refused registration and has to use the API-key path instead.
- The API key path is a separate principal that lives in the client's own config rather than in the host application's session, which is why it survives account switches and suits unattended agents.
- Rate limits are enforced per organization, so every key in one organization shares the same limiter.
- Each stored atom records its author principal, a read returns that provenance, and a read can exclude one author, which is how an agent avoids re-reading its own writes in a shared room.
- Room membership is checked on every call, revocation takes effect on the next request, and an invite's scope cannot be widened after it is minted.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP over Streamable HTTP | Hosted at `https://mcp.mnemoverse.com/mcp`, OAuth 2.1 + PKCE, POST only |
| MCP over stdio | `npx -y @mnemoverse/mcp-memory-server@latest`, authenticated with `MNEMOVERSE_API_KEY` |
| REST API | `https://core.mnemoverse.com/api/v1`, the full surface, including the administrative operations that sit outside the MCP tool set |
| Python SDK | `pip install mnemoverse` |
| Editor and CLI packages | Claude Code plugin, Cursor plugin, Gemini CLI extension, VS Code extension, and an MCPB desktop-extension manifest that runs the server as a local process |
| Agent Skill | `agent-memory-discipline`, CC0, distributed through the plugin marketplace and bundled in the Claude Code plugin |

---

## Human-in-the-Loop Support

A human is required exactly twice: to create the account, and to grant the connector its scopes at the consent screen or issue the API key. Everything after that is machine to machine.

The human keeps standing controls rather than per-call approval: scopes can be narrowed to read-only, access can be revoked from the console, room grants can be changed or revoked with effect from the next request, and rate limits bound the per-organization blast radius. There is no built-in approval queue for an individual write, and this entry does not claim one. An application that needs per-write review has to add that step around the call.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Per-tool instruction files** (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`) | Versioned and readable, but each copy belongs to one repository and one tool. Nothing follows the agent into the next tool or the next session, and there is no ranking at all |
| **A bare vector store behind RAG** | Retrieves by similarity, and similarity does not change because a retrieved item turned out to be wrong. There is no place to report an outcome and nothing re-ranks from one |
| **Application-owned chat history** | A transcript inside one product is not an independently addressable store that other agents, under their own credentials and scopes, can read and write |
| **A shared database with an agent wrapper** | Gives storage and queries but no agent-facing contract: no scoped delegation an agent can hold, no provenance on read, no outcome signal, and no cross-account room with a membership check on every request |

---

## Use Cases

- **Cross-tool continuity** - A decision made in Claude Code is recalled in Cursor or VS Code later the same day under one account, with no copying between configuration files.
- **Stop re-explaining the project** - Stack, conventions and deployment facts are written once and recalled at the start of each session instead of being restated in every prompt.
- **Ranking that follows outcomes** - An agent that reports which recalled entries actually helped gets those entries first next time, which matters once a store outgrows hand curation.
- **Shared team memory** - A room lets several accounts accumulate lessons about one codebase in a single pool, with each entry carrying its author and each invite carrying a fixed scope.
- **Unattended agents** - The API-key path keeps working through host application account switches and sign-outs, so a scheduled or CI agent does not silently lose memory.
- **Secrets by alias** - An agent lists vault aliases and refers to a credential by name, so the value never enters the model's context.
