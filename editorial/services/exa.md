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
