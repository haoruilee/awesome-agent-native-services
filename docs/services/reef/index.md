---
title: "Reef | Agent-Native Services"
service_name: "Reef"
description: "Infrastructure for continually self-improving agents"
permalink: /services/reef/
page_kind: service
service_slug: "reef"
category_slug: "agent-harnesses-and-control-planes"
category_label: "Agent Harnesses & Operator Surfaces"
hero_image: "/assets/images/editorial-harness.webp"
image: "/assets/images/editorial-harness.webp"
classification: "agent-native"
dossier_path: "services/agent-harnesses-and-control-planes/reef.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/reef.md"
tagline: "Infrastructure for continually self-improving agents"
verified_at: "2026-10-27"
website: "https://reefinfra.ai"
repository: "https://github.com/Human-Agent-Society/reef"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Agent Harnesses &amp; Operator Surfaces</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-27</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://reefinfra.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://reefinfra.ai/docs/getting-started/quickstart/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Human-Agent-Society/reef" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/reef.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Reef connects **agent inference, feedback, learning, and versioned delivery**. Recipes can train model weights (e.g. with Slime/SGLang) or improve an agent's **harness** (prompts, rules, skills) without local training GPUs. Learning cycles: Serve → Observe → Grow → Commit, with version history for accepted updates.

---

## Agent-facing interfaces

- **Interaction pattern:** Local/self-hosted Python infra (CLI)
- **Catalog protocols:** CLI, http
- **MCP:** ⚠️ No MCP server in the verified materials — primary surface is the reef CLI / Python package (serve, train, evaluate, artifact delivery).
- **Agent Skill:** ⚠️ No official AgentSkills bundle located; integration is the reef-infra Python package and CLI.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** Local/self-hosted Python infra (CLI)

```bash
uv venv && source .venv/bin/activate
uv pip install reef-infra
python3 -c "import reef; print(reef.__version__)"
# minimal inference serve example from upstream README:
uv run reef serve --inference.model-path Qwen/Qwen2.5-1.5B-Instruct
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/agent-harnesses-and-control-planes/reef.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| PyPI | `uv pip install reef-infra` |
| CLI | `reef serve`, training/eval modules under the package |
| Docs | https://reefinfra.ai/docs/getting-started/quickstart/ |
| Source | https://github.com/Human-Agent-Society/reef |

---

## Verification

Last verified **2026-10-27**.

Sources:
- https://github.com/Human-Agent-Society/reef

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/agent-harnesses-and-control-planes/' | relative_url }}"><small>Collection</small><strong>← Agent Harnesses &amp; Operator Surfaces</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
