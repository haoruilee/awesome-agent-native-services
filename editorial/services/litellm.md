### You run it

Nobody else operates LiteLLM in this catalog record. The documented path is a proxy you deploy yourself from the Python package, a Docker image, or Kubernetes, then point the OpenAI SDK's base URL at. That puts the provider keys, the logs, and the uptime on your side. What the dossier leaves open is the line between the open-source proxy and paid features: virtual keys with budgets and RBAC carry an Enterprise note, and audit through SSO is described only by reference to the enterprise docs. Check the [LiteLLM docs](https://docs.litellm.ai) for which controls you get without a license before designing around them.

MCP support is also hard to pin down. The dossier describes it as a gateway feature, with pass-through and proxy patterns for MCP servers, rather than as a package a coding agent can install, and it gives no single page for it. There is no official Agent Skill.

### Agents as routes

Beyond model routing, the Agent Gateway treats agents themselves as destinations. You register A2A-compatible agents, such as ones on Vertex Agent Engine, Bedrock AgentCore, LangGraph, or Pydantic AI, and invoke them through A2A JSON-RPC at `POST /a2a/{agent_name}/message/send` or through the OpenAI SDK with an `a2a/` model prefix. That is the clearest difference from gateways that only proxy model calls.

Two headers carry agent identity through nested calls. `X-LiteLLM-Trace-Id` groups the calls of one run, and `X-LiteLLM-Agent-Id` attributes spend to an agent. Iteration budgets cap how many loops an agent can make at the gateway, a stop for runaway agents that does not depend on the agent's own code behaving.

The rest is standard gateway work: fallbacks, load balancing, budgets, rate limits, guardrail hooks, and log export to OpenTelemetry, S3, or Langfuse. An Admin UI and REST APIs sit beside the proxy.

### Next to managed gateways

In [LLM Gateway & Routing](/categories/llm-gateway-and-routing/), the usual comparison is [Portkey](/services/portkey/), the AI gateway built for production agents, which its own dossier frames as the managed alternative. [Bifrost](/services/bifrost/) pitches applications that never go down. [Agentgateway](/services/agentgateway/) aims at connecting and securing agentic workflows, which overlaps with the A2A routing here. [OpenRouter](/services/openrouter/) offers a unified interface to models as a service. The vendor tagline stresses model access, fallbacks, and spend tracking in the OpenAI format. The listing criteria are explained in [What makes a service agent-native](/guides/what-makes-a-service-agent-native/).

### Editor's take

LiteLLM is the default for platform teams that must keep model traffic inside their own VPC and want A2A agents behind the same proxy as model calls. Teams that would rather not operate a gateway at all should evaluate Portkey or OpenRouter instead. We formed this view from the catalog record and LiteLLM's docs, without standing up the proxy.
