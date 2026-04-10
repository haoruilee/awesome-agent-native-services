# Browser & Web Execution Services

> Services that give AI agents a **remote, managed browser runtime** — so agents can navigate, interact with, and extract data from the web as an autonomous actor, without any human operating a browser on their behalf.

## Why This Category Exists

The web was designed for humans sitting in front of browsers. AI agents that need to take web actions — filling forms, clicking buttons, logging in to services, extracting dynamic content — require a fundamentally different substrate than a headless library bolted onto a developer's laptop. Agent-native browser services provide:

- **Remote, cloud-hosted browser sessions** that agents spin up and tear down programmatically
- **Session isolation** so thousands of agents can run parallel browser contexts without interference
- **Natural-language web action** interfaces that map agent intent directly to browser actions
- **Session recording** for debugging and audit without human observation

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Browserbase](browserbase.md) | A web browser for AI agents & applications | REST, Playwright, Puppeteer, Selenium, CDP | ✅ |
| [Firecrawl](firecrawl.md) | Turn any website into LLM-ready data | REST, Python SDK, Node.js SDK | ✅ |
| [Bright Data Agent Browser](bright-data-agent-browser.md) | A cloud browser built for AI agents — with built-in website unlocking | REST API, AI SDK, MCP | ✅ |
| [bb-browser](bb-browser.md) | Your browser is the API — 103 commands across 36 platforms using your real login state | CLI, MCP server, HTTP daemon | ✅ |
| [OpenCLI](opencli.md) | Make any website, Electron app, or local tool your CLI — reuse Chrome login, structured output | CLI, Browser Bridge extension, npm `registry` export | ⚠️ |
| [Steel](steel.md) | Browser infrastructure for AI agents | Sessions API, Puppeteer/Playwright/Selenium connect, MCP | ✅ |
| [Notte](notte.md) | Browser infrastructure that lets AI run on the internet at speed | CDP sessions, web agents, vaults, notte-mcp | ✅ |
| [Skyvern](skyvern.md) [![⭐](https://img.shields.io/github/stars/Skyvern-AI/skyvern?style=social)](https://github.com/Skyvern-AI/skyvern) | AI agents to automate workflows on any website | Task API · Vision browser · 2FA/TOTP · Sessions · Structured extraction | ✅ |
| [Browser Use Cloud](browser-use-cloud.md) [![⭐](https://img.shields.io/github/stars/browser-use/browser-use?style=social)](https://github.com/browser-use/browser-use) | Managed stealth browsers, CAPTCHA, proxies — agent or CDP mode | `run()` NL tasks · Sessions · Profiles · Hosted MCP | ✅ |
| [Anchor Browser](anchor-browser.md) | The secure infrastructure for computer use agents | Web Action Cache · OmniConnect auth · MCP · SDKs | ✅ |
| [Hyperbrowser](hyperbrowser.md) [![⭐](https://img.shields.io/github/stars/hyperbrowserai/mcp?style=social)](https://github.com/hyperbrowserai/mcp) | Web infra for AI agents | Scrape/crawl/CUA tools · HyperAgent · MCP | ✅ |
| [AgentQL](agentql.md) [![⭐](https://img.shields.io/github/stars/tinyfish-io/agentql?style=social)](https://github.com/tinyfish-io/agentql) | Make the web AI-ready | AgentQL queries · Remote browser CDP · Browserless REST | ⚠️ |
| [Crawl4AI](crawl4ai.md) [![⭐](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social)](https://github.com/unclecode/crawl4ai) | Open-source LLM-friendly web crawler & scraper | LLM-ready markdown · Extraction · Docker · MCP | ✅ |
| [Cloudflare Browser Rendering](cloudflare-browser-rendering.md) [![⭐](https://img.shields.io/github/stars/cloudflare/workers-sdk?style=social)](https://github.com/cloudflare/workers-sdk) | Headless Chrome on Cloudflare for AI-driven browsing | Workers bindings · Playwright/Puppeteer · Playwright MCP · REST | ✅ |
| [Olostep](olostep.md) [![⭐](https://img.shields.io/github/stars/olostep/olostep-mcp-server?style=social)](https://github.com/olostep/olostep-mcp-server) | Web data API for AI agents — scrape, search, crawl, batch | REST API · Official MCP · Remote `mcp.olostep.com` | ✅ |
| [Lightpanda](lightpanda.md) [![⭐](https://img.shields.io/github/stars/lightpanda-io/browser?style=social)](https://github.com/lightpanda-io/browser) | Headless browser built for AI agents and automation | CDP server · `fetch` CLI (HTML/markdown) · Built-in MCP (stdio) | ✅ |
| [Apify](apify.md) [![⭐](https://img.shields.io/github/stars/apify/crawlee?style=social)](https://github.com/apify/crawlee) | Real-time web data for AI — Actor marketplace & API | REST API v2, JS/Python clients, webhooks, schedules | ⚠️ |

---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide **cloud-hosted browser or web-extraction sessions** that agents control via API.
2. Support **programmatic session lifecycle** — create, use, and destroy without human browser setup.
3. Return **agent-consumable output** — structured data, clean markdown, or action confirmations, not raw HTML for human reading.
4. Scale to **parallel agent sessions** — not a single shared browser instance.
