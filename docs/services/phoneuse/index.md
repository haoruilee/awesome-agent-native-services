---
title: "PhoneUse | Agent-Native Services"
service_name: "PhoneUse"
description: "Your agent now has a phone"
permalink: /services/phoneuse/
page_kind: service
service_slug: "phoneuse"
category_slug: "agent-runtime-and-infrastructure"
category_label: "Agent Runtime & Infrastructure"
hero_image: "/assets/images/editorial-runtime.webp"
image: "/assets/images/editorial-runtime.webp"
classification: "agent-native"
dossier_path: "services/agent-runtime-and-infrastructure/phoneuse.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/phoneuse.md"
tagline: "Your agent now has a phone"
verified_at: "2026-11-25"
website: "https://www.phoneuse.com"
repository: "https://github.com/phoneuse-official/phoneuse"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Runtime &amp; Infrastructure</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT for the local USB iPhone repo (Copyright 2026 PhoneUse contributors); the hosted cloud control plane is a separate commercial product</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-11-25</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.phoneuse.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.phoneuse.com/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/phoneuse-official/phoneuse" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/phoneuse.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

PhoneUse's hosted product is a mobile execution layer: an agent leases a device, acts on it, and reads a trace. The public GitHub project is the local USB iPhone stack on a Mac. The website also offers a robot hand on a physical iPhone for traffic that must look like a person holding the phone. Cloud Android is the scale path described on the homepage.

On 2026-11-25 the API process was up and answered healthz, and it labeled itself degraded. Fleet integrity and the cloud renewal scan were not ok. Provisioning was still running and ok. Treat a lease as subject to that fleet state.

---

## Agent-facing interfaces

- **Interaction pattern:** hosted control-plane MCP + REST, after a human-minted key. Not a one-URL join.
- **Catalog protocols:** MCP, REST, http, API
- **MCP:** ✅ Available — hosted control-plane Streamable HTTP. Interactive OAuth is not live yet.
- **Agent Skill:** ⚠️ Not yet published
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** hosted control-plane MCP + REST, after a human-minted key. Not a one-URL join.

```bash
# Control-plane MCP (stateless Streamable HTTP): https://mcp.phoneuse.com/mcp
# Docs for agents: https://docs.phoneuse.com/getting-started/for-agents.md
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-runtime-and-infrastructure/phoneuse.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | Control-plane HTTP API. Start at https://docs.phoneuse.com/getting-started/for-agents.md |
| Hosted MCP | `https://mcp.phoneuse.com/mcp` |
| Health | `https://mcp.phoneuse.com/healthz` |
| Docs | https://docs.phoneuse.com/ |
| Docs index | https://docs.phoneuse.com/llms.txt |
| Local USB repo | https://github.com/phoneuse-official/phoneuse — MIT, not the cloud fleet |

---

## Verification

Last verified **2026-11-25**.

Sources:
- https://www.phoneuse.com
- https://docs.phoneuse.com/
- https://mcp.phoneuse.com/mcp
- https://mcp.phoneuse.com/healthz
- https://github.com/phoneuse-official/phoneuse

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-runtime-and-infrastructure/' | relative_url }}"><small>Collection</small><strong>← Agent Runtime &amp; Infrastructure</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
