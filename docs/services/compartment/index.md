---
title: "Compartment | Agent-Native Services"
service_name: "Compartment"
description: "Encrypted, fully offline memory for AI agents"
permalink: /services/compartment/
page_kind: service
service_slug: "compartment"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/compartment.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/compartment.md"
tagline: "Encrypted, fully offline memory for AI agents"
verified_at: "2026-10-19"
website: "https://maxfreedompollard.github.io/Compartment/"
repository: "https://github.com/MaxFreedomPollard/Compartment"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · STDIO</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://maxfreedompollard.github.io/Compartment/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/MaxFreedomPollard/Compartment#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/MaxFreedomPollard/Compartment" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/compartment.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Compartment is an **encrypted, fully offline** memory vault for AI agents. Official docs: one claim per memory (hard 200-character / no-list rule), required `source` + `discovered` date, optional `expires`, opinions that supersede rather than duplicate, hybrid vector+keyword recall (~12 ms) over an in-memory index, and a hash-chained audit log. Embeddings are a bundled ONNX model; **no LLM inside**, **CI-enforced no network**. Vectors are encrypted at rest; only the passphrase opens the vault.

A new vault includes ~6,700 reference facts (toggle-able). Capture does not depend on the model calling a tool: the Claude hook writes memory files even if the host’s system prompt overrides tool instructions.

Distinct from [Claude-Mem](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/claude-mem.md) / [agentmemory](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/agentmemory.md): Compartment’s differentiator is **offline + encryption + one-claim discipline**, not session compression or a shared unencrypted server.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + MCP (compartment serve)
- **Catalog protocols:** Agent Skill, MCP, CLI, STDIO
- **MCP:** ✅ Available — this is the agent surface
- **Agent Skill:** ✅ /compartmentalize installed by integrate claude|hermes|openclaw (not npx skills add)
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + MCP (compartment serve)

```bash
pip install compartment && compartment init
compartment integrate claude      # also: hermes, openclaw, or --all
# MCP clients without a recipe:
# { "mcpServers": { "compartment": { "command": "compartment", "args": ["serve"] } } }
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/compartment.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `compartment init`, `serve`, `integrate`, `unlock`/`lock`, `audit verify` |
| MCP | `compartment serve` (stdio) |
| Plugin | Claude Code / Codex marketplace |
| GUI / dashboard | Secondary; 127.0.0.1 read-only map |
| Packs | `compartment pack` / `setup airgap-bundle` |

---

## Verification

Last verified **2026-10-19**.

Sources:
- https://api.github.com/repos/MaxFreedomPollard/Compartment

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
