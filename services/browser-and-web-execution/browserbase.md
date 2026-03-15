# Browserbase

> **"A web browser for AI agents & applications."**

| | |
|---|---|
| **Website** | https://browserbase.com |
| **Docs** | https://docs.browserbase.com |
| **GitHub** | https://github.com/browserbase |
| **MCP** | https://www.browserbase.com/mcp |
| **Classification** | `agent-native` |
| **Category** | [Browser & Web Execution Services](README.md) |
| **Compliance** | SOC-2 Type I · HIPAA |

---

## What It Does

Browserbase provides managed, cloud-hosted headless browser infrastructure specifically for AI agents. Agents spin up isolated browser sessions via API, control them through Playwright, Puppeteer, or Selenium — or through the Stagehand SDK using natural-language web actions — and destroy them when done. The entire browser lifecycle is agent-controlled, with no human sitting at a keyboard.

---

## Why It Is Agent-Native

| Criterion | Evidence |
|---|---|
| **Agent-first positioning** | Homepage: *"A web browser for AI agents & applications"*; Stagehand SDK, MCP server, and agent integration guides are first-class products |
| **Agent-specific primitive** | Remote browser session with per-agent isolation; natural-language action via Stagehand (`"click the login button"`); session recording for agent trajectory audit |
| **Autonomy-compatible control plane** | Thousands of parallel sessions; stealth capabilities prevent bot detection; agents operate entirely without human intervention |
| **M2M integration surface** | REST API, Playwright/Puppeteer/Selenium driver, Chrome DevTools Protocol (CDP), MCP server |
| **Identity / delegation** | Per-session proxy and fingerprint configuration; session IDs enable per-agent audit |

---

## Primary Primitives

| Primitive | Description |
|---|---|
| **Remote Browser Session** | Isolated cloud browser instance created and destroyed via API |
| **Stagehand Actions** | Natural-language web commands (`act("click signup button")`, `extract(...)`) |
| **Session Recording** | Full replay of agent's browser actions for debugging and audit |
| **Stealth Mode** | Fingerprint randomization and proxy rotation to avoid bot detection |
| **Parallel Sessions** | Spin up thousands of simultaneous browser contexts in milliseconds |
| **MCP Server** | Direct LLM tool use via Model Context Protocol |

---

## Autonomy Model

1. Agent calls `POST /sessions` → receives a remote browser session endpoint
2. Agent connects via Playwright/CDP or Stagehand
3. Agent issues actions (navigate, click, extract, screenshot) without human involvement
4. Session is automatically recorded for later inspection
5. Agent calls `DELETE /sessions/{id}` when done

There is no human browser window. The agent is the only actor in the session.

---

## Identity and Delegation Model

- Each session is isolated — no shared state between agent sessions
- Proxy and fingerprint configuration is per-session, enabling agent-specific identity on the open web
- Session IDs provide per-agent attribution in logs
- API key authentication scopes access per project

---

## Protocol Surface

| Interface | Detail |
|---|---|
| REST API | Session lifecycle management (create, list, delete) |
| Playwright | Standard Playwright over CDP pointing to remote session |
| Puppeteer | Standard Puppeteer over CDP pointing to remote session |
| Selenium | Standard Selenium WebDriver pointing to remote session |
| Chrome DevTools Protocol | Low-level CDP access for custom tooling |
| Stagehand SDK | Natural-language action layer built on Browserbase |
| MCP Server | Model Context Protocol for direct LLM browser control |

---

## Human-in-the-Loop Support

None required by default. Session recordings can be reviewed by humans post-hoc for debugging. HumanLayer can be composed on top for approval gates on specific high-risk actions (e.g., before the agent submits a form with financial implications).

---

## Why Generic Alternatives Do Not Qualify

| Alternative | Why It Fails |
|---|---|
| **Local Playwright/Puppeteer** | Runs on developer's machine; no cloud scaling, no per-agent session isolation, no stealth, no agent-optimized SDK |
| **BrowserStack** | Built for human QA engineers running test suites; not designed for agent-initiated autonomous navigation at scale |
| **Selenium Grid** | Human test infrastructure; no natural-language action interface, no agent-oriented session management |
| **AWS Lambda + Chromium** | DIY infra with no agent-specific primitives; developer builds all session management, stealth, and recording from scratch |

---

## Use Cases

- **Web automation** — agents log in to third-party services, extract data, submit forms, take screenshots
- **Research agents** — agents navigate multi-step research workflows across multiple sites
- **Testing agents** — agents validate UI behavior as part of an agentic CI pipeline
- **E-commerce agents** — agents monitor prices, fill carts, complete checkouts on behalf of users
- **Data extraction** — agents navigate dynamic, JavaScript-rendered pages and extract structured information
