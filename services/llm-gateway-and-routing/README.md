# LLM Gateway & Routing Services

> Services that give AI agents a **reliable, observable, and cost-controlled interface to LLM providers** — with per-agent routing, budget enforcement, fallback logic, and semantic caching as first-class primitives.

## Why This Category Exists

Calling an LLM directly is fine for prototyping. Running agents in production — where a single agent may chain dozens of LLM calls across multiple providers — requires infrastructure that the LLM providers themselves don't offer:

- **Per-agent budget limits** — cap how much a specific agent instance can spend
- **Automatic fallback** — if GPT-4o is rate-limited, route to Claude without changing agent code
- **Agent-level observability** — trace every step of a multi-hop agent call chain with cost attribution
- **Semantic caching** — return cached responses for semantically similar agent queries, reducing cost
- **Virtual keys** — give each agent its own scoped API credential without exposing real provider keys

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Portkey](portkey.md) | The AI gateway built for production agents | REST API (OpenAI-compatible), Python SDK, TypeScript SDK | ❌ |
| [Respan (Keywords AI)](keywords-ai.md) | Route, observe, and evaluate every LLM call | Fallback · Caching · `OpenAIAgentsInstrumentor` · MCP | ✅ |
| [Agentgateway](agentgateway.md) | Connect, secure, and observe agentic workflows (MCP, A2A, LLM) | OpenAI-compatible proxy, MCP gateway, A2A, Kubernetes/bare metal | ✅ |
| [LiteLLM](litellm.md) [![⭐](https://img.shields.io/github/stars/BerriAI/litellm?style=social)](https://github.com/BerriAI/litellm) | Open-source AI gateway — 100+ LLMs, virtual keys, Agent Gateway (A2A) | OpenAI-compatible proxy, Docker/K8s, A2A JSON-RPC, MCP (gateway) | ✅ |
| [Bifrost](bifrost.md) [![⭐](https://img.shields.io/github/stars/maximhq/bifrost?style=social)](https://github.com/maximhq/bifrost) | High-performance AI gateway with provider routing, governance, and MCP gateway | OpenAI-compatible REST, Go SDK, MCP gateway, HTTP/SSE | ✅ |
| [OpenRouter](openrouter.md) | The unified interface for LLMs — one API, 300+ models | OpenAI-compatible REST, TypeScript/Python/Go/Java SDKs | ❌ |
| [Helicone](helicone.md) | AI Gateway & LLM observability — 100+ models, unified credits | OpenAI-compatible gateway (`ai-gateway.helicone.ai`), dashboard | ❌ |
| [Routerly](routerly.md) [![⭐](https://img.shields.io/github/stars/Inebrio/Routerly?style=social)](https://github.com/Inebrio/Routerly) | Self-hosted LLM gateway with LLM-native routing policy — no DB required | OpenAI/Anthropic-compatible HTTP, JSON config, Docker single binary | ⚠️ |
| [SageRoute](sageroute.md) [![⭐](https://img.shields.io/github/stars/codejunkie99/sageroute?style=social)](https://github.com/codejunkie99/sageroute) | Trajectory-aware model router that escalates from execution evidence | OpenAI Responses, Anthropic Messages, session history API, Bun proxy | ❌ |
| [XiuRouter](xiurouter.md) | Claude, GPT, Gemini, and more through one API | OpenAI Responses/Chat, Anthropic Messages, Gemini GenerateContent, scoped keys | ⚠️ |


---

## Criteria Reminder

To qualify for this category, a service must:

1. Expose **agent-specific primitives** — per-agent budgets, per-agent virtual keys, agent trace IDs — not just generic API proxying.
2. Support **autonomous fallback and routing** without human reconfiguration.
3. Provide **agent-aware observability** — tracing that understands multi-step agent chains.
4. Work as a **drop-in layer** between agent code and LLM providers via API.
