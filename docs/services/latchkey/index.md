---
title: "Latchkey | Agent-Native Services"
service_name: "Latchkey"
description: "CI your coding agents can run, read and fix"
permalink: /services/latchkey/
page_kind: service
service_slug: "latchkey"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/latchkey.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/latchkey.md"
tagline: "CI your coding agents can run, read and fix"
website: "https://latchkey.dev"
repository: "https://github.com/latchkey-dev/cache-action"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · CLI · openapi · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://latchkey.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://latchkey.dev/documentation/connect-your-ai-agent" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/latchkey-dev/cache-action" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/latchkey.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Latchkey gives coding agents a place to actually execute and verify work. `run_job` (or `latchkey run` from the CLI) runs one command on a fresh ephemeral Ubuntu 24.04 x86_64 runner with no workspace and no GitHub in the path, then returns the command's own exit code and logs, so an agent can run a test suite on a clean machine before it opens a pull request.

The same runners execute GitHub Actions jobs and diagnose failing steps while the job is still running: exit codes, then a pattern library, then a time-boxed sandboxed AI stage. Transient failures (registry timeouts, OOM kills, full disks, missing tools) are fixed on the ephemeral runner and retried; real defects are never retried or masked. What the runner cannot fix reaches the agent as a failure bundle: root cause, exact failing file and secret-scrubbed logs.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, CLI, openapi, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `mcp`

## How agents onboard

```
# Agent instructions (when to use it, how to call it, MCP / REST / CLI):
Read https://latchkey.dev/agent.txt and follow the instructions.

# MCP (Streamable HTTP):
claude mcp add --transport http latchkey https://latchkey.dev/mcp --header "Authorization: Bearer $LATCHKEY_TOKEN"

# CLI:
npm install -g @latchkeydev/cli  # then: latchkey run 'npm test'
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/latchkey.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | `https://latchkey.dev/mcp`, Streamable HTTP, 8 tools, 2 prompts |
| REST Jobs API | `https://api.latchkey.dev`, OpenAPI 3.1 at https://latchkey.dev/openapi.json |
| CLI | `@latchkeydev/cli` — https://latchkey.dev/documentation/latchkey-cli |
| Agent instructions | https://latchkey.dev/agent.txt, https://latchkey.dev/llms.txt, markdown twin of every docs page at URL + `.md` |
| GitHub Actions | `runs-on: latchkey-small` (and larger sizes) for existing workflows |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
