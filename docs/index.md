---
title: "Awesome Agent-Native Services"
description: "A curated list of agent-native services for AI agents: email, browsers, memory, sandboxes, payments, and MCP tools, with criteria and onboarding guides."
image: /assets/images/social-preview-wide.webp
page_kind: home
service_count: 301
collection_count: 16
new_arrivals_count: 112
---

<section id="practices" class="home-editorial" aria-labelledby="practices-title">
  <div class="section-intro">
    <span class="section-number">01</span>
    <h2 class="section-title" id="practices-title">Practices we keep coming back to</h2>
    <p class="section-note">From the guides</p>
  </div>
  <p class="home-editorial__lede">Seven decisions the guides keep returning to. The essays are the long form. These are the lines that still seem true once the comparison tables are closed.</p>
  <div class="practice-list">
    <article class="practice-list__item">
      <span class="practice-list__index">01</span>
      <div class="practice-list__copy">
        <h3>Four out of five is still a miss</h3>
        <p class="practice-list__takeaway">A page that says "for agents" can still be a person's account with a new headline.</p>
        <div class="practice-list__body">
        <p>The catalog refuses a service with tests you can point at. The vendor's pages have to name agents as the caller. The primitive has to be something a human product would not need. The agent has to finish the loop. The interface has to be a machine's. Outward action needs an identity that is not the operator's. Drop one and the proposal is out. The usual miss is an adapted product: a real API, a post that welcomes agents, and a user account. Operator surfaces are a narrow exception. They must read live agent state, tie it to a session, and admit the powers they lack. A passing card is a listing, not a recommendation.</p>
        </div>
        <p class="practice-list__links">
          <a href="{{ '/guides/what-makes-a-service-agent-native/' | relative_url }}">What makes a service agent-native</a>
          <a href="{{ '/categories/' | relative_url }}">All collections</a>
        </p>
      </div>
    </article>
    <article class="practice-list__item">
      <span class="practice-list__index">02</span>
      <div class="practice-list__copy">
        <h3>Who replies decides the inbox</h3>
        <p class="practice-list__takeaway">Correspondence, a one-time code, a notification, and notes between coding agents are four different products.</p>
        <div class="practice-list__body">
        <p>"Send email" is not a requirement until the other party has a name. A stranger who must reach the agent needs an address the agent owns, threads as data, and inbound mail as an event. A signup that only needs a code needs a mailbox that can wait. A person who already uses the product needs a notification, not a second public identity. Another coding agent in the same repository needs a record beside the code, not an MX record. A review-before-send gate is a real control. A sentence in the prompt that says not to email the customer is not. When a person must prove the domain first, that step is DNS being honest.</p>
        </div>
        <p class="practice-list__links">
          <a href="{{ '/guides/choose-an-email-api-for-agents/' | relative_url }}">How to choose an email API for AI agents</a>
          <a href="{{ '/categories/communication/' | relative_url }}">Communication</a>
        </p>
      </div>
    </article>
    <article class="practice-list__item">
      <span class="practice-list__index">03</span>
      <div class="practice-list__copy">
        <h3>A document, a click, or someone else's login</h3>
        <p class="practice-list__takeaway">Extraction, a disposable session, and a browser that is already signed in are not interchangeable.</p>
        <div class="practice-list__body">
        <p>The browser collection shares a page and not an architecture. An extraction API returns markdown or JSON and never submits the form. A hosted session is a browser the agent creates, drives, and throws away, which is what a click with a side effect requires. A local browser that kept its cookies can do what a fresh cloud profile cannot, because it is already signed in as a person. Mixing those up is how an agent reports a task that never happened, or pays for a full browser to fetch a public document. A task that works only when someone is already signed in is borrowing an identity, and the gate has to sit outside the model.</p>
        </div>
        <p class="practice-list__links">
          <a href="{{ '/guides/browser-infrastructure-for-agents/' | relative_url }}">Browser infrastructure for agents compared</a>
          <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}">Browser &amp; Web Execution</a>
        </p>
      </div>
    </article>
    <article class="practice-list__item">
      <span class="practice-list__index">04</span>
      <div class="practice-list__copy">
        <h3>Retrieval is not a memory</h3>
        <p class="practice-list__takeaway">What may be written, contradicted, forgotten, and named is the product. The index is only a part.</p>
        <div class="practice-list__body">
        <p>The next call sees the prompt you assembled, not the previous session, unless something was stored on purpose. Putting the transcript back in fails once the old lines crowd out the question. A vector index finds similar chunks and still has no lifecycle. Something has to decide that a sentence was a fact, that a newer sentence retired it, and which identity may read the row. Automatic extractors write when the agent forgets to, and also when the agent would have refused. A shared store leaks if user and agent are the same key. A store on one laptop is blank in CI unless the sync is real.</p>
        </div>
        <p class="practice-list__links">
          <a href="{{ '/guides/memory-layers-for-agents/' | relative_url }}">Memory layers for agents: approaches and trade-offs</a>
          <a href="{{ '/categories/memory-and-state/' | relative_url }}">Memory &amp; State</a>
        </p>
      </div>
    </article>
    <article class="practice-list__item">
      <span class="practice-list__index">05</span>
      <div class="practice-list__copy">
        <h3>Name the wall, including the network</h3>
        <p class="practice-list__takeaway">A filesystem that cannot see your disk, and a network that can still see the internet, are different promises.</p>
        <div class="practice-list__body">
        <p>Code a model just wrote should not run in the process that wrote it. This collection is environments an agent can create, run, read a result from, and destroy, with enough state that the next snippet still sees the previous files. A hosted microVM is the short path, and the vendor sees the code. A Kubernetes resource fits when you already operate a cluster, and nowhere else. A local hypervisor is only as strict as its mounts and its egress list. A container that bind-mounts a home directory is not a sandbox because the command says so. Secrets belong in neither the prompt nor an image shared across tenants.</p>
        </div>
        <p class="practice-list__links">
          <a href="{{ '/guides/sandboxes-and-code-execution/' | relative_url }}">Sandboxes and code execution for agents</a>
          <a href="{{ '/categories/code-execution/' | relative_url }}">Code Execution</a>
        </p>
      </div>
    </article>
    <article class="practice-list__item">
      <span class="practice-list__index">06</span>
      <div class="practice-list__copy">
        <h3>The protocol is not the permission</h3>
        <p class="practice-list__takeaway">A registry can tell you a tool exists. It cannot decide that this agent may call it.</p>
        <div class="practice-list__body">
        <p>MCP is how a host talks to servers that offer tools. It is not what this catalog means by agent-native. An HTTP API can pass the admission tests with no server, and a product built for people can ship a server and still fail. Stdio is a program you start beside the host. Remote HTTP is someone else's endpoint, and a secret in the query string is not an auth design. One server, one read, and the narrowest token that works is a finished first setup. The block on a bad write should not be a sentence in the prompt. A gateway moves where tokens sit. It does not remove the trust boundary.</p>
        </div>
        <p class="practice-list__links">
          <a href="{{ '/guides/getting-started-with-mcp-servers/' | relative_url }}">Getting started with MCP servers</a>
          <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}">Tool Access &amp; Integration</a>
        </p>
      </div>
    </article>
    <article class="practice-list__item">
      <span class="practice-list__index">07</span>
      <div class="practice-list__copy">
        <h3>Three layers before anything is signed</h3>
        <p class="practice-list__takeaway">Identity, settlement, and the right to refuse are different parts. A demo usually has only one.</p>
        <div class="practice-list__body">
        <p>A checkout for people has a signal an agent lacks: someone clicked Buy. What remains is who the agent is, what it may spend, and which record names the agent rather than a shared card. A wallet whose cap lives outside the model makes the agent a principal. An HTTP 402 challenge lets a metered API demand payment inside the request, and it does not create that cap. A mandate is evidence of what a person authorized when nobody was at the button. A probe, a co-signer, or a band the signing key cannot bypass is the check that should run first. A token transfer with no identity and no limit is not this category.</p>
        </div>
        <p class="practice-list__links">
          <a href="{{ '/guides/payments-for-autonomous-agents/' | relative_url }}">Payments for autonomous agents</a>
          <a href="{{ '/categories/commerce-and-payments/' | relative_url }}">Commerce &amp; Payments</a>
        </p>
      </div>
    </article>
  </div>
  <p class="guide-list__more"><a href="{{ '/guides/' | relative_url }}">All guides</a></p>
