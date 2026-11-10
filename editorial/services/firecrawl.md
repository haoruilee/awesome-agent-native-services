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
