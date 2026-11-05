---
title: "Tracekit | Agent-Native Services"
service_name: "Tracekit"
description: "Let your agents act. Prove every action"
permalink: /services/tracekit/
page_kind: service
service_slug: "tracekit"
category_slug: "oversight-and-approval"
category_label: "Oversight & Approval"
hero_image: "/assets/images/editorial-oversight.webp"
image: "/assets/images/editorial-oversight.webp"
classification: "agent-native"
dossier_path: "services/oversight-and-approval/tracekit.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/tracekit.md"
tagline: "Let your agents act. Prove every action"
website: "https://tracekit.tech"
repository: "https://github.com/Cygnux-Labs/Tracekit"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Oversight &amp; Approval</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">Status</span><span class="service-page__chip-value">Self-hosted software: a stable core, with the other surfaces marked experimental (what&#x27;s stable)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · SDK · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://tracekit.tech" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/Cygnux-Labs/Tracekit/wiki" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Cygnux-Labs/Tracekit" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/tracekit.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Tracekit checks every tool call an agent makes before it runs, signs each call and decision into a hash chain, and exports one `.tkb` file per run that anyone can verify offline. The policy answers allow, deny or ask. A denied call goes back to the model as a refusal and the agent carries on; an asked call waits until a person approves it, and the approval covers those exact arguments and works once.

The signer is a separate process the agent reaches over a Unix socket, loopback TCP or HTTPS. The agent holds a run token, never a signing key, and never assigns sequence numbers. The record is tamper-evident: an edited, deleted, swapped or inserted record fails verification at that record. Cutting off the end of the log, or re-signing it with a stolen key, takes an independent witness (experimental) to catch.

Limits, from the project's own docs: in dev mode the signer runs as the agent's own user, so the agent could read the key and rewrite the store; the guarantee needs the signer under another user, in a container or on another host. A verified run proves the record is intact, not intent, not that a reported tool result is true, and not that every action was captured. Calls that skip the SDK, hook or gateway aren't decided or recorded, and policy rules match text and tool names, so a determined agent can reword a command ([limits](https://github.com/Cygnux-Labs/Tracekit/wiki/Limits)).

---

## Agent-facing interfaces

- **Interaction pattern:** SDK (Python or TypeScript) that asks a signer you run before each tool call
- **Catalog protocols:** MCP, CLI, SDK, http
- **MCP:** ✅ Available: an MCP gateway in front of your MCP servers (experimental)
- **Agent Skill:** ⚠️ Not yet published as a standalone SKILL.md package
- **Onboarding type:** `sdk`

## How agents onboard

**Interaction pattern:** SDK (Python or TypeScript) that asks a signer you run before each tool call

```bash
pip install tracekit-ai   # then make "import tracekit; tracekit.instrument()" the agent's first line and run it
tracekit last             # export the latest run and verify it offline
tracekit approvals list   # calls held for a person; answer with: tracekit approvals approve ID
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/oversight-and-approval/tracekit.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **Python SDK** | `pip install tracekit-ai`; `tracekit.instrument()` or `RunHandle`; Python 3.9 to 3.13 (framework integrations need 3.10 or newer) |
| **TypeScript SDK** | `npm install @cygnuxlabs/tracekit` (experimental); speaks the signer RPC itself; Node 18 or newer |
| **Framework integrations** | Stable: OpenAI Agents SDK, LangChain / LangGraph, Claude Agent SDK, MCP client. Experimental: CrewAI, Browser Use, Pydantic AI, Google ADK, Haystack, LlamaIndex, Microsoft Agent Framework, Strands Agents, Vercel AI SDK |
| **Coding-agent hooks** | Claude Code (stable); Codex CLI, Cursor, Gemini CLI and OpenCode (experimental), wired by `tracekit init --dev --v2` |
| **MCP gateway** | `tracekit mcp-gateway serve` (experimental): Streamable HTTP for agents; decides each tool call in the signer |
| **Signer RPC** | A versioned request and response contract over a Unix socket, loopback TCP with a token, or HTTPS (experimental) |
| **CLI** | `tracekit approvals list / show / approve / reject`, `tracekit export --v2`, `tracekit verify`, `tracekit view` |
| **Bundle format** | `.tkb`, evidence format v2; verifiers in Python and TypeScript |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/oversight-and-approval/' | relative_url }}"><small>Collection</small><strong>← Oversight &amp; Approval</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
