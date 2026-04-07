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
| [Keywords AI](keywords-ai.md) | AI gateway — 250+ models via OpenAI-compatible API | Fallback · Load balancing · OpenAI Agents trace processor | ⚠️ |
| [Agentgateway](agentgateway.md) | Connect, secure, and observe agentic workflows (MCP, A2A, LLM) | OpenAI-compatible proxy, MCP gateway, A2A, Kubernetes/bare metal | ✅ |

---

## Criteria Reminder

To qualify for this category, a service must:

1. Expose **agent-specific primitives** — per-agent budgets, per-agent virtual keys, agent trace IDs — not just generic API proxying.
2. Support **autonomous fallback and routing** without human reconfiguration.
3. Provide **agent-aware observability** — tracing that understands multi-step agent chains.
4. Work as a **drop-in layer** between agent code and LLM providers via API.
