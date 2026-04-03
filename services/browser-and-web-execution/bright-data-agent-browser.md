# Bright Data Agent Browser

> **"A cloud browser built for AI agents — with built-in website unlocking."**

| | |
|---|---|
| **Website** | https://brightdata.com/ai/agent-browser |
| **Docs** | https://docs.brightdata.com/ai/agents |
| **GitHub** | https://github.com/brightdata/ai-sdk |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **Scale** | 150M+ proxy IPs · 195 countries · 1M+ concurrent sessions |

---

## Official Website

https://brightdata.com/ai/agent-browser

---

## Official Repo

https://github.com/brightdata/ai-sdk — AI SDK for Vercel AI SDK integration

---

## Agent Skills

**Status:** ⚠️ No official skill published by Bright Data yet.

```bash
npx clawhub@latest search brightdata
```

---

## MCP

**Status:** ✅ Available (Web MCP — free tier available)

Bright Data provides a Web MCP server enabling agents to perform web searches, scraping, and data collection directly through the Model Context Protocol.

| Detail | Value |
|---|---|
| **MCP Page** | https://brightdata.com/mcp |
| **Transport** | stdio |
| **Compatible Clients** | Claude Desktop, Cursor, any MCP-compatible client |

---

## What It Does

Bright Data Agent Browser is a cloud-hosted browser automation platform designed specifically for AI agents, combining browser infrastructure with **built-in website unlocking** — fingerprinting, CAPTCHA solving, and bot-detection evasion handled transparently. Agents spin up parallel browser sessions via API or MCP, navigate dynamic sites, and extract data at scale without building any unlocking infrastructure themselves.

Unlike general headless browsers, Bright Data's unlocking layer covers 3M+ domains and is continuously updated against anti-bot measures — solving the most common reason agent web automation fails in production.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Dedicated product page: *"Agent Browser for AI Agents"*; *"Agent Web Access"* is a distinct product line with AI-agent-specific docs |
| **Agent-specific primitive** | Built-in unlocking (fingerprinting + CAPTCHA) as a first-class infrastructure layer; unlimited parallel sessions; MCP server for direct LLM tool use; `@brightdata/ai-sdk` for Vercel AI SDK |
| **Autonomy-compatible control plane** | Agents manage session lifecycle via API; unlocking is transparent; 99.99% uptime; sub-second responses |
| **M2M integration surface** | REST API, `@brightdata/ai-sdk` (npm), MCP server, Playwright/Puppeteer/Selenium-compatible |
| **Identity / delegation** | Per-session identity (fingerprint randomization); proxy rotation per session; API key scoped per project |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Agent Browser Session** | Cloud browser session with automatic anti-bot bypass and fingerprint management |
| **Built-in Unlocking** | Automatic CAPTCHA solving, fingerprinting, and bot-detection evasion covering 3M+ domains |
| **Parallel Sessions** | Auto-scale to unlimited concurrent browser sessions |
| **Web MCP** | Model Context Protocol server for direct LLM browser control and data collection |
| **AI SDK** | `@brightdata/ai-sdk` — ready-made Vercel AI SDK tools for scraping, searching, and structured data collection |
| **Proxy Network** | 150M+ IPs across 195 countries integrated transparently into browser sessions |

---

## Autonomy Model

```
Agent calls Bright Data API to create a browser session (or uses MCP tool)
    ↓
Session spawns with automatic fingerprint and proxy configuration
    ↓
Agent navigates to target site — unlocking layer handles bot detection transparently
    ↓
Agent extracts data or takes actions
    ↓
Session destroyed; data returned as structured output
```

No human manages CAPTCHA solving or proxy rotation. Agents operate at scale without anti-bot failures.

---

## Identity and Delegation Model

- Per-session proxy identity (IP address from the Bright Data residential/datacenter network)
- Fingerprint randomization per session prevents tracking across agent requests
- API key scoped per project; per-session audit logs available

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Session management, scraping endpoints, data collection APIs |
| Playwright/Puppeteer/Selenium | Standard drivers pointing at Bright Data's cloud browser |
| `@brightdata/ai-sdk` | Vercel AI SDK tools for scraping, searching, structured extraction |
| Web MCP | Model Context Protocol for LLM direct control (free tier available) |
| Proxy API | Direct proxy network access for custom tooling |

---

## Human-in-the-Loop Support

None required. Bright Data handles all unlocking autonomously. Session recordings are available for debugging.

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Self-hosted Playwright/Puppeteer** | Browser automation only; agents must build and maintain their own proxy, fingerprinting, and CAPTCHA bypass layers |
| **Generic proxy providers** | Provide IP rotation, but not a full browser runtime with integrated unlocking and MCP-facing agent controls |
| **Human-oriented scraping SaaS** | Often optimized for dashboard-led usage, not agent-managed session lifecycle and direct LLM/MCP integration |

## How It Differs from Browserbase

Both qualify as agent-native browser services, but they address different problems:

| Dimension | Browserbase | Bright Data Agent Browser |
|---|---|---|
| Core primitive | Remote browser session + Stagehand NL actions | Cloud browser + built-in unlocking across 3M+ domains |
| Anti-bot handling | Stealth mode (fingerprint randomization) | Full unlocking infrastructure (CAPTCHA, fingerprinting, proxy network) |
| Proxy network | Configurable proxy | 150M+ IPs across 195 countries built-in |
| Primary strength | NL web automation (Stagehand SDK) | Data collection at scale from blocked/anti-bot sites |

---

## Use Cases

- **Data collection at scale** — agent collects pricing, inventory, or review data from sites that aggressively block bots
- **Competitor monitoring** — agent tracks competitor product pages across thousands of sites without CAPTCHA failures
- **News and content aggregation** — agent fetches articles from dynamic, JavaScript-rendered news sites at scale
- **E-commerce agents** — agent monitors availability and prices across retailer sites with strong anti-bot measures
- **Research agents** — agent gathers structured data from paywalled or restricted sources via residential proxy rotation
