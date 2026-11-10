---
title: "Exa | Agent-Native Services"
service_name: "Exa"
description: "The search engine designed for AI"
permalink: /services/exa/
page_kind: service
service_slug: "exa"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/exa.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/exa.md"
tagline: "The search engine designed for AI"
website: "https://exa.ai"
repository: "https://github.com/exa-labs/exa-py"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://exa.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.exa.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/exa-labs/exa-py" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/exa.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

Retrieval happens inside a search engine the vendor builds and hosts, ranked by embeddings rather than keyword matching. The agent sends a query with an API key and receives parsed text. Because the engine is the vendor's, what an agent can find is whatever that engine returns, and the dossier says nothing about how broad or fresh it is. That is a different dependency from a service that fetches a live page on request.

### Neural search, contents, answers, Websets

The vendor's wording is "The search engine designed for AI." The dossier lists the primitives. Neural search retrieves documents by meaning, which it presents as an advantage on entity-heavy queries about specific people, companies, or research topics. Contents returns the full clean text of results. Answer synthesizes a reply from several sources. Websets builds structured datasets of entities from search. A separate corpus, `exa-code`, holds code and documentation for coding agents that want examples without spending tokens on whole pages.

The documented quickest path is the Python SDK: `pip install exa-py`, then `exa.search(query)`. A JavaScript and TypeScript SDK is in the exa-labs organization. The dossier lists native tool integrations for LangChain, CrewAI, LlamaIndex, and Mastra, and an official MCP server, exa-mcp-server, over stdio for Claude Desktop, Cursor, Windsurf, and Mastra. Agent Skills are the weak spot. Exa has not published an official one; the dossier points to a community-maintained exa-search skill installable from the LobeHub marketplace or a playbooks registry, with an `EXA_API_KEY` in the environment. Treat it as third-party code. The [Exa docs](https://docs.exa.ai) are the reference.

### Semantic ranking among search APIs

In [Search & Web Intelligence](/categories/search-and-web-intelligence/), several neighbors also return text instead of links. [Tavily](/services/tavily/) offers search plus extraction, crawl, and research endpoints under one key, a broader toolbox where Exa's dossier emphasizes the ranking model. [Jina DeepSearch](/services/jina-deepsearch/) is built around agentic deep research. [Context7](/services/context7/) overlaps with `exa-code` by serving up-to-date docs to coding agents, but it is a narrower source. [Agent Search MCP](/services/agent-search-mcp/) is a Node.js MCP server and CLI that covers English and Chinese search. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why LLM-ready output is part of the bar.

### What the dossier leaves out

Identity is an API key per integration, which the dossier calls sufficient because Exa only returns results and takes no action on a user's behalf. That narrow delegation is a fair point in its favor. Still, check whether keys can be separated per agent or per environment for cost tracking.

The accuracy comparison in the dossier is the vendor's own claim; evaluate it against your queries. The dossier also does not describe index coverage, recency controls beyond what the community skill mentions, query retention, or how Websets are built and kept current. Read the docs on each before building a pipeline around them.

### Editor's take

Research agents hunting for specific companies, papers, or people, where keyword search returns noise, are the best case for it. If your agent mostly needs to read particular pages or crawl a site, Tavily's extraction endpoints are closer to the job, and a coding agent that only needs library docs may find Context7 enough. No query has gone through Exa from this project; the opinion is formed from the catalog dossier and the docs Exa publishes.

</section>

## What it does

Exa is a neural search engine that retrieves semantically relevant web content using embeddings rather than keyword matching. Its output is clean, parsed text ready for LLM consumption — not SERP links. Where keyword search fails on complex entity queries (specific people, companies, research topics), Exa's semantic model returns 20× more accurate results. The `exa-code` product specifically targets coding agents with token-efficient code and documentation retrieval.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Community skills available; no official SKILL.md published by Exa yet
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | Search, contents, answer, websets endpoints |
| Python SDK | `exa-py` package |
| LangChain | Native tool integration |
| CrewAI | Native tool integration |
| LlamaIndex | Native tool integration |
| Mastra | Native integration |
| MCP | Model Context Protocol server |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
