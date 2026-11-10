[Nango](/services/nango/) hands your code a fresh access token and leaves the API call to you. Arcade takes the call itself. Its tools run with credentials injected on the server side, so the model and the client see the result of a Gmail or Slack action without ever seeing the token that authorized it.

### Authorized tool calls

The dossier describes Arcade as a way to ship production MCP servers whose tools call third-party APIs with OAuth on behalf of end users. Its central idea is authorized tool calling: before a tool executes, Arcade checks the intersection of what the agent is allowed to do and what the user has delegated. If both permit it, Arcade injects the credential and runs the tool; results go back to the agent with secrets stripped out.

That framing is in the tagline, "MCP tools with managed OAuth — credentials stay out of the LLM." The docs also discuss SSO for agents, where enterprise identity providers supply the user side of the delegation. Pre-built integrations, including GitHub, Slack, Google, Gmail, and Salesforce, ship with managed OAuth, and Arcade stores refresh tokens and refreshes them without model visibility.

### Building with the CLI

The documented starting point is the Arcade CLI. The dossier prints `uv tool install arcade-mcp` followed by `arcade new my_server` to scaffold a server, and the CLI also handles local development and deploy. Hosted servers run on Arcade Cloud, reachable through HTTP APIs; transport is stdio or hosted MCP depending on the deployment. Per Arcade's docs, clients include Claude Desktop, Cursor, OpenAI Agents, Google ADK, Vercel AI, Mastra, and CrewAI. The [Arcade docs](https://docs.arcade.dev) have separate guides for building a server and for authorized tool calling.

No official Agent Skill bundle was located. The dossier points to community search.

### Questions for the docs

Within [Tool Access & Integration](/categories/tool-access-and-integration/), Arcade and Nango answer the same question from different heights. [ToolHive](/services/toolhive/) is about running any MCP server securely, which concerns the process more than the credential. [MCP Toolbox for Databases](/services/google-mcp-toolbox/) covers database access configured by an operator rather than OAuth granted by each user. The [MCP servers guide](/guides/getting-started-with-mcp-servers/) explains where an authoring platform like this sits.

A careful adopter should confirm where custom tools execute, on Arcade Cloud or on infrastructure you run, because that decides who holds stored refresh tokens. Find out how authorization policy is expressed and where audit logs can be read. The dossier notes that high-risk actions can still be gated by application policy outside Arcade, which means approval steps are your responsibility, not a built-in feature.

### Editor's take

Arcade is aimed at teams building user-facing copilots that act in mail, calendars, chat, or a CRM, where keeping tokens out of the model is a hard requirement and Python tool code is acceptable. Teams that only want a token store and prefer writing their own HTTP calls should compare Nango. If the main worry is whether a third-party server is safe to install, [Snyk Agent Scan](/services/snyk-agent-scan/) addresses that separate question. This judgement draws on the dossier and Arcade's documentation alone; the project has not deployed an Arcade server.
