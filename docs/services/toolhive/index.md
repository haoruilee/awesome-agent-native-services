---
title: "ToolHive | Agent-Native Services"
service_name: "ToolHive"
description: "Run any MCP server securely, instantly, anywhere"
permalink: /services/toolhive/
page_kind: service
service_slug: "toolhive"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/toolhive.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhive.md"
tagline: "Run any MCP server securely, instantly, anywhere"
website: "https://stacklok.com/download/"
repository: "https://github.com/stacklok/toolhive-studio"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://stacklok.com/download/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.stacklok.com" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/stacklok/toolhive-studio" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhive.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

The first requirement sits on the operator's machine rather than in the agent: someone installs the `thv` CLI, and only then can an agent client connect to the MCP servers it runs. The dossier prints the install as `brew tap stacklok/tap`, `brew install thv`, and `thv --help`, then points to the docs for runtime commands. Managed servers are offered to stdio, socket, or HTTP-compatible clients. No Agent Skill is published.

### A control plane for MCP servers

The tagline is "Run any MCP server securely, instantly, anywhere." The dossier describes a control plane covering discovery, deployment, sandboxed execution, and secure connection for agent runtimes and coding assistants. Primitives are server install and discovery, runtime lifecycle management, isolation and security policy for MCP execution, and agent-client connection management.

The autonomy model is a short sequence: install `thv`, select servers, run them in isolated contexts, connect clients to approved endpoints. The dossier says agents can drive this non-interactively. Access is controlled by runtime and environment credentials, and teams can restrict which servers each agent environment sees. Humans approve the server list; agents then call approved tools without per-action confirmation.

What the dossier does not explain is the isolation mechanism, how secrets reach a running server, or how the server catalog is curated. The [Stacklok docs](https://docs.stacklok.com) cover operational configuration. The GitHub link in the catalog points at the desktop app repository.

### Runner versus server

Most of [Tool Access & Integration](/categories/tool-access-and-integration/) lists servers. [Apify MCP Server](/services/apify-mcp-server/), [Framelink MCP for Figma](/services/framelink-figma-mcp/), and [MCP Toolbox for Databases](/services/google-mcp-toolbox/) each expose one domain. ToolHive sits a layer below them, as the place those servers might run with policy around them.

Two other neighbors overlap in purpose. [Snyk Agent Scan](/services/snyk-agent-scan/) inspects servers for security problems, which complements running them in isolation. [Arcade](/services/arcade/) and [Nango](/services/nango/) handle OAuth so credentials stay away from the model, a concern ToolHive's dossier touches only as per-environment credentials. The [MCP servers guide](/guides/getting-started-with-mcp-servers/) covers the stdio and HTTP transports a runner like this manages.

### Points to settle with Stacklok

Check what the isolation boundary is and what a misbehaving server can still reach. Confirm how the allowed server list is enforced when several developers share one policy. Find out whether central management exists or only the local CLI and desktop app. Read how secrets are injected and whether the server process can see them in plain form.

### Editor's take

Platform teams standardizing MCP across many developers or agent environments, and wanting an approved list with isolation, should evaluate ToolHive early. A single developer adding one server to one editor gains little from a control plane. If credentials are the actual problem, Arcade or Nango addresses it more directly. I have read the dossier and Stacklok's docs; ToolHive has not been installed or run for this page.

</section>

## What it does

ToolHive provides a control plane for MCP servers: discovery, deployment, sandboxed execution, and secure connection for agent runtimes and coding assistants.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, STDIO, http, API
- **MCP:** ✅ Core product.
- **Agent Skill:** ⚠️ No official AgentSkills package yet.
- **Onboarding type:** `cli`

## How agents onboard

```bash
brew tap stacklok/tap
brew install thv
thv --help
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/toolhive.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `thv` install/run/manage lifecycle |
| MCP | Runs MCP servers for stdio/socket/HTTP-compatible clients |
| Docs/API | Operational configuration and server management workflows |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
