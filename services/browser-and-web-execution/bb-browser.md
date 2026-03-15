# bb-browser

> **"Your browser is the API. No keys. No bots. No scrapers."**

| | |
|---|---|
| **Website** | https://github.com/epiral/bb-browser |
| **npm** | https://www.npmjs.com/package/bb-browser |
| **GitHub** | https://github.com/epiral/bb-browser |
| **Adapters** | https://github.com/epiral/bb-sites |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **License** | MIT |
| **GitHub Stars** | 376+ |
| **Scale** | 103 commands · 36 platforms |

---

## Official Website

https://github.com/epiral/bb-browser

---

## Official Repo

https://github.com/epiral/bb-browser — CLI, MCP server, Chrome extension

https://github.com/epiral/bb-sites — Community adapter registry (one JS file per command)

---

## Agent Skills

**Status:** ✅ Available on ClawHub

```bash
npx clawhub@latest install bb-browser
```

Also available as an OpenClaw-specific variant:

```bash
npx clawhub@latest install bb-browser-openclaw
```

| Skill | What It Teaches the Agent |
|---|---|
| `bb-browser` | Use 103 CLI commands across 36 platforms via the user's real browser; MCP integration; OpenClaw browser mode; how to add new site adapters |

---

## MCP

**Status:** ✅ Available (built-in)

bb-browser ships a built-in MCP server requiring zero additional setup — just add it to your MCP config.

```json
{
  "mcpServers": {
    "bb-browser": {
      "command": "npx",
      "args": ["-y", "bb-browser", "--mcp"]
    }
  }
}
```

| Detail | Value |
|---|---|
| **Transport** | stdio |
| **NPM** | `npx -y bb-browser --mcp` |
| **Compatible Clients** | Claude Code, Cursor, Claude Desktop, any MCP-compatible client |

---

## What It Does

bb-browser (BadBoy Browser) gives AI agents access to the entire authenticated internet by **routing commands through the user's real Chrome browser** — not a headless bot, not a scraper, not a reverse-engineered API. The agent calls a CLI command or MCP tool; bb-browser runs `fetch()` or `eval()` inside the user's actual browser tab, where the user is already logged in.

The core insight: **99% of websites don't offer public APIs, but they all accept browser requests. The user's authenticated session is the API.**

103 commands across 36 platforms are available instantly. Adding a new website takes an AI agent ~10 minutes to reverse-engineer autonomously.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | README opens with: *"bb-browser lets AI agents use that [existing login state] directly"*; GitHub description: *"CLI + MCP server for AI agents to control Chrome with your login state"* |
| **Agent-specific primitive** | **Authenticated session delegation** — the agent inherits the user's live browser cookies and tokens without any credential management; this primitive has no human-tool equivalent |
| **Autonomy-compatible control plane** | All 103 commands output structured JSON; `--jq` inline filtering; `--tab` for concurrent multi-tab operations; 20 parallel agents tested |
| **M2M integration surface** | CLI (`bb-browser site twitter/search "query"`), MCP server (`npx -y bb-browser --mcp`), HTTP daemon on `localhost:19824`, all `--json` output |
| **Identity / delegation** | The user installs the Chrome extension once; from that point, the agent acts with the user's identity across all 36 platforms — no per-platform OAuth, no API keys |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Authenticated Session Delegation** | Agent uses the user's live Chrome cookies/tokens — the website sees the real user, not a bot |
| **Site Command** | `bb-browser site <platform>/<command> [args]` — structured JSON output from any of 103 commands |
| **Browser Automation** | `open`, `click`, `fill`, `eval`, `snapshot`, `screenshot`, `fetch`, `network` — full CDP-level control |
| **Adapter Registry** | Community-maintained adapters (one JS file per command) at `epiral/bb-sites` |
| **MCP Server** | Built-in stdio MCP server — agents use `bb-browser` tools directly in Claude Code / Cursor |
| **OpenClaw Mode** | `--openclaw` flag routes through OpenClaw's built-in browser — no extension needed |
| **Self-extending** | Agents can autonomously reverse-engineer new sites and add adapters via `bb-browser guide` |

