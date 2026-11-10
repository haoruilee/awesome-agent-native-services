---
title: "CodeRunner | Agent-Native Services"
service_name: "CodeRunner"
description: "A local sandbox for your AI agents"
permalink: /services/coderunner/
page_kind: service
service_slug: "coderunner"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/coderunner.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/coderunner.md"
tagline: "A local sandbox for your AI agents"
website: "https://github.com/instavm/coderunner"
repository: "https://github.com/instavm/coderunner"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/instavm/coderunner" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/instavm/coderunner" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/coderunner.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

The host constraint comes first. The dossier lists the surfaces as Apple Containers, a local sandbox CLI, and MCP, so the agent has to run on, or reach, a Mac set up with Apple's container tooling. An MCP-capable client is the natural caller. The catalog also lists HTTP, though the dossier does not describe an HTTP interface. No Agent Skill has been verified.

### Isolation on the developer's own machine

The tagline is "A local sandbox for your AI agents." The How to Use line says to install from GitHub and run agent workloads in isolated Apple containers. Those two sentences carry nearly all the product-specific information in the entry. The remaining sections follow the catalog's template for recent candidates and describe session boundaries, audit trails, and delegation in terms broad enough to fit many sandboxes.

What can be said with confidence: code the agent writes runs in a container on the local machine instead of directly on the host, and an MCP client can request that. The [repository](https://github.com/instavm/coderunner) serves as website, docs, and code, since the catalog has no separate docs URL. The dossier does not say which languages are available, whether files persist between runs, how the container gets network access, or which MCP tools are offered.

### Local against hosted

[Code Execution](/categories/code-execution/) offers three broad choices. Hosted sandboxes such as [E2B](/services/e2b/) and [Vercel Sandbox](/services/vercel-sandbox/) run code on vendor infrastructure behind an API key. Self-run platforms such as [OpenSandbox](/services/opensandbox/) and [Axern](/services/axern/) move that onto your servers. Local options like CodeRunner keep everything on the laptop. [AIO Sandbox](/services/agent-infra-sandbox/) is a single Docker container combining browser, shell, files, MCP, and VS Code Server, which makes it the nearest local alternative outside Apple's tooling.

Local execution means no network hop and no code leaving the machine, which matters for private repositories. The cost is that isolation is only as strong as the local container runtime, and capacity ends at one machine. The [sandboxes guide](/guides/sandboxes-and-code-execution/) compares those properties across the category.

### Read the README for these

Check the macOS version and hardware that Apple Containers requires. Find out what the container can see of the host filesystem and network by default. Confirm whether state is cleared between tasks or carried forward. Look at how actively the project is maintained.

### Editor's take

Mac-based developers who want their coding agent to execute generated code locally, without sending it to a cloud sandbox, are the obvious fit. Linux and Windows users should compare AIO Sandbox. Teams that need many concurrent sandboxes or shared infrastructure belong with E2B, Vercel Sandbox, or a self-run platform. With a dossier this short, the judgement here is mostly inference from the tagline, the install line, and the public repository; the project has not run CodeRunner.

</section>

## What it does

CodeRunner provides a local sandbox for your AI agents. Its agent-facing value is to give autonomous systems a programmatic primitive that can be invoked during a task loop without requiring a human to operate a dashboard for each action.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, http
- **MCP:** ✅ Verified/documented by upstream or MCP server listings.
- **Agent Skill:** ⚠️ No dedicated catalog skill verified in this entry. Search ClawHub or the upstream README for the latest installable skills.
- **Onboarding type:** `other`

## Protocol surface

| Interface | Detail |
|---|---|
| **Primary surface** | Apple Containers, local sandbox CLI, MCP |
| **Repository** | https://github.com/instavm/coderunner |
| **MCP** | ✅ |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
