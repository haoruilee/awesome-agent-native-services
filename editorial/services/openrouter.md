Every request an agent sends through this gateway passes through a hosted service that OpenRouter operates, then on to whichever model provider it routes to. Nothing runs on the agent's machine except an OpenAI-compatible client pointed at a different base URL. That places two parties between the agent and its model, and the account's routing and data policy settings decide which second party sees each prompt.

### One base URL, many providers

The vendor's wording is "The Unified Interface For LLMs." In the dossier that means a single OpenAI-compatible chat completions API across models from many labs, with routing, failover between providers, one credit balance, and usage analytics. An agent names a model by its slug, optionally adds routing hints, and OpenRouter picks a provider. Tool calls and multi-turn loops then behave as they would against the OpenAI API, which is why an agent framework can adopt it by changing a base URL and a key.

The documented surfaces are the REST base URL `https://openrouter.ai/api/v1`, official SDKs in TypeScript, Python, Go, and Java, and a dashboard for keys and credits that the dossier calls secondary. The quickstart sets an `OPENROUTER_API_KEY` and points an existing OpenAI client at that base URL. The dossier records no first-party MCP server and no official Agent Skill; HTTP and the SDKs are the path. Start from the [OpenRouter quickstart](https://openrouter.ai/docs/quickstart) and the provider selection guide it links.

### Hosted router versus a gateway you run

The [LLM Gateway & Routing](/categories/llm-gateway-and-routing/) category divides on who runs the router. [LiteLLM](/services/litellm/) is a gateway that keeps model access, fallbacks, and spend tracking in the OpenAI format, and the dossier's comparison table names a self-managed router as the alternative that leaves failover and provider contracts with you. [Portkey](/services/portkey/) positions itself as a gateway for production agents. [Helicone](/services/helicone/) pairs a gateway with LLM observability. [Bifrost](/services/bifrost/) is pitched on keeping applications up. OpenRouter's difference is that it is also the billing relationship: one balance replaces separate accounts with each lab. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) covers why programmatic keys and credits matter for unattended agents.

### Account settings to review

API keys belong to users or organizations, and usage is billed to the owner. Check how granular keys can be and whether each agent or environment can get its own key with its own spending ceiling, because an unattended loop can spend quickly.

Data policy is the setting with the most weight. The dossier says it controls what OpenRouter logs and which providers may process prompts. Set it before sending anything sensitive, and read which providers each model may route to. The dossier does not specify how failover handles differences in tool-calling behavior between providers serving the same model, or what happens to a request mid-stream when a provider fails. Test both with your own prompts before relying on automatic failover. Public app listings are optional; decide if you want your usage attributed by name.

### Editor's take

Agents that switch between cheap and frontier models, or that need to keep running when a single lab has an outage, get the most from one key and one bill. Teams that must keep prompts inside their own network, or want the router under their own control, should compare LiteLLM and Portkey, checking which deployment options each one documents. These remarks rest on the dossier and OpenRouter's quickstart and routing docs, not on traffic we have sent through it.
