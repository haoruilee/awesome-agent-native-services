### The gateway repository question

Which code is open is unclear from the record. It lists the Python and Node SDK repositories as the official code, while its stars badge points at a separate `Portkey-AI/gateway` repository that the dossier never describes. One use case mentions running Portkey on-prem or in a VPC, but no deployment steps are given, and nothing says whether that is the open gateway or an enterprise build. If running the proxy yourself matters, the [Portkey docs](https://portkey.ai/docs) need to answer that before anything else.

There is no dedicated MCP server and no official Agent Skill. The documented path is the OpenAI-compatible HTTP API, which works with any framework that lets you change a base URL.

### Keys that stand in for keys

The integration in the dossier is a base URL change: `pip install portkey-ai` or the Node package, then point the client at `https://api.portkey.ai/v1` with a virtual key. Portkey stores the real provider keys and hands each agent or project a scoped stand-in, so the provider credential never sits in agent code. Budgets attach to virtual keys, metadata tags, or workspaces, in currency or tokens, with alerts before they run out.

On each request Portkey checks the budget, consults a semantic cache, and routes to a provider. If that provider fails or rate-limits, a configured fallback takes the request. Sticky session routing keeps a multi-turn conversation on the same provider, and load balancing can split traffic by weight or in rotation. Guardrails check inputs and outputs against policy. Every call is logged with cost, tokens, and a trace ID that links the steps of a multi-hop agent chain.

Human approval is out of scope. Budget alerts are the only human-facing control the dossier names.

### Other gateways

[LLM Gateway & Routing](/categories/llm-gateway-and-routing/) has close competitors. The Portkey dossier itself names [LiteLLM](/services/litellm/) as the open-source, self-hosted sibling and positions Portkey as the managed one. [OpenRouter](/services/openrouter/) offers a unified interface for LLMs. [Helicone](/services/helicone/) pairs an AI gateway with LLM observability. [Agentgateway](/services/agentgateway/) is aimed at connecting and securing agentic workflows. Portkey's tagline, "The AI gateway built for production agents.", leans on virtual keys and per-agent budgets as the agent-specific parts. [What makes a service agent-native](/guides/what-makes-a-service-agent-native/) sets out why gateways are listed in this catalog.

### Editor's take

Portkey suits teams that want per-agent keys, budgets, and fallback without operating a proxy fleet, and who are comfortable sending prompt traffic through a vendor. If the traffic must stay on infrastructure you run, LiteLLM is the documented self-hosted route. We assembled this from the dossier and Portkey's public docs; no request was routed through Portkey for it.
