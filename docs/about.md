---
layout: default
title: "About"
description: "What The Agent-Native Index is, who maintains it, and how a service gets listed."
permalink: /about/
page_kind: document
ads: false
---

The Agent-Native Index is a public catalog of infrastructure built so that an AI agent can be the caller. The site at [theagentnative.com](https://theagentnative.com/) is the reading version of that catalog. The source is the Git repository [haoruilee/awesome-agent-native-services](https://github.com/haoruilee/awesome-agent-native-services).

It is a directory with an argument. The argument is that "works with AI" is not a useful category. A human product that later grew an agent tab, a plugin, or an MCP server is a different kind of thing from a service whose inbox, browser session, wallet, or sandbox only makes sense if the caller is an agent. The index exists to keep those apart, and to write down the difference in a place an agent can read as well as a person.

## Who maintains it

The repository is published under the GitHub account [haoruilee](https://github.com/haoruilee). That is the maintainer of record. This site does not name a company, because the repository does not publish one. It does not publish a personal biography, a client list, or a contact email. Questions and corrections go to the public issue tracker, which is also how the privacy policy tells visitors to reach the project.

Contributions are licensed [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/), the same dedication stated in the repository license and in [CONTRIBUTING.md](https://github.com/haoruilee/awesome-agent-native-services/blob/main/CONTRIBUTING.md). CC0 means the catalog text is dedicated to the public domain to the extent the law allows. It does not transfer anyone else's trademarks, and it does not make a listed vendor's documentation public domain. Service names belong to whoever owns them. The dossiers quote public pages so a reader can see why a listing passed.

## How a listing is chosen

A service enters the main list only when it passes a written admission track. The usual track is five tests, all required. The contribution guide states them in full. In short:

1. The official site or docs name AI agents as the primary consumer, not as a footnote.
2. The API exposes a primitive that has no meaningful human equivalent. An agent inbox is one. A generic CRUD API that an agent happens to call is not.
3. An agent can finish the loop this service provides without a person clicking each step, while constraints such as budgets, isolation, or approval gates still exist.
4. The primary interface is a machine one: an SDK, an HTTP API, an MCP server, a webhook, or a structured CLI. A dashboard may exist. It must not be required for the agent to operate.
5. Where the service acts outward, it distinguishes the agent from the user, models what the agent is allowed to do, and can attribute an action to that agent.

There is a narrow second track for operator surfaces. A human-facing view can qualify when it is built to operate live agents, continuously reads agent-specific state such as a session, tool calls, or context pressure, attributes that state to a session, and exposes a dedicated operational surface. Generic dashboards and terminal themes do not qualify. The exception is narrow on purpose. It is not a door for products that were built for people and later added an agent panel.

Everything else waits outside. Agent builders, where a person assembles the agent, are out. RAG studios, chat workspaces, and no-code bot products are out. Agent-adapted services, the ones that were human products first, are recorded in an excluded section of the repository README when they are useful as boundary cases. They are not wrong. They are in the wrong list. The guide [What makes a service agent-native](/guides/what-makes-a-service-agent-native/) walks through the tests with the examples the contribution guide already uses.

New services need a proposal issue and a maintainer's go-ahead before a pull request. That rule is in the contribution guide, along with the evidence each proposal has to include: a quote from the vendor's own site, and the URL of that quote. The editorial policy explains how updates, removals, and conflicts of interest work. There is no paid placement program in the repository. A listing is not for sale.

## How to read the site

The home page is an edition: new arrivals, sixteen collections, and a machine entrance. Each collection page explains what that group of services is for, what usually separates the entries, and where the trade-off sits. The cards under that essay are generated from the dossiers. A card's title links to the vendor when the catalog has an official URL. "Introduction" opens this site's short page for that service. "Dossier" opens the full evidence file on GitHub.

The introduction pages are summaries. They copy fields the dossier already states: what the service does, which interfaces the catalog recorded, and how an agent is supposed to start. They are not a second review, and they are not a test report. When a page and a vendor's docs disagree, the vendor's docs are the current product, and the dossier is the claim this index is willing to repeat. File an update if the dossier has fallen behind.

The [guides](/guides/) are original essays. They compare approaches using the services this catalog actually lists, and they link the vendor documentation for factual claims. They do not add prices, benchmarks, or hands-on results that the dossiers do not contain.

## For agents

A person can browse. An agent is expected to start from a document:

```
Read https://theagentnative.com/skill.md then find services designed for you natively.
```

[skill.md](/skill.md) is the task-oriented index. [catalog.json](/catalog.json) is the versioned record, with a [JSON Schema](/catalog.schema.json). [llms.txt](/llms.txt) is a short link list. Those files are generated from the same dossiers as the site. The guides and these about pages are written for human readers and are ordinary HTML.

## What this site will not do

It will not rank services by a score this project invented. It will not claim that one sandbox starts faster than another unless a cited document says so, and even then the sentence will say whose number it is. It will not take a fee to add, remove, or bury a listing. It does not operate the products it links to, and it does not hold accounts on them.

The [privacy policy](/privacy/) describes the static site, the host, and the advertising tags. Advertising is not enabled. The AdSense loader is present for account verification. That is a property of the site, not of the catalog's selection rules.
