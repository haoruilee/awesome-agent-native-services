---
title: "Agent Sandbox | Agent-Native Services"
service_name: "Agent Sandbox"
description: "The trusted runtime for untrusted code"
permalink: /services/agent-sandbox/
page_kind: service
service_slug: "agent-sandbox"
category_slug: "code-execution"
category_label: "Code Execution"
hero_image: "/assets/images/editorial-sandbox.webp"
image: "/assets/images/editorial-sandbox.webp"
classification: "agent-native"
dossier_path: "services/code-execution/agent-sandbox.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-sandbox.md"
tagline: "The trusted runtime for untrusted code"
website: "https://agentsandbox.co"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Code Execution</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentsandbox.co" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://agentsandbox.co/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-sandbox.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

<section class="service-essay" aria-label="Editorial" markdown="1">

[E2B](/services/e2b/) and Agent Sandbox both give an agent somewhere to run code that nobody reviewed line by line. The difference is emphasis. E2B's dossier leads with stateful execution contexts and output streamed back in real time. Agent Sandbox leads with files: get inputs in, run Python or shell against them, and get outputs back out, all through one API.

### Sessions, manifests, and artifacts

The dossier describes a managed, isolated runtime where an agent executes Python and shell commands, installs dependencies, and exchanges files. The vendor frames this as giving each agent a personal remote computer and drive. Three primitives carry that idea. A sandbox session is the isolated runtime itself. A dependency manifest installs packages per run, so the same job can be repeated with the same environment. The artifacts pipeline covers the upload, process, retrieve cycle that most code-interpreter tools end up rebuilding by hand.

The tagline, "The trusted runtime for untrusted code," states the purpose. The dossier does not say what makes the runtime trusted. It names no isolation technology, no VM or container boundary, and no network policy.

### Three ways in, no MCP

An agent can start from URL onboarding by reading `https://agentsandbox.co/skill.md`, which the dossier says teaches authentication, session creation, code execution, and file handling. Developers can call the REST API described in the [Agent Sandbox docs](https://agentsandbox.co/docs) or install the Python SDK with `pip install agentsandbox-sdk`.

There is no official MCP server as of the dossier's April 2026 check. An MCP-only client needs a thin wrapper of its own, or a runtime that can make HTTPS calls directly.

Identity is an API key. The operator decides which agent holds a key and what budget comes with it, and session and artifact operations are attributed to that key. A dashboard offers optional monitoring; nothing in the execution loop waits on a human click.

### Placement among sandboxes

Within [Code Execution](/categories/code-execution/), [Vercel Sandbox](/services/vercel-sandbox/) describes isolated microVMs, which is a specific claim about the boundary. [CodeRunner](/services/coderunner/) runs locally, and [OpenSandbox](/services/opensandbox/) is a runtime you can operate yourself. Agent Sandbox is hosted by the vendor, and the dossier mentions no self-hosted option. The [sandboxes guide](/guides/sandboxes-and-code-execution/) covers the isolation and leftover-state questions that apply here.

Before depending on it, check four things in the vendor docs: what separates one session from another, how long a session and its files persist, whether code inside can reach the network, and whether keys can be scoped per agent or only per account. Current pricing, limits, and startup timing belong on the vendor's pages, not this one.

### Editor's take

Agent Sandbox fits a Python-first agent whose work is file transformation: a CSV in, a chart or report out. The skill file and SDK make that path short. Teams that want a stateful interpreter whose variables persist between code blocks, with output streamed as it runs, should start with E2B. Teams that cannot send code off their own machines should look at CodeRunner or OpenSandbox. This assessment comes from the catalog dossier and the vendor's public pages; nobody on this project has run workloads on Agent Sandbox.

</section>

## What it does

Agent Sandbox provides a managed, isolated runtime where AI agents can execute Python and shell commands, install dependencies, and exchange files through a single API. The product is positioned around giving each agent a personal remote computer and drive, with explicit support for sessioned execution and artifact pipelines.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, Agent Skill, REST, SDK, http, API
- **MCP:** ⚠️ Not yet published as a dedicated official MCP server (as of April 15, 2026).
- **Agent Skill:** ✅ Available (URL onboarding at https://agentsandbox.co/skill.md)
- **Onboarding type:** `url`

## How agents onboard

```text
https://agentsandbox.co/skill.md
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/code-execution/agent-sandbox.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | https://agentsandbox.co/docs |
| Python SDK | `pip install agentsandbox-sdk` |
| URL Onboarding | `https://agentsandbox.co/skill.md` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/code-execution/' | relative_url }}"><small>Collection</small><strong>← Code Execution</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
