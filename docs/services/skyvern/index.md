---
title: "Skyvern | Agent-Native Services"
service_name: "Skyvern"
description: "AI agents to automate workflows on any website"
permalink: /services/skyvern/
page_kind: service
service_slug: "skyvern"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/skyvern.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/skyvern.md"
tagline: "AI agents to automate workflows on any website"
website: "https://www.skyvern.com"
repository: "https://github.com/Skyvern-AI/skyvern"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · openapi · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.skyvern.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.skyvern.com/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Skyvern-AI/skyvern" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/skyvern.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

Two operating models sit behind the same request. With Skyvern Cloud, the vendor runs the browsers and the models behind a production API. With the open-source stack, a team self-hosts on Docker or Kubernetes and brings its own LLM keys. The agent sends a plain-language goal either way, but the self-hosted path moves model spend, browser upkeep, and stored credentials onto your own staff.

### A prompt in, a run out

The dossier describes vision-driven browser automation. An agent states a goal; Skyvern drives a real browser, plans its actions, and works through forms, logins, downloads, and extraction without XPath-only scripts. The unit is a task run. Its required field is a prompt, and the optional fields include a starting URL, an engine choice between Skyvern's own agent and computer-use backends, a JSON Schema for the output, and a browser session ID for state that carries across runs.

On the cloud, that request is `POST https://api.skyvern.com/v1/run/tasks` with an `x-api-key` header, as printed in the dossier. Python and TypeScript SDKs wrap the same API, and the [Skyvern docs](https://www.skyvern.com/docs) describe an MCP-ready integration for Claude Desktop, Cursor, Windsurf, and other hosts. Results come back as structured output plus screenshots, recordings, and downloads, with an optional webhook on completion. For Agent Skills, the dossier found no official entry and points to a community registry search, `npx clawhub@latest search skyvern`.

### Goal-driven versus session-driven

Most of the [Browser & Web Execution](/categories/browser-and-web-execution/) listings hand an agent a browser and expect it to drive. [Browserbase](/services/browserbase/) and [Steel](/services/steel/) are that kind of infrastructure: the session is the product, and the planning stays in the caller's model. Skyvern takes the planning in-house, which means the calling agent gives up step-level control in exchange for a single call. [Browser Use Cloud](/services/browser-use-cloud/) is the nearest comparison, another managed AI automation layer. [Apify](/services/apify/) points the other way, toward web data rather than completed workflows. The [browser infrastructure guide](/guides/browser-infrastructure-for-agents/) covers the wider split.

### What to confirm first

Credentials deserve the most attention. The dossier describes a credentials vault and TOTP delivery by push or URL so that logins happen without secrets in prompts. Read the credentials docs to learn where those secrets are stored on the cloud, how a self-hosted install stores them, and who can read run recordings that may show logged-in pages.

The API key scopes access to an account or project; check whether finer scopes exist. Engine choice changes which model provider sees page content, so confirm what each engine sends where. Proxy and geo targeting, CAPTCHA handling, and workflow features are listed but not specified in detail, so test them against your own target sites.

### Editor's take

Back-office agents that file the same portal forms or pull the same invoices from many vendor sites are a good match, especially when a schema-shaped result is what the caller wants. An agent that needs fine control over each click is better served by a raw session from Browserbase or Steel. Our view rests on the catalog dossier and Skyvern's published API reference; no task has been submitted from this project.

</section>

## What it does

Skyvern runs **vision-driven browser automation**: an agent describes a goal in natural language; Skyvern drives a real browser, plans actions, and completes multi-step workflows (forms, logins, downloads, structured extraction) without brittle XPath-only scripts. It supports **CAPTCHA handling**, **2FA/TOTP** flows, **geo-targeted proxies**, **persistent browser sessions**, **JSON-schema extraction**, **webhooks**, and **recordings** for audit. **Skyvern Cloud** offers a production API; the core stack is **open source** for self-hosting.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK / REST + optional MCP
- **Catalog protocols:** Agent Skill, MCP, REST, SDK, openapi, http, API
- **MCP:** ✅ Documented as MCP-ready — see Skyvern docs integrations section.
- **Agent Skill:** ⚠️ No single official npx skills add … registry entry documented as primary path.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK / REST + optional MCP

```bash
curl -X POST https://api.skyvern.com/v1/run/tasks \
  -H "x-api-key: $SKYVERN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Find the top 3 posts on Hacker News", "url": "https://news.ycombinator.com"}'
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/skyvern.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | `https://api.skyvern.com` — OpenAPI-linked from docs |
| Python SDK | https://www.skyvern.com/docs/sdk-reference/overview |
| TypeScript SDK | https://www.skyvern.com/docs/ts-sdk-reference/overview |
| Self-hosted | Docker / K8s — own LLM keys |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
