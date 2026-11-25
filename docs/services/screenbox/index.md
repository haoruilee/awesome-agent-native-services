---
title: "Screenbox | Agent-Native Services"
service_name: "Screenbox"
description: "Real desktops for AI agents"
permalink: /services/screenbox/
page_kind: service
service_slug: "screenbox"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/screenbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/screenbox.md"
tagline: "Real desktops for AI agents"
verified_at: "2026-11-25"
website: "https://screenbox.dev"
repository: "https://github.com/dklymentiev/screenbox"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">AGPL-3.0 (LICENSE file; GitHub SPDX was NOASSERTION on 2026-11-25)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-25</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://screenbox.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/dklymentiev/screenbox" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/dklymentiev/screenbox" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/screenbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Screenbox is a self-hosted desktop runtime for MCP agents. Each desktop is an isolated Docker container with Chromium. The agent sees, clicks, types, and navigates. Snapshots save and restore state. Files move through the API, not through a bind mount of the host (README: *"No bind mounts — files move only through explicit API calls."*). A person can watch or take over with RDP or VNC. Takeover is optional.

The homepage `llms.txt` is only a title and a contact line. The README is the setup document.

---

## Agent-facing interfaces

- **Interaction pattern:** self-hosted Docker Compose and a local MCP URL. Not a one-URL join.
- **Catalog protocols:** MCP, http
- **MCP:** ✅ Available — local Streamable HTTP after you start the stack
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** self-hosted Docker Compose and a local MCP URL. Not a one-URL join.

```bash
git clone https://github.com/dklymentiev/screenbox
cd screenbox
./setup.sh
docker compose up -d
# Dashboard: http://localhost:16000
# MCP: http://localhost:8080/mcp
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/screenbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | `http://localhost:8080/mcp` |
| Dashboard | `http://localhost:16000` |
| Runtime | Docker Compose — https://github.com/dklymentiev/screenbox |
| Website | https://screenbox.dev |

---

## Verification

Last verified **2026-11-25**.

Sources:
- https://screenbox.dev
- https://github.com/dklymentiev/screenbox

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
