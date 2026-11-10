---
layout: default
title: "Browser infrastructure for agents compared"
description: "Hosted browser sessions, local engines, extraction APIs, and browsers that keep a login between tasks."
permalink: /guides/browser-infrastructure-for-agents/
page_kind: document
ads: false
guide_order: 3
---

"Give the agent a browser" hides a choice about whose browser, what it is allowed to keep, and whether anyone has to click. The [browser collection](/categories/browser-and-web-execution/) contains hosted sessions, engines you run, extraction APIs, and desktops that remember a login. They share a page because an agent is the driver or the reader. They do not share an architecture. Choosing as if they did produces a design that scrapes when it needed to click, or clicks when it needed a document back.

A useful split is the job, not the logo.

**Operate a live page.** Forms, buttons, multi-step flows, a session cookie that has to exist for the next click. Something has to be a browser.

**Read a site into context.** You need the text, the structure, or a JSON object, and you do not need to be logged in as a particular person. Fetching HTML and hoping is how agents waste a context window. An extraction API is built to return the other thing.

**Continue as a user who is already logged in.** The cookie is the point. A fresh cloud browser does not have it. A browser on the person's machine might.

Stealth, proxies, and CAPTCHA solving show up in several dossiers as vendor features. This guide does not score them. Sites change the checks. A vendor's current docs are the claim. A catalog essay is not a field test.

## Hosted sessions

