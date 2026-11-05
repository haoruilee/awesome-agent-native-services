---
title: "CLI-Anything | Agent-Native Services"
service_name: "CLI-Anything"
description: "CLI-Anything: Making ALL Software Agent-Native"
permalink: /services/cli-anything/
page_kind: service
service_slug: "cli-anything"
category_slug: "tool-access-and-integration"
category_label: "Tool Access & Integration"
hero_image: "/assets/images/editorial-tools.webp"
image: "/assets/images/editorial-tools.webp"
classification: "agent-native"
dossier_path: "services/tool-access-and-integration/cli-anything.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/cli-anything.md"
tagline: "CLI-Anything: Making ALL Software Agent-Native"
website: "https://clianything.cc"
repository: "https://github.com/HKUDS/CLI-Anything"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Tool Access &amp; Integration</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://clianything.cc" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/HKUDS/CLI-Anything/blob/main/cli-anything-plugin/HARNESS.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/HKUDS/CLI-Anything" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/cli-anything.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

CLI-Anything turns existing software (GUI applications, codebases and web APIs) into **agent-operable CLI harnesses**. A coding agent follows the project's seven-phase **HARNESS.md** procedure to analyze the target, map GUI actions to its real backend, and generate a stateful CLI with a REPL mode and subcommands. Every generated command supports `--json`. **CLI-Hub** is a registry where community-built CLIs can be searched and installed with one command.

---

## Agent-facing interfaces

- **Interaction pattern:** Agent Skill + Structured CLI (--json) + registry
- **Catalog protocols:** Agent Skill, MCP, CLI, http
- **MCP:** ⚠️ Not the primary surface — CLI-Anything targets shell-capable agents through generated CLIs and Skills.
- **Agent Skill:** ✅ Available
- **Onboarding type:** `agent-skill`

## How agents onboard

**Interaction pattern:** Agent Skill + Structured CLI (--json) + registry

```bash
# Let the agent find and install CLIs from CLI-Hub
npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y
# then prompt: "Find appropriate CLI software in CLI-Hub and complete the task: ..."

# Or manage CLIs yourself
pip install cli-anything-hub
cli-hub search <keyword>
cli-hub install <name>
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/tool-access-and-integration/cli-anything.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **CLI** | Generated `cli-anything-*` CLIs with REPL + subcommands and `--json` |
| **Registry** | `cli-hub` (PyPI `cli-anything-hub`) and https://clianything.cc |
| **Skill** | `cli-hub-meta-skill`, CLI-Anything plugin |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/tool-access-and-integration/' | relative_url }}"><small>Collection</small><strong>← Tool Access &amp; Integration</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
