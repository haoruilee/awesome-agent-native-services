---
title: "ParallelSandbox | Agent-Native Services"
service_name: "ParallelSandbox"
description: "A row of in-progress test builds of your app"
permalink: /services/parallelsandbox/
page_kind: service
service_slug: "parallelsandbox"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/parallelsandbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/parallelsandbox.md"
tagline: "A row of in-progress test builds of your app"
website: "https://parallelsandbox.com/en/"
repository: "https://github.com/parallel-sandbox/parallelsandbox-mcp"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · MCP · REST · SDK · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://parallelsandbox.com/en/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://parallelsandbox.com/en/docs/quickstart/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/parallel-sandbox/parallelsandbox-mcp" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/parallelsandbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

ParallelSandbox gives a coding agent a remote Linux machine (a "box") for each piece of work: a small virtual machine with its own disk and network, Docker, git, Node, Go, Python, Chromium and a virtual display. The agent starts a box with a goal, copies the project in, runs commands, docker compose stacks and browser tests there, and takes screenshots and screen recordings of what it built. Several boxes run at once, isolated from each other and from the person's own computer.

When a version works, the agent hands it to a person with `sandbox_review`. The person opens it as a user (a web page, or a phone or desktop app on the box's screen), says what is wrong and circles it on the screen; the recording, circled screenshots and transcript come back to the same agent conversation, and the agent makes the next version. For steps only a person can do, such as a login, a second factor or a payment, the agent asks for a takeover of the box's live screen and gets control back afterwards.

Before building, the agent can propose screens (`sandbox_draft`), services (`sandbox_architecture`) and data schemas (`sandbox_schema`) for the person to mark up. Idle boxes freeze and stop billing, and are stopped after a set time.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⚠️ — partial.
- **Catalog protocols:** URL onboarding, Agent Skill, MCP, REST, SDK, STDIO, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⚠️ — partial.

```
Read https://parallelsandbox.com/skill/SKILL.md and follow the instructions to install the ParallelSandbox skill and complete the connection.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/parallelsandbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | `https://mcp.parallelsandbox.com/mcp`, Streamable HTTP, OAuth |
| MCP stdio adapter | `npx -y parallelsandbox-mcp` (MIT, Node 20+), adds local file transfer |
| REST API | https://parallelsandbox.com/en/docs/tools/rest/ |
| Browser log SDK | `@parallelsandbox/log` — https://parallelsandbox.com/en/docs/log-sdk/ |
| Agent Skill | `npx skills add parallel-sandbox/parallelsandbox-mcp` |
| Docs for agents | https://parallelsandbox.com/llms.txt, https://parallelsandbox.com/skill/SKILL.md |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
