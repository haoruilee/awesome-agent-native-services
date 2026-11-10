### Library, platform, or both

The catalog marks the Agent Skill as unknown, even though the dossier prints an install command for an `agents-sdk` skill in the `cloudflare/skills` repository. Treat that as a lead to verify rather than a confirmed bundle. The larger gap is scope. The SDK is open source, but it runs on Workers and Durable Objects in your Cloudflare account, and the dossier lists Browser Run, Sandbox, AI Search, MCP governance, Code Mode, and payments in the same breath without saying which ship in the `agents` package and which are separate Cloudflare products with their own setup and terms. The [Agents docs](https://developers.cloudflare.com/agents/) are where to sort that out.

Operation is therefore shared. Cloudflare runs the runtime; you own the account, the API tokens, and the deployment.

### One Durable Object per agent

What the dossier documents well is the state model. An Agent class is a Durable Object, so each agent instance has a durable identity, its own SQL storage, WebSocket and SSE connections, and scheduled tasks. The runtime recovers from deploys, evictions, and dropped connections, so a long task picks up where it stopped without anyone rebuilding session state. Project Think adds a harness for long-running agents with sub-agents and workflows.

The start command is printed: `npx create-cloudflare@latest --template cloudflare/agents-starter`. The starter includes streaming chat, server-side and client-side tools, human approval, and scheduled tasks.

MCP is first-class in both directions. `McpAgent` and `createMcpHandler` build remote MCP servers over Streamable HTTP, `McpClient` consumes them, and OAuth guides cover authorization. Code Mode lets an agent write typed code against tools instead of carrying long tool definitions in the prompt. It can pause on approval-gated actions and replay completed calls from a durable log once a person approves.

### Next to other runtimes

[Agent Runtime & Infrastructure](/categories/agent-runtime-and-infrastructure/) mixes several kinds of product. [Letta](/services/letta/) pitches stateful agents in production, which overlaps with the Durable Object model; its dossier is the comparison to read if you want that state without committing to one cloud. [Modal](/services/modal/) describes AI infrastructure for developers, a compute pitch rather than an agent object model. [Cyberdesk](/services/cyberdesk/) provides virtual desktops, a different layer again. The tagline, "Build and host durable AI agents on Cloudflare's global network.", says the important part plainly: the network is the product. [What makes a service agent-native](/guides/what-makes-a-service-agent-native/) explains why a cloud vendor's SDK qualifies for the list.

### Editor's take

Teams already on Workers, or ones that want per-agent state, scheduling, and remote MCP without running servers, get a lot from this SDK. If your agents must run on another cloud or on hardware you control, it is the wrong dependency, and Letta or Modal are the comparisons to make. These conclusions come from reading the catalog's file and Cloudflare's developer docs; no agent was deployed to reach them.
