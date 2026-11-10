### Cloud versus the open image

Two shapes of Steel exist, and the dossier does not draw the line between them. The `steel-browser` repository is Apache-2.0 and ships a self-hosted Docker image; Steel Cloud is the managed service. CAPTCHA solving, proxy and fingerprint controls, and auto sign-in are described for the product in general, with no note on which of them work outside the cloud. Auto sign-in deserves the closest look. The dossier says it delegates authenticated site access to the platform and that operators must decide which sites agents may reach. Who stores those site credentials, and where, is the question to take to the [Steel docs](https://docs.steel.dev).

There is no official Agent Skill; the dossier points to cookbooks and the MCP server instead.

### Sessions you connect to

The documented primitive is a session: an isolated browser with its own cookies, storage, fingerprint, and connect endpoint. In Python, after `pip install steel-sdk`, the dossier shows `from steel import Steel`, then `client.sessions.create()`, then pointing Playwright, Puppeteer, or Selenium at the session's WebSocket URL. Moving from a local browser means swapping a launch for a connect. The TypeScript SDK installs as `steel-sdk` from npm.

Context injection is the agent-specific part. An agent can save cookies and local storage from one session and inject them into the next, so an authenticated flow resumes without logging in again. A session viewer shows live or recorded sessions for debugging. API keys gate who can create sessions, and the dossier advises against sharing a session across untrusted tenants.

The `steel-mcp-server` runs over stdio and can target either Steel Cloud or a local or self-hosted instance. That is the one place in the dossier where both shapes are plainly supported side by side.

### Among browser services

The [Browser & Web Execution](/categories/browser-and-web-execution/) category and the [browser infrastructure comparison](/guides/browser-infrastructure-for-agents/) cover several similar products. [Browserbase](/services/browserbase/) is the most direct comparison, a web browser for agents and applications. [Browser Use Cloud](/services/browser-use-cloud/) adds a natural-language task mode on top of raw browser control. [Browser MCP](/services/browser-mcp/) and [Vercel Agent Browser](/services/agent-browser/) are lighter tools, an MCP server and a CLI. Steel's tagline, "Browser Infrastructure for AI Agents.", fits; the fact that separates it in the dossier is an open-source browser API you can run yourself.

### Editor's take

Steel is a sensible pick when you want remote browser sessions under Playwright or Puppeteer and need the option to run the same API on your own machines later. If you would rather hand the agent a sentence and get a result back, Browser Use Cloud is closer to that. We have read the dossier and Steel's documentation and repositories, and have not started a session for this page.
