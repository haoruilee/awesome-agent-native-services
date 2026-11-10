---
title: "Firecrawl | Agent-Native Services"
service_name: "Firecrawl"
description: "Turn any website into LLM-ready data"
permalink: /services/firecrawl/
page_kind: service
service_slug: "firecrawl"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/firecrawl.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/firecrawl.md"
tagline: "Turn any website into LLM-ready data"
website: "https://firecrawl.dev"
repository: "https://github.com/firecrawl/firecrawl"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://firecrawl.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.firecrawl.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/firecrawl/firecrawl" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/firecrawl.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

Fetching, rendering, and crawling happen on the vendor's machines. An agent sends a request to the hosted API with a key and gets back markdown or JSON. The dossier lists an open-source repository, but every path it documents goes through that API, so in practice the vendor runs the crawler and sees the URLs and prompts the agent sends. That is the trade for not keeping a headless browser alive on the agent's side.

### Endpoints by how much the agent decides

The vendor's wording is "Turn any website into LLM-ready data." The dossier sorts the work into endpoints, and they differ mainly in who picks the pages. With /scrape the agent names one URL and gets clean markdown or structured JSON. With /crawl it names a site and a depth. /map returns the URLs on a site as a structured graph. /extract applies a schema to one or many URLs. The /agent endpoint removes URLs entirely: the agent describes the data it wants in natural language, and Firecrawl decides which sources to search, how far to navigate, and what to pull, returning a structured result.

Each step down that list hands more judgment to the vendor. An agent that needs to cite exactly where a fact came from may prefer /scrape or /extract over /agent.

Integration paths are broad. The dossier names a REST API, a Python SDK installed with `pip install firecrawl-py` that accepts Pydantic schemas, a Node.js SDK installed with `npm install @mendable/firecrawl-js` that accepts Zod schemas, and an official MCP server over stdio that lives in the main repository. Its quickest path is the official Agent Skill, `npx skills add firecrawl/cli`, which teaches a coding assistant to scrape, search, crawl, map, and extract, and expects a `FIRECRAWL_API_KEY` in the environment. Details are in the [Firecrawl docs](https://docs.firecrawl.dev).

### Extraction beside live browsers

Inside [Browser & Web Execution](/categories/browser-and-web-execution/), Firecrawl is on the data side of the line. [Browserbase](/services/browserbase/) and [Steel](/services/steel/) provide a browser for an agent to drive, which is what a task needs when the outcome is a submitted form rather than text. [Apify](/services/apify/) is the closer neighbor, aimed at real-time web data. [Browser Use Cloud](/services/browser-use-cloud/) automates the clicking itself. The [browser infrastructure guide](/guides/browser-infrastructure-for-agents/) lays the two approaches side by side.

### Open questions in the docs

Auth is a single API key per integration. Check whether keys can be scoped or rotated per agent. The dossier describes /agent as a research preview whose cost depends on query complexity and a model choice, so read the current terms before handing it open-ended prompts. It does not describe a self-hosted deployment, what happens on sites behind a login, or how long the service keeps fetched content. Confirm all three if your agent touches anything private.

### Editor's take

Research and ingestion agents that want page content as model-ready text, and do not need to log in or press buttons, get the most from it. If the job ends in an action on a page, a live session from Browserbase or Steel fits better; if it is broad data collection with existing scrapers, compare Apify. Nothing in this note comes from sending Firecrawl a request; it is a reading of the dossier and the vendor docs.

</section>

## What it does

Firecrawl is a web extraction API that converts websites into clean, LLM-ready markdown or structured JSON. Its `/agent` endpoint goes further: agents describe *what data they need* in natural language — no URLs required. Firecrawl autonomously searches, navigates, and extracts across multiple sources in parallel, returning structured output directly consumable by an LLM.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skill published at firecrawl/cli
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | All endpoints (agent, scrape, crawl, extract, map) |
| Python SDK | `pip install firecrawl-py`; Pydantic schema support |
| Node.js SDK | `npm install @mendable/firecrawl-js`; Zod schema support |
| MCP Server | Model Context Protocol for direct LLM tool use |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
