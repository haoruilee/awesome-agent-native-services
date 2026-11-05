---
title: "pi-dispatch | Agent-Native Services"
service_name: "pi-dispatch"
description: "Run the pi coding agent as a service — triggered on demand, on a cron schedule, or by a GitHub or GitLab issue, comment or pull/merge request — in a…"
permalink: /services/pi-dispatch/
page_kind: service
service_slug: "pi-dispatch"
category_slug: "durable-execution-and-scheduling"
category_label: "Durable Execution & Scheduling"
hero_image: "/assets/images/editorial-durable.webp"
image: "/assets/images/editorial-durable.webp"
classification: "agent-native"
dossier_path: "services/durable-execution-and-scheduling/pi-dispatch.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/pi-dispatch.md"
tagline: "Run the pi coding agent as a service — triggered on demand, on a cron schedule, or by a GitHub or GitLab issue, comment or pull/merge request — in a container you control, with a durable queue, a spend cap, and a live admin panel"
verified_at: "2026-09-26"
website: "https://github.com/edgehero/pi-dispatch"
repository: "https://github.com/edgehero/pi-dispatch"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Durable Execution &amp; Scheduling</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · webhook · CLI</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/edgehero/pi-dispatch" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/edgehero/pi-dispatch#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/edgehero/pi-dispatch" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/pi-dispatch.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

pi-dispatch turns the pi coding agent into a self-hosted background service. CLI submissions, cron schedules, and GitHub, GitLab, Forgejo/Gitea, or Azure DevOps events enter one BullMQ/Valkey queue. A worker checks spend and turn limits, starts a locked-down ephemeral container, runs one committed skill against the target repository, records the result and usage, and removes the container.

It is scheduling and job-level durability rather than a general step-checkpoint workflow engine. Queue state survives restarts, jobs can be paused without being dropped, and selected follow-up triggers can resume the session that opened a pull request. The operator console provides run history, cost attribution, trigger/flow topology, quiet hours, and a global stop control.

---

## Agent-facing interfaces

- **Interaction pattern:** Daemon / Extension + CLI
- **Catalog protocols:** Agent Skill, webhook, CLI
- **MCP:** ⚠️ No MCP server published. pi-dispatch exposes pi extension tools and a CLI rather than MCP.
- **Agent Skill:** ✅ Available in the admin pi package
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** Daemon / Extension + CLI

```bash
# Guided setup from pi
pi install npm:@edgehero/pi-dispatch-admin
# Then type /dispatch inside pi and follow the setup prompts.

# Headless setup and first job
mkdir my-dispatch && cd my-dispatch
npx @edgehero/pi-dispatch up
npx @edgehero/pi-dispatch worker
npx @edgehero/pi-dispatch run ./my-project --task "add type hints" --flow tidy
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/durable-execution-and-scheduling/pi-dispatch.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `pi-dispatch up`, `worker`, `run`, `pause`, `resume`, `status`, `service`, `sandbox`, and setup commands |
| pi Extension | `/dispatch` TUI and model-callable `dispatch_*` observation/control tools |
| Forge Events | HMAC-verified webhooks or polling for GitHub; webhook receivers for GitLab, Forgejo/Gitea, and Azure DevOps |
| Queue | BullMQ over Valkey with AOF persistence, deduplication, retention, and concurrency control |
| Configuration | `triggers.json`, pause windows, environment variables, committed `.pi/skills`, and pinned staged pi packages |
| Run History | Durable structured records plus a per-model token/cost ledger and generated insights report |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/edgehero/pi-dispatch/releases/tag/v1.10.3
- https://api.github.com/repos/edgehero/pi-dispatch

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/durable-execution-and-scheduling/' | relative_url }}"><small>Collection</small><strong>← Durable Execution &amp; Scheduling</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
