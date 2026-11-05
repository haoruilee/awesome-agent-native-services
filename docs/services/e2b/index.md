---
title: "E2B | Agent-Native Services"
service_name: "E2B"
description: "Cloud for AI agents — secure sandboxes for AI-generated code"
permalink: /services/e2b/
page_kind: service
service_slug: "e2b"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/e2b.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/e2b.md"
tagline: "Cloud for AI agents — secure sandboxes for AI-generated code"
website: "https://e2b.dev"
repository: "https://github.com/e2b-dev/e2b"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · REST · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://e2b.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://e2b.dev/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/e2b-dev/e2b" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/e2b.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

E2B provides secure, isolated Linux cloud sandboxes that AI agents can spin up in ~150ms to execute generated code. Each agent session gets its own sandbox with a full Linux filesystem, internet connectivity, and stateful execution contexts. Agents can run Python, JavaScript, shell commands, and more — with stdout, stderr, charts, and files streamed back in real time.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, REST, SDK, API
- **MCP:** ✅ Available — and uniquely, E2B *runs MCP servers inside sandboxes*
- **Agent Skill:** ✅ Official and community skills available via ClawHub and LobeHub
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `from e2b_code_interpreter import Sandbox` |
| TypeScript SDK | `import { Sandbox } from "@e2b/code-interpreter"` |
| REST API | Sandbox lifecycle management and code execution |
| LangChain | Native tool integration |
| AutoGen | Compatible with AutoGen's code execution model |
| CrewAI | Compatible with CrewAI tool definitions |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
