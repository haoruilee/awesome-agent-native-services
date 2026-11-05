---
title: "Polos | Agent-Native Services"
service_name: "Polos"
description: "The open-source runtime for AI agents. Sandboxed execution with built-in tools, human-in-the-loop approvals, Slack integration, and durable workflows with…"
permalink: /services/polos/
page_kind: service
service_slug: "polos"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/polos.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/polos.md"
tagline: "The open-source runtime for AI agents. Sandboxed execution with built-in tools, human-in-the-loop approvals, Slack integration, and durable workflows with automatic retries and prompt caching. You write the agent. Polos handles the infrastructure"
website: "https://github.com/polos-dev/polos"
repository: "https://github.com/polos-dev/polos"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Open source · early-stage · Jan 2026 launch</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Planned</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">webhook · SDK · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/polos-dev/polos" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/polos-dev/polos#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/polos-dev/polos" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/polos.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Polos is an **opinionated runtime for AI agents** that bundles four concerns into one stack:

1. **Sandboxed execution** — agent code runs in a Docker or E2B container with a clean, throw-away filesystem and a built-in tool kit (exec, files, search).
2. **Durable workflow** — each step is checkpointed; on failure, the runtime retries with prompt cache hits to avoid re-paying LLM costs.
3. **Multiple triggers** — HTTP, webhook, cron, and event triggers are first-class; agents are deployed once and react to many sources.
4. **HITL via Slack / UI** — pause-and-approve gates without ad-hoc plumbing.

The pitch is that it sits in the gap between code-execution sandboxes (E2B) and durable workflow engines (Trigger.dev, Inngest): you get both, agent-shaped, in one runtime — at small-team operational cost.

---

## Agent-facing interfaces

- **Catalog protocols:** webhook, SDK, http
- **MCP:** ⚠️ Not yet published as a first-party MCP server. Polos consumes MCP tools (it can call any MCP server from inside the sandbox); a server-side MCP surface is on the roadmap.
- **Agent Skill:** ⚠️ Not yet published.
- **Onboarding type:** `sdk`

## How agents onboard

```
# Install:
pip install polos
# or
npm install polos

# Run an agent inside the runtime:
import polos

@polos.agent(triggers=["http", "cron", "webhook"])
def my_agent(ctx): ...
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/polos.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install polos` |
| TypeScript SDK | `npm install polos` |
| HTTP / webhook / cron / event triggers | All first-class |
| Slack integration | HITL approval channel |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