</section>

<section id="attention" class="home-editorial" aria-labelledby="attention-title">
  <div class="section-intro">
    <span class="section-number">02</span>
    <h2 class="section-title" id="attention-title">Where attention clusters</h2>
    <p class="section-note">GitHub stars · 2026-11-10 UTC</p>
  </div>
  <p class="home-editorial__lede home-editorial__disclaimer">Each figure is the public stargazers_count of one repository, read from the GitHub API and stored with the fetch date so the site can build without calling GitHub. Stars measure public interest in that repository, not traffic, revenue, or quality, and they are not a ranking of "best".</p>
  <p class="home-editorial__lede">The linked repository is the one the dossier's star badge points at, or the official repository when a dossier has no badge. OpenRouter and Skyfire are omitted: their dossiers do not name a single public repository, so there is no count to show.</p>
  <div class="attention-list">
    <article class="attention-list__item">
      <span class="attention-list__index">01</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/firecrawl/' | relative_url }}">Firecrawl</a></h3>
          <a class="attention-list__stars" href="https://github.com/firecrawl/firecrawl" rel="noopener noreferrer">200,310 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}">Browser &amp; Web Execution</a>
          <a href="https://github.com/firecrawl/firecrawl" rel="noopener noreferrer">firecrawl/firecrawl</a>
        </p>
        <div class="attention-list__body">
        <p>Research and ingestion agents that want a page as text a model can quote, and that do not need to log in or press a button, are the fit. The repository is the open-source side of a service whose documented calls still go through the vendor's API, so a star is interest in that code while the fetch itself runs on their machines. An endpoint that takes a goal instead of a URL also hands them the choice of which pages to open. When the task has to end as an action on the page, a live browser session is the other tool.</p>
        </div>
      </div>
    </article>
    <article class="attention-list__item">
      <span class="attention-list__index">02</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/mem0/' | relative_url }}">Mem0</a></h3>
          <a class="attention-list__stars" href="https://github.com/mem0ai/mem0" rel="noopener noreferrer">68,741 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/memory-and-state/' | relative_url }}">Memory &amp; State</a>
          <a href="https://github.com/mem0ai/mem0" rel="noopener noreferrer">mem0ai/mem0</a>
        </p>
        <div class="attention-list__body">
        <p>Assistants that keep facts about a person across many sessions, without the application managing the table, are the job this project describes. An extractor chooses what to add, change, drop, or leave alone, which is both the convenience and the hazard: a stray preference in a test conversation can come back later as something the prompt treats as known. User, agent, and session need to stay different namespaces. Accuracy claims on the vendor site were not rerun for this note, and a star count does not confirm them.</p>
        </div>
      </div>
    </article>
    <article class="attention-list__item">
      <span class="attention-list__index">03</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/playwright-mcp/' | relative_url }}">Playwright MCP</a></h3>
          <a class="attention-list__stars" href="https://github.com/microsoft/playwright-mcp" rel="noopener noreferrer">39,402 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}">Browser &amp; Web Execution</a>
          <a href="https://github.com/microsoft/playwright-mcp" rel="noopener noreferrer">microsoft/playwright-mcp</a>
        </p>
        <div class="attention-list__body">
        <p>This is browser tooling that stays on a machine you control: the host starts the server, Playwright drives a local browser, and the model reads a structured view of the page rather than a screenshot. Coding agents checking a flow, or reading a document that only renders in a real browser, are the natural users. That is a sensible repository to star and a poor description of a hosted fleet. The process can reach whatever that machine can reach, so the allowed hosts have to be set before a run is left alone.</p>
        </div>
      </div>
    </article>
    <article class="attention-list__item">
      <span class="attention-list__index">04</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/langfuse/' | relative_url }}">Langfuse</a></h3>
          <a class="attention-list__stars" href="https://github.com/langfuse/langfuse" rel="noopener noreferrer">37,246 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/observability-and-tracing/' | relative_url }}">Observability &amp; Tracing</a>
          <a href="https://github.com/langfuse/langfuse" rel="noopener noreferrer">langfuse/langfuse</a>
        </p>
        <div class="attention-list__body">
        <p>The audience is a team that wants an agent run stored as a tree of spans, model calls, and tool calls, and a way to turn traces into an evaluation set, including the option to run the store themselves. Switching a decorator on captures whatever the current docs say it captures, which can include prompts, so the retention notes come before any customer data. If the only need is to export OpenTelemetry, a narrower collector may be the smaller commitment. The figure beside the name is this repository, not a census of self-hosted deployments.</p>
        </div>
      </div>
    </article>
    <article class="attention-list__item">
      <span class="attention-list__index">05</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/github-mcp-server/' | relative_url }}">GitHub MCP Server</a></h3>
          <a class="attention-list__stars" href="https://github.com/github/github-mcp-server" rel="noopener noreferrer">34,360 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}">Tool Access &amp; Integration</a>
          <a href="https://github.com/github/github-mcp-server" rel="noopener noreferrer">github/github-mcp-server</a>
        </p>
        <div class="attention-list__body">
        <p>A first-party server for repositories, issues, pull requests, Actions, and security alerts is the obvious remote starting point for agents that already work on GitHub. The agent acts as the user behind the token or the OAuth grant, and GitHub's own permissions still bound what it can do. Start with a read on one repository, and treat write toolsets as a separate decision. Being official does not make a broad token safe, and the hosted endpoint and a local build are different places for that credential to live.</p>
        </div>
      </div>
    </article>
    <article class="attention-list__item">
      <span class="attention-list__index">06</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/composio/' | relative_url }}">Composio</a></h3>
          <a class="attention-list__stars" href="https://github.com/ComposioHQ/composio" rel="noopener noreferrer">31,009 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}">Tool Access &amp; Integration</a>
          <a href="https://github.com/ComposioHQ/composio" rel="noopener noreferrer">ComposioHQ/composio</a>
        </p>
        <div class="attention-list__body">
        <p>Multi-user agents that must act inside many SaaS accounts, and can collect consent in the middle of a conversation, are the case this platform is built around. The agent sees tools, while refresh tokens are supposed to stay in a store the model cannot read. Where that store lives, and how a person disconnects an app, belong in the docs before the first consent link goes out. Stars do not say whether a team adopted this platform or kept the vault and the tool definitions in a system they operate.</p>
        </div>
      </div>
    </article>
    <article class="attention-list__item">
      <span class="attention-list__index">07</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/browserbase/' | relative_url }}">Browserbase</a></h3>
          <a class="attention-list__stars" href="https://github.com/browserbase/stagehand" rel="noopener noreferrer">25,991 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}">Browser &amp; Web Execution</a>
          <a href="https://github.com/browserbase/stagehand" rel="noopener noreferrer">browserbase/stagehand</a>
        </p>
        <div class="attention-list__body">
        <p>The number on this row is Stagehand, the open-source SDK the dossier badges, not a tally of cloud browser sessions. It suits people who already write Playwright and want a remote browser they can also steer with ordinary language, then throw the session away. Recordings let a person replay what the agent did, and they are a place typed secrets can land, so the retention note should be open before recording is turned on. Public interest in the SDK is not a measure of the hosted product.</p>
        </div>
      </div>
    </article>
    <article class="attention-list__item">
      <span class="attention-list__index">08</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/e2b/' | relative_url }}">E2B</a></h3>
          <a class="attention-list__stars" href="https://github.com/e2b-dev/E2B" rel="noopener noreferrer">14,794 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/code-execution/' | relative_url }}">Code Execution</a>
          <a href="https://github.com/e2b-dev/E2B" rel="noopener noreferrer">e2b-dev/E2B</a>
        </p>
        <div class="attention-list__body">
        <p>Coding and analysis agents that iterate in a REPL, keep state between steps, and read charts or files back from the run are the fit. The public project is the plain statement of a hosted sandbox, and part of its draw is running other tool servers inside the VM rather than on the agent's own machine. A disk that cannot see your files, paired with a network that can still reach the internet, is only half a boundary. This figure counts the repository, not sandboxes anyone has started.</p>
        </div>
      </div>
    </article>
    <article class="attention-list__item">
      <span class="attention-list__index">09</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/humanlayer/' | relative_url }}">HumanLayer</a></h3>
          <a class="attention-list__stars" href="https://github.com/humanlayer/humanlayer" rel="noopener noreferrer">12,849 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/oversight-and-approval/' | relative_url }}">Oversight &amp; Approval</a>
          <a href="https://github.com/humanlayer/humanlayer" rel="noopener noreferrer">humanlayer/humanlayer</a>
        </p>
        <div class="attention-list__body">
        <p>The repository is a human gate with a particular mechanism: mark the risky function, pause the run, and write the person's answer, including a reason for refusal, back into the agent's context. It suits teams whose dangerous calls are few and whose approver already lives in Slack or email. It is the wrong shape when a rule could decide and nobody should have to be waiting. The dossier does not settle what happens when the person never answers, or how an approval link proves who clicked it.</p>
        </div>
      </div>
    </article>
    <article class="attention-list__item">
      <span class="attention-list__index">10</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/steel/' | relative_url }}">Steel</a></h3>
          <a class="attention-list__stars" href="https://github.com/steel-dev/steel-browser" rel="noopener noreferrer">7,939 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}">Browser &amp; Web Execution</a>
          <a href="https://github.com/steel-dev/steel-browser" rel="noopener noreferrer">steel-dev/steel-browser</a>
        </p>
        <div class="attention-list__body">
        <p>Remote sessions for Playwright, Puppeteer, or Selenium, together with an open image you can run yourself, are why this repository is the one the dossier badges. The cloud service and that image are not promised to be the same set of features. CAPTCHA solving, proxies, and automatic sign-in need a check of which shape includes them, and automatic sign-in means site credentials are stored somewhere. The star count is the repository, and it says nothing about how many cloud sessions exist.</p>
        </div>
      </div>
    </article>
    <article class="attention-list__item">
      <span class="attention-list__index">11</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/tavily/' | relative_url }}">Tavily</a></h3>
          <a class="attention-list__stars" href="https://github.com/tavily-ai/tavily-mcp" rel="noopener noreferrer">2,483 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}">Search &amp; Web Intelligence</a>
          <a href="https://github.com/tavily-ai/tavily-mcp" rel="noopener noreferrer">tavily-ai/tavily-mcp</a>
        </p>
        <div class="attention-list__body">
        <p>Search, extraction, crawl, and a research pass under one key are why teams look here when they want the web as text for a context window, rather than a list of links a person would click. This count is the MCP server the dossier badges, not the Python SDK listed beside it and not the volume of queries anyone sends. Ranking, query retention, and what a research call does with the prompt are questions for the current docs. A neighboring tool is the closer fit when the need is embeddings-first retrieval, or only current library documentation.</p>
        </div>
      </div>
    </article>
    <article class="attention-list__item">
      <span class="attention-list__index">12</span>
      <div class="attention-list__copy">
        <div class="attention-list__head">
          <h3><a href="{{ '/services/vercel-sandbox/' | relative_url }}">Vercel Sandbox</a></h3>
          <a class="attention-list__stars" href="https://github.com/vercel/sandbox" rel="noopener noreferrer">224 stars · 2026-11-10 UTC</a>
        </div>
        <p class="attention-list__meta">
          <a href="{{ '/categories/code-execution/' | relative_url }}">Code Execution</a>
          <a href="https://github.com/vercel/sandbox" rel="noopener noreferrer">vercel/sandbox</a>
        </p>
        <div class="attention-list__body">
        <p>Firecracker microVMs for code a model just produced, with snapshots when the work outlasts one turn, are the fit, especially if the caller is already on Vercel and can use OIDC instead of a long-lived token. The repository is the SDK and the tooling, so the figure is public interest in that code, not a usage statistic for the hosted machines. This catalog does not have that statistic. Persistent sandboxes are marked beta in the dossier, which means the vendor docs have to say what is actually kept before anyone plans on a disk that is still there tomorrow.</p>
        </div>
      </div>
    </article>
  </div>
