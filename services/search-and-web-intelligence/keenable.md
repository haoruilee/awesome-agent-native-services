# Keenable

> **"Independent Web Search API for AI."**

| | |
|---|---|
| **Website** | https://keenable.ai |
| **Docs** | https://docs.keenable.ai |
| **GitHub** | https://github.com/keenableai/keenable-mcp |
| **License** | MIT |
| **Classification** | `agent-native` |
| **Category** | [Search & Web Intelligence Services](README.md) |
| **Interest disclosure** | [Issue #281](https://github.com/haoruilee/awesome-agent-native-services/issues/281) was opened by KGKallasmaa, who disclosed that they are an engineer at Keenable |
| **Latest-month signal** | Checked 2026-11-19: [keenable.ai](https://keenable.ai) HTTP 200, page title “Keenable.ai — Independent Web Search API for AI”; [docs](https://docs.keenable.ai) and [llms.txt](https://docs.keenable.ai/llms.txt) HTTP 200; public MCP `https://api.keenable.ai/mcp-public` `initialize` HTTP 200 as `keenable-mcp-server` 0.2.1, title “Keenable Web Search”; `tools/list` includes `search_web_pages` and `fetch_page_content`; [OpenAPI](https://api.keenable.ai/openapi.json) 0.1.37; `POST /v1/search` with no key HTTP 401; `POST /v1/search/public` with `X-Keenable-Title` HTTP 200; [keenable-mcp](https://github.com/keenableai/keenable-mcp) SPDX MIT, 7 stars, last push 2026-11-18; [keenable-sdk](https://github.com/keenableai/keenable-sdk) SPDX MIT, last push 2026-11-18; [keenable-cli](https://github.com/keenableai/keenable-cli) has no license file |
| **Verified at** | 2026-11-19 |

---

## Official Website

https://keenable.ai

---

## Official Repo

https://github.com/keenableai/keenable-mcp

The MCP server and the official SDKs are open source under MIT. The hosted crawler, index, and ranking are not in those repositories.

https://github.com/keenableai/keenable-sdk — MIT. Python, TypeScript, Go, and Rust clients. The repository description says search is keyless by default.

https://github.com/keenableai/keenable-cli — public CLI for auth, API keys, MCP setup, and search. Checked 2026-11-19: GitHub reports no license, and the repository has no `LICENSE` file. This entry does not assign one.

---

## ⭐ How to Use (Agent Onboarding)

> **⭐ URL Onboarding — an agent can connect by reading one URL. No account and no API key are required for the public tier.**

**Interaction pattern:** URL Onboarding

**One-sentence instruction:**

```
Read https://docs.keenable.ai/llms.txt and follow the instructions.
```

`llms.txt` says search and fetch work without an account or API key, and it points at the official SDK. The same keyless tier is on the public MCP server, which publishes no OAuth discovery:

```bash
claude mcp add --transport http keenable https://api.keenable.ai/mcp-public
```

An API key is optional. Production use can read `KEENABLE_API_KEY` from the environment. Key creation is documented at https://docs.keenable.ai/api-keys. x402 pay-per-request routes are also optional; they are not required to search.

Coding-time skill, also keyless:

```bash
npx skills add keenableai/keenable-mcp
```

---

## Agent Skills

**Status:** ✅ Available

```bash
npx skills add keenableai/keenable-mcp
```

| Skill | What It Teaches the Agent |
|---|---|
| `keenable-web-search` | Search the live web and return ranked, citable results with titles, URLs, and snippets. Version 1.2.0 calls the keyless public endpoint from a bundled standard-library script, so the skill itself needs no API key. MIT. |

---

## MCP

**Status:** ✅ Available

| Detail | Value |
|---|---|
| **Public endpoint** | `https://api.keenable.ai/mcp-public` |
| **Authenticated endpoint** | `https://api.keenable.ai/mcp` |
| **Transport** | Remote Streamable HTTP. Stdio bridge: `npx -y @keenable/mcp` |
| **Server** | `keenable-mcp-server` 0.2.1, title “Keenable Web Search”. Checked 2026-11-19 |
| **Tools** | `search_web_pages` returns ranked results with title, URL, and citable snippets. `fetch_page_content` returns one page as clean Markdown |
| **Auth** | None on `/mcp-public`. An API key is optional for higher limits |
| **Repo** | https://github.com/keenableai/keenable-mcp (MIT) |
| **Compatible Clients** | Claude Code, Cursor, and other remote-HTTP MCP clients |

---

## What It Does

Keenable is a web search API whose index, crawler, and ranking are its own. The homepage description is: “Keenable is independent web search infrastructure for AI: our own crawler, index and ranking, and it gets better the more agents use it.”

Agents call it over MCP, a REST API, official SDKs, or a published skill. Search results are ranked pages with titles, URLs, and snippets sized for a citation. Page fetch returns clean Markdown rather than a browser document. There is no consumer search page to operate; the product is the agent interface.

The open-source pieces are the MCP server, the SDKs, and the skill. The hosted index stays closed.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage title: “Independent Web Search API for AI.” Docs: “Web search and page fetch for AI agents, on Keenable's own index.” https://keenable.ai and https://docs.keenable.ai/llms.txt |
| **Agent-specific primitive** | `search_web_pages` tells the model to describe the ideal page rather than send keywords, and returns citable snippets. `fetch_page_content` returns the page as Markdown for a context window |
| **Autonomy-compatible control plane** | The public MCP and `POST /v1/search/public` run with no account and no API key. Limits on that tier are per IP (1,000 requests per hour and 10 per second, as stated in the MCP `initialize` instructions). An optional key or x402 wallet raises or replaces that path; neither is required for the first search |
| **M2M integration surface** | Remote MCP, OpenAPI 0.1.37, MIT SDKs, `npx -y @keenable/mcp`, and the `keenable-web-search` skill |
| **Identity / delegation** | Read-only search. The public tier is anonymous and per IP. An optional organization API key attributes usage to that key. An optional x402 wallet pays per request from the agent's own address. The service does not send, write, or buy on a person's behalf |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **search_web_pages** | Ranked live-web results with title, URL, snippet, and publish date when one is known. The tool text says to describe the ideal page, not a keyword list |
| **fetch_page_content** | One URL returned as clean Markdown when the snippet is not enough |
| **Public REST search** | `POST /v1/search/public` with an `X-Keenable-Title` header. Checked 2026-11-19: HTTP 200, with `title`, `url`, and `snippet` on each result. `POST /v1/search` without a key returns HTTP 401 |
| **Optional key and x402** | `X-API-Key` or a bearer token for the keyed API. OpenAPI also lists `/v1/x402/search` and `/v1/x402/fetch` |

---

## Autonomy Model

1. The agent reads https://docs.keenable.ai/llms.txt.
2. It connects to `https://api.keenable.ai/mcp-public` or calls `POST /v1/search/public` with `X-Keenable-Title`.
3. It searches, cites the returned URLs, and fetches a page as Markdown when it needs the full text.
4. No person creates an account for that loop. A person can later add `KEENABLE_API_KEY` for production limits, or the agent can use an x402 wallet. Both are optional.

---

## Identity and Delegation Model

- Public tier: no credential. Usage is limited per IP address.
- Organization API key: optional. Usage is attributed to that key. Creating one is a human step at https://docs.keenable.ai/api-keys.
- x402: optional pay-per-request from a wallet the agent controls. Listed in the OpenAPI spec; not required to qualify or to make a public search.
- The MCP `search_web_pages` schema accepts an optional `session_id` so calls from one agent session can be grouped. That field does not create an account.

---

## Protocol Surface

| Interface | Detail |
|---|---|
| URL onboarding | `Read https://docs.keenable.ai/llms.txt and follow the instructions.` |
| Remote MCP | `https://api.keenable.ai/mcp-public` (no key); `https://api.keenable.ai/mcp` (optional key) |
| REST / OpenAPI | https://api.keenable.ai/openapi.json version 0.1.37 |
| SDKs | https://github.com/keenableai/keenable-sdk (MIT). `npm install keenable`, `pip install keenable` |
| Stdio MCP | `npx -y @keenable/mcp` |
| Agent Skill | `npx skills add keenableai/keenable-mcp` (`keenable-web-search` 1.2.0, MIT) |
| CLI | https://github.com/keenableai/keenable-cli — license not published |

---

## Human-in-the-Loop Support

The public search and fetch loop does not ask a person to click. A person is needed only if the agent should use a keyed organization account, add credits after an HTTP 402 on a keyed call, or fund an x402 wallet. Docs tell the agent not to ask for a pasted key in chat and to send the person to the API-key page instead.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Google Programmable Search or a Bing-style web search API** | Built to fill a human results page, then exposed as an API. The first call needs a human account, project, and key. Results are SERP-shaped links, not an agent tool that returns citable snippets and page Markdown, and there is no keyless MCP tier |
| **A generic HTTP API that only adds x402** | A paywall on an ordinary API is not this listing. Keenable qualifies because the search index is agent-facing: keyless MCP tools, citation snippets, and Markdown page fetch work before any wallet is used |

---

## Use Cases

- **Cited research** — search for a current fact and keep the title and URL next to the snippet.
- **Documentation lookup** — restrict `search_web_pages` to one site, then fetch the page as Markdown.
- **Keyless trial** — an agent in a fresh session calls the public MCP or `/v1/search/public` before anyone creates a key.
