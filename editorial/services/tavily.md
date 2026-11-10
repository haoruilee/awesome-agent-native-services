The search index, the ranking, and the page extraction all live on Tavily's servers. What runs on the agent's side is thin: an SDK call, a stdio MCP server that forwards requests, or a skill file that tells a coding assistant how to call the API with a key. The vendor therefore decides which sources an agent reads first, and the agent mostly decides how deep to ask.

### Search, extract, crawl, map, research

The vendor's wording is "Connect your agent to the web." The dossier frames Tavily as a web intelligence API that returns ranked, pre-processed content meant to drop straight into a context window, instead of a list of links for a person to click. It names separate endpoints for search, extraction from given URLs, site crawling, site mapping, and multi-step research with synthesis and source attribution. Search depth is a parameter the agent sets per call.

The integration list is long. There is a REST API at api.tavily.com, the tavily-python package, a TypeScript SDK repository, framework tools for LangChain, LlamaIndex, and CrewAI, and an official MCP server, tavily-mcp, over stdio for Claude Desktop, Cursor, Windsurf, and other hosts. The dossier's quickest path is the skills bundle, `npx skills add tavily-ai/skills`, covering research, search, extract, and crawl, with a `TAVILY_API_KEY` set in the agent's settings. See the [Tavily docs](https://docs.tavily.com) for current endpoints.

### Pre-processed results next to other search APIs

The [Search & Web Intelligence](/categories/search-and-web-intelligence/) category has several services that return text instead of links, and the differences sit in the retrieval model. [Exa](/services/exa/) describes itself as a search engine designed for AI and ranks by embeddings. [Linkup](/services/linkup/) is pitched at the same buyer, as a search API for agents and LLM apps. [Jina DeepSearch](/services/jina-deepsearch/) leans toward agentic deep research. [Context7](/services/context7/) is narrower, focused on current library docs for coding agents. Tavily's distinguishing feature, per the dossier, is the spread of endpoints under one key: search, extraction, crawl, and research. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) covers why LLM-shaped output counts.

### Gaps worth closing

Identity is one API key per integration. The dossier lists rate limits and credit costs; check the current figures in the docs rather than planning around old ones. It says nothing about how long queries are retained or whether query text is used for anything beyond serving the request, which matters for agents searching on behalf of customers.

One inconsistency is worth resolving before you script an install. The dossier's skill command names tavily-ai/skills, while its repository link points at tavily-ai/tavily-plugins. Confirm which one the vendor maintains. Also check how the research endpoint attributes sources, since an agent that cites its findings needs those links intact.

### Editor's take

For a team that wants one vendor for both search and page extraction, with framework adapters and skills already written, Tavily is the straightforward pick. If ranking by meaning matters more than breadth of endpoints, try Exa; for coding agents that mainly need library documentation, Context7 is the narrower tool. The judgment above leans on the dossier and Tavily's public reference pages; this catalog has not issued queries against it.