[Browserbase](https://browserbase.com) is the sentence the contribution guide uses for this category: "A web browser for AI agents & applications." The [docs](https://docs.browserbase.com) and the dossier describe isolated cloud sessions, control through Playwright, Puppeteer, Selenium, or CDP, and Stagehand for natural-language actions on a page. Session recordings are there so a person can replay what the agent did. An MCP server is documented. The primitive is the session: create it, drive it, throw it away. The agent does not provision a virtual machine first.

[Steel](https://steel.dev) is the same shape, with a Sessions API and a one-line connect change from a local Playwright or Puppeteer launch, as the dossier puts it. Steel can be cloud or self-hosted. That option matters if the pages you touch cannot leave your network. The dossier emphasizes fast session startup as a product property. The figure, if you need one, belongs in the [Steel docs](https://docs.steel.dev), which are updated when the product is. This page will not freeze a number.

[Browser Use Cloud](https://browser-use.com) documents two modes. One is an agent mode: a natural-language task via `run()` or a session. The other is a browser mode that hands back CDP so your own agent drives. The dossier also describes stealth browsers, CAPTCHA handling, and residential proxies, and a hosted MCP server. Use agent mode when you want their loop. Use CDP when you already have a loop and only need the browser. Mixing those up is how people debug the wrong layer.

[Anchor Browser](https://www.anchorbrowser.io), [Hyperbrowser](https://www.hyperbrowser.ai), [Notte](https://www.notte.cc), and [Bright Data's agent browser](https://brightdata.com/ai/agent-browser) are further hosted sessions in the same collection, each with its own docs for auth, proxies, or extraction. [Kernel](https://www.kernel.sh/) describes sandboxed Chromium, Playwright or CDP, replay, and pools. Kernel's materials advertise a cold-start time. Treat that as their claim and read the current [docs](https://www.kernel.sh/docs/reference/mcp-server). This index has not reproduced it.

[Cloudflare Browser Rendering](https://developers.cloudflare.com/browser-rendering/) is hosted in a different sense. It is headless Chrome on Cloudflare's network, with Playwright and Puppeteer, REST, and a Browser Run path inside the Agents SDK where the model writes CDP-oriented code. You are already in that platform or you are not. It is a poor comparison against a standalone browser vendor if the rest of the agent is not on Workers, and a natural one if it is.

What these share is a session that is not your laptop. Parallel work is a consequence: each task can have its own cookies and fingerprint. What they do not share is your user's existing login. A fresh session is anonymous until the agent logs in, and logging in may be exactly what the site is trying to stop. Plan for that before you pick a vendor for the latency.

## Engines and MCP servers you run

[Playwright MCP](https://playwright.dev/docs/getting-started-mcp) exposes browser automation as MCP tools. The dossier's point is the accessibility snapshot: the agent reads structure and acts, instead of interpreting a screenshot as the only view. It is a server from the Playwright project, not a hosted fleet. You supply the browser it drives. That is a good first integration for a coding agent on a machine you control, and a weak answer for a production fleet of untrusted tasks.

[Lightpanda](https://lightpanda.io) is a headless browser written for automation, not a Chromium build. It speaks CDP so Puppeteer can connect, and it has a fetch mode that dumps HTML or markdown plus a built-in MCP server. [Obscura](https://obscura.sh) is another from-scratch headless browser in the collection, with CDP and MCP. [Moli](https://browser.lexmount.com) is described as a structured-first engine: a Rust CLI, MCP, CDP, and a semantic tree rather than only pixels. The reason to pick an engine like this is resource use and a snapshot the model can read. The reason to hesitate is compatibility. A browser that is not Chrome will not match Chrome on every site. The vendor docs are where known gaps should be, and you should look for them before you bet a workflow on a page that only renders correctly in one engine.

[CamoFox](https://github.com/jo-inc/camofox-browser), [Vessel](https://github.com/unmodeled-tyler/vessel-browser), and the various stealth MCP servers in the collection are local or self-driven browsers with their own claims about detection. Read those claims as claims. A local process that can click can also act as the user whose profile it loaded. That is the next section's problem, whether or not the project uses the word stealth.

## Extraction without a click

[Firecrawl](https://firecrawl.dev) turns sites into markdown or JSON. The dossier describes an `/agent` endpoint where the caller says what data it wants, without supplying every URL. That is a research loop, not a session you can click around in after the call returns. [Crawl4AI](https://crawl4ai.com) is the open-source crawler in the same collection, with LLM-oriented markdown and an MCP server. [Olostep](https://www.olostep.com) and [Apify](https://apify.com) are web-data APIs, Apify as an actor platform. [AgentQL](https://agentql.com) is a query language over pages, with a remote browser in its dossier, so it straddles extraction and a session.

Use this family when the output is a document the model will quote. Use a session when the output is a side effect on a site: a submitted form, a changed setting, a downloaded file that only exists after a click. Agents that "browse" by calling an extraction API will report success on tasks that never happened, because the API did the reading and nothing else. Agents that open a full browser to fetch a public documentation page pay for a session they did not need. The [search collection](/categories/search-and-web-intelligence/) is a third option when you do not even have a URL yet.

## Browsers that remember

[Hronaut](https://hronaut.dev/) is a visible desktop Chromium for coding agents. Named workspaces keep tabs, cookies, and local storage after the agent disconnects. A person can watch, pause the agent, and take over. It does not, as the dossier says, attach itself to whatever Chrome the person already had open. The persistence is the product: the agent comes back to a browser that is still logged in.

[bb-browser](https://github.com/epiral/bb-browser) is the other side of that idea. The catalog describes it as driving sites with the login state you already have, exposed as a CLI and an MCP server. [ego lite](https://lite.ego.app) is a local desktop browser with per-agent spaces. [OpenCLI](https://opencli.info/) is about turning a site the user can already open into a CLI, via a browser bridge.

The trade is obvious and easy to understate. The agent can do things a fresh cloud browser cannot, because it is authenticated as someone. That someone is a person, or a shared profile, and the audit trail is "the browser did it" unless you add your own. Cloud sessions in the previous section give you a session id that is not your daily profile. Local persistent browsers give you fewer login walls and a worse story when the agent clicks the wrong thing. [Oversight](/categories/oversight-and-approval/) is the collection for a gate. A visible window, as in Hronaut, is a weaker gate that at least lets a person see the cursor.

## What to match to a design

If tasks are untrusted, parallel, and logged out, start with a hosted session and throw the profile away. Browserbase, Steel, Browser Use's CDP mode, Kernel, and the other session APIs are the list to read. Decide whether you want their agent loop or only the browser.

If the agent is a coding assistant on one machine and the sites are public, Playwright MCP or a local engine is enough to learn the interaction, and a hosted fleet is a later bill.

If the result is text for a context window, use Firecrawl, Crawl4AI, Olostep, or a search API, and do not stand up Chromium.

If the task only works when already logged in, you are choosing a persistent local browser or a hosted profile feature that the vendor documents as such. Read how logout, 2FA, and a person taking over are supposed to work. Skyvern, also in this collection, documents 2FA and TOTP as part of workflow automation. That is a session product with an opinion about login, not a local profile.

Then read the network question, which the browser page will not answer. A session that can open arbitrary URLs is an exfiltration path. Egress control may live in the browser product or in a [sandbox](/guides/sandboxes-and-code-execution/) beside it. AIO Sandbox, in the code-execution collection, packages a browser with a shell for that reason. It is listed there because the primitive is the combined environment, not because this collection forgot it.

## Figures this guide is leaving out

Startup times, concurrency limits, and "bypass" rates are the numbers vendors lead with. Some dossiers repeat them. They go stale, and this project has not run the clock. Use the linked docs when you need a current figure, and use this page to decide which docs are about the job you have. The cards on the [collection page](/categories/browser-and-web-execution/) are the full inventory. This essay is the map.
