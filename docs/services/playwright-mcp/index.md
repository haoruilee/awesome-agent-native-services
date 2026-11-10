---
title: "Playwright MCP | Agent-Native Services"
service_name: "Playwright MCP"
description: "A Model Context Protocol (MCP) server that provides browser automation capabilities using Playwright"
permalink: /services/playwright-mcp/
page_kind: service
service_slug: "playwright-mcp"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/playwright-mcp.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/playwright-mcp.md"
tagline: "A Model Context Protocol (MCP) server that provides browser automation capabilities using Playwright"
website: "https://playwright.dev/docs/getting-started-mcp"
repository: "https://github.com/microsoft/playwright-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · STDIO · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://playwright.dev/docs/getting-started-mcp" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://playwright.dev/mcp/configuration/options" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/microsoft/playwright-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/playwright-mcp.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

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

</section>

## What it does

Playwright MCP exposes browser automation as MCP tools so coding agents can open pages, inspect structure, click/type, and extract information from real web sessions. It uses accessibility snapshots and structured tool responses, reducing reliance on pixel-based screenshot interpretation.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP server (stdio by default; optional HTTP transport)
- **Catalog protocols:** MCP, STDIO, http
- **MCP:** ✅ Native MCP server
- **Agent Skill:** ⚠️ No standalone SKILL.md package found from the Playwright MCP repository.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP server (stdio by default; optional HTTP transport)

```bash
npx @playwright/mcp@latest
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/playwright-mcp.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP stdio | `npx @playwright/mcp@latest` |
| MCP HTTP | `--port` mode, e.g. `http://localhost:8931/mcp` |
| npm package | `@playwright/mcp` |
| Docker | `mcr.microsoft.com/playwright/mcp` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
