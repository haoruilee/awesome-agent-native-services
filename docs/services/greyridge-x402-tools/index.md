---
title: "Grey Ridge x402 Tools | Agent-Native Services"
service_name: "Grey Ridge x402 Tools"
description: "Vet an MCP server before your agent trusts it"
permalink: /services/greyridge-x402-tools/
page_kind: service
service_slug: "greyridge-x402-tools"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/greyridge-x402-tools.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/greyridge-x402-tools.md"
tagline: "Vet an MCP server before your agent trusts it"
website: "https://x402-data-api.sigrunner.workers.dev/"
repository: "https://github.com/rezearcher/greyridge-x402-tools"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · CLI · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://x402-data-api.sigrunner.workers.dev/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/rezearcher/greyridge-x402-tools" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/rezearcher/greyridge-x402-tools" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/greyridge-x402-tools.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Grey Ridge x402 Tools gives an autonomous agent two preflight gates it can call on its own before it takes an irreversible action.

The first is **mcpscan**: every tool an MCP server advertises runs inside the agent's context — its name, description and JSON schema are read by the model — so a poisoned or injection-laden tool description can steer the agent before any tool is ever invoked. `mcpscan` statically scans a server's advertised tools for prompt-injection and tool-poisoning patterns (OWASP LLM01 / LLM08), returns a clear/review/block verdict, and is usable as a CI admission gate or an in-loop check.

The second is a **pre-trade token gate** for agents acting on Base: given a token address, it runs a live `eth_call` state-override transfer simulation (can a synthetic wallet actually sell the token?) plus a proxy/mint/pause/blacklist/fee-setter selector scan and an owner-renounce check, and returns `allow` / `review` / `block`. Both gates expose a free, keyless preview and a paid itemized endpoint settled per call in USDC over x402 on Base — no account and no API key.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, CLI, API
- **MCP:** ✅ MCP-aware scanner, plus a hosted MCP server entry.
- **Agent Skill:** ✅ Available
- **Onboarding type:** `mcp`

## How agents onboard

```bash
# Keyless CLI, no install — scan any MCP server's advertised tools before trusting them.
# (the package ships multiple bins, so -p selects mcpscan)
npx -y -p github:rezearcher/greyridge-x402-tools#v0.3.0 mcpscan https://mcp.deepwiki.com/mcp

# Coding-time Skill / Claude Code plugin:
/plugin marketplace add rezearcher/greyridge-x402-tools
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/greyridge-x402-tools.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `npx -y -p github:rezearcher/greyridge-x402-tools#v0.3.0 mcpscan <mcp-url>` — keyless, fails closed |
| GitHub Action | `uses: rezearcher/greyridge-x402-tools@v0.3.0` — admission gate on every push |
| REST API | `GET /scan/mcp`, `GET /scan/mcp/preview?url=`, `GET /gate/swap`, `GET /gate/swap/preview?token=` |
| Framework adapters | LangChain, CrewAI, ElizaOS (`CHECK_BASE_TOKEN`) |
| Payments | x402 / USDC on Base, inline per call |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
