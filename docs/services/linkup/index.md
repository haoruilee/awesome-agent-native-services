---
title: "Linkup | Agent-Native Services"
service_name: "Linkup"
description: "Search API for AI agents and LLM apps"
permalink: /services/linkup/
page_kind: service
service_slug: "linkup"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/linkup.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/linkup.md"
tagline: "Search API for AI agents and LLM apps"
website: "https://www.linkup.so"
repository: "https://github.com/LinkupPlatform/linkup-python-sdk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.linkup.so" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.linkup.so" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/LinkupPlatform/linkup-python-sdk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/linkup.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

What the agent must already have is an API credential and either a REST client or the Python SDK. The dossier lists those two paths and nothing else: there is no standalone MCP server and no Agent Skill. An MCP-only host would need a wrapper.

### Results built for citation

The vendor's line is "Search API for AI agents and LLM apps." In the dossier, the service provides LLM-oriented web search and structured retrieval for citations and downstream reasoning. The primitives are a web search API, structured retrieval outputs, and citation-ready sources. The agent-native case rests on output shaped for machine consumption and context-window efficiency, as opposed to a results page built for clicks.

The documented loop is: create credentials, call search endpoints, feed the structured response into planning. API keys scope tenant and agent usage and support request attribution. Human review is about the citation chain: a person can inspect sources and override a decision.

The entry does not describe the response schema, search depth options, or how fresh the index is. Those details decide whether results fit your prompt budget, and they live in the [Linkup docs](https://docs.linkup.so). The [Python SDK repository](https://github.com/LinkupPlatform/linkup-python-sdk) is the dossier's GitHub link.

### Sources versus answers

[Search & Web Intelligence](/categories/search-and-web-intelligence/) holds two kinds of service that are easy to confuse. Some return sources for the agent to read. Others return a researched answer. Linkup's dossier is firmly the first kind: retrieval and citations, with synthesis left to your model. [Jina DeepSearch](/services/jina-deepsearch/) lists a deep research synthesis primitive, which moves reasoning to the vendor. [Tavily](/services/tavily/) and [Exa](/services/exa/) are the closest comparisons as general agent search APIs; read their entries for how each frames retrieval.

Keeping synthesis on your side means your agent sees every source and decides what to trust. It also means more tokens spent reading. For a narrower job, [Context7](/services/context7/) targets current library documentation rather than the open web. The [agent-native guide](/guides/what-makes-a-service-agent-native/) covers why compact, structured output counts as an agent-first property.

### Things to confirm with Linkup

Check how keys map to tenants if several agents share an account, since attribution depends on it. Confirm what a citation contains: a URL alone, or a URL with the supporting passage. Look for documented behavior when a query returns nothing useful, so the agent can tell an empty result from a failure. Pricing and quota are on the vendor site.

### Editor's take

Linkup is a sensible pick for a Python or REST agent that wants sources it can quote and prefers to do its own synthesis. If you want the service to produce the research summary, look at Jina DeepSearch. If your agent writes code against libraries, Context7 is more targeted. The judgement comes from the dossier and Linkup's public documentation; the project has not issued queries against the API.

</section>

## What it does

Provides LLM-oriented web search and structured retrieval suitable for citations and downstream agent reasoning.

## Agent-facing interfaces

- **Catalog protocols:** REST, SDK, API
- **MCP:** ⚠️ No standalone official MCP server package.
- **Agent Skill:** ⚠️ No official AgentSkills package found.
- **Onboarding type:** `other`

## Protocol surface

REST API + Python SDK.

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
