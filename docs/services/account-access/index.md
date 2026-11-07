---
title: "Account Access | Agent-Native Services"
service_name: "Account Access"
description: "Connect once. Grant specific permissions. Let your existing AI agent do the routine work"
permalink: /services/account-access/
page_kind: service
service_slug: "account-access"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/account-access.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/account-access.md"
tagline: "Connect once. Grant specific permissions. Let your existing AI agent do the routine work"
website: "https://github.com/fainir/account-access"
repository: "https://github.com/fainir/account-access"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">0.7.4 public preview; reviewed connectors required for real websites</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · CLI · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/fainir/account-access" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/fainir/account-access/blob/main/docs/setup.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/fainir/account-access" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/account-access.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Account Access is a local authentication and delegated-access service for existing agents. The service manages credentials, sessions, renewal and resumable tasks while an agent requests fixed, owner-approved operations. Owner setup is separate from the agent API.

The [public README](https://github.com/fainir/account-access) identifies this as a preview: real websites require reviewed connectors. It does not establish validated production access to arbitrary websites, banks, Google, Meta or insurance accounts. Local operation under the same OS user is a trusted-agent pilot, not isolation from an agent with unrestricted shell access.

---

## Agent-facing interfaces

- **Interaction pattern:** Agent Skill + structured CLI over a local service.
- **Catalog protocols:** Agent Skill, CLI, API
- **MCP:** ⚠️ Not published; MCP is not a dependency.
- **Agent Skill:** ✅ Available through the official installer.
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** Agent Skill + structured CLI over a local service.

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/account-access.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Agent Skill | Portable `SKILL.md` integration, automatically discovered by supported hosts |
| Structured CLI | Account discovery, approved reads, durable task submission and inspection |
| Private service API | Unix-domain socket with bearer authentication; separate from owner setup |
| Provider adapters | Reviewed OAuth or browser reads under fixed operation and destination boundaries |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
