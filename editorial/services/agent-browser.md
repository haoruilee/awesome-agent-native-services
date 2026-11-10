Plenty of agents already work by running shell commands and reading the output. For them, the simplest way to keep a browser around is another command: open a page, act on it, print what happened, and leave the browser ready for the next call. Vercel's agent-browser project takes that approach. The repository describes it as "Browser automation CLI for AI agents."

### A browser behind a command line

The dossier lists three parts: a CLI written in Rust, Chrome for Testing as the browser it drives, and scriptable browser control. Installation is `npm install -g agent-browser`, which puts the command on the path for any agent that can run a terminal. Chrome for Testing is Google's build of Chrome meant for automation, so the engine is a known quantity, separate from whatever browser the user has open.

MCP is marked as not the primary verified surface for this entry, and no Agent Skill is listed. The integration is the command itself. That is less of a gap than it sounds for a coding agent with shell access, because every such agent can already call a CLI. It is a real gap for a chat client that only speaks MCP. The dossier does not list the subcommands or describe how state persists between calls, so the [GitHub repository](https://github.com/vercel-labs/agent-browser) is where to learn the command set, how sessions are kept, and what format the output takes.

### Where a CLI fits in the browser shelf

The [browser and web execution collection](/categories/browser-and-web-execution/) and the [browser infrastructure guide](/guides/browser-infrastructure-for-agents/) separate engines you run from sessions you rent. agent-browser belongs with the former. [Browser MCP](/services/browser-mcp/) is its closest neighbor: also local, also aimed at agents, but delivered as an MCP server that works from the accessibility tree. [Browserbase](/services/browserbase/) and [Anchor Browser](/services/anchor-browser/) are hosted, so the browser runs on their side and each session is something you create through their API. [Browser Use Cloud](/services/browser-use-cloud/) adds its own agent loop on top.

The choice between a CLI and an MCP server is mostly about the host. Shell output lands in the agent's context as text, which is easy to log and replay. MCP tools arrive with schemas the client can show the model. Neither is better in general. Match it to how your agent already calls tools.

A careful adopter should also ask the identity questions the record answers only generically. Which profile does Chrome for Testing start with? Does anything persist on disk between runs? Can two agents share one browser, and should they? Who owns cleanup when an agent crashes mid-task?

### Editor's take

agent-browser makes sense for a coding agent that already lives in a terminal and wants a browser it can drive with the same habits it uses for git and test runners. If your client only calls MCP tools, Browser MCP is the shorter path. For many parallel, isolated sessions, look at Browserbase or Anchor Browser. This assessment is a reading of the dossier and the public repository; the CLI has not been installed or run against a site for this page.
