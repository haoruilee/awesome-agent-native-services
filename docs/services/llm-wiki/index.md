---
title: "LLM Wiki | Agent-Native Services"
service_name: "LLM Wiki"
description: "LLM-compiled knowledge bases for any AI agent"
permalink: /services/llm-wiki/
page_kind: service
service_slug: "llm-wiki"
category_slug: "memory-and-state"
category_label: "Memory & State"
hero_image: "/assets/images/editorial-memory.webp"
image: "/assets/images/editorial-memory.webp"
classification: "agent-native"
dossier_path: "services/memory-and-state/llm-wiki.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/llm-wiki.md"
tagline: "LLM-compiled knowledge bases for any AI agent"
website: "https://llm-wiki.net"
repository: "https://github.com/nvk/llm-wiki"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Memory &amp; State</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://llm-wiki.net" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://llm-wiki.net/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/nvk/llm-wiki" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/llm-wiki.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

LLM Wiki builds a compounding, cross-session knowledge base for agents: parallel research, source ingestion, synthesis into wiki articles, deep query over accumulated content, and output generation (reports/slides/plans). The knowledge base is durable and grows with each run.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill
- **MCP:** ⚠️ No standalone first-party MCP server as the primary interface.
- **Agent Skill:** ✅ The repository ships agent-native instruction surfaces (Claude plugin skill tree + portable AGENTS.md).
- **Onboarding type:** `other`

## How agents onboard

```bash
claude plugin install wiki@llm-wiki
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/memory-and-state/llm-wiki.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Claude plugin | `claude plugin install wiki@llm-wiki` |
| Codex plugin | Clone repo, then install from `.agents/plugins/marketplace.json` in Codex `/plugins` |
| OpenCode instruction file | `plugins/llm-wiki-opencode/skills/wiki-manager/SKILL.md` |
| Portable protocol | `AGENTS.md` copied into agent context |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/memory-and-state/' | relative_url }}"><small>Collection</small><strong>← Memory &amp; State</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
