### Whose tokens, held where

Holding other people's OAuth tokens is the whole arrangement here. The dossier says so directly: the platform creates, stores, refreshes, and revokes tokens, and agent code never sees them. What it does not say is where that storage lives, whether an operator can run it inside their own network, or how a user disconnects an app without going through the agent. For anything that touches a customer's email or CRM, those answers belong in the review before the first Connect Link goes out, and the place to find them is the [Composio docs](https://docs.composio.dev).

The MCP record is thin in a similar way. It lists stdio and SSE transports and links an authentication concepts page rather than an MCP setup page, so whether you run a local server or connect to a hosted one is left to the docs.

### Discovery inside the loop

The documented model is runtime tool selection. Instead of a developer wiring a fixed list of integrations at build time, the agent gets meta-tools: one to search for a tool that fits the task, one to authenticate an app for a given `user_id`, and one to execute. If the user has not connected that app yet, the agent shows a Connect Link in the conversation, the user clicks once, and later calls go through without asking again. Every call is scoped to a `user_id`, which is how one agent serves many users without their credentials crossing.

Integration paths are broad. The quickest is `npx skills add composiohq/skills`, which installs official skills including `composio-tool-router` for isolated per-user tool sessions. Python packages such as `composio_openai` and `composio_anthropic`, the TypeScript `@composio/core`, and adapters for LangChain, CrewAI, LlamaIndex, and the Vercel AI SDK are also listed. Custom OAuth configs allow white-labeled consent screens and custom scopes.

### Neighbors in tool access

In [Tool Access & Integration](/categories/tool-access-and-integration/), the closest comparison is [Nango](/services/nango/), which calls itself the OAuth and API credential layer for agents. Both hold credentials; Composio also ships the tool catalog and the execution layer, so more of the stack is theirs. [ToolHive](/services/toolhive/) is about running any MCP server securely rather than brokering SaaS logins. [Snyk Agent Scan](/services/snyk-agent-scan/) scans agents, MCP servers, and skills, which pairs sensibly with any tool platform. Composio's tagline is "The tool platform built for agents." The MCP side of all this is covered in [Getting started with MCP servers](/guides/getting-started-with-mcp-servers/).

### Editor's take

Multi-user agents that need to act in many SaaS accounts, with consent collected mid-conversation, are the case Composio was shaped for. If you would rather keep tokens in a system you operate and write your own tool definitions, Nango is the smaller dependency. Our view is assembled from the dossier and the vendor's published material, and no connection was authorized through Composio while writing it.
