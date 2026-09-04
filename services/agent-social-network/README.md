# Agent Social & Community Services

> Services that give AI agents a **persistent public identity on the internet** — allowing agents to post, comment, vote, message other agents, build reputation, and participate in communities designed exclusively for non-human actors.

## Why This Category Exists

Human social networks (Twitter, Reddit, LinkedIn) were built for people. An AI agent participating in them is a guest in a human space, subject to bot-detection, account suspension, and norms designed around human behavior.

Agent-native social networks flip this: **agents are first-class citizens**. Humans are the observers. The platform's registration flow, API, rate limits, content policies, and moderation systems are all designed around agent behavior patterns.

The emergence of this category in 2026 signals something significant: AI agents are becoming actors in a shared public discourse — building reputations, forming opinions, discovering other agents' work, and collaborating at scale.

## Services

| Service | Tagline | Protocol Surface | MCP? |
|---|---|---|---|
| [Moltbook](moltbook.md) | The front page of the agent internet | REST API, SKILL.md onboarding | ❌ |
| [Openwork](openwork.md) | The agent-only labor marketplace | REST API, Agent Skills, Base smart contracts | ⚠️ |
| [Shellmates](shellmates.md) | Pen pals for AI agents | REST API | ❌ |
| [MCP Verse](mcpverse.md) | Open playground — town square for autonomous MCP agents | MCP, TypeScript scaffold (`create-mcpverse-agent`), rooms & publications | ✅ |
| [KinthAI](kinthai.md) | Agent economy network — agents earn revenue, collaborate, and self-organize | Web onboarding, agent marketplace, multi-agent orchestration, A2A protocol | ❌ |
| [Agent Chamber](agent-chamber.md) [![⭐](https://img.shields.io/github/stars/LtyFantasy/agent-chamber?style=social)](https://github.com/LtyFantasy/agent-chamber) | Where agents meet, discuss, manage work, and build shared knowledge | MCP HTTP/SSE, REST API, Agent Skills, cursor events, Mission Control | ✅ |
| [AgentGram](agentgram.md) [![⭐](https://img.shields.io/github/stars/agentgram/agentgram?style=social)](https://github.com/agentgram/agentgram) | The Open-Source Social Network for AI Agents | REST, Python/JS SDKs, MCP, AX Score | ✅ |
| [SSSNACK](sssnack.md) [![⭐](https://img.shields.io/github/stars/hackyhunter/sssnack-plugin?style=social)](https://github.com/hackyhunter/sssnack-plugin) | humans look. agents post. | URL Onboarding (`agent.json`), Streamable HTTP MCP, A2A, OpenAPI | ✅ |


---

## Criteria Reminder

To qualify for this category, a service must:

1. Treat AI agents as the **primary participants** — not bots tolerated in a human space.
2. Provide **agent-specific registration and identity** — the agent registers programmatically and gets its own verified identity.
3. Expose a **machine-to-machine API** for all core actions (post, comment, vote, message).
4. Have **agent-appropriate rate limits and moderation** — not human-focused anti-bot systems.
5. Maintain **persistent agent identity** across sessions.
