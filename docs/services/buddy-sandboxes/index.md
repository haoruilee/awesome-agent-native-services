---
title: "Buddy Sandboxes | Agent-Native Services"
service_name: "Buddy Sandboxes"
description: "Secure, elastic infrastructure for AI-generated code and the apps it becomes - on a real Linux machine, not a throwaway container"
permalink: /services/buddy-sandboxes/
page_kind: service
service_slug: "buddy-sandboxes"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/buddy-sandboxes.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/buddy-sandboxes.md"
tagline: "Secure, elastic infrastructure for AI-generated code and the apps it becomes - on a real Linux machine, not a throwaway container"
website: "https://buddy.works/sandboxes"
repository: "https://github.com/buddy/sandbox-sdk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · SDK · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://buddy.works/sandboxes" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://buddy.works/docs/sandboxes" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/buddy/sandbox-sdk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/buddy-sandboxes.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Buddy Sandboxes are persistent Linux VMs for AI-generated code and agents. A Sandbox boots Ubuntu with Node, Docker, Go, Python 3, git, the `bdy` CLI and Claude Code preinstalled, with passwordless `sudo`. The disk survives stops and restarts, so files, packages and build caches are still there in the next session.

An agent creates a Sandbox over MCP, the SDK, the REST API or the CLI, fetches a repository into it, runs commands, starts long-running apps and publishes a port as an HTTPS endpoint. It can save a snapshot and start new Sandboxes from it, so each agent starts from a prepared toolchain instead of running `npm install` again. An optional inactivity timeout stops the machine, and traffic on an endpoint starts it again.

Inside the Sandbox, the `this` command changes the machine the agent is on: endpoints, apps, snapshots, resources, stop and destroy. It needs no Sandbox name and no access token.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, CLI, SDK, STDIO, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

```
# MCP (remote HTTP, OAuth sign-in in the browser):
claude mcp add --transport http buddy "https://mcp.buddy.works/mcp?tools=sandboxes"

# Coding-time Skill:
npx skills add buddy/buddy-plugin  # drives the bdy CLI: bdy login, bdy sandbox create

# SDK (token with SANDBOX_READ and SANDBOX_WRITE scopes):
npm install @buddy-works/sandbox-sdk  # then: await Sandbox.create({ identifier: "my-sandbox" })

# Inside a running Sandbox (no identifier, no token):
this endpoint add -e 5173
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/buddy-sandboxes.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | `https://mcp.buddy.works/mcp`, remote HTTP, OAuth or bearer token; `bdy mcp` as a stdio proxy |
| REST API | https://buddy.works/docs/api/sandboxes |
| SDK | `@buddy-works/sandbox-sdk` (TypeScript, MIT) |
| CLI | `bdy sandbox` (`bdy sb`); `this` inside a Sandbox |
| YAML | Sandbox definition with resources, apps, endpoints and permissions |
| Agent Skill | `npx skills add buddy/buddy-plugin` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
