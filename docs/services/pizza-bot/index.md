---
title: "Pizza Bot | Agent-Native Services"
service_name: "Pizza Bot"
description: "Pizza Bot is an inbox for long-running AI work"
permalink: /services/pizza-bot/
page_kind: service
service_slug: "pizza-bot"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/pizza-bot.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/pizza-bot.md"
tagline: "Pizza Bot is an inbox for long-running AI work"
verified_at: "2026-09-20"
website: "https://github.com/pizza-bot-app/pizza-bot"
repository: "https://github.com/pizza-bot-app/pizza-bot"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · SDK · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-20</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/pizza-bot-app/pizza-bot" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/pizza-bot-app/pizza-bot/blob/main/docs/RUNNING.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/pizza-bot-app/pizza-bot" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/pizza-bot.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Pizza Bot is a local-first inbox for long-running AI agents. Start or schedule a task, leave, and let completed work collect in **Unread** while runs waiting for a decision collect in **Action**. Agents keep working when the UI navigates away or disconnects; the api-server process must remain running.

The runtime is a stateful DeepAgents / LangGraph graph. Desktop, web, and terminal clients all talk to the same api-server over HTTP/SSE. Checkpointed runs survive client disconnects. Cron or webhook triggers can start work without an open conversation. Skills become tool-scoped specialist subagents whose progress appears in the Activity panel.

**Human UI honesty:** the desktop/web inbox is an approval and review surface, not the primary worker. The agent loop runs in the api-server. Humans grant folders, configure providers, and decide Action-queue approvals.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + HTTP/SSE api-server (desktop, browser, or terminal)
- **Catalog protocols:** CLI, SDK, http, API
- **MCP:** ⚠️ Not published as an installable MCP *server* product.
- **Agent Skill:** ⚠️ Not published as a standalone npx skills add pack for this catalog entry.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI + HTTP/SSE api-server (desktop, browser, or terminal)

```bash
git clone https://github.com/pizza-bot-app/pizza-bot.git
cd pizza-bot
npm install
npm run build
npm run dev
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/pizza-bot.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP/SSE api-server | Hono Agent Protocol routes; clients use `@langchain/langgraph-sdk` |
| Electron desktop | Local inbox; forks and supervises the api-server |
| Browser UI | Vite / static deployment against a running backend |
| CLI | `npm run shell` or packaged `pizza` HTTP client |
| Standalone backend | Docker, Compose, Kubernetes — [backend guide](https://github.com/pizza-bot-app/pizza-bot/blob/main/docs/STANDALONE_BACKEND.md) |
| MCP host | Operator-configured servers via UI or `.mcp.json` |
| Agent Skills | `<PIZZA_DATA_ROOT>/skills`, Built-in, and Plugin packs |

---

## Verification

Last verified **2026-09-20**.

Sources:
- https://news.ycombinator.com/item?id=49713894

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
