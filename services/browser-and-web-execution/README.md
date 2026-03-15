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

---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide **cloud-hosted browser or web-extraction sessions** that agents control via API.
2. Support **programmatic session lifecycle** — create, use, and destroy without human browser setup.
3. Return **agent-consumable output** — structured data, clean markdown, or action confirmations, not raw HTML for human reading.
4. Scale to **parallel agent sessions** — not a single shared browser instance.
