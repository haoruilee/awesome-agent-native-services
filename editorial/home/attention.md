<!--
Homepage source for the attention section. scripts/home_editorial.py joins
these notes to editorial/home/github-stars.json and renders docs/index.md.
Star counts are not typed here, so a refresh cannot drift from the prose.
Refresh the snapshot with: python3 scripts/refresh-github-stars.py
-->

# Where attention clusters

Each figure is the public stargazers_count of one repository, read from the GitHub API and stored with the fetch date so the site can build without calling GitHub. Stars measure public interest in that repository, not traffic, revenue, or quality, and they are not a ranking of "best".

The linked repository is the one the dossier's star badge points at, or the official repository when a dossier has no badge. OpenRouter and Skyfire are omitted: their dossiers do not name a single public repository, so there is no count to show.

## Firecrawl

slug: firecrawl

Research and ingestion agents that want a page as text a model can quote, and that do not need to log in or press a button, are the fit. The repository is the open-source side of a service whose documented calls still go through the vendor's API, so a star is interest in that code while the fetch itself runs on their machines. An endpoint that takes a goal instead of a URL also hands them the choice of which pages to open. When the task has to end as an action on the page, a live browser session is the other tool.

## Mem0

slug: mem0

Assistants that keep facts about a person across many sessions, without the application managing the table, are the job this project describes. An extractor chooses what to add, change, drop, or leave alone, which is both the convenience and the hazard: a stray preference in a test conversation can come back later as something the prompt treats as known. User, agent, and session need to stay different namespaces. Accuracy claims on the vendor site were not rerun for this note, and a star count does not confirm them.

## Playwright MCP

slug: playwright-mcp

This is browser tooling that stays on a machine you control: the host starts the server, Playwright drives a local browser, and the model reads a structured view of the page rather than a screenshot. Coding agents checking a flow, or reading a document that only renders in a real browser, are the natural users. That is a sensible repository to star and a poor description of a hosted fleet. The process can reach whatever that machine can reach, so the allowed hosts have to be set before a run is left alone.

## Langfuse

slug: langfuse

The audience is a team that wants an agent run stored as a tree of spans, model calls, and tool calls, and a way to turn traces into an evaluation set, including the option to run the store themselves. Switching a decorator on captures whatever the current docs say it captures, which can include prompts, so the retention notes come before any customer data. If the only need is to export OpenTelemetry, a narrower collector may be the smaller commitment. The figure beside the name is this repository, not a census of self-hosted deployments.

## GitHub MCP Server

slug: github-mcp-server

A first-party server for repositories, issues, pull requests, Actions, and security alerts is the obvious remote starting point for agents that already work on GitHub. The agent acts as the user behind the token or the OAuth grant, and GitHub's own permissions still bound what it can do. Start with a read on one repository, and treat write toolsets as a separate decision. Being official does not make a broad token safe, and the hosted endpoint and a local build are different places for that credential to live.

## Composio

slug: composio

Multi-user agents that must act inside many SaaS accounts, and can collect consent in the middle of a conversation, are the case this platform is built around. The agent sees tools, while refresh tokens are supposed to stay in a store the model cannot read. Where that store lives, and how a person disconnects an app, belong in the docs before the first consent link goes out. Stars do not say whether a team adopted this platform or kept the vault and the tool definitions in a system they operate.

## Browserbase

slug: browserbase

The number on this row is Stagehand, the open-source SDK the dossier badges, not a tally of cloud browser sessions. It suits people who already write Playwright and want a remote browser they can also steer with ordinary language, then throw the session away. Recordings let a person replay what the agent did, and they are a place typed secrets can land, so the retention note should be open before recording is turned on. Public interest in the SDK is not a measure of the hosted product.

## E2B

slug: e2b

Coding and analysis agents that iterate in a REPL, keep state between steps, and read charts or files back from the run are the fit. The public project is the plain statement of a hosted sandbox, and part of its draw is running other tool servers inside the VM rather than on the agent's own machine. A disk that cannot see your files, paired with a network that can still reach the internet, is only half a boundary. This figure counts the repository, not sandboxes anyone has started.

## HumanLayer

slug: humanlayer

The repository is a human gate with a particular mechanism: mark the risky function, pause the run, and write the person's answer, including a reason for refusal, back into the agent's context. It suits teams whose dangerous calls are few and whose approver already lives in Slack or email. It is the wrong shape when a rule could decide and nobody should have to be waiting. The dossier does not settle what happens when the person never answers, or how an approval link proves who clicked it.

## Steel

slug: steel

Remote sessions for Playwright, Puppeteer, or Selenium, together with an open image you can run yourself, are why this repository is the one the dossier badges. The cloud service and that image are not promised to be the same set of features. CAPTCHA solving, proxies, and automatic sign-in need a check of which shape includes them, and automatic sign-in means site credentials are stored somewhere. The star count is the repository, and it says nothing about how many cloud sessions exist.

## Tavily

slug: tavily

Search, extraction, crawl, and a research pass under one key are why teams look here when they want the web as text for a context window, rather than a list of links a person would click. This count is the MCP server the dossier badges, not the Python SDK listed beside it and not the volume of queries anyone sends. Ranking, query retention, and what a research call does with the prompt are questions for the current docs. A neighboring tool is the closer fit when the need is embeddings-first retrieval, or only current library documentation.

## Vercel Sandbox

slug: vercel-sandbox

Firecracker microVMs for code a model just produced, with snapshots when the work outlasts one turn, are the fit, especially if the caller is already on Vercel and can use OIDC instead of a long-lived token. The repository is the SDK and the tooling, so the figure is public interest in that code, not a usage statistic for the hosted machines. This catalog does not have that statistic. Persistent sandboxes are marked beta in the dossier, which means the vendor docs have to say what is actually kept before anyone plans on a disk that is still there tomorrow.
