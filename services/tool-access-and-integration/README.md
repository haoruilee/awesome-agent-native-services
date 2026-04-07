# Tool Access & Integration Services

> Services that let AI agents **discover, authenticate, and invoke external tools at runtime** — without a human pre-configuring credentials or selecting which integrations to activate.

## Why This Category Exists

When an agent needs to call an external API (GitHub, Salesforce, Slack, Google Calendar), three problems arise that human iPaaS platforms were never designed to solve:

1. **Runtime discovery** — the agent may not know at planning time which tool it needs; it must discover tools from a registry at execution time.
2. **Delegated authentication** — the agent must act on behalf of a user through OAuth, but the user cannot be redirected to a browser consent screen in the middle of an agent loop.
3. **Execution isolation** — each agent (or each user-agent pair) needs its own credential scope so one agent's permissions don't bleed into another's.

Agent-native tool access services solve all three problems with primitives that generic iPaaS platforms (Zapier, Make, n8n) never needed because they assumed a human was clicking buttons.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Composio](composio.md) | The tool platform built for agents | Python SDK, TypeScript SDK, 10+ framework integrations | ✅ |
| [Nango](nango.md) | OAuth and credential layer for AI agents | REST API, Node SDK | ✅ |
| [Toolhouse](toolhouse.md) | BaaS for AI agents — tools, memory, and execution | CLI, MCP Server, Streaming REST API | ✅ |
| [Smithery](smithery.md) [![⭐](https://img.shields.io/github/stars/smithery-ai/cli?style=social)](https://github.com/smithery-ai/cli) | Connect agents to thousands of MCP tools and Agent Skills | CLI, TypeScript SDK, remote MCP registry, OAuth brokerage | ✅ |
| [MCP Gateway](mcpgateway.md) | The platform for production AI agents — tools, skills, sandboxes | Python SDK (`mcpgateway-sdk`), federated MCP, RBAC | ✅ |

---

## Criteria Reminder

To qualify for this category, a service must:

1. Enable **runtime tool discovery** — agents find and select tools dynamically, not through static configuration.
2. Handle **delegated authentication** — OAuth and credential lifecycle managed by the service, not the agent's code.
3. Provide **per-agent or per-user credential isolation**.
4. Expose a **machine-to-machine interface** as the primary surface.
