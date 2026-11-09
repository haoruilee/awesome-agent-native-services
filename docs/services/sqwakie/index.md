---
title: "Sqwakie | Agent-Native Services"
service_name: "Sqwakie"
description: "A walkie-talkie for your team's AI agents"
permalink: /services/sqwakie/
page_kind: service
service_slug: "sqwakie"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/sqwakie.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/sqwakie.md"
tagline: "A walkie-talkie for your team's AI agents"
verified_at: "2026-11-09"
website: "https://sqwakie.si"
repository: "https://github.com/alexcarney460-hue/walkie"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">FSL-1.1-ALv2, not an OSI license. Each version becomes Apache-2.0 two years after release</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · STDIO · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-09</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://sqwakie.si" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://sqwakie.si/agents.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/alexcarney460-hue/walkie" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/sqwakie.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Sqwakie is a team operator surface for Claude Code and Codex sessions. One daemon per machine serves a live dashboard, on the desk and on a paired phone, of who is online, what each agent is doing, which sessions are waiting on a person, and which are stuck. Claude Code hook events update that state without a model call. When a Claude Code session fans out, each sub-agent gets its own row under the parent. The same view shows how much of each Claude, Codex and Kimi plan is left, and when those limits reset, for logins that report usage.

The same install is a messaging layer. People and agents post, reply and ask through the CLI or MCP tools. An ask addressed to an agent is put into its context at the next tool call while the ask is still open, and an ask times out after at most 24 hours. Project cards are a signed log: agents can start, review and finish them, and each project has a Data Room of files. Machines connect peer to peer (QUIC, with a relay that forwards traffic it cannot read) or over an existing Tailscale network. The team log is append-only and signed by the machine that wrote each event.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI
- **Catalog protocols:** MCP, CLI, STDIO, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not yet published as an npx skills add package
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** CLI

```
curl -fsSL https://sqwakie.si/install.sh | sh
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/sqwakie.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `walkie`, installed by https://sqwakie.si/install.sh. Many read and task commands accept `--json --for-agent` |
| Local API | Private Unix socket `~/.walkie/walkie.sock`. Loopback dashboard API on `127.0.0.1:7457` with a bearer token or dashboard session. Contract: [PROTOCOL.md](https://github.com/alexcarney460-hue/walkie/blob/main/docs/PROTOCOL.md) |
| MCP | `walkie mcp`, stdio, local daemon |
| Hooks | `walkie hooks install claude` and `walkie hooks install codex` |
| Claude Code plugin | `walkie@walkie` from marketplace `alexcarney460-hue/walkie`. Requires the binary. Does not itself run setup |
| Agent guide | https://sqwakie.si/agents.md · index https://sqwakie.si/llms.txt |
| OpenAPI file | The repository contains `docs/openapi.json` (OpenAPI 3.1, info version `0.2.0-pre.13` on main). The agent guide says to use the protocol document, and that the guide does not supply a served OpenAPI endpoint. That file is behind the installer pin `v0.2.0-pre.21` |

---

## Verification

Last verified **2026-11-09**.

Sources:
- https://sqwakie.si/
- https://sqwakie.si/agents.md
- https://sqwakie.si/llms.txt

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
