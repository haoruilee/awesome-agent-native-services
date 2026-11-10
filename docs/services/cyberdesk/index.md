---
title: "Cyberdesk | Agent-Native Services"
service_name: "Cyberdesk"
description: "Open source virtual desktops for AI agents"
permalink: /services/cyberdesk/
page_kind: service
service_slug: "cyberdesk"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/cyberdesk.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cyberdesk.md"
tagline: "Open source virtual desktops for AI agents"
website: "https://www.cyberdesk.io"
repository: "https://github.com/cyberdesk-hq/cyberdesk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.cyberdesk.io" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.cyberdesk.io" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/cyberdesk-hq/cyberdesk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cyberdesk.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

An agent driving these desktops calls an SDK or API, and the model behind it has to work from screenshots and emit clicks and keystrokes. The dossier's install line is `pip install cyberdesk`, after which you create a desktop and send computer actions through the SDK or API. MCP is not the primary surface; the dossier calls the product API/SDK-first. No `SKILL.md` package exists yet.

### Desktops as disposable sessions

The tagline is "Open source virtual desktops for AI agents." The dossier describes cloud-hosted virtual desktops an agent controls with mouse, keyboard, screenshot, and app or browser interaction, in isolated sessions with auditable execution. Primitives are desktop create, start, stop, and delete; computer-use actions such as click, type, keypress, and screenshot; isolated sessions for concurrent agents; and execution logs.

The autonomy loop is: create a session, act, read the output, continue, then terminate or archive the session. Screenshots and logs are kept as session artifacts for replay, debugging, or compliance review. API keys identify the workspace and caller, and each session is attributable to a run. Humans can observe, review, or take over, though default operation is agent-driven.

One tension in the entry is worth resolving with the vendor. The tagline says open source, while the protocol section describes a cloud runtime. The dossier does not say whether you can host desktops yourself, which operating systems are offered, or how a human takeover works. Check the [Cyberdesk docs](https://docs.cyberdesk.io) and the [repository](https://github.com/cyberdesk-hq/cyberdesk).

### Where a desktop fits among runtimes

[Agent Runtime & Infrastructure](/categories/agent-runtime-and-infrastructure/) mostly hosts the agent itself. [Modal](/services/modal/) runs code, [Letta](/services/letta/) holds stateful agents, and the [Cloudflare Agents SDK](/services/cloudflare-agents-sdk/) hosts durable agents on Cloudflare. Cyberdesk hosts the environment an agent acts upon, which is a different layer. You might run the agent on Modal and point it at a Cyberdesk session.

Desktop control is the fallback for software without an API. When an API exists, a tool call is cheaper and easier to verify than a click sequence. Pairing desktop sessions with [APort Agent Guardrails](/services/aport-agent-guardrails/) for pre-action checks is one way to constrain what a computer-use agent can do. The [agent-native guide](/guides/what-makes-a-service-agent-native/) explains why lifecycle APIs for desktops count as agent primitives.

### Before handing it a workflow

Confirm what is retained in screenshots, since a session can capture anything on screen, including customer data. Check quota and concurrency behavior under your workspace key. Find out how credentials for applications inside the desktop are supplied and where they are stored.

### Editor's take

Teams automating back-office work in legacy desktop or web applications with no usable API are the intended users, especially where recorded sessions help with review. If the target system has an API, connect to it directly and skip the desktop. If you only need to run code, Modal is simpler. The dossier and Cyberdesk's public docs are the whole basis for this; we have not opened a session.

</section>

## What it does

Cyberdesk provides cloud-hosted virtual desktops that AI agents can control programmatically (mouse, keyboard, screenshot, app/browser interaction) with isolated sessions and auditable execution.

---

## Agent-facing interfaces

- **Catalog protocols:** SDK, API
- **MCP:** ⚠️ Not MCP-first.
- **Agent Skill:** ⚠️ No official SKILL.md package published yet.
- **Onboarding type:** `sdk`

## How agents onboard

```bash
pip install cyberdesk
# then create a desktop and execute computer actions via SDK/API
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/cyberdesk.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| SDK/API | Desktop lifecycle + computer-use action primitives |
| Session artifacts | Screenshots/logs for replay, debugging, or compliance review |
| Cloud runtime | Remote execution environment for agent browser/desktop tasks |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
