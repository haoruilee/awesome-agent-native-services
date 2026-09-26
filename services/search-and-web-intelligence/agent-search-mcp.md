# Agent Search MCP

> **"A Node.js MCP server and CLI for English and Chinese web search."**

| | |
|---|---|
| **Website** | https://lennney.com/en/agent-search-mcp |
| **Docs** | https://github.com/lennney/agent-search-mcp#readme |
| **GitHub** | https://github.com/lennney/agent-search-mcp |
| **Stars** | [![GitHub Stars](https://img.shields.io/github/stars/lennney/agent-search-mcp?style=social)](https://github.com/lennney/agent-search-mcp) |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |
| **License** | Apache-2.0 |
| **Latest-month signal** | Product page moved to [lennney.com/en/agent-search-mcp](https://lennney.com/en/agent-search-mcp); `take-a-deep-breath0.com` redirects there. Last GitHub push 2026-09-21; license Apache-2.0 ([repo](https://github.com/lennney/agent-search-mcp)) |
| **Verified at** | 2026-09-26 |

---

## Official Website

https://lennney.com/en/agent-search-mcp

`https://take-a-deep-breath0.com/en/agent-search-mcp` redirects here (confirmed 2026-09-26). Page title: **"Agent Search MCP: Free Web Search for AI Agents – Lennney"**.

---

## Official Repo

https://github.com/lennney/agent-search-mcp

---

## How to Use (Agent Onboarding)

**Interaction pattern:** `MCP` (stdio) + optional **Agent Skill** + `fasm` CLI

```json
{
  "mcpServers": {
    "agent-search": {
      "command": "npx",
      "args": ["-y", "agent-search-mcp"]
    }
  }
}
```

```bash
npx -y agent-search-mcp
npx skills add lennney/agent-search-mcp --skill agent-search
```

No API key is required for the default free-first runtime. HTTP mode requires `HTTP_AUTH_TOKEN` unless `HTTP_ALLOW_UNAUTHENTICATED=true`.

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add lennney/agent-search-mcp --skill agent-search
```

| Skill | What It Teaches the Agent |
|---|---|
| `agent-search` | Choose a bounded path (quick discovery, stricter verification, Chinese-source search, or URL extract); check the MCP tool exists; ask before install/config changes |

Installing the Skill does not start the MCP server.

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **MCP Repo** | https://github.com/lennney/agent-search-mcp |
| **Transport** | stdio (default) or Streamable HTTP |
| **Compatible Clients** | Claude Desktop, Cursor, VS Code, Windsurf, Claude Code, Codex |

Tools include `free_search`, `free_search_advanced`, `free_extract`, `fetch_github_readme`, `fetch_csdn_article`, `fetch_juejin_article`, and `search_with_synthesis`. All documented as read-only and idempotent.

---

## What It Does

Agent Search MCP is a Node.js search runtime that starts without an API key. It fans out to zero-key engines (and optional paid providers only when policy and credentials allow), then returns a Search Evidence Packet: results plus `meta.execution`, quality-gate `stop_reason`, budgets, and `partialFailures`. Compact mode bounds tokens while keeping provenance. Chinese queries can use Sogou/Baidu without a translation layer.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README title: **"Agent Search MCP: Free-first Web Search with Inspectable Evidence"** and **"A Node.js MCP server and CLI for English and Chinese web search."** — [repo](https://github.com/lennney/agent-search-mcp) |
| **Agent-specific primitive** | Evidence packet with independent `source_count`, visible `partialFailures`, and a quality-gate `stop_reason` — not a silent SERP scrape |
| **Autonomy-compatible control plane** | Default `free_first` policy never spends a configured key. Agent can search/extract without a human picking engines per query |
| **M2M integration surface** | MCP stdio/HTTP, `fasm` CLI, published Skill |
| **Identity / delegation** | HTTP deployments use `HTTP_AUTH_TOKEN`. Engine/tool allowlists are env policy. No per-end-user OAuth product; this is search infrastructure |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Search Evidence Packet** | Results + execution meta + failures, kept separate |
| **Provider policy** | `free_first`, `free_only`, `quality_escalation`, `paid_first` |
| **Request / evidence budgets** | Caps on adapter calls, time, results, and evidence characters |
| **`source_count`** | Independent provider families, not adapter aliases |
| **`fasm` CLI** | `search`, `extract`, `doctor` |

---

## Autonomy Model

```
Add npx -y agent-search-mcp to the MCP host
    -> agent calls free_search or related tools
    -> router runs zero-key sources (and paid only if policy allows)
    -> quality gate stops and records stop_reason
    -> failures stay in partialFailures
    -> compact evidence returns to the agent
```

---

## Identity and Delegation Model

- **No search-user identity:** Default local stdio has no account.
- **HTTP token:** Required unless explicitly unauthenticated.
- **Spend policy:** Keys in env do not authorize paid traffic until `SEARCH_PROVIDER_MODE` says so.
- **Allowlists:** `ENABLED_TOOLS` / `ALLOWED_ENGINES` (deny wins).
- **Doctor:** `fasm doctor` never prints credentials or proxy secrets.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| MCP stdio | `npx -y agent-search-mcp` |
| MCP HTTP | `MODE=http` + `HTTP_AUTH_TOKEN` |
| CLI | `fasm search`, `extract`, `doctor` |
| Skill | `npx skills add lennney/agent-search-mcp --skill agent-search` |

---

## Human-in-the-Loop Support

The Skill asks before install or configuration changes. Search itself is autonomous. Optional paid providers need a human-supplied key and an explicit policy.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Human SERP API** | Blue links for eyes; no evidence packet or failure visibility |
| **Silent multi-engine wrapper** | Drops failed providers; inflates source counts by adapter name |
| **Single paid agent search** | Requires a key up front; no free-first policy or budget contract |

---

## Use Cases

- **Keyless web search** from an MCP host
- **Claim verification** with inspectable evidence and stop reasons
- **Chinese-source search** without translating the query first
- **Token-bounded retrieval** via compact evidence budgets
