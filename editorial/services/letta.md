[Cloudflare Agents SDK](/services/cloudflare-agents-sdk/) is about building and hosting durable agents on Cloudflare's network, with the agent written as code on that platform. Letta makes the agent's state the thing you deploy: memory, conversation history, and reasoning traces stored in a model-agnostic format that outlives restarts and changes of model provider.

### The agent as deployment

The dossier traces Letta to the MemGPT research project at UC Berkeley and describes it as a platform for deploying and managing stateful agents. Each agent has a unique ID and isolated state. An agent template is a versioned blueprint for launching many agents with the same configuration. Memory variables are fields injected when an agent is created, such as a user's name or account tier. Self-editing memory, the MemGPT pattern, lets an agent rewrite its own memory blocks while it runs.

The Agent Development Environment, or ADE, is a visual debugger for inspecting an agent's memory, reasoning traces, and history. Letta Cloud is the managed hosting option; the dossier also lists self-hosting through an open-source Docker deployment. Claims about uptime and scaling belong in the vendor docs.

### Clients and the MCP angle

The quickest documented path is `pip install letta-client` and then `client.agents.create(...)`. A TypeScript client installs with `npm install @letta-ai/letta-client`, and a REST API covers create, query, update, and delete across the agent lifecycle. The [Letta docs](https://docs.letta.com) document each.

The MCP support runs in a specific direction. Per the dossier, it exposes Letta-managed agents as tools for other agents, over stdio or HTTP. That is useful in a multi-agent design where a long-lived specialist with its own memory is called by a short-lived orchestrator. No official Agent Skill is published.

### State that outlives a model

In [Agent Runtime & Infrastructure](/categories/agent-runtime-and-infrastructure/), [Modal](/services/modal/) describes itself more broadly as AI infrastructure, and Cloudflare's SDK is a framework plus hosting. [Cyberdesk](/services/cyberdesk/) offers virtual desktops, and [APort Agent Guardrails](/services/aport-agent-guardrails/) handles authorization before an action. Letta's distinguishing claim is persistence of agent identity and memory across sessions and model changes. The [agent-native guide](/guides/what-makes-a-service-agent-native/) explains why a stateful agent as a deployment unit counts as an agent-specific primitive.

Model-agnostic state deserves scrutiny. The data may move cleanly to a new provider, but a different model reading the same memory blocks can behave differently, so plan to re-evaluate after a switch. Self-editing memory means the agent can overwrite what an operator injected; check how the ADE or API shows those edits and whether they can be rolled back. Confirm which features exist in the self-hosted deployment versus Letta Cloud, and how agent state can be exported. The dossier mentions [HumanLayer](/services/humanlayer/) for approval gates on agent actions; Letta itself treats human oversight as optional.

### Editor's take

Letta fits products that give each user a long-lived agent that must remember across sessions and survive a change of model, especially where operators want to inspect memory directly. Teams that would rather write agents as code on an edge platform should compare Cloudflare Agents SDK; teams that want general AI infrastructure rather than a stateful-agent abstraction should look at Modal. Nothing was deployed to Letta Cloud or a local server in forming this view, which comes from the dossier and Letta's documentation.
