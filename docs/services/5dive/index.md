---
title: "5dive | Agent-Native Services"
service_name: "5dive"
description: "Run a company of AI agents on a server you own"
permalink: /services/5dive/
page_kind: service
service_slug: "5dive"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/5dive.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/5dive.md"
tagline: "Run a company of AI agents on a server you own"
verified_at: "2026-11-24"
website: "https://5dive.ai"
repository: "https://github.com/5dive-ai/5dive"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · webhook · CLI</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-24</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://5dive.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://5dive.ai/docs/5dive-cli" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/5dive-ai/5dive" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/5dive.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

5dive is a self-hosted runtime and operator surface for a team of CLI agents on the operator's own Linux server. It runs agents such as Claude Code and Codex (the README also lists OpenClaw, Hermes, Antigravity, Grok, OpenCode and Pi) as persistent Linux services. Each agent is its own Linux user with its own permissions and its own systemd service. Agents share one task queue stored in SQLite, hand work to each other, and a second agent can check the work before a task closes. Cron and webhooks trigger work, journald keeps the logs, and coordination goes through the `5dive` CLI, with no external orchestrator.

The operator watches and steers the team from the same CLI. `5dive watch` and `5dive wall` show the team working, live. `activity <agent>` shows what each agent actually did, and `sudo 5dive usage` shows who used the plan's limits. `5dive trace <task>` gives a task's history from the request to the verdict, and `5dive reflex log` keeps a receipt for each routine decision, such as who got a task and why. Permissions are `sandboxed`, `standard` or `admin`, and human approvals are configurable; `5dive human add` sends a person's agents' approvals to that person.

The primary consumer is the human operator of that agent team, and the primary interface is the `5dive` CLI on the server. This entry is admitted on the **operator-surface track**.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding ⚠️ — partial.
- **Catalog protocols:** URL onboarding, Agent Skill, webhook, CLI
- **MCP:** ⚠️ Not documented in the 5dive README
- **Agent Skill:** ✅ Available
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding ⚠️ — partial.

```
Install 5dive on this server: curl -fsSL https://install.5dive.ai | sudo bash
Then add the 5dive-cli skill: npx -y skills add https://github.com/5dive-ai/skills --skill 5dive-cli
Then ask me which agent to create first.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/5dive.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `5dive` on the server: agents, tasks, the approvals inbox, live views and traces; every command has `--help` |
| systemd / journald | One systemd service per agent; journald stores the logs |
| Task queue | SQLite, shared by every agent on the server |
| Agent Skill | `5dive-cli`, installed with `npx -y skills add` |
| Triggers | GitHub issues and webhook events become tasks (`5dive trigger add`); cron schedules run recurring tasks and loops |
| Human surfaces (optional) | The 5dive app (link the server at 5dive.ai/self-host), a daily digest in Telegram, and a read-only web dashboard plugin |
| Install | The `install.5dive.ai` script run as root, an apt package, Docker Compose, or the Vultr Marketplace |
| MCP | Not documented in the README |

---

## Verification

Last verified **2026-11-24**.

Sources:
- https://github.com/5dive-ai/5dive/releases/tag/v0.142.0
- https://5dive.ai
- https://github.com/5dive-ai/5dive/commit/f373b237a4f7356b92903dfeb45793af7fbf936a
- https://github.com/haoruilee/awesome-agent-native-services/issues/360#issuecomment-7118568294
- https://github.com/5dive-ai/5dive/commit/c615db886abbc3681470b02a2c4f467579367652

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
