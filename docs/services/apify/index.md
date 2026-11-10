---
title: "Apify | Agent-Native Services"
service_name: "Apify"
description: "Get real-time web data for your AI"
permalink: /services/apify/
page_kind: service
service_slug: "apify"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/apify.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/apify.md"
tagline: "Get real-time web data for your AI"
website: "https://apify.com"
repository: "https://github.com/apify/crawlee"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://apify.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.apify.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/apify/crawlee" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/apify.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

[Browserbase](/services/browserbase/) hands an agent a browser session to drive step by step. Apify hands it a finished job: pick an Actor, pass input, and collect a structured dataset when the run ends.

### Actors, runs, datasets

The dossier calls Apify a web data platform. An Actor is a packaged scraper, crawler, or browser automation with defined inputs and outputs. Starting one creates a run, an execution instance with status, logs, and compute metering. Output lands in a dataset that can be exported as JSON or CSV. Around that core sit platform-managed proxies and anti-blocking options, plus schedules and webhooks for recurring pulls.

The homepage pitch, "Get real-time web data for your AI," targets agents that need fresh social, maps, e-commerce, or site content without running their own proxy and browser fleet. The dossier names the Website Content Crawler Actor as the route for turning sites into Markdown for retrieval pipelines. The size of the Actor marketplace changes; the current catalog is on Apify's site.

### Calling it from an agent

The primary surface is the REST API v2, described in the [Apify docs](https://docs.apify.com), with official clients installed as `npm install apify-client` or `pip install apify-client`. An API token is created in the Apify Console. The loop in the dossier is short: choose an Actor and input JSON, start a run, wait for it to finish or receive a webhook, then fetch dataset items into the agent's context.

For MCP, the dossier says only that Apify lists MCP client integrations on its integrations page and that REST plus SDK remain the main path. Agent Skill status is unknown; the dossier suggests community search.

### Jobs versus sessions

Within [Browser & Web Execution](/categories/browser-and-web-execution/), most neighbors give an agent a browser. [Steel](/services/steel/) and [Anchor Browser](/services/anchor-browser/) provide browser infrastructure the agent controls directly. [Browser Use Cloud](/services/browser-use-cloud/) adds AI-driven automation on managed browsers. Apify sits a level up: someone has already written the automation, and the agent consumes its output. That is efficient when an Actor exists for the target and limiting when the task needs judgement at each click. The [browser infrastructure guide](/guides/browser-infrastructure-for-agents/) lays out the same split.

Check a few things before an agent depends on it. Marketplace Actors have different authors, so look at who maintains the one you choose and how its output schema changes over time. Tokens scope to the account, so any agent holding one can start any Actor the account can. Runs are metered, and cost per run depends on the Actor; current pricing is on the vendor site. Target sites' terms of use remain your concern.

### Editor's take

Apify is well suited to research, lead-generation, and retrieval-ingestion agents that need structured data from common site types on a schedule, where an existing Actor already does the extraction. Agents that must log in, make decisions mid-flow, or handle unusual pages are better served by Browserbase or Steel. Everything above is drawn from the catalog dossier and Apify's documentation; no Actor runs were started in writing it.

</section>

## What it does

Apify is a **web data platform** for running **Actors** — serverless scrapers, crawlers, and browser automations that return **structured datasets** (JSON, CSV) through an **API**. The homepage explicitly targets **AI apps and agents** that need **fresh web data** (social, maps, e-commerce, generic site content) without operating their own proxy and browser farms.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, http, API
- **MCP:** ⚠️ Apify integrates with MCP clients (per integrations page); the primary surface remains REST + SDK.
- **Agent Skill:** ⚠️ Search community skills for Apify patterns.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
npm install apify-client
# or
pip install apify-client
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/apify.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | https://docs.apify.com/api/v2 |
| JavaScript | `apify-client` npm package |
| Python | `apify-client` PyPI |
| Console | https://console.apify.com |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
