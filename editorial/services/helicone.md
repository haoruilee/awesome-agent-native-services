A long-running agent that calls several model providers ends up holding several keys, writing its own retry logic for each, and leaving no single record of what it asked and what it spent. Changing one line of client setup to fix all three is the promise of an AI gateway. Helicone's version of that promise, in the vendor's own words, is "Build Reliable AI Apps," with the dossier adding the description AI gateway and LLM observability.

### One base URL for many providers

The documented integration is the OpenAI SDK pointed at a different address. In TypeScript, the dossier shows `import OpenAI from "openai"` with the client's base URL set to `https://ai-gateway.helicone.ai` and the API key read from a Helicone environment variable. Python and cURL use the same base URL. From there, the agent calls OpenAI-style chat completions, and Helicone routes each request to the selected model and provider.

Three things come with that swap, according to the dossier. Billing is unified through credits, so one balance covers many underlying providers, or you can bring your own provider keys instead. Fallbacks route around a degraded provider automatically, per the docs. And every request is logged to the Helicone dashboard for debugging and cost tracking. The [Helicone docs](https://docs.helicone.ai) list the supported models and current pricing terms. This page does not repeat them.

There is no dedicated MCP server documented as a primary surface and no official Agent Skill. The gateway is REST, and any OpenAI-compatible client is the integration path. No public repository is cited; the dossier treats Helicone as a hosted platform.

### Gateway or tracer

The [LLM gateway and routing collection](/categories/llm-gateway-and-routing/) is crowded with services that accept an OpenAI-shaped request. [Portkey](/services/portkey/) emphasizes per-agent virtual keys, budgets, and sticky routing for multi-turn agents. [LiteLLM](/services/litellm/) is an open-source gateway you run, with spend tracking and an agent gateway for A2A routing. [OpenRouter](/services/openrouter/) is a single API across many model labs with its own routing and analytics. Helicone's dossier leans hardest on observability: the gateway is the way in, and the request log is a large part of the value.

That framing shapes the checks to make. Every prompt and response passes through and is stored by a third party, so read the docs for data retention, redaction options, and where logs are hosted. Confirm how fallbacks choose a substitute model, since a silent switch can change agent behavior. Check how keys are scoped. The dossier says requests are attributed to keys and projects, but not whether one agent's key can be limited independently of another's.

### Editor's take

For a team that wants hosted routing and a searchable request log without running infrastructure, Helicone is a short path from a working OpenAI client. If per-agent budgets and keys matter more than logs, Portkey's record is more specific. If you must self-host, LiteLLM is the usual answer. The [guide to what makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains how this catalog weighs gateways at all. Conclusions here are drawn from the dossier and Helicone's published docs; no traffic was sent through the gateway for this review.
