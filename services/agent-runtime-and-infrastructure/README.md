# Agent Runtime & Infrastructure Services

> Services that provide the **secure deployment substrate, session isolation, secret management, identity, gateway, and observability** required to run AI agents reliably in production — the "operating system layer" for autonomous agents.

## Why This Category Exists

Running a single agent in a Jupyter notebook is easy. Running thousands of agents in production — with isolated sessions, verified identities, managed secrets, secure tool access, and end-to-end observability — requires infrastructure that did not exist before AI agents became a first-class workload.

General-purpose cloud infrastructure (AWS EC2, Lambda, GCP Cloud Run) was designed for stateless functions and long-running services. It has no concept of:

- **Agent session isolation** — each agent run getting its own execution context
- **Agent identity tokens** — cryptographically verified proof of which agent took which action
- **Tool gateway** — a secure proxy controlling which external tools an agent can access
- **Agent-aware observability** — tracing that understands the semantic structure of agent reasoning (tool calls, memory reads, context injections), not just logs and metrics

The services in this category were purpose-built to fill this gap.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [acpx](acpx.md) | Headless ACP CLI — agents talk to coding agents over structured protocol, not PTY scraping | CLI, ACP protocol, SKILL.md | N/A |
| [Amazon Bedrock AgentCore](amazon-bedrock-agentcore.md) | Purpose-built for deploying and scaling dynamic AI agents and tools | AWS SDK, REST API, OpenTelemetry | ❌ |
| [Infisical Agent Sentinel](infisical-agent-sentinel.md) | Secrets and credential governance for AI agents | Daemon sidecar, REST API | ✅ |
| [Letta](letta.md) | The fastest way to bring stateful agents to production | REST API, Python SDK, TypeScript SDK, MCP | ✅ |
| [Aembit](aembit.md) | Secretless workload identity and access management for AI agents | Multi-protocol: MCP, OIDC, OAuth2, SSH, API keys | ✅ |

---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide **agent-specific execution or deployment primitives** (not just generic cloud compute).
2. Address **session isolation** — multiple agent runs do not share state.
3. Address **agent identity** — verifiable attribution of actions to specific agents.
4. Provide **agent-aware observability** — tracing that understands tool calls, memory, and reasoning steps.
5. Be designed for **production scale**, not just prototyping.
