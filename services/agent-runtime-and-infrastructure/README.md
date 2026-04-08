# Agent Runtime & Infrastructure Services

> Services that provide the **secure deployment substrate, session isolation, secret management, identity, gateway, and observability** required to run AI agents reliably in production — the "operating system layer" for autonomous agents.

## Why This Category Exists

Running a single agent in a Jupyter notebook is easy. Running thousands of agents in production — with isolated sessions, verified identities, managed secrets, secure tool access, and end-to-end observability — requires infrastructure that did not exist before AI agents became a first-class workload.

This category also includes **local agent-facing tooling** that changes how agents interact with codebases at scale — for example, semantic navigation CLIs that avoid standing up a full language-server stack for every short-lived session.

General-purpose cloud infrastructure (AWS EC2, Lambda, GCP Cloud Run) was designed for stateless functions and long-running services. It has no concept of:

- **Agent session isolation** — each agent run getting its own execution context
- **Agent identity tokens** — cryptographically verified proof of which agent took which action
- **Tool gateway** — a secure proxy controlling which external tools an agent can access
- **Agent-aware observability** — tracing that understands the semantic structure of agent reasoning (tool calls, memory reads, context injections), not just logs and metrics

The services in this category were purpose-built to fill this gap.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Claude Peers](claude-peers.md) | Local broker + MCP so Claude Code sessions discover peers and message ad-hoc | MCP (stdio), local broker, SQLite | ✅ |
| [acpx](acpx.md) | Headless ACP CLI — agents talk to coding agents over structured protocol, not PTY scraping | CLI, ACP protocol, SKILL.md | N/A |
| [Codex plugin for Claude Code](codex-plugin-cc.md) | Claude Code marketplace plugin — delegate reviews and rescue work to OpenAI Codex via slash commands | Slash commands · Subagent · Background jobs · Optional review gate | N/A |
| [Amazon Bedrock AgentCore](amazon-bedrock-agentcore.md) | Purpose-built for deploying and scaling dynamic AI agents and tools | AWS SDK, REST API, OpenTelemetry | ❌ |
| [Infisical Agent Sentinel](infisical-agent-sentinel.md) | Secrets and credential governance for AI agents | Daemon sidecar, REST API | ✅ |
| [Letta](letta.md) | The fastest way to bring stateful agents to production | REST API, Python SDK, TypeScript SDK, MCP | ✅ |
| [Aembit](aembit.md) | Secretless workload identity and access management for AI agents | Multi-protocol: MCP, OIDC, OAuth2, SSH, API keys | ✅ |
| [db9](db9.md) | Postgres but for agents | CLI, REST API, PostgreSQL wire, TypeScript SDK | ⚠️ |
| [AgentAnycast](agentanycast.md) | Connect AI agents across any network — no public IP | Python SDK, TypeScript SDK, MCP (`agentanycastd` / `uvx agentanycast-mcp`), P2P daemon | ✅ |
| [Multica](multica.md) | AI-native PM — agents as assignable teammates; local daemon runs Claude Code / Codex | Go backend + WebSocket · `multica` CLI (`--output json`) · local agent daemon | ⚠️ |
| [cx](cx.md) | Semantic code navigation for AI agents without a language server | CLI (TOON / JSON), tree-sitter index | ❌ |
| [Scrapybara](scrapybara.md) [![⭐](https://img.shields.io/github/stars/Scrapybara/scrapybara-python?style=social)](https://github.com/Scrapybara/scrapybara-python) | Remote desktops for computer-use agents (CUA) | Ubuntu/Browser/Windows instances · Act SDK · scrapybara-mcp | ✅ |
| [Agentuity](agentuity.md) [![⭐](https://img.shields.io/github/stars/agentuity/sdk?style=social)](https://github.com/agentuity/sdk) | The full-stack platform for AI agents | TypeScript/Python SDKs, CLI, sandboxes, storage, OTel, evals | ⚠️ |
| [Modal](modal.md) [![⭐](https://img.shields.io/github/stars/modal-labs/modal-client?style=social)](https://github.com/modal-labs/modal-client) | AI infrastructure — serverless GPUs, inference, sandboxes, batch | Python SDK, CLI, HTTP endpoints | ❌ |

---

## Criteria Reminder

To qualify for this category, a service must:

1. Provide **agent-specific execution, deployment, or coding-workflow primitives** (not just generic cloud compute).
2. Address **session isolation** — multiple agent runs do not share state (for hosted runtimes) **or** provide **agent-scoped local tooling** (for CLI utilities) that fits autonomous coding loops.
3. Address **agent identity** — verifiable attribution of actions to specific agents **or** clear **local OS-user / workspace** delegation for tools without cloud accounts.
4. Provide **agent-aware observability** — tracing that understands tool calls, memory, and reasoning steps **or** **token-efficient structured outputs** for agent navigation.
5. Be designed for **production scale** or **repeatable agent sessions**, not one-off demos.
