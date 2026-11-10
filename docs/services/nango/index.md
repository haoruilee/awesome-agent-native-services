---
title: "Nango | Agent-Native Services"
service_name: "Nango"
description: "The OAuth and API credential layer for AI agents"
permalink: /services/nango/
page_kind: service
service_slug: "nango"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/nango.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/nango.md"
tagline: "The OAuth and API credential layer for AI agents"
website: "https://nango.dev"
repository: "https://github.com/NangoHQ/nango"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://nango.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.nango.dev" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/NangoHQ/nango" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/nango.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

[Arcade](/services/arcade/) wraps OAuth inside MCP tools that it helps you build and host. Nango sits one layer lower. It is the credential store and refresh engine, and your agent code asks it for a valid token at the moment it needs to call a third-party API.

### Connections as the unit

The dossier's core object is a connection: one user's credentials for one external API. A Connect Session is the hosted OAuth consent flow that an agent can trigger mid-conversation, through `createConnectSession()`. After the user consents once, the agent calls `getConnection()` with an integration and user identifier and receives a current access token. Nango handles storage, automatic refresh, PKCE, token exchange, and revocation, so an agent in a long loop does not hit an expired-token error halfway through.

Connections multiply cleanly. Many users times many APIs gives an isolated matrix, which is why the dossier's use cases lean toward multi-tenant products where one agent deployment acts for many people. Auth observability rounds this out: logged authorization attempts, connection diagnostics, and detection of failing credentials. The number of supported APIs changes, and the current integration list belongs in the [Nango docs](https://docs.nango.dev).

### SDK, REST, MCP, and one skill

The Node.js SDK is `@nangohq/node`, which carries both methods above. A REST API covers connection management and credential retrieval. There is a first-class integration guide for the OpenAI Agents SDK.

Nango also exposes a built-in MCP server over stdio or HTTP, and an `mcp-generic` integration that the dossier says works with any OAuth 2.0 service through dynamic discovery. The official skill installs with `npx skills add NangoHQ/sync-builder-skill`. Note what it teaches: building Nango syncs for continuous data synchronization. That is a different job from runtime token retrieval, so do not expect the skill to cover the `getConnection()` path.

### Token handling questions

The [Tool Access & Integration](/categories/tool-access-and-integration/) category has two broad answers to agent credentials. In Nango's model, the token is returned to your code and your code makes the API call. The dossier says credentials never appear in agent code or logs, meaning nothing is hardcoded, but at call time the token is in your process, and keeping it out of the model's context is your job. Arcade's stated model keeps secrets and tokens out of the LLM context entirely. [MCP Toolbox for Databases](/services/google-mcp-toolbox/) handles a third case, database credentials, with operator-configured access instead of per-user OAuth. The [MCP servers guide](/guides/getting-started-with-mcp-servers/) covers where each fits in a client setup.

In the vendor docs, check whether you are using Nango's cloud or running the open-source repository yourself, since that decides who holds the stored tokens. Check how scopes are configured per integration, what your agent sees when a user revokes access, and how long authorization logs are retained.

### Editor's take

Nango is a strong fit for a SaaS product whose agent acts for many users across many third-party APIs, written by developers comfortable making the HTTP calls themselves. Teams that would rather ship hosted MCP tools with auth already inside should compare Arcade first. Treat this as an interpretation of the catalog dossier and the public docs, not a field report; no connection was created while writing it.

</section>

## What it does

Nango manages OAuth authentication and credential lifecycle for 700+ external APIs so AI agents can access third-party services without ever handling tokens directly. Agents call `getConnection()` at runtime to receive a valid access token; Nango handles token storage, automatic refresh, and credential validation invisibly.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skills published by NangoHQ on the AgentSkills marketplace
- **Onboarding type:** `other`

## Protocol surface

| Interface | Detail |
|---|---|
| Node.js SDK | `@nangohq/node` — `getConnection()`, `createConnectSession()` |
| REST API | Full connection management and credential retrieval |
| OpenAI Agents SDK | First-class integration guide and example |
| MCP-compatible | Patterns work with MCP-based agent frameworks |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
