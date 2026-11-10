---
title: "Browser MCP | Agent-Native Services"
service_name: "Browser MCP"
description: "Browser MCP server for AI agents"
permalink: /services/browser-mcp/
page_kind: service
service_slug: "browser-mcp"
category_slug: "browser-and-web-execution"
category_label: "Browser & Web Execution"
hero_image: "/assets/images/editorial-browser.webp"
image: "/assets/images/editorial-browser.webp"
classification: "agent-native"
dossier_path: "services/browser-and-web-execution/browser-mcp.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browser-mcp.md"
tagline: "Browser MCP server for AI agents"
website: "https://browsermcp.io/"
repository: "https://github.com/BrowserMCP/mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Browser &amp; Web Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://browsermcp.io/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/BrowserMCP/mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/browser-and-web-execution/browser-mcp.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

A coding assistant that needs to click through a web form has two broad options. It can rent a remote browser session, or it can be handed a browser through the same tool protocol it already uses for everything else. Browser MCP takes the second route. Its tagline, "Browser MCP server for AI agents," says what it is, and the dossier names the moving parts: Puppeteer behind an MCP server, actions based on the accessibility tree, and optional vision.

### One npx line, one browser

The documented start is a single command, `npx -y @browsermcp/mcp`. That launches the server, and an MCP-capable client registers it like any other tool server. From there the agent calls browser actions as MCP tools. Working from the accessibility tree means the agent acts on named elements and roles. Vision is listed as optional, and the docs are where to learn when it applies. The dossier does not list the tool names, so read the [project site](https://browsermcp.io/) and the repository before writing prompts that assume a particular action exists.

MCP is the primary surface and is marked as verified. There is no dedicated Agent Skill in the catalog. Nothing in the record describes a hosted fleet, an account, or an API key, which points to a process you run next to the agent rather than a service you subscribe to.

### Measured against hosted sessions

The [browser and web execution collection](/categories/browser-and-web-execution/) mixes engines you run with sessions you rent, and the [browser infrastructure guide](/guides/browser-infrastructure-for-agents/) separates them by job. Browser MCP sits on the run-it-yourself side. [Browserbase](/services/browserbase/) and [Steel](/services/steel/) sell remote browser sessions with their own infrastructure. [Vercel Agent Browser](/services/agent-browser/) is also local, but reaches the agent as a command-line tool rather than an MCP server. That last difference decides how you wire it: a tool registered in the client config, or a binary the agent shells out to.

Running locally has consequences the dossier does not spell out. Which browser profile does the server drive? Are cookies and logins from earlier sessions visible to the agent? What happens when two agents call it at once? The record's identity section is generic, stating only that delegation comes from runtime boundaries or caller credentials. For a browser, the runtime boundary is the machine and whatever profile is open on it. Find out from the vendor what the server can reach before you let an agent loose on a logged-in account.

### Editor's take

Browser MCP suits a developer who already lives in an MCP client and wants browser control on the same machine with one command. Teams running many unattended tasks in parallel, or handling pages that must not touch a personal profile, should compare Browserbase or Steel, whose sessions run away from your machine. If the agent prefers shell commands to tool calls, Vercel Agent Browser is the closer sibling. These conclusions rest on the catalog entry, the project site, and the repository; the server has not been installed or pointed at a page by anyone working on this index.

</section>

## What it does

Browser MCP provides browser MCP server for AI agents. Its agent-facing value is to give autonomous systems a programmatic primitive that can be invoked during a task loop without requiring a human to operate a dashboard for each action.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, http
- **MCP:** ✅ Verified/documented by upstream or MCP server listings.
- **Agent Skill:** ⚠️ No dedicated catalog skill verified in this entry. Search ClawHub or the upstream README for the latest installable skills.
- **Onboarding type:** `mcp`

## Protocol surface

| Interface | Detail |
|---|---|
| **Primary surface** | Puppeteer MCP, accessibility-tree actions, optional vision |
| **Repository** | https://github.com/BrowserMCP/mcp |
| **MCP** | ✅ |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/browser-and-web-execution/' | relative_url }}"><small>Collection</small><strong>← Browser &amp; Web Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