</section>
<section id="new-arrivals" aria-labelledby="new-arrivals-title">
  <div class="section-intro">
    <span class="section-number">03</span>
    <h2 class="section-title" id="new-arrivals-title">New arrivals</h2>
    <p class="section-note">Last 30 days</p>
  </div>
  <div class="arrival-rail" role="region" aria-label="Last 30 days additions" tabindex="0">
    <article class="arrival-card atlas-sheet--arrival atlas-visual--01">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Browser &amp; Web Execution</span>
        <a class="arrival-card__name" href="https://hronaut.dev/" rel="noopener noreferrer">Hronaut</a>
        <span class="listing-source">Listed on <a href="{{ '/services/hronaut/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--02">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Browser &amp; Web Execution</span>
        <a class="arrival-card__name" href="https://lite.ego.app" rel="noopener noreferrer">ego lite</a>
        <span class="listing-source">Listed on <a href="{{ '/services/ego-lite/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--03">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Voice &amp; Phone</span>
        <a class="arrival-card__name" href="https://github.com/QwenAudio/qwen-audio-agent" rel="noopener noreferrer">Qwen Audio Agent</a>
        <span class="listing-source">Listed on <a href="{{ '/services/qwen-audio-agent/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--04">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Social &amp; Community</span>
        <a class="arrival-card__name" href="https://github.com/LtyFantasy/agent-chamber" rel="noopener noreferrer">Agent Chamber</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agent-chamber/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--05">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://loopx-project.github.io/loopx/" rel="noopener noreferrer">LoopX</a>
        <span class="listing-source">Listed on <a href="{{ '/services/loopx/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--06">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://github.com/fwyc0573/codex-hud" rel="noopener noreferrer">Codex HUD (fwyc0573)</a>
        <span class="listing-source">Listed on <a href="{{ '/services/codex-hud-fwyc0573/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--07">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://memmy.bot/" rel="noopener noreferrer">Memmy</a>
        <span class="listing-source">Listed on <a href="{{ '/services/memmy-agent/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--08">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Browser &amp; Web Execution</span>
        <a class="arrival-card__name" href="https://browser.lexmount.com" rel="noopener noreferrer">Moli</a>
        <span class="listing-source">Listed on <a href="{{ '/services/moli/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--09">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://agent-memory.dev" rel="noopener noreferrer">agentmemory</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agentmemory/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--10">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://github.com/jarrodwatts/claude-hud" rel="noopener noreferrer">Claude HUD</a>
        <span class="listing-source">Listed on <a href="{{ '/services/claude-hud/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--11">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Voice &amp; Phone</span>
        <a class="arrival-card__name" href="https://getpatter.com" rel="noopener noreferrer">Patter</a>
        <span class="listing-source">Listed on <a href="{{ '/services/patter/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--12">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Social &amp; Community</span>
        <a class="arrival-card__name" href="https://agentgram.co" rel="noopener noreferrer">AgentGram</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agentgram/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--13">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Communication</span>
        <a class="arrival-card__name" href="https://atomicmail.ai/" rel="noopener noreferrer">Atomic Mail</a>
        <span class="listing-source">Listed on <a href="{{ '/services/atomic-mail/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--14">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://agentexecutor.io" rel="noopener noreferrer">Agent Executor (AX)</a>
        <span class="listing-source">Listed on <a href="{{ '/services/google-ax/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--15">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://oh-my-codex.dev" rel="noopener noreferrer">oh-my-codex (OMX)</a>
        <span class="listing-source">Listed on <a href="{{ '/services/oh-my-codex/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--16">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Tool Access &amp; Integration</span>
        <a class="arrival-card__name" href="https://openchatcut.com" rel="noopener noreferrer">OpenChatCut</a>
        <span class="listing-source">Listed on <a href="{{ '/services/openchatcut/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--01">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Observability &amp; Tracing</span>
        <a class="arrival-card__name" href="https://github.com/perplexityai/numbat" rel="noopener noreferrer">numbat</a>
        <span class="listing-source">Listed on <a href="{{ '/services/numbat/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--02">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Oversight &amp; Approval</span>
        <a class="arrival-card__name" href="https://preloop.ai" rel="noopener noreferrer">Preloop</a>
        <span class="listing-source">Listed on <a href="{{ '/services/preloop/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--03">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Code Execution</span>
        <a class="arrival-card__name" href="https://axern.cofy-x.space" rel="noopener noreferrer">Axern</a>
        <span class="listing-source">Listed on <a href="{{ '/services/axern/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--04">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://lh-harness.pages.dev" rel="noopener noreferrer">LongHorizon-Harness</a>
        <span class="listing-source">Listed on <a href="{{ '/services/longhorizon-harness/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--05">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://vostride.com/" rel="noopener noreferrer">Agent QA</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agent-qa/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--06">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://qm.ycombinator.com" rel="noopener noreferrer">QM</a>
        <span class="listing-source">Listed on <a href="{{ '/services/qm/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--07">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://openai.com/index/open-source-codex-orchestration-symphony/" rel="noopener noreferrer">OpenAI Symphony</a>
        <span class="listing-source">Listed on <a href="{{ '/services/openai-symphony/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--08">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Commerce &amp; Payments</span>
        <a class="arrival-card__name" href="https://shinjukustaition.com" rel="noopener noreferrer">Shinjuku Shield</a>
        <span class="listing-source">Listed on <a href="{{ '/services/shinjuku-shield/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--09">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://mnemoverse.com/" rel="noopener noreferrer">Mnemoverse</a>
        <span class="listing-source">Listed on <a href="{{ '/services/mnemoverse/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--10">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://github.com/cloudflare/computer" rel="noopener noreferrer">Cloudflare Computer</a>
        <span class="listing-source">Listed on <a href="{{ '/services/cloudflare-computer/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--11">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://auten.ai" rel="noopener noreferrer">Auten</a>
        <span class="listing-source">Listed on <a href="{{ '/services/auten/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--12">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Browser &amp; Web Execution</span>
        <a class="arrival-card__name" href="https://www.kernel.sh/" rel="noopener noreferrer">Kernel</a>
        <span class="listing-source">Listed on <a href="{{ '/services/kernel/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--13">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Voice &amp; Phone</span>
        <a class="arrival-card__name" href="https://voygr.tech/placecall/" rel="noopener noreferrer">PlaceCall</a>
        <span class="listing-source">Listed on <a href="{{ '/services/placecall/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--14">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Tool Access &amp; Integration</span>
        <a class="arrival-card__name" href="https://mobbin.com/mcp" rel="noopener noreferrer">Mobbin</a>
        <span class="listing-source">Listed on <a href="{{ '/services/mobbin/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--15">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://deed.page" rel="noopener noreferrer">deed.page</a>
        <span class="listing-source">Listed on <a href="{{ '/services/deed-page/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--16">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Social &amp; Community</span>
        <a class="arrival-card__name" href="https://crosswalk.to" rel="noopener noreferrer">crosswalk</a>
        <span class="listing-source">Listed on <a href="{{ '/services/crosswalk/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--01">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Voice &amp; Phone</span>
        <a class="arrival-card__name" href="https://cosvoice.com" rel="noopener noreferrer">CosVoice</a>
        <span class="listing-source">Listed on <a href="{{ '/services/cosvoice/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--02">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Browser &amp; Web Execution</span>
        <a class="arrival-card__name" href="https://full-selfbrowsing.com" rel="noopener noreferrer">FSB (Full Self Browsing)</a>
        <span class="listing-source">Listed on <a href="{{ '/services/fsb/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--03">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Social &amp; Community</span>
        <a class="arrival-card__name" href="https://agentel.tech" rel="noopener noreferrer">Agentel</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agentel/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--04">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">LLM Gateway &amp; Routing</span>
        <a class="arrival-card__name" href="https://github.com/codejunkie99/sageroute" rel="noopener noreferrer">SageRoute</a>
        <span class="listing-source">Listed on <a href="{{ '/services/sageroute/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--05">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Social &amp; Community</span>
        <a class="arrival-card__name" href="https://swarmmemo.com" rel="noopener noreferrer">SwarmMemo</a>
        <span class="listing-source">Listed on <a href="{{ '/services/swarmmemo/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--06">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://peerd.ai" rel="noopener noreferrer">peerd</a>
        <span class="listing-source">Listed on <a href="{{ '/services/peerd/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--07">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://cua.ai" rel="noopener noreferrer">Cua</a>
        <span class="listing-source">Listed on <a href="{{ '/services/cua/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--08">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://github.com/pizza-bot-app/pizza-bot" rel="noopener noreferrer">Pizza Bot</a>
        <span class="listing-source">Listed on <a href="{{ '/services/pizza-bot/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--09">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://dexio.wiki" rel="noopener noreferrer">Dexio</a>
        <span class="listing-source">Listed on <a href="{{ '/services/dexio/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--10">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Tool Access &amp; Integration</span>
        <a class="arrival-card__name" href="https://toolport.app" rel="noopener noreferrer">Toolport</a>
        <span class="listing-source">Listed on <a href="{{ '/services/toolport/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--11">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Code Execution</span>
        <a class="arrival-card__name" href="https://docs.celesto.ai/smolvm" rel="noopener noreferrer">SmolVM</a>
        <span class="listing-source">Listed on <a href="{{ '/services/smolvm/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--12">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Commerce &amp; Payments</span>
        <a class="arrival-card__name" href="https://dansgit2b.github.io/lumen-tab/" rel="noopener noreferrer">Lumen Tab</a>
        <span class="listing-source">Listed on <a href="{{ '/services/lumen-tab/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--13">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Social &amp; Community</span>
        <a class="arrival-card__name" href="https://anansi-haven.anansidata.workers.dev" rel="noopener noreferrer">Anansi Haven</a>
        <span class="listing-source">Listed on <a href="{{ '/services/anansi-haven/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--14">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Social &amp; Community</span>
        <a class="arrival-card__name" href="https://commons.dooza.ai" rel="noopener noreferrer">Agent Commons</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agent-commons/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--15">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Social &amp; Community</span>
        <a class="arrival-card__name" href="https://switchboard-ai.fly.dev" rel="noopener noreferrer">Switchboard</a>
        <span class="listing-source">Listed on <a href="{{ '/services/switchboard/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--16">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Code Execution</span>
        <a class="arrival-card__name" href="https://github.com/deeplethe/sandstorm" rel="noopener noreferrer">forkd</a>
        <span class="listing-source">Listed on <a href="{{ '/services/forkd/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--01">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Search &amp; Web Intelligence</span>
        <a class="arrival-card__name" href="https://github.com/akasakariko/ContextX" rel="noopener noreferrer">contextX</a>
        <span class="listing-source">Listed on <a href="{{ '/services/contextx/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--02">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://reefinfra.ai" rel="noopener noreferrer">Reef</a>
        <span class="listing-source">Listed on <a href="{{ '/services/reef/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--03">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Durable Execution &amp; Scheduling</span>
        <a class="arrival-card__name" href="https://github.com/edgehero/pi-dispatch" rel="noopener noreferrer">pi-dispatch</a>
        <span class="listing-source">Listed on <a href="{{ '/services/pi-dispatch/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--04">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Search &amp; Web Intelligence</span>
        <a class="arrival-card__name" href="https://lennney.com/en/agent-search-mcp" rel="noopener noreferrer">Agent Search MCP</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agent-search-mcp/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--05">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Communication</span>
        <a class="arrival-card__name" href="https://cooperemail.com" rel="noopener noreferrer">Cooper Email</a>
        <span class="listing-source">Listed on <a href="{{ '/services/cooper-email/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--06">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://agentrider.fly.dev" rel="noopener noreferrer">Agent Rider</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agent-rider/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--07">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://github.com/skillsynchq/txcript" rel="noopener noreferrer">txcript</a>
        <span class="listing-source">Listed on <a href="{{ '/services/txcript/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--08">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Oversight &amp; Approval</span>
        <a class="arrival-card__name" href="https://sallyport.dev" rel="noopener noreferrer">Sallyport</a>
        <span class="listing-source">Listed on <a href="{{ '/services/sallyport/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--09">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Commerce &amp; Payments</span>
        <a class="arrival-card__name" href="https://secondsignruntime.com" rel="noopener noreferrer">SecondSign Core</a>
        <span class="listing-source">Listed on <a href="{{ '/services/secondsign-core/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--10">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Communication</span>
        <a class="arrival-card__name" href="https://trycaspianai.com" rel="noopener noreferrer">Caspian</a>
        <span class="listing-source">Listed on <a href="{{ '/services/caspian/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--11">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Commerce &amp; Payments</span>
        <a class="arrival-card__name" href="https://mpp.dev" rel="noopener noreferrer">MPP</a>
        <span class="listing-source">Listed on <a href="{{ '/services/mpp/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--12">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Communication</span>
        <a class="arrival-card__name" href="https://www.agentteam.email" rel="noopener noreferrer">AgentTeam Email</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agentteam-email/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--13">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Search &amp; Web Intelligence</span>
        <a class="arrival-card__name" href="https://context7.com" rel="noopener noreferrer">Context7</a>
        <span class="listing-source">Listed on <a href="{{ '/services/context7/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--14">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://supermemory.ai" rel="noopener noreferrer">Supermemory</a>
        <span class="listing-source">Listed on <a href="{{ '/services/supermemory/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--15">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Code Execution</span>
        <a class="arrival-card__name" href="https://cubesandbox.com" rel="noopener noreferrer">CubeSandbox</a>
        <span class="listing-source">Listed on <a href="{{ '/services/cubesandbox/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--16">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://github.com/ruvnet/ruflo" rel="noopener noreferrer">Ruflo</a>
        <span class="listing-source">Listed on <a href="{{ '/services/ruflo/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--01">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://mcpmemory.services" rel="noopener noreferrer">mcp-memory-service</a>
        <span class="listing-source">Listed on <a href="{{ '/services/mcp-memory-service/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--02">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://help.getzep.com/graphiti" rel="noopener noreferrer">Graphiti</a>
        <span class="listing-source">Listed on <a href="{{ '/services/graphiti/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--03">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://beads.gascity.com" rel="noopener noreferrer">Beads</a>
        <span class="listing-source">Listed on <a href="{{ '/services/beads/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--04">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Tool Access &amp; Integration</span>
        <a class="arrival-card__name" href="https://www.mcphub.app" rel="noopener noreferrer">MCPHub</a>
        <span class="listing-source">Listed on <a href="{{ '/services/mcphub/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--05">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://github.com/AVIDS2/memorix" rel="noopener noreferrer">Memorix</a>
        <span class="listing-source">Listed on <a href="{{ '/services/memorix/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--06">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://maxfreedompollard.github.io/Compartment/" rel="noopener noreferrer">Compartment</a>
        <span class="listing-source">Listed on <a href="{{ '/services/compartment/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--07">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://www.memoir-ai.dev" rel="noopener noreferrer">Memoir</a>
        <span class="listing-source">Listed on <a href="{{ '/services/memoir/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--08">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Social &amp; Community</span>
        <a class="arrival-card__name" href="https://sssnack.com/" rel="noopener noreferrer">SSSNACK</a>
        <span class="listing-source">Listed on <a href="{{ '/services/sssnack/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--09">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://www.projectmem.dev" rel="noopener noreferrer">projectmem</a>
        <span class="listing-source">Listed on <a href="{{ '/services/projectmem/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--10">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Meeting &amp; Conversation</span>
        <a class="arrival-card__name" href="https://agentcall.dev" rel="noopener noreferrer">AgentCall</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agentcall/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--11">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Meeting &amp; Conversation</span>
        <a class="arrival-card__name" href="https://joinly.ai" rel="noopener noreferrer">joinly.ai</a>
        <span class="listing-source">Listed on <a href="{{ '/services/joinly/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--12">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://engram.gentlemanprogramming.com/" rel="noopener noreferrer">Engram</a>
        <span class="listing-source">Listed on <a href="{{ '/services/engram/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--13">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://cmem.ai/" rel="noopener noreferrer">Claude-Mem</a>
        <span class="listing-source">Listed on <a href="{{ '/services/claude-mem/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--14">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Commerce &amp; Payments</span>
        <a class="arrival-card__name" href="https://ucp.dev" rel="noopener noreferrer">Universal Commerce Protocol (UCP)</a>
        <span class="listing-source">Listed on <a href="{{ '/services/ucp/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--15">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://github.com/agent-substrate/substrate" rel="noopener noreferrer">Agent Substrate</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agent-substrate/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--16">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Observability &amp; Tracing</span>
        <a class="arrival-card__name" href="https://eunomia.dev/agentsight/" rel="noopener noreferrer">AgentSight</a>
        <span class="listing-source">Listed on <a href="{{ '/services/agentsight/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--01">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://mempalaceofficial.com" rel="noopener noreferrer">MemPalace</a>
        <span class="listing-source">Listed on <a href="{{ '/services/mempalace/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--02">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Code Execution</span>
        <a class="arrival-card__name" href="https://agent-sandbox.sigs.k8s.io" rel="noopener noreferrer">Agent Sandbox (Kubernetes SIG)</a>
        <span class="listing-source">Listed on <a href="{{ '/services/kubernetes-agent-sandbox/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--03">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Tool Access &amp; Integration</span>
        <a class="arrival-card__name" href="https://ibm.github.io/mcp-context-forge/" rel="noopener noreferrer">ContextForge</a>
        <span class="listing-source">Listed on <a href="{{ '/services/contextforge/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--04">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Tool Access &amp; Integration</span>
        <a class="arrival-card__name" href="https://agentic-community.github.io/mcp-gateway-registry/" rel="noopener noreferrer">MCP Gateway &amp; Registry</a>
        <span class="listing-source">Listed on <a href="{{ '/services/mcp-gateway-registry/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--05">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Tool Access &amp; Integration</span>
        <a class="arrival-card__name" href="https://www.sandbase.ai" rel="noopener noreferrer">SandBase CLI</a>
        <span class="listing-source">Listed on <a href="{{ '/services/sandbase-cli/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--06">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://zilliztech.github.io/memsearch/" rel="noopener noreferrer">MemSearch</a>
        <span class="listing-source">Listed on <a href="{{ '/services/memsearch/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--07">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://deepseek.com/harness" rel="noopener noreferrer">DeepSeek Harness (dsh)</a>
        <span class="listing-source">Listed on <a href="{{ '/services/deepseek-harness/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--08">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Code Execution</span>
        <a class="arrival-card__name" href="https://github.com/BitMiracle-AI/Dormice" rel="noopener noreferrer">Dormice</a>
        <span class="listing-source">Listed on <a href="{{ '/services/dormice/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--09">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Code Execution</span>
        <a class="arrival-card__name" href="https://github.com/clawkwork/clawk" rel="noopener noreferrer">Clawk</a>
        <span class="listing-source">Listed on <a href="{{ '/services/clawk/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--10">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Tool Access &amp; Integration</span>
        <a class="arrival-card__name" href="https://docs.mcpjungle.com" rel="noopener noreferrer">MCPJungle</a>
        <span class="listing-source">Listed on <a href="{{ '/services/mcpjungle/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--11">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Browser &amp; Web Execution</span>
        <a class="arrival-card__name" href="https://github.com/vibheksoni/stealth-browser-mcp" rel="noopener noreferrer">Stealth Browser MCP</a>
        <span class="listing-source">Listed on <a href="{{ '/services/stealth-browser-mcp/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--12">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Tool Access &amp; Integration</span>
        <a class="arrival-card__name" href="https://docs.metamcp.com" rel="noopener noreferrer">MetaMCP</a>
        <span class="listing-source">Listed on <a href="{{ '/services/metamcp/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--13">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Commerce &amp; Payments</span>
        <a class="arrival-card__name" href="https://ap2-protocol.org" rel="noopener noreferrer">Agent Payments Protocol (AP2)</a>
        <span class="listing-source">Listed on <a href="{{ '/services/ap2/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--14">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Commerce &amp; Payments</span>
        <a class="arrival-card__name" href="https://priors.trade" rel="noopener noreferrer">Priors</a>
        <span class="listing-source">Listed on <a href="{{ '/services/priors/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--15">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://contextstream.io" rel="noopener noreferrer">ContextStream</a>
        <span class="listing-source">Listed on <a href="{{ '/services/contextstream/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--service atlas-visual--16">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Search &amp; Web Intelligence</span>
        <a class="arrival-card__name" href="https://www.datawebot.com" rel="noopener noreferrer">datawebot</a>
        <span class="listing-source">Listed on <a href="{{ '/services/datawebot/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--01">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Search &amp; Web Intelligence</span>
        <a class="arrival-card__name" href="https://serpkite.com" rel="noopener noreferrer">SerpKite</a>
        <span class="listing-source">Listed on <a href="{{ '/services/serpkite/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--02">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://sqwakie.si" rel="noopener noreferrer">Sqwakie</a>
        <span class="listing-source">Listed on <a href="{{ '/services/sqwakie/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--03">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Commerce &amp; Payments</span>
        <a class="arrival-card__name" href="https://send21.io" rel="noopener noreferrer">send21</a>
        <span class="listing-source">Listed on <a href="{{ '/services/send21/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--04">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Commerce &amp; Payments</span>
        <a class="arrival-card__name" href="https://veyra.money" rel="noopener noreferrer">Veyra</a>
        <span class="listing-source">Listed on <a href="{{ '/services/veyra/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--05">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Tool Access &amp; Integration</span>
        <a class="arrival-card__name" href="https://tadka.xyz" rel="noopener noreferrer">Tadka</a>
        <span class="listing-source">Listed on <a href="{{ '/services/tadka/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--06">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Tool Access &amp; Integration</span>
        <a class="arrival-card__name" href="https://www.corpusiq.io" rel="noopener noreferrer">CorpusIQ</a>
        <span class="listing-source">Listed on <a href="{{ '/services/corpusiq/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--07">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://three.ws" rel="noopener noreferrer">three.ws</a>
        <span class="listing-source">Listed on <a href="{{ '/services/three-ws/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--08">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Commerce &amp; Payments</span>
        <a class="arrival-card__name" href="https://inamprotocol.org" rel="noopener noreferrer">INAM Protocol</a>
        <span class="listing-source">Listed on <a href="{{ '/services/inam-protocol/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--09">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Commerce &amp; Payments</span>
        <a class="arrival-card__name" href="https://402xagent.com" rel="noopener noreferrer">402xAgent</a>
        <span class="listing-source">Listed on <a href="{{ '/services/402xagent/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--10">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Memory &amp; State</span>
        <a class="arrival-card__name" href="https://github.com/TencentCloud/TencentDB-Agent-Memory" rel="noopener noreferrer">TencentDB Agent Memory</a>
        <span class="listing-source">Listed on <a href="{{ '/services/tencentdb-agent-memory/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--11">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Observability &amp; Tracing</span>
        <a class="arrival-card__name" href="https://github.com/Continuum-AI-Corp/OrcaReplay" rel="noopener noreferrer">OrcaReplay</a>
        <span class="listing-source">Listed on <a href="{{ '/services/orcareplay/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--12">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://mobilerun.ai" rel="noopener noreferrer">Mobilerun</a>
        <span class="listing-source">Listed on <a href="{{ '/services/mobilerun/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--13">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://mobilenext.ai" rel="noopener noreferrer">Mobile Next</a>
        <span class="listing-source">Listed on <a href="{{ '/services/mobile-next/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--14">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Runtime &amp; Infrastructure</span>
        <a class="arrival-card__name" href="https://e2b.dev" rel="noopener noreferrer">E2B Desktop</a>
        <span class="listing-source">Listed on <a href="{{ '/services/e2b-desktop/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--15">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Harnesses &amp; Operator Surfaces</span>
        <a class="arrival-card__name" href="https://kwant.si" rel="noopener noreferrer">kwant</a>
        <span class="listing-source">Listed on <a href="{{ '/services/kwant/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
    <article class="arrival-card atlas-sheet--arrival atlas-visual--16">
      <span class="arrival-card__image" aria-hidden="true"></span>
      <span class="arrival-card__copy">
        <span class="arrival-card__category">Agent Social &amp; Community</span>
        <a class="arrival-card__name" href="https://directhireagents.com" rel="noopener noreferrer">Direct Hire</a>
        <span class="listing-source">Listed on <a href="{{ '/services/direct-hire/' | relative_url }}">The Agent-Native Index</a></span>
      </span>
    </article>
  </div>
