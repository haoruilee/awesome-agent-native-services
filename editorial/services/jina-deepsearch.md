The only thing an agent needs before using Jina DeepSearch is the ability to make an authenticated HTTP request. The dossier lists no MCP server and no Agent Skill, and it describes the product as API-first. If your runtime only speaks MCP, you will be writing or finding a thin wrapper yourself.

### A research call over plain HTTP

The vendor's wording is "Agentic search and deep research API for AI applications." The dossier splits that into three primitives: a query endpoint for factual retrieval, a deep research synthesis step, and response formatting meant for an LLM rather than a results page. The autonomy model is one sentence long: the agent calls the API directly inside its reasoning loop. Identity is an API key scoped to a project or agent execution context. Human approval, if you want it, sits outside the service.

That is close to the whole entry. The dossier does not name endpoints, request fields, streaming behavior, or how a synthesized result carries its sources. It says output is structured for agent pipelines and lists citation gathering as a use case, which implies sources come back, but it does not show their shape. The [DeepSearch docs](https://jina.ai/deepsearch) are the place to confirm that before you write a parser.

### Next to Linkup, Exa, and the MCP search servers

In [Search & Web Intelligence](/categories/search-and-web-intelligence/), the useful split is between services that return search results and services that return a composed answer. [Linkup](/services/linkup/) and [Exa](/services/exa/) are described as search APIs: the agent gets sources and does its own reasoning. DeepSearch's dossier adds a research synthesis primitive on top of retrieval, so part of the reasoning moves to the vendor's side of the call. That can save tokens in your loop, and it costs you visibility into how the answer was assembled.

The other split is transport. [Agent Search MCP](/services/agent-search-mcp/) ships as a Node.js MCP server and CLI, and [contextX](/services/contextx/) is a remote MCP server with normal and deep search modes. Those drop into an MCP client through configuration. DeepSearch, per the dossier, expects you to call HTTP from code. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why the catalog counts an API-first service like this one: the consumer is software, not a person scanning a page of links.

### Gaps in the entry

Before depending on it, check in the vendor docs how keys are issued and scoped, since the dossier mentions project and agent scopes without detail. Check whether a deep research request runs synchronously or returns something to poll, because that decides how your loop waits. Check how sources are attributed inside synthesized output, and whether a claim can be traced to one of them. Pricing and throughput belong to the vendor's pages.

### Editor's take

Pick DeepSearch if your agent already runs in code, can hold an HTTP call open through a research step, and would rather receive a composed answer than a pile of links. If you want raw sources to rank yourself, Linkup or Exa fit better. If your host only loads MCP servers, start with contextX or Agent Search MCP. This view comes from reading the catalog's dossier and Jina's public pages; the project has not sent DeepSearch a single query.