---

## Autonomy Model

```
User installs bb-browser Chrome extension once — grants session delegation
    ↓
Agent calls CLI or MCP tool: bb-browser site arxiv/search "RAG"
    ↓
bb-browser CLI sends request to local daemon (localhost:19824)
    ↓
Daemon sends command via SSE to Chrome extension
    ↓
Extension runs fetch()/eval() inside the user's real browser tab
    ↓
Website responds — it sees the logged-in user, not a bot
    ↓
Result returned as structured JSON to the agent
```

Six platforms in six commands:

```bash
bb-browser site arxiv/search "retrieval augmented generation"
bb-browser site twitter/search "RAG"
bb-browser site github/search "rag-framework"
bb-browser site stackoverflow/search "RAG implementation"
bb-browser site zhihu/search "RAG"
bb-browser site 36kr/newsflash
```

---

## Identity and Delegation Model

- **User installs extension once** — this is the delegation act; all subsequent agent actions inherit the user's session
- **No per-platform credentials** — the agent never handles API keys, OAuth tokens, or passwords
- **The website sees the real user** — anti-bot measures are bypassed because the request originates from the actual authenticated browser session
- **Scoped to the local machine** — the daemon binds to `localhost:19824` by default; the agent operates within the user's trust boundary

---

## Protocol Surface

| Interface | Detail |
|---|---|
| CLI | `bb-browser site <platform>/<command>` — 103 commands, all `--json` |
| MCP Server | `npx -y bb-browser --mcp` — stdio transport |
| HTTP Daemon | `localhost:19824` — local REST API |
| Chrome Extension | SSE bridge from daemon to browser; CDP-level control |
| OpenClaw Mode | `--openclaw` flag for OpenClaw browser integration |
| `--jq` | Inline JSON filtering with jq expressions |
| `--tab <id>` | Concurrent multi-tab operations |

---

## Human-in-the-Loop Support

The user performs one action (installing the extension and granting permission). All subsequent agent operations are fully autonomous. The user's login state is the control boundary — if the user revokes or logs out, the agent loses access.

---

## How bb-browser Differs from Other Browser Services

| Dimension | Browserbase | Bright Data Agent Browser | bb-browser |
|---|---|---|---|
| Browser | Cloud-hosted headless | Cloud-hosted headless | **User's real local Chrome** |
| Authentication | Must re-login per session | Must handle cookies | **Already logged in — zero setup** |
| Anti-bot | Stealth mode | Full unlocking infrastructure | **Invisible — it IS the user** |
| Platforms | Any (raw browser) | Any (with unlocking) | **36 platforms, 103 ready commands** |
| Setup | API key + cloud session | API key | **npm install + Chrome extension** |
| Cost | Per session/minute | Per request | **Free (local)** |

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Playwright/Selenium** | Isolated headless browser — must re-login, easily detected as bot |
| **Scraping libraries (BeautifulSoup, Scrapy)** | No JavaScript execution, no login state, blocked by dynamic sites |
| **Browserbase** | Cloud-hosted remote sessions — must handle authentication per site; designed for scale, not for sharing the user's existing identity |
| **Direct REST API calls** | 99% of websites have no public API; this is the problem bb-browser solves |

---

## Use Cases

- **Cross-platform research** — agent searches arXiv, Twitter, GitHub, StackOverflow, Zhihu, and Reddit in parallel, all structured JSON, all authenticated
- **Finance agents** — agent monitors stock prices, hot stocks, and news on Xueqiu and Eastmoney using the user's real account data
- **Content aggregation** — agent pulls trending content from Bilibili, YouTube, Xiaohongshu, and LinkedIn feeds simultaneously
- **Job search agents** — agent searches BOSS Zhipin and LinkedIn with the user's actual account, seeing personalized results and salary estimates
- **Self-extending agent** — agent runs `bb-browser guide`, reverse-engineers a new website, writes an adapter, and submits a PR — entirely autonomously
- **Developer research** — agent queries npm, PyPI, GitHub issues, and StackOverflow from one tool call