</section>

<section id="material-studies" class="editorial-gallery" aria-label="Material studies for agent-native infrastructure">
  <figure class="editorial-gallery__item editorial-gallery__item--wide"><img src="{{ '/assets/images/editorial-network.webp' | relative_url }}" alt="Gold wires passing through a sequence of stone arches and converging into a circular hub." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-communication.webp' | relative_url }}" alt="Two white alcoves face each other on a dark plinth, joined by a thin gold line." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-authority.webp' | relative_url }}" alt="A gold beam balanced on stone disks in front of nested golden arches." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-oversight.webp' | relative_url }}" alt="A black arched doorway in a plaster wall barred by a horizontal brass rod beside a burgundy column." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-browser.webp' | relative_url }}" alt="A square opening in a plaster wall crossed by a brass rod, with dark stone steps and a red cube." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-runtime.webp' | relative_url }}" alt="Tiered beige stone platforms and matte-black pillars linked by thin gold rods." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-harness.webp' | relative_url }}" alt="A charcoal block strapped in a brushed-brass frame with handle-like rods." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-memory.webp' | relative_url }}" alt="A dark glass disc on a gold rod set against a layered white form with a spherical void." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-search.webp' | relative_url }}" alt="Textured plates and a smoked-glass disc threaded on a brass rod that ends in a black block." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-tools.webp' | relative_url }}" alt="Slender brass instruments standing in a grooved stone block, with two tools lying before a dark slab." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-routing-2.webp' | relative_url }}" alt="Five brass rods with spherical nodes converging into a vertical slot on a plaster wall." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-vault.webp' | relative_url }}" alt="A beige stone block with a central brass keyhole, standing on a dark pedestal." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-browser-2.webp' | relative_url }}" alt="A gold sphere resting on the ledge of a stepped rectangular recess in a plaster wall." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item"><img src="{{ '/assets/images/editorial-memory-2.webp' | relative_url }}" alt="Pale sheets stacked on a black cube and burgundy plinth, framed by a gold hoop, with a brass wedge marking one layer." width="1536" height="1024" loading="lazy" decoding="async"></figure>
  <figure class="editorial-gallery__item editorial-gallery__item--panorama"><img src="{{ '/assets/images/editorial-routing.webp' | relative_url }}" alt="Parallel gold pipes flowing through dark translucent panels above a winding marble and stone base." width="1536" height="1024" loading="lazy" decoding="async"></figure>
