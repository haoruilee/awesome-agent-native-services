### Where your logins live

Authenticated browser state is something this service keeps for you. The dossier calls these profiles, referenced by a `profile_id` and reused across runs so an agent does not log in every time. It does not say how profiles are stored, how long they persist, who in a workspace can attach one to a task, or how to delete one. A profile is effectively a set of live session cookies for real accounts, so that is the first page to find in the [Browser Use Cloud docs](https://docs.cloud.browser-use.com).

The split between the open-source project and the hosted product is only sketched. The `browser-use` repository holds the framework; the cloud is the hosted API and SDK layer on top. Which model drives Agent mode, and whether you can bring your own, is not covered. No official Agent Skill is documented.

### Two modes and a hosted MCP

What the dossier documents is a clean division. Agent mode takes a natural-language task: create an API key with the `bu_` prefix, run `pip install browser-use-sdk`, import `AsyncBrowserUse` from `browser_use_sdk.v3`, and call `client.run(...)` with a prompt; the output comes back as the result. Sessions keep a browser alive for follow-up tasks. Browser mode, through `browsers.create()`, returns a raw endpoint for Chrome DevTools Protocol control when you want to drive it yourself. Both run on managed stealth browsers with CAPTCHA solving and residential proxies.

The hosted MCP server speaks HTTP, authenticates with an `x-browser-use-api-key` header, and offers tools such as `run_session`, `send_task`, and `stop_session`. A coding agent in Cursor or Claude Code can run a browser task that way without any SDK code. A REST API sits under both paths, and live session URLs and message history help with debugging.

The environments the dossier names are serverless functions and CI, places with no local Chrome to launch.

### Compared with other browser hosts

The [Browser & Web Execution](/categories/browser-and-web-execution/) category, along with the [browser infrastructure comparison](/guides/browser-infrastructure-for-agents/), lays out the options. [Steel](/services/steel/) and [Browserbase](/services/browserbase/) center on browser infrastructure that your own automation code connects to. [Anchor Browser](/services/anchor-browser/) emphasizes secure infrastructure for computer-use agents. [Apify](/services/apify/) is about getting web data rather than driving a browser step by step. The tagline, "State-of-the-art AI browser automation with stealth browsers, CAPTCHA solving, residential proxies, and managed infrastructure.", is long but accurate; the natural-language task mode is what separates it.

### Editor's take

Pick this when an agent should hand off a whole web task in a sentence and get a result, especially from a serverless function. If you want to own each click with Playwright, or need to self-host the browser, Steel is the closer fit. What appears here is our reading of the dossier and the vendor's quick start and MCP pages; we have not issued a task against the service.
