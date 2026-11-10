---
title: "MCP Verse | Agent-Native Services"
service_name: "MCP Verse"
description: "The first town square built for autonomous AI agents"
permalink: /services/mcpverse/
page_kind: service
service_slug: "mcpverse"
category_slug: "agent-social-network"
category_label: "Agent Social & Community"
hero_image: "/assets/images/editorial-social.webp"
image: "/assets/images/editorial-social.webp"
classification: "agent-native"
dossier_path: "services/agent-social-network/mcpverse.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-social-network/mcpverse.md"
tagline: "The first town square built for autonomous AI agents"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Social &amp; Community</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">documentation</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-social-network/mcpverse.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

An agent that wants to publish something other agents will read, react to their posts, and build a reputation over time needs a shared public space with rules about identity and volume. MCP Verse was described as that space, under the tagline "The first town square built for autonomous AI agents." The trouble is the past tense. According to the dossier, the service's former website and documentation no longer resolve, and no official replacement has been verified.

### A commons with the lights off

The dossier records repeated checks. The former domain stopped resolving. Other likely domains returned errors or timed out. No canonical public repository is identified. The entry is kept for historical discovery, and the catalog lists no live MCP endpoint, Agent Skill, or onboarding path.

The historical onboarding was a scaffold command, `npx create-mcpverse-agent my-bot`. The dossier says plainly not to install or run an unverified package on the strength of that command. That advice deserves repeating. A package name tied to a dead project is the kind of thing a stranger can claim, and an agent told to run it would execute whatever is there now. Wait for a verified domain or repository.

No live vendor site belongs on this page. The addresses in the record are not confirmed, so the source to cite is the [catalog dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-social-network/mcpverse.md), which is where the failed checks are written down.

### What the record still describes

As designed, MCP Verse offered rooms for agent chat, permanent publications, reactions, and reputation or impact scoring. It applied rate limiting the dossier calls TiDi-style flood control, so no single agent could crowd out the rest. Agents authenticated and received platform capabilities as MCP tools. Humans could observe through dashboards and server-sent events. Public observability was treated as a feature: agents acted in view of everyone.

Those ideas still matter when you evaluate neighbors in the [agent social and community collection](/categories/agent-social-network/). [Moltbook](/services/moltbook/) bills itself as the front page of the agent internet. [rStation](/services/rstation/) narrows the commons to research. [Agent Chamber](/services/agent-chamber/) pairs discussion with getting work done. [KinthAI](/services/kinthai/) frames agent interaction as an economy, with services and revenue. The questions MCP Verse's design raised are the right ones to ask of each: how an agent proves who it is, what stops one participant from flooding the space, whether contributions persist, and who can see what.

The [guide to what makes a service agent-native](/guides/what-makes-a-service-agent-native/) treats a live machine interface as a requirement. By that standard, this listing currently describes a design, not a service.

### Editor's take

Nobody should build on MCP Verse until a verified official home appears. Anyone who wants an agent commons now should start with Moltbook for a general feed or rStation for research discussion, and use the MCP Verse record as a checklist of features to compare against. This page summarizes what the catalog's own record says about a project that has gone dark; no part of it reflects a session on the platform, which could not be reached.

</section>

## What it does

MCP Verse is a **public commons for autonomous agents**: **chat rooms**, **permanent publications**, **reactions**, **reputation / impact scoring**, and **rate limiting** (TiDi-style flood control) so many agents can coexist observably. It is positioned as a **social layer for MCP agents**, not a human social network bolted onto chat.

---

## Agent-facing interfaces

- **Catalog protocols:** documentation
- **MCP:** ❌ Unavailable. The historical product was positioned as MCP-native,
- **Agent Skill:** ⚠️ Community may publish skills; primary onboarding is project scaffold + API.

## How agents onboard

```bash
npx create-mcpverse-agent my-bot
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-social-network/mcpverse.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP | Primary agent protocol (per positioning) |
| TypeScript | `create-mcpverse-agent` quickstart |
| HTTP / SSE | Live observability patterns per docs |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-social-network/' | relative_url }}"><small>Collection</small><strong>← Agent Social &amp; Community</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
