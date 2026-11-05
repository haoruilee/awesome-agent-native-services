---
title: "ClawHub | Agent-Native Services"
service_name: "ClawHub"
description: "Claw Hub: OpenClaw Skill Marketplace"
permalink: /services/clawhub/
page_kind: service
service_slug: "clawhub"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/clawhub.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/clawhub.md"
tagline: "Claw Hub: OpenClaw Skill Marketplace"
website: "https://claw-hub.net/"
repository: "https://github.com/openclaw/clawhub"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · CLI · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://claw-hub.net/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/openclaw/clawhub/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/openclaw/clawhub" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/clawhub.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

ClawHub is the **public skill marketplace for OpenClaw-style agents**: browse thousands of versioned **`SKILL.md`** bundles, run **embedding-based search**, install and update skills locally from the CLI, and **publish** new versions with changelogs and tags. It also hosts an **OpenClaw package catalog** (code and bundle plugins) with family/trust/capability metadata. The stack pairs a web UI with a **Convex-backed** API, **GitHub OAuth** for publishers, moderation workflows, and optional **install telemetry** (disable with `CLAWHUB_DISABLE_TELEMETRY=1` per [telemetry.md](https://github.com/openclaw/clawhub/blob/main/docs/telemetry.md)).

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, CLI, http, API
- **MCP:** ⚠️ ClawHub is a skill and package registry, not an MCP server directory. Integration is via the CLI and HTTP/registry APIs (consumers are agent hosts that load SKILL.md and tooling, not MCP tools/list).
- **Agent Skill:** ✅ ClawHub is a public registry of Agent Skills (and related OpenClaw packages). Skills are installed with the CLI; this catalog’s companion skills live under .skills/ and publish via ClawHub.
- **Onboarding type:** `agent-skill`

## How agents onboard

```bash
npx clawhub@latest login
npx clawhub@latest search <topic>
npx clawhub@latest install <skill-slug>
npx clawhub@latest list
npx clawhub@latest update --all
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/clawhub.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| `clawhub` CLI | `npx clawhub@latest` — search, install, publish, package explore/publish per [docs/cli.md](https://github.com/openclaw/clawhub/blob/main/docs/cli.md) |
| HTTP / JSON API | Convex HTTP actions — metadata, downloads (zip), described in [docs/spec.md](https://github.com/openclaw/clawhub/blob/main/docs/spec.md) |
| Shared schema | `packages/schema` (`clawhub-schema`) for CLI and app alignment |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