</section>

<section id="collections" aria-labelledby="collections-title">
  <div class="section-intro">
    <span class="section-number">04</span>
    <h2 class="section-title" id="collections-title">The collections</h2>
    <p class="section-note">16 fields · 301 dossiers</p>
  </div>
  <div class="collection-grid">
    <a class="collection-card atlas-visual--01" href="{{ '/categories/communication/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">01</span>
      <span class="collection-card__title">Communication</span>
      <span class="collection-card__count">17</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--02" href="{{ '/categories/browser-and-web-execution/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">02</span>
      <span class="collection-card__title">Browser &amp; Web Execution</span>
      <span class="collection-card__count">31</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--03" href="{{ '/categories/tool-access-and-integration/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">03</span>
      <span class="collection-card__title">Tool Access &amp; Integration</span>
      <span class="collection-card__count">31</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--04" href="{{ '/categories/oversight-and-approval/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">04</span>
      <span class="collection-card__title">Oversight &amp; Approval</span>
      <span class="collection-card__count">7</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--05" href="{{ '/categories/commerce-and-payments/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">05</span>
      <span class="collection-card__title">Commerce &amp; Payments</span>
      <span class="collection-card__count">22</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--06" href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">06</span>
      <span class="collection-card__title">Agent Runtime &amp; Infrastructure</span>
      <span class="collection-card__count">43</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--07" href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">07</span>
      <span class="collection-card__title">Agent Harnesses &amp; Operator Surfaces</span>
      <span class="collection-card__count">17</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--08" href="{{ '/categories/memory-and-state/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">08</span>
      <span class="collection-card__title">Memory &amp; State</span>
      <span class="collection-card__count">33</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--09" href="{{ '/categories/search-and-web-intelligence/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">09</span>
      <span class="collection-card__title">Search &amp; Web Intelligence</span>
      <span class="collection-card__count">14</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--10" href="{{ '/categories/code-execution/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">10</span>
      <span class="collection-card__title">Code Execution</span>
      <span class="collection-card__count">18</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--11" href="{{ '/categories/observability-and-tracing/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">11</span>
      <span class="collection-card__title">Observability &amp; Tracing</span>
      <span class="collection-card__count">14</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--12" href="{{ '/categories/durable-execution-and-scheduling/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">12</span>
      <span class="collection-card__title">Durable Execution &amp; Scheduling</span>
      <span class="collection-card__count">6</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--13" href="{{ '/categories/meeting-and-conversation/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">13</span>
      <span class="collection-card__title">Meeting &amp; Conversation</span>
      <span class="collection-card__count">7</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--14" href="{{ '/categories/voice-and-phone/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">14</span>
      <span class="collection-card__title">Voice &amp; Phone</span>
      <span class="collection-card__count">9</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--15" href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">15</span>
      <span class="collection-card__title">LLM Gateway &amp; Routing</span>
      <span class="collection-card__count">12</span>
      </span>
    </a>
    <a class="collection-card atlas-visual--16" href="{{ '/categories/agent-social-network/' | relative_url }}">
      <span class="collection-card__image" aria-hidden="true"></span>
      <span class="collection-card__copy">
      <span class="collection-card__number">16</span>
      <span class="collection-card__title">Agent Social &amp; Community</span>
      <span class="collection-card__count">20</span>
      </span>
    </a>
  </div>
</section>

<section id="guides" aria-labelledby="guides-title">
  <div class="section-intro">
    <span class="section-number">05</span>
    <h2 class="section-title" id="guides-title">Guides</h2>
    <p class="section-note">How to choose</p>
  </div>
  <div class="guide-list">
    <a class="guide-list__item" href="{{ '/guides/what-makes-a-service-agent-native/' | relative_url }}">
      <span class="guide-list__index">01</span>
      <span class="guide-list__copy">
        <strong>What makes a service agent-native</strong>
        <span>The five admission tests this catalog applies, the narrow operator-surface exception, and the products that stay off the list.</span>
      </span>
    </a>
    <a class="guide-list__item" href="{{ '/guides/choose-an-email-api-for-agents/' | relative_url }}">
      <span class="guide-list__index">02</span>
      <span class="guide-list__copy">
        <strong>How to choose an email API for AI agents</strong>
        <span>Agent-owned inboxes, self-hosted mail, notification workflows, and coordination mail for coding agents.</span>
      </span>
    </a>
    <a class="guide-list__item" href="{{ '/guides/browser-infrastructure-for-agents/' | relative_url }}">
      <span class="guide-list__index">03</span>
      <span class="guide-list__copy">
        <strong>Browser infrastructure for agents compared</strong>
        <span>Hosted browser sessions, local engines, extraction APIs, and browsers that keep a login between tasks.</span>
      </span>
    </a>
    <a class="guide-list__item" href="{{ '/guides/memory-layers-for-agents/' | relative_url }}">
      <span class="guide-list__index">04</span>
      <span class="guide-list__copy">
        <strong>Memory layers for agents: approaches and trade-offs</strong>
        <span>Fact extractors, temporal graphs, shared wikis, and local memory for coding agents, and why a vector index is not the whole problem.</span>
      </span>
    </a>
    <a class="guide-list__item" href="{{ '/guides/sandboxes-and-code-execution/' | relative_url }}">
      <span class="guide-list__index">05</span>
      <span class="guide-list__copy">
        <strong>Sandboxes and code execution for agents</strong>
        <span>Where generated code should run, and how microVMs, Kubernetes sandboxes, and local hypervisors differ.</span>
      </span>
    </a>
    <a class="guide-list__item" href="{{ '/guides/getting-started-with-mcp-servers/' | relative_url }}">
      <span class="guide-list__index">06</span>
      <span class="guide-list__copy">
        <strong>Getting started with MCP servers</strong>
        <span>Hosts, clients, and servers; local stdio versus remote HTTP; and the registries and credential layers in this catalog.</span>
      </span>
    </a>
    <a class="guide-list__item" href="{{ '/guides/payments-for-autonomous-agents/' | relative_url }}">
      <span class="guide-list__index">07</span>
      <span class="guide-list__copy">
        <strong>Payments for autonomous agents</strong>
        <span>Wallets and Know Your Agent identity, HTTP 402, payment mandates, and the checks that run before anything is signed.</span>
      </span>
    </a>
  </div>
  <p class="guide-list__more"><a href="{{ '/guides/' | relative_url }}">All guides</a></p>
</section>

<section id="for-agents" class="agent-entry-panel" aria-labelledby="agent-entry-title">
  <p class="eyebrow">Machine entrance</p>
  <h2 id="agent-entry-title">Enter as an agent.</h2>

  <pre><code>Read https://theagentnative.com/skill.md then find services designed for you natively.</code></pre>

  <div class="agent-entry-panel__links">
    <a href="{{ '/skill.md' | relative_url }}">skill.md ↗</a>
    <a href="{{ '/guides/' | relative_url }}">Guides</a>
    <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/CONTRIBUTING.md">Criteria ↗</a>
    <a href="#faq">FAQ</a>
  </div>
</section>

{% include home-faq.html %}

<section class="source-gateway" id="complete-index">
  <span class="source-gateway__image" aria-hidden="true"></span>
  <div>
  <span class="section-number">06</span>
  <h2 class="section-title">Full source.</h2>
  <a class="source-gateway__link" href="https://github.com/haoruilee/awesome-agent-native-services">Awesome Agent-Native Services on GitHub ↗</a>
  </div>
</section>
