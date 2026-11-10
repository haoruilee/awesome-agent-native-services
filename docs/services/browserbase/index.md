---
title: "Browserbase | Agent-Native Services"
service_name: "Browserbase"
description: "A web browser for AI agents & applications"
permalink: /services/browserbase/
page_kind: service
service_slug: "browserbase"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/browserbase.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browserbase.md"
tagline: "A web browser for AI agents & applications"
website: "https://browserbase.com"
repository: "https://github.com/browserbase/stagehand"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://browserbase.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.browserbase.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/browserbase/stagehand" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browserbase.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

[Apify](/services/apify/) sells finished extraction jobs: an Actor runs and returns a dataset. Browserbase sells the browser itself, a remote headless session that the agent drives one action at a time and throws away when it is done.

### Remote sessions and Stagehand

The dossier describes managed, cloud-hosted headless browsers for agents. A session is created through the API, controlled, and deleted, with isolation between sessions and no shared state. Control can be low level, through Playwright, Puppeteer, Selenium, or the Chrome DevTools Protocol pointed at the remote session, or high level through the Stagehand SDK, which accepts natural-language actions. The dossier shows `act("click signup button")` and `extract(...)` as examples.

Two features sit around the session. Recording captures a full replay of the agent's actions for debugging and audit. Stealth mode randomizes fingerprints and rotates proxies to avoid bot detection, and proxy and fingerprint settings are configurable per session. The dossier makes claims about how many sessions run in parallel and how fast they start; current figures are in the vendor docs.

### Drivers, MCP, and skills

Because the session speaks standard browser protocols, existing Playwright or Puppeteer code mostly needs a new connection target. The REST API handles lifecycle; the dossier's loop begins with `POST /sessions` and ends with `DELETE /sessions/{id}`. The [Browserbase docs](https://docs.browserbase.com) describe each driver.

An official MCP server lets an LLM control remote sessions directly over stdio or Streamable HTTP. The quickest documented path is the official skill set, `npx skills add browserbase/skills`, which includes a `browser` skill for CLI automation with stealth, CAPTCHA solving, and residential proxies, and a `functions` skill for deploying serverless browser automations to Browserbase's cloud. API keys scope access per project.

### Recordings, stealth, and responsibility

In [Browser & Web Execution](/categories/browser-and-web-execution/), [Steel](/services/steel/) also offers browser infrastructure for agents and is the closest comparison. [Anchor Browser](/services/anchor-browser/) aims at computer-use agents, and [Vercel Agent Browser](/services/agent-browser/) is a browser automation CLI. The [browser infrastructure guide](/guides/browser-infrastructure-for-agents/) covers how to choose among session providers.

A careful adopter has questions the dossier leaves open. Recordings capture what the agent typed, which can include credentials, so find out how long they are kept and who can view them. Stealth, CAPTCHA solving, and residential proxies change how a site sees your traffic, and the target site's terms still apply. Keys are per project, so attributing an action to a particular agent depends on tracking session IDs yourself. Check session time limits too.

The dossier also notes that [HumanLayer](/services/humanlayer/) can be added for approval gates before high-risk actions, such as submitting a form with financial consequences. Browserbase itself does not require a human by default.

### Editor's take

Browserbase is the natural choice for agents that must log in, click, and fill forms on script-heavy sites, especially for teams already writing Playwright who want sessions off their own machines. If the data comes from a common site type and someone has already built the scraper, Apify is less work. The account here is based on the dossier and Browserbase's documentation, without a session ever being opened.

</section>

## What it does

Browserbase provides managed, cloud-hosted headless browser infrastructure specifically for AI agents. Agents spin up isolated browser sessions via API, control them through Playwright, Puppeteer, or Selenium — or through the Stagehand SDK using natural-language web actions — and destroy them when done. The entire browser lifecycle is agent-controlled, with no human sitting at a keyboard.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skills published at browserbase/skills
- **Onboarding type:** `agent-skill`

## Protocol surface

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

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
