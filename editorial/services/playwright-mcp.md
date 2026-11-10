Nothing here runs in a vendor cloud. The server is an npm package, `@playwright/mcp`, that the agent host launches on its own machine, over stdio by default, and the browser it drives is a local Playwright browser. The agent's reach is whatever that machine's network can reach, and the operator is whoever owns the laptop, CI runner, or container. That is the opposite trade from a hosted fleet: no account and no vendor in the path, but also no isolation beyond what you configure.

### Snapshots as tools

The dossier describes browser automation exposed as MCP tools: navigate, click, type, and extract. Instead of handing the model screenshots to interpret, the server returns accessibility snapshots, a structured view of the page that a model can reason over. The loop is plain. The host starts the server, the agent calls a tool, Playwright performs the action, and the structured result comes back for the next decision.

Setup is a single command, `npx @playwright/mcp@latest`, plus an entry in the host's MCP configuration that runs the same package. Passing `--port` starts a standalone HTTP transport for clients that prefer a URL. A container image, `mcr.microsoft.com/playwright/mcp`, is also listed. The [configuration options page](https://playwright.dev/mcp/configuration/options) is where the runtime flags live. No standalone Agent Skill was found in the repository; MCP is the documented interface.

### A local server among hosted browsers

The [Browser & Web Execution](/categories/browser-and-web-execution/) category splits between sessions you rent and engines you run. [Browserbase](/services/browserbase/) and [Steel](/services/steel/) are rented sessions with an account, an API key, and the vendor's network. Playwright MCP is an engine-plus-protocol you attach. [Browser MCP](/services/browser-mcp/) is its closest peer, another MCP server for browser control. [Vercel Agent Browser](/services/agent-browser/) covers similar ground as a CLI rather than an MCP server, which suits agents that already work through a shell. The [browser infrastructure guide](/guides/browser-infrastructure-for-agents/) walks through when local beats hosted.

### Settings to read before autonomy

The dossier's identity story is runtime policy, not accounts. Flags such as `--allowed-hosts`, along with allowed and blocked origins and file access controls, define where the agent may go. Set them before an unattended run, because the default reach is the host's own network, including internal services a coding agent may not need.

HTTP mode needs a second look. The dossier does not describe authentication for the HTTP transport, so do not expose that port beyond the local machine without putting your own control in front of it. It also does not cover how browser profiles persist between runs, which matters if an agent signs in to anything. Attribution comes from the host's logs and its MCP tool history.

### Editor's take

Coding agents checking a UI flow, writing tests, or reading a JavaScript-heavy page on a developer machine are the obvious users, since there is nothing to sign up for. Agents that need many parallel sessions or isolation from the host should look at Browserbase or Steel; for sites that resist automation, Browser Use Cloud advertises stealth browsers and CAPTCHA solving. Read this as a summary of the dossier and Microsoft's configuration pages rather than a report from running the server.
